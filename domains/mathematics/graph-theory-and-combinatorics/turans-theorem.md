---
id: turans-theorem
title: Turán's Theorem and Extremal Graph Theory
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-theory-intro
  type: hard
builds-toward:
- extremal-graph-theory
tags:
- graph-theory
- extremal
stage: formal-systems
status: draft
---

# Turán's Theorem and Extremal Graph Theory

## Core Idea
Turán's Theorem determines the maximum number of edges in an n-vertex graph containing no clique of size r+1: the extremal graph is the Turán graph T(n,r), a balanced complete r-partite graph. This foundational result shows that complete multipartite graphs are optimal for avoiding cliques, initiating extremal graph theory.

## Explainer

A **clique** in a graph is a set of vertices that are all mutually adjacent — everyone is connected to everyone else. A triangle is a clique of size 3; K₄ is a clique of size 4. Extremal graph theory asks: how many edges can a graph have before it's forced to contain a clique of a given size? Turán's theorem answers this question exactly.

The question is subtler than it appears. You can always add edges to a graph until you create a clique — the question is how many edges you can pack in while *avoiding* one. Turán's insight was to identify the precise structure that maximizes edges without forming a K_{r+1}. That structure is the **Turán graph T(n, r)**: take n vertices, divide them into r groups as evenly as possible, and add an edge between every pair of vertices that belong to *different* groups. Crucially, no two vertices in the same group are connected, which is exactly why no K_{r+1} can form: to have a clique of size r+1, you'd need r+1 mutually adjacent vertices, but since there are only r groups and two vertices in the same group share no edge, a clique can have at most one vertex from each group — giving maximum clique size r, not r+1.

The theorem says T(n, r) is not just *one* extremal graph — it is the *unique* graph (up to isomorphism) achieving the maximum edge count without a K_{r+1}. The edge count itself is called the **Turán number** ex(n, K_{r+1}). For example, ex(n, K₃) is the maximum number of edges in a triangle-free graph on n vertices, achieved by the complete bipartite graph K_{⌊n/2⌋, ⌈n/2⌉} — that's T(n, 2). Mantel's Theorem (1907) established this special case a generation before Turán proved the general result in 1941.

Why does "balanced" matter? If you split into r groups of unequal size, you can actually increase the edge count by equalizing them — transferring a vertex from a larger group to a smaller one always adds at least as many edges as it removes. This balancing argument is the combinatorial core of the proof. Turán's theorem inaugurated **extremal graph theory**, the study of how local constraints (avoiding a forbidden subgraph) bound global structure (edge density). It also underlies the **Kruskal-Katona theorem**, the **Zarankiewicz problem**, and many results in Ramsey theory — all asking what graph structure is forced when density is high enough.
