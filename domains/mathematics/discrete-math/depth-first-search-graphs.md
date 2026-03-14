---
id: depth-first-search-graphs
title: Depth-First Search (DFS)
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
- id: big-o-notation
  type: soft
builds-toward:
- topological-sorting
- strongly-connected-components
- cycle-detection-directed-graphs
tags:
- graph-algorithms
- traversal
- dfs
stage: formal-systems
status: draft
---

# Depth-First Search (DFS)

## Core Idea
Depth-first search systematically explores a graph by going as deep as possible before backtracking. Starting from a source vertex, DFS visits adjacent unvisited vertices recursively, generating a DFS tree. It runs in O(V+E) time and is fundamental to many graph algorithms.

## How It's Best Learned
Trace DFS by hand on small graphs, maintaining a stack of vertices to visit. Observe how DFS discovers edges as tree edges, back edges, and cross edges in directed graphs.

## Common Misconceptions
- Confusing the DFS tree with the original graph structure. - Assuming DFS always finds the shortest path, which is true only for unweighted graphs in BFS.
