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
