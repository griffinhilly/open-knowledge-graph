---
id: dot-product-precalculus
title: Dot Product
domain: mathematics
course: precalculus
prerequisites:
  - id: vector-operations
    type: hard
  - id: law-of-cosines
    type: soft
builds-toward:
  - work-as-integral
tags: [vectors, dot-product, orthogonality]
stage: formal-systems
status: validated
---

# Dot Product

## Core Idea
The dot product of two vectors u = (u1, u2) and v = (v1, v2) is u * v = u1*v1 + u2*v2, a scalar (not a vector). Geometrically, u * v = |u| |v| cos(theta), where theta is the angle between them. The dot product measures how much two vectors point in the same direction. It is zero when vectors are perpendicular (orthogonal), positive when they point similarly, and negative when they point oppositely.

## How It's Best Learned
Compute dot products algebraically, then verify with the geometric formula. Use the dot product to find angles between vectors, check orthogonality, and compute projections. Connect to work in physics (W = F * d) and to the Law of Cosines.

## Common Misconceptions
- Expecting the dot product to produce a vector (it produces a scalar).
- Forgetting that the geometric formula requires the angle between the vectors, not a reference angle.
- Confusing dot product with cross product (which exists in 3D and produces a vector).

## Questions

```yaml
- question: "Vectors u = (3, 0) and v = (0, 5). What is u · v, and what does it reveal about these vectors?"
  type: multiple-choice
  options:
    - "15 — multiply the nonzero components"
    - "8 — add all the components together"
    - "0 — the vectors are perpendicular to each other"
    - "(0, 0) — the dot product cancels the vectors"
  answer: 2
  explanation: "u · v = 3·0 + 0·5 = 0. The dot product is always a scalar (never a vector), and a value of zero means the angle between the vectors is 90° — they are orthogonal. This is the key test for perpendicularity: you don't need to find the angle explicitly, just check whether the dot product is zero. Options A and B reflect common arithmetic errors; option D reflects the misconception that the dot product produces a vector."

- question: "If u · v = −20 and both u and v are nonzero vectors, what can you conclude about the angle θ between them?"
  type: multiple-choice
  options:
    - "θ = 90°, because the product is not zero"
    - "θ is obtuse (greater than 90°), because cos θ must be negative"
    - "θ = 180°, because the dot product is negative"
    - "The vectors must have opposite signs in at least one component, so no conclusion about θ is possible"
  answer: 1
  explanation: "From the geometric formula u · v = |u||v|cos θ, a negative dot product means cos θ < 0, which means θ is between 90° and 180° — obtuse. The dot product is exactly −|u||v| only when θ = 180° (exactly opposite). A negative dot product rules out θ ≤ 90° but doesn't pin down the angle precisely. The sign of the dot product is a reliable indicator of which 'half' the angle falls in: positive (same general direction), zero (perpendicular), negative (opposing direction)."

- question: "The dot product of two nonzero vectors can equal zero."
  type: true-false
  answer: true
  explanation: "Yes — when two nonzero vectors are perpendicular (θ = 90°), cos 90° = 0, so u · v = |u||v|·0 = 0. This is the orthogonality test. For example, (1, 0) · (0, 1) = 1·0 + 0·1 = 0, even though neither vector is the zero vector. This is one of the most important uses of the dot product: efficiently checking whether two vectors are perpendicular without computing any angles."

- question: "The dot product u · v measures the length of the vector formed by adding u and v."
  type: true-false
  answer: false
  explanation: "This confuses two entirely different operations. The dot product produces a scalar measuring directional agreement between the vectors. Adding u and v produces a new vector (by the parallelogram rule), and its length is |u + v| — a completely separate computation. The dot product encodes the angle between vectors via u · v = |u||v|cos θ, not anything about their vector sum."

- question: "Why does the dot product equal zero when two vectors are perpendicular? Use the geometric formula to explain the connection between angle and scalar output."
  type: short-answer
  answer: "The geometric formula is u · v = |u||v|cos θ. When θ = 90°, cos 90° = 0, so the entire product collapses to zero regardless of the magnitudes. Geometrically, the dot product measures 'how much' the vectors align — how much one projects onto the other. At 90°, neither vector has any component in the direction of the other, so there is zero directional overlap, and the dot product reflects this with a value of zero."
  explanation: "This is why the dot product is the standard orthogonality test. The algebraic formula (sum of component products) and the geometric formula (|u||v|cos θ) are two ways of computing the same quantity, so checking whether the component sum is zero is equivalent to checking whether the angle is 90°."
```

## Explainer

From vector operations, you know how to add vectors and scale them, but those operations always return another vector. The **dot product** does something different: it takes two vectors and returns a single number. That number encodes something geometrically meaningful — how much the two vectors "agree" in direction.

The algebraic definition is straightforward: for u = (u₁, u₂) and v = (v₁, v₂), the dot product is u · v = u₁v₁ + u₂v₂. Multiply corresponding components, then add. For example, (3, 4) · (1, 2) = 3·1 + 4·2 = 3 + 8 = 11. This formula extends naturally to any number of dimensions: just multiply matching components and sum. The result is always a scalar — a plain number with no direction.

The geometric formula u · v = |u| |v| cos θ reveals what that scalar measures. Here θ is the angle between the vectors. When the vectors point in the same direction, θ = 0 and cos θ = 1, giving the maximum possible dot product. When they are **perpendicular** (θ = 90°), cos θ = 0 and the dot product is exactly zero — this is the test for **orthogonality**. When they point in opposite directions, θ = 180° and the dot product is negative. The dot product's sign alone tells you whether two vectors point toward the same half-space (positive), are perpendicular (zero), or oppose each other (negative).

You can connect this to the Law of Cosines you may have seen. The law of cosines says c² = a² + b² − 2ab cos θ for a triangle with sides a, b, c. If you set up the triangle with two sides as vectors u and v, then c = u − v, and expanding |u − v|² = |u|² − 2(u · v) + |v|² recovers the law of cosines exactly — with u · v playing the role of ab cos θ. This is more than a coincidence; it shows that the dot product is the algebraic encoding of angle, connecting the abstract component formula to the familiar geometry of triangles. This connection becomes the foundation for projection — decomposing one vector along the direction of another — which you will use extensively in calculus and linear algebra.
