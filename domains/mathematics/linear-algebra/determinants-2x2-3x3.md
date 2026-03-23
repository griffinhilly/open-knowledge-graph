---
id: determinants-2x2-3x3
title: Determinants of 2×2 and 3×3 Matrices
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrix-multiplication
  type: hard
builds-toward:
- determinant-properties
- matrix-inverses
- systems-of-linear-equations
- characteristic-polynomial
tags:
- determinant
- 2x2
- 3x3
- volume
stage: formal-systems
status: validated
---

# Determinants of 2×2 and 3×3 Matrices

## Core Idea
The determinant is a scalar assigned to a square matrix that measures how the matrix scales areas (2D) or volumes (3D). For 2×2: det(A) = ad − bc; for 3×3, it's computed via the rule of Sarrus or cofactor expansion. A nonzero determinant indicates the matrix is invertible.

## Questions

```yaml
- question: "A 2×2 matrix A transforms the unit square into a parallelogram with area 5. You then compute det(A) = −5. What does the negative sign indicate?"
  type: multiple-choice
  options:
    - "The determinant was computed incorrectly — area cannot be negative"
    - "The matrix is not invertible because the determinant is negative"
    - "The transformation reversed orientation (like a reflection) while scaling area by a factor of 5"
    - "The transformation shrinks area rather than expanding it"
  answer: 2
  explanation: "The absolute value |det(A)| = 5 gives the area scaling factor — the unit square maps to a parallelogram of area 5. The sign indicates orientation: positive means the transformation preserved handedness (rotation, scaling); negative means it reversed orientation (like a reflection or a shear that flips the axes). A determinant of −5 means area scales by 5 AND orientation flips. Neither sign makes the matrix non-invertible — det ≠ 0 in both cases means the matrix is invertible."

- question: "You compute the determinant of a 3×3 matrix and get 0. What does this tell you about the geometric effect of the transformation?"
  type: multiple-choice
  options:
    - "The transformation rotates 3D space by exactly 90 degrees"
    - "The transformation preserves all distances but changes angles"
    - "The transformation collapses 3D space into a lower-dimensional subspace, making it non-invertible"
    - "The transformation scales all volumes by 0 but remains one-to-one"
  answer: 2
  explanation: "det(A) = 0 means the transformation maps the unit cube to a shape with zero volume — 3D space is collapsed into a plane, a line, or a point. Different input vectors get mapped to the same output (the transformation is not one-to-one), so it cannot be reversed. Option D contradicts itself: a transformation that collapses volume to zero cannot be one-to-one. This connection between det = 0 and non-invertibility is the fundamental application of determinants throughout linear algebra."

- question: "For a 2×2 matrix, swapping its two rows produces a new matrix whose determinant is the negative of the original."
  type: true-false
  answer: true
  explanation: "Row swapping reverses orientation, which changes the sign of the determinant. If the original rows form a parallelogram with a certain signed area, swapping the rows is equivalent to reflecting that parallelogram, reversing its orientation. More generally, any single row interchange multiplies the determinant by −1. This is one of the key properties that uniquely characterizes the determinant function: multilinearity in each row, antisymmetry under row interchange, and det(I) = 1."

- question: "The Rule of Sarrus is a shortcut for computing determinants that generalizes to matrices larger than 3×3."
  type: true-false
  answer: false
  explanation: "The Rule of Sarrus works only for 3×3 matrices. Applying its diagonal shortcut to 4×4 or larger matrices gives the wrong answer. For larger matrices, you must use cofactor expansion (Laplace expansion) or row reduction. This is a common source of error: students memorize Sarrus for 3×3 and incorrectly extend the diagonal trick to larger matrices."

- question: "Explain the geometric meaning of the determinant of a 2×2 matrix, and why det(A) = 0 implies the matrix is not invertible."
  type: short-answer
  answer: "The determinant of a 2×2 matrix equals the signed area of the parallelogram formed by its two column vectors. It measures how the matrix scales area: a unit square transforms to a parallelogram of area |det(A)|. If det(A) = 0, the two column vectors are parallel (or one is zero), so the parallelogram collapses to a line with zero area. Geometrically, this means the transformation squashes 2D space into 1D — different input vectors map to the same output, so the transformation cannot be reversed."
  explanation: "The invertibility connection follows directly from the geometric picture: an invertible transformation must be one-to-one so it can be reversed. If the transformation collapses area to zero, it maps an entire line of input vectors to a single point — multiple inputs share the same output, which is irrecoverable. The formula det(A) = ad − bc captures this algebraically: if the columns are proportional, the anti-diagonal term bc equals the diagonal term ad, and their difference is zero."
```

## Explainer

From matrix multiplication, you know that a matrix transforms vectors — it stretches, rotates, reflects, or shears space. The **determinant** is a single number that captures one crucial aspect of that transformation: by what factor does the matrix scale areas (in 2D) or volumes (in 3D)? If you take a unit square and apply the matrix A, the resulting parallelogram has area equal to |det(A)|. The sign tells you whether the transformation preserved orientation (positive) or flipped it (negative, like a reflection).

For a 2×2 matrix A = [[a, b], [c, d]], the formula is det(A) = ad − bc. Geometrically, think of the two columns as vectors: [a, c] and [b, d]. The determinant is the signed area of the parallelogram they span. The product ad comes from the "main diagonal" contribution and bc from the "anti-diagonal" — you subtract the anti-diagonal because it represents the overlap. If the two column vectors are parallel (one is a multiple of the other), the parallelogram collapses to a line and det(A) = 0.

For a 3×3 matrix, the **cofactor expansion** (also called Laplace expansion) reduces the problem to three 2×2 determinants. Expanding along the first row: det(A) = a₁₁ · M₁₁ − a₁₂ · M₁₂ + a₁₃ · M₁₃, where each Mᵢⱼ is the determinant of the 2×2 matrix obtained by deleting row i and column j. The alternating signs (+ − +) follow the checkerboard pattern of cofactors. The **Rule of Sarrus** is a mnemonic shortcut specific to 3×3 matrices: write the matrix, repeat the first two columns alongside it, sum the three downward diagonals, subtract the three upward diagonals. It gives the same result as cofactor expansion and is faster by hand.

The determinant's most important application is the invertibility test: a square matrix is invertible if and only if its determinant is nonzero. When det(A) = 0, the transformation collapses space — it squashes some direction to zero, which means different inputs map to the same output, making the transformation non-reversible. This connects to everything downstream: Cramer's rule, eigenvalues (via the characteristic polynomial det(A − λI) = 0), and the theory of linear independence. The determinant is the gateway into all of these.
