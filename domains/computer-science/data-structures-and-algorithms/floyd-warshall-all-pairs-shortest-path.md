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
stage: advanced
status: draft
---

# Floyd-Warshall Algorithm for All-Pairs Shortest Paths

## Core Idea
Floyd-Warshall computes shortest paths between all pairs of vertices in O(V³) time and O(V²) space using dynamic programming. It iterates through intermediate vertices k, updating distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]). Unlike Dijkstra, it handles negative-weight edges (but not negative cycles) and is simple to implement.

## How It's Best Learned
Trace the algorithm on a small graph, layer-by-layer through intermediate vertices k. Understand the recurrence relation and why the triple-nested loop works. Detect negative cycles by checking the diagonal. Compare to running Dijkstra V times.

## Common Misconceptions
- Floyd-Warshall is always optimal (O(V³) is high; Dijkstra from all sources can be faster for sparse graphs). - It handles negative cycles (it detects them but doesn't fix them; shortest paths are undefined in their presence).

## Questions

```yaml
- question: "In Floyd-Warshall's triple-nested loop, why must k (the intermediate vertex index) be the outermost loop?"
  type: multiple-choice
  options:
    - "Because the algorithm processes vertices in decreasing order of their weights, which requires k to be fixed first"
    - "Because updating dist[i][j] via intermediate vertex k requires that dist[i][k] and dist[k][j] already reflect the best paths using intermediates 1 through k-1 — the k dimension must be fully processed first"
    - "Because j must complete all updates before k can be incremented, and k controls the j-loop range"
    - "To avoid overwriting distance values needed for other pairs in the same pass of the i and j loops"
  answer: 1
  explanation: "This is the most important implementation detail. The recurrence is dist_k[i][j] = min(dist_{k-1}[i][j], dist_{k-1}[i][k] + dist_{k-1}[k][j]). When computing whether vertex k improves the path from i to j, the algorithm needs the best distances from i to k and from k to j using only intermediates 1..k-1 — values from the previous iteration of k. If k were an inner loop, it would be updating dist[i][k] and dist[k][j] while still using those values for other pairs in the same k-pass, violating the DP dependency structure. Making k outermost ensures each layer is fully computed before the next."

- question: "After running Floyd-Warshall, you check the result matrix and find that dist[5][5] = -8. What does this indicate?"
  type: multiple-choice
  options:
    - "Vertex 5 has a self-loop with weight -8 that was part of the input graph"
    - "The matrix was initialized incorrectly — dist[i][i] should always remain 0"
    - "Vertex 5 lies on a negative-weight cycle; the path from 5 back to itself can be made arbitrarily short"
    - "Floyd-Warshall detected that 5 is unreachable from itself and assigned a sentinel value"
  answer: 2
  explanation: "Initially, dist[i][i] = 0 for all i. During the algorithm, if a path from vertex i back to i can be improved (i.e., passes through a negative-weight cycle), the diagonal entry becomes negative. A negative value at dist[v][v] signals that v is on a negative-weight cycle. In such graphs, shortest paths are undefined for any pair (i,j) where a path between them passes through this cycle — you can loop it infinitely to reduce the cost without bound. The algorithm detects the cycle but cannot compute valid shortest paths in its presence."

- question: "Floyd-Warshall correctly computes shortest paths in graphs containing negative-weight edges, as long as no negative-weight cycles exist."
  type: true-false
  answer: true
  explanation: "This is a key advantage over Dijkstra's algorithm, which breaks on negative edges because its greedy strategy assumes that once a vertex is finalized, no shorter path exists — an assumption violated by negative edges. Floyd-Warshall uses exhaustive dynamic programming: it tries all combinations of intermediate vertices for every pair (i,j), so it correctly finds paths that become shorter by taking a detour through a negative-weight edge. Negative cycles are a different problem — they make shortest paths undefined (unbounded), and Floyd-Warshall detects them via the diagonal check but cannot produce valid distances."

- question: "For sparse graphs (few edges), Floyd-Warshall is generally faster than running Dijkstra's algorithm once from every vertex."
  type: true-false
  answer: false
  explanation: "Floyd-Warshall always runs in O(V³) time regardless of the number of edges. Dijkstra with a binary heap runs in O((V + E) log V) per source, so running it from all V sources costs O(V(V + E) log V). For sparse graphs where E ≪ V², this is much less than O(V³). For example, on a sparse graph with E = O(V), repeated Dijkstra costs O(V² log V) versus Floyd-Warshall's O(V³). Floyd-Warshall becomes competitive only for dense graphs (E ≈ V²), where its simplicity and constant factors make it practical, or when negative edges prevent Dijkstra from being used."

- question: "Explain the dynamic programming recurrence in Floyd-Warshall: what is dist_k[i][j], and why does progressively expanding the set of allowed intermediate vertices correctly compute all-pairs shortest paths?"
  type: short-answer
  answer: "dist_k[i][j] is the length of the shortest path from vertex i to vertex j using only vertices 1 through k as intermediate vertices. The recurrence is: dist_k[i][j] = min(dist_{k-1}[i][j], dist_{k-1}[i][k] + dist_{k-1}[k][j]). By starting with k=0 (direct edges only) and expanding to k=V, the algorithm considers every possible intermediate vertex exactly once, building optimal sub-paths into optimal full paths."
  explanation: "The DP insight is that any shortest path either does not pass through vertex k (so dist_{k-1}[i][j] is already optimal) or does pass through k (so it splits into two sub-paths, each using only intermediates 1..k-1, which have already been optimized). This exhaustive enumeration over intermediate vertex sets is what allows negative edges: unlike Dijkstra's greedy approach, there is no assumption that the nearest vertex is settled. Every pair is reconsidered at each expansion of k."
```

## Explainer

You know Dijkstra's algorithm finds the shortest path from one source to all other vertices. But what if you need the shortest path between *every* pair of vertices — not just from one source, but from all of them? You could run Dijkstra V times (once from each vertex), but the **Floyd-Warshall algorithm** offers an elegant alternative built on dynamic programming, which you have already studied.

The algorithm maintains a V×V matrix `dist[i][j]` representing the best known distance from vertex i to vertex j. Initially, `dist[i][j]` is the weight of the direct edge from i to j (or infinity if no edge exists), and `dist[i][i]` is 0. Then comes the key insight: Floyd-Warshall iterates through every vertex k as a potential **intermediate vertex** and asks a simple question for every pair (i, j): "Is it shorter to go from i to j through k?" If `dist[i][k] + dist[k][j] < dist[i][j]`, then yes — update the distance. After considering all V possible intermediate vertices, the matrix contains the shortest path between every pair.

The recurrence relation makes this precise: `dist_k[i][j] = min(dist_{k-1}[i][j], dist_{k-1}[i][k] + dist_{k-1}[k][j])`, where the subscript k means "using only vertices 1 through k as intermediates." This is classic dynamic programming — building the solution by expanding the set of allowed intermediate vertices one at a time. The implementation is famously compact: three nested loops (for k, then i, then j), a single comparison, and a conditional update. The order of the loops matters — **k must be the outermost loop** — because each layer builds on the previous one.

A major advantage over Dijkstra is that Floyd-Warshall handles **negative-weight edges** correctly. Dijkstra's greedy strategy breaks when edges can be negative, but Floyd-Warshall's exhaustive dynamic programming approach works fine — it simply tries all intermediate paths and keeps the minimum. The one thing it cannot handle is **negative-weight cycles** (a cycle whose edge weights sum to a negative number), because you could traverse such a cycle infinitely to reduce the path length without bound. You can detect negative cycles by checking the diagonal of the result matrix: if any `dist[i][i] < 0`, vertex i is part of a negative cycle. The algorithm runs in O(V³) time and O(V²) space regardless of the number of edges, which makes it ideal for dense graphs but potentially wasteful for sparse ones where running Dijkstra from each vertex (with a priority queue) would be faster.
