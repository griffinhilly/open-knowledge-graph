---
id: minimum-spanning-trees-kruskal-prim
title: 'Minimum Spanning Trees: Kruskal''s and Prim''s Algorithms'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: graph-adjacency-list-matrix-representations
  type: hard
- id: greedy-algorithms
  type: soft
- id: union-find
  type: soft
tags:
- mst
- kruskal
- prim
- greedy
stage: formal-systems
status: validated
---

# Minimum Spanning Trees: Kruskal's and Prim's Algorithms

## Core Idea
An MST connects all vertices with minimum total edge weight. Kruskal's uses union-find to add edges in sorted order, stopping at V-1 edges; Prim's grows the tree by always adding the cheapest edge leaving the current tree. Both run in O((V + E) log V) with efficient data structures.

## Questions

```yaml
- question: "After running Kruskal's algorithm on a connected weighted graph, you notice it selected an edge that was NOT the globally lightest edge in the graph. Which statement best explains why this is still correct?"
  type: multiple-choice
  options:
    - "Kruskal's algorithm makes mistakes and may not produce a true MST"
    - "The cut property guarantees the cheapest edge crossing any partition must be in some MST, so skipping an edge due to cycle detection is always safe"
    - "Any spanning tree is an MST if it uses V-1 edges"
    - "The globally lightest edge was included earlier, so this selection is a replacement"
  answer: 1
  explanation: "Kruskal's skips an edge only when adding it would form a cycle — meaning both endpoints are already in the same component. The cut property guarantees that the cheapest edge crossing a valid cut (between two distinct components) is always safe to include. Skipping a cycle-forming edge doesn't violate this because that edge doesn't cross any relevant cut. The key is that Kruskal's considers every candidate edge in sorted order; the cut property justifies each acceptance."

- question: "Prim's algorithm and Dijkstra's algorithm look structurally similar — both use a priority queue and greedily select the minimum-cost next step. What is the key difference in what they are minimizing?"
  type: multiple-choice
  options:
    - "Prim's minimizes total path distance from the source; Dijkstra's minimizes tree weight"
    - "Prim's minimizes the weight of the single edge connecting a new vertex to the growing tree; Dijkstra's minimizes the cumulative path cost from the source"
    - "Prim's works on undirected graphs; Dijkstra's requires directed graphs"
    - "There is no meaningful difference — they produce the same result on the same graph"
  answer: 1
  explanation: "Dijkstra's stores cumulative distance from the source and updates nodes when a shorter total path is found. Prim's stores only the cost of the single cheapest edge connecting each unvisited node to the current tree — it ignores cumulative distance entirely. They can produce very different results: a cheap edge into a node that is far from the source is ideal for Prim's but irrelevant to Dijkstra's if a shorter cumulative path already exists."

- question: "An MST guarantees the shortest path between every pair of vertices in the graph."
  type: true-false
  answer: false
  explanation: "An MST minimizes the total weight of all edges used to connect the graph, but it does not guarantee shortest paths between pairs of vertices. The shortest path between two nodes may use edges not in the MST. MST optimizes a different objective — minimum total spanning weight — which is useful for network infrastructure but unrelated to point-to-point routing."

- question: "Kruskal's algorithm can produce a minimum spanning forest (rather than a single tree) if applied to a disconnected graph."
  type: true-false
  answer: true
  explanation: "A spanning forest is the natural extension of spanning trees to disconnected graphs — it contains one spanning tree per connected component. Kruskal's works identically whether the graph is connected or not: it adds the globally cheapest non-cycle-forming edge at each step, and the union-find structure naturally partitions into components. At termination, if the graph has k components, you have k trees. Prim's, by contrast, grows from a single starting vertex and will only find the MST of its connected component."

- question: "Explain why both Kruskal's and Prim's algorithms are guaranteed to produce a minimum spanning tree, despite using completely different strategies."
  type: short-answer
  answer: "Both algorithms are correct because they both respect the cut property: the lightest edge crossing any partition of vertices into two non-empty sets must belong to some MST. Kruskal's processes edges globally in sorted order, accepting each edge that doesn't form a cycle — each accepted edge is the lightest crossing the cut between its two endpoint components. Prim's grows the tree locally, always adding the cheapest edge from the current tree to a new vertex — this edge is the lightest crossing the cut between tree and non-tree vertices. In both cases, each greedy choice is justified by the cut property, ensuring the final result is globally optimal."
  explanation: "The cut property converts a greedy intuition ('take the cheapest thing available') into a provable guarantee. Without it, we couldn't know that locally cheap choices would sum to a globally optimal tree. The two algorithms exploit different cuts: Kruskal finds cuts between components, Prim finds cuts between the tree and the rest."
```

## Explainer

A **minimum spanning tree** (MST) is a subset of edges in a weighted, connected, undirected graph that connects every vertex with the smallest possible total edge weight, using exactly V − 1 edges and forming no cycles. Think of it as the cheapest possible network that keeps every node reachable from every other node — like finding the least expensive way to wire every house in a neighborhood to the power grid. The existence of an MST follows from the fact that any connected graph has at least one spanning tree, and among all spanning trees, at least one has minimum total weight.

Both Kruskal's and Prim's algorithms work because of a fundamental property called the **cut property**: for any partition of the vertices into two non-empty sets, the lightest edge crossing the cut must belong to some MST. This greedy insight means you can safely commit to cheap edges without worrying about painting yourself into a corner. **Kruskal's algorithm** exploits this globally: sort all edges by weight, then iterate through them in order, adding each edge to the MST unless it would create a cycle. You detect cycles using the union-find data structure you already know — if both endpoints are in the same component, skip the edge; otherwise, union their components. After accepting V − 1 edges, you are done. The runtime is dominated by sorting the edges: O(E log E), which is O(E log V) since E ≤ V².

**Prim's algorithm** takes a local, vertex-centered approach that mirrors Dijkstra's shortest-path algorithm in structure. Start from any vertex, and maintain a priority queue of edges leaving the current tree. Repeatedly extract the minimum-weight edge that connects a tree vertex to a non-tree vertex, add that vertex to the tree, and push its edges onto the queue. With a binary heap, this runs in O((V + E) log V). Prim's tends to perform better on dense graphs (where E is close to V²) especially with an adjacency matrix and a Fibonacci heap bringing the cost down to O(E + V log V), while Kruskal's is simpler and often faster on sparse graphs where sorting a small edge list is cheap.

The choice between the two algorithms is a practical engineering decision. Kruskal's naturally handles disconnected graphs (it produces a minimum spanning forest), works well when edges arrive in a stream, and pairs beautifully with union-find. Prim's is the better choice when the graph is dense or when you already have an adjacency list representation and a priority queue at hand. Both are greedy algorithms — they make locally optimal choices that happen to produce a globally optimal result, which is exactly the property that the cut property guarantees.
