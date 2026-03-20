---
id: linearization-of-nonlinear-systems
title: Linearization of Nonlinear Systems
domain: mathematics
course: differential-equations
prerequisites:
- id: stability-classification
  type: hard
- id: partial-derivatives
  type: hard
builds-toward: []
tags:
- nonlinear
- approximation
- local-analysis
stage: advanced
status: draft
---
# Linearization of Nonlinear Systems

## Core Idea
For a nonlinear system y' = f(y), linearize near an equilibrium y* by computing the Jacobian matrix J = ∇f(y*). The linearized system y' ≈ J(y - y*) reveals local stability; if J has eigenvalues with Re(λ) ≠ 0, the nonlinear equilibrium inherits the stability of the linearized system.

## Explainer

From stability classification, you can fully analyze linear systems x' = Ax: find the eigenvalues of A, and the signs of their real parts tell you whether the equilibrium at the origin is a stable node, unstable node, saddle, or spiral. Nonlinear systems are far harder in general — their phase portraits can be wildly complicated. But *near* a specific equilibrium, every smooth nonlinear system looks approximately linear, and this approximation is good enough to determine local stability. Linearization is the technique that makes this precise.

The idea comes directly from your work with partial derivatives. If f : Rⁿ → Rⁿ is a smooth vector field and y* is an equilibrium (so f(y*) = 0), then the **Taylor expansion** of f near y* starts: f(y) ≈ f(y*) + J(y − y*) + higher-order terms, where J = ∇f(y*) is the **Jacobian matrix** — the matrix of all first partial derivatives of f, evaluated at y*. Since f(y*) = 0, we get f(y) ≈ J(y − y*). Setting u = y − y* (the displacement from equilibrium), the nonlinear system y' = f(y) becomes approximately the linear system u' = Ju. This linear system you already know how to analyze completely.

The key theorem is that if every eigenvalue of J has a nonzero real part (the equilibrium is **hyperbolic**), then the qualitative behavior of the nonlinear system near y* is topologically the same as the behavior of the linear approximation. A stable node in the linearization means the nonlinear equilibrium is locally asymptotically stable; a saddle in the linearization means the nonlinear equilibrium is unstable; a source means unstable. The classification table from linear systems carries over exactly — stable node, unstable node, saddle, stable spiral, unstable spiral. The only gap is the **center case**: if J has pure imaginary eigenvalues (zero real part), the linear approximation gives a center, but the nonlinear system could be a center, a stable spiral, or an unstable spiral depending on higher-order terms. This is why the hyperbolicity condition Re(λ) ≠ 0 is essential.

In practice, linearization is a three-step process: (1) find the equilibria by solving f(y*) = 0, (2) compute the Jacobian J = ∇f and evaluate it at each equilibrium, (3) find the eigenvalues of J and apply the linear stability classification. For a 2D system dx/dt = P(x, y), dy/dt = Q(x, y), the Jacobian is the 2×2 matrix [[∂P/∂x, ∂P/∂y], [∂Q/∂x, ∂Q/∂y]] evaluated at the equilibrium point. This technique is the standard first tool for analyzing nonlinear systems in applications ranging from population ecology to mechanical engineering to epidemiology.
