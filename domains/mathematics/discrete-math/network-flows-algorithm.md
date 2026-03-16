---
id: network-flows-algorithm
title: 'Network Flows: Maximum Flow and Minimum Cut'
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-matching-halls-theorem
  type: soft
tags:
- graph-theory
- flows
stage: formal-systems
status: draft
---

# Network Flows: Maximum Flow and Minimum Cut

## Core Idea
In a flow network, edges have capacity constraints and carry flow values. A maximum flow is the largest total flow from source to sink. The max-flow min-cut theorem states that the maximum flow equals the minimum capacity of any cut separating source from sink.

## Explainer

Imagine water flowing through a network of pipes from a **source** (where water enters) to a **sink** (where it exits). Each pipe has a **capacity** — a maximum amount it can carry. You want to push as much total flow as possible from source to sink while respecting every capacity constraint. This is the maximum flow problem, and it sits at the intersection of graph theory, linear programming, and combinatorial optimization.

A **flow** assigns a non-negative value f(e) to each edge e, subject to two rules: (1) capacity constraints — f(e) ≤ cap(e) for every edge, and (2) flow conservation — for every internal node (not source or sink), the total flow in equals the total flow out. The **value** of a flow is the total amount leaving the source. The problem is to find a flow of maximum value. The algorithmic workhorse is **Ford-Fulkerson**: repeatedly find an **augmenting path** — a path from source to sink with remaining capacity on every edge — and push more flow along it. The process terminates when no augmenting path exists, at which point the flow is maximum. The **residual graph** tracks remaining capacity on forward edges and the possibility of "un-sending" flow on backward edges, which is what allows the algorithm to correct earlier suboptimal routing decisions.

The deep structural result is the **max-flow min-cut theorem**: the maximum value of any flow equals the minimum capacity of any **cut**. A cut is a partition of the vertices into two sets S (containing the source) and T (containing the sink); its capacity is the total capacity of edges going from S to T. Every cut imposes an upper bound on all flows (you can only send as much as crosses the cut), and the theorem says the tightest of these bounds is actually achievable. Ford-Fulkerson terminates precisely when it has found a flow equal to the minimum cut, providing a simultaneous certificate of optimality: here is the flow achieving the maximum, and here is the cut proving no larger flow is possible.

Network flow has immediate practical applications. If you've studied Hall's theorem for bipartite matching (your prerequisite), you can see bipartite matching as a special flow problem: add a source connected to all left vertices, connect all right vertices to a sink, and assign all edges capacity 1. A maximum matching corresponds exactly to a maximum flow, and Hall's condition corresponds to the min-cut condition. This unification is one of the most elegant aspects of combinatorial optimization — many seemingly different problems (matching, assignment, transportation, scheduling) are all instances of the same flow framework, and fast flow algorithms solve them all.
