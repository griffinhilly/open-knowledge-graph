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

## Explainer

You've already studied the Jacobi method, which solves a linear system Ax = b iteratively by isolating each variable and updating using all values from the *previous* iteration. The key insight of Jacobi is that if the matrix A is diagonally dominant, this process converges: each sweep brings the current estimate closer to the true solution. The Gauss-Seidel method asks a simple question: once you've computed the updated x_1 in this sweep, why wait to use it when computing x_2?

In Jacobi, all updates for iteration k+1 are computed using only iteration-k values — a batch update. In Gauss-Seidel, you update x_1 first and immediately use the fresh x_1 when computing x_2, then use both updated x_1 and x_2 for x_3, and so on through all n variables. The update formula x_i^{(k+1)} = (b_i − Σ_{j<i} A_{ij}x_j^{(k+1)} − Σ_{j>i} A_{ij}x_j^{(k)}) / A_{ii} makes this explicit: the first sum uses already-updated values (j < i), the second uses old values (j > i). Each component update incorporates the best available information.

Intuitively, Jacobi is like a committee where everyone polls the previous meeting's results before submitting new opinions; Gauss-Seidel is like an assembly line where each person's update immediately informs the next person's decision. The more current information flows through each sweep, and the result is roughly twice as many iterations eliminated per unit of computation. For the same convergence criterion, Gauss-Seidel typically requires about half as many sweeps as Jacobi.

The convergence conditions are similar: **diagonal dominance** guarantees convergence for both methods, and for symmetric positive definite matrices Gauss-Seidel always converges. The cost is sequential dependency: because each x_i update depends on freshly updated x_j for j < i, all n updates must run in order within each sweep. Jacobi's "stale" values, counterintuitively, are an advantage when parallel hardware is available — each Jacobi update can be computed independently, while Gauss-Seidel must wait. This trade-off between convergence speed and parallelizability motivates further methods like **successive over-relaxation** (SOR), which extrapolates each Gauss-Seidel update by a factor ω to accelerate convergence even further.
