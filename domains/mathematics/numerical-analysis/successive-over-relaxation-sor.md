---
id: successive-over-relaxation-sor
title: Successive Over-Relaxation (SOR)
domain: mathematics
course: numerical-analysis
prerequisites:
- id: gauss-seidel-iterative-method
  type: hard
builds-toward:
- convergence-iterative-linear-solvers
tags:
- sor
- over-relaxation
- acceleration
stage: advanced
status: draft
---

# Successive Over-Relaxation (SOR)

## Core Idea
SOR accelerates Gauss-Seidel using a relaxation parameter ω: x_i^{(k+1)} = (1-ω)x_i^{(k)} + ω(GS_i^{(k+1)}) where GS_i is the Gauss-Seidel update. For ω > 1, the method overrelaxes the corrections, accelerating convergence when ω is chosen optimally. Optimal ω depends on spectral properties of the system and must be determined numerically or theoretically.

## Explainer

You already know Gauss-Seidel: to solve Ax = b iteratively, update each component x_i in turn using the most recently computed values of all other components. It converges faster than Jacobi because it immediately uses updated values. But Gauss-Seidel can still converge slowly, especially for large, ill-conditioned systems. **Successive Over-Relaxation (SOR)** is a simple but powerful modification: instead of accepting the Gauss-Seidel update directly, you take a weighted blend of the old value and the Gauss-Seidel update, with a parameter ω controlling how aggressively you move.

The idea has an intuitive analogy: imagine a ball rolling toward the bottom of a bowl. Gauss-Seidel takes one step in the right direction and stops. SOR says: if you're already moving in the right direction, why not overshoot a little? If ω = 1, you recover Gauss-Seidel exactly. If ω > 1, you move further in the direction the update indicated — this is **overrelaxation**, and for many systems it dramatically accelerates convergence. If ω < 1, you move less than Gauss-Seidel suggests — this is **underrelaxation**, which can stabilize a method that would otherwise diverge. The valid range for convergence is 0 < ω < 2.

The convergence rate is governed by the **spectral radius** of the iteration matrix — the largest absolute eigenvalue. For Gauss-Seidel, this spectral radius determines how fast errors shrink each iteration. SOR with optimal ω_opt can dramatically reduce this spectral radius. For a model problem — the Poisson equation on a regular grid of size n × n — the optimal parameter is ω_opt = 2/(1 + sin(π/n)), and the spectral radius drops from approximately 1 − π²/n² (Gauss-Seidel) to approximately 1 − 2π/n (SOR). This changes the number of iterations needed from O(n²) to O(n), a quadratic speedup.

The challenge is finding ω_opt in practice. It depends on the spectral radius of the Jacobi iteration matrix, which must either be estimated from the system's structure (e.g., for finite-difference discretizations of elliptic PDEs, theoretical formulas exist) or estimated adaptively during the iteration. Using a suboptimal ω still helps as long as it's on the right side of 1, but overestimating ω_opt can cause the method to diverge. For modern large-scale problems, SOR has largely been superseded by Krylov subspace methods like conjugate gradient with preconditioning — but understanding SOR builds the conceptual foundation for why relaxation parameters appear in multigrid and other advanced solvers.
