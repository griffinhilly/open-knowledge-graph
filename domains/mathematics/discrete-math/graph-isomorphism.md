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

## Explainer

Two graphs can look completely different drawn on paper yet be mathematically identical in structure. A graph drawn as a neat square with diagonals and the same graph drawn as a tangled mess of crossing lines are — assuming the same connections — the same graph. **Graph isomorphism** is the formal tool for saying "these two graphs are structurally the same." Two graphs G and H are isomorphic if you can find a **bijection** — a one-to-one, onto function — from G's vertices to H's vertices that preserves every edge. If vertices u and v are connected in G, then their images under the bijection must be connected in H, and vice versa.

Think of it like renaming the players in a game. If you take a social network and rename every person, the friendship structure hasn't changed. Isomorphism asks: is there a renaming that makes one graph look exactly like the other? The challenge is that with n vertices, there are n! possible bijections to check, which becomes impossibly large even for moderate n. This is why the computational side of graph isomorphism — determining whether two graphs are isomorphic efficiently — is famously hard.

To avoid checking all bijections, mathematicians use **graph invariants**: properties that must be equal in isomorphic graphs. If any invariant differs, the graphs cannot be isomorphic. Vertex count, edge count, and degree sequence are the cheapest invariants to compute. If G has degree sequence [3, 2, 2, 1] and H has degree sequence [3, 3, 1, 1], they cannot be isomorphic — stop there. Stronger invariants include the number of triangles, girth (length of shortest cycle), and diameter. Each invariant is a filter, and applying them cheapest-first prunes the search space efficiently.

Proving two graphs *are* isomorphic requires more: you must explicitly exhibit the bijection and verify that every edge is preserved. A useful strategy is to match high-degree vertices to high-degree vertices (degree must be preserved under any isomorphism), then check that those vertices' neighborhoods also match up. For small graphs, this process is manageable; for large ones, it remains an open problem whether a polynomial-time algorithm exists. Graph isomorphism sits in an unusual limbo in complexity theory — not known to be in P, but also not known to be NP-complete — making it one of the most intriguing open questions in combinatorics and computer science.
