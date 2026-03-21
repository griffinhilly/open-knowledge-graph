---
id: vector-valued-functions-curves
title: Vector-Valued Functions and Parametric Curves
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vectors-3d-coordinate-system
  type: hard
- id: vector-valued-functions
  type: hard
builds-toward:
- arc-length-parametric
- curvature-and-torsion
tags:
- vector-functions
- curves
- parametrization
stage: formal-systems
status: draft
---

# Vector-Valued Functions and Parametric Curves

## Core Idea
A vector-valued function r(t) = ⟨f(t), g(t), h(t)⟩ traces a curve in space as t varies. The derivative r'(t) is the tangent vector pointing in the direction of motion. Speed is |r'(t)|, and the direction of r'(t) gives the curve's orientation.

## Questions

```yaml
- question: "Two vector-valued functions r₁(t) = ⟨cos t, sin t, 0⟩ and r₂(t) = ⟨cos 2t, sin 2t, 0⟩ both trace curves. Which statement is correct?"
  type: multiple-choice
  options:
    - "They trace different curves because their derivatives are different"
    - "They trace the same curve at the same speed"
    - "They trace the same curve, but r₂ traverses it twice as fast"
    - "They have the same tangent vectors at corresponding parameter values"
  answer: 2
  explanation: "Both functions trace the unit circle in the xy-plane — the same set of points. But r₂(t) has a parameter that runs at double the angular rate, so it completes a full revolution in half the time. The geometric curve (the set of points) is unchanged by reparametrization; the velocity vectors and speed change. This is the core distinction: the parametrization controls how fast you travel, not where you go."

- question: "A particle moves along r(t) from t = 0 to t = T. What does |∫₀ᵀ r'(t) dt| represent?"
  type: multiple-choice
  options:
    - "The total arc length of the path traveled"
    - "The magnitude of the net displacement"
    - "The average speed of the particle"
    - "The total distance traveled, accounting for backtracking"
  answer: 1
  explanation: "∫₀ᵀ r'(t) dt = r(T) − r(0) by the Fundamental Theorem of Calculus, which is the net displacement vector — a straight-line arrow from start to end. Its magnitude is the straight-line distance between endpoints, not the path length. To get arc length (total distance traveled, accounting for the curve's shape), you must integrate the speed: L = ∫₀ᵀ |r'(t)| dt. Confusing these two is the most common error when students first encounter vector integration."

- question: "The derivative r'(t) of a vector-valued function is a vector that is tangent to the curve and points in the direction of increasing t."
  type: true-false
  answer: true
  explanation: "r'(t) = ⟨f'(t), g'(t), h'(t)⟩ is the velocity vector of the particle at time t. Geometrically, it is tangent to the curve at the point r(t) — it points in the direction the curve is heading at that instant — and it specifically points in the direction of increasing t (the orientation given by the parametrization). Dividing by its magnitude gives the unit tangent vector T(t) = r'(t)/|r'(t)|, which strips away speed and keeps only direction."

- question: "Integrating a vector-valued function r(t) component-by-component from a to b gives the total arc length of the curve traced on that interval."
  type: true-false
  answer: false
  explanation: "∫ₐᵇ r(t) dt computes an antiderivative (or, with limits, a displacement-like quantity) — it is a vector, not a scalar arc length. Arc length requires integrating the scalar speed: L = ∫ₐᵇ |r'(t)| dt. This is a crucial distinction: integrating r itself evaluates its antiderivative; integrating |r'| accumulates the total distance traveled. These are different operations with different outputs — one a vector, one a positive real number."

- question: "Why must you integrate |r'(t)| to compute arc length rather than simply computing |∫r'(t) dt|?"
  type: short-answer
  answer: "Because ∫r'(t) dt gives the net displacement vector (start to end), whose magnitude is the straight-line distance between endpoints — and that equals arc length only if the curve is a straight line with no backtracking. For any curved or winding path, the straight-line distance is shorter than the total distance traveled. Arc length accumulates tiny increments of actual path distance at each moment, which is |r'(t)| dt — the speed times the time step. Integrating speed gives total distance; integrating velocity gives net displacement."
  explanation: "The distinction mirrors the one you know from single-variable calculus: ∫₀ᵀ v(t) dt gives net displacement (can be zero if you return to start), while ∫₀ᵀ |v(t)| dt gives total odometer distance. In 3D, the speed |r'(t)| is the instantaneous rate at which arc length is accumulating, so integrating it gives the total path length regardless of how the curve winds through space."
```

## Explainer

You already know how to work with **vectors in 3D** as fixed arrows in space. A **vector-valued function** r(t) = ⟨f(t), g(t), h(t)⟩ is simply a vector whose components are functions of a parameter t. As t increases, the tip of r(t) traces a path — a curve in ℝ³. Think of t as time and r(t) as the position of a moving particle: f(t), g(t), h(t) give its x, y, and z coordinates at each moment. The curve is the trajectory, and the parameter t gives it an orientation (a sense of direction). This is the geometric content that ordinary scalar functions lack: instead of plotting one output against one input, you are plotting a moving point in space.

Differentiation works component-by-component: r'(t) = ⟨f'(t), g'(t), h'(t)⟩. Geometrically, r'(t) is the **velocity vector** — a vector tangent to the curve at the point r(t), pointing in the direction of increasing t. Its magnitude |r'(t)| = √(f'(t)² + g'(t)² + h'(t)²) is the **speed** — how fast the particle is moving. Dividing by speed gives the **unit tangent vector** T(t) = r'(t)/|r'(t)|, which captures direction only. The distinction between velocity (vector, carries direction and magnitude) and speed (scalar, magnitude only) is the same one you know from single-variable calculus, now extended to curves in space.

The parametrization is not unique: the same curve can be traced by infinitely many different r(t). For instance, r₁(t) = ⟨cos t, sin t, 0⟩ and r₂(t) = ⟨cos 2t, sin 2t, 0⟩ both trace the unit circle in the xy-plane, but r₂ goes twice as fast. Changing the parameter is like changing the clock speed on the same journey. The geometric curve (the set of points) is the same; the parametrization affects velocity and speed but not the shape. When comparing curves or computing arc length, it is often necessary to re-parametrize — for example, using arc length as the parameter so that |r'(t)| = 1 everywhere.

Integration of r(t) also works component-by-component: ∫r(t) dt = ⟨∫f(t) dt, ∫g(t) dt, ∫h(t) dt⟩. If r'(t) is velocity, then ∫₀ᵀ r'(t) dt = r(T) − r(0) is the net displacement from t = 0 to t = T. To find the total distance traveled (arc length), you integrate speed: L = ∫₀ᵀ |r'(t)| dt. This is the direct generalization of arc length for parametric curves in R², and it is the foundation for curvature, which describes how sharply the curve bends at each point.
