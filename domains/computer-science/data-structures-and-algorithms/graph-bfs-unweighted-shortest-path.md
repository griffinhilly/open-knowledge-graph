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

## Explainer

From your study of breadth-first search, you know that BFS explores a graph by visiting all neighbors of the current node before moving deeper — processing vertices level by level using a queue. From your knowledge of queues, you understand the FIFO discipline that makes this possible. The key insight for shortest paths is that this level-by-level expansion is not just a traversal strategy — it is a **shortest-path algorithm** for unweighted graphs.

Here is why BFS finds shortest paths. When you start BFS from a source vertex s, you first discover all vertices exactly 1 edge away from s (level 1). Only after processing all of level 1 do you discover vertices 2 edges away (level 2), and so on. Because the queue is FIFO, a vertex discovered at level d is always processed before any vertex at level d+1. This means the **first time BFS reaches a vertex v, it has found the shortest path** from s to v — any later discovery of v would arrive via a longer path. You record the distance by setting `dist[v] = dist[u] + 1` when vertex v is first discovered from vertex u. To reconstruct the actual path, you also store `parent[v] = u`, then trace parent pointers backward from the destination to the source.

The implementation is straightforward. Initialize `dist[s] = 0` and `dist[v] = ∞` for all other vertices. Enqueue s. While the queue is not empty, dequeue a vertex u, and for each neighbor v of u: if `dist[v]` is still ∞ (unvisited), set `dist[v] = dist[u] + 1`, set `parent[v] = u`, and enqueue v. The algorithm visits every vertex and examines every edge exactly once, giving **O(V + E)** time — optimal since you must at least look at every edge to determine shortest paths.

It is critical to understand why this **only works for unweighted graphs** (or equivalently, graphs where every edge has the same weight). BFS assumes that each edge adds exactly 1 to the distance. If edges have different weights, a path with more edges might have a smaller total weight than a path with fewer edges — but BFS would report the fewer-edge path as "shorter" because it discovers that vertex first. For weighted graphs, you need **Dijkstra's algorithm**, which uses a priority queue to always process the vertex with the smallest *total distance* next, regardless of how many edges are on the path. BFS is a special case of Dijkstra where all edge weights equal 1, and the priority queue degenerates into a simple FIFO queue.
