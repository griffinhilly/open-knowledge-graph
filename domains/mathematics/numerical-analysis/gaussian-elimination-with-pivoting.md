---
id: gaussian-elimination-with-pivoting
title: Gaussian Elimination with Pivoting
domain: mathematics
course: numerical-analysis
prerequisites:
- id: matrix-operations
  type: hard
builds-toward:
- condition-number-of-a-matrix
- numerical-least-squares
tags:
- gaussian-elimination
- pivoting
- linear-systems
stage: advanced
status: draft
---

# Gaussian Elimination with Pivoting

## Core Idea
Gaussian elimination solves linear systems Ax = b by transforming A to upper triangular form through elementary row operations, followed by back-substitution. Pivoting (selecting large entries as pivots and swapping rows/columns) is essential for numerical stability; without it, small pivots amplify rounding errors. Partial pivoting is the practical standard.
