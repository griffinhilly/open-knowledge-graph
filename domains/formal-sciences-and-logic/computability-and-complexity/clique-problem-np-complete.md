---
id: clique-problem-np-complete
title: Clique Problem and Its Variants
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: three-sat-np-complete
  type: hard
- id: np-completeness-formal
  type: hard
builds-toward:
- vertex-cover-problem
tags:
- graph-problems
- np-complete
- optimization
stage: advanced
status: draft
---

# Clique Problem and Its Variants

## Core Idea
The clique problem asks whether a graph contains a subset of k vertices all pairwise adjacent (a complete subgraph). NP-completeness of the clique problem follows from reduction from 3-SAT. Its complement, the independent set problem, is also NP-complete, illustrating how graph optimization problems naturally exhibit computational hardness.
