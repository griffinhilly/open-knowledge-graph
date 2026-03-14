---
id: np-completeness-reduction-proof-techniques
title: Reductions for Proving NP-Completeness
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: polynomial-time-reductions
  type: hard
builds-toward:
- approximation-hardness-results
tags:
- reductions
- NP-completeness
- proof-techniques
stage: advanced
status: draft
---

# Reductions for Proving NP-Completeness

## Core Idea
To prove a problem L is NP-complete, show L ∈ NP and reduce a known NP-complete problem to L in polynomial time. Standard reduction templates (clique to independent set, 3-SAT to Hamiltonian path) encode one computational structure into another, allowing hardness to propagate. This technique has identified thousands of NP-complete problems across computer science.
