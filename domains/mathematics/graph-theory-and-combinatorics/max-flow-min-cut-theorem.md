---
id: max-flow-min-cut-theorem
title: Max-Flow Min-Cut Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: network-flows
  type: hard
builds-toward:
- mengers-theorem
tags:
- graph-theory
- flows
- optimization
stage: abstract-reasoning
status: draft
---

# Max-Flow Min-Cut Theorem

## Core Idea
The Max-Flow Min-Cut Theorem states that the maximum flow from source to sink equals the minimum capacity of any cut separating them. This powerful result provides both a theoretical characterization and a practical algorithm for solving flow problems.

## How It's Best Learned
Work through small networks by hand, computing flows and cuts to see the equality in action. Use the Ford-Fulkerson method to incrementally build flows.

## Common Misconceptions
A cut's capacity is the sum of edge capacities crossing it, not the number of edges. Minimum cut is not the cut with fewest edges, but minimum total capacity.

## Explainer

From your study of network flows, you know that a **flow** assigns a value to each edge — respecting capacity constraints and conservation (flow in = flow out at every internal vertex). The value of a flow is the total amount leaving the source. You also know that you can push flow along augmenting paths to increase the total flow. The Max-Flow Min-Cut Theorem provides the theoretical foundation for why augmenting path algorithms actually find the maximum: they stop precisely when the flow equals the minimum cut.

A **cut** is a partition of all vertices into two sets: S, containing the source, and T, containing the sink. Every path from source to sink must cross from S to T at least once. The **capacity of the cut** is the total capacity of edges going from S to T (forward edges only — backward edges from T to S do not count). This immediately implies that any flow ≤ any cut capacity: the flow must pass through the cut's forward edges, and can never exceed their combined capacity. This "weak duality" is easy to see — any cut gives an upper bound on the maximum flow.

The remarkable result is that these two quantities are not just bounded together — they are **equal**: max flow = min cut. The proof uses the idea of residual capacity. When Ford-Fulkerson terminates (no augmenting paths remain), define S as all vertices reachable from the source in the residual graph. Then T = V \ S contains the sink (otherwise there would be an augmenting path). Every forward edge from S to T must be fully saturated (otherwise the endpoint in T would be reachable), and every backward edge from T to S must carry zero flow (otherwise the tail in S would be reachable). Therefore the current flow value exactly equals the capacity of the S-T cut — proving equality.

The theorem is one of the great duality results in combinatorics and optimization. It connects two seemingly different questions — "how much can flow from source to sink?" and "what is the bottleneck in the network?" — and shows they have the same answer. Applications are wide-ranging: maximum matching in bipartite graphs reduces to max-flow (finding the minimum vertex cover equals the maximum matching, by König's theorem, which is itself a consequence of max-flow min-cut). Network reliability, airline scheduling, image segmentation, and supply chain optimization all use this theorem. Whenever you want to maximize throughput through a constrained network, or find the minimum set of resources to disrupt a network, the Max-Flow Min-Cut Theorem is the underlying guarantee that your algorithm will find the exact answer.
