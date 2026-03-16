---
id: matrix-inverses-computation
title: Matrix Inverses and Invertibility
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrix-addition-multiplication
  type: hard
- id: determinants-2x2-3x3
  type: soft
builds-toward:
- solving-linear-systems-matrix-form
- linear-transformations-definition
tags:
- inverses
- invertibility
- square-matrices
stage: formal-systems
status: draft
---

# Matrix Inverses and Invertibility

## Core Idea
An n×n matrix A is invertible if there exists A⁻¹ such that AA⁻¹ = A⁻¹A = I. A matrix is invertible if and only if det(A) ≠ 0. For 2×2 matrices, the inverse formula is simple; for larger matrices, use row reduction or cofactor methods. Invertible matrices correspond to bijective linear transformations.

## Explainer

From your work with matrix multiplication, you know that the **identity matrix** I acts like the number 1: multiplying any matrix by I leaves it unchanged. The inverse A⁻¹ is defined as the matrix that "undoes" A — applying A and then A⁻¹ returns you to the identity. This is the matrix analogue of the number 1/a: just as a · (1/a) = 1, we want A · A⁻¹ = I. The critical difference is that matrix multiplication is not commutative, so we require both AA⁻¹ = I *and* A⁻¹A = I.

The condition det(A) ≠ 0 is the gateway test for invertibility, and your prerequisite knowledge of determinants makes this concrete. For a 2×2 matrix [[a, b], [c, d]], the determinant is ad − bc. If this equals zero, the two row vectors are linearly dependent — they lie on the same line through the origin — and the matrix squashes the plane into a lower-dimensional subspace. You cannot recover the original input from the output because information was lost; no inverse exists. When det(A) ≠ 0, the formula A⁻¹ = (1/det(A)) · [[d, -b], [-c, a]] gives the inverse directly for the 2×2 case.

For larger matrices, the **row reduction method** is the systematic approach: form the augmented matrix [A | I] and apply row operations until the left side becomes I. Whatever operations transform A into I simultaneously transform I into A⁻¹. Mechanically, you are solving n linear systems simultaneously — one for each column of A⁻¹. If A cannot be reduced to I (a row of zeros appears on the left), then A is not invertible, confirming det(A) = 0.

The geometric interpretation ties everything together: an invertible matrix corresponds to a **bijective linear transformation** — one that is both injective (no two inputs give the same output) and surjective (every output is achievable). Non-invertible matrices collapse the space: a rank-deficient matrix maps multiple inputs to the same output, making reversal impossible. Invertibility is thus not just a computational property but a structural one. The inverse A⁻¹ literally reverses the transformation: if A rotates and scales the plane, A⁻¹ rotates and scales back. This geometric view becomes essential when you study linear systems, where solving Ax = b is equivalent to applying A⁻¹ to both sides — provided A is invertible.
