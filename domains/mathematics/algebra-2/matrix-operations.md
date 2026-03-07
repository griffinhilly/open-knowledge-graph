---
id: matrix-operations
title: Matrix Operations
domain: mathematics
course: algebra-2
prerequisites:
  - id: matrices-intro
    type: hard
builds-toward:
  - linear-algebra-course
tags: [matrices, addition, multiplication, scalar, determinant]
stage: abstract-reasoning
status: draft
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
