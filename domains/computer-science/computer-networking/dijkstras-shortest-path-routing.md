---
id: dijkstras-shortest-path-routing
title: Dijkstra's Shortest Path Algorithm in Routing
domain: computer-science
course: computer-networking
prerequisites:
- id: routing-algorithms-overview
  type: hard
builds-toward:
- ospf-open-shortest-path-first
tags:
- dijkstra
- link-state
- shortest-path
- ospf
stage: advanced
status: validated
---

# Dijkstra's Shortest Path Algorithm in Routing

## Core Idea
Dijkstra's algorithm is used in link-state routing protocols like OSPF to compute the shortest path from a router to all other routers in a network. Each router runs Dijkstra independently on its synchronized view of the network topology, producing a shortest-path tree rooted at that router.

## Questions

```yaml
- question: "A student argues that Dijkstra's greedy step — always confirming the minimum-cost tentative node — might miss a cheaper path discovered later through other nodes. Why is this concern unfounded in standard routing networks?"
  type: multiple-choice
  options:
    - "Routers cache all possible paths, so any missed path is retrieved from cache"
    - "The priority queue automatically re-examines all tentative nodes after each confirmation"
    - "All link costs are non-negative, so no path through an unvisited node can be cheaper than a path already confirmed"
    - "In practice, the greedy step occasionally produces suboptimal results, but the error is negligible"
  answer: 2
  explanation: "The correctness proof relies on non-negative edge weights. If all costs are ≥ 0, then adding any further edge to a path can only increase or maintain its total cost — it can never decrease it. So once a node is confirmed (selected as the minimum-cost tentative node), no future path through unvisited nodes can be cheaper. If negative weights were allowed, a 'cheaper' path could appear later, breaking the algorithm. This is why Dijkstra fails with negative weights."

- question: "After running Dijkstra's algorithm, what does a router actually store in its forwarding table for use in packet delivery?"
  type: multiple-choice
  options:
    - "The complete shortest-path tree so it can recompute optimal paths on demand for each packet"
    - "Only the first hop toward each destination — the outgoing interface for each reachable network prefix"
    - "The complete sequence of routers for every destination path through the network"
    - "The total cost (distance) to each destination, updated on every packet arrival"
  answer: 1
  explanation: "A router only needs to know which interface to forward a packet through — the next hop. Once a packet takes the correct first hop, the next router applies its own forwarding table, and so on. Because all routers run Dijkstra on the same synchronized topology, their independent first-hop decisions produce globally consistent, loop-free paths. Storing full paths would be wasteful and scale poorly."

- question: "In link-state routing with OSPF, every router in the network independently runs Dijkstra's algorithm on the same topology database, each computing a shortest-path tree rooted at itself."
  type: true-false
  answer: true
  explanation: "This distributed independence is the key architectural property of link-state routing. Because every router has flooded its link-state advertisement to all others, all routers share an identical topology database. Each runs Dijkstra independently to compute its own SPT. The results are globally consistent even though no central coordinator exists — as long as all routers have the same database, their independent computations produce compatible forwarding decisions."

- question: "Dijkstra's algorithm produces correct shortest paths even when some link costs are negative, as long as no cycle in the network has a negative total cost."
  type: true-false
  answer: false
  explanation: "Dijkstra requires all individual edge weights to be non-negative — not just that no negative cycle exists. The greedy step's correctness depends on the property that confirmed paths cannot be improved by going through unvisited nodes. A single negative edge (even without a negative cycle) can violate this: a cheaper path through a not-yet-visited node might exist after a node is already confirmed. Bellman-Ford handles negative edges (without negative cycles) at the cost of higher time complexity."

- question: "Explain why the greedy step in Dijkstra's algorithm — always selecting the minimum-cost tentative node and treating its shortest path as final — is guaranteed to produce correct results in a routing network."
  type: short-answer
  answer: "The greedy step is correct because all link costs are non-negative. When a tentative node v is selected as the cheapest unconfirmed node, the cost to reach it via the current best path is d(v). Any alternative path to v would have to pass through some other unconfirmed node u, whose current tentative cost is ≥ d(v). Since all remaining edge weights are ≥ 0, the cost through u can only be ≥ d(v). Therefore no cheaper path to v can exist, and confirming it as d(v) is correct."
  explanation: "This is a proof by contradiction: assume confirming v is wrong and a cheaper path exists. That cheaper path must pass through some unvisited node u. But u's tentative cost is already ≥ d(v), and adding the non-negative edge from u to v can only increase cost further. Contradiction. Non-negative weights are the essential precondition — the entire correctness argument collapses if any edge weight is negative, which is why Dijkstra cannot be used on networks with negative link costs."
```

## Explainer

From your overview of routing algorithms, you know that routers must decide which interface to forward each packet through, and that link-state protocols work by giving every router a complete map of the network. Dijkstra's algorithm is the engine that turns that map into actual forwarding decisions. It answers the question: given a weighted graph where nodes are routers and edge weights represent link costs (delay, bandwidth, or administrative metrics), what is the least-cost path from me to every other router?

The algorithm works by maintaining two sets: a **confirmed set** of routers whose shortest path is already known, and a **tentative set** of candidates. Initially, only the source router (you) is confirmed, with cost 0. You examine all links from confirmed routers to unconfirmed neighbors, recording the total cost to reach each neighbor through the best known path. Then you move the lowest-cost tentative node into the confirmed set — this is the greedy step, and it works because all link costs are non-negative, so no cheaper path to that node can exist through an unvisited router. You then examine that newly confirmed node's neighbors and update their tentative costs if a cheaper path through the new node exists. This process repeats until every router is confirmed.

The result is a **shortest-path tree (SPT)** rooted at the source router. Each branch of this tree represents the optimal forwarding path to a destination. The router only needs the first hop of each path to build its **forwarding table**: to reach destination X, send the packet out the interface that leads to the next hop on the shortest path to X. Because every router in the network has the same topology database (synchronized via link-state advertisements), every router independently computes its own SPT, and the forwarding decisions are globally consistent — packets follow optimal paths without loops.

In practice, OSPF (Open Shortest Path First) runs Dijkstra every time the topology changes — a link goes down, a cost changes, or a new router joins. The algorithm's time complexity is O(N² ) for a simple implementation or O(N log N + E) with a priority queue, where N is the number of routers and E is the number of links. For networks of hundreds or even thousands of routers, this runs in milliseconds. The real cost is not computation but **convergence** — the time for all routers to receive the updated topology information and recompute their trees. During convergence, routers may briefly have inconsistent views, potentially causing transient loops or packet drops until the network stabilizes.
