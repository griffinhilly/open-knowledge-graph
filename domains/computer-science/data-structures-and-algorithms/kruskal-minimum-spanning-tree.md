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
status: validated
---

# Kruskal's Algorithm for Minimum Spanning Trees

## Core Idea
Kruskal's algorithm greedily builds an MST by sorting edges by weight and adding each edge if it doesn't create a cycle (detected via union-find). It runs in O(E log E) time and works on any connected weighted graph. The greedy choice is safe: every MST edge is the minimum-weight edge crossing some cut of the graph.

## How It's Best Learned
Trace the algorithm on a small graph: sort edges, add them, and use union-find to detect cycles. Understand why the greedy choice is optimal (cut property). Compare to Prim's: Kruskal is simpler but requires sorting; Prim is incremental.

## Common Misconceptions
- The MST is unique (unique only if all edge weights are distinct). - Union-find is required (any cycle-detection method works; union-find is just efficient).

## Questions

```yaml
- question: "A graph has 6 vertices and 10 edges sorted by weight. When Kruskal's processes the 7th edge in order, it finds both endpoints are already in the same component. What does the algorithm do?"
  type: multiple-choice
  options:
    - "Start over, choosing a different starting vertex"
    - "Add the edge anyway since it is the next lightest"
    - "Skip the edge and continue to the 8th edge"
    - "Terminate, since a spanning tree needs fewer than 7 edges"
  answer: 2
  explanation: "Kruskal's skips any edge that would create a cycle (both endpoints already in the same component) and continues scanning. It does not restart or terminate early — it keeps going until it has collected exactly V−1 edges. A spanning tree on V vertices needs V−1 edges, so with 6 vertices the algorithm collects 5 edges total, skipping however many cycle-forming edges it encounters."

- question: "Why does Kruskal's algorithm run in O(E log E) rather than O(E) time?"
  type: multiple-choice
  options:
    - "Union-find operations each take O(log E) time in the worst case"
    - "The initial sorting of all edges dominates, requiring O(E log E) comparisons"
    - "Each edge must be checked against all previously added edges for cycles"
    - "The algorithm requires O(log E) passes over the edge list"
  answer: 1
  explanation: "After sorting, each union-find operation runs in nearly O(1) time with path compression and union by rank, so processing all edges takes effectively O(E). The bottleneck is sorting E edges, which takes O(E log E). The common misconception is that cycle detection is expensive — union-find makes it nearly constant per edge, so sorting dominates."

- question: "The cut property guarantees that the minimum-weight edge crossing any partition of vertices into two non-empty groups must belong to some MST."
  type: true-false
  answer: true
  explanation: "This is the fundamental correctness guarantee for Kruskal's algorithm. Every time Kruskal's adds an edge, it is connecting two previously disconnected components — which defines exactly such a partition (cut). Since the edge chosen is the lightest available that crosses this cut, the cut property guarantees the addition is safe and the result will be a valid MST."

- question: "Kruskal's algorithm always produces the unique minimum spanning tree of any connected weighted graph."
  type: true-false
  answer: false
  explanation: "The MST is unique only when all edge weights are distinct. When multiple edges share the same weight, different valid MSTs may exist, and Kruskal's may find different ones depending on tie-breaking order. This is a common misconception: 'minimum' does not imply uniqueness. Both Kruskal's and Prim's are correct for any MST — they may just select different ones when weights are tied."

- question: "Why does the greedy strategy of always adding the lightest non-cycle-forming edge guarantee a globally optimal spanning tree, rather than just a locally convenient one?"
  type: short-answer
  answer: "The cut property provides the guarantee: for any partition of the graph's vertices into two groups, the minimum-weight edge crossing that partition must belong to some MST. Every time Kruskal's adds an edge, it connects two previously disconnected components, which defines exactly such a partition. Since the chosen edge is the lightest crossing that cut, the cut property guarantees it belongs to a valid MST. Each greedy choice is globally safe, not just locally convenient."
  explanation: "The cut property is what separates Kruskal's from naive greedy approaches that fail. The mathematical structure of spanning trees (specifically, spanning tree edge sets form a matroid) ensures that no sequence of locally greedy safe choices leads to a suboptimal result. Without this structural guarantee, greedy algorithms can get stuck in locally good but globally suboptimal solutions."
```

## Explainer

You already know that greedy algorithms make locally optimal choices and that union-find efficiently tracks which elements belong to the same connected component. Kruskal's algorithm combines these two ideas into an elegant procedure for finding a **minimum spanning tree** (MST) — the subset of edges that connects every vertex in a weighted graph at the lowest possible total cost, without forming any cycles.

The algorithm works in three steps. First, sort all edges in the graph by weight from lightest to heaviest. Second, iterate through the sorted edges one at a time. For each edge, ask: "Would adding this edge create a cycle?" If no, add it to the growing tree. If yes, skip it. Third, stop when you have exactly V−1 edges (where V is the number of vertices), because any tree on V vertices has exactly V−1 edges. The cycle-detection question is where union-find earns its place — each vertex starts in its own set, adding an edge merges two sets, and an edge would create a cycle precisely when both its endpoints are already in the same set. With union-find using path compression and union by rank, each of these operations runs in nearly constant time.

Why does this greedy strategy actually produce the optimal tree? The answer rests on the **cut property**: for any partition of the vertices into two non-empty groups, the lightest edge crossing that partition must belong to some MST. Since Kruskal's considers edges lightest-first and only adds edges that connect previously disconnected components, every edge it adds is the lightest edge crossing the cut between those two components — exactly the condition the cut property guarantees is safe.

The overall running time is dominated by sorting: O(E log E), which equals O(E log V) since E ≤ V². After sorting, each union-find operation is nearly O(1), so processing all edges takes nearly O(E). Compared to Prim's algorithm, which grows the MST from a single starting vertex, Kruskal's has the advantage of simplicity — sort and scan — and works naturally on sparse graphs or edge lists. Prim's can be faster on dense graphs with a priority queue. When all edge weights are distinct, the MST is unique, so both algorithms produce the same result; when weights repeat, multiple valid MSTs may exist, and the two algorithms may find different ones.
