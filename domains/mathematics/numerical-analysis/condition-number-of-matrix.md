---
id: condition-number-of-matrix
title: Condition Number of a Matrix
domain: mathematics
course: numerical-analysis
prerequisites:
- id: condition-number
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- jacobi-iterative-method
tags:
- condition-number
- matrix
- ill-conditioning
stage: abstract-reasoning
status: draft
---

# Condition Number of a Matrix

## Core Idea
The condition number of a matrix A is κ(A) = ‖A‖ ‖A⁻¹‖, measuring how much small perturbations in A or b affect the solution x to Ax = b. If κ(A) is large, the system is ill-conditioned: small changes in inputs produce large changes in outputs. The condition number depends on the chosen norm; large κ(A) indicates potential numerical difficulties regardless of algorithm.
