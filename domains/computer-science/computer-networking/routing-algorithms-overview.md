---
id: routing-algorithms-overview
title: Routing Algorithms and Protocols
domain: computer-science
course: computer-networking
prerequisites:
- id: ip-routing-basics
  type: hard
builds-toward:
- dijkstras-shortest-path-routing
- bellman-ford-distance-vector-routing
- ospf-open-shortest-path-first
tags:
- routing-algorithms
- protocols
- distance-vector
- link-state
stage: advanced
status: draft
---

# Routing Algorithms and Protocols

## Core Idea
Routing algorithms compute paths through a network to reach destination addresses. Distance-vector algorithms (e.g., RIP) share distances to known destinations with neighbors; link-state algorithms (e.g., OSPF) flood the entire network topology to all routers. Each approach has tradeoffs in convergence time, overhead, and scalability.

## How It's Best Learned
Simulate both distance-vector and link-state protocols in a network simulator; observe how each converges after topology changes.

## Common Misconceptions
- All routing algorithms find globally optimal paths; distributed algorithms converge to locally good paths.
- Distance-vector converges faster than link-state; link-state typically converges faster despite higher overhead.

## Questions

```yaml
- question: "A router running a distance-vector protocol learns from its neighbor that a destination is 3 hops away. What distance does the router record for that destination in its own routing table?"
  type: multiple-choice
  options: ["3 hops, identical to the neighbor's distance", "4 hops, adding 1 for the link to the neighbor", "1 hop, since the neighbor is one step away", "The router queries the destination directly to find the true distance"]
  answer: 1
  explanation: "In distance-vector routing, a router adds 1 (the cost of reaching its neighbor) to the neighbor's advertised distance. If the neighbor says the destination is 3 hops, the route through that neighbor costs 3 + 1 = 4 hops. This additive logic is the 'distance vector' — each router only knows distances, not the full path."

- question: "Link-state routing protocols are slower to converge than distance-vector protocols because they flood more information across the network."
  type: true-false
  answer: false
  explanation: "Despite the higher overhead of flooding, link-state protocols (like OSPF) converge faster. Each router builds a complete, accurate map of the network and computes optimal paths independently. Distance-vector protocols are prone to slow convergence — especially the 'count-to-infinity' problem — because routers only know their neighbors' distances and may cycle through incorrect routes before settling."

- question: "What is the fundamental difference between the information a distance-vector router shares with its neighbors and the information a link-state router floods to all routers?"
  type: short-answer
  answer: "A distance-vector router shares its routing table — a list of destinations and the distances to them. A link-state router shares its link-state advertisements (LSAs) — a description of its directly connected links and their costs, not the full routing table."
  explanation: "This distinction is the key conceptual divide. Distance-vector routers share their computed conclusions (how far away things seem). Link-state routers share raw facts about their local environment (what links they have). Every link-state router then independently reconstructs the full topology and computes shortest paths using Dijkstra's algorithm, rather than trusting its neighbors' potentially stale conclusions."
```

## Explainer

From your study of IP routing basics, you know that routers forward packets hop-by-hop toward a destination by consulting their routing tables. Routing algorithms are the mechanisms by which routers populate those tables — determining the best path to every known destination in the network. Two fundamentally different approaches exist: distance-vector and link-state.

In a distance-vector protocol, each router maintains a table of distances to every known destination and periodically shares this table with its direct neighbors. When a neighbor advertises a distance, the receiving router adds 1 (or some cost) for the link to that neighbor and updates its own table if it found a shorter route. Over many rounds of exchange, routing information propagates hop by hop until all routers converge on consistent paths. RIP (Routing Information Protocol) is the classic example. The weakness of this approach is slow convergence: if a link fails, the misinformation can bounce between neighbors in a phenomenon called "count to infinity" — routers keep advertising increasingly large (but nonexistent) distances until the protocol stabilizes.

Link-state protocols take a different approach: each router builds a complete map of the entire network. Every router floods a short advertisement describing only its directly connected links and their costs — not its full routing table. Once a router has received link-state advertisements from every other router, it runs Dijkstra's shortest-path algorithm on the complete topology to compute the optimal path to every destination. OSPF (Open Shortest Path First) is the dominant real-world example. Because every router works from the same complete map, link-state protocols converge much faster and avoid count-to-infinity problems, at the cost of more flooding overhead and more memory.

The tradeoff between the two approaches comes down to what information is shared and where computation happens. Distance-vector is simple and low-overhead but slow to react to failures. Link-state is more complex and chatty but produces faster, more accurate convergence. Modern enterprise and ISP networks almost universally prefer link-state protocols (OSPF, IS-IS) for their superior convergence properties, while distance-vector protocols (RIP) survive mainly in simpler or legacy environments.
