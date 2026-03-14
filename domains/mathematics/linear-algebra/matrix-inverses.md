---
id: matrix-inverses
title: Matrix Inverses
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrix-multiplication
  type: hard
- id: determinants-2x2-3x3
  type: hard
builds-toward:
- linear-transformations
- matrix-representation-linear-transformations
tags:
- matrix-inverse
- invertibility
- nonsingular
stage: formal-systems
status: draft
---

# Matrix Inverses

## Core Idea
An n × n matrix A is invertible if there exists A⁻¹ such that AA⁻¹ = A⁻¹A = I. Invertibility is equivalent to det(A) ≠ 0, full rank, and having trivial null space. The inverse can be computed via the adjugate formula, Gauss–Jordan elimination, or LU decomposition.
