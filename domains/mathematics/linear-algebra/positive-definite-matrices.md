---
id: positive-definite-matrices
title: Positive Definite Matrices
domain: mathematics
course: linear-algebra
prerequisites:
- id: symmetric-matrices-properties
  type: hard
builds-toward:
- least-squares-approximation
tags:
- positive-definite
- quadratic-forms
stage: formal-systems
status: draft
---

# Positive Definite Matrices

## Core Idea
A symmetric matrix A is positive definite if xᵀAx > 0 for all nonzero x. Equivalently, all eigenvalues are positive. Positive definite matrices are invertible, have a unique Cholesky decomposition A = LLᵀ, and define a valid inner product. The normal equations AᵀAx = Aᵀb have a unique solution when A has full column rank (AᵀA is positive definite).
