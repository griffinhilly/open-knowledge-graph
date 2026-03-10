---
id: area-moment-of-inertia-engineering
title: Area Moment of Inertia (Second Moment of Area)
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: centroid-areas-composite
  type: hard
- id: definite-integral-definition
  type: hard
builds-toward:
- parallel-axis-theorem-statics
tags:
- statics
- moment of inertia
- second moment of area
- bending stiffness
stage: formal-systems
status: draft
---

# Area Moment of Inertia (Second Moment of Area)

## Core Idea
The area moment of inertia (second moment of area) measures how an area's distribution relative to an axis resists bending and is defined as Ix = ∫y² dA and Iy = ∫x² dA. It is a purely geometric property — not a mass property — with units of length⁴. For standard shapes, tabulated centroidal formulas apply (rectangle: Ix_c = bh³/12). The polar moment of inertia J = Ix + Iy. This quantity governs beam bending stiffness and appears in the flexure formula σ = My/I.

## How It's Best Learned
Derive the centroidal moment of inertia for a rectangle and triangle by integration to understand its origin. Then memorize tabulated centroidal values and use the parallel axis theorem for composite sections.

## Common Misconceptions
- Confusing area moment of inertia (units: m⁴) with mass moment of inertia (units: kg·m²).
- Forgetting that tabulated formulas give the centroidal moment — the parallel axis theorem is needed to transfer to any other axis.
- Misidentifying which axis (horizontal or vertical) a formula applies to.
