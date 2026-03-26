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
status: validated
---

# Link-State Routing Protocols

## Core Idea
Link-state routing protocols have each router flood information about its directly connected links to all other routers, allowing each router to independently compute shortest paths using Dijkstra's algorithm. OSPF is the most deployed link-state protocol; it converges faster than distance-vector approaches and avoids count-to-infinity problems but requires more memory and CPU.

## Questions

```yaml
- question: "A link between routers A and B fails in a network running a link-state protocol. How does this topology change reach all other routers?"
  type: multiple-choice
  options:
    - "Router A sends an update only to its directly connected neighbors, who propagate it hop-by-hop until all routers are informed"
    - "Routers A and B each generate a new Link-State Advertisement and flood it to every router in the network"
    - "The routing tables are updated centrally on a designated router, which distributes the new forwarding table to all others"
    - "All routers detect the failure simultaneously through periodic table exchanges and recalculate in unison"
  answer: 1
  explanation: "In link-state routing, the routers with the changed link generate updated LSAs and flood them to every router in the network. Flooding means each receiving router forwards the LSA out all other interfaces until the update reaches every router, which then updates its LSDB and independently reruns Dijkstra's algorithm. Option A describes distance-vector behavior (hop-by-hop propagation of routing tables). Option C describes a centralized scheme that link-state protocols explicitly avoid. Option D also describes distance-vector exchange behavior."

- question: "Why is the count-to-infinity problem impossible in a link-state routing protocol?"
  type: multiple-choice
  options:
    - "Link-state routers enforce a maximum hop count, preventing route costs from growing indefinitely"
    - "Link-state routers use split horizon — they never advertise a route back toward the router it came from"
    - "Every router has a complete topology map and computes paths from first-hand link data, so there are no second-hand estimates that can loop"
    - "Link-state protocols use triggered updates on topology changes, enabling faster convergence before loops can develop"
  answer: 2
  explanation: "Count-to-infinity arises in distance-vector routing because routers only know distances advertised by neighbors — if a link fails, routers may advertise incorrect paths based on stale estimates, creating loops where costs increment indefinitely. This cannot happen in link-state routing because every router has the actual network topology: each router's LSA describes only its own directly connected links, and Dijkstra runs on a complete, accurate map. There are no second-hand distance estimates to go wrong. Triggered updates (option D) help convergence speed but do not prevent count-to-infinity by themselves."

- question: "In a link-state network, all routers run Dijkstra's algorithm independently on their own copy of the link-state database, yet their forwarding tables are globally consistent because all copies of the LSDB are identical."
  type: true-false
  answer: true
  explanation: "This is a key insight into why link-state routing works. Because flooding ensures every router receives every LSA and builds the same topology map, each router's independent Dijkstra computation uses the same input graph. Different routers use themselves as the source node, but because they all agree on the network topology, their forwarding decisions are globally consistent — no loops or conflicting paths result. This stands in contrast to distance-vector, where consistency emerges only gradually through iterative table exchanges."

- question: "Link-state routing is more memory-efficient than distance-vector routing because routers mainly store their own routing table rather than a complete topology database."
  type: true-false
  answer: false
  explanation: "The opposite is true. Link-state routing requires each router to maintain a complete link-state database containing every router and every link in the network — significantly more memory than distance-vector routing, where routers store only the best distance to each destination via each neighbor. The LSDB grows with network size, which is why OSPF uses area-based hierarchy to limit the full topology each router must store. The memory and CPU cost of link-state routing is an explicit trade-off for its faster convergence and avoidance of routing loops."

- question: "What is the key architectural difference between link-state and distance-vector routing that explains why link-state converges faster and avoids count-to-infinity?"
  type: short-answer
  answer: "In distance-vector routing, each router knows only the distance to each destination via each neighbor — it has no visibility into the actual network topology. Routers share full routing tables with neighbors, so topology information propagates hop-by-hop through iterative table exchanges. This slow propagation and reliance on second-hand estimates creates the conditions for loops and count-to-infinity. In link-state routing, each router knows only its own directly connected links but immediately floods this accurate, first-hand information to every router in the network. Every router then has a complete, accurate topology map and computes shortest paths independently. Topology changes propagate in a single flooding wave rather than through iterative exchanges, enabling much faster convergence and eliminating the estimation errors that cause count-to-infinity."
  explanation: "The architectural contrast is: distance-vector routers know global distances but advertise only to neighbors; link-state routers know only local links but advertise globally. Flooding first-hand link information to all routers enables globally consistent computation that makes link-state reliable — each router has the same map and draws the same conclusions independently."
```

## Explainer

You already understand two foundations that link-state routing builds on: routing algorithms in general (the problem of finding best paths through a network) and Dijkstra's shortest-path algorithm (the specific method for computing shortest paths given a complete graph). **Link-state routing** is the practical protocol framework that puts Dijkstra's algorithm to work in real networks. The core idea is simple: give every router a complete map of the network, then let each router independently compute the best paths using that map.

The protocol operates in two phases. In the **flooding phase**, each router discovers its directly connected neighbors and the cost (bandwidth, delay, or administrative weight) of each link. It packages this information into a **Link-State Advertisement (LSA)** and floods it to every other router in the network. Flooding means each router that receives an LSA forwards it out all other interfaces, so information propagates everywhere. Each LSA carries a sequence number to prevent stale data from overwriting fresh updates. Once flooding completes, every router holds an identical copy of the **link-state database (LSDB)** — a complete topology map showing all routers and all links with their costs.

In the **computation phase**, each router runs Dijkstra's algorithm on its copy of the LSDB, with itself as the source node. The result is a **shortest-path tree** rooted at that router, from which it builds its forwarding table. Because every router has the same LSDB, each one computes paths that are globally consistent — they all agree on the topology even though each computes independently. This is fundamentally different from distance-vector protocols, where routers only know the cost to reach each destination via each neighbor and have no visibility into the full network structure.

The advantages over distance-vector routing are significant. **Convergence is faster** because topology changes are flooded immediately rather than propagated hop-by-hop through iterative exchanges. The **count-to-infinity problem** — where distance-vector routers slowly increment costs after a link failure, sometimes creating temporary routing loops — simply cannot occur because every router sees the actual topology change. The tradeoff is resource consumption: each router must store the entire LSDB (memory) and run Dijkstra's algorithm whenever the topology changes (CPU). For large networks, OSPF addresses this through **area-based hierarchy**, dividing the network into areas so that routers only maintain detailed topology for their own area and receive summarized information about others — a practical compromise between complete knowledge and scalability.
