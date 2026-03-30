---
id: turans-theorem
title: Turán's Theorem and Extremal Graph Theory
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-theory-intro
  type: hard
- id: erdos-gallai-theorem
  type: soft
- id: turan-theorem
  type: soft
- id: hamiltonian-cycles-dirac-ore
  type: soft
- id: graph-operations-and-products
  type: soft
builds-toward:
- extremal-graph-theory
tags:
- graph-theory
- extremal
stage: advanced
status: validated
---
# Turán's Theorem and Extremal Graph Theory

## Core Idea
Turán's Theorem determines the maximum number of edges in an n-vertex graph containing no clique of size r+1: the extremal graph is the Turán graph T(n,r), a balanced complete r-partite graph. This foundational result shows that complete multipartite graphs are optimal for avoiding cliques, initiating extremal graph theory.

## Questions

```yaml
- question: "In the Turán graph T(n, r), why can't a clique of size r+1 form, no matter how many edges the graph has?"
  type: multiple-choice
  options:
    - "The graph has exactly r edges, which is not enough to form a larger clique"
    - "There are only r groups and vertices in the same group share no edges, so any clique can have at most one vertex per group — giving maximum clique size r"
    - "The balanced partition ensures that no vertex has degree greater than r, preventing cliques of size r+1"
    - "T(n, r) is a planar graph, and planar graphs cannot contain large cliques by the four-color theorem"
  answer: 1
  explanation: "The no-clique guarantee comes from the partition structure, not from degree bounds or planarity. In T(n, r), vertices in the same group have NO edges between them (that's the definition of the complete r-partite structure). A clique requires every pair of vertices to be adjacent. So a clique can contain at most one vertex from each group — otherwise two same-group vertices would need an edge that doesn't exist. With r groups, maximum clique size is r, never r+1."

- question: "You want to build a triangle-free graph on 6 vertices with as many edges as possible. Which graph achieves the maximum edge count?"
  type: multiple-choice
  options:
    - "A 6-cycle (hexagon), which avoids triangles and uses all vertices"
    - "The complete bipartite graph K_{3,3}, which splits vertices into two groups of 3 with all cross-edges"
    - "The complete graph K_6 minus one edge, which removes the minimum needed to destroy all triangles"
    - "A path on 6 vertices, which is maximally sparse and therefore triangle-free"
  answer: 1
  explanation: "A triangle-free graph avoids K₃, so by Turán's theorem the extremal graph is T(6, 2) — the balanced complete bipartite graph K_{3,3}. It has 3 × 3 = 9 edges. The 6-cycle has only 6 edges. K_6 minus one edge still contains many triangles — you'd need to remove many more. T(6, 2) = K_{3,3} is the unique maximum triangle-free graph on 6 vertices, a special case of Mantel's Theorem. The key insight: complete bipartite = Turán graph for r = 2."

- question: "If you split n vertices into r groups of unequal sizes for a K_{r+1}-free graph, you can always increase the edge count by transferring vertices to make the groups more balanced."
  type: true-false
  answer: true
  explanation: "This balancing argument is the combinatorial core of Turán's proof. Suppose groups A and B have sizes a > b + 1. Transferring one vertex from A to B changes the edge count: you lose (n − a) cross-edges involving that vertex (edges to vertices outside A and B) but gain (a − 1) new cross-edges to A's remaining vertices and lose edges to B. The net effect of balancing is always non-negative, with strict gain when groups are sufficiently unequal. This is why the Turán graph with equal (or near-equal) group sizes uniquely maximizes the edge count."

- question: "The Turán graph T(n, r) is not the unique graph achieving the maximum number of edges in a K_{r+1}-free graph — there are many other graphs with the same edge count."
  type: true-false
  answer: false
  explanation: "Turán's theorem proves that T(n, r) is the UNIQUE extremal graph up to isomorphism. Any other K_{r+1}-free graph on n vertices either has fewer edges or is isomorphic to T(n, r). This uniqueness makes the theorem stronger than a mere bound — it characterizes the exact structure of the extremal case. The proof works by showing that any deviation from the balanced complete r-partite structure either violates the K_{r+1}-free condition or reduces the edge count."

- question: "Explain intuitively why the 'balanced' requirement in the Turán graph maximizes edges. Why does having groups of equal size produce more cross-edges than groups of unequal size?"
  type: short-answer
  answer: "Each vertex contributes edges to every vertex NOT in its own group. A vertex in a group of size s contributes (n − s) cross-edges. Making groups more equal distributes vertices so that each contributes more cross-edges on average. Concentrating vertices in large groups is wasteful: the large-group vertices all 'waste' their same-group non-edges on each other, while contributing fewer cross-edges. The product of group sizes is maximized when they're equal (by AM-GM inequality), and the total cross-edge count is the sum of all products of pairs of group sizes."
  explanation: "The formal argument uses a vertex-transfer: moving a vertex from a larger group to a smaller one always increases or maintains the total edge count. After each transfer, the groups are more balanced. The process terminates at the balanced partition, which must therefore be optimal. The AM-GM inequality formalizes this: for fixed sum, the product (and hence total edges, which counts each cross-group pair) is maximized when all parts are equal."
```

## Explainer

A **clique** in a graph is a set of vertices that are all mutually adjacent — everyone is connected to everyone else. A triangle is a clique of size 3; K₄ is a clique of size 4. Extremal graph theory asks: how many edges can a graph have before it's forced to contain a clique of a given size? Turán's theorem answers this question exactly.

The question is subtler than it appears. You can always add edges to a graph until you create a clique — the question is how many edges you can pack in while *avoiding* one. Turán's insight was to identify the precise structure that maximizes edges without forming a K_{r+1}. That structure is the **Turán graph T(n, r)**: take n vertices, divide them into r groups as evenly as possible, and add an edge between every pair of vertices that belong to *different* groups. Crucially, no two vertices in the same group are connected, which is exactly why no K_{r+1} can form: to have a clique of size r+1, you'd need r+1 mutually adjacent vertices, but since there are only r groups and two vertices in the same group share no edge, a clique can have at most one vertex from each group — giving maximum clique size r, not r+1.

The theorem says T(n, r) is not just *one* extremal graph — it is the *unique* graph (up to isomorphism) achieving the maximum edge count without a K_{r+1}. The edge count itself is called the **Turán number** ex(n, K_{r+1}). For example, ex(n, K₃) is the maximum number of edges in a triangle-free graph on n vertices, achieved by the complete bipartite graph K_{⌊n/2⌋, ⌈n/2⌉} — that's T(n, 2). Mantel's Theorem (1907) established this special case a generation before Turán proved the general result in 1941.

Why does "balanced" matter? If you split into r groups of unequal size, you can actually increase the edge count by equalizing them — transferring a vertex from a larger group to a smaller one always adds at least as many edges as it removes. This balancing argument is the combinatorial core of the proof. Turán's theorem inaugurated **extremal graph theory**, the study of how local constraints (avoiding a forbidden subgraph) bound global structure (edge density). It also underlies the **Kruskal-Katona theorem**, the **Zarankiewicz problem**, and many results in Ramsey theory — all asking what graph structure is forced when density is high enough.
