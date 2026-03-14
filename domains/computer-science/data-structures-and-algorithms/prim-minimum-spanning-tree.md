---
id: prim-minimum-spanning-tree
title: Prim's Algorithm for Minimum Spanning Trees
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: heaps-and-priority-queues
  type: hard
- id: greedy-algorithms
  type: hard
tags:
- minimum-spanning-tree
- prim
- greedy
- priority-queue
- mst
stage: formal-systems
status: draft
---

# Prim's Algorithm for Minimum Spanning Trees

## Core Idea
Prim's algorithm builds an MST incrementally: start with a single vertex, then repeatedly add the minimum-weight edge connecting the tree to a non-tree vertex. With a priority queue, it runs in O((V + E) log V) time. Unlike Kruskal, it doesn't require sorting and is incremental, making it efficient for dense graphs.

## How It's Best Learned
Trace Prim's starting from different vertices; the MST is the same regardless. Implement using a priority queue, tracking the minimum outgoing edge from the tree. Compare time complexity: Prim with a min-heap suits dense graphs; Kruskal suits sparse graphs.

## Common Misconceptions
- Prim's is always better than Kruskal's (choice depends on graph density and edge-sorting overhead). - Vertex processing order matters (the greedy choice at each step is optimal regardless of order).
