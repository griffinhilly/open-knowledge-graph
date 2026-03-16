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

## Explainer

The **transpose** operation is deceptively simple in definition but surprisingly rich in consequences. You already know how to add and multiply matrices; the transpose adds a third fundamental operation — reflecting a matrix across its main diagonal. Concretely, if A has entry aᵢⱼ at row i, column j, then Aᵀ has that same value at row j, column i. An m×n matrix becomes n×m. A column vector (n×1) becomes a row vector (1×n). This is the geometric intuition: you are swapping the roles of rows and columns.

The property (Aᵀ)ᵀ = A is immediate — reflecting twice returns to the original. More interesting is what happens with sums: (A + B)ᵀ = Aᵀ + Bᵀ, which follows directly from the definition. The surprising rule is for products: **(AB)ᵀ = BᵀAᵀ**, with the order reversed. Why does order reverse? Think about dimensions: if A is m×n and B is n×p, then AB is m×p, and (AB)ᵀ is p×m. Meanwhile Bᵀ is p×n and Aᵀ is n×m, so BᵀAᵀ is also p×m — the only possible order that makes the dimensions compatible. A concrete 2×2 verification will build more intuition than any abstract argument; multiply out both sides and confirm they match.

The transpose connects naturally to two concepts you will meet shortly. First, a matrix is called **symmetric** if Aᵀ = A, meaning it is unchanged by reflection — entries mirror across the diagonal. Symmetric matrices appear everywhere in applied mathematics (covariance matrices, the Hessian in optimization, the Laplacian in physics). Second, the dot product of two column vectors u and v can be written as uᵀv — the row vector uᵀ times the column vector v produces a 1×1 matrix, which is just the scalar dot product. This notation bridges linear algebra and calculus cleanly.

For invertible matrices, (A⁻¹)ᵀ = (Aᵀ)⁻¹. You can verify this: multiply Aᵀ by (A⁻¹)ᵀ and use the product reversal rule — you get (A⁻¹A)ᵀ = Iᵀ = I. This fact matters in least squares and in understanding **orthogonal matrices**, where Aᵀ = A⁻¹, meaning the transpose is so structured that it perfectly undoes the transformation A performs.
