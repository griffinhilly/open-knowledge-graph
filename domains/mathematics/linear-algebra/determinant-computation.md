---
id: determinant-computation
title: Computing Determinants
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrices-definition
  type: hard
builds-toward:
- determinant-properties
- cramers-rule
- eigenvalues-and-eigenvectors
tags:
- determinants
- computation
- algorithms
stage: formal-systems
status: validated
---

# Computing Determinants

## Core Idea
The determinant of an n × n matrix is a scalar with geometric meaning (signed volume of the parallelepiped spanned by columns). For 2×2: det([a b; c d]) = ad − bc. For larger matrices, use cofactor expansion C_ij = (−1)^{i+j} M_ij or row reduction. det(A) = 0 iff A is singular.

## Questions

```yaml
- question: "During row reduction of a matrix, you swap two rows to get a zero into a pivot position. How does this affect the determinant?"
  type: multiple-choice
  options:
    - "It multiplies the determinant by 2, since you are rearranging two rows"
    - "It negates the determinant — multiplies it by −1"
    - "It leaves the determinant unchanged, since the same rows are still present"
    - "It multiplies the determinant by the ratio of the two swapped rows"
  answer: 1
  explanation: "Swapping any two rows of a matrix negates its determinant (multiplies by −1). This is one of three fundamental row operation rules: row swap → negate det; multiply a row by scalar c → multiply det by c; add a multiple of one row to another → det unchanged. When computing det via row reduction, you must track every row swap and multiply the final result (product of the upper triangular diagonal) by (−1)^(number of swaps)."

- question: "A 3×3 matrix has three column vectors that all lie in the same plane through the origin. What is the determinant?"
  type: multiple-choice
  options:
    - "1, since the vectors form a valid basis for the plane"
    - "0, since the columns are linearly dependent and the matrix is singular"
    - "The area of the triangle spanned by the three column tips"
    - "Undefined, since three coplanar vectors cannot form a 3×3 matrix"
  answer: 1
  explanation: "The determinant measures the signed volume of the parallelepiped spanned by the column vectors. If all three columns lie in the same plane, the parallelepiped is completely flat — it has zero volume. This is also the algebraic signal: three coplanar vectors are linearly dependent (one is a linear combination of the others), and det(A) = 0 if and only if the matrix is singular. Zero determinant, singular matrix, and linearly dependent columns are all equivalent conditions."

- question: "Adding a multiple of one row to another row during row reduction leaves the determinant unchanged."
  type: true-false
  answer: true
  explanation: "This is one of three fundamental row operation rules, and the most useful: Gaussian elimination primarily uses this operation, so it preserves the determinant throughout. Only row swaps (which negate it) and row scaling (which multiply it by a scalar) change the value. You can row-reduce freely using add-a-multiple-of-a-row operations and only need to track swaps and scalings. This is why row reduction is efficient for computing determinants."

- question: "If det(A) = 5 for a 3×3 matrix A, then the matrix 2A (every entry doubled) has determinant 10."
  type: true-false
  answer: false
  explanation: "Multiplying every entry of an n×n matrix by scalar c multiplies the determinant by cⁿ, not c. Each row is scaled by c, and each row scaling multiplies the determinant by c. For a 3×3 matrix with c = 2: det(2A) = 2³ · det(A) = 8 · 5 = 40, not 10. This mistake comes from thinking of the determinant as linear in the matrix entries overall. It is multilinear — linear separately in each row — so scaling all n rows by c raises c to the nth power."

- question: "Why does det(A) = 0 imply that the matrix A is singular (non-invertible)?"
  type: short-answer
  answer: "The determinant measures the signed volume of the parallelepiped spanned by the column vectors of A. If det(A) = 0, the columns span a lower-dimensional space — they are linearly dependent, meaning at least one column is a linear combination of the others. A linear transformation with linearly dependent columns squashes space onto a lower-dimensional subspace: it is not one-to-one, so no inverse can exist. Algebraically: the system Ax = 0 has non-trivial solutions, the null space is non-trivial, and A cannot be inverted."
  explanation: "The equivalence runs in both directions: det(A) ≠ 0 iff A is invertible iff the columns are linearly independent iff Ax = b has a unique solution for every b. All of these conditions are equivalent, and the determinant provides a single scalar test for all of them. This is why the determinant appears throughout linear algebra — in Cramer's rule, eigenvalue computation, and the matrix inverse formula — as the fundamental indicator of whether a linear transformation preserves or collapses dimensionality."
```

## Explainer

You know from your work with matrices that a matrix represents a linear transformation — it takes a vector and produces a new vector. The **determinant** measures how that transformation scales space. Specifically, the absolute value of the determinant of a 2×2 matrix equals the area of the parallelogram formed by the two column vectors. For a 3×3 matrix, it equals the volume of the parallelepiped formed by the three column vectors. If the determinant is negative, it means the transformation includes a reflection — it reversed the orientation of space. If the determinant is zero, the transformation squashes all of space onto a lower-dimensional subspace (the columns are linearly dependent), which is why det(A) = 0 if and only if A is singular.

For a 2×2 matrix [a b; c d], the formula is simply ad − bc. The geometric intuition: one column is (a, c) and the other is (b, d). The area of the parallelogram they span is the base times the height — computing this gives ad − bc. You can verify: if the two columns are identical, the parallelogram collapses to a line, giving area 0, and indeed ad − bc = ad − ad = 0.

For larger matrices, the two main methods are **cofactor expansion** and **row reduction**. In cofactor expansion, you pick any row or column and expand along it: det(A) = Σ aᵢⱼ · Cᵢⱼ, where the **cofactor** Cᵢⱼ = (−1)^{i+j} · Mᵢⱼ and Mᵢⱼ is the determinant of the (n−1)×(n−1) matrix left after deleting row i and column j. The (−1)^{i+j} factor creates a checkerboard sign pattern (+,−,+,−,…). This reduces an n×n determinant to a sum of (n−1)×(n−1) determinants, applied recursively. For a 3×3 matrix, this means three 2×2 determinants; for 4×4, four 3×3 determinants.

Row reduction is usually faster for larger matrices. The key facts: swapping two rows negates the determinant; multiplying a row by a scalar multiplies the determinant by that scalar; adding a multiple of one row to another leaves the determinant unchanged. By tracking these operations as you row-reduce to upper triangular form, you can compute the determinant as the product of the diagonal entries (times any sign flips from row swaps and any scalars you factored out). This connects the determinant computation directly to Gaussian elimination, which you will use throughout linear algebra — determinants and row reduction are deeply intertwined tools.
