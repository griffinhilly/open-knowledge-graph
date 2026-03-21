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

## Questions

```yaml
- question: "Bellman-Ford performs V−1 relaxation passes over all edges. Why V−1 specifically?"
  type: multiple-choice
  options:
    - "Because there are at most V−1 distinct edge weights in any valid graph"
    - "Because any simple shortest path in a graph with V vertices contains at most V−1 edges, so V−1 passes guarantee all shortest paths are propagated correctly"
    - "Because the source vertex must be excluded from relaxation, leaving V−1 vertices to process"
    - "It is an empirical constant chosen to balance accuracy against runtime"
  answer: 1
  explanation: "In a graph with V vertices, any simple path (one without repeated vertices) can have at most V−1 edges. After one pass, all vertices reachable in exactly one hop have correct shortest-path estimates. After two passes, all vertices reachable in exactly two hops have correct estimates, and so on. After V−1 passes, every possible simple shortest path has been explored, regardless of the edge ordering. This is the structural guarantee that makes the algorithm correct — and it is why a V-th pass that still improves distances must indicate a negative cycle (requiring a path of infinite length to keep improving)."

- question: "After V−1 Bellman-Ford relaxation passes, you run one more pass and find that the distance to vertex w decreases. What does this tell you?"
  type: multiple-choice
  options:
    - "Vertex w has a negative-weight self-loop that must be removed before the algorithm can terminate"
    - "The algorithm has a bug; distances should never decrease after V−1 passes in a correct implementation"
    - "The graph contains a negative cycle reachable from the source, so no finite shortest path exists for vertices reachable from that cycle"
    - "Dijkstra's algorithm would solve this case more efficiently since Bellman-Ford has failed to converge"
  answer: 2
  explanation: "If all shortest paths were correctly computed after V−1 passes, a V-th pass cannot improve any distance — there is nothing left to relax. The only way a distance can still decrease is if there exists a cycle in the graph with total negative weight, meaning a path can be made arbitrarily short by traversing the cycle more times. This is the negative cycle detection step. For any vertex reachable from such a cycle, there is no well-defined shortest path because the 'path' can always be extended around the cycle to get shorter."

- question: "A graph with a negative cycle has no well-defined shortest path for vertices reachable from that cycle, because you can always reduce the path length further by traversing the cycle one more time."
  type: true-false
  answer: true
  explanation: "A negative cycle is a sequence of edges whose total weight is negative. If you can reach vertex t via a path that passes through such a cycle, you can make the path's total weight arbitrarily negative by going around the cycle additional times. There is no minimum — the infimum of path weights is −∞. This is why Bellman-Ford reports 'negative cycle detected' rather than a distance for such vertices, and why Dijkstra's algorithm cannot be trivially extended to handle this case."

- question: "Bellman-Ford is always slower than Dijkstra's algorithm in practice, making it a last resort only for graphs where negative-weight edges are unavoidable."
  type: true-false
  answer: false
  explanation: "Bellman-Ford's worst-case O(VE) is indeed worse than Dijkstra's O((V+E) log V) with a binary heap. But Bellman-Ford includes an important early-termination optimization: if no distance changes during an entire pass, all shortest paths are finalized and the algorithm exits immediately. On sparse graphs, graphs where all shortest paths are short, or when the graph has a special structure, Bellman-Ford may terminate in far fewer than V−1 passes and outperform Dijkstra. The statement 'always slower' is also incorrect for dense graphs where Dijkstra with a simple array runs in O(V²) while Bellman-Ford runs in O(VE)."

- question: "Why does Dijkstra's algorithm fail on graphs with negative-weight edges, and what specific property of Bellman-Ford allows it to handle them correctly?"
  type: short-answer
  answer: "Dijkstra's greedy strategy permanently finalizes the shortest-path estimate for the vertex with the smallest current distance at each step. This works because non-negative edge weights guarantee that no future path through unvisited vertices can produce a shorter route. With negative-weight edges, this guarantee fails: a vertex 'finalized' early could later be reached via a longer route that traverses a negative edge, yielding a shorter total distance. Dijkstra cannot revise finalized vertices, so it produces incorrect results. Bellman-Ford does not finalize vertices; it repeatedly relaxes all edges V−1 times, allowing distances to be updated in any order. This repeated relaxation ensures that even paths that 'zig-zag' through negative edges are eventually discovered correctly."
  explanation: "The root cause of Dijkstra's failure is the irrevocable greedy selection, which relies on the monotonicity property of non-negative weights. Bellman-Ford sacrifices that greedy efficiency in exchange for correctness under any weight distribution (except negative cycles, which have no solution by definition)."
```

## Explainer

You already know Dijkstra's algorithm, which finds shortest paths from a single source by greedily selecting the closest unvisited vertex and relaxing its edges. Dijkstra works beautifully — but it makes one critical assumption: all edge weights are non-negative. When a negative-weight edge exists, Dijkstra's greedy choice can be wrong, because visiting a vertex later via a negative edge might yield a shorter total path than the one Dijkstra already committed to. The **Bellman-Ford algorithm** solves shortest paths without this restriction, handling negative edge weights correctly at the cost of a slower running time.

The algorithm is conceptually simple. Initialize the distance to the source as 0 and all other vertices as infinity. Then, repeat the following V−1 times: for every edge (u, v) with weight w, check if `dist[u] + w < dist[v]`. If so, update `dist[v]` — this is called **relaxation**. Why V−1 iterations? Because the shortest path from the source to any vertex can contain at most V−1 edges (in a graph with V vertices and no negative cycles). After one iteration, you have correct distances for all vertices reachable in one hop. After two iterations, correct distances for vertices reachable in two hops. After V−1 iterations, every shortest path has been found.

The key advantage over Dijkstra is the **negative cycle detection**. After V−1 iterations, all shortest paths should be finalized. Run one more iteration — the Vth pass. If any distance decreases during this pass, a negative cycle exists: some loop in the graph has a total weight less than zero, meaning you could keep going around it forever, reducing the path length without bound. No finite shortest path exists for vertices reachable from such a cycle. This detection is valuable in practical applications like **currency arbitrage** (a negative cycle in a graph of exchange rates means a sequence of trades yields profit) and **difference constraint systems** (a negative cycle means the constraints are unsatisfiable).

The tradeoff is performance. Dijkstra's algorithm with a binary heap runs in O((V + E) log V), while Bellman-Ford runs in O(VE). On dense graphs this can be dramatically slower. However, an important optimization exists: if no distance changes during a complete pass, the algorithm can terminate early — all shortest paths are already correct. On sparse graphs or graphs where shortest paths are short, this optimization often makes Bellman-Ford finish well before V−1 iterations. In practice, reach for Dijkstra when all weights are non-negative, and switch to Bellman-Ford when negative weights appear or when you need to detect negative cycles.
