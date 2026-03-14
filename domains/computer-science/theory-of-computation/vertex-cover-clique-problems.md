---
id: vertex-cover-clique-problems
title: Vertex Cover and Clique Problems
domain: computer-science
course: theory-of-computation
prerequisites:
- id: np-completeness
  type: hard
- id: boolean-satisfiability-and-reductions
  type: hard
builds-toward:
- approximation-algorithms-design
tags:
- np-complete
- graph-problems
- reduction-chains
stage: advanced
status: draft
---

# Vertex Cover and Clique Problems

## Core Idea
Vertex cover asks: given a graph and integer k, does a set of k vertices exist such that every edge touches at least one? Clique asks: does the graph contain a complete subgraph of size k? Both are NP-complete. Clique and independent set are complementary: finding a clique in G equals finding an independent set in the complement graph. These problems exemplify how different-seeming combinatorial problems connect via polynomial reductions, sharing fundamental hardness despite surface dissimilarity.
