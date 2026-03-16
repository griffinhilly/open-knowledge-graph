---
id: principal-axes-and-rotation
title: Principal Axes and Rotation of Inertia
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: moment-of-inertia-about-centroid
  type: hard
tags:
- principal-axes
- principal-moments
- rotation
stage: formal-systems
status: draft
---

# Principal Axes and Rotation of Inertia

## Core Idea
For any shape, there exist two perpendicular axes through the centroid (in 2D) where the moment of inertia reaches maximum and minimum values, and the product of inertia is zero. These principal axes are found through eigenvalue analysis or using Mohr's circle. Knowing principal axes is essential for analyzing bending in unsymmetric sections.

## Explainer

When you computed Ix and Iy for a shape, you chose a coordinate system — but that choice was arbitrary. Rotate the axes by some angle θ and you get different values for Ix', Iy', and also for a new quantity called the **product of inertia** Ixy = ∫xy dA. The product of inertia measures the asymmetry of the area distribution: it is zero for shapes symmetric about either axis, and nonzero for skewed or L-shaped sections. The moment-of-inertia transformation equations under rotation are structurally identical to the stress transformation equations you may know from mechanics of materials — the same trigonometric form, the same underlying mathematics.

Because I varies with axis orientation, there is a natural question: at what angle is I maximized or minimized? The answer is the **principal axes**. At these two perpendicular orientations, the product of inertia Ixy vanishes, and the moments Ix and Iy reach their extreme values I₁ (maximum) and I₂ (minimum), called the **principal moments of inertia**. Finding them is formally an eigenvalue problem: the inertia tensor [Ix, -Ixy; -Ixy, Iy] has two eigenvalues (I₁ and I₂) and two orthogonal eigenvectors (the principal axis directions).

The most practical tool for finding principal axes is **Mohr's circle for inertia**, a graphical method directly analogous to Mohr's circle for stress. Plot the point (Ix, Ixy) and (Iy, -Ixy) on a graph with I on the horizontal axis and Ixy on the vertical axis. The circle connecting them has its center at ((Ix + Iy)/2, 0) and a radius R = √[((Ix - Iy)/2)² + Ixy²]. The rightmost and leftmost points on the circle give I₁ and I₂; the angle to rotate to reach those points (halved, because Mohr's circle angles are doubled relative to physical angles) gives the principal axis orientation.

Why does any of this matter in practice? For symmetric sections like rectangles and I-beams, the coordinate axes of symmetry are already principal axes — so you rarely need to think about this explicitly. But for asymmetric sections — angle irons (L-shapes), Z-sections, and channel sections mounted off-axis — the principal axes do *not* align with the geometric edges. A beam bent about a non-principal axis will deflect in two directions simultaneously, not just the intended one. This phenomenon, called **unsymmetric bending**, can cause unexpected lateral deflections and is a critical consideration in structural engineering with thin-walled or asymmetric cross-sections.
