---
id: matrix-transpose-properties
title: Matrix Transpose and Its Properties
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrix-operations
  type: hard
builds-toward:
- symmetric-matrices
- row-space
- inner-product-spaces
- least-squares-approximation
tags:
- transpose
- symmetric
- AT
- properties of transpose
stage: formal-systems
status: validated
---

# Matrix Transpose and Its Properties

## Core Idea
The transpose of an m×n matrix A, written Aᵀ, is the n×m matrix formed by reflecting entries across the main diagonal so that the (i,j) entry of Aᵀ equals the (j,i) entry of A. Key algebraic properties include (Aᵀ)ᵀ = A, (AB)ᵀ = BᵀAᵀ (note the reversal of order), and (A⁻¹)ᵀ = (Aᵀ)⁻¹ for invertible A. The transpose converts column vectors to row vectors and vice versa. It appears throughout linear algebra in dot product formulas, in defining symmetric matrices, and in the normal equations for least squares.

## How It's Best Learned
Practice computing transposes of various matrix sizes. Pay special attention to the product reversal rule (AB)ᵀ = BᵀAᵀ, which surprises many students. Verify properties numerically on small matrices before using them symbolically.

## Common Misconceptions
- Students often write (AB)ᵀ = AᵀBᵀ, forgetting the reversal of order.
- Transposing a square matrix does not change its determinant or eigenvalues (though eigenvectors may differ).
- Row vectors and column vectors are technically transposes of each other, not the same object.
