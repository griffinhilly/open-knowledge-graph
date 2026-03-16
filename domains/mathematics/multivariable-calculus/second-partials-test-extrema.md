---
id: second-partials-test-extrema
title: Second Partial Test for Local Extrema (Hessian)
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: higher-order-partials-mixed
  type: hard
- id: critical-points-multivariable-classification
  type: hard
builds-toward:
- constrained-optimization-lagrange
tags:
- second-derivative-test
- hessian
- eigenvalues
stage: formal-systems
status: draft
---

# Second Partial Test for Local Extrema (Hessian)

## Core Idea
At critical point (a, b), compute the Hessian matrix H = [[f_xx, f_xy], [f_xy, f_yy]]. If det(H) > 0 and f_xx > 0, it's a local min; if f_xx < 0, local max. If det(H) < 0, it's a saddle point. If det(H) = 0, test is inconclusive.

## Explainer

In single-variable calculus, the second derivative test says: if f'(c) = 0 and f''(c) > 0, then c is a local minimum. The sign of the second derivative tells you the concavity — whether the function curves upward (bowl) or downward (hill) near the critical point. The second partials test generalizes this to functions of two variables, but the geometry is richer: near a critical point of f(x, y), the surface could curve upward in every direction (a local minimum), downward in every direction (a local maximum), or upward in some directions and downward in others (a saddle point, shaped like a mountain pass).

From your work on higher-order mixed partials, you know that f_xy = f_yx for smooth functions. The **Hessian matrix** H packages all this second-order information:

H = [[f_xx, f_xy], [f_xy, f_yy]]

The determinant D = det(H) = f_xx · f_yy − (f_xy)² is the key quantity. Think about what D measures geometrically. If D > 0, both eigenvalues of H have the same sign — meaning the surface curves the same way (both up or both down) in every cross-sectional direction through the critical point. Then f_xx (or equivalently f_yy) tells you which way: f_xx > 0 means concave up in all directions (local min), f_xx < 0 means concave down in all directions (local max). If D < 0, the eigenvalues have opposite signs — the surface curves up in some directions and down in others, producing a **saddle point**. The function increases if you walk one way, decreases if you walk another way; there is no local extremum.

A useful analogy: D is like the discriminant of the second-order behavior. Just as the discriminant of a quadratic b² − 4ac tells you whether roots are real or complex, D = f_xx f_yy − f_xy² tells you whether the critical point is a "definite" extremum or an indefinite saddle. The cross-term f_xy encodes the "twisting" of the surface; a large f_xy relative to f_xx and f_yy can turn a point that looks like an extremum along the axes into a saddle.

The test is applied in two steps: first locate critical points by solving ∇f = 0 (both partial derivatives vanish), then evaluate D and f_xx at each critical point. The inconclusive case D = 0 requires other methods — higher-order analysis, comparison with nearby values, or geometric inspection. This test extends conceptually to higher dimensions via the eigenvalues of the Hessian: a local min requires all eigenvalues positive (positive definite), a local max requires all negative (negative definite), and a saddle requires mixed signs (indefinite).
