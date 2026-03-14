---
id: graph-matching-halls-theorem
title: Graph Matching and Hall's Marriage Theorem
domain: mathematics
course: discrete-math
prerequisites:
- id: bipartite-graphs-characterization
  type: hard
builds-toward:
- network-flows-algorithm
tags:
- graph-theory
- matching
- halls-theorem
stage: formal-systems
status: draft
---

# Graph Matching and Hall's Marriage Theorem

## Core Idea
A matching is a set of edges with no common vertices. A perfect matching covers all vertices. Hall's Marriage Theorem: a bipartite graph G = (X ∪ Y, E) has a matching covering all vertices in X if and only if for every subset S ⊆ X, |N(S)| ≥ |S|, where N(S) is the neighborhood of S.
