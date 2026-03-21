---
id: bgp-route-filtering-hijacking-prevention
title: BGP Route Filtering and Hijacking Prevention
domain: computer-science
course: computer-networking
prerequisites:
- id: bgp-border-gateway-protocol
  type: hard
- id: network-security-fundamentals
  type: hard
builds-toward:
- network-security-fundamentals
- network-standards-and-ietf
tags:
- routing
- bgp
- security
- hijacking
stage: advanced
status: draft
---

# BGP Route Filtering and Hijacking Prevention

## Core Idea
BGP route hijacking occurs when unauthorized ASes announce prefixes they do not own or should not announce. Prevention mechanisms include route filtering (accepting only authorized prefixes from peers), prefix lists, AS-PATH filtering, and RPKI (Resource Public Key Infrastructure). Inbound and outbound filters enforce routing policies and prevent propagation of invalid routes.

## How It's Best Learned
Configure inbound route filters on a BGP router using prefix lists and AS-PATH filters. Simulate a route hijack by announcing a legitimate prefix from an unauthorized AS. Deploy RPKI validation and observe its effect on route acceptance. Monitor BGP RIB (Routing Information Base) changes.

## Common Misconceptions
BGP does not verify that an AS owns a prefix; it relies on filtering and RPKI. AS-PATH filtering is not foolproof against path manipulation. Default-deny filtering is essential; permitting all routes by default opens the network to hijacking.

## Questions

```yaml
- question: "A legitimate network operator owns the prefix 203.0.113.0/24 and announces it to their BGP peers. A malicious AS begins announcing 203.0.113.0/25 and 203.0.113.128/25. Even if neighboring ASes have a prefix list allowing 203.0.113.0/24, what happens to traffic destined for addresses in that block?"
  type: multiple-choice
  options:
    - "Traffic is unaffected because the prefix list blocks the more-specific announcements from propagating"
    - "Traffic follows the hijacker's more-specific /25 routes because routers prefer the longest matching prefix"
    - "Traffic is dropped because the conflicting announcements trigger BGP loop detection"
    - "Traffic splits evenly between the legitimate owner and the hijacker using ECMP load balancing"
  answer: 1
  explanation: "BGP routers always prefer the most specific (longest prefix) matching route. A /25 prefix is more specific than a /24 for addresses in the same range, so any router that has both routes in its table will forward traffic toward the /25 — the hijacker. A prefix list that explicitly permits 203.0.113.0/24 will block those exact routes from neighbors, but it does NOT automatically block the more-specific /25 sub-prefixes unless the filter is written to cover them. This is why more-specific prefix hijacking is so effective: it exploits the fundamental routing preference without requiring any forgery of the legitimate route itself."

- question: "What does RPKI (Resource Public Key Infrastructure) validate when a BGP router checks an incoming route announcement, and what form of hijacking does it NOT prevent?"
  type: multiple-choice
  options:
    - "RPKI validates the entire AS-PATH of an announcement and prevents all forms of route hijacking"
    - "RPKI validates that the origin AS is authorized to announce the prefix, but does not verify the intermediate AS-PATH"
    - "RPKI validates the BGP community attributes attached to a route, preventing traffic engineering manipulation"
    - "RPKI validates that the announced prefix exists in the global routing table at the time of announcement"
  answer: 1
  explanation: "RPKI uses Route Origin Authorizations (ROAs) — cryptographic certificates issued by Regional Internet Registries — to verify that the origin AS (the AS that first announces a prefix) is legitimately authorized to do so. This closes the most common gap: an AS announcing a prefix it doesn't own. However, RPKI says nothing about the intermediate ASes in the path. Path manipulation attacks — where an AS fabricates or prepends ASes in the AS-PATH — are not addressed by RPKI alone. Additional mechanisms like BGPsec are needed for full path validation."

- question: "RPKI validates that a BGP announcement's origin AS matches a signed authorization, which means RPKI alone is sufficient to prevent all BGP route hijacking attacks."
  type: true-false
  answer: false
  explanation: "RPKI validates origin AS only, not the full AS path. A hijacker who announces a prefix from an authorized origin AS (e.g., by forging or prepending the real origin AS at the start of a fabricated path) would pass RPKI validation. Path manipulation attacks, where an attacker manipulates the AS-PATH to redirect traffic while still showing a valid origin, require BGPsec for full cryptographic path validation. RPKI is a significant improvement over unverified BGP, but it is not a complete solution."

- question: "A BGP router that is configured with a 'default-deny' inbound filter will reject any prefix announcement not explicitly included in its prefix list, even from trusted peers."
  type: true-false
  answer: true
  explanation: "Default-deny is the correct and security-critical posture for BGP filtering. Without it, a misconfiguration or malicious announcement from any peer — including a trusted one — can propagate through your router to the broader internet. Many of the most damaging real-world BGP incidents have involved routers that accepted all routes by default and then accidentally propagated a hijacked or leaked route to thousands of downstream networks. Explicit permit lists ensure that only authorized prefixes, in expected size ranges, from authorized peers, are accepted and re-advertised."

- question: "BGP has no built-in mechanism to verify that an AS owns the prefix it is announcing. What are the two main layers of defense against prefix hijacking, and what does each one address?"
  type: short-answer
  answer: "The first layer is route filtering — prefix lists and AS-PATH filters configured on each BGP session that explicitly allow only expected prefixes from each peer. This prevents unauthorized prefixes from propagating and enforces a default-deny posture. The second layer is RPKI, which adds cryptographic verification by allowing routers to check announced prefixes against signed Route Origin Authorizations (ROAs). RPKI addresses the root problem — that BGP trusts all announcements equally — by binding prefixes to authorized origin ASes with cryptographic proof. Together, filtering handles what is expected while RPKI provides cryptographic verification of what is legitimate."
  explanation: "Neither layer alone is sufficient. Filtering without RPKI still relies on operators manually maintaining accurate prefix lists — error-prone at internet scale. RPKI without filtering still requires router operators to act on invalid-marked routes (many currently only flag rather than reject them). The combination, along with BGP monitoring services and community coordination, forms the practical defense in depth used by security-conscious network operators."
```

