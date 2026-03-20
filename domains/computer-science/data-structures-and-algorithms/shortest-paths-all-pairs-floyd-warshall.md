---
id: shortest-paths-all-pairs-floyd-warshall
title: 'All-Pairs Shortest Paths: Floyd-Warshall Algorithm'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dijkstras-algorithm
  type: soft
- id: bellman-ford-algorithm
  type: soft
- id: divide-and-conquer-strategy
  type: soft
tags:
- shortest-path
- all-pairs
- dynamic-programming
stage: advanced
status: draft
---

# All-Pairs Shortest Paths: Floyd-Warshall Algorithm

## Core Idea
Floyd-Warshall solves all-pairs shortest paths in O(V³) time using dynamic programming: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) for all k. It works on graphs with negative edges (but no negative cycles) and is simpler to code than running Dijkstra V times.

## Explainer

You already know how Dijkstra's algorithm and Bellman-Ford find the shortest path from a single source to all other vertices. But what if you need the shortest path between *every* pair of vertices — not just from one source? You could run Dijkstra V times (once from each vertex), giving O(V² log V + VE) with a priority queue, or Bellman-Ford V times at O(V²E). **Floyd-Warshall** offers a cleaner approach: a single O(V³) algorithm that computes all-pairs shortest paths with remarkably simple code.

The algorithm maintains a V×V distance matrix, initially filled with direct edge weights (or infinity where no edge exists). It then considers each vertex k as a potential **intermediate node**. For every pair (i, j), it asks: "Is the path from i to j shorter if we route through k?" The update rule is `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`. The outer loop iterates over all possible intermediates k = 0 to V-1, and the two inner loops iterate over all pairs (i, j). After considering all intermediates, dist[i][j] holds the shortest-path distance for every pair.

The reason this works is a dynamic programming insight: define dist_k[i][j] as the shortest path from i to j using only vertices {0, 1, ..., k} as intermediates. Either the shortest path through vertices {0..k} uses vertex k — in which case it equals dist_{k-1}[i][k] + dist_{k-1}[k][j] — or it doesn't, in which case dist_k[i][j] = dist_{k-1}[i][j]. The recurrence is exactly the min of these two cases. Because the update for intermediate k only depends on the matrix from intermediate k-1, you can do this in-place with a single matrix rather than maintaining V separate copies.

Floyd-Warshall handles **negative edge weights** correctly, unlike Dijkstra, as long as no negative-weight cycle exists. You can even detect negative cycles: if after running the algorithm any diagonal entry dist[i][i] is negative, vertex i lies on a negative cycle. The algorithm's simplicity is its greatest practical strength — the entire implementation is three nested loops with a one-line update — making it easy to code, debug, and reason about. For dense graphs where E is close to V², it is competitive with running Dijkstra V times and far simpler to implement. For sparse graphs with non-negative weights, repeated Dijkstra is usually faster.
