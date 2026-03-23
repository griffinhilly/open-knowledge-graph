---
id: basis-and-dimension
title: Basis and Dimension
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-independence
  type: hard
- id: span-of-vectors
  type: hard
builds-toward:
- rank-and-nullity-theorem
- change-of-basis
tags:
- basis
- dimension
- coordinates
stage: formal-systems
status: validated
---

# Basis and Dimension

## Core Idea
A basis of vector space V is a linearly independent spanning set. Every basis has the same cardinality, called the dimension of V. Dimension is the minimum number of vectors needed to span V and the maximum size of a linearly independent set. Coordinates relative to a basis are unique.

## Questions

```yaml
- question: "Which of the following sets is a basis for ℝ²?"
  type: multiple-choice
  options:
    - "{(1,0), (0,1), (1,1)}"
    - "{(1,2), (2,4)}"
    - "{(1,0), (0,1)}"
    - "{(0,0), (1,0)}"
  answer: 2
  explanation: "A basis must be linearly independent AND span the space. {(1,0),(0,1)} is the standard basis — 2 independent vectors that span ℝ². The first set has 3 vectors and is not linearly independent. The second set is linearly dependent (each vector is a scalar multiple of the other). The fourth contains the zero vector, which makes any set linearly dependent."

- question: "Every linearly independent set of vectors in ℝ³ is a basis for ℝ³."
  type: true-false
  answer: false
  explanation: "A basis must satisfy two conditions: linear independence AND spanning. Two linearly independent vectors in ℝ³ span only a plane through the origin, not all of ℝ³. A basis for ℝ³ requires exactly 3 linearly independent vectors. Having too few independent vectors means the set cannot span the full space."

- question: "If a vector space has dimension n, what is the maximum number of vectors in any linearly independent set?"
  type: short-answer
  answer: "n"
  explanation: "The dimension n is simultaneously the size of every basis, the maximum size of any linearly independent set, and the minimum size of any spanning set. Any linearly independent set with n vectors automatically spans the space and is therefore a basis. Trying to find n+1 linearly independent vectors always fails — the (n+1)th must be a linear combination of the others."
```

## Explainer

A basis is the most economical way to describe a vector space: it is a set of vectors that is both large enough to reach everywhere in the space (spanning) and small enough to have no redundancy (linear independence). Think of it like a coordinate system — the standard basis vectors **e₁ = (1,0)** and **e₂ = (0,1)** in ℝ² let you describe any vector as a unique combination, like (3,−2) = 3**e₁** + (−2)**e₂**. If you added a third vector like (1,1), you would have redundancy; if you removed one, you could no longer reach all of ℝ².

The central theorem is that every basis for a given vector space has the same number of vectors. This common count is the **dimension** of the space. It does not matter which basis you pick — the standard basis, a rotated basis, an unusual-looking basis — they all have the same size. This is what makes dimension a well-defined property of the space itself, not of any particular basis. ℝ³ has dimension 3, the space of polynomials of degree ≤ 2 has dimension 3 (basis: {1, x, x²}), and the zero vector space has dimension 0.

Dimension has two equivalent characterizations that are worth internalizing: it is the *minimum* number of vectors needed to span the space, and the *maximum* number of vectors that can be linearly independent. These are dual perspectives on the same fact. Any spanning set with exactly n vectors must be independent (hence a basis). Any independent set with exactly n vectors must span (hence a basis). So checking either condition, if the count is right, automatically gives you the other.

The uniqueness of coordinates is the payoff. Once you fix a basis {**v₁**, …, **vₙ**}, every vector **w** in the space can be written as **w** = c₁**v₁** + ⋯ + cₙ**vₙ** in exactly one way. Those scalars (c₁, …, cₙ) are the **coordinates** of **w** in that basis. This is why linear independence matters so deeply — if the basis vectors were linearly dependent, coordinates would not be unique, and the whole coordinate system would break down.
