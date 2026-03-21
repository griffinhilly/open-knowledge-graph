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

## Questions

```yaml
- question: "Let A be a 3×2 matrix and B be a 2×4 matrix. A student claims (AB)ᵀ = AᵀBᵀ. What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — (AB)ᵀ = AᵀBᵀ is a valid identity"
    - "The dimensions don't work: Aᵀ is 2×3 and Bᵀ is 4×2, so AᵀBᵀ requires a 3×4 inner product that doesn't exist"
    - "The identity holds only when A and B are square"
    - "The transpose distributes over products only when the result is symmetric"
  answer: 1
  explanation: "Aᵀ is 2×3 and Bᵀ is 4×2, so forming AᵀBᵀ requires multiplying a 2×3 matrix by a 4×2 matrix — the inner dimensions (3 and 4) don't match. The correct identity (AB)ᵀ = BᵀAᵀ reverses the order: Bᵀ is 4×2 and Aᵀ is 2×3, giving a valid 4×3 product, which matches the shape of (AB)ᵀ. The dimension check is the clearest way to remember why the order must reverse."

- question: "A square matrix A has eigenvalue λ. Which of the following is guaranteed about the eigenvalues of Aᵀ?"
  type: multiple-choice
  options:
    - "Aᵀ has eigenvalue λ only if A is symmetric"
    - "Aᵀ always has eigenvalue λ, because A and Aᵀ share the same characteristic polynomial"
    - "Aᵀ has eigenvalue 1/λ, because transposing inverts eigenvalues"
    - "Aᵀ has eigenvalue λ only when λ is real"
  answer: 1
  explanation: "A and Aᵀ have identical characteristic polynomials: det(A − λI) = det((A − λI)ᵀ) = det(Aᵀ − λI). So they always share the same eigenvalues, regardless of whether A is symmetric or λ is real. This surprises students who know that eigenvectors can differ under transposition — the eigenvalues are preserved even when the eigenvectors are not."

- question: "Transposing a square matrix always changes its determinant."
  type: true-false
  answer: false
  explanation: "det(Aᵀ) = det(A) for any square matrix. This follows from the fact that the determinant formula involves the same set of products regardless of whether you expand along rows or columns — transposing swaps the roles of rows and columns, but the scalar value of the determinant is unchanged. A common error is conflating 'the matrix changed' with 'its scalar properties changed.'"

- question: "For any matrix A (not necessarily square), the product AᵀA is always a symmetric matrix."
  type: true-false
  answer: true
  explanation: "Applying the reversal rule: (AᵀA)ᵀ = Aᵀ(Aᵀ)ᵀ = AᵀA. So AᵀA equals its own transpose, making it symmetric by definition. This is a non-obvious consequence of the reversal rule and is practically important: AᵀA appears in the normal equations for least squares regression and is always symmetric (and positive semi-definite)."

- question: "Why does the product reversal rule (AB)ᵀ = BᵀAᵀ require the order to reverse? Give a dimensional argument."
  type: short-answer
  answer: "If A is m×n and B is n×p, then AB is m×p and (AB)ᵀ is p×m. Now Bᵀ is p×n and Aᵀ is n×m, so BᵀAᵀ is p×m — which matches. But AᵀBᵀ would multiply an n×m matrix by a p×n matrix; the inner dimensions m and p need not be equal, so AᵀBᵀ is generally undefined. The reversal is dimensionally forced."
  explanation: "The same reversal appears elsewhere: (AB)⁻¹ = B⁻¹A⁻¹ for invertible matrices, and the pattern generalizes — (ABC)ᵀ = CᵀBᵀAᵀ. Think of it like putting on gloves: right glove first, then left glove; to remove them you reverse the order. Any operation that 'distributes' over matrix products must reverse the order to preserve dimensional compatibility."
```

## Explainer

The **transpose** operation is deceptively simple in definition but surprisingly rich in consequences. You already know how to add and multiply matrices; the transpose adds a third fundamental operation — reflecting a matrix across its main diagonal. Concretely, if A has entry aᵢⱼ at row i, column j, then Aᵀ has that same value at row j, column i. An m×n matrix becomes n×m. A column vector (n×1) becomes a row vector (1×n). This is the geometric intuition: you are swapping the roles of rows and columns.

The property (Aᵀ)ᵀ = A is immediate — reflecting twice returns to the original. More interesting is what happens with sums: (A + B)ᵀ = Aᵀ + Bᵀ, which follows directly from the definition. The surprising rule is for products: **(AB)ᵀ = BᵀAᵀ**, with the order reversed. Why does order reverse? Think about dimensions: if A is m×n and B is n×p, then AB is m×p, and (AB)ᵀ is p×m. Meanwhile Bᵀ is p×n and Aᵀ is n×m, so BᵀAᵀ is also p×m — the only possible order that makes the dimensions compatible. A concrete 2×2 verification will build more intuition than any abstract argument; multiply out both sides and confirm they match.

The transpose connects naturally to two concepts you will meet shortly. First, a matrix is called **symmetric** if Aᵀ = A, meaning it is unchanged by reflection — entries mirror across the diagonal. Symmetric matrices appear everywhere in applied mathematics (covariance matrices, the Hessian in optimization, the Laplacian in physics). Second, the dot product of two column vectors u and v can be written as uᵀv — the row vector uᵀ times the column vector v produces a 1×1 matrix, which is just the scalar dot product. This notation bridges linear algebra and calculus cleanly.

For invertible matrices, (A⁻¹)ᵀ = (Aᵀ)⁻¹. You can verify this: multiply Aᵀ by (A⁻¹)ᵀ and use the product reversal rule — you get (A⁻¹A)ᵀ = Iᵀ = I. This fact matters in least squares and in understanding **orthogonal matrices**, where Aᵀ = A⁻¹, meaning the transpose is so structured that it perfectly undoes the transformation A performs.
