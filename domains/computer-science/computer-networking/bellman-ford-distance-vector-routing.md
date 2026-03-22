---
id: bellman-ford-distance-vector-routing
title: Bellman-Ford Algorithm and Distance-Vector Routing
domain: computer-science
course: computer-networking
prerequisites:
- id: routing-algorithms-overview
  type: hard
- id: bellman-ford-algorithm
  type: hard
tags:
- bellman-ford
- distance-vector
- rip
- distributed-algorithm
stage: advanced
status: draft
---

# Bellman-Ford Algorithm and Distance-Vector Routing

## Core Idea
The Bellman-Ford algorithm is the basis for distance-vector routing protocols (e.g., RIP) where routers share their distance vectors (hop counts or costs) with direct neighbors. Each router updates its routing table based on neighbors' announcements, converging to shortest paths in a distributed manner, though more slowly than link-state protocols.

## Questions

```yaml
- question: "Router A reaches network X through router B (cost 2). The direct link from B to X then fails. Before B can propagate the failure, A sends B its distance vector saying it can reach X at cost 3. What happens next?"
  type: multiple-choice
  options:
    - "B correctly detects the loop and immediately removes X from its routing table"
    - "B updates its route to X via A at cost 4, and A may then update again via B, creating a counting loop"
    - "A's advertisement is ignored because B originally told A about X, and split horizon prevents A from advertising it back"
    - "The count-to-infinity cannot start because triggered updates will propagate the failure instantly"
  answer: 1
  explanation: "This is the count-to-infinity problem. B's direct link to X has failed, so its cost to X is now infinite. But before that failure propagates, A tells B: 'I can reach X at cost 3 (via you!).' B doesn't know A's route loops back through itself, so it updates to reach X via A at cost 4. Next round, A hears B's update (cost 4 to X) and updates to cost 5, then B to cost 6, and so on — the cost increments indefinitely until it reaches 16 (RIP's infinity). Split horizon (option C) would only prevent this if A had a simple two-router topology with B, not in more complex network configurations."

- question: "Why is RIP (which uses distance-vector routing) limited to networks with a maximum diameter of 15 hops?"
  type: multiple-choice
  options:
    - "Hardware limitations prevent RIP routers from storing routing tables larger than 15 entries"
    - "RIP uses 16 as 'infinity' to bound the count-to-infinity problem, making any route with cost 16 unreachable"
    - "The 30-second update timer means a 15-hop network takes 7.5 minutes to converge, which is the maximum allowed"
    - "TCP/IP protocol headers can only encode hop counts up to 15 bits"
  answer: 1
  explanation: "RIP defines cost 16 as 'infinity' (unreachable). During count-to-infinity, costs increment until they hit 16, at which point the route is poisoned. This design choice bounds the counting loop at the cost of limiting usable network diameter to 15 hops — any legitimate route with more than 15 hops would appear unreachable. This trade-off is why RIP is unsuitable for large networks and why link-state protocols (OSPF) are used instead when networks grow beyond a few dozen routers."

- question: "Split horizon completely eliminates the count-to-infinity problem in distance-vector routing protocols."
  type: true-false
  answer: false
  explanation: "Split horizon prevents a router from advertising a route back to the neighbor it learned it from, which stops simple two-router counting loops. However, it does not eliminate count-to-infinity in networks with three or more routers arranged in a topology where routes can loop through intermediate routers. In a triangle topology (A-B-C-A), if the link between A and the destination fails, B and C can still form a counting loop with each other because neither is advertising the route back to the specific neighbor it learned from. Poison reverse strengthens split horizon but still cannot guarantee loop-freedom in all topologies."

- question: "In distance-vector routing, each router requires knowledge of the full network topology to compute its routing table."
  type: true-false
  answer: false
  explanation: "This is the key distinction between distance-vector and link-state routing. In distance-vector routing, each router only knows its own distance vector (estimated costs to all destinations) and its direct neighbors' distance vectors. It has no knowledge of the overall network topology — which routers connect to which. Global shortest-path routing emerges from purely local exchanges: routers share costs, not topology. This simplicity is both the elegance (less information to store) and the weakness (counts to infinity, slow convergence) of the approach."

- question: "Why does the count-to-infinity problem not occur in link-state routing protocols like OSPF?"
  type: short-answer
  answer: "In link-state routing, every router floods the network with its local link-state information, so each router builds a complete, consistent map of the entire network topology. When a link fails, all routers update their maps and recompute shortest paths independently — there is no iterative exchange of distance estimates that can create counting loops."
  explanation: "Count-to-infinity arises because distance-vector routers only know costs, not topology — they cannot detect that an advertised route loops through themselves. Link-state protocols share raw topology (who is connected to whom with what cost), not computed distances. With a full topology map, Dijkstra's algorithm computes correct shortest paths in one shot per router, and link-failure updates propagate as topology changes rather than as incrementing cost estimates."
```

## Explainer

From your study of routing algorithms and the Bellman-Ford shortest-path algorithm, you know that finding optimal paths through a network graph requires systematically relaxing edge weights until distances stabilize. **Distance-vector routing** applies this algorithm in a distributed setting: instead of one central computer running Bellman-Ford on the entire network topology, each router independently runs its own local version, sharing partial results with its neighbors until the whole network converges on correct routing tables.

Here is how it works in practice. Each router maintains a **distance vector** — a table listing every known destination and the estimated cost (typically hop count) to reach it. Initially, each router only knows about its directly connected neighbors (cost = 1 hop or the link's metric). Periodically — every 30 seconds in RIP (Routing Information Protocol) — each router sends its entire distance vector to all directly connected neighbors. When a router receives a neighbor's distance vector, it applies the **Bellman-Ford equation**: for each destination D in the neighbor's table, it computes "cost to reach that neighbor + neighbor's cost to reach D." If this total is less than the router's current best cost to D, it updates its own table to route through that neighbor. Over successive rounds of exchange, shortest-path information propagates outward from each destination like ripples in a pond, and all routers converge to optimal routes.

The elegance of this approach is its simplicity: routers need no global knowledge of the network topology. Each router only talks to its immediate neighbors, and correct global routing emerges from purely local interactions. However, this simplicity comes with significant drawbacks. **Convergence is slow** — information propagates one hop per update interval, so a network with a diameter of 15 hops takes at minimum 15 rounds (7.5 minutes in RIP) to fully converge after a change. Worse, distance-vector protocols suffer from the **count-to-infinity problem**: when a link fails, routers may keep advertising stale routes to each other, incrementing the cost by one each round until it finally exceeds a maximum threshold (16 in RIP, which treats 16 as infinity). During this slow convergence, routing loops form and packets circle endlessly.

Several techniques mitigate these problems. **Split horizon** prevents a router from advertising a route back to the neighbor it learned it from — if router A reaches network X through router B, it does not tell B about that route, since B already knows a better path. **Poison reverse** strengthens this by explicitly advertising such routes with infinite cost. **Triggered updates** send changes immediately when a route fails rather than waiting for the periodic timer. Despite these fixes, distance-vector protocols remain slower to converge than link-state alternatives like OSPF, which is why RIP is largely confined to small networks. But the Bellman-Ford distributed model lives on in BGP (Border Gateway Protocol), the protocol that routes traffic between autonomous systems across the entire Internet — proof that the distance-vector concept scales when adapted appropriately.
