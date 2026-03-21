---
id: dot-product-geometry
title: Dot Product and Projections
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vectors-3d-coordinate-system
  type: hard
- id: dot-product
  type: hard
builds-toward:
- directional-derivatives
- gradient-vector-properties
tags:
- dot-product
- projections
- orthogonality
stage: formal-systems
status: draft
---

# Dot Product and Projections

## Core Idea
The dot product a·b = |a||b|cos(θ) measures how aligned two vectors are. Geometrically, it computes the projection of one vector onto another: proj_a(b) = (a·b/|a|²)a. When a·b = 0, vectors are orthogonal.

## Questions

```yaml
- question: "Vectors u and v are both nonzero, and their dot product u·v = 0. A student concludes at least one must actually be zero, reasoning 'you can't multiply two nonzero numbers and get zero.' What error is this?"
  type: multiple-choice
  options:
    - "The student is correct — zero dot product requires at least one zero vector"
    - "The dot product is not scalar multiplication of lengths; the formula u·v = |u||v|cos(θ) shows that two nonzero vectors can have zero dot product when θ = 90°, since cos(90°) = 0"
    - "The student should check whether the vectors are in the same dimension before concluding"
    - "Zero dot product means the vectors are parallel, not that one must be zero"
  answer: 1
  explanation: "The dot product is not a simple multiplication of magnitudes — it includes the cosine of the angle between them. When two nonzero vectors are perpendicular, cos(90°) = 0, making the entire product zero regardless of the magnitudes. This is precisely the orthogonality test: u·v = 0 if and only if u and v are perpendicular (or one is the zero vector). The student's error was treating the dot product like regular scalar multiplication."

- question: "The vector projection proj_a(b) represents which geometric quantity?"
  type: multiple-choice
  options:
    - "The component of b that is perpendicular to a"
    - "A vector in the direction of a whose length equals the full magnitude of b"
    - "The component of b along the direction of a — its shadow cast onto the line through a"
    - "The vector midpoint between a and b"
  answer: 2
  explanation: "proj_a(b) decomposes b into its component parallel to a. The formula proj_a(b) = ((a·b)/|a|²)a gives a vector in the direction of a, scaled by how much of b lies in that direction. The remaining component b − proj_a(b) is perpendicular to a by construction. This decomposition — parallel plus perpendicular — is one of the most repeatedly useful tools in vector calculus, underlying everything from distance-to-a-plane computations to directional derivatives."

- question: "Two vectors with equal magnitudes must have a non-negative dot product."
  type: true-false
  answer: false
  explanation: "Equal magnitudes say nothing about direction. If two vectors of equal length point in opposite directions (θ = 180°), their dot product is |u||v|cos(180°) = −|u|², which is negative. The dot product depends on both magnitude and the cosine of the angle. Equal magnitudes fix |u||v| but leave cos(θ) free to be positive, zero, or negative."

- question: "The scalar projection of b onto a gives the signed length of b's component in the direction of a."
  type: true-false
  answer: true
  explanation: "The scalar projection comp_a(b) = (a·b)/|a| = |b|cos(θ) is the signed length of b's shadow along a. It is positive when b has a component in the same direction as a (θ < 90°), zero when perpendicular, and negative when b leans away from a (θ > 90°). The signed quality is important: it tells you not just how long the projection is but which way it points along a."

- question: "Why does the gradient vector ∇f point in the direction of steepest ascent? Use the dot product to explain."
  type: short-answer
  answer: "The directional derivative of f in direction u is ∇f · u. By the formula a·b = |a||b|cos(θ), this equals |∇f||u|cos(θ). Since u is a unit vector (|u| = 1), this simplifies to |∇f|cos(θ), which is maximized when cos(θ) = 1 — i.e., when u aligns exactly with ∇f. The gradient points in the direction that maximizes alignment with itself, which is by definition the direction of steepest ascent."
  explanation: "This is why learning the dot product as a measure of alignment pays off immediately in vector calculus. Every question about 'how fast does f change in direction u?' reduces to a dot product with the gradient. The direction of steepest ascent is the direction that maximizes cos(θ) — a purely geometric fact about alignment that follows directly from the cosine interpretation of the dot product."
```

## Explainer

You already know the algebraic definition of the dot product: **a** · **b** = a₁b₁ + a₂b₂ + a₃b₃ for vectors in R³. What the formula **a** · **b** = |**a**||**b**|cos(θ) adds is a geometric interpretation: the dot product is the product of the two magnitudes, scaled by the cosine of the angle between them. Cosine is 1 when the vectors point the same way, 0 when perpendicular, and −1 when antiparallel. So the dot product is a measure of **alignment** — how much the two vectors point in the same direction, weighted by their lengths.

This is why **orthogonality** (perpendicularity) has the clean test **a** · **b** = 0. At 90°, cos(θ) = 0, so the product vanishes regardless of the magnitudes. Two nonzero vectors with zero dot product are perpendicular. This test generalizes to any dimension, even when you have no direct geometric picture of "perpendicular" — in Rⁿ, we *define* orthogonality by the dot product being zero. The algebraic formula extends the geometric notion.

The **scalar projection** of **b** onto **a** is the signed length of **b**'s shadow cast along the direction of **a**: comp_**a**(**b**) = (**a** · **b**)/|**a**| = |**b**|cos(θ). The **vector projection** rescales the unit vector in **a**'s direction by this amount: proj_**a**(**b**) = ((**a** · **b**)/|**a**|²)**a**. Intuitively, you are decomposing **b** into two components: one along **a** and one perpendicular to **a**. The vector projection gives the parallel component; subtracting it from **b** gives the perpendicular component **b** − proj_**a**(**b**), which is orthogonal to **a** by construction. This decomposition — parallel plus perpendicular — is one of the most repeatedly useful tools in vector calculus.

The dot product's role will grow significantly as you move to directional derivatives and gradients. The directional derivative of f in direction **u** is ∇f · **u** — the dot product of the gradient with a unit vector. This dot product is maximized when **u** aligns with ∇f, which is why the gradient points in the direction of steepest ascent. Every statement about "how fast f changes in direction **u**" is a dot product statement. Learning to see alignment and projection as the fundamental interpretations of the dot product now sets you up to read gradient geometry fluently.
