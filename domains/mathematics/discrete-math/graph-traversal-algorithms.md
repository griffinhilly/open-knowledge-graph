---
id: graph-traversal-algorithms
title: 'Graph Traversal: Depth-First and Breadth-First Search'
domain: mathematics
course: discrete-math
prerequisites:
- id: depth-first-search-graphs
  type: hard
- id: breadth-first-search-graphs
  type: hard
builds-toward:
- graph-coloring-discrete
tags:
- DFS
- BFS
- traversal
- tree-edges
- back-edges
stage: formal-systems
status: draft
---

# Graph Traversal: Depth-First and Breadth-First Search

## Core Idea
Depth-first search (DFS) explores as far as possible along each branch (recursively), while breadth-first search (BFS) explores level-by-level using a queue. Both visit all reachable vertices, producing a spanning tree. DFS finds back-edges (identifying cycles); BFS finds shortest paths in unweighted graphs.

## How It's Best Learned
Trace DFS and BFS by hand on small graphs, noting discovery and finish times for DFS. Implement both iteratively. Recognize DFS orderings and topological sorting applications.

## Common Misconceptions
DFS can visit vertices in many different orders depending on starting vertex and edge order; BFS finds the shortest path in unweighted graphs, not weighted ones.
