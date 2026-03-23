---
id: singular-value-decomposition
title: Singular Value Decomposition (SVD)
domain: mathematics
course: linear-algebra
prerequisites:
- id: symmetric-matrices-properties
  type: hard
builds-toward:
- least-squares-approximation
- matrix-norms-conditioning
tags:
- SVD
- singular-values
- decomposition
stage: formal-systems
status: validated
---

# Singular Value Decomposition (SVD)

## Core Idea
Every m×n matrix A can be written as A = UΣVᵀ where U and V are orthogonal and Σ is diagonal with singular values σ₁ ≥ σ₂ ≥ ... ≥ 0. Singular values are square roots of eigenvalues of AᵀA or AAᵀ. SVD reveals the rank, condition number, and principal directions of A. It is the most general and numerically stable decomposition.

## Questions

```yaml
- question: "A 1000×500 matrix A has 50 nonzero singular values, the rest being zero. What does this immediately tell you about A?"
  type: multiple-choice
  options:
    - "A is invertible, since it has more rows than columns"
    - "A has rank 50 — it maps its 500-dimensional input space into a 50-dimensional subspace"
    - "A is numerically unstable because its condition number is 500/50 = 10"
    - "A can only be decomposed if it is first converted to a square matrix"
  answer: 1
  explanation: "The rank of a matrix equals the number of nonzero singular values. So this matrix, despite having 500 columns, only has rank 50 — its column space is 50-dimensional, not 500-dimensional. The other 450 dimensions are in the null space. Option A is wrong because a 1000×500 matrix cannot be square-invertible regardless of rank. Option C confuses condition number (σ₁/σₙ, not total/nonzero count). Option D is wrong — SVD works for any matrix without modification."

- question: "You want the best rank-3 approximation to a 100×100 image matrix A. SVD gives you singular values σ₁ ≥ σ₂ ≥ ... ≥ σ₁₀₀. Which approximation is mathematically optimal?"
  type: multiple-choice
  options:
    - "A₃ = σ₁u₁v₁ᵀ + σ₂u₂v₂ᵀ + σ₃u₃v₃ᵀ, using the three largest singular values"
    - "A₃ = σ₉₈u₉₈v₉₈ᵀ + σ₉₉u₉₉v₉₉ᵀ + σ₁₀₀u₁₀₀v₁₀₀ᵀ, using the three smallest singular values"
    - "The average of all rank-1 terms: (1/100)∑σᵢuᵢvᵢᵀ"
    - "The choice depends on the application — SVD does not define a canonical best approximation"
  answer: 0
  explanation: "Keeping the k largest singular values and their corresponding outer products gives the best rank-k approximation to A in both the Frobenius and spectral norms — this is the Eckart–Young theorem. The largest singular values correspond to the directions of greatest variance in A; discarding the small ones loses the least information. This is the mathematical foundation of PCA, image compression, and recommender systems — you keep the 'big pieces' and throw away noise."

- question: "SVD can be applied to any matrix — rectangular or square, symmetric or not — whereas eigendecomposition requires a square matrix."
  type: true-false
  answer: true
  explanation: "This is SVD's key advantage over eigendecomposition. Eigendecomposition A = PΛP⁻¹ requires A to be square and, for a real orthogonal factorization, symmetric. SVD A = UΣVᵀ works for any m×n matrix: U is m×m orthogonal, Σ is m×n diagonal with nonneg entries, Vᵀ is n×n orthogonal. This generality — combined with numerical stability — is why SVD is the decomposition of choice in applications like least squares, PCA, and pseudoinverse computation."

- question: "The singular values of a matrix A are the same as the eigenvalues of A."
  type: true-false
  answer: false
  explanation: "Singular values and eigenvalues are related but distinct. Singular values σᵢ are the square roots of the eigenvalues of AᵀA (or AAᵀ), which are always nonneg. Eigenvalues of A itself can be negative, complex, or zero in ways unrelated to singular values. For a symmetric positive definite matrix, singular values and eigenvalues coincide — but in general they differ. Confusing the two leads to errors when assessing numerical stability (condition number uses singular values, not eigenvalues)."

- question: "Why is SVD described geometrically as 'rotation, then scaling, then rotation,' and why does this interpretation matter?"
  type: short-answer
  answer: "Any linear map A = UΣVᵀ can be decomposed as: Vᵀ rotates the input, Σ stretches or shrinks along each axis (axis-aligned scaling), and U rotates the output. This matters because it means every linear transformation — no matter how complex — is secretly just these three operations. The singular values (the scaling factors) reveal how much the map amplifies each direction, which tells you the rank (how many directions have nonzero scaling), the condition number (ratio of largest to smallest nonzero scaling), and which directions to keep for a low-rank approximation."
  explanation: "The geometric decomposition makes SVD interpretable rather than just computational. It explains why the best rank-k approximation keeps the k largest singular values — those are the k directions in which A 'stretches most,' carrying the most information. And it generalizes the eigendecomposition's 'rotate-scale-unrotate' story to non-symmetric and rectangular matrices by allowing the two rotations to be different."
```

## Explainer

Start from what you know about symmetric matrices. From your prerequisite work, you know that symmetric matrices A have a special eigendecomposition: A = QΛQᵀ, where Q is orthogonal (Qᵀ = Q⁻¹) and Λ is diagonal. This says every symmetric matrix is "rotation, scale, rotate back" using the same rotation twice. **Singular value decomposition** generalizes this idea to *any* matrix — rectangular or square, symmetric or not — by allowing two different orthogonal matrices.

The SVD writes A = UΣVᵀ. The interpretation is geometric: Vᵀ is a rotation in the input space, Σ stretches or shrinks along each axis (with no rotation), and U is a rotation in the output space. So any linear map, however complicated, is secretly just a rotation, then an axis-aligned scaling, then another rotation. The **singular values** σ₁ ≥ σ₂ ≥ ... ≥ 0 are those scaling factors. To find them, form AᵀA (which is always symmetric and positive semidefinite); its eigenvalues are σᵢ², and their square roots are the singular values.

The singular values reveal the structure of A. The **rank** of A equals the number of nonzero singular values. The **condition number** σ₁/σₙ measures how numerically stable A is — a large ratio means small input errors produce large output errors. If you truncate the SVD by keeping only the largest k singular values (set the rest to zero), you get the best rank-k approximation to A in a precise sense — this is the mathematical foundation of dimensionality reduction in data science.

There is also a beautiful outer product decomposition: A = σ₁u₁v₁ᵀ + σ₂u₂v₂ᵀ + ... Each term is a rank-1 matrix (one column of U times one row of Vᵀ), scaled by a singular value. The first term captures the "most important" direction, the second the next, and so on. This is why SVD underlies principal component analysis, image compression, and recommender systems — you can keep the big pieces and discard the small ones, approximating complex data with a compact description.

Unlike eigendecomposition, SVD works for *any* matrix, making it the most broadly applicable decomposition in numerical linear algebra. When floating-point stability matters or when the matrix is not square or symmetric, SVD is the tool of choice. The price is computational cost, but the payoff is a decomposition that is geometrically interpretable, numerically stable, and directly informative about rank, approximability, and the structure of linear maps.
