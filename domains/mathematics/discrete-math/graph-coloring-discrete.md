---
id: graph-coloring-discrete
title: Graph Coloring and Chromatic Numbers
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-coloring
  type: hard
builds-toward:
- bipartite-graphs-matching
tags:
- coloring
- chromatic-number
- greedy-coloring
- bounds
stage: formal-systems
status: validated
---

# Graph Coloring and Chromatic Numbers

## Core Idea
A proper graph coloring assigns colors to vertices so adjacent vertices have different colors. The chromatic number χ(G) is the minimum colors needed. Computing χ(G) is NP-hard in general, but bounds exist: χ(G) ≤ Δ(G) + 1, where Δ is max degree.

## How It's Best Learned
Find the chromatic number of small graphs by hand. Implement a greedy coloring algorithm. Understand special cases: bipartite graphs have χ = 2; complete graphs have χ = n; cycles of odd length have χ = 3.

## Common Misconceptions
The four-color theorem applies to planar graphs, not all graphs. χ(G) = 2 iff G is bipartite (no odd cycles). Greedy coloring doesn't always find the optimal number.

## Questions

```yaml
- question: "Graph G contains a triangle (three mutually adjacent vertices) as a subgraph. What can you conclude about χ(G)?"
  type: multiple-choice
  options:
    - "χ(G) = 2, since most graphs are bipartite and 2-colorable"
    - "χ(G) = n, where n is the number of vertices in G"
    - "χ(G) ≥ 3, since the three mutually adjacent vertices of the triangle each require a different color"
    - "χ(G) ≤ 3, since the four-color theorem guarantees any graph needs at most 4 colors"
  answer: 2
  explanation: "A triangle (K₃) has three vertices that are all pairwise adjacent — each pair shares an edge and so must receive different colors. This forces at least 3 colors for those vertices alone, so χ(G) ≥ 3. The four-color theorem (option D) applies only to planar graphs, not all graphs. The general principle: the chromatic number of any graph is at least as large as its largest clique (complete subgraph)."

- question: "You run a greedy coloring algorithm on graph G and use 5 colors. Your friend claims to have found a valid coloring of G using only 4 colors. Is this a contradiction?"
  type: multiple-choice
  options:
    - "Yes — greedy coloring always finds the minimum number of colors, so χ(G) = 5"
    - "No — greedy coloring gives an upper bound but doesn't guarantee optimality; χ(G) could be 4 or even fewer"
    - "Yes — if a 4-coloring existed, the greedy algorithm would have found it"
    - "No — but χ(G) must be exactly the average of 4 and 5, since both are valid"
  answer: 1
  explanation: "Greedy coloring produces a valid coloring but not necessarily a minimum one. The order in which vertices are processed affects the result, and a poor ordering can waste colors. The greedy bound χ(G) ≤ Δ(G) + 1 guarantees termination but is often not tight. Your friend's 4-coloring proves χ(G) ≤ 4, which is a better upper bound. The true chromatic number is the minimum over all valid colorings — greedy can only approach it from above."

- question: "Every bipartite graph has a chromatic number of exactly 2."
  type: true-false
  answer: true
  explanation: "A bipartite graph has vertices split into two independent sets — no two vertices within the same set share an edge. Assign color 1 to all vertices in one set and color 2 to all vertices in the other set. Since every edge goes between the two sets, adjacent vertices always receive different colors. This is a valid 2-coloring. And since a bipartite graph has at least one edge, it cannot be 1-colored. So χ(G) = 2 exactly. Conversely, if χ(G) = 2, the two color classes form a bipartition, so G is bipartite — bipartiteness and χ = 2 are equivalent."

- question: "The four-color theorem guarantees that any graph, regardless of structure, can be properly colored with at most 4 colors."
  type: true-false
  answer: false
  explanation: "The four-color theorem applies specifically to planar graphs — graphs that can be drawn in the plane without edge crossings. For non-planar graphs, the chromatic number can be arbitrarily large. For example, the complete graph Kₙ requires n colors, and complete graphs with n ≥ 5 are non-planar. A common misconception is extending the theorem beyond its planar constraint, but the theorem says nothing about non-planar graph colorability."

- question: "Why is computing the chromatic number χ(G) of an arbitrary graph computationally hard, even though verifying whether a given coloring is proper is easy?"
  type: short-answer
  answer: "Verifying a coloring requires only checking each edge to confirm its two endpoints have different colors — a linear-time scan. But computing χ(G) requires finding the minimum k such that a valid k-coloring exists, which means determining whether a k-coloring exists for k = 1, 2, 3, … in turn. Deciding whether a graph has a valid k-coloring (for k ≥ 3) is NP-complete, meaning no polynomial-time algorithm is known. The gap between easy verification and hard search is the hallmark of NP-hard problems, and graph coloring is one of the classic examples."
  explanation: "This easy-to-verify, hard-to-compute structure is why graph coloring models genuinely difficult real-world problems: exam scheduling, register allocation in compilers, and frequency assignment in wireless networks are all NP-hard optimizations. In practice, one establishes bounds (clique size ≤ χ ≤ Δ+1) and uses heuristics or approximations."
```

## Explainer

Building on your understanding of graph coloring, the **chromatic number** χ(G) answers the optimization question: what is the *minimum* number of colors needed for a proper coloring? Think of the classic scheduling problem — you want to assign time slots for university exams so that no two courses sharing a student are scheduled at the same time. Each course is a vertex; a shared student creates an edge. Colors are time slots. A proper coloring corresponds to a valid schedule, and χ(G) is the fewest time slots you need.

The upper bound χ(G) ≤ Δ(G) + 1 (where Δ is the maximum vertex degree) comes from a simple greedy algorithm: process vertices in any order, and assign each vertex the smallest color not used by any of its neighbors. At the moment you color a vertex with at most Δ neighbors, at most Δ colors are already excluded, so the (Δ+1)th color is always available. This guarantees the bound, but greedy often does better — and the bound isn't always tight.

Special graph families reveal what χ(G) actually measures. A **complete graph** Kₙ has every pair of vertices adjacent, so all n vertices must get different colors: χ(Kₙ) = n. A **bipartite graph** can be 2-colored — label one partition class with color 1 and the other with color 2 — and χ(G) = 2 characterizes exactly the bipartite graphs (those with no odd cycles). An odd cycle like C₅ (a pentagon) needs 3 colors: you can alternate 2 colors around most of the cycle, but the last vertex ends up adjacent to vertices of both colors, forcing a third.

The bad news for algorithms: computing χ(G) exactly for an arbitrary graph is NP-hard. No polynomial-time algorithm is known. This is why graph coloring appears in so many "hard optimization" contexts — the scheduling, register allocation, and frequency assignment problems it models are genuinely difficult. In practice, one bounds χ(G) between the size of the largest **clique** (complete subgraph) below and Δ+1 above, and applies heuristics in between.
