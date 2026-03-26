---
id: curvature
title: Curvature and the Frenet Frame
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: space-curves
  type: hard
- id: cross-product
  type: soft
tags:
- curvature
- frenet
- TNB
- torsion
- differential-geometry
stage: formal-systems
status: validated
---

# Curvature and the Frenet Frame

## Core Idea
Curvature κ measures how rapidly a curve turns at each point; it is defined as κ = |dT/ds| where T = r′/|r′| is the unit tangent vector and s is arc length. In practice κ = |r′ × r″| / |r′|³. The unit normal N points toward the center of curvature, and the binormal B = T × N completes the Frenet-Serret frame. Torsion τ measures how the curve twists out of the plane defined by T and N.

## How It's Best Learned
Start with plane curves where torsion is zero and verify that a circle of radius r has constant curvature 1/r. The Frenet frame is best understood by animating it moving along a helix. Emphasize that curvature is an intrinsic property of the curve, not of the parametrization.

## Common Misconceptions
- Curvature depends only on the shape of the curve, not on how fast it is traversed.
- A straight line has curvature zero everywhere, not undefined.
- Torsion can be negative; its sign encodes the direction of twist.

## Questions

```yaml
- question: "One student parametrizes a circle of radius 3 as r(t) = (3cos(t/2), 3sin(t/2), 0) and another as r(t) = (3cos(2t), 3sin(2t), 0). Which statement is true about the curvature κ computed from each?"
  type: multiple-choice
  options:
    - "The fast parametrization gives larger curvature because the tangent vector changes direction more quickly in time"
    - "Both parametrizations give κ = 1/3, because curvature is a property of the curve's shape, not the speed of traversal"
    - "The slow parametrization gives smaller curvature because direction changes per unit of time are less frequent"
    - "Curvature is undefined unless the curve is parametrized by arc length"
  answer: 1
  explanation: "Curvature is intrinsic to the curve's geometry, not its parametrization. The formula κ = |r′ × r″|/|r′|³ corrects for speed through the |r′|³ denominator, ensuring both parametrizations yield κ = 1/3. Options A and C confuse dT/dt — which does depend on traversal speed — with dT/ds, which is purely geometric. The whole point of defining curvature via arc length is to make it parametrization-independent."

- question: "The unit normal vector N in the Frenet-Serret frame points:"
  type: multiple-choice
  options:
    - "In the direction of the velocity vector, along the tangent to the curve"
    - "Toward the center of curvature — the direction the curve is turning"
    - "Perpendicular to the plane of the curve, out of the osculating plane"
    - "In the direction of maximum torsion"
  answer: 1
  explanation: "N = (dT/ds)/|dT/ds|: it is the direction in which the unit tangent is changing, which points toward the center of curvature — the curve is, so to speak, turning toward N. It is the binormal B = T × N that points out of the T-N plane (the osculating plane). Confusing N and B is a common error."

- question: "A straight line has curvature zero everywhere, because the unit tangent vector does not change direction as you move along it."
  type: true-false
  answer: true
  explanation: "κ = |dT/ds|. For a straight line, T is constant — the direction of travel never changes — so dT/ds = 0 and κ = 0 everywhere. This matches the intuition that a line has no bending. A common misconception is that curvature is 'undefined' for a straight line; it is defined and equals zero."

- question: "Torsion τ can primarily be zero or positive; a negative value indicates a computational error in the Frenet-Serret calculations."
  type: true-false
  answer: false
  explanation: "Torsion can be negative. Its sign encodes the handedness of the twist: a right-handed helix has positive torsion and a left-handed helix has negative torsion. Negative torsion is geometrically meaningful, not an error. This is analogous to how the sign of a cross product encodes orientation."

- question: "Why is curvature defined with respect to arc length s rather than the parameter t, and what goes wrong if you compute dT/dt instead of dT/ds?"
  type: short-answer
  answer: "Using dT/dt makes the rate of change of the tangent depend on how fast you traverse the curve, not on its shape. A car driving fast around a circle generates a large dT/dt; the same car crawling around the same circle generates a small dT/dt — yet the circle's geometry is unchanged. Arc length s represents actual distance traveled, so dT/ds measures direction-change per unit of distance, which is purely geometric. The practical formula κ = |r′ × r″|/|r′|³ uses the |r′|³ denominator precisely to convert from parameter-time to arc-length, making curvature intrinsic to the curve's shape regardless of how fast it is traversed."
  explanation: "The intrinsic vs. parameter-dependent distinction is the conceptual core of curvature. Students who miss this compute 'curvature' that changes when they reparametrize the same curve — a sign that they are measuring something about their description of the curve rather than the curve itself."
```

## Explainer

You already know how to describe a space curve as a vector-valued function r(t) and compute its unit tangent vector T = r′/|r′|. The tangent vector tells you the direction of travel, but it says nothing about how quickly that direction is changing. **Curvature** κ is precisely this rate of change of direction, measured with respect to arc length rather than the parameter t. The arc-length parametrization is essential here: if you drive faster along a curve, the curve's shape doesn't change, but dT/dt would. Using arc length s instead makes curvature an intrinsic property of the curve's geometry, not of how fast you happen to traverse it.

To compute κ in practice you don't need to reparametrize. The formula κ = |r′ × r″| / |r′|³ connects directly to the cross product you know. The cross product r′ × r″ measures the "turning" between the velocity and acceleration vectors; dividing by |r′|³ corrects for the speed. The simplest test case is a circle of radius a: you can verify that κ = 1/a everywhere — large circles are nearly flat (small κ), small circles are tightly curved (large κ). A straight line, having no turning at all, has κ = 0. These check against intuition perfectly.

The curvature defines two more vectors that together with T complete the **Frenet-Serret frame**, a moving coordinate system attached to the curve. The **unit normal** N = (dT/ds)/|dT/ds| points toward the center of curvature — it is the direction the curve is "turning toward." The **binormal** B = T × N (which uses your cross product) is perpendicular to both and points out of the plane containing T and N. These three orthonormal vectors {T, N, B} form a right-handed frame that travels with the curve and completely describes its local geometry.

**Torsion** τ measures how the curve twists out of the T-N plane — how fast the binormal B rotates. A planar curve stays in one plane, so B is constant and τ = 0. A helix spirals in three dimensions: it has constant, nonzero curvature and constant, nonzero torsion. The sign of torsion distinguishes a right-handed helix (positive τ) from a left-handed one (negative τ). Curvature and torsion together determine a space curve completely up to rigid motion — a theorem (the fundamental theorem of space curves) that makes the Frenet frame the natural language for differential geometry of curves.
