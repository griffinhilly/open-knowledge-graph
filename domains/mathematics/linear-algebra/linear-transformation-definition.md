---
id: linear-transformation-definition
title: Linear Transformations and Properties
domain: mathematics
course: linear-algebra
prerequisites:
- id: vector-spaces-definition
  type: hard
builds-toward:
- matrix-representation-linear-map
- kernel-image-rank
tags:
- transformations
- linear maps
- properties
stage: formal-systems
status: draft
---

# Linear Transformations and Properties

## Core Idea
A function T: V → W between vector spaces is linear if T(u + v) = T(u) + T(v) and T(cu) = cT(u) for all vectors u, v and scalar c. Linear transformations preserve vector space structure and can be represented by matrices once bases are chosen. Kernel and image are fundamental subspaces of any linear map.

## Questions

```yaml
- question: "A function T: ℝ² → ℝ² is defined by T(x, y) = (x + 3, y + 3), shifting every vector by the constant (3, 3). Is T a linear transformation?"
  type: multiple-choice
  options:
    - "Yes, because every input maps to a unique output"
    - "Yes, because the rule is simple and well-defined"
    - "No, because T(0, 0) = (3, 3) ≠ (0, 0), violating the requirement that a linear map sends zero to zero"
    - "No, because linear transformations only work on one-dimensional spaces"
  answer: 2
  explanation: "A linear transformation must satisfy T(u + v) = T(u) + T(v) and T(cu) = cT(u). A quick necessary check is that T must send the zero vector to zero: T(0) = T(c·0) = cT(0) forces T(0) = 0. Here T(0,0) = (3,3) ≠ (0,0), so T cannot be linear — no further checking is needed. Translation (adding a fixed nonzero vector) is one of the most common non-linear operations that students mistakenly call linear, because it looks like simple arithmetic."

- question: "Why does knowing what a linear transformation T does to a basis {e₁, e₂, …, eₙ} of V completely determine T on all of V?"
  type: multiple-choice
  options:
    - "Because basis vectors are the only inputs that matter for most applications"
    - "Because any vector v in V can be written as a linear combination of basis vectors, and linearity forces T(v) to equal the same linear combination of T(e₁), …, T(eₙ)"
    - "Because the basis spans V, so T only needs to be defined on a representative subset"
    - "Because T is continuous and continuous functions are determined by their values on a dense set"
  answer: 1
  explanation: "If v = c₁e₁ + … + cₙeₙ, then T(v) = c₁T(e₁) + … + cₙT(eₙ) by linearity. This means T is completely determined by the images of the basis vectors — there is no freedom left once you fix T(e₁), …, T(eₙ). This is why linear transformations can be encoded as matrices: the columns are exactly the images of the basis vectors. A matrix is a lookup table for the transformation in a given coordinate system."

- question: "Rotation of every vector in ℝ² by a fixed angle θ is a linear transformation."
  type: true-false
  answer: true
  explanation: "True. Rotation satisfies both linearity conditions. Rotating the sum of two vectors gives the same result as rotating each separately and adding: R(u + v) = R(u) + R(v). Scaling then rotating gives the same result as rotating then scaling: R(cu) = cR(u). Crucially, R(0) = 0 — rotation sends the origin to itself. Geometrically, rotation preserves the vector space structure: it can be represented by a 2×2 matrix and is the canonical example of a linear transformation."

- question: "A function satisfying T(u + v) = T(u) + T(v) for all vectors u and v is guaranteed to be a linear transformation."
  type: true-false
  answer: false
  explanation: "False. A linear transformation requires both T(u + v) = T(u) + T(v) (additivity) AND T(cu) = cT(u) (homogeneity). A function satisfying only additivity is called an additive function. Pathological additive functions that fail homogeneity exist (they require the Axiom of Choice to construct and are not continuous). Both conditions together characterize linear transformations, which is why the definition lists them both explicitly."

- question: "Explain what it means for a function T to be a linear transformation, and why a translation T(v) = v + b (where b ≠ 0) fails to qualify."
  type: short-answer
  answer: "A function T: V → W is linear if it preserves the two vector space operations: T(u + v) = T(u) + T(v) (it commutes with addition) and T(cv) = cT(v) (it commutes with scalar multiplication). A translation T(v) = v + b fails both conditions. Most directly: T(0) = b ≠ 0, but any linear map must send 0 to 0, since T(0) = T(0·v) = 0·T(v) = 0. Also T(u + v) = u + v + b, while T(u) + T(v) = u + b + v + b = u + v + 2b ≠ u + v + b. The translation shifts the origin, destroying the algebraic structure that linearity requires."
  explanation: "The intuition is that linear transformations preserve the vector space's structure — they can rotate, reflect, scale, and shear, but they cannot shift the origin. Translations treat the zero vector differently from all others, violating the fundamental symmetry that linearity requires. This distinction matters enormously: affine transformations (linear plus translation) require a different mathematical treatment than purely linear ones."
```

## Explainer

From your study of vector spaces, you know that a vector space is defined by two operations — addition and scalar multiplication — together with a list of axioms that make them behave predictably. A **linear transformation** is a function between two vector spaces that respects exactly those two operations. When you apply T to a sum, you get the same result as summing the outputs: T(u + v) = T(u) + T(v). When you scale an input first, the output scales by the same factor: T(cu) = cT(u). These two conditions together mean T doesn't distort the underlying algebraic structure — it carries vectors over to the new space in a way that honors how those spaces work.

A useful way to build intuition is through geometry. Consider the transformation T: ℝ² → ℝ² that rotates every vector by 45 degrees. If you rotate u + v, you get the same result as rotating u and v separately and adding them. Scaling a vector then rotating gives the same result as rotating then scaling. Rotation is linear. Now consider a translation — shifting every vector by adding a fixed constant vector b: T(v) = v + b. This fails linearity because T(0) = b ≠ 0; a linear map must always send the zero vector to the zero vector. That's a useful first check: if T doesn't map 0 to 0, it cannot be linear.

The power of linearity is that knowing what T does to a **basis** is enough to determine T completely. If {e₁, e₂, …, eₙ} is a basis for V, then any vector v in V can be written as a linear combination of basis vectors, and linearity forces T(v) to be the corresponding linear combination of T(e₁), T(e₂), …, T(eₙ). This is why linear transformations can be encoded as **matrices**: each column of the matrix is the image of the corresponding basis vector. The matrix is the lookup table for the transformation in those coordinates.

Two subspaces tell you the most important structural facts about T. The **kernel** (or null space) is the set of all inputs that T sends to zero — it measures how "far from injective" T is. If the kernel is just {0}, then T is one-to-one; every input maps to a distinct output. The **image** (or range) is the set of all possible outputs — it measures how much of W the transformation actually covers. The Rank-Nullity theorem, which you'll prove soon, gives the precise relationship between the sizes of these two subspaces: dim(kernel) + dim(image) = dim(V). Understanding a linear transformation means understanding its kernel and image.
