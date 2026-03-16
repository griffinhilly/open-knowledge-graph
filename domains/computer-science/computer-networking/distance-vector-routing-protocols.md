---
id: distance-vector-routing-protocols
title: Distance-Vector Routing Protocols
domain: computer-science
course: computer-networking
prerequisites:
- id: routing-algorithms-overview
  type: hard
- id: bellman-ford-distance-vector-routing
  type: hard
builds-toward:
- bgp-border-gateway-protocol
tags:
- distance-vector
- dv-routing
- bellman-ford
- rip
stage: advanced
status: draft
---

# Distance-Vector Routing Protocols

## Core Idea
Distance-vector routing protocols compute shortest paths based on a simple metric by having each router advertise its distances to all destinations and update based on neighbors' advertisements. RIP is a classic distance-vector protocol that uses hop count as its metric. Distance-vector protocols converge slowly and suffer from count-to-infinity problems, but remain simple to implement.

## Explainer

From your study of routing algorithms and Bellman-Ford, you know the mathematical foundation: the shortest distance from node X to destination D equals the minimum over all neighbors N of (cost to N + N's distance to D). **Distance-vector routing protocols** are the direct implementation of this equation in real networks. Each router maintains a **routing table** (the "distance vector") that lists, for every known destination, the best distance and the next-hop router to use. Periodically, each router sends its entire distance vector to its directly connected neighbors.

Here is how convergence works in practice. Initially, each router only knows about its directly connected networks (distance = 0 or the link cost). Router A tells neighbor B: "I can reach network 10.0.1.0 with cost 1." Router B, which has cost 1 to reach A, now knows it can reach 10.0.1.0 with cost 2 via A. B adds this to its table and shares its updated vector with its own neighbors. Through repeated exchanges, knowledge of all destinations propagates outward like ripples in a pond. After enough rounds of updates (bounded by the network diameter), every router has a consistent shortest-path entry for every destination. This is the Bellman-Ford algorithm running in a distributed, asynchronous fashion.

**RIP (Routing Information Protocol)** is the textbook distance-vector protocol. It uses **hop count** as its metric (each link costs 1), sends updates every 30 seconds, and caps the maximum distance at 15 hops (16 = infinity/unreachable). RIP's simplicity makes it easy to configure but limits it to small networks. Larger or more complex networks use protocols with richer metrics.

The critical weakness of distance-vector routing is slow convergence after failures — the **count-to-infinity problem**. Suppose router A reaches network X through B with cost 2, and the link from B to X fails. B removes its route, but then receives A's next update saying "I can reach X with cost 2." B mistakenly concludes it can reach X through A with cost 3. A then updates to cost 4 via B, B updates to 5, and so on — the distance "counts to infinity" (15 in RIP) before the routers agree the network is unreachable. Mitigations include **split horizon** (don't advertise a route back to the neighbor you learned it from), **poison reverse** (advertise it back with infinite cost), and **triggered updates** (send changes immediately instead of waiting for the periodic timer). These techniques reduce but do not fully eliminate slow convergence, which is why larger networks often prefer link-state protocols that have a complete topology view.
