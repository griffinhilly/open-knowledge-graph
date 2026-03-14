---
id: jacobi-iterative-method
title: Jacobi Iterative Method
domain: mathematics
course: numerical-analysis
prerequisites:
- id: fixed-point-iteration
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- gauss-seidel-method
- convergence-iterative-methods
tags:
- jacobi
- iterative
- linear-systems
stage: abstract-reasoning
status: draft
---

# Jacobi Iterative Method

## Core Idea
The Jacobi method solves Ax = b by iterating x^{(k+1)} = D⁻¹(b - (L+U)x^{(k)}), where D is A's diagonal and L, U are its lower and upper parts. Each component is updated simultaneously using values from the previous iteration. Jacobi is simple to implement and parallelize but converges slowly unless A is diagonally dominant or well-conditioned.
