---
id: extremal-graph-theory
title: Extremal Graph Theory and Forbidden Subgraphs
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: turans-theorem
  type: soft
- id: erdos-gallai-theorem
  type: soft
- id: graph-operations-and-products
  type: soft
tags:
- graph-theory
- extremal
stage: formal-systems
status: validated
---
# Extremal Graph Theory and Forbidden Subgraphs

## Core Idea
Extremal graph theory studies the maximum number of edges in graphs avoiding certain subgraphs. Given forbidden graphs H, ex(n, H) is the maximum edges in n-vertex graphs with no copy of H. Classical results include Turán (forbidding cliques), Kővári-Sós-Turán (forbidding complete bipartite graphs), and connections to combinatorial designs and incidence geometry.

## Questions

```yaml
- question: "You want to find ex(n, K₄) — the maximum number of edges in an n-vertex graph with no K₄. Which graph achieves this maximum?"
  type: multiple-choice
  options:
    - "A complete bipartite graph K_{n/2, n/2}"
    - "The Turán graph T(n, 3) — a balanced complete 3-partite graph"
    - "A random graph with edge probability 1/2"
    - "The cycle graph Cₙ"
  answer: 1
  explanation: "By Turán's theorem, ex(n, Kᵣ₊₁) is achieved by the Turán graph T(n, r). For K₄ (= K_{3+1}), r = 3, so the extremal graph is T(n, 3): partition n vertices into 3 equal parts and place all edges between different parts (no edges within parts). This graph contains no K₄ because any four vertices must include two from the same part, and those have no edge between them. The balance of part sizes is essential to maximizing edges within the K₄-free constraint. K_{n/2, n/2} is T(n, 2), which avoids triangles (K₃), not K₄."

- question: "The Kővári-Sós-Turán theorem provides an upper bound on edges in graphs forbidding the complete bipartite graph Kₛ,ₜ. What is one major application of this result outside pure graph theory?"
  type: multiple-choice
  options:
    - "Bounding the chromatic number of planar graphs"
    - "Proving that all Hamiltonian graphs have an Eulerian circuit"
    - "Bounding incidence counts between points and lines in combinatorial geometry"
    - "Establishing the four-color theorem for maps"
  answer: 2
  explanation: "KST has a direct application to incidence geometry: if you have n points and n lines in the plane, the number of incidences (point-on-line pairs) is equivalent to edges in a bipartite 'incidence graph' between the point set and the line set. Any such graph cannot contain K_{2,2} (no two points lie on two common lines in the Euclidean plane), so KST bounds the total incidence count. This connection — between forbidden subgraph problems and geometric configurations — illustrates how extremal graph theory provides tools for questions that do not initially look like graph problems."

- question: "The Turán graph T(n, r) is the unique n-vertex graph with no K_{r+1} that maximizes the number of edges — any addition of a single edge creates a clique of the forbidden size."
  type: true-false
  answer: true
  explanation: "True. Turán's theorem establishes that T(n, r) is the unique extremal graph for K_{r+1}: it is the densest K_{r+1}-free graph, uniquely determined by the balanced complete r-partite structure. Adding any edge to T(n, r) creates a K_{r+1}, because any two vertices in the same part now have an edge, and with cross-part edges they can form a larger clique. The balance of part sizes (making parts as equal as possible) is essential to the uniqueness: unbalanced partitions produce fewer edges within the K_{r+1}-free constraint."

- question: "The Bondy-Simonovits theorem implies that all forbidden graphs H produce the same asymptotic growth rate for ex(n, H) — specifically that ex(n, H) = Θ(n²) for any choice of H."
  type: true-false
  answer: false
  explanation: "False. The Bondy-Simonovits theorem shows that the asymptotic growth rate of ex(n, H) depends critically on the chromatic number χ(H) of the forbidden graph. For non-bipartite H (χ(H) ≥ 3), ex(n, H) = Θ(n^(1 + 1/(χ(H)−1))), which gives different exponents for different chromatic numbers. For bipartite H (χ(H) = 2), the theorem doesn't apply and the growth rate is subquadratic — often much harder to determine exactly, and frequently open. Growth rates vary substantially with the structure of H."

- question: "What does the Bondy-Simonovits theorem establish about ex(n, H), and why is the bipartite case harder than the non-bipartite case?"
  type: short-answer
  answer: "The Bondy-Simonovits theorem establishes that for any non-bipartite graph H with chromatic number χ(H), the Turán number satisfies ex(n, H) = Θ(n^(1 + 1/(χ(H)−1))). This ties extremal density directly to the coloring structure of the forbidden graph. For bipartite forbidden graphs (χ(H) = 2), this formula breaks down — the exact exponent depends on the specific structure of H in ways not captured by chromatic number alone, making many cases (including ex(n, C₆)) still open."
  explanation: "The deeper reason bipartite forbidden graphs are harder is that the Turán-style multipartite constructions that work for non-bipartite cases rely on chromatic structure. For bipartite H, you need algebraic constructions (often from finite geometry) or probabilistic arguments, and tighter upper bounds require more delicate combinatorial techniques. The Zarankiewicz problem — ex(n, Kₛ,ₜ) — captures much of this difficulty and remains one of the central open problems in combinatorics."
```

## Explainer

Extremal graph theory asks a precise optimization question: how many edges can a graph on n vertices have, given that it is *not allowed* to contain a particular subgraph? The function **ex(n, H)** — called the **Turán number** of H — captures the answer. The graph achieving this maximum (or asymptotically approaching it) is called an **extremal graph** for H.

From Turán's theorem, you already know one landmark result: ex(n, Kᵣ₊₁), the maximum edges avoiding a complete graph on r+1 vertices, is achieved by the **Turán graph** T(n, r) — a balanced complete r-partite graph. The key insight there was that forbidding cliques forces a multipartite structure, and balancing the parts maximizes edges within those constraints. Extremal graph theory generalizes this: for any forbidden graph H, what structure must an extremal graph have?

For complete bipartite graphs, the **Kővári-Sós-Turán theorem** gives an upper bound: any graph on n vertices with more than roughly (1/2)t^(1/s) · n^(2−1/s) edges must contain a copy of Kₛ,ₜ (s ≤ t). This matters for incidence geometry — if you have n points and n lines in the plane, asking how many incidences (point-on-line pairs) can occur is equivalent to a forbidden subgraph problem on a bipartite incidence graph, and KST bounds the answer.

The deepest results in the field come from the **Zarankiewicz problem** and connections to the **Bondy-Simonovits theorem**, which says that for any graph H that isn't bipartite, ex(n, H) grows like n^(1+1/(χ(H)−1)), where χ(H) is the chromatic number. This ties extremal density directly to coloring structure: the more chromatic the forbidden graph, the fewer edges you can have while avoiding it. For bipartite forbidden graphs, the problem is much harder and often open — the correct growth rate is not known even for simple cases like C₆. Extremal graph theory lives at the intersection of combinatorics, algebra, and geometry, and its techniques (probabilistic arguments, algebraic constructions, flag algebras) represent some of the deepest tools in modern combinatorics.
