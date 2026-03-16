---
id: critical-points-extrema-saddle
title: Critical Points, Extrema, and Saddle Points
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector-properties
  type: hard
builds-toward:
- hessian-matrix-second-derivative-test
- unconstrained-optimization
tags:
- critical-points
- extrema
- saddle-points
stage: formal-systems
status: draft
---

# Critical Points, Extrema, and Saddle Points

## Core Idea
Critical points occur where ∇f = 0 (or partials fail to exist). A point is a local maximum or minimum (extremum) if f is larger or smaller than nearby values; it is a saddle point if it is larger in some directions and smaller in others. Finding critical points is the first step in optimization.

## Explainer

In single-variable calculus, you find maxima and minima by solving f'(x) = 0. In multivariable calculus, the gradient ∇f = (∂f/∂x, ∂f/∂y, ...) plays the role of the derivative, and the condition ∇f = 0 generalizes the flatness condition. A **critical point** is a point where every partial derivative is zero simultaneously — where the function has no slope in any direction. At such a point, the tangent plane to the graph of f is perfectly horizontal, just as a tangent line is horizontal at a single-variable extremum.

But here a new phenomenon appears that has no single-variable analogue: the **saddle point**. At a saddle, the gradient is zero but the point is neither a maximum nor a minimum. The classic example is f(x, y) = x² − y² at the origin: moving along the x-axis, the function increases (like a bowl); moving along the y-axis, it decreases (like an inverted bowl). The origin is the lowest point in one cross-section and the highest in another — a mountain pass, or the seat of a saddle. Your gradient knowledge tells you ∇f(0,0) = (0, 0), confirming it as a critical point, but the geometry reveals it is neither a maximum nor a minimum.

The challenge is that solving ∇f = 0 gives you a list of candidates — critical points — but does not tell you what kind each one is. You might have a local minimum (the surface curves up in all directions), a local maximum (curves down in all directions), or a saddle (curves up in some directions and down in others). Classifying requires more information about the curvature of the surface near the critical point, which is captured by the Hessian matrix — your next topic. The Hessian plays the role that the second derivative plays in single-variable calculus, extended to capture curvature in every direction.

Geometrically, you can build intuition by thinking of a topographic map. Peaks are local maxima, valleys are local minima, and mountain passes are saddle points. In all three cases, the gradient is zero (you are at a locally flat spot), but their local geometry differs fundamentally. In optimization, this matters enormously: an algorithm that only finds points where ∇f = 0 needs an additional test to confirm it has found a minimum rather than a saddle. Modern machine learning is full of high-dimensional saddle points, which is one reason optimization in neural networks is so subtle.
