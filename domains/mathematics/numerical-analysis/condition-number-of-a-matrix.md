---
id: condition-number-of-a-matrix
title: Condition Number of a Matrix
domain: mathematics
course: numerical-analysis
prerequisites:
- id: gaussian-elimination-with-pivoting
  type: hard
builds-toward:
- jacobi-iterative-method
tags:
- condition-number
- matrix-sensitivity
- ill-conditioning
stage: advanced
status: draft
---

# Condition Number of a Matrix

## Core Idea
The condition number κ(A) = ||A|| ||A⁻¹|| measures sensitivity of the linear system Ax = b to perturbations in A and b. Relative error in x is bounded by approximately κ(A) times relative error in data. Large condition numbers indicate ill-conditioned problems; small perturbations cause large solution changes regardless of algorithm choice.
