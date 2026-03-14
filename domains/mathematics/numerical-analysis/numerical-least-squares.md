---
id: numerical-least-squares
title: Numerical Least Squares
domain: mathematics
course: numerical-analysis
prerequisites:
- id: gaussian-elimination-with-pivoting
  type: hard
- id: matrix-operations
  type: hard
tags:
- least-squares
- overdetermined-systems
- qr-decomposition
stage: advanced
status: draft
---

# Numerical Least Squares

## Core Idea
Least squares solves overdetermined systems Ax = b (more equations than unknowns) by minimizing ||Ax - b||. The normal equations A^T Ax = A^T b give the solution but can be ill-conditioned. Orthogonal factorizations (QR, SVD) are more stable, avoiding the product A^T A that squares the condition number.
