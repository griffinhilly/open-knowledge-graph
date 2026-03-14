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
