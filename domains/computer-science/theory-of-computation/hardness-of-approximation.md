---
id: hardness-of-approximation
title: Hardness of Approximation
domain: computer-science
course: theory-of-computation
prerequisites:
- id: approximation-algorithms-design
  type: hard
- id: np-completeness
  type: hard
tags:
- hardness
- inapproximability
- lower-bounds
stage: advanced
status: draft
---

# Hardness of Approximation

## Core Idea
Hardness of approximation studies which optimization problems resist good approximations unless P=NP. Using the PCP (probabilistically checkable proofs) theorem, one proves problems cannot be approximated better than specific thresholds: vertex cover cannot be approximated better than 1.36, max clique not better than n^ε for any ε > 0. This shows approximation hardness is orthogonal to decision hardness—some NP-hard problems have arbitrary approximations, others have tight inapproximability barriers.
