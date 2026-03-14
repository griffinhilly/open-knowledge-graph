---
id: lu-decomposition-numerical
title: LU Decomposition and Forward/Back Substitution
domain: mathematics
course: linear-algebra
prerequisites:
- id: gaussian-elimination-pivoting
  type: hard
builds-toward:
- matrix-norms-conditioning
tags:
- lu-decomposition
- forward-substitution
- numerical-methods
stage: formal-systems
status: draft
---

# LU Decomposition and Forward/Back Substitution

## Core Idea
LU decomposition factors A = LU where L is lower triangular (result of Gaussian elimination) and U is upper triangular. To solve Ax = b: first solve Ly = b (forward substitution), then solve Ux = y (back substitution). LU is efficient for multiple right-hand sides and provides cost O(n²) when decomposed once. Pivoting is necessary for stability: PA = LU with permutation P.
