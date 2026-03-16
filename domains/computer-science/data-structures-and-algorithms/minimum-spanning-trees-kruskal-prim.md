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
status: draft
---

# Minimum Spanning Trees: Kruskal's and Prim's Algorithms

## Core Idea
An MST connects all vertices with minimum total edge weight. Kruskal's uses union-find to add edges in sorted order, stopping at V-1 edges; Prim's grows the tree by always adding the cheapest edge leaving the current tree. Both run in O((V + E) log V) with efficient data structures.

## Explainer

A **minimum spanning tree** (MST) is a subset of edges in a weighted, connected, undirected graph that connects every vertex with the smallest possible total edge weight, using exactly V − 1 edges and forming no cycles. Think of it as the cheapest possible network that keeps every node reachable from every other node — like finding the least expensive way to wire every house in a neighborhood to the power grid. The existence of an MST follows from the fact that any connected graph has at least one spanning tree, and among all spanning trees, at least one has minimum total weight.

Both Kruskal's and Prim's algorithms work because of a fundamental property called the **cut property**: for any partition of the vertices into two non-empty sets, the lightest edge crossing the cut must belong to some MST. This greedy insight means you can safely commit to cheap edges without worrying about painting yourself into a corner. **Kruskal's algorithm** exploits this globally: sort all edges by weight, then iterate through them in order, adding each edge to the MST unless it would create a cycle. You detect cycles using the union-find data structure you already know — if both endpoints are in the same component, skip the edge; otherwise, union their components. After accepting V − 1 edges, you are done. The runtime is dominated by sorting the edges: O(E log E), which is O(E log V) since E ≤ V².

**Prim's algorithm** takes a local, vertex-centered approach that mirrors Dijkstra's shortest-path algorithm in structure. Start from any vertex, and maintain a priority queue of edges leaving the current tree. Repeatedly extract the minimum-weight edge that connects a tree vertex to a non-tree vertex, add that vertex to the tree, and push its edges onto the queue. With a binary heap, this runs in O((V + E) log V). Prim's tends to perform better on dense graphs (where E is close to V²) especially with an adjacency matrix and a Fibonacci heap bringing the cost down to O(E + V log V), while Kruskal's is simpler and often faster on sparse graphs where sorting a small edge list is cheap.

The choice between the two algorithms is a practical engineering decision. Kruskal's naturally handles disconnected graphs (it produces a minimum spanning forest), works well when edges arrive in a stream, and pairs beautifully with union-find. Prim's is the better choice when the graph is dense or when you already have an adjacency list representation and a priority queue at hand. Both are greedy algorithms — they make locally optimal choices that happen to produce a globally optimal result, which is exactly the property that the cut property guarantees.
