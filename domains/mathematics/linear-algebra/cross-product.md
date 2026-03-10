---
id: cross-product
title: The Cross Product
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn
  type: hard
- id: dot-product
  type: soft
- id: determinants-2x2-3x3
  type: soft
tags:
- cross product
- 3D vectors
- orthogonality
- right-hand rule
- area
stage: formal-systems
status: draft
---

# The Cross Product

## Core Idea
The cross product of two vectors u and v in R³ produces a third vector u × v that is perpendicular to both u and v. Its magnitude equals the area of the parallelogram spanned by u and v, and its direction is determined by the right-hand rule. The cross product is computed using a 3×3 determinant-like expansion along the standard basis vectors i, j, k. Unlike the dot product, the cross product is anti-commutative (u × v = −v × u) and is only defined in R³.

## How It's Best Learned
Practice computing the cross product via the cofactor expansion mnemonic, then verify geometric properties: confirm the result is orthogonal to both inputs using the dot product. Use the cross product to find normal vectors to planes and to compute areas of triangles in 3D.

## Common Misconceptions
- Students often forget the sign alternation (−j term) in cofactor expansion, leading to sign errors in the j component.
- The cross product is not commutative — reversing order negates the result.
- The cross product is unique to R³ and has no direct analog in R² or Rⁿ for n > 3.
