---
id: matrix-operations
title: Matrix Operations
domain: mathematics
course: algebra-2
prerequisites:
  - id: matrices-intro
    type: hard
builds-toward:
  - matrix-inverses
  - eigenvalues-and-eigenvectors
tags: [matrices, addition, multiplication, scalar, determinant]
stage: abstract-reasoning
status: validated
---

# Matrix Operations

## Core Idea
Matrix addition/subtraction: add/subtract corresponding entries (matrices must have the same dimensions). Scalar multiplication: multiply every entry by the scalar. Matrix multiplication: the (i,j) entry of AB is the dot product of row i of A and column j of B. A is m x n and B is n x p, giving AB as m x p. Matrix multiplication is NOT commutative (AB != BA in general). The identity matrix I acts as a multiplicative identity: AI = IA = A.

## How It's Best Learned
Start with addition and scalar multiplication (straightforward). For matrix multiplication, practice the dot product of a row and column. Emphasize dimension compatibility: the number of columns of A must equal the number of rows of B. Show that AB != BA with a concrete example. Introduce the identity matrix. Optionally introduce determinants for 2x2 matrices.

## Common Misconceptions
- Multiplying corresponding entries like addition (matrix multiplication uses dot products, not element-wise multiplication).
- Assuming matrix multiplication is commutative.
- Multiplying matrices of incompatible dimensions.
- Thinking the identity matrix is all 1's (it has 1's on the diagonal and 0's elsewhere).

## Questions

```yaml
- question: "Matrix A is 3×4 and matrix B is 4×2. What are the dimensions of the product AB?"
  type: multiple-choice
  options: ["4×4", "3×2", "2×3", "Undefined — incompatible dimensions"]
  answer: 1
  explanation: "For AB to be defined, the number of columns in A must equal the number of rows in B — here both are 4, so the product is defined. The result has the same number of rows as A (3) and the same number of columns as B (2), giving a 3×2 matrix. The rule: if A is m×n and B is n×p, then AB is m×p."

- question: "For any two square matrices A and B of the same size, AB generally equals BA."
  type: true-false
  answer: false
  explanation: "Matrix multiplication is not commutative. Even when both A and B are square and the same size (so both AB and BA are defined and have the same dimensions), AB ≠ BA in general. You can verify this with any two 2×2 matrices. The identity matrix is a special case where AI = IA = A, but this does not generalize."

- question: "Why does the identity matrix have 1s on the diagonal and 0s elsewhere, rather than 1s everywhere?"
  type: short-answer
  answer: "The identity matrix is defined by the property AI = IA = A. The diagonal 1s ensure that each row-column dot product returns the original matrix entry, while the off-diagonal 0s prevent mixing entries from different rows or columns. A matrix of all 1s would add up entries in a way that changes A."
  explanation: "The (i,j) entry of AI is the dot product of row i of A with column j of I. Column j of I has a 1 only in position j and 0s elsewhere, so the dot product returns the j-th entry of row i of A — exactly what's needed to leave A unchanged. All-1s would sum an entire row into each entry, which destroys the original matrix."
```

## Explainer

You already know that a matrix is a rectangular grid of numbers with defined rows and columns. Matrix operations let you combine and transform these grids — and the rules differ meaningfully from ordinary arithmetic in ways that matter.

Matrix addition and scalar multiplication are the intuitive cases. To add two matrices, add corresponding entries — both must have identical dimensions. To multiply by a scalar, multiply every entry by that constant. These operations behave just like arithmetic on numbers, and there is little to misunderstand once you know matrices must have the same shape for addition.

Matrix multiplication is different. To compute the (i, j) entry of the product AB, take the dot product of row i from A and column j from B: multiply corresponding entries pair by pair and sum them up. This means the number of columns in A must equal the number of rows in B — if A is m×n and B is n×p, then AB is m×p. The most common error is treating matrix multiplication like addition (multiplying corresponding entries). That operation, called the element-wise or Hadamard product, is different and far less common. The dot-product rule exists because matrices represent linear transformations, and multiplying AB captures what happens when you apply A's transformation after B's.

The single most important fact about matrix multiplication is that it is not commutative: AB ≠ BA in general. This shocks students accustomed to arithmetic, where 3 × 5 = 5 × 3 always. Try any two 2×2 matrices and compute both orders — you will almost always get different results. Understanding why requires thinking about transformations: applying a rotation and then a reflection gives a different result than applying the reflection first, and matrices capture that asymmetry.

The identity matrix I is the exception to commutativity: for any compatible matrix A, AI = IA = A. The identity has 1s on the main diagonal and 0s everywhere else — not all 1s. The diagonal 1s ensure that each dot product in the multiplication returns exactly the entry it started from, while the off-diagonal 0s block any mixing of entries. Think of I as the matrix analog of the number 1 in multiplication.
