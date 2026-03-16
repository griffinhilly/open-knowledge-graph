---
id: dot-product
title: Dot Product (Inner Product in R^n)
domain: mathematics
course: linear-algebra
prerequisites:
- id: vector-addition-subtraction
  type: hard
- id: scalar-multiplication-vectors
  type: hard
builds-toward:
- vector-norms-magnitude
- cross-product
- orthogonal-projections
- inner-product-spaces
tags:
- dot-product
- inner-product
- angle
- projection
stage: formal-systems
status: draft
---

# Dot Product (Inner Product in R^n)

## Core Idea
The dot product of two vectors u and v is the sum of products of corresponding components: u · v = u₁v₁ + u₂v₂ + ... + uₙvₙ. It measures alignment between vectors and connects to angle via cos(θ) = (u · v)/(‖u‖‖v‖). The dot product is zero precisely when vectors are orthogonal.

## Questions

```yaml
- question: "Let u = (2, −1, 3) and v = (1, 4, 0). What is u · v?"
  type: multiple-choice
  options: ["-2", "2", "7", "-7"]
  answer: 0
  explanation: "u · v = (2)(1) + (−1)(4) + (3)(0) = 2 − 4 + 0 = −2. Each pair of corresponding components is multiplied and the products are summed. The zero from the third pair contributes nothing, illustrating that components beyond the shared dimension vanish."

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
