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
status: draft
---

# Singular Value Decomposition (SVD)

## Core Idea
Every m×n matrix A can be written as A = UΣVᵀ where U and V are orthogonal and Σ is diagonal with singular values σ₁ ≥ σ₂ ≥ ... ≥ 0. Singular values are square roots of eigenvalues of AᵀA or AAᵀ. SVD reveals the rank, condition number, and principal directions of A. It is the most general and numerically stable decomposition.

## Explainer

Start from what you know about symmetric matrices. From your prerequisite work, you know that symmetric matrices A have a special eigendecomposition: A = QΛQᵀ, where Q is orthogonal (Qᵀ = Q⁻¹) and Λ is diagonal. This says every symmetric matrix is "rotation, scale, rotate back" using the same rotation twice. **Singular value decomposition** generalizes this idea to *any* matrix — rectangular or square, symmetric or not — by allowing two different orthogonal matrices.

The SVD writes A = UΣVᵀ. The interpretation is geometric: Vᵀ is a rotation in the input space, Σ stretches or shrinks along each axis (with no rotation), and U is a rotation in the output space. So any linear map, however complicated, is secretly just a rotation, then an axis-aligned scaling, then another rotation. The **singular values** σ₁ ≥ σ₂ ≥ ... ≥ 0 are those scaling factors. To find them, form AᵀA (which is always symmetric and positive semidefinite); its eigenvalues are σᵢ², and their square roots are the singular values.

The singular values reveal the structure of A. The **rank** of A equals the number of nonzero singular values. The **condition number** σ₁/σₙ measures how numerically stable A is — a large ratio means small input errors produce large output errors. If you truncate the SVD by keeping only the largest k singular values (set the rest to zero), you get the best rank-k approximation to A in a precise sense — this is the mathematical foundation of dimensionality reduction in data science.

There is also a beautiful outer product decomposition: A = σ₁u₁v₁ᵀ + σ₂u₂v₂ᵀ + ... Each term is a rank-1 matrix (one column of U times one row of Vᵀ), scaled by a singular value. The first term captures the "most important" direction, the second the next, and so on. This is why SVD underlies principal component analysis, image compression, and recommender systems — you can keep the big pieces and discard the small ones, approximating complex data with a compact description.

Unlike eigendecomposition, SVD works for *any* matrix, making it the most broadly applicable decomposition in numerical linear algebra. When floating-point stability matters or when the matrix is not square or symmetric, SVD is the tool of choice. The price is computational cost, but the payoff is a decomposition that is geometrically interpretable, numerically stable, and directly informative about rank, approximability, and the structure of linear maps.
