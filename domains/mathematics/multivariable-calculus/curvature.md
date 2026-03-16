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

## Explainer

You already know how to describe a space curve as a vector-valued function r(t) and compute its unit tangent vector T = r′/|r′|. The tangent vector tells you the direction of travel, but it says nothing about how quickly that direction is changing. **Curvature** κ is precisely this rate of change of direction, measured with respect to arc length rather than the parameter t. The arc-length parametrization is essential here: if you drive faster along a curve, the curve's shape doesn't change, but dT/dt would. Using arc length s instead makes curvature an intrinsic property of the curve's geometry, not of how fast you happen to traverse it.

To compute κ in practice you don't need to reparametrize. The formula κ = |r′ × r″| / |r′|³ connects directly to the cross product you know. The cross product r′ × r″ measures the "turning" between the velocity and acceleration vectors; dividing by |r′|³ corrects for the speed. The simplest test case is a circle of radius a: you can verify that κ = 1/a everywhere — large circles are nearly flat (small κ), small circles are tightly curved (large κ). A straight line, having no turning at all, has κ = 0. These check against intuition perfectly.

The curvature defines two more vectors that together with T complete the **Frenet-Serret frame**, a moving coordinate system attached to the curve. The **unit normal** N = (dT/ds)/|dT/ds| points toward the center of curvature — it is the direction the curve is "turning toward." The **binormal** B = T × N (which uses your cross product) is perpendicular to both and points out of the plane containing T and N. These three orthonormal vectors {T, N, B} form a right-handed frame that travels with the curve and completely describes its local geometry.

**Torsion** τ measures how the curve twists out of the T-N plane — how fast the binormal B rotates. A planar curve stays in one plane, so B is constant and τ = 0. A helix spirals in three dimensions: it has constant, nonzero curvature and constant, nonzero torsion. The sign of torsion distinguishes a right-handed helix (positive τ) from a left-handed one (negative τ). Curvature and torsion together determine a space curve completely up to rigid motion — a theorem (the fundamental theorem of space curves) that makes the Frenet frame the natural language for differential geometry of curves.
