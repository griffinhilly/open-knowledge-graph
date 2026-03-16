---
id: kruskal-minimum-spanning-tree
title: Kruskal's Algorithm for Minimum Spanning Trees
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: union-find
  type: hard
- id: greedy-algorithms
  type: hard
tags:
- minimum-spanning-tree
- kruskal
- greedy
- union-find
- mst
stage: formal-systems
status: draft
---

# Kruskal's Algorithm for Minimum Spanning Trees

## Core Idea
Kruskal's algorithm greedily builds an MST by sorting edges by weight and adding each edge if it doesn't create a cycle (detected via union-find). It runs in O(E log E) time and works on any connected weighted graph. The greedy choice is safe: every MST edge is the minimum-weight edge crossing some cut of the graph.

## How It's Best Learned
Trace the algorithm on a small graph: sort edges, add them, and use union-find to detect cycles. Understand why the greedy choice is optimal (cut property). Compare to Prim's: Kruskal is simpler but requires sorting; Prim is incremental.

## Common Misconceptions
- The MST is unique (unique only if all edge weights are distinct). - Union-find is required (any cycle-detection method works; union-find is just efficient).

## Explainer

You already know that greedy algorithms make locally optimal choices and that union-find efficiently tracks which elements belong to the same connected component. Kruskal's algorithm combines these two ideas into an elegant procedure for finding a **minimum spanning tree** (MST) — the subset of edges that connects every vertex in a weighted graph at the lowest possible total cost, without forming any cycles.

The algorithm works in three steps. First, sort all edges in the graph by weight from lightest to heaviest. Second, iterate through the sorted edges one at a time. For each edge, ask: "Would adding this edge create a cycle?" If no, add it to the growing tree. If yes, skip it. Third, stop when you have exactly V−1 edges (where V is the number of vertices), because any tree on V vertices has exactly V−1 edges. The cycle-detection question is where union-find earns its place — each vertex starts in its own set, adding an edge merges two sets, and an edge would create a cycle precisely when both its endpoints are already in the same set. With union-find using path compression and union by rank, each of these operations runs in nearly constant time.

Why does this greedy strategy actually produce the optimal tree? The answer rests on the **cut property**: for any partition of the vertices into two non-empty groups, the lightest edge crossing that partition must belong to some MST. Since Kruskal's considers edges lightest-first and only adds edges that connect previously disconnected components, every edge it adds is the lightest edge crossing the cut between those two components — exactly the condition the cut property guarantees is safe.

The overall running time is dominated by sorting: O(E log E), which equals O(E log V) since E ≤ V². After sorting, each union-find operation is nearly O(1), so processing all edges takes nearly O(E). Compared to Prim's algorithm, which grows the MST from a single starting vertex, Kruskal's has the advantage of simplicity — sort and scan — and works naturally on sparse graphs or edge lists. Prim's can be faster on dense graphs with a priority queue. When all edge weights are distinct, the MST is unique, so both algorithms produce the same result; when weights repeat, multiple valid MSTs may exist, and the two algorithms may find different ones.
