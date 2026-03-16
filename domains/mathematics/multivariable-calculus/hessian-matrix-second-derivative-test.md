---
id: hessian-matrix-second-derivative-test
title: The Hessian Matrix and Second Derivative Test
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: critical-points-extrema-saddle
  type: hard
- id: higher-order-partials
  type: hard
builds-toward:
- unconstrained-optimization
tags:
- hessian
- second-derivative-test
- eigenvalues
stage: formal-systems
status: draft
---

# The Hessian Matrix and Second Derivative Test

## Core Idea
The Hessian matrix H = [[f_xx, f_xy], [f_yx, f_yy]] contains all second partial derivatives. At a critical point, the determinant det(H) and trace tr(H) determine whether it is a local max (det > 0, f_xx > 0), local min (det > 0, f_xx < 0), or saddle point (det < 0).

## Explainer

You already know how to find critical points of a multivariable function: set ∇f = 0 and solve. A critical point could be a local minimum, a local maximum, or a saddle point. In single-variable calculus, the second derivative test resolves this cleanly: f''(c) > 0 means the function curves upward, giving a local minimum; f''(c) < 0 means downward curvature, giving a local maximum. The **Hessian matrix** extends this idea to higher dimensions, packaging all second-order information into a matrix that captures curvature in every direction simultaneously.

For f: R² → R, the Hessian is H = [[f_xx, f_xy], [f_yx, f_yy]]. Since Clairaut's theorem guarantees f_xy = f_yx under continuity, H is symmetric. The question at a critical point is: does f curve upward in every direction (local min), downward in every direction (local max), or upward in some directions and downward in others (saddle)? That question is exactly whether H is **positive definite**, **negative definite**, or **indefinite** — which is determined by the signs of its eigenvalues. Positive definite means all eigenvalues are positive (upward curvature in every direction); negative definite means all eigenvalues are negative; indefinite means mixed signs.

For the 2×2 Hessian, the eigenvalue structure reduces to two computable numbers: det(H) = f_xx · f_yy − (f_xy)² and f_xx. If det(H) > 0 and f_xx > 0, the Hessian is positive definite: both eigenvalues are positive, the function curves upward in every direction from the critical point, and you have a **local minimum**. If det(H) > 0 and f_xx < 0, the Hessian is negative definite: both eigenvalues are negative, downward curvature everywhere, giving a **local maximum**. If det(H) < 0, the eigenvalues have opposite signs, giving a **saddle point** — one direction curves up, another down. When det(H) = 0, an eigenvalue is zero and the test is inconclusive.

The geometric intuition for saddle points is worth dwelling on. At a saddle the function increases along some paths through the critical point and decreases along others — like the center of a mountain pass, which is a local maximum along the ridge but a local minimum along the crossing direction. The Hessian test at such a point has one positive and one negative eigenvalue, hence negative determinant. In optimization applications, saddle points are critical to identify because gradient descent can stall near them, mistaking them for minima. For higher-dimensional functions, the full spectrum of the Hessian — not just its determinant — governs the classification, making eigenvalue analysis the natural tool.
