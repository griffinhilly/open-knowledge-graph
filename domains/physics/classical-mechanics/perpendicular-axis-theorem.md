---
id: perpendicular-axis-theorem
title: Perpendicular Axis Theorem
domain: physics
course: classical-mechanics
prerequisites:
- id: moment-of-inertia
  type: hard
builds-toward:
- rotational-kinetic-energy
tags:
- moment-of-inertia
- rotation
- 2d-shapes
stage: formal-systems
status: draft
---

# Perpendicular Axis Theorem

## Core Idea
For any planar (2D) object, the moment of inertia about an axis perpendicular to the plane equals the sum of moments about two perpendicular axes in the plane: I_z = I_x + I_y. This gives a quick way to find the out-of-plane moment from in-plane measurements, especially useful for thin disks and plates.

## Explainer

From moment of inertia theory you know that I = Σmᵢrᵢ² (or ∫r² dm for continuous objects), where r is measured from the axis of rotation. The value of I depends crucially on which axis you choose — the same object can have very different moments about different axes. The **perpendicular axis theorem** is a relationship that connects three different moments of a single planar object, letting you find one if you know the other two.

The proof follows directly from the definition of r. Set up a coordinate system with x and y axes in the plane of the object and z perpendicular to it. For any mass element at position (x, y) in the plane: the distance from the z-axis is r_z = √(x² + y²), the distance from the x-axis is r_x = y (since the object is flat, z = 0), and the distance from the y-axis is r_y = x. Therefore I_z = Σmᵢ(xᵢ² + yᵢ²) = Σmᵢxᵢ² + Σmᵢyᵢ² = I_y + I_x. The theorem is essentially the 2D Pythagorean theorem applied to distances from axes. Note that the object *must be planar* — if it has any thickness in the z-direction, the distances r_x and r_y pick up a z² contribution and the sum no longer equals I_z.

The theorem is most useful when a shape has symmetry that makes I_x = I_y. For a uniform disk, symmetry about the center means any two perpendicular diameters are equivalent axes, so I_x = I_y = I_disk. The perpendicular theorem then gives I_z = I_x + I_y = 2I_x, so I_x = I_z/2. Since the moment of a disk about its symmetry axis (z) is ½MR², the moment about a diameter is ¼MR². This result would be more painful to derive by direct integration over the tilted axis, so the perpendicular theorem is a real shortcut.

A related theorem — the **parallel axis theorem** (which you may also encounter) — shifts an axis away from the center of mass rather than rotating it. The two theorems together form a toolkit for building up moments for composite objects or for axes that are not through the center of mass. When a problem asks for the moment about a strange axis for a planar object, your first question should be: can I find two in-plane moments that sum to this one? If the geometry cooperates, the perpendicular axis theorem turns a complicated integral into a lookup plus addition.
