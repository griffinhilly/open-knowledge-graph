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

## Questions

```yaml
- question: "A force F = 3j N is applied at point r = 2i m from the origin. What is the moment about the origin?"
  type: multiple-choice
  options:
    - "M = 6i N·m — the moment points in the direction of the position vector"
    - "M = 6j N·m — the moment points in the direction of the force"
    - "M = 6k N·m — from r × F using the right-hand rule"
    - "M = −6k N·m — the moment is negative because the force is in the y-direction"
  answer: 2
  explanation: "Using M = r × F with r = 2i and F = 3j: the cross product i × j = k, so M = 2·3·(i × j) = 6k N·m. The moment vector points in the +z direction. This illustrates the critical 3D insight: the moment vector points *perpendicular* to both r and F — not in the direction of either. A force in the y-direction at an x-offset produces a rotational tendency about the z-axis. Options A and B represent the common misconception that M points along r or F."

- question: "An engineer computes M_O = (4i + 2j − 3k) N·m as the moment about point O. She wants the moment about a shaft axis defined by unit vector û = j. What is the result, and what type of quantity is it?"
  type: multiple-choice
  options:
    - "A vector: (4i + 2j − 3k) N·m — the full moment vector projected onto the axis"
    - "A scalar: 2 N·m — the dot product û · M_O extracts the y-component"
    - "A vector: 2j N·m — the j-component of M_O"
    - "A scalar: −3 N·m — the component perpendicular to the shaft"
  answer: 1
  explanation: "The moment about a specific axis is the scalar M_a = û · M_O = j · (4i + 2j − 3k) = 0(4) + 1(2) + 0(−3) = 2 N·m. This is a scalar, not a vector — it represents the rotational tendency about the chosen axis. The x- and z-components (4i and −3k) are reactions absorbed by the bearing and don't drive rotation about the y-axis. The transition from moment-about-a-point (vector) to moment-about-an-axis (scalar) via dot product is a key operation in 3D statics."

- question: "In the cross product formula M_O = r × F, swapping the order to F × r gives a result that is equal in magnitude but opposite in direction."
  type: true-false
  answer: true
  explanation: "The cross product is anti-commutative: F × r = −(r × F). This means swapping operand order flips all three components of the moment vector — same magnitude, opposite direction. In practice, this is one of the most common sign errors in 3D statics. The correct form is r × F (position vector crossed into force), following the right-hand rule: curl fingers from r toward F, thumb points in the direction of M_O."

- question: "The moment vector M_O = r × F points in the direction of the applied force F."
  type: true-false
  answer: false
  explanation: "The moment vector is perpendicular to both r and F, by definition of the cross product. It points along the axis about which the force tends to cause rotation — which is generally in a completely different direction from the force itself. For example, a vertical force (in the z-direction) applied at a horizontal offset (in the x-direction) produces a moment vector in the y-direction. The moment vector's direction tells you the rotational axis, not the force direction. Confusing these is the central conceptual error students make when first encountering 3D moments."

- question: "What is the conceptual difference between the moment of a force about a point and the moment of a force about an axis, and when would you use each?"
  type: short-answer
  answer: "The moment about a *point* M_O = r × F is a vector describing the full rotational tendency — both which axis the rotation acts about and how strong it is. The moment about a specific *axis* is the scalar M_a = û · M_O, which isolates just the rotational component acting about one particular direction. You use moment about a point when writing full 3D equilibrium equations (summing all moment components to zero). You use moment about an axis when analyzing a specific shaft, hinge, or pin — to find what torque acts through that constrained direction."
  explanation: "For example, analyzing a bolted plate in 3D requires taking moments about the point of application to write three vector equations. But computing the torque on a specific drive shaft means projecting the moment vector onto the shaft's axis — the other components are reacted by bearings. The axis moment gives the scalar answer a mechanical designer needs: how much torque must the shaft handle?"
```

## Explainer

In 2D statics, the moment of a force about a point is a scalar: M = r × F = r·F·sin θ, with a positive or negative sign indicating clockwise or counterclockwise. In 3D, that sign is replaced by a direction — the moment becomes a **vector** that points along the axis about which the rotation tends to occur. The formula is **M**_O = **r** × **F**, where **r** is any position vector from the moment reference point O to any point on the line of action of **F**. The direction of the moment vector is given by the right-hand rule: curl your right-hand fingers from **r** toward **F**, and your thumb points in the direction of **M**_O.

To compute this in practice, you express **r** and **F** in Cartesian components and evaluate the 3×3 determinant:

**M**_O = |**i**  **j**  **k**|
          |r_x  r_y  r_z|
          |F_x  F_y  F_z|

Expanding: **M**_O = (r_y·F_z − r_z·F_y)**i** − (r_x·F_z − r_z·F_x)**j** + (r_x·F_y − r_y·F_x)**k**. The **order matters**: it's **r** × **F**, not **F** × **r**. Reversing order flips all three signs — a common sign error.

Once you have the moment about a point, you can find the **moment about a specific axis** by projecting: M_a = **û**_a · **M**_O = **û**_a · (**r** × **F**), where **û**_a is the unit vector along the axis. This scalar tells you the rotational tendency about that particular axis — for example, the torque experienced by a shaft aligned with a given direction. Geometrically, the dot product extracts the component of the moment vector that is parallel to the axis; components perpendicular to the axis are reacted by the bearing and don't cause rotation about it.

The key conceptual leap from 2D is that **the moment vector points along the axis of rotation tendency, not in the direction of the force**. A vertical force applied at a horizontal offset from a vertical axis creates a horizontal moment vector — the tendency is to rotate about a horizontal axis, not a vertical one. Building this three-dimensional geometric intuition is worth more than memorizing the determinant formula. Once you're comfortable visualizing what axis a cross product points along, 3D statics becomes a systematic extension of 2D rather than an entirely new subject.
