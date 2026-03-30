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
stage: advanced
status: validated
---

# Turán's Theorem

## Core Idea
Turán's theorem characterizes the densest K_r-free graph on n vertices: the Turán graph T(n,r−1), a complete (r−1)-partite graph. This foundational result in extremal graph theory provides the edge-count upper bound ex(n, K_r) = |E(T(n,r−1))|.

## How It's Best Learned
Construct the Turán graph T(n,r−1) explicitly for small n and r, verifying it is K_r-free and counting its edges. Apply the theorem to find upper bounds on edge density in forbidden-subgraph problems.

## Common Misconceptions
- Thinking the Turán graph is unique; it is, but understanding why is non-trivial.
- Assuming Turán's bound applies to forbidden subgraphs beyond cliques without modification (it generalizes, but requires care).

## Questions

```yaml
- question: "What happens to ex(n, K_r) — the maximum number of edges in a K_r-free graph on n vertices — as r increases while n stays fixed?"
  type: multiple-choice
  options:
    - "It decreases, because larger cliques are harder to avoid and require a sparser graph"
    - "It increases, because forbidding a larger clique is a weaker constraint, allowing more edges"
    - "It stays the same, because the number of vertices has not changed"
    - "It approaches zero, since avoiding any clique eventually forces an empty graph"
  answer: 1
  explanation: "Forbidding K_r is a weaker constraint when r is large — you only need to avoid r-cliques, not smaller ones. The Turán edge count (1 − 1/(r−1)) · n²/2 increases toward n²/2 as r grows. Triangle-free graphs (r=3) are the most restricted at roughly n²/4; as r grows, the bound approaches n²/2. Larger forbidden clique means more edges are permitted."

- question: "A student claims: 'K_{3,3} is the densest triangle-free graph on 6 vertices.' What does Turán's theorem say about this claim?"
  type: multiple-choice
  options:
    - "False — K_{3,3} contains triangles and is not triangle-free"
    - "True — T(6, 2) is exactly K_{3,3}, splitting 6 vertices into two equal parts, achieving the maximum edge count for K₃-free graphs on 6 vertices"
    - "False — a denser triangle-free graph on 6 vertices can be constructed using unequal partition sizes"
    - "True — but any bipartite graph on 6 vertices achieves this same maximum"
  answer: 1
  explanation: "T(6, 2) is the Turán graph for K₃-free graphs with n=6: partition into r−1 = 2 equal parts of size 3 each and add all edges between parts. This gives K_{3,3} with 9 edges. It is triangle-free (a triangle would need an edge within a part, which doesn't exist). Turán's theorem guarantees no other triangle-free graph on 6 vertices can exceed 9 edges, and the balanced partition is uniquely optimal."

- question: "According to Turán's theorem, a K₄-free graph on n vertices can have approximately n²/3 edges, compared to roughly n²/4 for a K₃-free graph — meaning forbidding a larger clique allows more edges."
  type: true-false
  answer: true
  explanation: "The Turán edge count formula (1 − 1/(r−1)) · n²/2 gives n²/4 for r=3 (K₃-free) and n²/3 for r=4 (K₄-free). Avoiding K₄ is a weaker constraint than avoiding K₃, so a denser graph is achievable. As r grows, the bound approaches n²/2, the complete graph."

- question: "In the Turán graph T(n, r−1), making one partition class much larger than the others while keeping remaining parts equal would increase the total number of edges beyond the balanced construction."
  type: true-false
  answer: false
  explanation: "Any imbalance decreases the edge count. If two parts have sizes a and b with a > b+1, moving a vertex from the larger to the smaller replaces a·b inter-part edges between those classes with (a−1)·(b+1) = a·b + a − b − 1, which is larger when a > b+1. Equal parts maximize the product of partition sizes and thus maximize edges. Unbalanced partitions waste edge potential."

- question: "Why does the Turán graph T(n, r−1) contain no K_r, and why does balancing the partition sizes maximize edges?"
  type: short-answer
  answer: "T(n, r−1) has r−1 independent sets (parts) with edges only between different parts. Any r chosen vertices must include two from the same part by the pigeonhole principle, but there are no edges within parts — so no K_r can exist. Balancing matters because any imbalance can be corrected: moving a vertex from a larger part (size a) to a smaller part (size b, with a > b+1) increases inter-part edges between those two classes from a·b to (a−1)(b+1), which is strictly larger. Equal parts maximize the sum of products of partition sizes, yielding the most edges possible."
  explanation: "These two facts together give the full picture: the construction is K_r-free by pigeonhole, and it is optimal because the balanced partition maximizes edges. The Zykov symmetrization argument formalizes why any asymmetry can always be profitably corrected."
```

## Explainer

The central question of **extremal graph theory** is: among all graphs on n vertices that avoid some forbidden subgraph H, how many edges can there be? Turán's theorem answers this completely when H is a complete graph K_r. Start with the simplest case: triangle-free graphs (no K₃). How many edges can a graph on n vertices have if it contains no triangle? Turán's answer, for K₃-free graphs, is the **complete bipartite graph** K_{⌊n/2⌋, ⌈n/2⌉} — split the vertices into two equal halves and put every possible edge between the halves (no edges within a half). This graph has no triangles (a triangle would need two vertices in the same half with an edge between them, which doesn't exist) and has roughly n²/4 edges.

The general **Turán graph** T(n, r−1) extends this to K_r-free graphs: split n vertices into r−1 parts as equally as possible and put every edge between different parts (none within a part). This is a complete (r−1)-partite graph. It's K_r-free because any K_r needs r vertices, but in a (r−1)-partite graph, by the pigeonhole principle, at least two vertices from any r chosen vertices must come from the same part — and there are no edges within parts. **Turán's theorem** says this construction is optimal: any K_r-free graph on n vertices has at most |E(T(n, r−1))| edges, and equality holds only for the Turán graph itself (up to relabeling).

The edge count of T(n, r−1) is approximately (1 − 1/(r−1)) · n²/2. As r grows, the forbidden clique gets larger and you can pack in more edges before violating the constraint. For r = 2 (triangle-free), the bound is n²/4; for r = 3 (K₄-free), it's n²/3; as r → ∞ the bound approaches n²/2, which is the complete graph. The extremal number **ex(n, K_r) = |E(T(n, r−1))|** is the exact threshold. Knowing this number and the structure of the extremal graph is the complete solution to the K_r case.

The proof strategy is elegant and worth understanding. Suppose G is K_r-free with the maximum number of edges. Look at a vertex v of maximum degree. Replace every other vertex u with a copy of v's neighborhood structure — this "greedy" replacement can only increase edges while maintaining K_r-freeness. Iterating this process pushes G toward the complete multipartite structure, and the optimal partition turns out to be as equal as possible. This argument, called the **Zykov symmetrization**, shows why equal parts maximize edges: any imbalance between part sizes can be corrected by moving a vertex from the larger part to the smaller, increasing the edge count. Turán's theorem is the prototype for dozens of results in extremal combinatorics, all asking: what structure maximizes edges subject to a local constraint?
