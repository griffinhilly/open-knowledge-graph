---
id: gauss-seidel-iterative-method
title: Gauss-Seidel Iterative Method
domain: mathematics
course: numerical-analysis
prerequisites:
- id: jacobi-iterative-method
  type: hard
builds-toward:
- successive-over-relaxation-sor
- convergence-iterative-linear-solvers
tags:
- gauss-seidel
- iterative-solver
- fast-convergence
stage: advanced
status: draft
---

# Gauss-Seidel Iterative Method

## Core Idea
Gauss-Seidel improves Jacobi by using updated variable values immediately as they become available within each iteration. The method typically converges twice as fast as Jacobi for the same problems. Convergence is guaranteed for symmetric positive-definite matrices and diagonally dominant matrices, making it a practical alternative to direct methods for large sparse systems.
