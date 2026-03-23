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
stage: formal-systems
status: draft
---

# Successive Over-Relaxation (SOR)

## Core Idea
SOR accelerates Gauss-Seidel using a relaxation parameter ω: x_i^{(k+1)} = (1-ω)x_i^{(k)} + ω(GS_i^{(k+1)}) where GS_i is the Gauss-Seidel update. For ω > 1, the method overrelaxes the corrections, accelerating convergence when ω is chosen optimally. Optimal ω depends on spectral properties of the system and must be determined numerically or theoretically.

## Questions

```yaml
- question: "SOR with ω = 1.7 converges faster than Gauss-Seidel on a given system. A student increases ω to 2.3, expecting even faster convergence. What most likely happens?"
  type: multiple-choice
  options:
    - "Convergence improves further, since more overrelaxation means larger steps toward the solution"
    - "Convergence slows down but the method still converges, because ω = 2.3 is too aggressive"
    - "The method diverges, because the valid range for SOR convergence is 0 < ω < 2"
    - "The method converges to a different (incorrect) solution due to overshooting"
  answer: 2
  explanation: "The valid range for SOR convergence is strictly 0 < ω < 2. Setting ω ≥ 2 causes the spectral radius of the iteration matrix to exceed 1, and errors grow rather than shrink with each iteration. More overshoot is NOT always better — the convergence rate is a non-monotone function of ω with a unique optimal point. Overshooting ω_opt slightly still converges (slower), but ω ≥ 2 guarantees divergence."

- question: "For a Poisson equation on an n×n grid, optimal SOR requires O(n) iterations while Gauss-Seidel requires O(n²). What is the mathematical reason for this improvement?"
  type: multiple-choice
  options:
    - "SOR processes more unknowns per iteration by updating blocks rather than individual components"
    - "Optimal ω reduces the spectral radius of the iteration matrix from ~1 − π²/n² (Gauss-Seidel) to ~1 − 2π/n (SOR), so each iteration removes a larger fraction of the error"
    - "SOR uses a better initial guess than Gauss-Seidel by averaging the boundary conditions"
    - "SOR parallelizes the updates, reducing wall-clock time by a factor of n"
  answer: 1
  explanation: "Convergence rate is governed by the spectral radius ρ of the iteration matrix — the fraction of the error that survives each iteration. For Gauss-Seidel, ρ ≈ 1 − π²/n², meaning each step removes only a tiny fraction for large n, requiring O(1/ρ) ≈ O(n²) steps. With optimal ω, ρ_SOR ≈ 1 − 2π/n, so each step removes a much larger fraction, requiring only O(n) steps. The number of unknowns per iteration is unchanged — the improvement is entirely in how fast errors contract."

- question: "Setting ω < 1 in SOR (underrelaxation) always slows convergence and should be avoided."
  type: true-false
  answer: false
  explanation: "Underrelaxation (ω < 1) intentionally moves less than the Gauss-Seidel update suggests. This can be useful when Gauss-Seidel itself would diverge for a given system — underrelaxation damps the updates enough to stabilize convergence. While it is slower than optimal SOR, it may be the only way to obtain convergence at all for systems that are not diagonally dominant enough for Gauss-Seidel. Underrelaxation trades speed for stability."

- question: "The optimal relaxation parameter ω_opt for SOR depends on the specific linear system being solved — it cannot be determined without knowing something about the system's spectral structure."
  type: true-false
  answer: true
  explanation: "ω_opt = 2/(1 + sqrt(1 − ρ_J²)) where ρ_J is the spectral radius of the Jacobi iteration matrix, which depends entirely on the matrix A being solved. For regular finite-difference grids this can be computed analytically; for general matrices it must be estimated. Using the wrong ω still improves on Gauss-Seidel as long as ω is on the right side of 1, but significant underperformance or even divergence results from large estimation errors."

- question: "What does the relaxation parameter ω actually do in the SOR update, and why can overshooting the Gauss-Seidel update (ω > 1) accelerate convergence?"
  type: short-answer
  answer: "ω blends the current value and the Gauss-Seidel update: x_i^{new} = (1−ω)x_i^{old} + ω·(GS update). For ω = 1 you recover Gauss-Seidel. For ω > 1 you move further in the direction the Gauss-Seidel update indicated — overshooting — which works because the Gauss-Seidel update consistently points toward the true solution. By moving past the Gauss-Seidel point, SOR compensates for the undershooting that Gauss-Seidel inherently does, reducing the spectral radius and requiring fewer iterations to reach the desired accuracy."
  explanation: "The intuition is momentum: if each Gauss-Seidel step consistently undershoots the solution (common for elliptic PDE discretizations), then deliberately overshooting averages out to a more direct path. The analogy to a ball rolling in a bowl is useful: Gauss-Seidel takes cautious steps; SOR says 'since we're heading the right direction, take a bigger step.' The risk is that if ω is too large, the overshoot overshoots and the method oscillates or diverges."
```

## Explainer

You already know Gauss-Seidel: to solve Ax = b iteratively, update each component x_i in turn using the most recently computed values of all other components. It converges faster than Jacobi because it immediately uses updated values. But Gauss-Seidel can still converge slowly, especially for large, ill-conditioned systems. **Successive Over-Relaxation (SOR)** is a simple but powerful modification: instead of accepting the Gauss-Seidel update directly, you take a weighted blend of the old value and the Gauss-Seidel update, with a parameter ω controlling how aggressively you move.

The idea has an intuitive analogy: imagine a ball rolling toward the bottom of a bowl. Gauss-Seidel takes one step in the right direction and stops. SOR says: if you're already moving in the right direction, why not overshoot a little? If ω = 1, you recover Gauss-Seidel exactly. If ω > 1, you move further in the direction the update indicated — this is **overrelaxation**, and for many systems it dramatically accelerates convergence. If ω < 1, you move less than Gauss-Seidel suggests — this is **underrelaxation**, which can stabilize a method that would otherwise diverge. The valid range for convergence is 0 < ω < 2.

The convergence rate is governed by the **spectral radius** of the iteration matrix — the largest absolute eigenvalue. For Gauss-Seidel, this spectral radius determines how fast errors shrink each iteration. SOR with optimal ω_opt can dramatically reduce this spectral radius. For a model problem — the Poisson equation on a regular grid of size n × n — the optimal parameter is ω_opt = 2/(1 + sin(π/n)), and the spectral radius drops from approximately 1 − π²/n² (Gauss-Seidel) to approximately 1 − 2π/n (SOR). This changes the number of iterations needed from O(n²) to O(n), a quadratic speedup.

The challenge is finding ω_opt in practice. It depends on the spectral radius of the Jacobi iteration matrix, which must either be estimated from the system's structure (e.g., for finite-difference discretizations of elliptic PDEs, theoretical formulas exist) or estimated adaptively during the iteration. Using a suboptimal ω still helps as long as it's on the right side of 1, but overestimating ω_opt can cause the method to diverge. For modern large-scale problems, SOR has largely been superseded by Krylov subspace methods like conjugate gradient with preconditioning — but understanding SOR builds the conceptual foundation for why relaxation parameters appear in multigrid and other advanced solvers.
