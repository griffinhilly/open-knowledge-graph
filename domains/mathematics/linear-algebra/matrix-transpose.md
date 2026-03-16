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

## Explainer

You already know that a matrix is a rectangular grid of numbers, where the entry in row i and column j is written a_ij. The **transpose** of a matrix A, written A^T, is the result of reflecting A across its main diagonal: every row becomes a column and every column becomes a row. Formally, the entry in row i and column j of A^T equals the entry in row j and column i of A. If A is a 3×2 matrix, then A^T is a 2×3 matrix — the dimensions swap.

The most important algebraic property of the transpose is how it interacts with products: **(AB)^T = B^T A^T**. Notice the reversal of order — this is the same "flip-the-order" pattern you'd expect from experience with inverses. Intuitively, if you think of matrix multiplication as a sequence of transformations applied right-to-left, transposing reverses not just the matrices but the order in which they act. The additive property is simpler: (A + B)^T = A^T + B^T, and taking the transpose twice returns the original matrix.

A **symmetric matrix** is one that equals its own transpose: A = A^T. This means entry (i,j) equals entry (j,i) — the matrix is a mirror image of itself across the diagonal. Symmetric matrices appear constantly in applications: covariance matrices in statistics, the Hessian matrix in optimization, and adjacency matrices for undirected graphs are all symmetric. Symmetry is a strong structural condition that constrains eigenvalues to be real and guarantees diagonalizability, topics you'll encounter as you build toward eigenvalue decomposition.

The transpose also unlocks the concept of the **dot product** in matrix language: if u and v are column vectors, then the dot product u · v equals u^T v (a 1×n matrix times an n×1 matrix giving a scalar). This connection between the transpose and inner products is the seed of a deeper idea — the **adjoint** — which generalizes to abstract linear maps on inner product spaces and is foundational in quantum mechanics and functional analysis. For now, treat the transpose as the basic bookkeeping operation that reorients a matrix, and practice applying the product-reversal rule until it becomes automatic.
