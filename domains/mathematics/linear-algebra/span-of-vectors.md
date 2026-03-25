---
id: span-of-vectors
title: Span and Linear Combinations
domain: mathematics
course: linear-algebra
prerequisites:
- id: vector-spaces
  type: hard
- id: span-and-basis
  type: soft
builds-toward:
- basis-and-dimension
- column-space
tags:
- span
- linear-combination
- closure
stage: formal-systems
status: validated
---
# Span and Linear Combinations

## Core Idea
The span of vectors v₁, ..., vₖ is the set of all linear combinations c₁v₁ + ... + cₖvₖ where cᵢ ∈ ℝ. Span is a subspace, the smallest containing all given vectors. The columns of a matrix A span the column space; row vectors span the row space.

## Questions

```yaml
- question: "You have vectors v₁ = (1, 0) and v₂ = (0, 1) in ℝ². Which of the following is NOT in their span?"
  type: multiple-choice
  options:
    - "(3, −7)"
    - "(0, 0)"
    - "(1/2, √2)"
    - "None of the above — every vector in ℝ² is in their span"
  answer: 3
  explanation: "v₁ and v₂ are linearly independent vectors in ℝ², so their span is all of ℝ². Any vector (a, b) = a·v₁ + b·v₂, using real-valued scalars. All three listed vectors are in the span: (3, −7) = 3v₁ − 7v₂, (0, 0) uses coefficients 0 and 0, and (1/2, √2) = (1/2)v₁ + √2·v₂. The key insight: two linearly independent vectors in ℝ² reach every point in the plane."

- question: "A linear system Ax = b has no solution. What does this tell you about b relative to A?"
  type: multiple-choice
  options:
    - "b must be the zero vector"
    - "b lies in the column space of A"
    - "b does not lie in the column space of A"
    - "A has linearly dependent columns"
  answer: 2
  explanation: "Solving Ax = b asks: can b be written as a linear combination of the columns of A? That is exactly the question of whether b lies in the column space (the span of the columns). If there is no solution, b cannot be expressed as such a combination — b is outside the column space. The system Ax = b is solvable if and only if b ∈ col(A)."

- question: "The span of any set of vectors always contains the zero vector."
  type: true-false
  answer: true
  explanation: "Yes — set all scalar coefficients to zero: c₁·0 + c₂·0 + … + cₖ·0 = 0 is a valid linear combination. The zero vector is always achievable, which is one reason the span is always a subspace (subspaces must contain 0). This is a structural property of span, not a special case."

- question: "Adding any new vector to a spanning set always strictly enlarges the span."
  type: true-false
  answer: false
  explanation: "If the new vector is already in the existing span — that is, it can be expressed as a linear combination of the vectors already present — then adding it contributes nothing. The span remains the same. Only a vector that points in a genuinely 'new' direction (one not reachable from the current spanning set) enlarges the span. This is why linear independence matters: redundant vectors don't expand the span."

- question: "Why is the span of any set of vectors guaranteed to be a subspace? What two closure properties must be verified?"
  type: short-answer
  answer: "Span is closed under addition and scalar multiplication. If u = c₁v₁ + … + cₖvₖ and w = d₁v₁ + … + dₖvₖ are two linear combinations, then u + w = (c₁+d₁)v₁ + … + (cₖ+dₖ)vₖ is also a linear combination (closed under addition), and cu = (cc₁)v₁ + … + (ccₖ)vₖ is also a linear combination (closed under scalar multiplication)."
  explanation: "These two closure conditions — plus containing the zero vector — are exactly what a subspace requires. Span satisfies them automatically because adding coefficients and scaling coefficients produces new coefficients for the same generators. This is why span is the *smallest* subspace containing the given vectors: any subspace containing v₁, …, vₖ must be closed under linear combinations and therefore must contain the entire span."
```

## Explainer

From your study of vector spaces, you know that vectors can be added and scaled by real numbers. Now ask a natural question: starting from a small collection of vectors, what is the full set of vectors you can construct just using those two operations? The answer is the **span**. Given vectors v₁, v₂, ..., vₖ, a **linear combination** is any expression c₁v₁ + c₂v₂ + ... + cₖvₖ where the cᵢ are arbitrary real numbers. The span is the set of all such linear combinations — every vector you can reach by stretching, shrinking, and adding your starting collection.

Geometry gives the clearest intuition. A single nonzero vector v in ℝ³ spans a line through the origin: { tv : t ∈ ℝ }. Two vectors that are not parallel span a plane through the origin. Three vectors that don't all lie in a common plane span all of ℝ³. In each case, the span is the "flat space" that contains the given vectors and is closed under linear combinations. You cannot escape it without introducing a new vector that points in a direction not already expressible in terms of the others.

The span of any set of vectors is always a **subspace** of the ambient vector space. You can verify the two closure conditions directly: if u and w are both linear combinations of v₁, ..., vₖ, then so is u + w (just add the coefficients), and so is cu for any scalar c. Span is also the *smallest* subspace containing all of v₁, ..., vₖ — any subspace containing those vectors must contain all their linear combinations. Adding more vectors to the spanning set can only maintain or enlarge the span, never shrink it.

The connection to matrices ties everything together. For a matrix A, the **column space** is exactly the span of its column vectors. When you write the linear system Ax = b, you are asking whether b can be expressed as a linear combination of the columns of A — that is, whether b lies in the span of those columns. This reframes the question of solvability entirely: "does b lie in the column space?" becomes the central question of linear systems, leading directly to the concepts of basis and dimension.
