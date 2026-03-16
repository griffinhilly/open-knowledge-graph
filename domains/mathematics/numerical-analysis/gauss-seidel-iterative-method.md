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

## Explainer

In the Jacobi method you studied, each new iteration computes all updated values simultaneously from the previous iteration's values. It's like updating a spreadsheet where every cell reads only the old values, then all cells refresh at once. **Gauss-Seidel** makes one conceptually simple change: as soon as you compute an updated value for variable x₁, you immediately use that new value when computing x₂, and so on through the system. Within a single sweep, each variable is computed using the most current estimates available.

To see why this helps, consider a 3×3 system. In Jacobi, when you compute the new x₂, you use the old x₁ even though you just computed a better x₁. Gauss-Seidel feeds the improved x₁ forward immediately. This isn't just slightly faster — it typically means the error shrinks in roughly half as many iterations. The spectral radius of the Gauss-Seidel iteration matrix is approximately the square of the Jacobi spectral radius for many common matrix types, which translates directly into faster convergence. In practice, this halving of iteration count often matters more than theoretical constants.

The convergence conditions for Gauss-Seidel are the same as for Jacobi: **strict diagonal dominance** (each diagonal entry is larger in absolute value than the sum of the other entries in its row) guarantees convergence, and so does **symmetric positive-definiteness**. However, Gauss-Seidel can converge even when Jacobi diverges, and vice versa — they are not strictly comparable in general, though for the most practically important matrix classes (SPD and diagonally dominant), Gauss-Seidel wins. One important limitation: the method is inherently sequential, since each update depends on the previous update in the same sweep. This makes parallelization harder than for Jacobi.

The update formula for Gauss-Seidel solving Ax = b is: for each i, set xᵢ ← (bᵢ − Σ_{j<i} aᵢⱼxⱼ^{new} − Σ_{j>i} aᵢⱼxⱼ^{old}) / aᵢᵢ. The left sum uses already-updated values from this sweep; the right sum uses holdovers from the previous sweep. This single formula captures the key idea: Gauss-Seidel is Jacobi with a greedy update policy. For large, sparse, well-conditioned linear systems — such as those arising in finite element methods or discretized PDEs — Gauss-Seidel is a practical first choice before turning to more sophisticated preconditioned Krylov methods.
