---
id: unconstrained-optimization
title: 'Unconstrained Optimization: Finding Extrema'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: hessian-matrix-second-derivative-test
  type: hard
builds-toward:
- lagrange-multipliers
tags:
- optimization
- extrema
- applications
stage: formal-systems
status: draft
---

# Unconstrained Optimization: Finding Extrema

## Core Idea
To optimize f(x, y) without constraints: (1) find critical points by setting ∇f = 0, (2) classify each using the Hessian test, (3) check boundary behavior. This process identifies global maxima and minima.

## Explainer

Optimization in single-variable calculus works by finding points where f'(x) = 0 (critical points) and then applying the second derivative test to classify them as local max, min, or neither. Multivariable unconstrained optimization follows exactly the same logical structure, with the gradient replacing the derivative and the Hessian replacing the second derivative.

The first step is finding **critical points**: solve ∇f = 0, meaning both ∂f/∂x = 0 and ∂f/∂y = 0 simultaneously. Geometrically, the gradient points in the direction of steepest ascent; setting it to zero means the surface is locally "flat" at that point — neither ascending nor descending in any direction. Solving the system ∂f/∂x = 0 and ∂f/∂y = 0 gives you the candidate locations for extrema. This is typically a system of nonlinear equations, and solving it may require algebraic manipulation, substitution, or numerical methods.

The second step is **classifying each critical point** using the Hessian matrix H, whose entries are the second partial derivatives: H = [[f_xx, f_xy], [f_yx, f_yy]]. You already know that the Hessian encodes the local curvature of f in all directions. The second derivative test says: compute D = f_xx · f_yy − (f_xy)². If D > 0 and f_xx > 0, the point is a **local minimum**. If D > 0 and f_xx < 0, it is a **local maximum**. If D < 0, it is a **saddle point** — like the center of a mountain pass, which is a minimum along one direction but a maximum along another. If D = 0, the test is inconclusive. The quantity D is the determinant of H, and its sign tells you whether H is positive definite (bowl-shaped upward), negative definite (bowl-shaped downward), or indefinite (saddle).

The third step — checking boundary behavior — depends on the domain. If f is defined on all of ℝ² and f → ∞ in all directions, then a local minimum is a global minimum. But if the domain is bounded, you must also examine what happens as you approach the boundary (or, on a closed bounded domain, optimize f on the boundary using single-variable techniques). A critical point in the interior is only guaranteed to be a **global** optimum if the function behaves appropriately at infinity or at the boundary. Forgetting this step is the most common source of wrong answers in applied optimization problems.
