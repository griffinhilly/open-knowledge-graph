---
id: basis-definition
title: Basis of a Vector Space
domain: mathematics
course: linear-algebra
prerequisites:
- id: span-and-basis
  type: hard
- id: linear-independence
  type: hard
builds-toward:
- dimension-vector-space
- rank-nullity-theorem
tags:
- basis
- vector spaces
- linear combinations
stage: formal-systems
status: validated
---

# Basis of a Vector Space

## Core Idea
A basis of a vector space V is a linearly independent spanning set. Every vector in V has a unique representation as a linear combination of basis vectors. A space with a finite basis has dimension equal to the number of basis vectors. Different bases have equal size.

## Questions

```yaml
- question: "The set {(1,0), (0,1), (1,1)} spans ℝ². Why is it NOT a basis for ℝ²?"
  type: multiple-choice
  options:
    - "It contains more than 2 vectors, and a basis for ℝ² must have exactly 2"
    - "The vector (1,1) is a linear combination of the other two, so the set is linearly dependent — any vector in ℝ² has multiple representations"
    - "The vectors do not all have length 1, so they cannot form a basis"
    - "Three vectors cannot span a 2-dimensional space"
  answer: 1
  explanation: "The set spans ℝ² (option A captures something real — 3 vectors in a 2D space is 'too many' — but the precise reason is linear dependence). Because (1,1) = (1,0) + (0,1), it is redundant. Any vector in ℝ² can now be written in infinitely many ways as a combination of these three, destroying the uniqueness property a basis requires. Removing the redundant vector gives the standard basis {(1,0),(0,1)}, which is both independent and spanning."

- question: "A set S is linearly independent in a vector space V but does not span V. What is the most accurate statement about S?"
  type: multiple-choice
  options:
    - "S is a basis for V, since independence is the harder condition to satisfy"
    - "S is too large — a basis cannot contain vectors that don't span"
    - "S fails to be a basis because it is missing the spanning condition; it is a basis only for the subspace it does span"
    - "S can never be extended to a basis for V by adding more vectors"
  answer: 2
  explanation: "A basis requires both independence AND spanning. S has independence but lacks spanning — it is 'too small.' It serves as a basis for the subspace it spans (which is a proper subspace of V), but not for V itself. Importantly, S can always be extended to a basis for V by adding vectors; the extension theorem guarantees this. The common error here is thinking independence alone is sufficient — both conditions are necessary."

- question: "If a set of vectors spans a vector space, it is automatically a basis for that space."
  type: true-false
  answer: false
  explanation: "Spanning is necessary but not sufficient. A spanning set may contain redundant vectors — vectors that are linear combinations of others — making it linearly dependent. Such a set allows each vector in the space to be represented in multiple ways, which defeats the coordinate system a basis provides. To be a basis, the set must be both spanning and linearly independent. Removing redundant vectors from a spanning set produces a basis."

- question: "If a vector space V has one basis consisting of 4 vectors, then every basis of V consists of exactly 4 vectors."
  type: true-false
  answer: true
  explanation: "This is the invariance of dimension theorem: all bases of a finite-dimensional vector space have the same cardinality, which defines the dimension of the space. The proof uses the fact that any independent set has size ≤ any spanning set. This invariance is what makes dimension a well-defined property of the space itself rather than of a particular choice of basis — and it flows directly from the uniqueness-of-representation property that a basis guarantees."

- question: "Explain why a linearly dependent spanning set fails to be a basis, and what specifically goes wrong with representations."
  type: short-answer
  answer: "When a spanning set contains a redundant vector — one expressible as a combination of the others — every vector in the space can be written as a linear combination in infinitely many ways. A basis requires that every vector have exactly one representation as a combination of basis vectors. That uniqueness is what makes coordinates meaningful: in a basis, the coefficients of the linear combination are the coordinates. Dependency destroys this by introducing free choices in how to distribute weight among the redundant vectors."
  explanation: "The redundancy creates a 'free parameter': you can always shift some weight from the redundant vector to the others and get a different-looking representation of the same vector. This is not a minor issue — it means there is no canonical coordinate system, no way to assign unique numerical labels to vectors. The independence condition eliminates this degree of freedom and restores uniqueness."
```

## Explainer

Your two prerequisites give you the two halves of the basis definition. A **spanning set** is a set of vectors from which you can reach every vector in the space by taking linear combinations — it's big enough to cover everything. A **linearly independent** set is one in which no vector is redundant — none can be written as a combination of the others. A **basis** is a set that is both at once: big enough to span, lean enough to be independent. It is the "just right" set — neither too small nor too large.

Why does independence matter if you already have a spanning set? Suppose you span ℝ² with three vectors: (1,0), (0,1), and (1,1). You can reach every point in the plane, but (1,1) is redundant — it's already the sum of the first two. That redundancy has a cost: the representation of any vector as a linear combination is no longer unique. The vector (2,3) could be written as 2(1,0) + 3(0,1) + 0(1,1), or as 1(1,0) + 3(0,1) + 1(1,1) − something, or infinitely many ways. A basis eliminates this ambiguity: with a basis, every vector has **exactly one** representation as a linear combination of basis vectors.

The standard example in ℝ³ is the **standard basis**: e₁ = (1,0,0), e₂ = (0,1,0), e₃ = (0,0,1). These three vectors are clearly independent (none is a combination of the others) and clearly span ℝ³ (any (a,b,c) = ae₁ + be₂ + ce₃). The coefficients (a,b,c) are simply the coordinates — a fact that feels obvious here but generalizes powerfully to abstract vector spaces where "coordinates" only make sense relative to a chosen basis.

A fundamental theorem says all bases of a finite-dimensional vector space have the same number of vectors. That number is the **dimension** of the space. ℝ³ has dimension 3; the space of polynomials of degree ≤ 2 has dimension 3 (basis: {1, x, x²}); a line through the origin has dimension 1. Dimension is a property of the space itself, not of any particular basis. This invariance is what makes dimension a meaningful concept, and it flows directly from the uniqueness-of-representation property that a basis guarantees.
