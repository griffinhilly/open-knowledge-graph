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
