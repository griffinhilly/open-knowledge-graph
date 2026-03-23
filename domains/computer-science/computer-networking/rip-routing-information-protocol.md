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
status: validated
---

# RIP: Routing Information Protocol

## Core Idea
RIP (Routing Information Protocol) is a distance-vector interior gateway protocol using hop count as the metric, with a maximum of 15 hops (limiting scalability). RIPv1 sends classful updates via broadcast; RIPv2 supports CIDR and multicast updates. Routers exchange routing tables periodically, implementing the Bellman-Ford algorithm with slow convergence and high overhead.

## How It's Best Learned
Deploy RIPv2 in a GNS3 lab and observe periodic updates (30-second intervals). Cause a topology change and measure convergence time. Monitor update traffic with Wireshark to understand message structure and timers.

## Common Misconceptions
RIP converges very slowly due to counting to infinity; split-horizon and poison reverse partially mitigate this. Hop count is a poor metric, favoring paths through many low-capacity links over fewer high-capacity ones. RIP is rarely used in production; OSPF and BGP are preferred.

## Questions

```yaml
- question: "A network has two paths from Router A to a destination server. Path X uses 2 hops over T1 lines (1.5 Mbps each). Path Y uses 4 hops over gigabit Ethernet links (1 Gbps each). How will RIP route traffic?"
  type: multiple-choice
  options:
    - "Via Path Y, because RIP weights routes by available bandwidth"
    - "Via Path X, because RIP uses hop count as its only metric and Path X has fewer hops"
    - "Via Path Y, because RIP computes a bandwidth-delay product for each path"
    - "RIP will load-balance across both paths since they are both valid routes"
  answer: 1
  explanation: "RIP uses hop count as its sole metric, treating every link as cost 1 regardless of bandwidth, latency, or reliability. Path X has 2 hops, Path Y has 4 hops, so RIP selects Path X — even though Path Y offers roughly 667× more bandwidth per link. This is a fundamental limitation of hop-count metrics: they are blind to link quality, leading RIP to frequently choose suboptimal paths in real networks."

- question: "After a link in a RIP network fails, why can it take several minutes for all routers to learn about the failure and converge on new routes?"
  type: multiple-choice
  options:
    - "RIP routers must synchronize their clocks before exchanging topology information"
    - "RIP sends updates only every 30 seconds, and counting-to-infinity can cause routers to slowly increment a dead route's cost one hop at a time until reaching 16"
    - "RIP requires explicit acknowledgment from every router in the autonomous system before removing a route"
    - "The default TTL of RIP packets is set equal to the update interval of 30 seconds"
  answer: 1
  explanation: "RIP's 30-second update timer means bad news travels slowly — a failure may not be propagated for up to 30 seconds per hop. Worse, the count-to-infinity problem causes routers to keep incrementing a failed route's hop count (1, 2, 3 ... 16) rather than immediately marking it unreachable, because each router believes a neighbor still has a valid path. Reaching the maximum hop count of 16 is the only way the route is eventually discarded. Mitigations like split horizon, poison reverse, and triggered updates reduce but do not eliminate this problem."

- question: "Split horizon completely solves the count-to-infinity problem, making RIP as fast to converge as link-state protocols like OSPF after a topology change."
  type: true-false
  answer: false
  explanation: "Split horizon prevents a router from advertising a route back to the neighbor it learned it from, which eliminates simple two-router routing loops. However, in networks with three or more routers forming a loop topology, counting-to-infinity can still occur even with split horizon. Additionally, the 30-second update interval itself fundamentally limits convergence speed regardless of loop prevention. OSPF, which uses link-state flooding and Dijkstra's algorithm, converges far more quickly after a failure."

- question: "RIPv2 improved on RIPv1 by adding support for classless (CIDR) addressing, including subnet mask information in route advertisements."
  type: true-false
  answer: true
  explanation: "RIPv1 is a classful protocol that assumes routes conform to class A/B/C boundaries and does not include subnet masks in updates. This made it incompatible with variable-length subnet masking (VLSM) and CIDR. RIPv2 fixed this by including a subnet mask field in each route entry, enabling classless routing. RIPv2 also switched from broadcast (255.255.255.255) to multicast (224.0.0.9) delivery, reducing unnecessary processing on non-RIP devices."

- question: "Explain why hop count is a poor routing metric and describe a specific network scenario where RIP would choose a significantly worse path than a bandwidth-aware routing protocol. What fundamental information is hop count unable to capture?"
  type: short-answer
  answer: "Hop count treats every link as identical, assigning a cost of 1 regardless of bandwidth, latency, reliability, or load. It cannot distinguish a 1 Gbps fiber link from a 56 Kbps dial-up connection. A concrete scenario: a path through three gigabit links (3 hops) vs. a path through two dial-up modems (2 hops) — RIP selects the dial-up path because it has fewer hops, even though the gigabit path delivers orders of magnitude more throughput. OSPF avoids this by using link cost inversely proportional to bandwidth, so high-capacity links are strongly preferred. The fundamental limitation is that hop count conflates topological distance (number of routers traversed) with actual transmission quality."
```

## Explainer

From your study of distance-vector routing, you know the basic idea: each router maintains a table of destinations and costs, periodically shares that table with its neighbors, and updates its own routes when it learns of a shorter path. **RIP** is the simplest real-world implementation of this pattern — it takes the Bellman-Ford algorithm you've studied and runs it as a distributed protocol across a network of routers.

RIP uses **hop count** as its sole metric. Every link costs 1, regardless of bandwidth or latency. A destination three routers away has a cost of 3. The maximum hop count is 15; anything at 16 hops is considered unreachable. This hard ceiling means RIP cannot operate on networks with a diameter larger than 15 hops, which is why it is limited to small or medium-sized networks. Every 30 seconds, each RIP router broadcasts (RIPv1) or multicasts (RIPv2) its entire routing table to its neighbors. When a router receives an update, it adds 1 to each advertised hop count and checks whether the new path is shorter than what it currently has.

The critical weakness of RIP is **slow convergence**. When a link fails, the bad news propagates slowly because routers only exchange updates every 30 seconds, and the count-to-infinity problem can cause routers to keep incrementing a dead route's cost one hop at a time until it reaches 16. Several mechanisms partially address this: **split horizon** prevents a router from advertising a route back to the neighbor it learned it from; **poison reverse** actively advertises failed routes with a cost of 16; and **triggered updates** send immediate notifications when a route changes rather than waiting for the next 30-second cycle. Even with these fixes, convergence after a failure can take minutes.

**RIPv2** improved on the original by adding support for CIDR (classless addressing) and subnet masks in route advertisements, authentication for security, and multicast delivery (224.0.0.9) instead of broadcast to reduce unnecessary processing on non-RIP devices. Despite these improvements, RIP's reliance on hop count as the only metric means it often chooses suboptimal paths — a route through five gigabit links looks worse than a route through four dial-up connections. This, combined with slow convergence and high bandwidth overhead from full table exchanges, is why modern networks overwhelmingly prefer link-state protocols like OSPF. Understanding RIP remains valuable, though, because it is the clearest illustration of how distance-vector theory translates into protocol mechanics.
