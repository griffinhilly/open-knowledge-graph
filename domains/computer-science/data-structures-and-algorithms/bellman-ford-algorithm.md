---
id: bellman-ford-algorithm
title: Bellman-Ford Algorithm
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: graph-representation
  type: hard
- id: dijkstras-algorithm
  type: soft
- id: breadth-first-search
  type: soft
- id: graph-theory-intro
  type: soft
tags:
- shortest-path
- Bellman-Ford
- negative-weights
- negative-cycles
stage: advanced
status: validated
---

# Bellman-Ford Algorithm

## Core Idea
The Bellman-Ford algorithm finds shortest paths from a single source in a weighted graph, correctly handling negative edge weights. It relaxes all edges V−1 times; after these iterations, all shortest paths (assuming no negative cycles) are found. A V-th relaxation pass detects negative cycles: if any distance still decreases, a negative cycle is reachable from the source. Bellman-Ford runs in O(VE) time, slower than Dijkstra's but applicable to a broader class of graphs.

## How It's Best Learned
Implement Bellman-Ford on a graph with negative edge weights where Dijkstra's would fail. Trace through each round of edge relaxations to see how distances converge. Test negative cycle detection by introducing a cycle with negative total weight.

## Common Misconceptions
- Bellman-Ford handles negative weights correctly; it only fails on negative-weight cycles, where shortest paths are undefined.
- The V−1 bound on iterations comes from the fact that any shortest path without cycles visits at most V−1 edges.

## Explainer

If you've studied Dijkstra's algorithm, you know it finds shortest paths efficiently by always expanding the closest unvisited node — but it breaks when edge weights are negative, because its greedy assumption (once a node is finalized, its distance won't improve) no longer holds. **Bellman-Ford** solves this by taking a more patient approach: instead of making clever choices about which node to visit next, it simply relaxes every edge in the graph, over and over, until no more improvements are possible.

**Relaxation** is the core operation. For an edge from node *u* to node *v* with weight *w*, relaxation checks: is `distance[u] + w < distance[v]`? If so, we've found a shorter path to *v*, so we update `distance[v]`. One pass through all edges might improve some distances, which in turn enables further improvements in the next pass. The algorithm performs exactly **V−1 passes** over all edges, where V is the number of vertices. Why V−1? Because any shortest path in a graph without negative cycles visits at most V−1 edges (it passes through at most V vertices). After the first pass, all shortest paths of length 1 edge are correct. After the second pass, all paths of length 2 edges are correct. By the (V−1)th pass, even the longest possible shortest path has been discovered.

The algorithm's most distinctive feature is **negative cycle detection**. After V−1 passes, run one more pass over all edges. If any distance still decreases, it means the graph contains a cycle whose total weight is negative — and you can keep going around it to reduce the distance infinitely. Bellman-Ford reports this explicitly, which is valuable in applications like currency arbitrage detection (where a negative cycle in an exchange-rate graph means you can trade in a circle and end up with more money than you started with). Dijkstra's algorithm has no mechanism for this detection.

The tradeoff is speed. Bellman-Ford runs in **O(VE)** time — for each of V−1 iterations, it examines all E edges. On dense graphs (where E approaches V²), this becomes O(V³), significantly slower than Dijkstra's O((V+E) log V) with a priority queue. In practice, Bellman-Ford is the right choice when negative weights are present, when you need negative cycle detection, or when the graph is represented as an edge list (since the algorithm iterates over edges rather than expanding from nodes). It also forms the theoretical basis for distance-vector routing protocols like RIP, where each router independently runs a distributed version of this same iterative relaxation process.
