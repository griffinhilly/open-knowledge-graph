---
id: lu-decomposition-numerical-numerical-analysis
title: LU Decomposition
domain: mathematics
course: numerical-analysis
prerequisites:
- id: gaussian-elimination-with-pivoting
  type: hard
builds-toward:
- condition-number-of-a-matrix
tags:
- lu-decomposition
- matrix-factorization
- linear-solver
stage: advanced
status: draft
---

# LU Decomposition

## Core Idea
LU decomposition factors a matrix as A = LU where L is lower triangular and U is upper triangular. This factorization is obtained via Gaussian elimination and allows efficient solution of multiple systems with the same coefficient matrix A. With partial pivoting, the factorization A = PLU provides numerical stability and is the basis for efficient linear system solvers.
