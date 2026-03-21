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

## Questions

```yaml
- question: "Which of the following 2×2 matrices is invertible?"
  type: multiple-choice
  options:
    - "[[1, 2], [2, 4]] — determinant = 4 − 4 = 0"
    - "[[3, 1], [5, 2]] — determinant = 6 − 5 = 1"
    - "[[2, 6], [1, 3]] — determinant = 6 − 6 = 0"
    - "[[0, 0], [1, 0]] — determinant = 0"
  answer: 1
  explanation: "A matrix is invertible if and only if its determinant is nonzero. For [[3,1],[5,2]], det = (3)(2) − (1)(5) = 6 − 5 = 1 ≠ 0, so it is invertible. All other options have determinant zero: [[1,2],[2,4]] has det = 4 − 4 = 0 (its rows are proportional); [[2,6],[1,3]] has det = 6 − 6 = 0 (same reason); [[0,0],[1,0]] has det = 0 (first row is all zeros). The det = 0 condition signals that the matrix collapses the plane into a lower-dimensional subspace — information is lost, and no inverse can recover it."

- question: "A linear transformation A maps the entire plane onto a single line through the origin (it has rank 1). A student claims A must still have an inverse because 'every transformation has an inverse.' What is the flaw in this reasoning?"
  type: multiple-choice
  options:
    - "The student is right — every square matrix has at least a left inverse"
    - "When A maps multiple distinct inputs to the same output, it is not injective — you cannot recover which original vector produced a given output, so no inverse function can exist"
    - "The inverse exists but is only defined for vectors that lie on the image line"
    - "The flaw is that A maps to a line, not a plane — you need a different theorem for non-surjective maps"
  answer: 1
  explanation: "An invertible matrix must correspond to a bijective transformation — both injective (no two inputs give the same output) and surjective (every output is achievable). When A collapses the plane to a line, infinitely many distinct input vectors map to the same output vector. An inverse function would need to 'undo' this mapping, but cannot determine which of the many inputs produced a given output. Geometrically, information is irreversibly lost when dimensions are collapsed, which is exactly why det(A) = 0 and invertibility fail together."

- question: "A square matrix with a row of all zeros has determinant zero and therefore has no inverse."
  type: true-false
  answer: true
  explanation: "True. A row of zeros means the corresponding row operation produces a zero row during reduction — the matrix cannot be row-reduced to the identity, confirming it is singular. Algebraically, expanding the determinant along the zero row immediately gives det = 0. Geometrically, a row of zeros means the transformation annihilates at least one dimension of the input space, collapsing it to a lower-dimensional image from which the original cannot be recovered."

- question: "If A and B are both invertible n×n matrices, then (AB)⁻¹ = A⁻¹B⁻¹."
  type: true-false
  answer: false
  explanation: "False — the correct formula is (AB)⁻¹ = B⁻¹A⁻¹ (order reverses). This follows from the non-commutativity of matrix multiplication: (AB)(B⁻¹A⁻¹) = A(BB⁻¹)A⁻¹ = AIA⁻¹ = AA⁻¹ = I. The reversal of order is analogous to dressing and undressing: if you put on socks then shoes (AB), you must remove shoes first, then socks (B⁻¹A⁻¹) to get back to the start. A⁻¹B⁻¹ is a different matrix and generally does not satisfy the inverse definition."

- question: "Explain geometrically why a matrix with det(A) = 0 cannot be inverted. What has happened to the space that makes reversal impossible?"
  type: short-answer
  answer: "When det(A) = 0, the matrix is rank-deficient — it collapses the input space into a lower-dimensional subspace (e.g., a 2D plane into a 1D line, or a 3D space into a plane or point). Multiple distinct input vectors get mapped to the same output vector. An inverse would need to determine which original input produced each output, but this is impossible when many inputs share a single image — the mapping is many-to-one. The 'squashed' dimension contains information that is irreversibly lost; it cannot be reconstructed from the image alone. This is why the det = 0 condition and non-invertibility are equivalent: determinant zero geometrically encodes that the transformation destroys dimension."
  explanation: "The geometric perspective unifies what might otherwise seem like separate facts: the algebraic condition det(A) ≠ 0, the rank condition (rank = n for an n×n matrix), the bijection condition on the linear transformation, and the solvability condition on the system Ax = b all describe the same underlying geometric reality — whether the transformation preserves the full dimensionality of the space."
```

## Explainer

From your work with matrix multiplication, you know that the **identity matrix** I acts like the number 1: multiplying any matrix by I leaves it unchanged. The inverse A⁻¹ is defined as the matrix that "undoes" A — applying A and then A⁻¹ returns you to the identity. This is the matrix analogue of the number 1/a: just as a · (1/a) = 1, we want A · A⁻¹ = I. The critical difference is that matrix multiplication is not commutative, so we require both AA⁻¹ = I *and* A⁻¹A = I.

The condition det(A) ≠ 0 is the gateway test for invertibility, and your prerequisite knowledge of determinants makes this concrete. For a 2×2 matrix [[a, b], [c, d]], the determinant is ad − bc. If this equals zero, the two row vectors are linearly dependent — they lie on the same line through the origin — and the matrix squashes the plane into a lower-dimensional subspace. You cannot recover the original input from the output because information was lost; no inverse exists. When det(A) ≠ 0, the formula A⁻¹ = (1/det(A)) · [[d, -b], [-c, a]] gives the inverse directly for the 2×2 case.

For larger matrices, the **row reduction method** is the systematic approach: form the augmented matrix [A | I] and apply row operations until the left side becomes I. Whatever operations transform A into I simultaneously transform I into A⁻¹. Mechanically, you are solving n linear systems simultaneously — one for each column of A⁻¹. If A cannot be reduced to I (a row of zeros appears on the left), then A is not invertible, confirming det(A) = 0.

The geometric interpretation ties everything together: an invertible matrix corresponds to a **bijective linear transformation** — one that is both injective (no two inputs give the same output) and surjective (every output is achievable). Non-invertible matrices collapse the space: a rank-deficient matrix maps multiple inputs to the same output, making reversal impossible. Invertibility is thus not just a computational property but a structural one. The inverse A⁻¹ literally reverses the transformation: if A rotates and scales the plane, A⁻¹ rotates and scales back. This geometric view becomes essential when you study linear systems, where solving Ax = b is equivalent to applying A⁻¹ to both sides — provided A is invertible.
