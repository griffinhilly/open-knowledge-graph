---
id: all-pairs-shortest-path-complexity
title: 'All-Pairs Shortest Paths: Floyd-Warshall Analysis'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: shortest-paths-all-pairs-floyd-warshall
  type: hard
tags:
- shortest-paths
- algorithms
- dynamic-programming
stage: formal-systems
status: draft
---

# All-Pairs Shortest Paths: Floyd-Warshall Analysis

## Core Idea
Floyd-Warshall solves all-pairs shortest paths in O(V³) time via dynamic programming. It works with negative weights and detects negative cycles. Although slower than running Dijkstra V times on sparse graphs, it's simpler and often preferred for small to medium-sized graphs.

## How It's Best Learned
Implement Floyd-Warshall and trace the DP recurrence D[k][i][j] = min(D[k-1][i][j], D[k-1][i][k] + D[k-1][k][j]). Compare performance and simplicity to running Bellman-Ford or Dijkstra multiple times.

## Common Misconceptions
- Assuming Floyd-Warshall is inefficient; O(V³) is acceptable for small graphs and offers elegance.
- Not recognizing the cache-friendly dense representation; it can beat sparse algorithms in practice.
- Forgetting that Floyd-Warshall extends naturally to detecting negative cycles and reconstructing paths.

## Explainer

From your study of Floyd-Warshall, you already know the algorithm and its recurrence: D[k][i][j] = min(D[k-1][i][j], D[k-1][i][k] + D[k-1][k][j]). Now let's examine *why* this runs in O(V³) and when that cost is actually a good deal compared to the alternatives.

The O(V³) bound comes directly from the structure of the algorithm: three nested loops, each iterating over V vertices. The outer loop considers each vertex k as a potential intermediate node, and the two inner loops examine every pair (i, j) to see if routing through k improves the shortest path. There is no way to skip iterations — every pair must be checked against every intermediate vertex — so the cubic bound is tight, not just an upper bound. Space-wise, you can optimize from O(V³) (storing a separate matrix for each k) down to O(V²) by updating the distance matrix in place, since the recurrence only depends on the current state of row k and column k, which remain unchanged when k is the intermediate vertex being considered.

How does O(V³) compare to alternatives? For all-pairs shortest paths, you could instead run a **single-source algorithm V times** — once from each vertex. Running Dijkstra V times with a binary heap gives O(V · (V + E) log V), which simplifies to O(V² log V) on sparse graphs (where E ≈ V) but becomes O(V³ log V) on dense graphs (where E ≈ V²). Running Bellman-Ford V times (necessary when edges have negative weights) gives O(V² · E), which is O(V⁴) on dense graphs. Floyd-Warshall's O(V³) beats both approaches on dense graphs, and its constant factors are small because the inner loop performs only a comparison and an addition on a contiguous matrix — highly **cache-friendly** operations.

The practical lesson is that Floyd-Warshall shines in a specific niche: small to medium-sized graphs (say, V < 1000), especially dense ones, and especially when negative edge weights are present. For large sparse graphs, running Dijkstra from each source with a priority queue will be faster. For large graphs with negative weights, Johnson's algorithm (which reweights edges using Bellman-Ford, then runs Dijkstra from each source) achieves O(V² log V + VE) — better than Floyd-Warshall when the graph is sparse. The elegance of Floyd-Warshall is that it requires no priority queue, no edge relaxation loop, and no special handling of graph representation — just three loops and a matrix. That simplicity makes it the right default for small dense graphs and a valuable baseline for understanding the all-pairs shortest path problem.
