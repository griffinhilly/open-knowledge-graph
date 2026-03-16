---
id: second-moment-of-area-calculation
title: Calculation of Second Moment of Area
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: area-moment-of-inertia-engineering
  type: hard
- id: parallel-axis-theorem-statics
  type: hard
builds-toward:
- moment-of-inertia-about-centroid
tags:
- moment-of-inertia
- second-moment
- integration
stage: formal-systems
status: draft
---

# Calculation of Second Moment of Area

## Core Idea
The second moment of area I is calculated by integration: I = ∫∫ r² dA, where r is the perpendicular distance from an axis. For composite sections, use the parallel-axis theorem: I = I_c + A d², where I_c is the moment about the centroid and d is the distance between axes. These properties are fundamental to beam bending analysis.

## Explainer

The **second moment of area** (also called the **area moment of inertia**) I measures how a cross-section's area is distributed relative to an axis. The defining integral is I_x = ∫ y² dA for the axis parallel to x, and I_y = ∫ x² dA for the axis parallel to y. The key feature is the squared distance: area far from the axis contributes disproportionately more than area close to it. A hollow pipe and a solid rod of the same cross-sectional area can have very different I values because the pipe concentrates its material at a large radius, while the rod spreads it near the center.

The physical meaning becomes clear in beam bending. When a beam bends under load, the bending stress at any point in the cross-section is σ = M·y / I, where M is the bending moment at that section, y is the distance from the neutral axis, and I is the second moment of area about the neutral axis. A larger I means less stress for the same bending moment — the beam resists bending more effectively. This is why I-beams (W-shapes in structural steel) are shaped as they are: the flanges at the top and bottom maximize I by placing most of the area far from the neutral axis, while the thin web between them contributes little to I but provides shear resistance.

For standard shapes, the integrals have closed-form results you can tabulate: a rectangle of width b and height h has I = bh³/12 about its centroidal axis (parallel to the width). The cube of h explains why doubling a beam's depth increases its bending stiffness eightfold. From your prerequisite, the **parallel-axis theorem** I = I_c + A·d² lets you shift from the centroidal axis to any parallel axis, adding the area times the squared distance between axes. This is how you compute I for composite sections: split the shape into simple sub-shapes, find each sub-shape's centroidal I from the table, apply the parallel-axis theorem to transfer it to the overall neutral axis, and sum.

The practical workflow for a composite section — say an I-beam made from welded plates — is: (1) find the centroid of the entire section, (2) for each rectangular piece, compute I_c = bh³/12 about its own centroid, (3) compute A·d² where d is the vertical distance from each piece's centroid to the composite section's centroid, and (4) sum I_c + A·d² for all pieces. The largest contributors are always the pieces farthest from the neutral axis, which reinforces why efficient structural sections concentrate area at the extreme fibers.
