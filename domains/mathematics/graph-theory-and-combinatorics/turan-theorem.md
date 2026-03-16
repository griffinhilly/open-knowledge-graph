---
id: turan-theorem
title: Turán's Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: formal-definitions-graph-theory
  type: hard
builds-toward:
- extremal-graph-theory
- probabilistic-method-graphs
tags:
- turan-theorem
- extremal-graphs
- clique-free
stage: formal-systems
status: draft
---

# Turán's Theorem

## Core Idea
Turán's theorem characterizes the densest K_r-free graph on n vertices: the Turán graph T(n,r−1), a complete (r−1)-partite graph. This foundational result in extremal graph theory provides the edge-count upper bound ex(n, K_r) = |E(T(n,r−1))|.

## How It's Best Learned
Construct the Turán graph T(n,r−1) explicitly for small n and r, verifying it is K_r-free and counting its edges. Apply the theorem to find upper bounds on edge density in forbidden-subgraph problems.

## Common Misconceptions
- Thinking the Turán graph is unique; it is, but understanding why is non-trivial.
- Assuming Turán's bound applies to forbidden subgraphs beyond cliques without modification (it generalizes, but requires care).

## Explainer

The central question of **extremal graph theory** is: among all graphs on n vertices that avoid some forbidden subgraph H, how many edges can there be? Turán's theorem answers this completely when H is a complete graph K_r. Start with the simplest case: triangle-free graphs (no K₃). How many edges can a graph on n vertices have if it contains no triangle? Turán's answer, for K₃-free graphs, is the **complete bipartite graph** K_{⌊n/2⌋, ⌈n/2⌉} — split the vertices into two equal halves and put every possible edge between the halves (no edges within a half). This graph has no triangles (a triangle would need two vertices in the same half with an edge between them, which doesn't exist) and has roughly n²/4 edges.

The general **Turán graph** T(n, r−1) extends this to K_r-free graphs: split n vertices into r−1 parts as equally as possible and put every edge between different parts (none within a part). This is a complete (r−1)-partite graph. It's K_r-free because any K_r needs r vertices, but in a (r−1)-partite graph, by the pigeonhole principle, at least two vertices from any r chosen vertices must come from the same part — and there are no edges within parts. **Turán's theorem** says this construction is optimal: any K_r-free graph on n vertices has at most |E(T(n, r−1))| edges, and equality holds only for the Turán graph itself (up to relabeling).

The edge count of T(n, r−1) is approximately (1 − 1/(r−1)) · n²/2. As r grows, the forbidden clique gets larger and you can pack in more edges before violating the constraint. For r = 2 (triangle-free), the bound is n²/4; for r = 3 (K₄-free), it's n²/3; as r → ∞ the bound approaches n²/2, which is the complete graph. The extremal number **ex(n, K_r) = |E(T(n, r−1))|** is the exact threshold. Knowing this number and the structure of the extremal graph is the complete solution to the K_r case.

The proof strategy is elegant and worth understanding. Suppose G is K_r-free with the maximum number of edges. Look at a vertex v of maximum degree. Replace every other vertex u with a copy of v's neighborhood structure — this "greedy" replacement can only increase edges while maintaining K_r-freeness. Iterating this process pushes G toward the complete multipartite structure, and the optimal partition turns out to be as equal as possible. This argument, called the **Zykov symmetrization**, shows why equal parts maximize edges: any imbalance between part sizes can be corrected by moving a vertex from the larger part to the smaller, increasing the edge count. Turán's theorem is the prototype for dozens of results in extremal combinatorics, all asking: what structure maximizes edges subject to a local constraint?
