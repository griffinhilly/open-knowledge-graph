---
id: basis-and-dimension
title: Basis and Dimension
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-independence
  type: hard
- id: subspaces
  type: hard
- id: span-of-vectors
  type: hard
builds-toward:
- rank-and-nullity-theorem
- change-of-basis
- orthonormal-bases
tags:
- basis
- dimension
- coordinate
- minimal spanning set
- uniqueness
stage: formal-systems
status: validated
---

# Basis and Dimension

## Core Idea
A basis for a vector space (or subspace) V is a set of vectors that is both linearly independent and spans V — it is a minimal spanning set and a maximal independent set simultaneously. Every basis for the same vector space has the same number of elements, and that number is the dimension of V. Any vector in V can be written uniquely as a linear combination of basis vectors, providing a coordinate system for V. The standard basis {e₁, e₂, …, eₙ} for Rⁿ is the familiar example, but infinitely many other bases exist.

## How It's Best Learned
Prove that every spanning set can be trimmed to a basis (remove dependent vectors) and every independent set can be extended to a basis (add vectors). This 'shrink' and 'grow' intuition clarifies what a basis achieves.

## Common Misconceptions
- A basis is not unique; a vector space has infinitely many bases, all with the same number of elements.
- 'Dimension' of a vector space is not the same as the number of components of a vector (e.g., the space of 3×3 matrices has dimension 9, not 3).
- A basis must satisfy BOTH conditions — spanning alone (with dependence) or independence alone (without spanning) is insufficient.
