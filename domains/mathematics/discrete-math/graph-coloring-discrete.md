---
id: graph-coloring-discrete
title: Graph Coloring and Chromatic Numbers
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-coloring
  type: hard
builds-toward:
- bipartite-graphs-matching
tags:
- coloring
- chromatic-number
- greedy-coloring
- bounds
stage: formal-systems
status: draft
---

# Graph Coloring and Chromatic Numbers

## Core Idea
A proper graph coloring assigns colors to vertices so adjacent vertices have different colors. The chromatic number χ(G) is the minimum colors needed. Computing χ(G) is NP-hard in general, but bounds exist: χ(G) ≤ Δ(G) + 1, where Δ is max degree.

## How It's Best Learned
Find the chromatic number of small graphs by hand. Implement a greedy coloring algorithm. Understand special cases: bipartite graphs have χ = 2; complete graphs have χ = n; cycles of odd length have χ = 3.

## Common Misconceptions
The four-color theorem applies to planar graphs, not all graphs. χ(G) = 2 iff G is bipartite (no odd cycles). Greedy coloring doesn't always find the optimal number.
