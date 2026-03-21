---
id: dot-product-definition
title: Dot Product and Inner Product
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn-definition
  type: hard
- id: vector-magnitude-norm
  type: hard
builds-toward:
- orthogonal-vectors-orthonormal-bases
- inner-product-spaces
tags:
- vectors
- dot product
- inner product
stage: formal-systems
status: draft
---

# Dot Product and Inner Product

## Core Idea
The dot product of vectors u and v is u·v = u₁v₁ + ... + uₙvₙ, a scalar equal to ||u|| ||v|| cos(θ) where θ is the angle between them. The dot product measures alignment: it's zero for perpendicular vectors and positive/negative based on acute/obtuse angles. It underpins geometric reasoning in linear algebra.

## Questions

```yaml
- question: "Two nonzero vectors u and v have dot product u·v = 0. What can you conclude?"
  type: multiple-choice
  options:
    - "One of the vectors must be the zero vector"
    - "The vectors are parallel — they point in the same direction"
    - "The vectors are perpendicular — the angle between them is 90°"
    - "The magnitudes of the two vectors are equal"
  answer: 2
  explanation: "Since u·v = ||u|| ||v|| cos(θ), and both ||u|| and ||v|| are nonzero (given), the dot product is zero only when cos(θ) = 0, which means θ = 90°. The vectors are perpendicular (orthogonal). This is one of the most important uses of the dot product: testing orthogonality. The zero dot product says nothing about magnitudes or about either vector being zero — it only tells you the angle is a right angle."

- question: "A student calculates that u·v = ||u|| × ||v|| for two nonzero vectors. What does this imply?"
  type: multiple-choice
  options:
    - "The vectors are perpendicular"
    - "The vectors point in exactly the same direction (θ = 0°)"
    - "The dot product has reached its minimum value"
    - "The vectors have equal magnitude"
  answer: 1
  explanation: "Since u·v = ||u|| ||v|| cos(θ), the equation u·v = ||u|| × ||v|| means cos(θ) = 1, which means θ = 0°. The vectors point in identical directions — they are parallel with no angular separation. This is the maximum possible value of the dot product for vectors of given magnitudes. When θ = 180° (opposite directions), u·v = −||u|| ||v||, its minimum. When θ = 90°, u·v = 0. The dot product traces the full range of directional agreement."

- question: "The dot product of two vectors is itself a vector pointing in the direction of the first vector."
  type: true-false
  answer: false
  explanation: "The dot product produces a scalar — a single number — not a vector. This is fundamental: multiplying matching components and adding the results yields a real number (e.g., u·v = u₁v₁ + u₂v₂ + u₃v₃ ∈ ℝ). Students often confuse the dot product with the cross product, which does produce a vector. The scalar nature of the dot product is precisely what makes it useful for measuring alignment (a property of the relationship between two vectors, summarizable as a single number) and for testing orthogonality."

- question: "If the dot product u·v is positive, then the angle between u and v is less than 90°."
  type: true-false
  answer: true
  explanation: "Since u·v = ||u|| ||v|| cos(θ) and both magnitudes are positive, the sign of u·v equals the sign of cos(θ). cos(θ) > 0 when 0° ≤ θ < 90° (the angle is acute). So a positive dot product tells you the vectors make an acute angle — they 'agree' more than they 'disagree' in direction. A negative dot product means the angle is obtuse (θ > 90°), indicating the vectors point in roughly opposite directions. The sign of the dot product is a fast way to classify the angle."

- question: "Why is the dot product described as measuring 'alignment' between vectors? How does the formula u·v = ||u|| ||v|| cos(θ) capture this intuition?"
  type: short-answer
  answer: "The dot product equals the product of the two magnitudes scaled by cos(θ), the cosine of the angle between them. Cosine is 1 when vectors point the same direction (maximum agreement), 0 when perpendicular (no agreement), and −1 when pointing opposite directions (maximum disagreement). So the dot product simultaneously accounts for how large the vectors are AND how well they agree directionally. Two long vectors pointing exactly the same way have the maximum dot product; two perpendicular vectors have zero regardless of their lengths. This is why the dot product measures directional alignment rather than just magnitude."
  explanation: "This geometric interpretation is what makes the dot product more than arithmetic. It enables projection (how much of u lies along v), orthogonality testing (u·v = 0 ↔ perpendicular), and angle computation (θ = arccos(u·v / (||u|| ||v||))). Without this geometric reading, the dot product would be an arbitrary computation; with it, it becomes the core tool for reasoning about angles and direction in any number of dimensions."
```

## Explainer

You already know that vectors in ℝⁿ are lists of coordinates representing direction and magnitude, and that the **norm** (length) of a vector is computed by summing squared components and taking the square root. The dot product is the next operation — and while it looks like a simple coordinate calculation (multiply matching components, add the products), its geometric meaning is what makes it so useful.

The dot product u·v = u₁v₁ + u₂v₂ + ... + uₙvₙ produces a single number, a **scalar**. Think of two vectors in ℝ² pointing in different directions. If they point in exactly the same direction, their dot product equals the product of their lengths (||u|| × ||v||), its maximum possible value. If they are perpendicular — pointing at a right angle — the dot product is exactly zero. If they point in roughly opposite directions, the dot product is negative. This is the geometric meaning: u·v = ||u|| ||v|| cos(θ), where θ is the angle between them. The dot product measures how much the two vectors "agree" in direction.

The most immediate use is testing for **orthogonality**: two nonzero vectors are perpendicular if and only if their dot product is zero. This is one of the most important computations in linear algebra — orthogonal vectors are independent in the strongest geometric sense, and building orthogonal sets of vectors is a central technique. The dot product also gives you the angle between any two vectors directly: θ = arccos(u·v / (||u|| ||v||)). You could never compute angles between high-dimensional vectors any other way.

A concrete application builds intuition: **projecting** one vector onto another. If you want to know how much of vector u lies in the direction of v, you compute the scalar projection: (u·v) / ||v||. Physically, this is like asking "how far does u's shadow extend along v?" If you then multiply by the unit vector in v's direction, you get the **vector projection** of u onto v. This operation is the geometric heart of least-squares fitting, Gram-Schmidt orthogonalization, and nearly every algorithm that decomposes vectors into components. The dot product is not just an arithmetic rule — it is the core tool for thinking about angles, projections, and geometric relationships in any number of dimensions.
