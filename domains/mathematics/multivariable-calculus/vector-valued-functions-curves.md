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

## Explainer

You already know how to work with **vectors in 3D** as fixed arrows in space. A **vector-valued function** r(t) = ⟨f(t), g(t), h(t)⟩ is simply a vector whose components are functions of a parameter t. As t increases, the tip of r(t) traces a path — a curve in ℝ³. Think of t as time and r(t) as the position of a moving particle: f(t), g(t), h(t) give its x, y, and z coordinates at each moment. The curve is the trajectory, and the parameter t gives it an orientation (a sense of direction). This is the geometric content that ordinary scalar functions lack: instead of plotting one output against one input, you are plotting a moving point in space.

Differentiation works component-by-component: r'(t) = ⟨f'(t), g'(t), h'(t)⟩. Geometrically, r'(t) is the **velocity vector** — a vector tangent to the curve at the point r(t), pointing in the direction of increasing t. Its magnitude |r'(t)| = √(f'(t)² + g'(t)² + h'(t)²) is the **speed** — how fast the particle is moving. Dividing by speed gives the **unit tangent vector** T(t) = r'(t)/|r'(t)|, which captures direction only. The distinction between velocity (vector, carries direction and magnitude) and speed (scalar, magnitude only) is the same one you know from single-variable calculus, now extended to curves in space.

The parametrization is not unique: the same curve can be traced by infinitely many different r(t). For instance, r₁(t) = ⟨cos t, sin t, 0⟩ and r₂(t) = ⟨cos 2t, sin 2t, 0⟩ both trace the unit circle in the xy-plane, but r₂ goes twice as fast. Changing the parameter is like changing the clock speed on the same journey. The geometric curve (the set of points) is the same; the parametrization affects velocity and speed but not the shape. When comparing curves or computing arc length, it is often necessary to re-parametrize — for example, using arc length as the parameter so that |r'(t)| = 1 everywhere.

Integration of r(t) also works component-by-component: ∫r(t) dt = ⟨∫f(t) dt, ∫g(t) dt, ∫h(t) dt⟩. If r'(t) is velocity, then ∫₀ᵀ r'(t) dt = r(T) − r(0) is the net displacement from t = 0 to t = T. To find the total distance traveled (arc length), you integrate speed: L = ∫₀ᵀ |r'(t)| dt. This is the direct generalization of arc length for parametric curves in R², and it is the foundation for curvature, which describes how sharply the curve bends at each point.
