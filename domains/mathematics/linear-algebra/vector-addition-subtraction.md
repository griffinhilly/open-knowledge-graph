---
id: vector-addition-subtraction
title: Vector Addition and Subtraction
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn
  type: hard
builds-toward:
- vector-spaces
- span-and-basis
- linear-independence
tags:
- vectors
- operations
- addition
stage: formal-systems
status: validated
---

# Vector Addition and Subtraction

## Core Idea
Vectors are added and subtracted component-wise: (u₁ + v₁, u₂ + v₂, ..., uₙ + vₙ). Geometrically, addition follows the parallelogram rule; subtraction finds the vector between two points. These operations satisfy closure, associativity, and commutativity, forming the foundation of vector space structure.

## How It's Best Learned
Visualize in R^2 using arrows. Add vectors tip-to-tail or using the parallelogram method. Verify algebraically with components. Then practice with higher dimensions using notation only.

## Common Misconceptions
- Thinking vector addition is like adding magnitudes; magnitudes don't add linearly.
- Incorrectly applying operations component-by-component when vectors have different dimensions.

## Questions

```yaml
- question: "Two forces act on an object: 6 N pointing east and 8 N pointing north. What is the magnitude of their resultant?"
  type: multiple-choice
  options:
    - "14 N, since 6 + 8 = 14"
    - "10 N, found by applying the Pythagorean theorem to the perpendicular components"
    - "2 N, since the forces partially cancel"
    - "48 N, since forces multiply when combined"
  answer: 1
  explanation: "Because the forces are perpendicular, |u + v| = √(6² + 8²) = √100 = 10 N. Adding magnitudes directly (giving 14) is the classic error — magnitudes add linearly only when both vectors point in exactly the same direction. For perpendicular vectors, the Pythagorean theorem applies. The correct approach is always to add component-wise first, then compute the magnitude of the resulting vector."

- question: "Point P is at position (3, 5) and point Q is at position (7, 2). Which vector represents the displacement from P to Q?"
  type: multiple-choice
  options:
    - "(10, 7), by adding the position vectors of P and Q"
    - "(4, −3), by computing Q − P"
    - "(−4, 3), by computing P − Q"
    - "(3, 5), since displacement is measured from the origin"
  answer: 1
  explanation: "The displacement from P to Q is Q − P = (7−3, 2−5) = (4, −3). This follows from the key geometric interpretation: u − v is the vector *from* v *to* u. So to go from P to Q, compute Q − P. Option C, P − Q = (−4, 3), is the displacement from Q back to P — the opposite direction. Adding position vectors (option A) produces (10, 7), which has no geometric meaning as a displacement between specific points."

- question: "If vector u has magnitude 5 and vector v has magnitude 5, then u + v must have magnitude 10."
  type: true-false
  answer: false
  explanation: "Magnitudes do not add in general. |u + v| = |u| + |v| only when u and v point in exactly the same direction. If they point in opposite directions, |u + v| = 0. If they are perpendicular, |u + v| = √50 ≈ 7.07. The magnitude of a sum must be computed from the sum vector itself — not from the individual magnitudes — using the Pythagorean theorem or the full component calculation. The triangle inequality |u + v| ≤ |u| + |v| shows that 10 is the maximum, achieved only in the collinear case."

- question: "The vector u − v can be interpreted geometrically as the vector pointing from the tip of v to the tip of u, when both vectors are drawn from the origin."
  type: true-false
  answer: true
  explanation: "This is the key geometric interpretation of subtraction. If u and v are position vectors of points P and Q respectively, then u − v is the displacement from Q (tip of v) to P (tip of u). Equivalently, u − v = u + (−v): negate v (reverse its direction), then add tip-to-tail. Getting the direction right is essential in applications like computing displacement paths between two points, normal vectors in geometry, and relative velocity in physics."

- question: "Explain why the magnitude of u + v is not generally equal to |u| + |v|, and describe when equality does hold."
  type: short-answer
  answer: "Vector addition is component-wise: (u₁ + v₁, u₂ + v₂). The magnitude of the sum is √((u₁+v₁)² + (u₂+v₂)²), which does not generally simplify to √(u₁²+u₂²) + √(v₁²+v₂²). Equality holds only when u and v point in exactly the same direction — in that case the components scale proportionally and the Pythagorean theorem reduces to simple addition. In all other cases the angle between the vectors reduces the magnitude of the sum, which is precisely what the triangle inequality captures: |u + v| ≤ |u| + |v| with equality only in the collinear, same-direction case."
  explanation: "A concrete example: u = (3, 0), v = (0, 4). |u| = 3, |v| = 4, sum of magnitudes = 7. But u + v = (3, 4), and |u + v| = √(9+16) = 5. The same numbers as the classic 3-4-5 right triangle — because that's exactly what's happening geometrically. The vectors are perpendicular, so the Pythagorean theorem gives the magnitude of the sum."
```

## Explainer

You already know that a vector in Rⁿ is an ordered list of n real numbers — a point, or equivalently an arrow, in n-dimensional space. **Vector addition** is the simplest thing you can do with two such arrows: add them entry by entry. If **u** = (u₁, u₂) and **v** = (v₁, v₂), then **u** + **v** = (u₁ + v₁, u₂ + v₂). The component-wise rule is purely algebraic, but geometry makes it vivid.

In the plane, picture **u** as an arrow from the origin to some point, and **v** as another. The **tip-to-tail rule** says: to add them, place the tail of **v** at the tip of **u**. The result is the arrow from the origin to the new tip. Equivalently, **u** + **v** is the diagonal of the parallelogram whose sides are **u** and **v**. These two geometric pictures — tip-to-tail and the parallelogram — are equivalent, and either one lets you visualize addition in R² or R³ before generalizing to higher dimensions where pictures are no longer available.

**Vector subtraction** **u** − **v** = **u** + (−**v**) is just addition of the negated vector. Geometrically, −**v** is the same arrow pointing in the opposite direction. A particularly useful interpretation: **u** − **v** is the vector *from* **v** *to* **u**. If **u** and **v** are position vectors of two points P and Q, then **u** − **v** is the displacement from Q to P. This shows up constantly in geometry — the vector connecting two points is always a difference of their position vectors.

One thing to watch: adding magnitudes is wrong. If |**u**| = 3 and |**v**| = 4, then |**u** + **v**| is *not* 7 in general. It equals 7 only if the vectors point in exactly the same direction. If they are perpendicular, it equals 5 (by the Pythagorean theorem), and if they are antiparallel, it equals 1. This is why the triangle inequality ||**u** + **v**|| ≤ ||**u**|| + ||**v**|| holds with equality only in the collinear case. The component-wise addition rule is always exact; the magnitude has to be computed from the sum, not from the summands' magnitudes.
