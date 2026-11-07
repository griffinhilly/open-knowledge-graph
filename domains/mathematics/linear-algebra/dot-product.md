---
id: dot-product
title: Dot Product (Inner Product in R^n)
domain: mathematics
course: linear-algebra
prerequisites:
- id: vector-addition-subtraction
  type: hard
- id: scalar-multiplication
  type: hard
- id: vector-operations
  type: hard
- id: vectors-3d-coordinate-system
  type: soft
- id: vectors-in-rn-operations
  type: hard
- id: vectors-in-two-dimensions
  type: soft
- id: law-of-cosines
  type: soft
builds-toward:
- vector-norms
- cross-product
- orthogonal-projections
- inner-product-spaces
tags:
- dot-product
- inner-product
- angle
- projection
stage: formal-systems
status: validated
---

# Dot Product (Inner Product in R^n)

## Core Idea
The dot product of two vectors u and v is the sum of products of corresponding components: u · v = u₁v₁ + u₂v₂ + ... + uₙvₙ. It measures alignment between vectors and connects to angle via cos(θ) = (u · v)/(‖u‖‖v‖). The dot product is zero precisely when vectors are orthogonal.

## How It's Best Learned
Check the angle formula against angles you can see. On graph paper, (1,0) and (1,1) meet at 45°. The formula gives cos(θ) = 1/√2, which agrees. Then try (1,1,0) and (0,1,1) in ℝ³: the dot product is 1, the norms multiply to 2, so θ = 60°. Finally draw (3,4) and (4,−3) and confirm a zero dot product looks like a right angle.

## Common Misconceptions
- The dot product of (u₁, u₂) and (v₁, v₂) is the vector (u₁v₁, u₂v₂). (The products are added, so the result is a single number.)
- A larger dot product means a smaller angle. (Length matters too. (10,0) · (10,10) = 100 at 45°, while (1,0) · (2,0) = 2 at 0°. Compare angles using cos(θ), which divides out the lengths.)
- u · v equals ‖u‖ ‖v‖ for any two vectors. (That holds only when the vectors point the same way or one of them is zero. In general |u · v| ≤ ‖u‖ ‖v‖, which is the Cauchy–Schwarz inequality.)

## Questions

```yaml
- question: "Let u = (2, −1, 3) and v = (1, 4, 0). What is u · v?"
  type: multiple-choice
  options: ["-2", "2", "7", "-7"]
  answer: 0
  explanation: "u · v = (2)(1) + (−1)(4) + (3)(0) = 2 − 4 + 0 = −2. Each pair of corresponding components is multiplied and the products are summed. The zero from the third pair contributes nothing."

- question: "If u · v = 0, then at least one of u or v must be the zero vector."
  type: true-false
  answer: false
  explanation: "Two nonzero vectors can have a zero dot product whenever they are orthogonal (perpendicular). For example, u = (1, 0) and v = (0, 1) are both nonzero but u · v = 0. Only the zero vector has a zero dot product with every other vector."

- question: "The dot product of two nonzero vectors is negative. What does this tell you about the angle between them?"
  type: short-answer
  answer: "The angle is obtuse — strictly between 90° and 180°."
  explanation: "From cos(θ) = (u · v) / (‖u‖ ‖v‖): since the norms ‖u‖ and ‖v‖ are positive, a negative dot product forces cos(θ) < 0, which means θ ∈ (90°, 180°). The vectors point more away from each other than toward each other."
```

## Explainer

You already know how to add vectors component-by-component and scale them by scalars. The dot product is a new kind of operation: it takes two vectors and returns a single number (a scalar), not another vector. The formula is straightforward — multiply corresponding components and add all the products: u · v = u₁v₁ + u₂v₂ + … + uₙvₙ. What makes this operation important is not the arithmetic but what the resulting number means.

The dot product measures how much two vectors "agree in direction." The key relationship is the angle formula: cos(θ) = (u · v) / (‖u‖ ‖v‖), where θ is the angle between u and v and ‖u‖, ‖v‖ are their lengths (magnitudes). This lets you interpret the sign and size of the dot product geometrically. If u · v > 0, the angle is acute — the vectors point roughly the same way. If u · v = 0, the angle is exactly 90°, meaning the vectors are orthogonal (perpendicular). If u · v < 0, the angle is obtuse — the vectors point more away from each other than toward each other.

Orthogonality deserves special attention because it comes up constantly in linear algebra. Two vectors are orthogonal if and only if their dot product is zero. This is a purely algebraic test for a geometric property: no trigonometry required. From your work with vector addition, you know that vectors can be decomposed and recombined; orthogonal vectors are the cleanest building blocks because they carry zero "overlap" with each other.

The dot product also connects directly to projections. The scalar projection of u onto v — how much of u lies along v's direction — is exactly (u · v) / ‖v‖. If you have been thinking of u as a force and v as a direction of motion, this projection is the component of the force doing useful work. That physical interpretation is why the dot product appears throughout mechanics, electromagnetism, and signal processing.
