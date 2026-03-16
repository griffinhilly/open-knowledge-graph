---
id: linearization-nonlinear-systems
title: Linearization of Nonlinear Systems Near Equilibria
domain: mathematics
course: differential-equations
prerequisites:
- id: stability-classification
  type: hard
- id: partial-derivatives
  type: hard
tags:
- linearization
- jacobian
- local-analysis
stage: advanced
status: draft
---

# Linearization of Nonlinear Systems Near Equilibria

## Core Idea
For a nonlinear system dx/dt = f(x) near equilibrium x*, compute the Jacobian J = ∂f/∂x at x*. The linearized system dx/dt ≈ J(x - x*) determines local behavior. If all eigenvalues of J have non-zero real parts, the nonlinear stability matches the linear prediction (Hartman-Grobman theorem). Linearization provides local information when global analysis is infeasible.

## Explainer

From your work on stability classification, you know how to fully analyze a linear system ẋ = Ax: find eigenvalues of A, determine whether their real parts are positive, negative, or zero, and classify the equilibrium at the origin as a stable node, unstable node, saddle, spiral, or center. For a nonlinear system ẋ = f(x), the same classification is not directly available — f is not a matrix, and eigenvalues of a nonlinear system are not defined. Linearization closes this gap by approximating f with the best linear approximation near an equilibrium.

The approximation tool is the **Jacobian matrix**: J = ∂f/∂x evaluated at the equilibrium x*. Each entry J_{ij} = ∂fᵢ/∂xⱼ(x*) measures how the i-th component of f changes with the j-th variable, evaluated at the fixed point. This comes directly from your prerequisite on partial derivatives — the Jacobian is the multivariable generalization of the derivative. Near x*, the Taylor expansion of f gives f(x) ≈ f(x*) + J(x − x*), and since f(x*) = 0 at an equilibrium, the system becomes ẋ ≈ J(x − x*). With the substitution u = x − x*, this is the linear system u̇ = Ju, which you already know how to classify.

The **Hartman-Grobman theorem** tells you when this linearization gives reliable local stability information: if all eigenvalues of J have **non-zero real parts** (a condition called hyperbolicity), the qualitative phase portrait of the nonlinear system near x* is topologically equivalent to the portrait of the linearization. In other words, if the linearization says "stable spiral," the nonlinear system really does spiral inward near x*. Hyperbolicity fails at centers (purely imaginary eigenvalues) and at degenerate cases (zero eigenvalues) — in those cases, the linear approximation is ambiguous about stability, and higher-order terms in the Taylor expansion must be examined.

The procedure is: find all equilibria by solving f(x*) = 0, compute J at each equilibrium, find the eigenvalues of each J, classify each equilibrium from the eigenvalues, and note any non-hyperbolic cases requiring further analysis. For a 2D system dx/dt = P(x,y), dy/dt = Q(x,y), the Jacobian is the 2×2 matrix [[∂P/∂x, ∂P/∂y], [∂Q/∂x, ∂Q/∂y]], and the eigenvalues follow from the characteristic polynomial λ² − (trace)λ + det = 0. The trace and determinant of J provide the fastest route to classification: det < 0 means a saddle; det > 0 and trace < 0 means stable; det > 0 and trace > 0 means unstable; the discriminant distinguishes spirals from nodes. Linearization converts a hard nonlinear problem into a sequence of linear ones you already know how to solve.
