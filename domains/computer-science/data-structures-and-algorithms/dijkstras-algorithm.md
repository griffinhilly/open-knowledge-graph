---
id: dijkstras-algorithm
title: Dijkstra's Algorithm
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: heaps-and-priority-queues
  type: hard
- id: breadth-first-search
  type: hard
- id: graph-adjacency-list-matrix-representations
  type: hard
- id: greedy-algorithms
  type: soft
- id: dijkstras-shortest-path-routing
  type: soft
- id: minimum-spanning-trees-kruskal-prim
  type: soft
- id: huffman-coding-optimal-prefixes
  type: soft
- id: greedy-activity-selection
  type: soft
builds-toward:
- bellman-ford-algorithm
tags:
- shortest-path
- Dijkstra
- weighted-graph
- greedy
stage: advanced
status: validated
---
# Dijkstra's Algorithm

## Core Idea
Dijkstra's algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights. It uses a greedy strategy with a priority queue: always extend the shortest known tentative path first. With a binary heap, the algorithm runs in O((V + E) log V). The algorithm maintains a distance array and relaxes edges by updating distances when a shorter path is discovered. It is the workhorse of navigation systems, network routing, and game AI pathfinding.

## How It's Best Learned
Implement Dijkstra's using Python's heapq module. Trace through a small weighted graph manually, tracking the priority queue state and distance table at each step. Add path reconstruction using a previous-node array.

## Common Misconceptions
- Dijkstra's fails with negative edge weights; use Bellman-Ford instead.
- The algorithm is greedy and correct because non-negative weights guarantee that once a node's shortest distance is finalized it cannot later be improved.
- With a Fibonacci heap the complexity improves to O(V log V + E), but binary heaps are used in practice due to simpler implementation.

## Questions

```yaml
- question: "Why does Dijkstra's algorithm produce incorrect results when the graph contains a negative edge weight?"
  type: multiple-choice
  options:
    - "The priority queue cannot store negative numbers."
    - "The algorithm may finalize a node's distance as shortest, but a later negative edge could provide an even shorter path to that node."
    - "Negative weights cause the algorithm to run forever in an infinite loop."
    - "The algorithm only works on trees, not graphs with cycles."
  answer: 1
  explanation: "Dijkstra's correctness relies on a key invariant: once a node is extracted from the priority queue (finalized), its tentative distance is already the true shortest distance and will never decrease. With non-negative weights, every subsequent path through an unvisited node can only be longer. A single negative edge breaks this: a finalized node could later be reached via a cheaper path using that negative edge, but the algorithm has already moved on."

- question: "Dijkstra's algorithm with a binary heap priority queue runs in O(V²) time."
  type: true-false
  answer: false
  explanation: "With a binary heap, Dijkstra's runs in O((V + E) log V) — each of the V node extractions and up to E edge relaxations costs O(log V) for the heap operation. O(V²) is the complexity of the naive array-based implementation where finding the minimum-distance unvisited node requires scanning all V nodes each time. The binary heap version is strictly better for sparse graphs where E << V²."

- question: "How does Dijkstra's algorithm differ from BFS, and when would you choose one over the other?"
  type: short-answer
  answer: "BFS finds shortest paths in unweighted graphs (or graphs where all edges have equal weight) by exploring nodes layer by layer. Dijkstra's generalizes this to weighted graphs by using a priority queue keyed on cumulative path cost rather than hop count. Use BFS when edges are unweighted or all equal — it is simpler and O(V + E). Use Dijkstra's when edge weights differ and are non-negative."
  explanation: "BFS's 'layer' structure is implicitly a priority queue ordered by hop count — each node is processed in the order it was first discovered, which corresponds to fewest edges. Dijkstra's replaces 'fewest edges' with 'minimum total weight' by swapping the queue for a min-heap. The algorithmic structure is nearly identical; only the ordering changes. This connection to BFS — which is a prerequisite — makes Dijkstra's feel like a natural extension rather than a new algorithm."
```

## Explainer

You already know BFS explores a graph level by level, finding the shortest path in terms of number of edges. Now suppose every edge has a different cost — a road map with varying distances, a network with different latencies. "Fewest hops" is no longer the right objective; you want "minimum total cost." Dijkstra's algorithm solves exactly this, and it extends BFS in the most natural way possible: replace the FIFO queue with a min-heap (priority queue) ordered by tentative path cost.

The algorithm maintains a **distance table**: `dist[v]` = the shortest path cost found so far from the source to vertex `v`. Initially, `dist[source] = 0` and all other distances are infinity. The priority queue holds `(cost, vertex)` pairs. At each step, you extract the vertex with the lowest tentative cost, then examine every edge from that vertex. For each neighbor, you compute the cost of reaching it through the current vertex (`dist[current] + edge_weight`). If this cost is less than the neighbor's current `dist` value, you **relax** the edge — update `dist[neighbor]` and push the improved `(new_cost, neighbor)` into the priority queue. Vertices that have been extracted from the queue are "finalized" and never revisited.

The algorithm's correctness depends entirely on one invariant: **once a vertex is extracted from the min-heap, its distance is final and optimal**. This is true only if all edge weights are non-negative. Why? When you extract the minimum-cost vertex, every path to it that hasn't been explored yet must pass through an unvisited vertex with equal or higher tentative cost. Because all remaining edges are non-negative, those unexplored paths can only get longer or stay the same — they can never sneak in and provide a shorter route to the already-finalized vertex. A single negative edge destroys this guarantee, which is why Dijkstra's fails in that case (Bellman-Ford handles negative weights instead).

The runtime is O((V + E) log V) with a binary heap. You perform V extractions (each O(log V)) and at most E relaxations (each involving a push or decrease-key, O(log V)). For dense graphs where E ≈ V², this is O(V² log V), actually worse than the naive O(V²) array implementation. Dijkstra's with a heap wins on sparse graphs — exactly the kind found in road networks and game maps, which is why it dominates in practice.

To reconstruct the actual shortest path (not just the distance), maintain a `prev` array alongside `dist`: when you relax an edge to neighbor `v` through vertex `u`, record `prev[v] = u`. After the algorithm finishes, walk backward from the destination following the `prev` pointers to recover the full path. This adds no asymptotic cost and turns Dijkstra's from a "find the cost" tool into a "find the route" tool.
