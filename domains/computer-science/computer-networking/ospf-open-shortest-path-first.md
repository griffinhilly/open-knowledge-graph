---
id: ospf-open-shortest-path-first
title: 'OSPF: Open Shortest Path First'
domain: computer-science
course: computer-networking
prerequisites:
- id: dijkstras-shortest-path-routing
  type: hard
builds-toward:
- bgp-border-gateway-protocol
tags:
- ospf
- link-state
- igp
- interior-gateway-protocol
stage: advanced
status: draft
---

# OSPF: Open Shortest Path First

## Core Idea
OSPF is a widely-used interior gateway protocol (IGP) that routers within an autonomous system use to exchange topology information and compute shortest paths. OSPF organizes networks into areas to reduce overhead, supports equal-cost multipath routing, and converges quickly to topology changes.

## Explainer

You already know Dijkstra's algorithm: given a weighted graph and a source node, it computes the shortest path to every other node. OSPF is what happens when you deploy Dijkstra's algorithm across a real network of routers. Each router runs OSPF to discover the network topology, share that topology with its neighbors, and then independently compute the best forwarding paths. The key insight is that every OSPF router builds the same complete map of the network, then runs the same shortest-path computation locally — there is no central authority deciding routes.

OSPF is a **link-state protocol**. Each router advertises the state of its directly connected links (which neighbors it can reach and at what cost) using **Link-State Advertisements (LSAs)**. These LSAs are flooded throughout the network: when a router receives a new LSA, it forwards copies to all its other neighbors. Through this flooding process, every router accumulates a complete **Link-State Database (LSDB)** — essentially an adjacency list representation of the entire network graph. Each router then runs Dijkstra's algorithm on this shared database to build its own routing table. Because all routers have the same LSDB, they all compute consistent, loop-free paths.

The challenge with pure link-state flooding is scalability. In a network with thousands of routers, every link change triggers a flood of LSAs to every router, and every router must re-run Dijkstra on the full graph. OSPF solves this with **areas** — logical subdivisions of the network. Area 0 (the **backbone area**) connects all other areas. Routers within an area exchange detailed LSAs only with each other; **Area Border Routers (ABRs)** summarize routes between areas. This hierarchy means a link failure in Area 3 triggers re-computation only within Area 3 — routers in Area 1 see only a summarized route change, not the internal topology details. The result is faster convergence and smaller LSDBs.

OSPF also supports **equal-cost multipath (ECMP)** routing: when Dijkstra finds multiple paths with the same total cost, OSPF installs all of them in the routing table and load-balances traffic across them. This is a significant advantage over protocols that select a single best path. Combined with fast convergence (routers detect link failures through hello packets and can recompute paths within seconds), OSPF remains the dominant interior gateway protocol for enterprise and service provider networks.
