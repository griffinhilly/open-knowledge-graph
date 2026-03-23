---
id: rank-nullity-theorem
title: Rank-Nullity Theorem
domain: mathematics
course: linear-algebra
prerequisites:
- id: kernel-image-rank
  type: hard
- id: dimension-vector-space
  type: hard
tags:
- rank-nullity
- dimensions
- linear transformations
stage: formal-systems
status: validated
---

# Rank-Nullity Theorem

## Core Idea
For a linear transformation T: V → W with V finite-dimensional: dim(V) = rank(T) + nullity(T), where rank(T) = dim(im(T)) and nullity(T) = dim(ker(T)). For an m × n matrix A: rank(A) + nullity(A) = n. This fundamental relation connects the sizes of key subspaces.

## Questions

```yaml
- question: "A linear map T: ℝ⁶ → ℝ⁴ has rank 3. What is the nullity of T?"
  type: multiple-choice
  options:
    - "1"
    - "3"
    - "4"
    - "7"
  answer: 1
  explanation: "The rank-nullity theorem says rank(T) + nullity(T) = dim(domain) = 6. With rank 3, nullity = 6 − 3 = 3. A common error is subtracting from the codomain dimension (4 − 3 = 1), but the theorem accounts for the *input* space, not the output space. The codomain dimension is irrelevant here — what matters is how the 6-dimensional input is divided between what gets erased (kernel) and what survives (image)."

- question: "A linear transformation T: ℝ⁴ → ℝ⁶ is injective (one-to-one). What must be true about its rank and nullity?"
  type: multiple-choice
  options:
    - "Rank 6 and nullity 0 — the map fills the codomain"
    - "Rank 4 and nullity 0 — the map is injective exactly when the kernel is trivial"
    - "Rank 4 and nullity 2 — some dimensions are lost in the larger codomain"
    - "T cannot be injective because the codomain has higher dimension than the domain"
  answer: 1
  explanation: "Injectivity means no two distinct inputs map to the same output, which is equivalent to the kernel being trivial (nullity = 0). By rank-nullity: rank = 4 − 0 = 4. The image has dimension 4, which sits inside ℝ⁶ — the map can be injective even though it doesn't fill the codomain (that would require surjectivity, which would need rank 6, impossible here). The common confusion is conflating injectivity with surjectivity."

- question: "If a linear map T: ℝ⁵ → ℝ³ has rank 3, then T is surjective (onto)."
  type: true-false
  answer: true
  explanation: "Surjectivity means the image equals the entire codomain. Here the codomain is ℝ³, dimension 3. If rank(T) = 3 = dim(ℝ³), the image spans the entire codomain — T is surjective. By rank-nullity, nullity = 5 − 3 = 2, meaning a 2-dimensional subspace of ℝ⁵ is collapsed to zero, but the remaining 3 dimensions map onto all of ℝ³."

- question: "A linear map T: ℝ³ → ℝ⁵ can be both injective and surjective."
  type: true-false
  answer: false
  explanation: "For T to be bijective (both injective and surjective), it would need rank equal to both dim(domain) = 3 and dim(codomain) = 5 simultaneously — impossible. Surjectivity requires rank = 5, but rank-nullity says rank ≤ dim(domain) = 3. So T can be at most injective (rank 3, nullity 0), but it cannot be surjective. A bijection between finite-dimensional spaces requires equal dimensions."

- question: "In your own words, explain what the rank-nullity theorem says about where the dimensions of a linear map's input space 'go.'"
  type: short-answer
  answer: "The theorem says the input dimension is completely accounted for by two subspaces: the kernel (vectors that get 'erased' — mapped to zero) and the image (vectors that 'survive' — produce distinct nonzero outputs). Their dimensions sum exactly to the input dimension. Nothing is counted twice, and nothing is missed. It is a conservation law for dimension."
  explanation: "The intuition of 'erased vs. survived' is what makes the theorem memorable and useful. Every dimension of the input either gets crushed into the kernel or contributes a dimension to the image. This directly constrains what is possible: a map from a large space to a small one must have a nontrivial kernel (some information is always lost), and a map from a small space to a large one cannot fill the codomain (some output directions are unreachable)."
```

## Explainer

From your prerequisites, you know that a linear transformation T: V → W has two fundamental subspaces: the **kernel** (or null space) ker(T), which consists of all vectors that T sends to zero, and the **image** im(T), which consists of all outputs T can produce. The rank-nullity theorem says these two subspaces account for all of V together: their dimensions sum exactly to dim(V).

Think of T as sorting the input space V into two populations. One population — the kernel — gets "erased" by T, collapsing to the zero vector. The other population carries information forward into the image. The theorem says the total dimension of V is just the size of what gets erased (nullity) plus the size of what survives (rank). Nothing is counted twice, and nothing is missed. This is a conservation law for dimension.

For a concrete example, take a linear map T: ℝ⁵ → ℝ³ represented by a 3 × 5 matrix. The input space has dimension 5. Suppose T has rank 3 — its image fills all of ℝ³. Then the rank-nullity theorem tells you immediately that nullity = 5 − 3 = 2: there is a 2-dimensional subspace of ℝ⁵ that T crushes to zero. You can verify this by row-reducing the matrix and finding the free variables. Each free variable corresponds to a dimension in the kernel. The count always works out.

A useful consequence is that T can never be injective (one-to-one) if the domain has higher dimension than the codomain — the kernel must be nontrivial, so distinct inputs must collide. Conversely, T can never be surjective (onto) if the codomain has higher dimension than the domain — the image can't have dimension exceeding dim(V). The rank-nullity theorem thus immediately constrains which linear maps can be injective, surjective, or bijective, making it one of the most used tools in linear algebra for reasoning about solvability of linear systems.
