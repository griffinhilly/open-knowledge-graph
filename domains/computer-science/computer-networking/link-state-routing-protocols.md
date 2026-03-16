---
id: link-state-routing-protocols
title: Link-State Routing Protocols
domain: computer-science
course: computer-networking
prerequisites:
- id: routing-algorithms-overview
  type: hard
- id: dijkstras-shortest-path-routing
  type: hard
builds-toward:
- ospf-open-shortest-path-first
tags:
- link-state
- ls-routing
- dijkstra
- flooding
stage: advanced
status: draft
---

# Link-State Routing Protocols

## Core Idea
Link-state routing protocols have each router flood information about its directly connected links to all other routers, allowing each router to independently compute shortest paths using Dijkstra's algorithm. OSPF is the most deployed link-state protocol; it converges faster than distance-vector approaches and avoids count-to-infinity problems but requires more memory and CPU.

## Explainer

You already understand two foundations that link-state routing builds on: routing algorithms in general (the problem of finding best paths through a network) and Dijkstra's shortest-path algorithm (the specific method for computing shortest paths given a complete graph). **Link-state routing** is the practical protocol framework that puts Dijkstra's algorithm to work in real networks. The core idea is simple: give every router a complete map of the network, then let each router independently compute the best paths using that map.

The protocol operates in two phases. In the **flooding phase**, each router discovers its directly connected neighbors and the cost (bandwidth, delay, or administrative weight) of each link. It packages this information into a **Link-State Advertisement (LSA)** and floods it to every other router in the network. Flooding means each router that receives an LSA forwards it out all other interfaces, so information propagates everywhere. Each LSA carries a sequence number to prevent stale data from overwriting fresh updates. Once flooding completes, every router holds an identical copy of the **link-state database (LSDB)** — a complete topology map showing all routers and all links with their costs.

In the **computation phase**, each router runs Dijkstra's algorithm on its copy of the LSDB, with itself as the source node. The result is a **shortest-path tree** rooted at that router, from which it builds its forwarding table. Because every router has the same LSDB, each one computes paths that are globally consistent — they all agree on the topology even though each computes independently. This is fundamentally different from distance-vector protocols, where routers only know the cost to reach each destination via each neighbor and have no visibility into the full network structure.

The advantages over distance-vector routing are significant. **Convergence is faster** because topology changes are flooded immediately rather than propagated hop-by-hop through iterative exchanges. The **count-to-infinity problem** — where distance-vector routers slowly increment costs after a link failure, sometimes creating temporary routing loops — simply cannot occur because every router sees the actual topology change. The tradeoff is resource consumption: each router must store the entire LSDB (memory) and run Dijkstra's algorithm whenever the topology changes (CPU). For large networks, OSPF addresses this through **area-based hierarchy**, dividing the network into areas so that routers only maintain detailed topology for their own area and receive summarized information about others — a practical compromise between complete knowledge and scalability.
