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

## Questions

```yaml
- question: "Why is the first time BFS reaches a vertex guaranteed to be via the shortest path in terms of edge count?"
  type: multiple-choice
  options:
    - "BFS marks visited nodes, so it can't revisit them via longer paths"
    - "The FIFO queue ensures nodes are processed in order of increasing distance, so earlier-discovered nodes are always closer to the source than later ones"
    - "BFS uses backtracking to compare all possible routes before committing"
    - "BFS processes nodes by degree, naturally favoring shorter paths"
  answer: 1
  explanation: "The FIFO discipline of the queue is the key. Every vertex at distance d is enqueued before any vertex at distance d+1, because to reach d+1 you must first process a vertex at d. So when BFS dequeues a vertex, it has come from the front of the queue — from the closest frontier. The first time v is discovered, it was reached from the current closest frontier, so that path is minimal. Option A is true but doesn't explain *why* the first discovery is shortest — it's a consequence, not the cause."

- question: "In a weighted graph, A connects to B (weight 1) and A connects to C (weight 1). B connects directly to target T (weight 100). C connects to D (weight 1) and D connects to T (weight 1). BFS from A finds A→B→T as the shortest path. What does this reveal about BFS on weighted graphs?"
  type: multiple-choice
  options:
    - "BFS is correct; A→B→T uses the fewest edges (2 hops) so it is the shortest path"
    - "BFS optimizes for edge count, not cumulative weight — A→C→D→T has total weight 3 vs. A→B→T's total weight 101, showing BFS gives wrong answers when edge weights differ"
    - "BFS should have backtracked to discover A→C→D→T"
    - "BFS cannot run on graphs that have any edge weights at all"
  answer: 1
  explanation: "BFS finds the path with the fewest edges, treating each edge as having equal cost. Here A→B→T has 2 hops and total weight 101; A→C→D→T has 3 hops and total weight 3. BFS reports the 2-hop path as 'shortest' because it doesn't account for edge weights. In unweighted graphs (where every edge costs 1), fewest edges = lowest cost, so BFS is correct. In weighted graphs, these diverge and Dijkstra's algorithm — using a priority queue ordered by cumulative cost — is needed instead."

- question: "In BFS, when a vertex is first discovered, its distance from the source is finalized and will not be updated by any later discovery."
  type: true-false
  answer: true
  explanation: "Because BFS explores level by level, the first time vertex v is reached, it has been reached via the minimum number of edges. Any subsequent path to v would arrive at the same or greater distance. This is the property that makes BFS a correct shortest-path algorithm for unweighted graphs — no relaxation step is needed, unlike in Dijkstra's algorithm."

- question: "BFS finds shortest paths (by edge count) in both weighted and unweighted graphs, making Dijkstra's algorithm redundant for graphs where only path length in edges matters."
  type: true-false
  answer: false
  explanation: "The second half is true: if you only care about edge count (hops), BFS is sufficient and Dijkstra is unnecessary overhead. But the first claim — that BFS finds shortest paths in weighted graphs — is false. BFS minimizes edge count, which equals total cost only when all edges have identical weight. In weighted graphs, a path with more edges can have lower total weight, and BFS would miss it. Dijkstra handles weighted graphs; BFS is the special case where all weights are 1."

- question: "Why does BFS guarantee shortest paths in unweighted graphs but give incorrect results for weighted graphs? Explain the mechanism."
  type: short-answer
  answer: "In unweighted graphs, every edge costs 1, so minimizing edge count is identical to minimizing total path cost. BFS's FIFO queue processes vertices in order of hop count from the source — distance d before d+1 — so the first discovery of any vertex is always via the minimum number of edges, which is also the minimum cost path. In weighted graphs, a 2-hop path with large weights can be more expensive than a 3-hop path with small weights. BFS still finds the 2-hop path first and reports it as 'shortest,' but it's only shortest by edge count, not by total weight. Dijkstra's algorithm fixes this by using a priority queue ordered by cumulative cost, always expanding the vertex with the lowest total distance regardless of hop count."
  explanation: "The core insight is that BFS's level-by-level guarantee maps perfectly to 'shortest path' only when 'level' and 'cost' are the same thing — i.e., when every edge has cost 1. The moment edge costs differ, the level-by-level guarantee breaks down because you can 'jump levels' in cost by traversing an expensive edge."
```

## Explainer

From your study of breadth-first search, you know that BFS explores a graph by visiting all neighbors of the current node before moving deeper — processing vertices level by level using a queue. From your knowledge of queues, you understand the FIFO discipline that makes this possible. The key insight for shortest paths is that this level-by-level expansion is not just a traversal strategy — it is a **shortest-path algorithm** for unweighted graphs.

Here is why BFS finds shortest paths. When you start BFS from a source vertex s, you first discover all vertices exactly 1 edge away from s (level 1). Only after processing all of level 1 do you discover vertices 2 edges away (level 2), and so on. Because the queue is FIFO, a vertex discovered at level d is always processed before any vertex at level d+1. This means the **first time BFS reaches a vertex v, it has found the shortest path** from s to v — any later discovery of v would arrive via a longer path. You record the distance by setting `dist[v] = dist[u] + 1` when vertex v is first discovered from vertex u. To reconstruct the actual path, you also store `parent[v] = u`, then trace parent pointers backward from the destination to the source.

The implementation is straightforward. Initialize `dist[s] = 0` and `dist[v] = ∞` for all other vertices. Enqueue s. While the queue is not empty, dequeue a vertex u, and for each neighbor v of u: if `dist[v]` is still ∞ (unvisited), set `dist[v] = dist[u] + 1`, set `parent[v] = u`, and enqueue v. The algorithm visits every vertex and examines every edge exactly once, giving **O(V + E)** time — optimal since you must at least look at every edge to determine shortest paths.

It is critical to understand why this **only works for unweighted graphs** (or equivalently, graphs where every edge has the same weight). BFS assumes that each edge adds exactly 1 to the distance. If edges have different weights, a path with more edges might have a smaller total weight than a path with fewer edges — but BFS would report the fewer-edge path as "shorter" because it discovers that vertex first. For weighted graphs, you need **Dijkstra's algorithm**, which uses a priority queue to always process the vertex with the smallest *total distance* next, regardless of how many edges are on the path. BFS is a special case of Dijkstra where all edge weights equal 1, and the priority queue degenerates into a simple FIFO queue.
