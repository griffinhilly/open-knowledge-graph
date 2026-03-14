---
id: gauss-seidel-method
title: Gauss-Seidel Method
domain: mathematics
course: numerical-analysis
prerequisites:
- id: jacobi-iterative-method
  type: hard
builds-toward:
- successive-over-relaxation
- convergence-iterative-methods
tags:
- gauss-seidel
- iterative
- linear-systems
stage: abstract-reasoning
status: draft
---

# Gauss-Seidel Method

## Core Idea
The Gauss-Seidel method improves Jacobi by using updated values immediately: x_i^{(k+1)} = (b_i - Σ_{j<i} A_{ij}x_j^{(k+1)} - Σ_{j>i} A_{ij}x_j^{(k)})/A_{ii}. By exploiting the latest available values, Gauss-Seidel typically converges roughly twice as fast as Jacobi. The trade-off is that updates must be sequential, making parallelization difficult.
