---
id: prim-minimum-spanning-tree
title: Prim's Algorithm for Minimum Spanning Trees
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: heaps-and-priority-queues
  type: hard
- id: greedy-algorithms
  type: hard
tags:
- minimum-spanning-tree
- prim
- greedy
- priority-queue
- mst
stage: formal-systems
status: draft
---

# Prim's Algorithm for Minimum Spanning Trees

## Core Idea
Prim's algorithm builds an MST incrementally: start with a single vertex, then repeatedly add the minimum-weight edge connecting the tree to a non-tree vertex. With a priority queue, it runs in O((V + E) log V) time. Unlike Kruskal, it doesn't require sorting and is incremental, making it efficient for dense graphs.

## How It's Best Learned
Trace Prim's starting from different vertices; the MST is the same regardless. Implement using a priority queue, tracking the minimum outgoing edge from the tree. Compare time complexity: Prim with a min-heap suits dense graphs; Kruskal suits sparse graphs.

## Common Misconceptions
- Prim's is always better than Kruskal's (choice depends on graph density and edge-sorting overhead). - Vertex processing order matters (the greedy choice at each step is optimal regardless of order).

## Explainer

A **minimum spanning tree** (MST) of a weighted, connected graph is a subset of edges that connects every vertex with the smallest possible total weight and forms no cycles. You already know from your study of greedy algorithms that a greedy strategy makes the locally optimal choice at each step, and from priority queues that you can efficiently extract the minimum element from a dynamic collection. Prim's algorithm combines both ideas: it grows the MST one edge at a time by always picking the cheapest edge that connects the tree built so far to a vertex not yet in the tree.

Here is the concrete procedure. Start by picking any vertex and adding it to the tree. Look at all edges leaving the tree and going to vertices outside the tree — these are the **frontier edges**. Pick the frontier edge with the smallest weight, add it and its endpoint to the tree, and update the frontier. Repeat until all vertices are included. The priority queue makes this efficient: instead of scanning all frontier edges each time, you maintain a min-heap keyed on edge weight. When you add a new vertex to the tree, you push its edges to non-tree neighbors into the heap. Each extraction gives you the next cheapest connection. With a binary min-heap, this yields O((V + E) log V) time — each of the E edges is inserted into and possibly extracted from the heap, and each operation costs O(log V).

The correctness of Prim's algorithm rests on the **cut property**: for any cut that divides the graph's vertices into two sets, the minimum-weight edge crossing the cut must belong to some MST. At every step, Prim's algorithm considers the cut between tree vertices and non-tree vertices, and it picks the minimum crossing edge — so it always selects an MST edge. This is why the starting vertex does not matter: regardless of where you begin, the greedy choices converge to the same MST (or one of equal total weight if ties exist).

Prim's algorithm is especially well-suited to **dense graphs** — graphs where E is close to V². In a dense graph, Kruskal's algorithm pays a heavy cost to sort all E edges upfront, while Prim's incrementally processes edges through the heap. Conversely, for sparse graphs where E is close to V, Kruskal's sorting overhead is modest and its union-find approach can be simpler. Understanding when to prefer each algorithm is a practical skill: Prim's with an adjacency list and a min-heap is the standard choice for dense weighted graphs, while Kruskal's with edge sorting and union-find is cleaner for sparse ones.
