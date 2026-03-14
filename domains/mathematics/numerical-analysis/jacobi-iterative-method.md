---
id: jacobi-iterative-method
title: Jacobi Iterative Method
domain: mathematics
course: numerical-analysis
prerequisites:
- id: matrix-operations
  type: hard
builds-toward:
- gauss-seidel-iterative-method
- convergence-iterative-linear-solvers
tags:
- jacobi-method
- iterative-solver
- splitting-method
stage: advanced
status: draft
---

# Jacobi Iterative Method

## Core Idea
The Jacobi method solves Ax = b iteratively by rearranging each equation to isolate one variable and iterating. Writing A = D + L + U where D is diagonal, the iteration is x^{(k+1)} = D⁻¹(b - (L+U)x^{(k)}). Convergence is guaranteed if A is diagonally dominant. The method is simple and highly parallelizable but often slower than direct methods.