## Explainer

From your understanding of BGP, you know that autonomous systems (ASes) exchange reachability information by announcing the IP prefixes they can route to, and that BGP routers select the best path based on attributes like AS-PATH length and local preference. What BGP fundamentally lacks, however, is any built-in mechanism to verify that an AS actually has the right to announce a given prefix. If AS 64500 announces that it can route traffic for 198.51.100.0/24, BGP peers have no native way to confirm whether AS 64500 legitimately owns that address block. This trust-by-default design is the root of the **route hijacking** problem.

A **route hijack** occurs when an AS announces a prefix it does not own, either maliciously or by misconfiguration. Neighboring ASes accept the announcement, propagate it further, and traffic destined for the legitimate owner gets redirected to the hijacker. A particularly effective variant is announcing a more-specific prefix — if the legitimate owner announces 198.51.100.0/24, the hijacker announces 198.51.100.0/25 and 198.51.100.128/25. Because routers prefer the longest matching prefix, traffic follows the hijacker's more-specific routes. Real-world incidents have redirected traffic for major services, financial institutions, and even government networks, sometimes for hours before detection.

The first line of defense is **route filtering**: explicitly configuring which prefixes you will accept from each BGP peer and which you will announce. **Prefix lists** define the exact address blocks a peer is authorized to send you — anything not on the list is rejected. **AS-PATH filters** verify that the AS path in an announcement matches expected patterns; for example, you might only accept routes from a customer AS if that customer's AS number appears in the path. The cardinal rule is **default-deny**: reject everything not explicitly permitted. Operators who accept all routes by default are one misconfiguration away from propagating a hijack across the internet.

**RPKI (Resource Public Key Infrastructure)** adds cryptographic verification to this process. Regional Internet Registries (RIRs) issue digital certificates called **Route Origin Authorizations (ROAs)** that bind an IP prefix to the AS number authorized to originate it. When a BGP router receives an announcement, it can validate the origin AS against the ROA database. If the announcement's origin AS does not match any valid ROA, the route is marked as "invalid" and can be rejected or deprioritized. RPKI does not prevent all forms of hijacking — it validates origin but not the full path — but it addresses the most common scenario of unauthorized prefix origination. Combined with disciplined filtering, BGP monitoring services, and community coordination, RPKI moves BGP security from pure trust toward cryptographic verification, closing the most dangerous gap in the internet's routing infrastructure.
