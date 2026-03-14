---
id: gaussian-elimination-with-pivoting
title: Gaussian Elimination with Pivoting
domain: mathematics
course: numerical-analysis
prerequisites:
- id: gaussian-elimination
  type: hard
- id: numerical-stability
  type: hard
builds-toward:
- lu-decomposition
- condition-number-of-matrix
tags:
- gaussian-elimination
- pivoting
- linear-systems
stage: abstract-reasoning
status: draft
---

# Gaussian Elimination with Pivoting

## Core Idea
Gaussian elimination with partial (row) or complete (row and column) pivoting reorders equations to avoid dividing by small numbers, which amplifies rounding errors. Pivoting maintains multipliers |m_ij| ≤ 1, keeping roundoff errors bounded. While Gaussian elimination without pivoting can fail catastrophically on well-conditioned systems, pivoting recovers numerical stability without significantly increasing computation.
