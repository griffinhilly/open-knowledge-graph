---
id: linear-independence
title: Linear Independence and Linear Dependence
domain: mathematics
course: linear-algebra
prerequisites:
- id: vector-spaces
  type: hard
- id: scalar-multiplication
  type: hard
builds-toward:
- basis-definition
- span-and-basis
tags:
- linear independence
- dependence
- vectors
stage: formal-systems
status: validated
---

# Linear Independence and Linear Dependence

## Core Idea
Vectors v₁, ..., vₖ are linearly independent if c₁v₁ + ... + cₖvₖ = 0 implies all c_i = 0. They are linearly dependent if a non-trivial combination equals zero. Independence means no vector is a combination of others. For matrices: columns are independent iff rank equals the number of columns.

## Questions

```yaml
- question: "You have three vectors in ℝ² (the 2D plane). Can they be linearly independent?"
  type: multiple-choice
  options:
    - "Yes, as long as no two of the three vectors are parallel to each other"
    - "Yes, provided all three vectors are nonzero"
    - "No — any set of three vectors in ℝ² must be linearly dependent"
    - "Only if all three vectors are mutually orthogonal"
  answer: 2
  explanation: "ℝ² is 2-dimensional, meaning at most 2 linearly independent vectors can exist in it. A third vector must lie in the plane spanned by the first two — it is always expressible as a linear combination of them. This is a fundamental constraint: you cannot have more linearly independent vectors than the dimension of the space. The options about 'not parallel' or 'nonzero' represent common misconceptions — independence is about dimensional redundancy, not just pairwise geometric distinctness."

- question: "For vectors v₁, v₂, v₃, suppose the equation c₁v₁ + c₂v₂ + c₃v₃ = 0 has the solution c₁ = 2, c₂ = −1, c₃ = 1. What can you conclude?"
  type: multiple-choice
  options:
    - "The vectors are linearly independent, because the coefficients are not all equal"
    - "The vectors are linearly dependent, because a nontrivial combination equals zero"
    - "We need to know whether the vectors are in ℝ² or ℝ³ before concluding anything"
    - "The vectors are orthogonal, since combining them in this way yields zero"
  answer: 1
  explanation: "Linear independence requires that the only solution to c₁v₁ + c₂v₂ + c₃v₃ = 0 is the trivial solution (all cᵢ = 0). Here we have a nontrivial solution — at least one coefficient is nonzero (c₁ = 2). This immediately establishes linear dependence. From c₁ = 2 ≠ 0, we can solve: v₁ = (1/2)v₂ − (1/2)v₃, showing v₁ is redundant. The dimension of the space is irrelevant to this conclusion; what matters is whether a nontrivial combination can be zero."

- question: "The zero vector cannot be a member of a linearly independent set, even if all other vectors in the set are nonzero."
  type: true-false
  answer: true
  explanation: "If the zero vector 0 is in a set {0, v₂, ..., vₖ}, then the equation 1·0 + 0·v₂ + ··· + 0·vₖ = 0 is a nontrivial solution (the coefficient of 0 is 1, not 0). This violates the definition of linear independence, which requires that the only solution be all-zero coefficients. The zero vector is always redundant: you can 'zero it out' with a nonzero coefficient while leaving the rest unchanged."

- question: "If a set of vectors is linearly dependent, then at least one of them can be written as a linear combination of the others."
  type: true-false
  answer: true
  explanation: "This is exactly what dependence means in practice. If there is a nontrivial combination c₁v₁ + ··· + cₖvₖ = 0 with some cᵢ ≠ 0, then vᵢ = −(c₁/cᵢ)v₁ − ··· (omitting vᵢ) — it is reachable from the others by scaling and adding. Linear independence means no vector can be reached this way; linear dependence means at least one can. This is the geometric content of the algebraic definition: dependence equals redundancy."

- question: "Why does the definition of linear independence use the algebraic condition 'c₁v₁ + ⋯ + cₖvₖ = 0 implies all cᵢ = 0' rather than a simpler geometric condition like 'no two vectors point in the same direction'?"
  type: short-answer
  answer: "The geometric condition 'no two vectors are parallel' only catches pairwise collinearity — it misses the case where three or more vectors are dependent even though no two of them are parallel. For example, in ℝ², the vectors (1,0), (0,1), and (1,1) have no two pairs that are parallel, yet they are linearly dependent because (1,1) = 1·(1,0) + 1·(0,1). The algebraic definition captures all forms of redundancy simultaneously: any vector expressible as a combination of the others will produce a nontrivial solution to the zero-combination equation. The algebraic condition is both necessary and sufficient; the pairwise geometric condition is neither."
  explanation: "Geometric intuition about 'direction' breaks down in higher dimensions and for more than two vectors. The algebraic definition is universal — it applies in any vector space of any dimension, including abstract ones where 'direction' has no geometric meaning."
```

## Explainer

Start with what you already know about vector spaces: they are sets closed under addition and scalar multiplication, and every element can be "moved around" by scaling. **Linear independence** asks a sharp question about a collection of vectors: is any one of them redundant? A vector is redundant if it can be written as a combination of the others — meaning it adds no new "direction" to the collection. Linear independence is exactly the property that none of them is redundant.

The formal definition encodes this idea elegantly. Write the equation c₁v₁ + c₂v₂ + ··· + cₖvₖ = 0 and ask: does it have a solution other than all cᵢ = 0? The trivial solution (all coefficients zero) always works, because the zero vector is always 0. If that is the *only* solution, the vectors are **linearly independent** — the only way to combine them to zero is to use nothing. If there is a nontrivial solution, say c₁ ≠ 0, you can solve: v₁ = −(c₂/c₁)v₂ − ··· − (cₖ/c₁)vₖ, showing v₁ is a combination of the others. That is **linear dependence**.

Geometrically, this is about dimension. Two vectors in the plane are linearly independent if they point in genuinely different directions — not just scaled versions of each other. Three vectors in 3D space are independent if none lies in the plane spanned by the other two. Dependence occurs whenever you have "too many" vectors relative to the space's dimension: three vectors in a plane must be dependent, because the plane is only two-dimensional. The connection to your prerequisite on scalar multiplication is direct: dependence always reduces to one vector being reachable from others by combinations of scaling and adding.

For matrices, the condition translates cleanly. The columns of an m × n matrix A are linearly independent if and only if the equation Ax = 0 has only the trivial solution x = 0 — meaning the kernel (null space) is just {0}. Equivalently, the rank of A equals n: all n columns are "active" in the sense that no column is a shadow of the others. This connection to rank makes independence testable by Gaussian elimination, which is how you will compute it in practice.
