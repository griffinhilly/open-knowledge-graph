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

## Questions

```yaml
- question: "A developer uses Dijkstra's algorithm on a graph with mostly positive edge weights but a few negative ones. The algorithm sometimes returns incorrect shortest paths. What is the root cause?"
  type: multiple-choice
  options:
    - "Dijkstra's algorithm cannot handle directed edges, only undirected graphs"
    - "Dijkstra's greedy assumption — that once a node is finalized its shortest distance is permanent — breaks when negative weights allow a later-discovered path to improve an already-finalized distance"
    - "Dijkstra's priority queue cannot store negative distance values"
    - "Dijkstra requires exactly V-1 iterations; fewer edges in the path than V-1 causes it to terminate too early"
  answer: 1
  explanation: "Dijkstra's correctness relies on the guarantee that the shortest path to a node already processed will never improve. With all non-negative weights, this holds — a later path through unexplored nodes can only be longer. With negative weights, a path through an unvisited node might subtract enough weight to beat the already-finalized distance, invalidating the greedy approach entirely. Bellman-Ford avoids this by never finalizing distances — it keeps relaxing."

- question: "After running V-1 iterations of Bellman-Ford, you run one additional relaxation pass over all edges and find that the distance to node X decreases. What does this tell you?"
  type: multiple-choice
  options:
    - "The algorithm needed more iterations; V-1 was insufficient for this graph"
    - "The graph contains a negative-weight cycle reachable from the source — shortest paths in such graphs are undefined because you could loop around the cycle to reduce distance indefinitely"
    - "The edge weights were incorrectly specified and should be rechecked"
    - "The algorithm converged correctly; the decrease is due to floating-point rounding error"
  answer: 1
  explanation: "After V-1 iterations, all true shortest paths (assuming no negative cycles) have been found — because no simple path visits more than V-1 edges. If a distance still decreases in iteration V, it means some cycle with negative total weight is reachable and is being traversed, causing the distance to decrease without bound. This is Bellman-Ford's negative cycle detection mechanism, which Dijkstra lacks entirely."

- question: "Bellman-Ford requires exactly V-1 iterations because any shortest path in a graph without negative cycles uses at most V-1 edges."
  type: true-false
  answer: true
  explanation: "A simple path (one that doesn't revisit vertices) through a graph with V vertices visits at most V vertices, therefore uses at most V-1 edges. After k iterations of Bellman-Ford, all shortest paths that use at most k edges are correctly computed. So after V-1 iterations, the longest possible simple shortest path has been discovered. This bound is tight — a linear chain of V nodes has a shortest path of exactly V-1 edges."

- question: "Bellman-Ford can correctly report shortest-path distances in graphs with negative-weight cycles by flagging the affected nodes."
  type: true-false
  answer: false
  explanation: "When a negative-weight cycle is reachable from the source, shortest paths to nodes reachable via that cycle are undefined — you can keep traversing the cycle to reduce the distance without bound, so no finite minimum exists. Bellman-Ford detects that a negative cycle is present (by showing that distances continue to decrease after V-1 iterations) but cannot produce valid distance values for affected nodes. The algorithm reports the existence of a negative cycle; it does not produce meaningful distances."

- question: "Why does Bellman-Ford require exactly V-1 iterations, and what property of shortest paths justifies this bound?"
  type: short-answer
  answer: "Any shortest path in a graph without negative cycles is a simple path — it visits no vertex more than once (since revisiting a vertex with non-negative-weight cycles could only increase cost). A simple path through V vertices uses at most V-1 edges. After the kth Bellman-Ford iteration, all shortest paths using at most k edges are correct. Therefore V-1 iterations suffice to find all shortest paths, however long."
  explanation: "The V-1 bound is both an upper bound (no more is needed) and a tight bound (a linear chain of V nodes requires exactly V-1 iterations). This contrasts with Dijkstra, which processes each node once but requires non-negative weights. Bellman-Ford's patient, redundant approach is what lets it handle negative weights correctly."
```

## Explainer

If you've studied Dijkstra's algorithm, you know it finds shortest paths efficiently by always expanding the closest unvisited node — but it breaks when edge weights are negative, because its greedy assumption (once a node is finalized, its distance won't improve) no longer holds. **Bellman-Ford** solves this by taking a more patient approach: instead of making clever choices about which node to visit next, it simply relaxes every edge in the graph, over and over, until no more improvements are possible.

**Relaxation** is the core operation. For an edge from node *u* to node *v* with weight *w*, relaxation checks: is `distance[u] + w < distance[v]`? If so, we've found a shorter path to *v*, so we update `distance[v]`. One pass through all edges might improve some distances, which in turn enables further improvements in the next pass. The algorithm performs exactly **V−1 passes** over all edges, where V is the number of vertices. Why V−1? Because any shortest path in a graph without negative cycles visits at most V−1 edges (it passes through at most V vertices). After the first pass, all shortest paths of length 1 edge are correct. After the second pass, all paths of length 2 edges are correct. By the (V−1)th pass, even the longest possible shortest path has been discovered.

The algorithm's most distinctive feature is **negative cycle detection**. After V−1 passes, run one more pass over all edges. If any distance still decreases, it means the graph contains a cycle whose total weight is negative — and you can keep going around it to reduce the distance infinitely. Bellman-Ford reports this explicitly, which is valuable in applications like currency arbitrage detection (where a negative cycle in an exchange-rate graph means you can trade in a circle and end up with more money than you started with). Dijkstra's algorithm has no mechanism for this detection.

The tradeoff is speed. Bellman-Ford runs in **O(VE)** time — for each of V−1 iterations, it examines all E edges. On dense graphs (where E approaches V²), this becomes O(V³), significantly slower than Dijkstra's O((V+E) log V) with a priority queue. In practice, Bellman-Ford is the right choice when negative weights are present, when you need negative cycle detection, or when the graph is represented as an edge list (since the algorithm iterates over edges rather than expanding from nodes). It also forms the theoretical basis for distance-vector routing protocols like RIP, where each router independently runs a distributed version of this same iterative relaxation process.
