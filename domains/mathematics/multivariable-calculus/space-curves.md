---
id: space-curves
title: Space Curves and Tangent Vectors
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vector-valued-functions
  type: hard
- id: arc-length-parametric
  type: hard
builds-toward:
- parametric-surfaces
- stokes-theorem
tags:
- curves
- tangent
- geometry
stage: formal-systems
status: validated
---

# Space Curves and Tangent Vectors

## Core Idea
A space curve r(t) has tangent vector r'(t), which indicates direction of motion. Arc length parameterization uses s(t) as the parameter and gives unit tangent T(s) = dr/ds. Curvature κ measures how quickly the curve changes direction.

## Questions

```yaml
- question: "Two parametrizations of the same helix: r₁(t) traverses it at speed 2, r₂(t) traverses it at speed 5. At corresponding geometric points, which quantities are the same for both parametrizations?"
  type: multiple-choice
  options:
    - "Both the tangent vector magnitude (speed) and curvature are the same"
    - "The curvature is the same but the tangent vector magnitudes differ"
    - "The tangent vector direction and magnitude are both the same"
    - "Neither the tangent vector nor the curvature is the same, since the parametrizations differ"
  answer: 1
  explanation: "Curvature κ measures geometric bending — how sharply the curve turns — which is intrinsic to the curve's shape, independent of traversal speed. The tangent vector magnitudes (speeds ‖r'(t)‖) differ between the two parametrizations, but the unit tangent directions and curvature are the same at corresponding geometric points. Arc length parameterization makes this precise: κ = ‖dT/ds‖ is defined in terms of arc length, not t, so it captures geometry alone."

- question: "A curve has constant curvature κ = 1/5. What does this tell you about the curve's shape?"
  type: multiple-choice
  options:
    - "The curve is a straight line, since only a line can have constant curvature"
    - "The curve is locally shaped like a circle of radius 5, bending at the same rate everywhere"
    - "The curve completes a full circle every 5 units of arc length"
    - "The curve's speed is constant at 1/5"
  answer: 1
  explanation: "Constant curvature κ = 1/R means the curve bends at the same rate throughout — this characterizes a circle of radius R (or a circular helix in 3D). A straight line has κ = 0 (no bending). Curvature is a geometric property of the curve's shape, independent of how fast you traverse it. It is not speed."

- question: "Curvature measures how fast you are moving along a space curve."
  type: true-false
  answer: false
  explanation: "Curvature measures how quickly the direction of the curve changes — how sharply it bends — not speed of travel. Formally, κ = ‖dT/ds‖ where s is arc length and T is the unit tangent: it is the rate of turning per unit distance traveled, with speed removed entirely. A curve can be traversed fast or slow; its curvature — the geometric shape — is the same either way. Speed is ‖r'(t)‖, a completely separate quantity."

- question: "Arc length parameterization produces a curve r(s) where ‖dr/ds‖ = 1, so the tangent vector always has unit length."
  type: true-false
  answer: true
  explanation: "This is the defining property of arc length parameterization. By using arc length s as the parameter, each unit increase in s corresponds to exactly one unit of distance traveled along the curve. The tangent vector T(s) = dr/ds therefore has magnitude 1 at every point. This removes all dependence on traversal speed, leaving only geometric information about the curve's shape."

- question: "Why is reparametrizing a space curve by arc length useful for studying its geometry, even though it is often computationally inconvenient?"
  type: short-answer
  answer: "A curve's natural parameter (often time) is arbitrary — two parametrizations of the same curve produce different tangent vectors with different magnitudes depending on speed. Arc length parameterization removes this ambiguity by making speed exactly 1 everywhere, so the unit tangent T(s) depends only on where you are on the curve, not how fast you got there. This means quantities like curvature κ = ‖dT/ds‖ describe the curve's intrinsic geometry rather than an artifact of how it was traversed."
  explanation: "The key insight is separating the curve's geometric shape from the accidental choice of how to traverse it. Arc length is intrinsic to the curve itself. The computational inconvenience — s(t) often can't be inverted in closed form — doesn't diminish the conceptual value: arc length parameterization is the foundation for defining curvature, torsion, and the Frenet-Serret frame."
```

## Explainer

You already know that a **vector-valued function** r(t) = (x(t), y(t), z(t)) traces a path through three-dimensional space as t varies. The parameter t is often time, and r(t) records the position of a moving particle. The derivative r'(t) = (x'(t), y'(t), z'(t)) is the **tangent vector** — it points in the direction of motion and its magnitude ‖r'(t)‖ is the speed. This is a direct generalization of the single-variable derivative: just as f'(a) gives the slope of a curve in the plane, r'(t₀) gives the direction of motion along a space curve at the moment t₀.

The challenge with a parameter like t is that it is arbitrary. Two parametrizations of the same geometric curve — say, one traversed slowly and one quickly — produce different tangent vectors ‖r'(t)‖ (different speeds) even though they trace the same shape. To remove this parameter-dependence and focus purely on the geometry of the curve, we use **arc length parameterization**. The arc length s(t) = ∫₀ᵗ ‖r'(u)‖ du measures how far you have traveled along the curve. Reparametrizing by s gives a curve r(s) that always moves at unit speed: ‖dr/ds‖ = 1. The unit tangent **T**(s) = dr/ds now depends only on where you are on the curve, not on how fast you got there.

**Curvature** κ measures how sharply the curve bends. In arc length terms, κ = ‖dT/ds‖ — it is the rate at which the unit tangent vector changes direction as you walk along the curve at unit speed. A straight line has κ = 0 (the tangent never rotates). A circle of radius R has constant curvature κ = 1/R (tighter circles bend more sharply). An arbitrary space curve has varying curvature that characterizes its local geometry at each point. High curvature means the curve is turning quickly; low curvature means it is nearly straight.

Together, the tangent vector and curvature begin building what is called the **Frenet-Serret frame** — a moving coordinate system that travels with the curve and reveals its intrinsic geometry. Beyond curvature, a space curve (unlike a plane curve) can also twist out of a plane, measured by a quantity called torsion. These local geometric quantities — direction, bending, and twisting — completely characterize a space curve up to rigid motion. This geometric perspective connects back to arc length from your prerequisites and forward to the study of surfaces and Stokes' theorem, where curves appear as the boundaries of surfaces.
