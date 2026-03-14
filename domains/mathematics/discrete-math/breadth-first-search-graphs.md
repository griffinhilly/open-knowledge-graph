---
id: breadth-first-search-graphs
title: Breadth-First Search (BFS)
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
- id: big-o-notation
  type: soft
builds-toward:
- shortest-paths-unweighted-graphs
tags:
- graph-algorithms
- traversal
- bfs
stage: formal-systems
status: draft
---

# Breadth-First Search (BFS)

## Core Idea
Breadth-first search systematically explores a graph level by level, visiting all neighbors of a vertex before moving deeper. BFS uses a queue to process vertices, runs in O(V+E) time, and finds shortest paths in unweighted graphs.
