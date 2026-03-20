---
id: bellman-ford-negative-weight-paths
title: 'Bellman-Ford Algorithm: Shortest Paths with Negative Weights'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: dijkstras-algorithm
  type: hard
tags:
- shortest-paths
- algorithms
- negative-weights
stage: advanced
status: draft
---

# Bellman-Ford Algorithm: Shortest Paths with Negative Weights

## Core Idea
Bellman-Ford finds single-source shortest paths even with negative edge weights, running in O(VE) time. It relaxes all edges V-1 times; a Vth pass detecting a decreased distance indicates a negative cycle. Unlike Dijkstra, it cannot handle negative cycles gracefully but works on a broader class of graphs.

## How It's Best Learned
Implement Bellman-Ford and contrast with Dijkstra on graphs with negative weights. Observe the relaxation process and how the Vth pass detects negative cycles. Apply to currency arbitrage and difference constraints.

## Common Misconceptions
- Thinking Bellman-Ford is always slower; on sparse graphs with few edges, it can be faster than Dijkstra with binary heaps.
- Assuming negative weights are rare; they appear in many practical problems (e.g., cost/benefit models).
- Not detecting negative cycles; failing to do so yields incorrect shortest paths.

## Explainer

You already know Dijkstra's algorithm, which finds shortest paths from a single source by greedily selecting the closest unvisited vertex and relaxing its edges. Dijkstra works beautifully — but it makes one critical assumption: all edge weights are non-negative. When a negative-weight edge exists, Dijkstra's greedy choice can be wrong, because visiting a vertex later via a negative edge might yield a shorter total path than the one Dijkstra already committed to. The **Bellman-Ford algorithm** solves shortest paths without this restriction, handling negative edge weights correctly at the cost of a slower running time.

The algorithm is conceptually simple. Initialize the distance to the source as 0 and all other vertices as infinity. Then, repeat the following V−1 times: for every edge (u, v) with weight w, check if `dist[u] + w < dist[v]`. If so, update `dist[v]` — this is called **relaxation**. Why V−1 iterations? Because the shortest path from the source to any vertex can contain at most V−1 edges (in a graph with V vertices and no negative cycles). After one iteration, you have correct distances for all vertices reachable in one hop. After two iterations, correct distances for vertices reachable in two hops. After V−1 iterations, every shortest path has been found.

The key advantage over Dijkstra is the **negative cycle detection**. After V−1 iterations, all shortest paths should be finalized. Run one more iteration — the Vth pass. If any distance decreases during this pass, a negative cycle exists: some loop in the graph has a total weight less than zero, meaning you could keep going around it forever, reducing the path length without bound. No finite shortest path exists for vertices reachable from such a cycle. This detection is valuable in practical applications like **currency arbitrage** (a negative cycle in a graph of exchange rates means a sequence of trades yields profit) and **difference constraint systems** (a negative cycle means the constraints are unsatisfiable).

The tradeoff is performance. Dijkstra's algorithm with a binary heap runs in O((V + E) log V), while Bellman-Ford runs in O(VE). On dense graphs this can be dramatically slower. However, an important optimization exists: if no distance changes during a complete pass, the algorithm can terminate early — all shortest paths are already correct. On sparse graphs or graphs where shortest paths are short, this optimization often makes Bellman-Ford finish well before V−1 iterations. In practice, reach for Dijkstra when all weights are non-negative, and switch to Bellman-Ford when negative weights appear or when you need to detect negative cycles.
