---
id: bipartite-graphs-matching
title: Bipartite Graphs and Matching Problems
domain: mathematics
course: discrete-math
prerequisites:
- id: bipartite-graphs
  type: hard
- id: graph-coloring-discrete
  type: soft
builds-toward:
- hamiltonian-cycles-discrete
tags:
- bipartite
- matching
- Hall's-theorem
- perfect-matching
stage: formal-systems
status: draft
---

# Bipartite Graphs and Matching Problems

## Core Idea
A bipartite graph has vertex partition into two sets with edges only between sets (not within). A matching is a set of disjoint edges. Hall's marriage theorem characterizes when a perfect matching (every vertex matched) exists in a bipartite graph.

## How It's Best Learned
Recognize bipartite graphs: they have no odd cycles. Use BFS/DFS to 2-color them. Apply Hall's theorem to prove existence of matchings. Model problems as bipartite matching: job assignments, system administrators, Latin rectangles.

## Common Misconceptions
A bipartite graph need not be complete bipartite. Hall's condition is necessary and sufficient: every subset S of one part must have at least |S| neighbors on the other side.
