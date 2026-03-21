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

## Questions

```yaml
- question: "A weighted graph has two paths from vertex A to vertex B: one with 2 edges (total weight 100) and one with 5 edges (total weight 3). If you run BFS from A, which path does it find, and is this the shortest path?"
  type: multiple-choice
  options:
    - "BFS finds the 2-edge path; this is the shortest path by weight"
    - "BFS finds the 2-edge path because it minimizes edge count; this is NOT the shortest-weight path"
    - "BFS finds the 5-edge path because it has lower total weight"
    - "BFS cannot be applied to weighted graphs at all"
  answer: 1
  explanation: "BFS minimizes the number of edges, not total weight. It will find the 2-edge path (the fewest-edge path) and report a distance of 2. But the shortest path by weight is the 5-edge path with total weight 3. BFS is correct for unweighted graphs precisely because edge count = cost, but in weighted graphs this assumption breaks down. Any long sequence of cheap edges may beat a direct but expensive path, which is why Dijkstra's algorithm replaces the FIFO queue with a priority queue ordered by accumulated weight."

- question: "In an unweighted graph, BFS visits vertex V for the first time after processing 12 other vertices. What can you conclude about V's shortest-path distance from the source?"
  type: multiple-choice
  options:
    - "Nothing — BFS visiting order depends on the graph's adjacency list order, not distance"
    - "The distance is at most 12, but BFS does not guarantee it finds the shortest path on first visit"
    - "The distance equals the BFS level at which V was first discovered, and this IS the shortest-path distance"
    - "The distance is exactly 12, since V was the 12th vertex processed"
  answer: 2
  explanation: "BFS visits vertices in non-decreasing order of distance. The first time BFS reaches V, it does so via the shortest path — any later path to V would have equal or greater length (BFS would have already processed all shorter paths). The distance is recorded as dist[parent] + 1 at the moment of first discovery, and this value is exactly the shortest-path distance. The number of vertices processed before V (12) has no direct relationship to V's distance — it depends on graph structure."

- question: "In an unweighted graph, the first time BFS reaches a vertex is always via a shortest path from the source."
  type: true-false
  answer: true
  explanation: "This is the FIFO invariant: BFS processes all vertices at distance d before any at distance d+1. When vertex V is first discovered from vertex U, dist[V] = dist[U] + 1. Any alternative path to V of length dist[V] would have been discovered no earlier (same distance), and any shorter path would have been discovered first — but no shorter path exists, or BFS would have found V sooner. The first-arrival guarantee is what makes BFS produce correct shortest-path distances in unweighted graphs."

- question: "Running BFS from a source vertex and recording parent pointers produces a unique shortest-path tree."
  type: true-false
  answer: false
  explanation: "The parent pointers from BFS produce A shortest-path tree — one valid tree where every path from root to leaf is a shortest path — but not necessarily THE unique one. When multiple shortest paths of equal length exist between the source and a vertex, different adjacency-list orderings will cause BFS to record different parent pointers, producing different (but equally valid) shortest-path trees. The distances dist[v] are unique, but the tree structure depends on tie-breaking order."

- question: "Why does BFS correctly find shortest paths in unweighted graphs, and why does the same approach fail for weighted graphs?"
  type: short-answer
  answer: "In unweighted graphs, all edges cost 1, so path length equals edge count. BFS explores vertices in non-decreasing order of edge count (level by level via its FIFO queue), so when it first reaches any vertex, it has found the fewest-edge path — which is also the shortest path. In weighted graphs, edge count no longer equals path cost: a 5-edge path with total weight 3 beats a 1-edge path with weight 100. BFS's FIFO queue ignores weights entirely and would choose the 1-edge path. Dijkstra's algorithm fixes this by replacing the FIFO queue with a priority queue ordered by accumulated path cost, always extending the cheapest known path next."
  explanation: "The correctness of BFS rests on one assumption: all edges are equally costly. Under that assumption, 'explored earliest' is equivalent to 'reached most cheaply.' The moment you allow different edge weights, this equivalence breaks, and FIFO ordering no longer corresponds to distance ordering. This is the conceptual gap between BFS and Dijkstra — not a different algorithm structure, but a different queue discipline that respects path costs."
```

## Explainer

You already know how BFS works: it explores a graph level by level, starting from a source vertex and visiting all neighbors before moving on to their neighbors. The key insight here is that this "level by level" property is exactly what defines distance in an unweighted graph — the level at which BFS first visits a vertex equals its **shortest-path distance** from the source, measured in number of edges.

To compute shortest paths, augment BFS with two arrays: `dist[]` and `parent[]`. Initialize `dist[source] = 0` and all others to infinity. When BFS first visits a vertex v from vertex u, record `dist[v] = dist[u] + 1` and `parent[v] = u`. Since BFS visits vertices in non-decreasing order of distance, the first time it reaches any vertex v is always via a shortest path — any later arrival would be at equal or greater distance. To reconstruct the actual path from source to a target, follow the parent pointers backward from target to source and reverse the result.

The correctness argument rests on the **FIFO invariant** of the queue: all vertices at distance d are processed before any at distance d+1. When a vertex v is first dequeued, every possible shorter path has already been processed, and the parent pointer records the optimal route. This reasoning depends critically on all edges having equal weight. In a weighted graph, BFS fails because a long sequence of cheap edges might produce a shorter total cost than a direct but expensive edge — equal edge counts do not imply equal costs. That gap motivates Dijkstra's algorithm, which generalizes BFS by replacing the FIFO queue with a priority queue.

The parent pointers produced by BFS form a **shortest path tree**: a subgraph rooted at the source where every root-to-leaf path is a shortest path in the original graph. This tree is not necessarily unique when multiple shortest paths exist, but every choice of parent pointers gives a valid one. BFS-based shortest paths solve a wide range of practical problems — minimum moves on a game board, degrees of separation in a social network, hops in a communication network — anywhere that edge count is the right measure of cost.
