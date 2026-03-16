---
id: floyd-warshall-all-pairs-shortest-path
title: Floyd-Warshall Algorithm for All-Pairs Shortest Paths
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dynamic-programming-intro
  type: hard
- id: dijkstras-algorithm
  type: soft
tags:
- shortest-path
- all-pairs
- dynamic-programming
- negative-weights
- transitive-closure
stage: formal-systems
status: draft
---

# Floyd-Warshall Algorithm for All-Pairs Shortest Paths

## Core Idea
Floyd-Warshall computes shortest paths between all pairs of vertices in O(V³) time and O(V²) space using dynamic programming. It iterates through intermediate vertices k, updating distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]). Unlike Dijkstra, it handles negative-weight edges (but not negative cycles) and is simple to implement.

## How It's Best Learned
Trace the algorithm on a small graph, layer-by-layer through intermediate vertices k. Understand the recurrence relation and why the triple-nested loop works. Detect negative cycles by checking the diagonal. Compare to running Dijkstra V times.

## Common Misconceptions
- Floyd-Warshall is always optimal (O(V³) is high; Dijkstra from all sources can be faster for sparse graphs). - It handles negative cycles (it detects them but doesn't fix them; shortest paths are undefined in their presence).

## Explainer

You know Dijkstra's algorithm finds the shortest path from one source to all other vertices. But what if you need the shortest path between *every* pair of vertices — not just from one source, but from all of them? You could run Dijkstra V times (once from each vertex), but the **Floyd-Warshall algorithm** offers an elegant alternative built on dynamic programming, which you have already studied.

The algorithm maintains a V×V matrix `dist[i][j]` representing the best known distance from vertex i to vertex j. Initially, `dist[i][j]` is the weight of the direct edge from i to j (or infinity if no edge exists), and `dist[i][i]` is 0. Then comes the key insight: Floyd-Warshall iterates through every vertex k as a potential **intermediate vertex** and asks a simple question for every pair (i, j): "Is it shorter to go from i to j through k?" If `dist[i][k] + dist[k][j] < dist[i][j]`, then yes — update the distance. After considering all V possible intermediate vertices, the matrix contains the shortest path between every pair.

The recurrence relation makes this precise: `dist_k[i][j] = min(dist_{k-1}[i][j], dist_{k-1}[i][k] + dist_{k-1}[k][j])`, where the subscript k means "using only vertices 1 through k as intermediates." This is classic dynamic programming — building the solution by expanding the set of allowed intermediate vertices one at a time. The implementation is famously compact: three nested loops (for k, then i, then j), a single comparison, and a conditional update. The order of the loops matters — **k must be the outermost loop** — because each layer builds on the previous one.

A major advantage over Dijkstra is that Floyd-Warshall handles **negative-weight edges** correctly. Dijkstra's greedy strategy breaks when edges can be negative, but Floyd-Warshall's exhaustive dynamic programming approach works fine — it simply tries all intermediate paths and keeps the minimum. The one thing it cannot handle is **negative-weight cycles** (a cycle whose edge weights sum to a negative number), because you could traverse such a cycle infinitely to reduce the path length without bound. You can detect negative cycles by checking the diagonal of the result matrix: if any `dist[i][i] < 0`, vertex i is part of a negative cycle. The algorithm runs in O(V³) time and O(V²) space regardless of the number of edges, which makes it ideal for dense graphs but potentially wasteful for sparse ones where running Dijkstra from each vertex (with a priority queue) would be faster.
