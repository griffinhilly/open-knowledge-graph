---
id: vector-addition-subtraction
title: Vector Addition and Subtraction
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn-definition
  type: hard
builds-toward:
- vector-spaces-definition
- span-spanning-set
- linear-independence
tags:
- vectors
- operations
- addition
stage: formal-systems
status: draft
---

# Vector Addition and Subtraction

## Core Idea
Vectors are added and subtracted component-wise: (u₁ + v₁, u₂ + v₂, ..., uₙ + vₙ). Geometrically, addition follows the parallelogram rule; subtraction finds the vector between two points. These operations satisfy closure, associativity, and commutativity, forming the foundation of vector space structure.

## How It's Best Learned
Visualize in R^2 using arrows. Add vectors tip-to-tail or using the parallelogram method. Verify algebraically with components. Then practice with higher dimensions using notation only.

## Common Misconceptions
- Thinking vector addition is like adding magnitudes; magnitudes don't add linearly.
- Incorrectly applying operations component-by-component when vectors have different dimensions.

## Explainer

You already know that a vector in Rⁿ is an ordered list of n real numbers — a point, or equivalently an arrow, in n-dimensional space. **Vector addition** is the simplest thing you can do with two such arrows: add them entry by entry. If **u** = (u₁, u₂) and **v** = (v₁, v₂), then **u** + **v** = (u₁ + v₁, u₂ + v₂). The component-wise rule is purely algebraic, but geometry makes it vivid.

In the plane, picture **u** as an arrow from the origin to some point, and **v** as another. The **tip-to-tail rule** says: to add them, place the tail of **v** at the tip of **u**. The result is the arrow from the origin to the new tip. Equivalently, **u** + **v** is the diagonal of the parallelogram whose sides are **u** and **v**. These two geometric pictures — tip-to-tail and the parallelogram — are equivalent, and either one lets you visualize addition in R² or R³ before generalizing to higher dimensions where pictures are no longer available.

**Vector subtraction** **u** − **v** = **u** + (−**v**) is just addition of the negated vector. Geometrically, −**v** is the same arrow pointing in the opposite direction. A particularly useful interpretation: **u** − **v** is the vector *from* **v** *to* **u**. If **u** and **v** are position vectors of two points P and Q, then **u** − **v** is the displacement from Q to P. This shows up constantly in geometry — the vector connecting two points is always a difference of their position vectors.

One thing to watch: adding magnitudes is wrong. If |**u**| = 3 and |**v**| = 4, then |**u** + **v**| is *not* 7 in general. It equals 7 only if the vectors point in exactly the same direction. If they are perpendicular, it equals 5 (by the Pythagorean theorem), and if they are antiparallel, it equals 1. This is why the triangle inequality ||**u** + **v**|| ≤ ||**u**|| + ||**v**|| holds with equality only in the collinear case. The component-wise addition rule is always exact; the magnitude has to be computed from the sum, not from the summands' magnitudes.
