---
id: graph-bfs-unweighted-shortest-path
title: Breadth-First Search for Shortest Paths in Unweighted Graphs
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: breadth-first-search
  type: hard
- id: queues-data-structure
  type: hard
- id: adjacency-list-representation
  type: soft
tags:
- bfs
- shortest-path
- unweighted
- level-by-level
- graph-traversal
stage: formal-systems
status: draft
---

# Breadth-First Search for Shortest Paths in Unweighted Graphs

## Core Idea
BFS explores a graph level-by-level from a source, visiting all neighbors before moving deeper. It naturally finds the shortest path (in edge count) in unweighted graphs because it discovers nodes in order of distance. The algorithm maintains a queue of frontier nodes and tracks visited nodes and distances, running in O(V + E) time.

## How It's Best Learned
Trace BFS by hand, level-by-level, on small graphs. Implement with a queue and distance array. Compare BFS to DFS (level-by-level vs. depth-first). Use BFS for connected components, shortest paths, reachability, and bipartiteness checking.

## Common Misconceptions
- BFS works on weighted graphs (it finds shortest paths only in unweighted; use Dijkstra for weighted). - Distances must be stored separately (you can reconstruct them from parent pointers).
