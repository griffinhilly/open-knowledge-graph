---
id: column-space
title: Column Space and Row Space
domain: mathematics
course: linear-algebra
prerequisites:
- id: subspaces
  type: hard
- id: span-of-vectors
  type: hard
builds-toward:
- least-squares-approximation
tags:
- column-space
- row-space
- image
stage: formal-systems
status: draft
---

# Column Space and Row Space

## Core Idea
The column space col(A) is the span of the columns of A; it equals the image of the linear transformation x ↦ Ax. The row space row(A) is the span of the rows of A, equal to col(Aᵀ). Both are fundamental subspaces determined by A; rank(A) is the dimension of each.

## Questions

```yaml
- question: "The system Ax = b has no solution. What does this tell you about b in relation to A?"
  type: multiple-choice
  options:
    - "b is in the null space of A"
    - "b is not in the column space of A"
    - "b is a linear combination of the rows of A"
    - "b equals the zero vector"
  answer: 1
  explanation: "Ax = b has a solution if and only if b is in the column space of A. Since Ax computes a linear combination of A's columns with x as coefficients, the set of all achievable right-hand sides is exactly col(A). If b is not in col(A), no combination of the columns can produce it, so no solution exists. Option A (null space) is the set of x where Ax = 0 — it describes inputs that map to zero, not right-hand sides."

- question: "A student row-reduces a matrix A to its echelon form and finds that columns 1 and 3 are pivot columns. To find a basis for col(A), she takes columns 1 and 3 from the echelon form. What has she done wrong?"
  type: multiple-choice
  options:
    - "Nothing — the echelon form's pivot columns form a valid basis for col(A)"
    - "She should take columns 1 and 3 from the original matrix A, not the row-reduced form"
    - "She should use the rows rather than the columns to find the column space basis"
    - "She should take all columns, not just the pivot ones"
  answer: 1
  explanation: "Row reduction identifies *which* columns are pivot columns, but the basis vectors for col(A) must be taken from the *original* matrix A, not the row-reduced form. Row operations preserve the row space but change the column space — the specific column vectors change. The correct procedure: row-reduce to identify pivot positions, then return to A and take those columns as the basis."

- question: "Row reduction preserves the column space of a matrix."
  type: true-false
  answer: false
  explanation: "Row reduction preserves the *row space* but generally changes the *column space*. The column vectors change when you perform elementary row operations. This is why you must identify pivot columns from the row-reduced form but return to the original matrix to extract the actual basis vectors. The row and column spaces have the same dimension (rank), but they are found by different procedures."

- question: "The column space of an m × n matrix A is a subspace of ℝⁿ."
  type: true-false
  answer: false
  explanation: "The column space of an m × n matrix A is a subspace of ℝᵐ, not ℝⁿ. The columns of A are vectors in ℝᵐ (each column has m entries), so their span lives in ℝᵐ. The row space, by contrast, is a subspace of ℝⁿ. It's easy to confuse these because m and n both appear in descriptions of A — keeping track of which dimension corresponds to rows versus columns is essential."

- question: "Why does the equation Ax = b have a solution if and only if b is in the column space of A? Explain in terms of what matrix-vector multiplication actually computes."
  type: short-answer
  answer: "Matrix-vector multiplication Ax computes a linear combination of the columns of A, where the entries of x are the scalar coefficients. If A = [a₁ | a₂ | ... | aₙ], then Ax = x₁a₁ + x₂a₂ + ... + xₙaₙ. The set of all such linear combinations, as x ranges over all of ℝⁿ, is exactly col(A). So Ax = b asks: can b be written as a linear combination of A's columns? If yes, the corresponding coefficients are a solution x. If no, b is outside the reachable set, and no solution exists."
  explanation: "This interpretation is the geometric heart of linear algebra. The column space is the image of the transformation T(x) = Ax — the set of all outputs the transformation can produce. Understanding Ax as a linear combination of columns (rather than mechanically multiplying rows by x) unlocks the connection between solvability of Ax = b and the geometry of col(A)."
```

## Explainer

From your prerequisite on span of vectors, you know that the span of a set of vectors is all linear combinations of those vectors — it is the smallest subspace containing them all. The **column space** of a matrix A, written col(A), applies this idea directly: take the columns of A as your set of vectors and form their span. If A is m × n, its columns are vectors in ℝᵐ, so col(A) is a subspace of ℝᵐ. From your subspaces prerequisite, you know this span is guaranteed to be a subspace: it contains the zero vector and is closed under addition and scalar multiplication.

The geometric interpretation is the most important thing to understand. Multiplying A by a vector x computes a linear combination of the columns of A, where the entries of x are the coefficients. So the set of all vectors Ax, as x ranges over all of ℝⁿ, is exactly col(A). This means **col(A) is the image of the linear transformation** T(x) = Ax — the set of all outputs the transformation can possibly produce. The equation Ax = b has a solution if and only if b is in col(A). Geometrically: b must lie in the space that A's columns can reach.

The **row space** row(A) is the span of the rows of A, viewed as vectors in ℝⁿ. Equivalently, it is the column space of Aᵀ. A crucial fact: row reduction preserves the row space but can change the column space. When you row-reduce A to its echelon form, the nonzero rows of the echelon form span the same row space as the original rows of A. The pivot columns of A (not the echelon form) form a basis for the column space. This asymmetry is a source of many student errors — do not take the pivot columns from the reduced form and declare them a basis for col(A); go back to the original matrix.

The **rank** of A is defined as the dimension of the column space, and it equals the dimension of the row space — these two numbers always agree, a non-obvious theorem. The rank counts the number of pivot columns (or pivot rows) after row reduction. Together with the rank-nullity theorem, which you will use extensively in least-squares approximation, rank organizes all four fundamental subspaces of a matrix: the column space, the row space, the null space, and the left null space. Understanding which space a given vector belongs to — and why — is the unifying question of linear algebra.
