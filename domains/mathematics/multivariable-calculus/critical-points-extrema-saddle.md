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
status: validated
---

# Critical Points, Extrema, and Saddle Points

## Core Idea
Critical points occur where ∇f = 0 (or partials fail to exist). A point is a local maximum or minimum (extremum) if f is larger or smaller than nearby values; it is a saddle point if it is larger in some directions and smaller in others. Finding critical points is the first step in optimization.

## Questions

```yaml
- question: "For f(x, y) = x² − y², you compute ∇f(0,0) = (0, 0). What type of critical point is the origin?"
  type: multiple-choice
  options:
    - "A local minimum — the function curves upward near the origin"
    - "A local maximum — the function curves downward near the origin"
    - "A saddle point — the function increases in some directions and decreases in others"
    - "Not a critical point — the gradient must be nonzero to classify it"
  answer: 2
  explanation: "Along the x-axis (y=0), f = x² increases away from the origin — like a valley. Along the y-axis (x=0), f = −y² decreases away from the origin — like a ridge. Since f is larger than f(0,0) in some directions and smaller in others, the origin is a saddle point, not an extremum. Option D is wrong: ∇f = 0 is exactly the condition defining a critical point. The origin is a critical point; the issue is that ∇f = 0 alone doesn't tell you what kind."

- question: "Why does the saddle point phenomenon have no analogue in single-variable calculus?"
  type: multiple-choice
  options:
    - "Single-variable functions can have saddle points, but they are called inflection points instead"
    - "In one dimension, there is only one direction to move from a critical point, so the function either increases or decreases — there are no competing directions for a saddle to exist"
    - "Single-variable calculus uses a different definition of critical point that excludes saddles"
    - "Saddle points only occur when the Hessian has negative eigenvalues, which is impossible in 1D"
  answer: 1
  explanation: "A saddle point requires the function to increase in some directions and decrease in others. In one dimension, 'direction' means only left or right. If f'(c) = 0 at a critical point, the second derivative test tells you whether the function curves up (minimum), curves down (maximum), or has a degenerate case (inflection point at a horizontal tangent). But there are no competing spatial directions — the 'saddle' structure requires at least two independent directions. Option A conflates inflection points (where curvature changes sign in 1D) with saddle points (a multidimensional phenomenon)."

- question: "If ∇f(p) = 0 at a point p, then p must be either a local maximum or a local minimum."
  type: true-false
  answer: false
  explanation: "∇f = 0 is a necessary condition for a local extremum but not a sufficient one. Saddle points also satisfy ∇f = 0 yet are neither maxima nor minima. The canonical example is f(x,y) = x² − y² at the origin: the gradient vanishes, but the function increases along the x-axis and decreases along the y-axis. To determine which case applies, you need additional information about the curvature — provided by the Hessian matrix and the second-derivative test."

- question: "Every local minimum of a differentiable function f: ℝ² → ℝ is a critical point."
  type: true-false
  answer: true
  explanation: "This is the multivariable generalization of Fermat's theorem: if f has a local extremum at an interior point and is differentiable there, then ∇f = 0 at that point. The reasoning is that each partial derivative must be zero — if ∂f/∂x ≠ 0, then moving in the x-direction from the point would increase or decrease f, contradicting it being a local minimum. So ∇f = 0 is necessary (but not sufficient) for a local extremum."

- question: "Why is finding all points where ∇f = 0 not sufficient to identify the minima of a function? What additional step is required?"
  type: short-answer
  answer: "Solving ∇f = 0 gives a list of critical point candidates — but each candidate could be a local minimum, local maximum, or saddle point. To classify each one, you need the Hessian matrix (the matrix of second-order partial derivatives), which captures the curvature of the surface in every direction. The second-derivative test uses the Hessian's determinant and leading entry to distinguish these cases: positive definite Hessian → local minimum; negative definite → local maximum; indefinite → saddle point."
  explanation: "This distinction is practically crucial in optimization: an algorithm that stops at ∇f = 0 may have found a saddle rather than a minimum. In high-dimensional problems like neural network training, saddle points are extremely common and can stall gradient-based optimizers. The Hessian test is the theoretical tool; in practice, other methods (second-order optimization, checking the sign of the function change) are used to verify that a critical point is truly a minimum."
```

## Explainer

In single-variable calculus, you find maxima and minima by solving f'(x) = 0. In multivariable calculus, the gradient ∇f = (∂f/∂x, ∂f/∂y, ...) plays the role of the derivative, and the condition ∇f = 0 generalizes the flatness condition. A **critical point** is a point where every partial derivative is zero simultaneously — where the function has no slope in any direction. At such a point, the tangent plane to the graph of f is perfectly horizontal, just as a tangent line is horizontal at a single-variable extremum.

But here a new phenomenon appears that has no single-variable analogue: the **saddle point**. At a saddle, the gradient is zero but the point is neither a maximum nor a minimum. The classic example is f(x, y) = x² − y² at the origin: moving along the x-axis, the function increases (like a bowl); moving along the y-axis, it decreases (like an inverted bowl). The origin is the lowest point in one cross-section and the highest in another — a mountain pass, or the seat of a saddle. Your gradient knowledge tells you ∇f(0,0) = (0, 0), confirming it as a critical point, but the geometry reveals it is neither a maximum nor a minimum.

The challenge is that solving ∇f = 0 gives you a list of candidates — critical points — but does not tell you what kind each one is. You might have a local minimum (the surface curves up in all directions), a local maximum (curves down in all directions), or a saddle (curves up in some directions and down in others). Classifying requires more information about the curvature of the surface near the critical point, which is captured by the Hessian matrix — your next topic. The Hessian plays the role that the second derivative plays in single-variable calculus, extended to capture curvature in every direction.

Geometrically, you can build intuition by thinking of a topographic map. Peaks are local maxima, valleys are local minima, and mountain passes are saddle points. In all three cases, the gradient is zero (you are at a locally flat spot), but their local geometry differs fundamentally. In optimization, this matters enormously: an algorithm that only finds points where ∇f = 0 needs an additional test to confirm it has found a minimum rather than a saddle. Modern machine learning is full of high-dimensional saddle points, which is one reason optimization in neural networks is so subtle.
