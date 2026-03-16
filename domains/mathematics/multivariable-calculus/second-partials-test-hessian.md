---
id: second-partials-test-hessian
title: Second Partial Test and the Hessian
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: second-partials-test
  type: hard
- id: mixed-partials-clairaut
  type: hard
builds-toward:
- optimization-multivariable-basics
tags:
- hessian
- classification
stage: formal-systems
status: draft
---

# Second Partial Test and the Hessian

## Core Idea
The Hessian H = [[f_xx, f_xy], [f_xy, f_yy]] classifies critical points. If det(H) > 0 and f_xx > 0, it's a local minimum. If det(H) > 0 and f_xx < 0, it's a maximum. If det(H) < 0, it's a saddle point.

## Explainer

In single-variable calculus, the second derivative test classifies critical points: if f′(a) = 0 and f′′(a) > 0, the graph is concave up at a, so a is a local minimum; if f′′(a) < 0, it's concave down, so a is a local maximum. For functions of two variables, you already know that critical points satisfy ∇f = 0 (both partial derivatives are zero). The **Hessian matrix** is the multivariable analogue of the second derivative — it captures the curvature of the surface in all directions simultaneously.

The **Hessian** at a critical point (a, b) is the 2×2 matrix H = [[f_xx, f_xy], [f_xy, f_yy]], where all second partials are evaluated at (a, b). By Clairaut's theorem (which you have studied), f_xy = f_yx under smoothness conditions, so H is symmetric. The entries measure curvature in specific directions: f_xx is the concavity along the x-axis, f_yy is the concavity along the y-axis, and f_xy measures how the x-slope changes as y varies — a cross-curvature or "twist."

The classification hinges on the **determinant** D = det(H) = f_xx · f_yy − (f_xy)². Think of D as the product of curvatures in the two "principal" directions of the surface (the directions where the mixed terms vanish). If D > 0, the surface curves the same way in all directions at that point — it's bowl-shaped (either upward or downward), giving a local extremum. The sign of f_xx (or equivalently f_yy when D > 0) tells you which: positive means bowl-opening-upward (local minimum), negative means bowl-opening-downward (local maximum). If D < 0, the surface curves upward in one direction and downward in another — a **saddle point**, like the surface of a mountain pass that goes up toward ridges but down toward valleys.

Here is the geometric intuition for why D = f_xx · f_yy − (f_xy)² is the right quantity. A quadratic function ax² + 2bxy + cy² (which approximates f near a critical point) curves upward in every direction if and only if a > 0 and ac − b² > 0. The determinant condition is exactly testing whether this quadratic form is positive definite (curves up everywhere), negative definite (curves down everywhere), or indefinite (saddle). When D = 0, the test is inconclusive — you need higher-order information.

The Hessian matrix generalizes naturally beyond two variables: for a function of n variables, H is an n×n symmetric matrix of second partials, and the classification criterion generalizes to checking whether H is positive definite (local min), negative definite (local max), or indefinite (saddle). This is the heart of multivariable optimization, and understanding the Hessian as a curvature object — not just as a formula to memorize — is what makes it usable in more complex settings like constrained optimization and machine learning loss landscapes.
