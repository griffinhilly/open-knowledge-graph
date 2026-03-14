---
id: moment-of-force-3d
title: Moment of a Force in 3D
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: moment-of-force-2d
  type: hard
- id: cross-product
  type: soft
builds-toward:
- equivalent-force-systems
- equilibrium-rigid-bodies
tags:
- statics
- moment
- 3D
- cross product
- moment about an axis
stage: formal-systems
status: draft
---

# Moment of a Force in 3D

## Core Idea
In three dimensions, the moment of a force F about a point O is a vector quantity computed as M_O = r x F, where r is any position vector from O to a point on the force's line of action. The result is a moment vector whose direction (given by the right-hand rule) defines the axis of rotational tendency and whose magnitude equals the force times the perpendicular distance. To find the moment about a specific axis (not just a point), the scalar projection is used: M_a = u_a . (r x F), where u_a is the unit vector along the axis. This allows engineers to isolate the rotational effect about a shaft, hinge, or any defined axis within a three-dimensional force system.

## How It's Best Learned
Start by expressing r and F in Cartesian component form, then evaluate the 3x3 determinant (i, j, k / r_x, r_y, r_z / F_x, F_y, F_z). Verify the result by checking that a known 2D case reduces to the expected scalar moment. For moment about an axis, practice choosing the axis unit vector, computing the full moment vector first, and then taking the dot product.

## Common Misconceptions
- Using a position vector that does not start at the moment reference point or does not end on the force's line of action.
- Confusing moment about a point (a vector) with moment about an axis (a scalar projection of that vector).
- Reversing the order of the cross product (F x r instead of r x F), which flips the sign of the result.
