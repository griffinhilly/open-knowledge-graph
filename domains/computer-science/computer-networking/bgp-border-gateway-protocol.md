---
id: bgp-border-gateway-protocol
title: 'BGP: Border Gateway Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: ospf-open-shortest-path-first
  type: soft
tags:
- bgp
- egp
- exterior-gateway-protocol
- autonomous-system
- path-vector
stage: advanced
status: draft
---

# BGP: Border Gateway Protocol

## Core Idea
BGP is the exterior gateway protocol used to route traffic between autonomous systems (AS) on the Internet. Unlike OSPF, BGP uses path-vector routing where routers announce the full AS path to each destination, allowing policies (e.g., business relationships, traffic engineering) to influence route selection, not just hop count.

## Questions

```yaml
- question: "AS 100 (a small ISP) has two routes to a destination: one through its provider AS 200 (2 hops, fast link) and one through a paying customer AS 300 (4 hops, slower link). Which route will AS 100 most likely prefer under standard BGP routing policy?"
  type: multiple-choice
  options:
    - "The route through AS 200, because BGP prefers paths with fewer AS hops"
    - "The route through AS 200, because BGP selects for lowest physical latency"
    - "The route through AS 300, because AS 100 earns revenue for carrying customer traffic and sets higher local preference for customer routes"
    - "Whichever route has the lower BGP MED (multi-exit discriminator) value"
  answer: 2
  explanation: "BGP's highest-priority decision criterion is local preference, which is set by the operator to reflect business relationships — not path length or latency. Customer routes are preferred because the customer pays AS 100 for transit; provider routes are least preferred because AS 100 pays the provider. AS path length (option 0) and physical performance (option 1) are lower-priority criteria in BGP's decision algorithm. This is the fundamental distinction from interior protocols: BGP routing is a business decision, not a technical optimization."

- question: "What is the primary technical purpose of BGP's path-vector mechanism — advertising the full list of AS numbers in each route announcement?"
  type: multiple-choice
  options:
    - "To allow receiving routers to calculate the total end-to-end latency of each path"
    - "To prevent routing loops by enabling routers to reject routes that already contain their own AS number"
    - "To compress route update messages so they consume less bandwidth than link-state flooding"
    - "To provide a path quality metric equivalent to OSPF's link-state cost calculation"
  answer: 1
  explanation: "The full AS path serves two purposes: loop prevention (if a router sees its own AS number already in the path, it rejects the route — it would be routing back to itself) and policy input (the path list is available for operators to make business-based decisions). BGP has no knowledge of link latency or performance (option 0), its updates are not compressed path representations (option 2), and it deliberately does not use a cost metric like OSPF (option 3). Loop prevention is the technical necessity; policy expressiveness is the operational value."

- question: "BGP always selects the route with the fewest AS hops to any given destination."
  type: true-false
  answer: false
  explanation: "AS path length is only one criterion in BGP's multi-step decision algorithm, and it ranks below local preference. Because local preference reflects business relationships — customer routes are preferred over peer routes, which are preferred over provider routes — an operator will routinely select a longer AS path to a customer destination over a shorter path through a provider. 'Shortest path' is the OSPF paradigm; BGP's paradigm is 'policy-optimal path,' which may be quite long. Operators regularly add artificial AS path prepending to make their own routes appear longer and influence other ASes' routing decisions."

- question: "A single misconfigured BGP route announcement by one autonomous system can redirect or blackhole traffic for millions of Internet users globally."
  type: true-false
  answer: true
  explanation: "Because BGP glues together every AS on the Internet and route announcements propagate globally, a single AS incorrectly announcing ownership of a prefix (BGP hijacking) or advertising an overly specific route can redirect enormous volumes of traffic. A well-known example: in 2008, Pakistan Telecom accidentally advertised a more-specific route for YouTube's prefix, redirecting YouTube's global traffic through Pakistan and effectively taking YouTube offline worldwide for about two hours. BGP's trust model — routers accept advertised routes by default — makes this a persistent security vulnerability."

- question: "Explain why BGP uses policy-based routing rather than shortest-path routing, and give a concrete example of how business relationships shape routing decisions."
  type: short-answer
  answer: "BGP connects independently operated autonomous systems with competing commercial interests — it is not a single cooperative network with a shared optimization goal. Shortest-path routing ignores whether carrying traffic is profitable or costly. The concrete mechanism is local preference: an ISP sets higher local preference for routes learned from paying customers than for routes through providers (where it pays for transit) or peers (free exchange). Even if the customer path is longer and slower, the ISP will route through it because it generates revenue. This means Internet traffic often takes economically optimal paths rather than technically optimal ones."
  explanation: "The three main relationship types — customer-provider, peer-peer, and transit — each generate different financial obligations that local preference encodes. 'Prefer customer > peer > provider' is the canonical BGP policy rule. The result is that the Internet's routing topology is shaped as much by business contracts as by physical infrastructure, which is why BGP misconfiguration or route hijacking can have such dramatic real-world consequences."
```

## Explainer

Interior routing protocols like OSPF optimize for a single objective: find the shortest path. That works inside a single organization's network where every router cooperates and the goal is simple efficiency. But the Internet is not a single cooperative network — it is tens of thousands of independently operated **autonomous systems (AS)**, each with its own business interests, peering agreements, and traffic policies. **BGP** is the protocol that makes routing work across this landscape of competing interests, and it is fundamentally different in character from the interior protocols you have studied.

BGP uses **path-vector routing**, which means each route advertisement carries the complete list of autonomous systems the traffic would traverse. When AS 100 advertises a route to prefix 10.0.0.0/8, it tells its neighbor "I can reach 10.0.0.0/8 via the path [AS 100]." That neighbor (say AS 200) prepends its own AS number and advertises the path [AS 200, AS 100] to its neighbors. This full-path information serves two purposes. First, it prevents routing loops — if a router sees its own AS number already in the path, it rejects that route. Second, it provides the raw material for **policy-based routing decisions**. An AS can prefer a route through a paying customer over a cheaper path through a competitor, or avoid sending traffic through certain countries entirely.

The route selection process in BGP follows a multi-step **decision algorithm** that evaluates routes by local preference (administrator-set priority), AS path length, origin type, multi-exit discriminator, and several tiebreakers. Critically, the highest-priority criterion — **local preference** — is entirely under the operator's control and has nothing to do with path optimality. This means BGP routing is as much about business relationships as it is about network topology. The three main relationship types are **customer-provider** (the customer pays the provider for transit), **peer-peer** (two networks exchange traffic for free), and **transit** (traffic flowing through an intermediary). An AS will typically prefer customer routes (it gets paid) over peer routes (free) over provider routes (it pays).

BGP operates over TCP connections between neighboring routers, exchanging route updates incrementally rather than flooding entire topology databases. Two BGP routers establishing a session are called **peers** (confusingly, this is different from the business peering relationship). **eBGP** (external BGP) runs between routers in different autonomous systems, while **iBGP** (internal BGP) distributes externally learned routes within an AS. Because BGP is the protocol that literally holds the Internet together, its failure modes have outsized consequences — a single misconfigured route announcement can redirect or blackhole traffic for millions of users, which is why BGP security and route validation remain active areas of concern.
