---
id: extremal-graph-theory
title: Extremal Graph Theory and Forbidden Subgraphs
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: turans-theorem
  type: soft
tags:
- graph-theory
- extremal
stage: advanced
status: draft
---

# Extremal Graph Theory and Forbidden Subgraphs

## Core Idea
Extremal graph theory studies the maximum number of edges in graphs avoiding certain subgraphs. Given forbidden graphs H, ex(n, H) is the maximum edges in n-vertex graphs with no copy of H. Classical results include Turán (forbidding cliques), Kővári-Sós-Turán (forbidding complete bipartite graphs), and connections to combinatorial designs and incidence geometry.

## Explainer

Extremal graph theory asks a precise optimization question: how many edges can a graph on n vertices have, given that it is *not allowed* to contain a particular subgraph? The function **ex(n, H)** — called the **Turán number** of H — captures the answer. The graph achieving this maximum (or asymptotically approaching it) is called an **extremal graph** for H.

From Turán's theorem, you already know one landmark result: ex(n, Kᵣ₊₁), the maximum edges avoiding a complete graph on r+1 vertices, is achieved by the **Turán graph** T(n, r) — a balanced complete r-partite graph. The key insight there was that forbidding cliques forces a multipartite structure, and balancing the parts maximizes edges within those constraints. Extremal graph theory generalizes this: for any forbidden graph H, what structure must an extremal graph have?

For complete bipartite graphs, the **Kővári-Sós-Turán theorem** gives an upper bound: any graph on n vertices with more than roughly (1/2)t^(1/s) · n^(2−1/s) edges must contain a copy of Kₛ,ₜ (s ≤ t). This matters for incidence geometry — if you have n points and n lines in the plane, asking how many incidences (point-on-line pairs) can occur is equivalent to a forbidden subgraph problem on a bipartite incidence graph, and KST bounds the answer.

The deepest results in the field come from the **Zarankiewicz problem** and connections to the **Bondy-Simonovits theorem**, which says that for any graph H that isn't bipartite, ex(n, H) grows like n^(1+1/(χ(H)−1)), where χ(H) is the chromatic number. This ties extremal density directly to coloring structure: the more chromatic the forbidden graph, the fewer edges you can have while avoiding it. For bipartite forbidden graphs, the problem is much harder and often open — the correct growth rate is not known even for simple cases like C₆. Extremal graph theory lives at the intersection of combinatorics, algebra, and geometry, and its techniques (probabilistic arguments, algebraic constructions, flag algebras) represent some of the deepest tools in modern combinatorics.
