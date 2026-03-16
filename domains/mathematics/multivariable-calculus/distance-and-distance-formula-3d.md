---
id: distance-and-distance-formula-3d
title: Distance Formula and Metric in 3D Space
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: 3d-coordinate-systems
  type: hard
- id: pythagorean-theorem
  type: hard
builds-toward:
- vectors-in-3d
- spheres-and-level-sets
tags:
- distance
- metric
- 3d-space
stage: formal-systems
status: draft
---

# Distance Formula and Metric in 3D Space

## Core Idea
The distance between two points in 3D space (x₁, y₁, z₁) and (x₂, y₂, z₂) is √[(x₂−x₁)² + (y₂−y₁)² + (z₂−z₁)²]. This formula extends the 2D distance formula by including the z-component and defines the Euclidean metric in ℝ³.

## Explainer

You already know the 2D distance formula from the Pythagorean theorem: the distance between (x₁, y₁) and (x₂, y₂) is √[(x₂−x₁)² + (y₂−y₁)²]. This is just the length of the hypotenuse of a right triangle whose legs have lengths |x₂−x₁| and |y₂−y₁|. Extending to 3D requires one more application of the same theorem. Think of it as a two-step process: first find the horizontal distance in the xy-plane (ignoring z), then treat that horizontal distance and the vertical displacement |z₂−z₁| as the legs of a new right triangle. Applying Pythagoras again gives the full 3D distance.

Explicitly: the horizontal distance in the xy-plane is √[(x₂−x₁)² + (y₂−y₁)²]. Call this d_xy. Now the 3D diagonal from the first point to the second is the hypotenuse of a right triangle with legs d_xy and |z₂−z₁|, giving distance = √[d_xy² + (z₂−z₁)²] = √[(x₂−x₁)² + (y₂−y₁)² + (z₂−z₁)²]. The 3D coordinate system you studied as a prerequisite provides exactly the framework for this decomposition: the three axes are mutually perpendicular, so the three coordinate differences contribute independently and orthogonally to the total displacement.

This formula defines the **Euclidean metric** on ℝ³ — the standard way to measure distance in three-dimensional space. The word "metric" means a function that measures distance and satisfies three axioms: d(A, A) = 0, d(A, B) = d(B, A), and the triangle inequality d(A, C) ≤ d(A, B) + d(B, C). The Euclidean metric satisfies all three, and it is the natural notion of "straight-line distance" in physical space.

The distance formula also provides the equation of a **sphere**: all points (x, y, z) at distance r from a center (a, b, c) satisfy (x−a)² + (y−b)² + (z−c)² = r². This is just the distance formula squared, set equal to r². From here, the same ideas generalize: replacing the equality with an inequality describes the interior or exterior of a sphere, and the notion of distance is the foundation for limits, continuity, and convergence in three-dimensional calculus — all of which build directly on this formula.
