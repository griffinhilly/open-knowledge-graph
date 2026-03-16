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

## Explainer

From your understanding of BGP, you know that autonomous systems (ASes) exchange reachability information by announcing the IP prefixes they can route to, and that BGP routers select the best path based on attributes like AS-PATH length and local preference. What BGP fundamentally lacks, however, is any built-in mechanism to verify that an AS actually has the right to announce a given prefix. If AS 64500 announces that it can route traffic for 198.51.100.0/24, BGP peers have no native way to confirm whether AS 64500 legitimately owns that address block. This trust-by-default design is the root of the **route hijacking** problem.

A **route hijack** occurs when an AS announces a prefix it does not own, either maliciously or by misconfiguration. Neighboring ASes accept the announcement, propagate it further, and traffic destined for the legitimate owner gets redirected to the hijacker. A particularly effective variant is announcing a more-specific prefix — if the legitimate owner announces 198.51.100.0/24, the hijacker announces 198.51.100.0/25 and 198.51.100.128/25. Because routers prefer the longest matching prefix, traffic follows the hijacker's more-specific routes. Real-world incidents have redirected traffic for major services, financial institutions, and even government networks, sometimes for hours before detection.

The first line of defense is **route filtering**: explicitly configuring which prefixes you will accept from each BGP peer and which you will announce. **Prefix lists** define the exact address blocks a peer is authorized to send you — anything not on the list is rejected. **AS-PATH filters** verify that the AS path in an announcement matches expected patterns; for example, you might only accept routes from a customer AS if that customer's AS number appears in the path. The cardinal rule is **default-deny**: reject everything not explicitly permitted. Operators who accept all routes by default are one misconfiguration away from propagating a hijack across the internet.

**RPKI (Resource Public Key Infrastructure)** adds cryptographic verification to this process. Regional Internet Registries (RIRs) issue digital certificates called **Route Origin Authorizations (ROAs)** that bind an IP prefix to the AS number authorized to originate it. When a BGP router receives an announcement, it can validate the origin AS against the ROA database. If the announcement's origin AS does not match any valid ROA, the route is marked as "invalid" and can be rejected or deprioritized. RPKI does not prevent all forms of hijacking — it validates origin but not the full path — but it addresses the most common scenario of unauthorized prefix origination. Combined with disciplined filtering, BGP monitoring services, and community coordination, RPKI moves BGP security from pure trust toward cryptographic verification, closing the most dangerous gap in the internet's routing infrastructure.
