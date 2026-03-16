---
id: cross-product
title: Cross Product in R^3
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn-definition
  type: hard
tags:
- vectors
- cross product
- r3
stage: formal-systems
status: draft
---

# Cross Product in R^3

## Core Idea
The cross product u × v in R^3 produces a vector perpendicular to both u and v with magnitude ||u|| ||v|| sin(θ). It can be computed using: u × v = (u₂v₃ − u₃v₂, u₃v₁ − u₁v₃, u₁v₂ − u₂v₁). The cross product is anti-commutative and non-associative.

## Questions

```yaml
- question: "Let u = (1, 0, 0) and v = (0, 1, 0). What is u × v?"
  type: multiple-choice
  options:
    - "(0, 0, 0)"
    - "(1, 1, 0)"
    - "(0, 0, 1)"
    - "(0, 0, −1)"
  answer: 2
  explanation: "Applying the component formula: u × v = (u₂v₃ − u₃v₂, u₃v₁ − u₁v₃, u₁v₂ − u₂v₁) = (0·0 − 0·1, 0·0 − 1·0, 1·1 − 0·0) = (0, 0, 1). Geometrically, the cross product of the first and second standard basis vectors is the third — consistent with the right-hand rule."

- question: "The cross product is commutative: u × v = v × u for all vectors u and v in R^3."
  type: true-false
  answer: false
  explanation: "The cross product is anti-commutative, meaning v × u = −(u × v). Reversing the order reverses the direction of the resulting vector. This follows from the right-hand rule: curling from v to u points in the opposite direction from curling u to v. This is a fundamental difference from the dot product and from scalar multiplication, both of which are commutative."

- question: "What geometric quantity does the magnitude ||u × v|| represent?"
  type: short-answer
  answer: "The area of the parallelogram with u and v as adjacent sides."
  explanation: "||u × v|| = ||u|| ||v|| sin(θ), which is base times height for the parallelogram formed by u and v. When the vectors are parallel (θ = 0), sin(θ) = 0 and the 'parallelogram' is flat with zero area. When they are perpendicular (θ = 90°), the magnitude reaches its maximum of ||u|| ||v||, matching the area of the rectangle they form."
```

## Explainer

The dot product condenses two vectors into a single number that measures alignment — how much one vector projects onto the other. The cross product is a fundamentally different operation: given two vectors in R^3, it produces a third vector that is perpendicular to both inputs. This geometric output is what makes the cross product indispensable in physics and 3D geometry.

To compute u × v for u = (u₁, u₂, u₃) and v = (v₁, v₂, v₃), use the component formula: u × v = (u₂v₃ − u₃v₂, u₃v₁ − u₁v₃, u₁v₂ − u₂v₁). A reliable way to remember this is to expand the determinant of a 3×3 matrix whose first row is (i, j, k) (the standard basis vectors) and whose second and third rows are u and v. Each component of the result is a 2×2 minor of that matrix, alternating in sign. The formula looks intimidating at first but becomes mechanical with practice.

The magnitude of u × v equals ||u|| ||v|| sin(θ), where θ is the angle between the two vectors. Geometrically, this is the area of the parallelogram with u and v as adjacent sides. Two immediate consequences follow: if the vectors are parallel (θ = 0° or 180°), sin(θ) = 0 and the cross product is the zero vector — there is no unique perpendicular when the vectors lie along the same line. If they are perpendicular (θ = 90°), the cross product achieves its largest possible magnitude.

The direction of u × v follows the right-hand rule: point your right hand's fingers along u, curl them toward v, and your thumb indicates the direction of u × v. This rule exposes anti-commutativity: curling from v toward u reverses the thumb direction, so v × u = −(u × v). Anti-commutativity is one of the cross product's defining properties and the source of many sign errors — never assume you can swap the arguments without flipping the sign.

The cross product is only defined in R^3 (and, in a generalized form, R^7), unlike the dot product which generalizes to any dimension. In physics, it appears in torque (r × F), angular momentum (r × p), and magnetic force (qv × B). In computer graphics, it is the standard method for computing surface normals — the vector pointing perpendicularly outward from a 3D face — which is essential for lighting calculations.
