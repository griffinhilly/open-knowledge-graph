---
id: matrix-transpose
title: Matrix Transpose
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrices-definition
  type: hard
builds-toward:
- matrix-inverses
- determinant-properties
- eigenvalues-eigenvectors
tags:
- matrices
- transpose
- symmetric
stage: formal-systems
status: draft
---

# Matrix Transpose

## Core Idea
The transpose of A, denoted A^T, swaps rows and columns: (A^T)_ij = a_ji. Properties: (A^T)^T = A, (AB)^T = B^T A^T, (A + B)^T = A^T + B^T. A symmetric matrix satisfies A = A^T. The transpose is essential for defining adjoints and studying eigenvalues.

## Questions

```yaml
- question: "If A is a 3×4 matrix and B is a 4×2 matrix, what is the size of (AB)^T?"
  type: multiple-choice
  options:
    - "3×2"
    - "2×3"
    - "4×3"
    - "2×4"
  answer: 1
  explanation: "AB is a 3×2 matrix (3 rows of A times 2 columns of B). Transposing swaps rows and columns, so (AB)^T is 2×3. Confirming via the rule: (AB)^T = B^T A^T, where B^T is 2×4 and A^T is 4×3, giving a 2×3 product. The order-reversal in the product rule is essential — B^T A^T is defined and gives 2×3, while A^T B^T would require multiplying 4×3 by 2×4, which is not defined."

- question: "Which of the following statements about the transpose operation is FALSE?"
  type: multiple-choice
  options:
    - "(A^T)^T = A"
    - "(AB)^T = A^T B^T"
    - "(A + B)^T = A^T + B^T"
    - "If A = A^T, then A is called a symmetric matrix"
  answer: 1
  explanation: "Option B is false: (AB)^T = B^T A^T, not A^T B^T. The order must be reversed — this is one of the most important properties of the transpose and is analogous to the inverse rule (AB)^{-1} = B^{-1}A^{-1}. Options A, C, and D are all true: transposing twice returns the original, the transpose distributes over addition without reversing order, and A = A^T is precisely the definition of a symmetric matrix."

- question: "A symmetric matrix can be non-square (e.g., a 3×2 matrix can satisfy A = A^T)."
  type: true-false
  answer: false
  explanation: "A = A^T requires the matrix and its transpose to have the same dimensions. If A is m×n, then A^T is n×m. For A = A^T to hold, we need m = n — A must be square. Beyond being square, entry (i,j) must equal entry (j,i) for all i and j, meaning the matrix is symmetric across its main diagonal. Non-square matrices cannot satisfy A = A^T."

- question: "For column vectors u and v of the same length, u^T v equals the dot product u · v."
  type: true-false
  answer: true
  explanation: "If u and v are n×1 column vectors, then u^T is a 1×n row vector, and u^T v is a 1×n matrix times an n×1 matrix — the result is a 1×1 scalar. That scalar is exactly the sum of u_i times v_i, which is the dot product. This identity u · v = u^T v is the bridge between geometric dot products and matrix algebra, and it motivates the definition of the transpose in abstract inner product spaces."

- question: "A student claims that (ABC)^T = A^T B^T C^T, reasoning that you just transpose each factor. What is the correct formula, and why does the student's version fail?"
  type: short-answer
  answer: "(ABC)^T = C^T B^T A^T — the order of the factors reverses. The student's version fails because transposing a product is not the same as multiplying the transposed factors in the same order. Applying the rule twice: (ABC)^T = ((AB)C)^T = C^T (AB)^T = C^T B^T A^T. The reversal is necessary because matrix multiplication is not commutative, and the dimensions only line up correctly when the order is reversed."
  explanation: "The reversal rule (AB)^T = B^T A^T is analogous to (AB)^{-1} = B^{-1}A^{-1}: both arise because reversing the order is what makes dimensions (or the product with the identity) work out. For n factors, (A_1 A_2 ... A_n)^T = A_n^T ... A_2^T A_1^T. Students who forget this reversal will write expressions that are dimensionally impossible for non-square matrices, which is the easiest way to catch the error."
```

## Explainer

You already know that a matrix is a rectangular grid of numbers, where the entry in row i and column j is written a_ij. The **transpose** of a matrix A, written A^T, is the result of reflecting A across its main diagonal: every row becomes a column and every column becomes a row. Formally, the entry in row i and column j of A^T equals the entry in row j and column i of A. If A is a 3×2 matrix, then A^T is a 2×3 matrix — the dimensions swap.

The most important algebraic property of the transpose is how it interacts with products: **(AB)^T = B^T A^T**. Notice the reversal of order — this is the same "flip-the-order" pattern you'd expect from experience with inverses. Intuitively, if you think of matrix multiplication as a sequence of transformations applied right-to-left, transposing reverses not just the matrices but the order in which they act. The additive property is simpler: (A + B)^T = A^T + B^T, and taking the transpose twice returns the original matrix.

A **symmetric matrix** is one that equals its own transpose: A = A^T. This means entry (i,j) equals entry (j,i) — the matrix is a mirror image of itself across the diagonal. Symmetric matrices appear constantly in applications: covariance matrices in statistics, the Hessian matrix in optimization, and adjacency matrices for undirected graphs are all symmetric. Symmetry is a strong structural condition that constrains eigenvalues to be real and guarantees diagonalizability, topics you'll encounter as you build toward eigenvalue decomposition.

The transpose also unlocks the concept of the **dot product** in matrix language: if u and v are column vectors, then the dot product u · v equals u^T v (a 1×n matrix times an n×1 matrix giving a scalar). This connection between the transpose and inner products is the seed of a deeper idea — the **adjoint** — which generalizes to abstract linear maps on inner product spaces and is foundational in quantum mechanics and functional analysis. For now, treat the transpose as the basic bookkeeping operation that reorients a matrix, and practice applying the product-reversal rule until it becomes automatic.
