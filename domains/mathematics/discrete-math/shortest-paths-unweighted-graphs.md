---
id: shortest-paths-unweighted-graphs
title: Shortest Paths in Unweighted Graphs
domain: mathematics
course: discrete-math
prerequisites:
- id: breadth-first-search-graphs
  type: hard
builds-toward:
- dijkstra-algorithm
tags:
- shortest-paths
- graph-algorithms
stage: formal-systems
status: draft
---

# Shortest Paths in Unweighted Graphs

## Core Idea
In unweighted graphs, the shortest path between two vertices is the one with fewest edges. BFS directly computes shortest paths by tracking distances and parent pointers. This is the foundation for understanding shortest-path problems in more complex settings.

## Explainer

You already know how BFS works: it explores a graph level by level, starting from a source vertex and visiting all neighbors before moving on to their neighbors. The key insight here is that this "level by level" property is exactly what defines distance in an unweighted graph — the level at which BFS first visits a vertex equals its **shortest-path distance** from the source, measured in number of edges.

To compute shortest paths, augment BFS with two arrays: `dist[]` and `parent[]`. Initialize `dist[source] = 0` and all others to infinity. When BFS first visits a vertex v from vertex u, record `dist[v] = dist[u] + 1` and `parent[v] = u`. Since BFS visits vertices in non-decreasing order of distance, the first time it reaches any vertex v is always via a shortest path — any later arrival would be at equal or greater distance. To reconstruct the actual path from source to a target, follow the parent pointers backward from target to source and reverse the result.

The correctness argument rests on the **FIFO invariant** of the queue: all vertices at distance d are processed before any at distance d+1. When a vertex v is first dequeued, every possible shorter path has already been processed, and the parent pointer records the optimal route. This reasoning depends critically on all edges having equal weight. In a weighted graph, BFS fails because a long sequence of cheap edges might produce a shorter total cost than a direct but expensive edge — equal edge counts do not imply equal costs. That gap motivates Dijkstra's algorithm, which generalizes BFS by replacing the FIFO queue with a priority queue.

The parent pointers produced by BFS form a **shortest path tree**: a subgraph rooted at the source where every root-to-leaf path is a shortest path in the original graph. This tree is not necessarily unique when multiple shortest paths exist, but every choice of parent pointers gives a valid one. BFS-based shortest paths solve a wide range of practical problems — minimum moves on a game board, degrees of separation in a social network, hops in a communication network — anywhere that edge count is the right measure of cost.
