---
id: turan-theorem
title: Turán's Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: formal-definitions-graph-theory
  type: hard
builds-toward:
- extremal-graph-theory
- probabilistic-method-graphs
tags:
- turan-theorem
- extremal-graphs
- clique-free
stage: formal-systems
status: draft
---

# Turán's Theorem

## Core Idea
Turán's theorem characterizes the densest K_r-free graph on n vertices: the Turán graph T(n,r−1), a complete (r−1)-partite graph. This foundational result in extremal graph theory provides the edge-count upper bound ex(n, K_r) = |E(T(n,r−1))|.

## How It's Best Learned
Construct the Turán graph T(n,r−1) explicitly for small n and r, verifying it is K_r-free and counting its edges. Apply the theorem to find upper bounds on edge density in forbidden-subgraph problems.

## Common Misconceptions
- Thinking the Turán graph is unique; it is, but understanding why is non-trivial.
- Assuming Turán's bound applies to forbidden subgraphs beyond cliques without modification (it generalizes, but requires care).
