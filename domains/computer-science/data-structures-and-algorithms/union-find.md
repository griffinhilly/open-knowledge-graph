---
id: union-find
title: Union-Find (Disjoint Set Union)
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: amortized-analysis
  type: soft
- id: time-space-complexity
  type: soft
- id: equivalence-relations
  type: soft
tags:
- union-find
- disjoint-sets
- DSU
- connectivity
stage: formal-systems
status: draft
---

# Union-Find (Disjoint Set Union)

## Core Idea
Union-Find (Disjoint Set Union, DSU) tracks a collection of elements partitioned into disjoint sets, supporting union (merge two sets) and find (identify a set's representative). With two optimizations — union by rank and path compression — both operations run in nearly O(1) amortized time, formally O(α(n)) where α is the inverse Ackermann function, an astronomically slowly growing function. Union-Find is used to detect cycles in undirected graphs and is the core component of Kruskal's minimum spanning tree algorithm.

## How It's Best Learned
Implement union-find with a plain parent array first, then add union by rank, then path compression. Measure how the effective tree height changes with each optimization on large inputs.

## Common Misconceptions
- Path compression restructures the tree during find operations, but this does not affect correctness — only future query speed.
- The near-O(1) amortized bound requires BOTH union by rank AND path compression; either optimization alone gives a weaker guarantee.
