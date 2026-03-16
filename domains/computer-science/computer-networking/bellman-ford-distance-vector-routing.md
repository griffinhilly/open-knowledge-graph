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

## Explainer

From your study of routing algorithms and the Bellman-Ford shortest-path algorithm, you know that finding optimal paths through a network graph requires systematically relaxing edge weights until distances stabilize. **Distance-vector routing** applies this algorithm in a distributed setting: instead of one central computer running Bellman-Ford on the entire network topology, each router independently runs its own local version, sharing partial results with its neighbors until the whole network converges on correct routing tables.

Here is how it works in practice. Each router maintains a **distance vector** — a table listing every known destination and the estimated cost (typically hop count) to reach it. Initially, each router only knows about its directly connected neighbors (cost = 1 hop or the link's metric). Periodically — every 30 seconds in RIP (Routing Information Protocol) — each router sends its entire distance vector to all directly connected neighbors. When a router receives a neighbor's distance vector, it applies the **Bellman-Ford equation**: for each destination D in the neighbor's table, it computes "cost to reach that neighbor + neighbor's cost to reach D." If this total is less than the router's current best cost to D, it updates its own table to route through that neighbor. Over successive rounds of exchange, shortest-path information propagates outward from each destination like ripples in a pond, and all routers converge to optimal routes.

The elegance of this approach is its simplicity: routers need no global knowledge of the network topology. Each router only talks to its immediate neighbors, and correct global routing emerges from purely local interactions. However, this simplicity comes with significant drawbacks. **Convergence is slow** — information propagates one hop per update interval, so a network with a diameter of 15 hops takes at minimum 15 rounds (7.5 minutes in RIP) to fully converge after a change. Worse, distance-vector protocols suffer from the **count-to-infinity problem**: when a link fails, routers may keep advertising stale routes to each other, incrementing the cost by one each round until it finally exceeds a maximum threshold (16 in RIP, which treats 16 as infinity). During this slow convergence, routing loops form and packets circle endlessly.

Several techniques mitigate these problems. **Split horizon** prevents a router from advertising a route back to the neighbor it learned it from — if router A reaches network X through router B, it does not tell B about that route, since B already knows a better path. **Poison reverse** strengthens this by explicitly advertising such routes with infinite cost. **Triggered updates** send changes immediately when a route fails rather than waiting for the periodic timer. Despite these fixes, distance-vector protocols remain slower to converge than link-state alternatives like OSPF, which is why RIP is largely confined to small networks. But the Bellman-Ford distributed model lives on in BGP (Border Gateway Protocol), the protocol that routes traffic between autonomous systems across the entire Internet — proof that the distance-vector concept scales when adapted appropriately.
