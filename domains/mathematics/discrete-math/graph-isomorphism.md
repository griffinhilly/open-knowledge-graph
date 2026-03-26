---
id: graph-isomorphism
title: Graph Isomorphism
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
- id: graph-representation
  type: soft
tags:
- graph-isomorphism
- structural-equivalence
- invariants
- bijection
stage: formal-systems
status: validated
---

# Graph Isomorphism

## Core Idea
Two graphs G and H are isomorphic if there exists a bijection between their vertex sets that preserves the edge relation — the graphs are structurally identical, differing only in vertex labeling. Proving isomorphism requires exhibiting an explicit edge-preserving bijection. Disproving it uses graph invariants: properties preserved under isomorphism, such as vertex count, edge count, degree sequence, girth, and number of triangles. Graph isomorphism is one of the few natural computational problems not known to be either in P or NP-complete.

## How It's Best Learned
Practice by examining pairs of graphs and deciding isomorphism using cheap invariants first (degree sequence), then attempting bijection construction. For small graphs, generate all possible degree-respecting bijections systematically. Appreciation for the computational difficulty grows from experiencing larger cases.

## Common Misconceptions
- Concluding two differently drawn graphs are non-isomorphic just because they look different — drawings are arbitrary.
- Using only vertex and edge counts to confirm isomorphism (necessary but far from sufficient).

## Questions

```yaml
- question: "Graphs G and H have the same vertex count, edge count, and degree sequence [3, 2, 2, 1]. What can you conclude?"
  type: multiple-choice
  options:
    - "G and H are isomorphic, since they share all these invariants"
    - "G and H are not isomorphic, since no further checks are needed once three invariants match"
    - "G and H may or may not be isomorphic — matching invariants is necessary but not sufficient"
    - "G and H are isomorphic only if they are drawn the same way"
  answer: 2
  explanation: "Matching invariants (vertex count, edge count, degree sequence) rules out non-isomorphism only when they *differ*. When they match, you cannot yet conclude isomorphism — you must still exhibit an explicit edge-preserving bijection. Option A is the classic misconception: necessary conditions are not sufficient. Option D confuses graph drawings with graph structure — two isomorphic graphs can look completely different when drawn."

- question: "You want to prove two graphs are NOT isomorphic as efficiently as possible. Which strategy is best?"
  type: multiple-choice
  options:
    - "Enumerate all n! possible bijections between their vertex sets and verify none preserve edges"
    - "Apply cheap invariants first (degree sequence, girth, triangle count); stop as soon as one differs"
    - "Draw both graphs and observe whether they look different"
    - "Check whether both graphs are connected"
  answer: 1
  explanation: "Disproving isomorphism only requires finding one invariant that differs. Applying cheap invariants (degree sequence first, then girth, triangle count, etc.) prunes the search immediately — if degree sequences differ, no bijection can exist, and you're done. Option A (enumerating all n! bijections) is what you'd do to prove isomorphism, not disprove it, and is computationally infeasible for large n. Option C is the fundamental misconception: graph drawings are arbitrary and visually different graphs may be isomorphic."

- question: "Two graphs that are drawn differently on paper can seldom be isomorphic."
  type: true-false
  answer: false
  explanation: "This is the most common misconception in graph isomorphism. A graph can be drawn in infinitely many ways — vertex positions and edge curves are arbitrary visual choices, not part of the mathematical structure. The same graph drawn as a neat square with diagonals and as a tangled mess of crossing lines is still the same graph. Isomorphism is about whether an edge-preserving bijection exists between vertex sets, not about visual similarity."

- question: "The degree sequence of a graph is preserved under any isomorphism — if two graphs are isomorphic, their degree sequences must be identical."
  type: true-false
  answer: true
  explanation: "Degree is a structural property: the degree of a vertex is the number of edges incident to it. Any isomorphism maps vertices to vertices in an edge-preserving way, so each vertex's degree must be the same as its image's degree. This makes degree sequence one of the most useful and cheapest invariants to check. Note, however, that matching degree sequences does not guarantee isomorphism — it is a necessary, not sufficient, condition."

- question: "Why is proving two graphs are isomorphic harder than proving they are non-isomorphic?"
  type: short-answer
  answer: "To prove non-isomorphism, you only need to find a single invariant that differs — one mismatch is enough to rule out any bijection. To prove isomorphism, you must exhibit an explicit edge-preserving bijection and verify every edge is mapped correctly. There is no shortcut: you cannot simply confirm invariants match and declare success. For n vertices, there are n! possible bijections to consider, which grows impossibly large even for moderate n, making the constructive proof the difficult direction."
  explanation: "This asymmetry — that disproving is easy (find a counterexample invariant) while proving requires construction — is a general feature of existence proofs. It also explains why graph isomorphism is computationally hard: while invariant-checking can rule out most pairs quickly, the remaining 'pass' cases require expensive construction. The fact that graph isomorphism sits in computational limbo (not known to be in P or NP-complete) reflects exactly this asymmetry."
```

## Explainer

Two graphs can look completely different drawn on paper yet be mathematically identical in structure. A graph drawn as a neat square with diagonals and the same graph drawn as a tangled mess of crossing lines are — assuming the same connections — the same graph. **Graph isomorphism** is the formal tool for saying "these two graphs are structurally the same." Two graphs G and H are isomorphic if you can find a **bijection** — a one-to-one, onto function — from G's vertices to H's vertices that preserves every edge. If vertices u and v are connected in G, then their images under the bijection must be connected in H, and vice versa.

Think of it like renaming the players in a game. If you take a social network and rename every person, the friendship structure hasn't changed. Isomorphism asks: is there a renaming that makes one graph look exactly like the other? The challenge is that with n vertices, there are n! possible bijections to check, which becomes impossibly large even for moderate n. This is why the computational side of graph isomorphism — determining whether two graphs are isomorphic efficiently — is famously hard.

To avoid checking all bijections, mathematicians use **graph invariants**: properties that must be equal in isomorphic graphs. If any invariant differs, the graphs cannot be isomorphic. Vertex count, edge count, and degree sequence are the cheapest invariants to compute. If G has degree sequence [3, 2, 2, 1] and H has degree sequence [3, 3, 1, 1], they cannot be isomorphic — stop there. Stronger invariants include the number of triangles, girth (length of shortest cycle), and diameter. Each invariant is a filter, and applying them cheapest-first prunes the search space efficiently.

Proving two graphs *are* isomorphic requires more: you must explicitly exhibit the bijection and verify that every edge is preserved. A useful strategy is to match high-degree vertices to high-degree vertices (degree must be preserved under any isomorphism), then check that those vertices' neighborhoods also match up. For small graphs, this process is manageable; for large ones, it remains an open problem whether a polynomial-time algorithm exists. Graph isomorphism sits in an unusual limbo in complexity theory — not known to be in P, but also not known to be NP-complete — making it one of the most intriguing open questions in combinatorics and computer science.
