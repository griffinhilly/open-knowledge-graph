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

## Questions

```yaml
- question: "After running Floyd-Warshall, you find dist[3][3] = −7. What does this indicate?"
  type: multiple-choice
  options:
    - "There is a bug — diagonal entries should always be 0 after initialization"
    - "Vertex 3 lies on a negative-weight cycle in the graph"
    - "The graph has a negative edge weight incident on vertex 3, but no cycle"
    - "The path from vertex 3 to itself found a shortcut through negative edges"
  answer: 1
  explanation: "A negative diagonal entry means Floyd-Warshall found a path from vertex 3 back to itself with total weight less than zero — exactly the definition of a negative-weight cycle through vertex 3. Traversing this cycle repeatedly makes any path through vertex 3 arbitrarily short, so shortest-path distances involving that vertex are undefined. Checking for negative diagonals after running the algorithm is the standard way to detect negative cycles."

- question: "For a dense graph with V = 500 vertices and E ≈ V² edges and non-negative weights, which is typically faster: Floyd-Warshall once, or Dijkstra V times with a binary heap?"
  type: multiple-choice
  options:
    - "Dijkstra V times is faster: O(V² log V + VE) simplifies to O(V³ log V), beating Floyd-Warshall's O(V³)"
    - "Floyd-Warshall is competitive or faster: Dijkstra V times costs O(V(E log V)) = O(V³ log V) for dense graphs, which exceeds O(V³)"
    - "They are exactly equal because E = O(V²) makes their complexities identical"
    - "Dijkstra is always faster because priority queues exploit sparse structure"
  answer: 1
  explanation: "For a dense graph where E ≈ V², running Dijkstra V times with a binary heap costs O(V · (E log V)) = O(V³ log V), which is asymptotically slower than Floyd-Warshall's O(V³). With a Fibonacci heap, Dijkstra V times achieves O(V(E + V log V)) = O(V³), matching Floyd-Warshall asymptotically — but Floyd-Warshall's three nested loops with a one-line update have small constants and are far simpler to implement correctly."

- question: "Floyd-Warshall produces incorrect shortest-path distances on graphs that contain negative-weight edges."
  type: true-false
  answer: false
  explanation: "Unlike Dijkstra's algorithm, Floyd-Warshall correctly handles negative-weight edges. Dijkstra's greedy assumption — that a settled vertex's distance is already finalized — breaks down with negative edges. Floyd-Warshall has no such assumption; its DP recurrence considers all possible intermediate vertices and is valid as long as no negative-weight cycle exists. The presence of negative edges alone does not invalidate the algorithm."

- question: "Floyd-Warshall can be implemented with a single in-place V×V matrix because updating dist[i][j] for intermediate k cannot corrupt the values dist[i][k] and dist[k][j] that the same iteration relies on."
  type: true-false
  answer: true
  explanation: "When processing intermediate k, the update is dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]). The key insight: dist[i][k] and dist[k][j] are not changed by any update in the same pass of k (since those updates only change dist[i][j] for arbitrary i and j, not for entries involving k as the destination). So the values used in the min computation remain correct throughout the entire k-th iteration, making in-place updates safe."

- question: "Explain the core DP subproblem that Floyd-Warshall solves and why iterating the outer loop over all possible intermediate vertices k yields correct all-pairs shortest paths."
  type: short-answer
  answer: "Define dist_k[i][j] as the shortest path from i to j using only vertices {0, ..., k} as intermediates. The recurrence is: dist_k[i][j] = min(dist_{k-1}[i][j], dist_{k-1}[i][k] + dist_{k-1}[k][j]). Either the optimal path uses vertex k as an intermediate (split at k, each half uses only {0..k-1}), or it doesn't (same as dist_{k-1}[i][j]). After iterating k from 0 to V-1, every vertex has been considered as a potential intermediate, so dist_{V-1}[i][j] is the true shortest path between all pairs."
  explanation: "Each iteration of the outer loop expands the set of allowed intermediates by one vertex. Starting from direct edges (no intermediates), the algorithm methodically asks: 'can I improve any path by routing through vertex k?' After all V vertices have been tried, no further improvement is possible — every indirect route has been considered."
```

## Explainer

You already know how Dijkstra's algorithm and Bellman-Ford find the shortest path from a single source to all other vertices. But what if you need the shortest path between *every* pair of vertices — not just from one source? You could run Dijkstra V times (once from each vertex), giving O(V² log V + VE) with a priority queue, or Bellman-Ford V times at O(V²E). **Floyd-Warshall** offers a cleaner approach: a single O(V³) algorithm that computes all-pairs shortest paths with remarkably simple code.

The algorithm maintains a V×V distance matrix, initially filled with direct edge weights (or infinity where no edge exists). It then considers each vertex k as a potential **intermediate node**. For every pair (i, j), it asks: "Is the path from i to j shorter if we route through k?" The update rule is `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`. The outer loop iterates over all possible intermediates k = 0 to V-1, and the two inner loops iterate over all pairs (i, j). After considering all intermediates, dist[i][j] holds the shortest-path distance for every pair.

The reason this works is a dynamic programming insight: define dist_k[i][j] as the shortest path from i to j using only vertices {0, 1, ..., k} as intermediates. Either the shortest path through vertices {0..k} uses vertex k — in which case it equals dist_{k-1}[i][k] + dist_{k-1}[k][j] — or it doesn't, in which case dist_k[i][j] = dist_{k-1}[i][j]. The recurrence is exactly the min of these two cases. Because the update for intermediate k only depends on the matrix from intermediate k-1, you can do this in-place with a single matrix rather than maintaining V separate copies.

Floyd-Warshall handles **negative edge weights** correctly, unlike Dijkstra, as long as no negative-weight cycle exists. You can even detect negative cycles: if after running the algorithm any diagonal entry dist[i][i] is negative, vertex i lies on a negative cycle. The algorithm's simplicity is its greatest practical strength — the entire implementation is three nested loops with a one-line update — making it easy to code, debug, and reason about. For dense graphs where E is close to V², it is competitive with running Dijkstra V times and far simpler to implement. For sparse graphs with non-negative weights, repeated Dijkstra is usually faster.
