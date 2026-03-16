---
id: critical-points-multivariable-classification
title: Critical Points and Classification of Extrema
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector-definition
  type: hard
- id: critical-points-multivariable
  type: hard
builds-toward:
- second-partials-test-extrema
tags:
- critical-points
- extrema
- saddle-points
stage: formal-systems
status: draft
---

# Critical Points and Classification of Extrema

## Core Idea
A critical point (a, b) of f(x, y) satisfies ∇f(a, b) = 0 (or ∇f is undefined). Critical points are candidates for local maxima, local minima, or saddle points. Every continuous function on a closed bounded set attains its absolute maximum and minimum.

## Explainer

From your prerequisite on the gradient, you know that ∇f at a point gives the direction and magnitude of steepest ascent. A **critical point** is where this steepest-ascent direction ceases to exist in the usual sense: the gradient is zero, meaning the function is instantaneously flat in every direction. In single-variable calculus you found critical points where f′(x) = 0; the multivariable condition ∇f = 0 is the exact generalization — it requires both ∂f/∂x = 0 and ∂f/∂y = 0 simultaneously.

The three types of critical point correspond to three distinct topographic shapes. A **local minimum** looks like the bottom of a bowl: the function rises in every direction away from the point. A **local maximum** looks like the top of a hill: the function falls in every direction. A **saddle point** looks like a mountain pass: the function rises in some directions and falls in others. The gradient is zero at all three, so the gradient condition alone cannot tell them apart — that requires additional information about the second-order behavior.

The **second derivative test** for two variables uses the **Hessian matrix** H, whose entries are the second partial derivatives: H = [[f_xx, f_xy], [f_yx, f_yy]]. The **discriminant** D = f_xx · f_yy − (f_xy)² captures the Hessian's determinant. If D > 0 and f_xx > 0, the point is a local minimum (bowl opening upward). If D > 0 and f_xx < 0, it's a local maximum (bowl opening downward). If D < 0, it's a saddle point. If D = 0, the test is inconclusive — higher-order methods are needed. The intuition: D > 0 means both principal curvatures have the same sign (pure bowl), while D < 0 means they have opposite signs (saddle).

For optimization on a closed bounded region, the story extends beyond interior critical points. By the extreme value theorem, a continuous function on a compact set attains its absolute extrema somewhere. The candidates are: all interior critical points where ∇f = 0, and all points on the boundary. The boundary is typically a curve, so you parameterize it and apply single-variable optimization there. Checking all candidates and comparing values gives the absolute maximum and minimum — this is the complete algorithm for constrained optimization on closed bounded domains.
