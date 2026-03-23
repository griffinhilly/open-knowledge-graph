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
stage: advanced
status: validated
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

## Questions

```yaml
- question: "A road network has V=400 cities and E=80,000 roads (a dense graph). Edge weights can be negative (representing subsidized routes). You need shortest paths between all city pairs. Which algorithm is the best choice?"
  type: multiple-choice
  options:
    - "Run Dijkstra from every vertex — it has the same asymptotic cost and is more widely understood"
    - "Run Bellman-Ford from every vertex — it handles negative weights correctly"
    - "Floyd-Warshall — O(V³) with simple matrix operations, handles negative weights, and beats V×Bellman-Ford on dense graphs"
    - "Johnson's algorithm — it is always optimal regardless of graph density"
  answer: 2
  explanation: "On a dense graph with negative weights, Floyd-Warshall is the right tool. Dijkstra cannot handle negative weights, so option A is incorrect. Bellman-Ford V times runs in O(V² × E) = O(V⁴) on a dense graph — far worse than Floyd-Warshall's O(V³). Johnson's algorithm is excellent for large sparse graphs but introduces overhead (one Bellman-Ford pass for reweighting) that's unnecessary when V is moderate. Floyd-Warshall's three nested loops on a contiguous matrix are cache-friendly and correct, making it the standard choice for small-to-medium dense graphs with potentially negative weights."

- question: "A social network has V=10,000 users and E=30,000 friendships (sparse, E ≈ 3V). All edge weights are non-negative. Which all-pairs shortest path approach has better asymptotic performance?"
  type: multiple-choice
  options:
    - "Floyd-Warshall — O(V³) is simple, cache-friendly, and always reliable"
    - "Running Dijkstra from each vertex with a binary heap — O(V·(V+E)·log V) = O(V² log V) for sparse graphs, beating O(V³)"
    - "Running Bellman-Ford from each vertex — correct and handles any weight distribution"
    - "Both Floyd-Warshall and Dijkstra have identical asymptotic performance on sparse graphs"
  answer: 1
  explanation: "When E ≈ V (sparse), running Dijkstra V times with a binary heap costs O(V·(V+E)·log V) = O(V·V·log V) = O(V² log V). Floyd-Warshall costs O(V³). For large V, V² log V ≪ V³, so Dijkstra wins on sparse graphs. Floyd-Warshall's advantage (no log factor, handles negative weights) only materializes on dense graphs where E ≈ V². The lesson: algorithm selection depends critically on graph density, not just problem type."

- question: "Floyd-Warshall's O(V³) time complexity is a tight bound — the three nested loops cannot be short-circuited, so the cubic cost is inherent to the algorithm's structure."
  type: true-false
  answer: true
  explanation: "Every pair (i, j) must be checked against every possible intermediate vertex k, because any vertex could be on the optimal path. There is no way to prune the k-loop or the i,j loops without risking missing the true shortest path. The O(V³) bound is therefore not a worst-case upper bound but an exact characterization — Floyd-Warshall always performs exactly V³ iterations of the inner comparison."

- question: "Floyd-Warshall is generally less practical than running Dijkstra V times because its O(V³) complexity is always worse."
  type: true-false
  answer: false
  explanation: "This is wrong in two ways. First, Floyd-Warshall beats V×Dijkstra on dense graphs: Dijkstra V times with a heap is O(V³ log V) when E ≈ V², which is worse than O(V³). Second, Floyd-Warshall handles negative-weight edges (unlike Dijkstra), making it the only option in that scenario without the overhead of Johnson's algorithm. Floyd-Warshall also has small constant factors due to simple cache-friendly array accesses. It is worse than V×Dijkstra only on sparse graphs with non-negative weights."

- question: "On what type of graph does Floyd-Warshall outperform running Dijkstra V times, and why?"
  type: short-answer
  answer: "Dense graphs (E ≈ V²). Running Dijkstra V times with a binary heap costs O(V·(V+E)·log V), which becomes O(V³ log V) when E ≈ V² — worse than Floyd-Warshall's O(V³) by a log V factor. Additionally, Floyd-Warshall handles negative-weight edges (which Dijkstra cannot), and its inner loop performs only a comparison and addition on a contiguous matrix, giving excellent cache performance with small constant factors."
  explanation: "The density threshold is roughly where E = Ω(V²/log V). Below that, V×Dijkstra wins; above it, Floyd-Warshall's simpler constant factor and lack of a log term tips the balance. For practical purposes: if you have a dense graph (adjacency matrix representation makes sense) and possibly negative weights, Floyd-Warshall is the default. For large sparse graphs with non-negative weights, V×Dijkstra is better; for large sparse graphs with negative weights, Johnson's algorithm is the right choice."
```

## Explainer

From your study of Floyd-Warshall, you already know the algorithm and its recurrence: D[k][i][j] = min(D[k-1][i][j], D[k-1][i][k] + D[k-1][k][j]). Now let's examine *why* this runs in O(V³) and when that cost is actually a good deal compared to the alternatives.

The O(V³) bound comes directly from the structure of the algorithm: three nested loops, each iterating over V vertices. The outer loop considers each vertex k as a potential intermediate node, and the two inner loops examine every pair (i, j) to see if routing through k improves the shortest path. There is no way to skip iterations — every pair must be checked against every intermediate vertex — so the cubic bound is tight, not just an upper bound. Space-wise, you can optimize from O(V³) (storing a separate matrix for each k) down to O(V²) by updating the distance matrix in place, since the recurrence only depends on the current state of row k and column k, which remain unchanged when k is the intermediate vertex being considered.

How does O(V³) compare to alternatives? For all-pairs shortest paths, you could instead run a **single-source algorithm V times** — once from each vertex. Running Dijkstra V times with a binary heap gives O(V · (V + E) log V), which simplifies to O(V² log V) on sparse graphs (where E ≈ V) but becomes O(V³ log V) on dense graphs (where E ≈ V²). Running Bellman-Ford V times (necessary when edges have negative weights) gives O(V² · E), which is O(V⁴) on dense graphs. Floyd-Warshall's O(V³) beats both approaches on dense graphs, and its constant factors are small because the inner loop performs only a comparison and an addition on a contiguous matrix — highly **cache-friendly** operations.

The practical lesson is that Floyd-Warshall shines in a specific niche: small to medium-sized graphs (say, V < 1000), especially dense ones, and especially when negative edge weights are present. For large sparse graphs, running Dijkstra from each source with a priority queue will be faster. For large graphs with negative weights, Johnson's algorithm (which reweights edges using Bellman-Ford, then runs Dijkstra from each source) achieves O(V² log V + VE) — better than Floyd-Warshall when the graph is sparse. The elegance of Floyd-Warshall is that it requires no priority queue, no edge relaxation loop, and no special handling of graph representation — just three loops and a matrix. That simplicity makes it the right default for small dense graphs and a valuable baseline for understanding the all-pairs shortest path problem.
