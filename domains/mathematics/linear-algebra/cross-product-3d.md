---
id: cross-product-3d
title: Cross Product in R³
domain: mathematics
course: linear-algebra
prerequisites:
- id: dot-product
  type: hard
- id: determinants-2x2-3x3
  type: soft
builds-toward:
- linear-transformations-definition
tags:
- cross-product
- 3d-vectors
- determinants
stage: formal-systems
status: validated
---

# Cross Product in R³

## Core Idea
The cross product u × v in R³ produces a vector perpendicular to both u and v, with magnitude ||u × v|| = ||u|| ||v|| sin(θ). It is computed using a determinant formula and has applications in computing areas of parallelograms and normals to planes. Unlike the dot product, cross product is only defined in R³ (and R⁷).

## Questions

```yaml
- question: "If u × v = w, what is the direction of v × u?"
  type: multiple-choice
  options:
    - "The same direction as w"
    - "The opposite direction of w (i.e., −w)"
    - "Perpendicular to w"
    - "It depends on the magnitudes of u and v"
  answer: 1
  explanation: "The cross product is anti-commutative: v × u = −(u × v) = −w. This follows from the determinant definition — swapping two rows of a determinant negates it. Geometrically, the right-hand rule applied with the fingers pointing from v to u gives the opposite orientation from v to u. This is fundamentally different from the dot product, which is commutative."

- question: "The magnitude of u × v equals ||u|| ||v|| cos(θ), where θ is the angle between the vectors."
  type: true-false
  answer: false
  explanation: "The magnitude of the cross product is ||u × v|| = ||u|| ||v|| sin(θ). It is the dot product that uses cosine: u · v = ||u|| ||v|| cos(θ). This distinction is conceptually important: the dot product is maximized when vectors point in the same direction (cos(0°) = 1), while the cross product is maximized when they are perpendicular (sin(90°) = 1) and equals zero when they are parallel (sin(0°) = 0)."

- question: "What does it mean geometrically when u × v = 0 (the zero vector), assuming neither u nor v is itself the zero vector?"
  type: short-answer
  answer: "The vectors u and v are parallel (they point in the same or opposite directions, i.e., θ = 0° or θ = 180°)."
  explanation: "The magnitude formula ||u × v|| = ||u|| ||v|| sin(θ) equals zero when sin(θ) = 0, which happens when θ = 0° or 180°. Geometrically, parallel vectors lie in a line rather than defining a plane, so there is no unique perpendicular direction and no parallelogram area to compute. This makes the cross product a useful test for collinearity of direction vectors."
```

## Explainer

You have already seen the dot product, which takes two vectors and returns a scalar. The cross product does something fundamentally different: it takes two vectors in R³ and returns a new vector that is perpendicular to both. This output-as-vector behavior is what makes the cross product geometrically powerful — and what limits it to three dimensions (plus the exotic R⁷).

To compute u × v for u = (u₁, u₂, u₃) and v = (v₁, v₂, v₃), use the determinant formula: write a 3×3 matrix with the standard basis vectors i, j, k in the first row, the components of u in the second row, and the components of v in the third. Expanding along the first row gives u × v = (u₂v₃ − u₃v₂)i − (u₁v₃ − u₃v₁)j + (u₁v₂ − u₂v₁)k. This looks complex, but each component is just a 2×2 determinant — exactly the structure from your determinant prerequisites. The minus sign on the j component is the one most students forget.

The direction of u × v is determined by the right-hand rule: curl the fingers of your right hand from u toward v, and your thumb points in the direction of u × v. This also explains anti-commutativity: if you curl from v toward u instead, your thumb points the opposite way, so v × u = −(u × v). Unlike addition and multiplication of numbers — and unlike the dot product — order matters for cross products.

The magnitude formula ||u × v|| = ||u|| ||v|| sin(θ) has a beautiful geometric interpretation: it equals the area of the parallelogram formed by u and v. When the vectors are perpendicular (θ = 90°), sin(θ) = 1 and the magnitude is at its largest; the parallelogram is a rectangle. When they are parallel (θ = 0° or 180°), sin(θ) = 0 and the cross product is zero — the parallelogram collapses to a line segment with no area. Compare this to the dot product, which is zero when vectors are perpendicular and maximized when they are parallel — the two products are in a sense complementary.

The most common application you will see is computing a normal vector to a plane: if you know two vectors lying in the plane, their cross product points perpendicular to it. This is used extensively in 3D graphics, physics (torque and angular momentum are cross products), and multivariable calculus when setting up surface integrals.
