---
id: matrix-addition-multiplication
title: Matrix Addition, Multiplication, and Transpose
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrices-intro
  type: hard
builds-toward:
- linear-transformations-definition
- matrix-inverses-computation
- determinant-computation
tags:
- matrices
- operations
- algebra
stage: formal-systems
status: draft
---

# Matrix Addition, Multiplication, and Transpose

## Core Idea
Matrices are rectangular arrays of numbers. Matrix addition/subtraction works entry-wise, while multiplication of an (m×p) matrix A by a (p×n) matrix B produces an (m×n) matrix with entries (AB)ᵢⱼ = Σₖ Aᵢₖ Bₖⱼ. The transpose Aᵀ swaps rows and columns. These operations do not all commute, and matrix algebra is noncommutative.

## How It's Best Learned
Practice small 2×2 and 2×3 multiplications by hand to develop intuition. Verify that AB ≠ BA with numerical examples. Connect matrix multiplication to composition of linear transformations.

## Common Misconceptions
Matrix multiplication is not entry-wise. (AB)ᵢⱼ is a dot product of row i of A with column j of B, not a simple product. AB and BA are different and both may not even be defined.
