---
id: numerical-least-squares
title: Numerical Least Squares
domain: mathematics
course: numerical-analysis
prerequisites:
- id: linear-regression
  type: soft
- id: matrix-operations
  type: hard
tags:
- least-squares
- linear-regression
- overdetermined
stage: abstract-reasoning
status: draft
---

# Numerical Least Squares

## Core Idea
Least squares solves overdetermined systems Ax = b (more equations than unknowns) by minimizing ‖Ax - b‖². The normal equations A^T Ax = A^T b can be ill-conditioned; stable alternatives use QR decomposition or SVD. Understanding numerical least squares is critical for robust data fitting and statistical applications.

## How It's Best Learned
Implement least squares using both normal equations and QR decomposition on an overdetermined system, comparing accuracy and conditioning.

## Common Misconceptions
- Thinking normal equations are always acceptable; large condition number of A^T A can destroy accuracy.
- Assuming any orthogonal factorization works equally well; QR and SVD have different numerical properties.
