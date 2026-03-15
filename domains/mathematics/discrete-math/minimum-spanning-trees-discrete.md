---
id: minimum-spanning-trees-discrete
title: Minimum Spanning Trees and Algorithms
domain: mathematics
course: discrete-math
prerequisites:
- id: minimum-spanning-trees
  type: hard
- id: trees-and-tree-properties
  type: hard
builds-toward:
- graph-traversal-algorithms
tags:
- MST
- Kruskal
- Prim
- weighted-graphs
- optimization
stage: formal-systems
status: draft
---

# Minimum Spanning Trees and Algorithms

## Core Idea
A spanning tree of a connected graph includes all vertices using n−1 edges. A minimum spanning tree (MST) minimizes total edge weight. Kruskal's algorithm greedily adds edges in weight order; Prim's algorithm grows a tree vertex by vertex. Both yield optimal MSTs.

## How It's Best Learned
Implement or trace Kruskal's and Prim's algorithms on small weighted graphs. Understand why greedy works (matroid structure). Recognize applications: network design, clustering.

## Common Misconceptions
An MST is not necessarily unique (ties in edge weights yield different MSTs with equal cost). There is no single 'right' spanning tree for a given graph unless weights are specified.
