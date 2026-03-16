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

## Explainer

Interior routing protocols like OSPF optimize for a single objective: find the shortest path. That works inside a single organization's network where every router cooperates and the goal is simple efficiency. But the Internet is not a single cooperative network — it is tens of thousands of independently operated **autonomous systems (AS)**, each with its own business interests, peering agreements, and traffic policies. **BGP** is the protocol that makes routing work across this landscape of competing interests, and it is fundamentally different in character from the interior protocols you have studied.

BGP uses **path-vector routing**, which means each route advertisement carries the complete list of autonomous systems the traffic would traverse. When AS 100 advertises a route to prefix 10.0.0.0/8, it tells its neighbor "I can reach 10.0.0.0/8 via the path [AS 100]." That neighbor (say AS 200) prepends its own AS number and advertises the path [AS 200, AS 100] to its neighbors. This full-path information serves two purposes. First, it prevents routing loops — if a router sees its own AS number already in the path, it rejects that route. Second, it provides the raw material for **policy-based routing decisions**. An AS can prefer a route through a paying customer over a cheaper path through a competitor, or avoid sending traffic through certain countries entirely.

The route selection process in BGP follows a multi-step **decision algorithm** that evaluates routes by local preference (administrator-set priority), AS path length, origin type, multi-exit discriminator, and several tiebreakers. Critically, the highest-priority criterion — **local preference** — is entirely under the operator's control and has nothing to do with path optimality. This means BGP routing is as much about business relationships as it is about network topology. The three main relationship types are **customer-provider** (the customer pays the provider for transit), **peer-peer** (two networks exchange traffic for free), and **transit** (traffic flowing through an intermediary). An AS will typically prefer customer routes (it gets paid) over peer routes (free) over provider routes (it pays).

BGP operates over TCP connections between neighboring routers, exchanging route updates incrementally rather than flooding entire topology databases. Two BGP routers establishing a session are called **peers** (confusingly, this is different from the business peering relationship). **eBGP** (external BGP) runs between routers in different autonomous systems, while **iBGP** (internal BGP) distributes externally learned routes within an AS. Because BGP is the protocol that literally holds the Internet together, its failure modes have outsized consequences — a single misconfigured route announcement can redirect or blackhole traffic for millions of users, which is why BGP security and route validation remain active areas of concern.
