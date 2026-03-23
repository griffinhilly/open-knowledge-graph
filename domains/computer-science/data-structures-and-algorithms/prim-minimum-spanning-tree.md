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
status: validated
---

# Prim's Algorithm for Minimum Spanning Trees

## Core Idea
Prim's algorithm builds an MST incrementally: start with a single vertex, then repeatedly add the minimum-weight edge connecting the tree to a non-tree vertex. With a priority queue, it runs in O((V + E) log V) time. Unlike Kruskal, it doesn't require sorting and is incremental, making it efficient for dense graphs.

## How It's Best Learned
Trace Prim's starting from different vertices; the MST is the same regardless. Implement using a priority queue, tracking the minimum outgoing edge from the tree. Compare time complexity: Prim with a min-heap suits dense graphs; Kruskal suits sparse graphs.

## Common Misconceptions
- Prim's is always better than Kruskal's (choice depends on graph density and edge-sorting overhead). - Vertex processing order matters (the greedy choice at each step is optimal regardless of order).

## Questions

```yaml
- question: "You run Prim's algorithm on a weighted graph starting from vertex A and get an MST with total weight 47. Your colleague runs it starting from vertex D on the same graph. What can you conclude about the total weight of their MST?"
  type: multiple-choice
  options:
    - "Their MST will have a higher total weight because vertex D is farther from the center of the graph"
    - "Their MST will have the same total weight of 47, though the tree structure may differ if there are ties"
    - "Their MST will have a lower total weight because different starting vertices explore different edge sets"
    - "Nothing can be concluded without knowing the graph's edge weights"
  answer: 1
  explanation: "The cut property guarantees that Prim's algorithm always selects minimum-weight edges crossing the current cut, regardless of starting vertex. The result must be an MST — a tree spanning all vertices with minimum total weight. If the MST is unique (no weight ties), both runs produce identical trees. If ties exist, structures may differ but total weights remain equal. Starting vertex affects the order of exploration, not the optimality of the outcome."

- question: "A graph has 1,000 vertices and 400,000 edges (E ≈ 0.4 * V²). Which algorithm is generally preferred and why?"
  type: multiple-choice
  options:
    - "Kruskal's, because union-find makes it faster than any heap-based approach"
    - "Prim's with a min-heap, because Kruskal's upfront edge sorting is expensive for dense graphs"
    - "Kruskal's, because sparse graphs benefit from its incremental approach"
    - "Both perform identically on dense graphs; the choice is a matter of style"
  answer: 1
  explanation: "For dense graphs where E is close to V², Kruskal's algorithm must sort all E edges upfront — an O(E log E) cost that becomes very expensive. Prim's with a binary min-heap avoids sorting entirely: it incrementally processes edges through the heap at O((V + E) log V), which for dense graphs scales better in practice. Kruskal's is preferred for sparse graphs (E ≈ V) where the sorting overhead is modest."

- question: "In Prim's algorithm, the starting vertex you choose determines the total weight of the resulting MST."
  type: true-false
  answer: false
  explanation: "The starting vertex has no effect on the MST's total weight. This is a consequence of the cut property: at every step, Prim's picks the minimum-weight edge crossing the cut between tree and non-tree vertices. This greedy choice is always locally optimal regardless of which vertex you began from. The resulting MST (or one of equal total weight in case of ties) is the same. Starting vertex only affects the order in which vertices are visited."

- question: "Prim's algorithm is correct because the minimum-weight edge crossing any cut of the graph must belong to some MST."
  type: true-false
  answer: true
  explanation: "This is the cut property, which is the formal guarantee of Prim's correctness. At each step, Prim's considers the cut between vertices already in the tree and those not yet included. By always selecting the minimum-weight edge crossing this cut, it is guaranteed to select an edge that belongs to some MST. The property holds for any cut, which is why the starting vertex doesn't matter and why the greedy choice is always safe."

- question: "Why does Prim's algorithm guarantee a correct MST despite making purely local greedy choices at each step — never revisiting or adjusting previous decisions?"
  type: short-answer
  answer: "The cut property provides the correctness guarantee: for any partition of the graph's vertices into two sets, the minimum-weight edge crossing the partition must appear in some MST. At each step, Prim's creates exactly such a partition — tree vertices versus non-tree vertices — and selects the minimum crossing edge. Because this holds for any cut, and because Prim's always respects it, every edge added is provably an MST edge. No backtracking is needed because each greedy choice is globally safe, not just locally convenient."
  explanation: "This distinguishes Prim's from greedy algorithms that can get stuck. The cut property is a theorem about MSTs, not just a heuristic. It guarantees that the locally optimal choice (minimum crossing edge) is also globally optimal. The proof uses the exchange argument: if you replaced the minimum crossing edge with any heavier crossing edge, the resulting tree would have greater total weight — so the greedy choice can never make the MST worse."
```

## Explainer

A **minimum spanning tree** (MST) of a weighted, connected graph is a subset of edges that connects every vertex with the smallest possible total weight and forms no cycles. You already know from your study of greedy algorithms that a greedy strategy makes the locally optimal choice at each step, and from priority queues that you can efficiently extract the minimum element from a dynamic collection. Prim's algorithm combines both ideas: it grows the MST one edge at a time by always picking the cheapest edge that connects the tree built so far to a vertex not yet in the tree.

Here is the concrete procedure. Start by picking any vertex and adding it to the tree. Look at all edges leaving the tree and going to vertices outside the tree — these are the **frontier edges**. Pick the frontier edge with the smallest weight, add it and its endpoint to the tree, and update the frontier. Repeat until all vertices are included. The priority queue makes this efficient: instead of scanning all frontier edges each time, you maintain a min-heap keyed on edge weight. When you add a new vertex to the tree, you push its edges to non-tree neighbors into the heap. Each extraction gives you the next cheapest connection. With a binary min-heap, this yields O((V + E) log V) time — each of the E edges is inserted into and possibly extracted from the heap, and each operation costs O(log V).

The correctness of Prim's algorithm rests on the **cut property**: for any cut that divides the graph's vertices into two sets, the minimum-weight edge crossing the cut must belong to some MST. At every step, Prim's algorithm considers the cut between tree vertices and non-tree vertices, and it picks the minimum crossing edge — so it always selects an MST edge. This is why the starting vertex does not matter: regardless of where you begin, the greedy choices converge to the same MST (or one of equal total weight if ties exist).

Prim's algorithm is especially well-suited to **dense graphs** — graphs where E is close to V². In a dense graph, Kruskal's algorithm pays a heavy cost to sort all E edges upfront, while Prim's incrementally processes edges through the heap. Conversely, for sparse graphs where E is close to V, Kruskal's sorting overhead is modest and its union-find approach can be simpler. Understanding when to prefer each algorithm is a practical skill: Prim's with an adjacency list and a min-heap is the standard choice for dense weighted graphs, while Kruskal's with edge sorting and union-find is cleaner for sparse ones.
