---
id: rip-routing-information-protocol
title: 'RIP: Routing Information Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: distance-vector-routing-protocols
  type: hard
- id: routing-algorithms-overview
  type: hard
builds-toward:
- eigrp-enhanced-distance-vector-routing
- routing-convergence-flap-damping
tags:
- routing
- distance-vector
- igp
- dynamic-routing
stage: advanced
status: draft
---

# RIP: Routing Information Protocol

## Core Idea
RIP (Routing Information Protocol) is a distance-vector interior gateway protocol using hop count as the metric, with a maximum of 15 hops (limiting scalability). RIPv1 sends classful updates via broadcast; RIPv2 supports CIDR and multicast updates. Routers exchange routing tables periodically, implementing the Bellman-Ford algorithm with slow convergence and high overhead.

## How It's Best Learned
Deploy RIPv2 in a GNS3 lab and observe periodic updates (30-second intervals). Cause a topology change and measure convergence time. Monitor update traffic with Wireshark to understand message structure and timers.

## Common Misconceptions
RIP converges very slowly due to counting to infinity; split-horizon and poison reverse partially mitigate this. Hop count is a poor metric, favoring paths through many low-capacity links over fewer high-capacity ones. RIP is rarely used in production; OSPF and BGP are preferred.

## Explainer

From your study of distance-vector routing, you know the basic idea: each router maintains a table of destinations and costs, periodically shares that table with its neighbors, and updates its own routes when it learns of a shorter path. **RIP** is the simplest real-world implementation of this pattern — it takes the Bellman-Ford algorithm you've studied and runs it as a distributed protocol across a network of routers.

RIP uses **hop count** as its sole metric. Every link costs 1, regardless of bandwidth or latency. A destination three routers away has a cost of 3. The maximum hop count is 15; anything at 16 hops is considered unreachable. This hard ceiling means RIP cannot operate on networks with a diameter larger than 15 hops, which is why it is limited to small or medium-sized networks. Every 30 seconds, each RIP router broadcasts (RIPv1) or multicasts (RIPv2) its entire routing table to its neighbors. When a router receives an update, it adds 1 to each advertised hop count and checks whether the new path is shorter than what it currently has.

The critical weakness of RIP is **slow convergence**. When a link fails, the bad news propagates slowly because routers only exchange updates every 30 seconds, and the count-to-infinity problem can cause routers to keep incrementing a dead route's cost one hop at a time until it reaches 16. Several mechanisms partially address this: **split horizon** prevents a router from advertising a route back to the neighbor it learned it from; **poison reverse** actively advertises failed routes with a cost of 16; and **triggered updates** send immediate notifications when a route changes rather than waiting for the next 30-second cycle. Even with these fixes, convergence after a failure can take minutes.

**RIPv2** improved on the original by adding support for CIDR (classless addressing) and subnet masks in route advertisements, authentication for security, and multicast delivery (224.0.0.9) instead of broadcast to reduce unnecessary processing on non-RIP devices. Despite these improvements, RIP's reliance on hop count as the only metric means it often chooses suboptimal paths — a route through five gigabit links looks worse than a route through four dial-up connections. This, combined with slow convergence and high bandwidth overhead from full table exchanges, is why modern networks overwhelmingly prefer link-state protocols like OSPF. Understanding RIP remains valuable, though, because it is the clearest illustration of how distance-vector theory translates into protocol mechanics.
