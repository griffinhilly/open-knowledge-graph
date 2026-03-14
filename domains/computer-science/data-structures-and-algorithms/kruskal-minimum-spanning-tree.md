---
id: kruskal-minimum-spanning-tree
title: Kruskal's Algorithm for Minimum Spanning Trees
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: union-find
  type: hard
- id: greedy-algorithms
  type: hard
tags:
- minimum-spanning-tree
- kruskal
- greedy
- union-find
- mst
stage: formal-systems
status: draft
---

# Kruskal's Algorithm for Minimum Spanning Trees

## Core Idea
Kruskal's algorithm greedily builds an MST by sorting edges by weight and adding each edge if it doesn't create a cycle (detected via union-find). It runs in O(E log E) time and works on any connected weighted graph. The greedy choice is safe: every MST edge is the minimum-weight edge crossing some cut of the graph.

## How It's Best Learned
Trace the algorithm on a small graph: sort edges, add them, and use union-find to detect cycles. Understand why the greedy choice is optimal (cut property). Compare to Prim's: Kruskal is simpler but requires sorting; Prim is incremental.

## Common Misconceptions
- The MST is unique (unique only if all edge weights are distinct). - Union-find is required (any cycle-detection method works; union-find is just efficient).
