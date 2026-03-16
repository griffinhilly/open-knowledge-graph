---
id: network-flows-max-flow-min-cut
title: Network Flows and the Max-Flow Min-Cut Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: formal-definitions-graph-theory
  type: hard
builds-toward:
- menger-theorem
tags:
- network-flows
- max-flow-min-cut
- optimization
stage: formal-systems
status: draft
---

# Network Flows and the Max-Flow Min-Cut Theorem

## Core Idea
A flow on a directed graph assigns values to edges respecting capacity constraints and flow conservation. The max-flow min-cut theorem proves that the maximum flow value equals the minimum cut capacity, a fundamental min-max result with applications to matching, connectivity, and scheduling.

## How It's Best Learned
Implement the Ford–Fulkerson method or Edmonds–Karp algorithm, watching augmenting paths progressively increase the flow. Verify that the final flow equals the minimum cut capacity.

## Common Misconceptions
- Thinking flow conservation applies at the source and sink (it does not; they are special).
- Assuming every augmenting path yields the same final flow value (the max-flow value is unique, but augmenting paths are not).

## Explainer

From your work with directed graphs, you know that edges have direction. A **flow network** adds two more pieces of structure: every edge has a **capacity** (an upper limit on how much can flow through it), and there are two special vertices — a **source** s where flow originates and a **sink** t where flow terminates. A **flow** is an assignment of a nonneg value to each edge satisfying two rules: (1) **capacity constraint** — the flow on each edge cannot exceed its capacity; and (2) **flow conservation** — for every vertex except s and t, the total flow in equals the total flow out. The **value** of the flow is the net flow leaving s (equivalently, arriving at t).

The central question is: what is the maximum flow you can push from s to t? The **Ford-Fulkerson method** answers this iteratively. Build a **residual graph**: for each edge with capacity c carrying flow f, add a forward edge with residual capacity c − f (room to add more flow) and a backward edge with capacity f (flow that can be "undone"). Find any **augmenting path** from s to t in the residual graph — a path with positive residual capacity on every edge. Push as much flow as possible along that path (the bottleneck capacity). Repeat until no augmenting path exists. The backward edges are the clever part: they allow the algorithm to "reroute" previously committed flow, correcting suboptimal early choices.

A **cut** is a partition of vertices into two sets S (containing s) and T (containing t). The **capacity** of a cut is the total capacity of edges going from S to T (forward edges only; backward edges don't count). Any cut capacity gives an upper bound on the flow: you cannot push more flow from s to t than can cross any dividing line. The **Max-Flow Min-Cut Theorem** is the deep result: the maximum flow value exactly equals the minimum cut capacity. When Ford-Fulkerson terminates — no augmenting path remains — the vertices reachable from s in the residual graph form one side of a minimum cut. The equality is not just a bound; it is tight.

The theorem is a celebrated example of a **min-max duality**: a maximization problem (max flow) equals a minimization problem (min cut). This pattern appears throughout combinatorics and optimization. Immediate applications include maximum bipartite matching (via a flow construction), the maximum number of edge-disjoint paths between two vertices (equal to the min cut, by Menger's theorem), and resource scheduling problems where bottlenecks are cuts. Whenever you have a system where something flows through a network with capacity limits, the max-flow min-cut theorem tells you exactly where the bottleneck is.
