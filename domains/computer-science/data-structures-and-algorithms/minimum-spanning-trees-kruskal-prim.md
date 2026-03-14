---
id: minimum-spanning-trees-kruskal-prim
title: 'Minimum Spanning Trees: Kruskal''s and Prim''s Algorithms'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: graph-adjacency-list-matrix-representations
  type: hard
- id: greedy-algorithms
  type: soft
- id: union-find
  type: soft
tags:
- mst
- kruskal
- prim
- greedy
stage: formal-systems
status: draft
---

# Minimum Spanning Trees: Kruskal's and Prim's Algorithms

## Core Idea
An MST connects all vertices with minimum total edge weight. Kruskal's uses union-find to add edges in sorted order, stopping at V-1 edges; Prim's grows the tree by always adding the cheapest edge leaving the current tree. Both run in O((V + E) log V) with efficient data structures.
