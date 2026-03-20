---
id: successive-over-relaxation
title: Successive Over-Relaxation (SOR)
domain: mathematics
course: numerical-analysis
prerequisites:
- id: gauss-seidel-method
  type: hard
builds-toward:
- convergence-iterative-methods
tags:
- sor
- over-relaxation
- iterative
stage: formal-systems
status: draft
---

# Successive Over-Relaxation (SOR)

## Core Idea
SOR accelerates Gauss-Seidel by introducing a relaxation parameter ω: x_i^{(k+1)} = (1-ω)x_i^{(k)} + ω·(Gauss-Seidel step). For 0 < ω < 2, SOR can significantly reduce iterations needed for convergence. The optimal ω depends on the matrix eigenvalues; poor choice of ω can slow or even prevent convergence.

## Explainer

From the Gauss-Seidel method, you know that solving Ax = b iteratively means updating each variable x_i in turn using the latest available values of the other variables. Gauss-Seidel converges faster than Jacobi because it uses fresh updates immediately, but for large sparse systems — especially those arising from discretized PDEs — even Gauss-Seidel can require thousands of iterations. SOR's insight is simple: if Gauss-Seidel is moving in the right direction, why not take a bigger step in that direction?

The **relaxation parameter** ω controls the step size. At each update, the SOR formula is x_i^{(k+1)} = (1 − ω) x_i^{(k)} + ω · x_i^{GS}, where x_i^{GS} is the Gauss-Seidel update. When ω = 1, you recover plain Gauss-Seidel. When ω > 1, you **over-relax**: you move past the Gauss-Seidel update by interpolating (or extrapolating) further in that direction, attempting to "leap" toward the solution. When ω < 1 (under-relaxation), you take a smaller step — useful for stabilizing a method that would otherwise diverge, though not the typical application of SOR.

Why does over-relaxation help? The convergence rate of iterative methods is governed by the **spectral radius** of the iteration matrix — the largest eigenvalue in absolute value. For Gauss-Seidel applied to problems with a known structure (like the five-point stencil for Laplace's equation on a rectangle), the spectral radius ρ is close to 1, meaning convergence is slow. The optimal SOR parameter is ω_opt = 2 / (1 + √(1 − ρ²)), which can reduce the spectral radius from something near 1 to something near 1 − O(h) where h is the grid spacing. In practice, this accelerates convergence by an order of magnitude: where Gauss-Seidel might need O(N²) iterations for an N × N grid, optimal SOR needs only O(N).

The critical challenge is choosing ω. The formula ω_opt requires knowing the spectral radius of the Gauss-Seidel iteration matrix, which is only analytically available for special matrix structures (those with a "Property A" and consistent ordering). For general matrices, ω must be estimated experimentally — by running a few iterations and observing the convergence rate — or by more sophisticated adaptive methods. Choosing ω poorly (say, ω > 2) causes divergence, since the SOR iteration is guaranteed to converge only for 0 < ω < 2. SOR laid the groundwork for understanding **preconditioning** and **multigrid** methods, which address the same slow-convergence problem through more powerful approaches.
