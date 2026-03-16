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

## Explainer

In 2D statics, the moment of a force about a point is a scalar: M = r × F = r·F·sin θ, with a positive or negative sign indicating clockwise or counterclockwise. In 3D, that sign is replaced by a direction — the moment becomes a **vector** that points along the axis about which the rotation tends to occur. The formula is **M**_O = **r** × **F**, where **r** is any position vector from the moment reference point O to any point on the line of action of **F**. The direction of the moment vector is given by the right-hand rule: curl your right-hand fingers from **r** toward **F**, and your thumb points in the direction of **M**_O.

To compute this in practice, you express **r** and **F** in Cartesian components and evaluate the 3×3 determinant:

**M**_O = |**i**  **j**  **k**|
          |r_x  r_y  r_z|
          |F_x  F_y  F_z|

Expanding: **M**_O = (r_y·F_z − r_z·F_y)**i** − (r_x·F_z − r_z·F_x)**j** + (r_x·F_y − r_y·F_x)**k**. The **order matters**: it's **r** × **F**, not **F** × **r**. Reversing order flips all three signs — a common sign error.

Once you have the moment about a point, you can find the **moment about a specific axis** by projecting: M_a = **û**_a · **M**_O = **û**_a · (**r** × **F**), where **û**_a is the unit vector along the axis. This scalar tells you the rotational tendency about that particular axis — for example, the torque experienced by a shaft aligned with a given direction. Geometrically, the dot product extracts the component of the moment vector that is parallel to the axis; components perpendicular to the axis are reacted by the bearing and don't cause rotation about it.

The key conceptual leap from 2D is that **the moment vector points along the axis of rotation tendency, not in the direction of the force**. A vertical force applied at a horizontal offset from a vertical axis creates a horizontal moment vector — the tendency is to rotate about a horizontal axis, not a vertical one. Building this three-dimensional geometric intuition is worth more than memorizing the determinant formula. Once you're comfortable visualizing what axis a cross product points along, 3D statics becomes a systematic extension of 2D rather than an entirely new subject.
