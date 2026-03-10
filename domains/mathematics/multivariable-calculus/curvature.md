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
status: draft
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
