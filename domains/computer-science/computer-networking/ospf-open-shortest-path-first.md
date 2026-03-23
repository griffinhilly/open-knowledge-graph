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
status: validated
---

# OSPF: Open Shortest Path First

## Core Idea
OSPF is a widely-used interior gateway protocol (IGP) that routers within an autonomous system use to exchange topology information and compute shortest paths. OSPF organizes networks into areas to reduce overhead, supports equal-cost multipath routing, and converges quickly to topology changes.

## Questions

```yaml
- question: "A link fails between two routers in OSPF Area 3. The network has 5 areas total (Area 0 through Area 4). Which routers must re-run Dijkstra's algorithm?"
  type: multiple-choice
  options:
    - "All routers in the network, because OSPF floods LSAs to every router regardless of area"
    - "Only the two routers directly adjacent to the failed link"
    - "All routers within Area 3, plus Area Border Routers that summarize Area 3 routes to other areas"
    - "No routers — OSPF pre-computes backup paths and switches automatically without recalculation"
  answer: 2
  explanation: "OSPF areas limit the propagation of detailed topology changes. A link failure in Area 3 triggers LSAs that flood only within Area 3, so only routers inside Area 3 re-run Dijkstra on the updated LSDB. Area Border Routers (ABRs) may generate summarized LSAs to inform other areas of changed summary routes, but routers in Areas 1, 2, and 4 never see the internal topology detail. This is the core scalability benefit of areas: failures are localized, minimizing unnecessary computation across the network."

- question: "OSPF discovers two routes to the same destination with total costs of 20 and 20 (identical). What does OSPF do?"
  type: multiple-choice
  options:
    - "Drops one route arbitrarily and installs only the other to avoid routing loops"
    - "Installs both routes and load-balances traffic across them (ECMP)"
    - "Waits for the costs to differ before making a forwarding decision"
    - "Selects the route through the router with the lower Router ID as a tiebreaker"
  answer: 1
  explanation: "OSPF supports Equal-Cost Multipath (ECMP) routing: when Dijkstra finds multiple paths with the same total cost, all are installed in the routing table and traffic is load-balanced across them. This is a significant advantage over protocols that must pick one best path — ECMP improves throughput and resilience. Option D describes a tiebreaker used in some other contexts (like Designated Router election), but it does not apply to ECMP path selection."

- question: "In OSPF, a central route-computation server calculates shortest paths and distributes them to all routers."
  type: true-false
  answer: false
  explanation: "OSPF is fully distributed. Every router independently builds the same complete Link-State Database (LSDB) through the flooding of LSAs, and every router independently runs Dijkstra's algorithm on that database to compute its own routing table. There is no central authority. The key insight is that because all routers share the same LSDB, they all compute consistent, loop-free results without coordination — each router reaches the same conclusion autonomously."

- question: "Area 0 (the backbone area) must connect all other OSPF areas, either directly or through virtual links."
  type: true-false
  answer: true
  explanation: "OSPF's hierarchical area design requires all non-backbone areas to connect to Area 0. Inter-area routing flows through the backbone: when traffic moves from Area 2 to Area 4, it goes through Area 0. Area Border Routers (ABRs) connect their area to Area 0 and summarize topology between them. If a non-backbone area cannot connect directly to Area 0, OSPF provides virtual links as a workaround — but the logical requirement that all routing pass through Area 0 remains absolute."

- question: "Why does OSPF organize routers into areas rather than flooding all topology information to every router in the network?"
  type: short-answer
  answer: "Areas limit the scope of topology flooding and path computation. In a flat OSPF network, every link change floods LSAs to every router, and every router must re-run Dijkstra on the entire network graph. As the network grows, this becomes prohibitive: LSA traffic consumes bandwidth, and Dijkstra re-runs consume CPU proportional to the number of edges. Areas contain topology detail within logical boundaries — a failure in one area triggers flooding and re-computation only within that area. Area Border Routers summarize inter-area reachability, so routers in other areas see only abstract route changes, not internal topology. The result is smaller LSDBs, faster convergence, and dramatically reduced overhead in large networks."
  explanation: "The tradeoff is that summarization loses some information — ABRs cannot propagate every metric detail across area boundaries, and OSPF cannot achieve globally optimal paths in all cases with summarization. But the scalability gains in large networks far outweigh this cost."
```

## Explainer

You already know Dijkstra's algorithm: given a weighted graph and a source node, it computes the shortest path to every other node. OSPF is what happens when you deploy Dijkstra's algorithm across a real network of routers. Each router runs OSPF to discover the network topology, share that topology with its neighbors, and then independently compute the best forwarding paths. The key insight is that every OSPF router builds the same complete map of the network, then runs the same shortest-path computation locally — there is no central authority deciding routes.

OSPF is a **link-state protocol**. Each router advertises the state of its directly connected links (which neighbors it can reach and at what cost) using **Link-State Advertisements (LSAs)**. These LSAs are flooded throughout the network: when a router receives a new LSA, it forwards copies to all its other neighbors. Through this flooding process, every router accumulates a complete **Link-State Database (LSDB)** — essentially an adjacency list representation of the entire network graph. Each router then runs Dijkstra's algorithm on this shared database to build its own routing table. Because all routers have the same LSDB, they all compute consistent, loop-free paths.

The challenge with pure link-state flooding is scalability. In a network with thousands of routers, every link change triggers a flood of LSAs to every router, and every router must re-run Dijkstra on the full graph. OSPF solves this with **areas** — logical subdivisions of the network. Area 0 (the **backbone area**) connects all other areas. Routers within an area exchange detailed LSAs only with each other; **Area Border Routers (ABRs)** summarize routes between areas. This hierarchy means a link failure in Area 3 triggers re-computation only within Area 3 — routers in Area 1 see only a summarized route change, not the internal topology details. The result is faster convergence and smaller LSDBs.

OSPF also supports **equal-cost multipath (ECMP)** routing: when Dijkstra finds multiple paths with the same total cost, OSPF installs all of them in the routing table and load-balances traffic across them. This is a significant advantage over protocols that select a single best path. Combined with fast convergence (routers detect link failures through hello packets and can recompute paths within seconds), OSPF remains the dominant interior gateway protocol for enterprise and service provider networks.
