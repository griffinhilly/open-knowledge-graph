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

## Explainer

You already know the mechanics of **depth-first search** and **breadth-first search** individually. This topic is about understanding them together — their structural differences, what each one reveals about a graph, and when to reach for one versus the other.

The key distinction is the data structure each algorithm uses to decide which vertex to explore next. DFS uses a stack (or the call stack via recursion): push neighbors, pop the most recent, explore it, repeat. This sends the search diving deep before it backtracks. BFS uses a queue: push neighbors, dequeue the oldest, explore it, repeat. This sends the search spreading outward one layer at a time, like ripples from a stone dropped in water. The same logic, two different data structures, two completely different exploration patterns.

Both algorithms produce a **spanning tree** of the reachable portion of the graph. But the shape of that tree differs. A DFS spanning tree tends to be tall and thin — the algorithm follows long chains before backtracking. A BFS spanning tree tends to be short and wide — all vertices at distance 1 are found before any at distance 2. This is why BFS gives you **shortest paths** in unweighted graphs: every vertex is first discovered via the shortest possible route from the source. DFS makes no such guarantee.

DFS reveals something BFS cannot: **back-edges**. When DFS revisits a vertex that is still on the current recursion stack (marked "in progress"), it has found a back-edge — an edge that points backward in the DFS tree, closing a loop. Back-edges are exactly how you detect cycles in a graph using DFS. BFS, exploring layer by layer, can detect cross-edges between already-visited vertices, but it does not naturally expose cycle structure the same way. This connects directly to topological sorting and DAG detection: run DFS, check for back-edges. If none exist, the graph is acyclic and the reverse finish-time order is a valid topological ordering.

A practical summary: use **BFS** when you need shortest paths (in unweighted graphs) or want to explore a graph level by level. Use **DFS** when you need to detect cycles, produce a topological sort, find strongly connected components, or exhaustively enumerate paths. Both are linear-time O(V + E) — the difference is not efficiency but what structure each exposes.
