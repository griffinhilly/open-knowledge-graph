---
id: span-and-basis
title: Span, Linear Independence, and Basis
domain: mathematics
course: linear-algebra
prerequisites:
- id: subspaces
  type: hard
builds-toward:
- basis-and-dimension
- change-of-basis
tags:
- span
- linear-independence
- basis
stage: formal-systems
status: validated
---

# Span, Linear Independence, and Basis

## Core Idea
The span of vectors v₁, ..., vₖ is all linear combinations c₁v₁ + ... + cₖvₖ, forming a subspace. Vectors are linearly independent if c₁v₁ + ... + cₖvₖ = 0 only when all cᵢ = 0. A basis is a maximal linearly independent set (or equivalently, a minimal spanning set). Every basis has the same cardinality—the dimension.

## How It's Best Learned
Compute span geometrically in R² and R³ (lines, planes). Check linear independence by row-reducing the matrix of vectors. Build a basis by selecting pivot columns from a spanning set.

## Questions

```yaml
- question: "You have three vectors in R²: v₁=(1,0), v₂=(0,1), v₃=(2,3). Which is true?"
  type: multiple-choice
  options:
    - "{v₁, v₂, v₃} is a valid basis for R² because all three are needed to reach every point"
    - "{v₁, v₂, v₃} spans R² but is not a basis, because v₃ is a linear combination of v₁ and v₂"
    - "{v₁, v₂} is not a basis because it doesn't include the large vector v₃=(2,3)"
    - "Any two of these three vectors form a linearly independent set and thus a basis for R²"
  answer: 1
  explanation: "Since v₃ = 2v₁ + 3v₂, v₃ is linearly dependent on v₁ and v₂. The set {v₁,v₂,v₃} spans R² correctly, but fails the independence requirement — v₃ is redundant. A basis must be both spanning AND independent. Option A is the classic misconception: 'we need v₃ to reach (2,3)' confuses span (you can reach (2,3) using v₁ and v₂ alone) with independence. Option D is also false: (1,0) and (2,0) are two vectors in R² that are NOT independent — being two vectors doesn't guarantee independence."

- question: "Five vectors span a subspace V, but some are linearly dependent. After removing the redundant ones, 3 linearly independent vectors remain that still span V. What can you conclude?"
  type: multiple-choice
  options:
    - "V has dimension 3, and any basis for V must contain exactly 3 vectors"
    - "V has dimension between 3 and 5, since the original set needed 5 vectors"
    - "The dimension of V depends on which 3 vectors were kept, not just their count"
    - "V is 5-dimensional because 5 vectors were originally required to describe it"
  answer: 0
  explanation: "Once you have 3 linearly independent vectors that span V, you have a basis. The fundamental theorem of dimension states that every basis for the same subspace has the same cardinality. So V has dimension exactly 3 — any other basis will also have 3 vectors. Option B is wrong because the original 5-vector spanning set was overcomplete (had redundancy); it's the size of a *minimal* spanning set (a basis) that defines dimension, not the size of any spanning set. Option D conflates the size of an over-complete spanning set with dimension."

- question: "Two vectors are linearly dependent if and only if at least one of them is the zero vector."
  type: true-false
  answer: false
  explanation: "Linear dependence means one vector can be written as a linear combination of the others — equivalently, there exist scalars c₁, c₂, not all zero, such that c₁v₁ + c₂v₂ = 0. Two nonzero vectors like (1,2) and (2,4) are linearly dependent (the second is 2× the first) without either being zero. Geometrically in R², two nonzero vectors are dependent if and only if they are parallel (collinear through the origin). The zero vector does always create dependence, but dependence does not require a zero vector."

- question: "If you add a vector w to a linearly independent set {v₁, ..., vₖ}, the result is still linearly independent only if w is not in the span of {v₁, ..., vₖ}."
  type: true-false
  answer: true
  explanation: "If w is already a linear combination of v₁,...,vₖ, then adding w creates linear dependence: you can write w − (c₁v₁ + ... + cₖvₖ) = 0 with non-trivial coefficients. If w is outside the span, no such combination exists, and independence is preserved. This is the key link between span and independence: a vector extends the span if and only if it extends the independent set — the two concepts are dual in exactly this sense."

- question: "Why must every basis for the same subspace have the same number of vectors? What would go wrong if two bases had different cardinalities?"
  type: short-answer
  answer: "If V had a basis B₁ with k vectors and a basis B₂ with m > k vectors, then B₂ is a set of m linearly independent vectors all living in a space spanned by k vectors. But any independent set in a k-dimensional space has at most k vectors — a contradiction. The Exchange Lemma formalizes this: any independent set has at most as many vectors as any spanning set, forcing all minimal spanning sets (bases) to share the same size."
  explanation: "The equal-cardinality result is why 'dimension' is a well-defined property of the subspace itself, not of any particular basis. Without it, dimension would be ambiguous — the same plane through the origin might have 'dimension 2' with one basis and 'dimension 3' with another, making the concept useless. The result says dimension measures the degrees of freedom in a subspace — how many truly independent directions it contains — a fact about the geometry, not the coordinates."
```

## Explainer

You already know that a **subspace** is a subset of Rⁿ closed under addition and scalar multiplication. The concept of span answers the question: given a collection of vectors, what subspace do they generate? The **span** of vectors v₁, …, vₖ is the set of all linear combinations c₁v₁ + c₂v₂ + … + cₖvₖ, where each cᵢ is any real number. In R², the span of a single nonzero vector is a line through the origin. The span of two vectors that point in different directions is all of R² — you can reach any point by choosing the right scalars. If the two vectors point in the same direction, their span is still just a line: one of them adds no new reach.

That last observation motivates **linear independence**. A set of vectors is linearly independent if the only way to combine them to get the zero vector is by setting every coefficient to zero: c₁v₁ + … + cₖvₖ = 0 implies c₁ = c₂ = … = cₖ = 0. Linear independence means no vector in the set is redundant — none can be written as a combination of the others. If one can, you have linear dependence, and removing that vector doesn't shrink the span. Geometrically: two vectors in R² are linearly dependent if and only if they are collinear (parallel or anti-parallel).

A **basis** for a subspace V is a set of vectors that does two things simultaneously: it spans V (you can reach everything in V), and it is linearly independent (there is no redundancy). These are dual requirements: a spanning set might have too many vectors (some redundant), while a linearly independent set might have too few (missing some of V). A basis hits the sweet spot — it is a minimal spanning set and a maximal independent set at the same time. For example, the standard basis vectors e₁ = (1,0,0), e₂ = (0,1,0), e₃ = (0,0,1) form a basis for R³: they span all of R³ and are independent.

The deepest theorem in this area is that **every basis for a subspace has the same number of vectors**. That common count is the **dimension** of the subspace. This is not obvious — it requires proof — but it means dimension is a well-defined property of the subspace, not of the particular basis you chose. R³ has dimension 3; any plane through the origin has dimension 2; any line through the origin has dimension 1; the zero subspace has dimension 0. Dimension captures the "degrees of freedom" in a subspace and will govern nearly every theorem you encounter from here: the rank-nullity theorem, the invertibility of matrices, the structure of solutions to linear systems.
