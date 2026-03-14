---
id: cross-product
title: Cross Product in R³
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn
  type: hard
- id: dot-product
  type: hard
builds-toward:
- determinants-2x2-3x3
- linear-transformations
tags:
- cross-product
- 3d-geometry
- determinant
stage: formal-systems
status: draft
---

# Cross Product in R³

## Core Idea
The cross product of two vectors u and v in R³ produces a vector perpendicular to both, with magnitude equal to the area of the parallelogram they span. The formula u × v = (u₂v₃ − u₃v₂, u₃v₁ − u₁v₃, u₁v₂ − u₂v₁) can be expressed as a determinant. The cross product is anti-commutative: u × v = −(v × u).
