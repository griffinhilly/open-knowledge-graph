---
id: breadth-first-search
title: Breadth-First Search (BFS)
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: queues-data-structure
  type: hard
- id: graph-representation
  type: hard
- id: graph-theory-intro
  type: soft
- id: tree-traversals
  type: soft
builds-toward:
- dijkstras-algorithm
- topological-sort
tags:
- BFS
- graph-traversal
- shortest-path
- level-order
stage: formal-systems
status: validated
---
# Breadth-First Search (BFS)

## Core Idea
Breadth-first search (BFS) explores a graph layer by layer, visiting all neighbors of a node before moving deeper. It uses a queue and a visited set, running in O(V + E) time for V vertices and E edges. BFS finds the shortest path in terms of edge count between two nodes in an unweighted graph. It also determines connected components, checks bipartiteness, and forms the basis for Dijkstra's algorithm when extended to weighted graphs.

## How It's Best Learned
Implement BFS on both adjacency list and adjacency matrix representations. Trace through a small graph by hand showing the queue state at each step. Then add path reconstruction using a parent-pointer array.

## Common Misconceptions
- BFS finds shortest paths only in unweighted graphs; for weighted graphs, Dijkstra's algorithm is needed.
- The visited set must be marked before enqueuing a node, not after dequeuing, to prevent the same node from being added to the queue multiple times.
