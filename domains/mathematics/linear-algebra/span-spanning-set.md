---
id: span-spanning-set
title: Span and Spanning Sets
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-independence
  type: hard
builds-toward:
- basis-definition
- dimension-vector-space
tags:
- span
- spanning sets
- subspaces
stage: formal-systems
status: validated
---

# Span and Spanning Sets

## Core Idea
The span of vectors v₁, ..., vₖ is the set of all linear combinations c₁v₁ + ... + cₖvₖ. Span(v₁, ..., vₖ) is a subspace. A set spans a space V if every vector in V can be expressed as a combination. Spanning sets can be linearly dependent; bases are minimal spanning sets.

## Questions

```yaml
- question: "In ℝ², what is the span of the vectors (1, 2) and (2, 4)?"
  type: multiple-choice
  options:
    - "All of ℝ² — two vectors always span the plane when placed in the plane"
    - "A line through the origin — the vectors are linearly dependent and add no new reach"
    - "The zero vector only — the vectors cancel each other"
    - "A bounded parallelogram region defined by both vectors"
  answer: 1
  explanation: "The key misconception is that 'more vectors = larger span.' Here (2, 4) = 2(1, 2), so the second vector is a scalar multiple of the first — they are linearly dependent. Their span is the set of all c₁(1,2) + c₂(2,4) = (c₁ + 2c₂)(1,2), which is just all scalar multiples of (1,2): a line through the origin. Adding a redundant (dependent) vector adds no new reach to the span. Two linearly dependent vectors can only span a line, not the plane."

- question: "You have three vectors in ℝ³. Under what conditions do they span all of ℝ³?"
  type: multiple-choice
  options:
    - "Always — ℝ³ is three-dimensional and three vectors match the dimension"
    - "If and only if they are linearly independent"
    - "Only if one of the vectors is the zero vector"
    - "Whenever all three are nonzero, regardless of their directions"
  answer: 1
  explanation: "In ℝ³, three vectors span all of ℝ³ if and only if they are linearly independent (equivalently, the 3×3 matrix they form has nonzero determinant). If they are linearly dependent, their span is at most a plane (if two are independent) or a line (if all three are parallel). Three vectors in ℝ³ is the right *count* for a basis, but linear independence is the actual condition. Counting vectors without checking independence is the central error this concept addresses."

- question: "The span of any set of vectors is always a subspace of the ambient vector space."
  type: true-false
  answer: true
  explanation: "Span(v₁,...,vₖ) always satisfies the three subspace criteria: (1) it contains the zero vector (set all scalars to 0); (2) it is closed under addition (any sum of two linear combinations is itself a linear combination); (3) it is closed under scalar multiplication (scaling a linear combination gives another linear combination). In fact, the span is the *smallest* subspace containing all the given vectors — the intersection of all subspaces that contain them."

- question: "A spanning set for a vector space V must be linearly independent."
  type: true-false
  answer: false
  explanation: "A spanning set only requires that every vector in V can be expressed as a linear combination of the set — linear independence is not required. For example, {e₁, e₂, e₁ + e₂} spans ℝ² despite being linearly dependent (the third vector is the sum of the first two). A *basis* is a spanning set that is also linearly independent — it is the *minimal* spanning set. A spanning set may have redundant vectors without losing its spanning property."

- question: "What is the span of the zero vector {0} in ℝ³, and why does this result follow from the definition of span?"
  type: short-answer
  answer: "The span of {0} is just {0} — the set containing only the zero vector. By definition, span({0}) = {c·0 : c ∈ ℝ} = {0}. No matter what scalar you choose, c·0 = 0, so no other vector is reachable. This is consistent with the subspace requirement: {0} is itself a valid subspace (the smallest possible one). The zero vector has no direction and cannot 'reach' any nonzero vector through scaling or addition."
  explanation: "This edge case tests genuine understanding of span as 'all reachable vectors via scaling and adding,' rather than as a formula to apply mechanically. It also reinforces that the span always contains the zero vector — verified here directly from the definition."
```

## Explainer

You already understand linear independence: a set of vectors is independent if none of them can be written as a linear combination of the others — no vector is redundant. The concept of **span** asks a complementary question. Instead of asking "is any vector in this set built from the others?", span asks: "what can you build using these vectors as ingredients?" The span of {v₁, ..., vₖ} is every vector of the form c₁v₁ + c₂v₂ + ... + cₖvₖ, where the constants c₁, ..., cₖ range over all real numbers. It is the set of everything reachable by scaling and adding the given vectors.

Concrete examples make this vivid. In ℝ², the span of a single nonzero vector v is a line through the origin — you can reach any point on that line by scaling v, but nothing off it. The span of two linearly independent vectors in ℝ² is all of ℝ² — you can reach every point in the plane by choosing appropriate scalars. But if two vectors are parallel (linearly dependent), their span is still just a line, because the second vector adds no new reach. This illustrates the key insight: **more vectors in a set does not automatically mean a larger span** if the new vectors are already combinations of the old ones.

Span always produces a **subspace**: it contains the zero vector (take all scalars to be zero), it is closed under addition, and it is closed under scalar multiplication. This is not a coincidence — the span is the smallest subspace containing all the vectors in the set. Any subspace that contains v₁, ..., vₖ must contain all their linear combinations, so Span(v₁, ..., vₖ) is the intersection of all such subspaces.

A set of vectors **spans** a vector space V if Span(v₁, ..., vₖ) = V — meaning every vector in V is reachable. A spanning set can have redundancy: for instance, {e₁, e₂, e₁ + e₂} spans ℝ² even though three vectors are more than the minimum needed. A **basis** is a spanning set with no redundancy — it spans V and is linearly independent simultaneously. This is why bases are described as minimal spanning sets: remove any vector and you lose the ability to reach some part of the space. Span and linear independence are the two sides of the coin that define a basis, the topic you will encounter next.
