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

## Explainer

You already know that a matrix is a rectangular array of numbers. Now consider that you might want to combine two matrices — perhaps to represent two transformations applied in sequence, or simply to add quantities organized in tabular form. **Matrix addition** is the straightforward case: if A and B have the same dimensions, you add them entry-by-entry. (A + B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ. Think of adding two spreadsheets cell by cell. The same-dimension requirement is the only constraint, and the operation inherits all the familiar arithmetic properties — commutativity, associativity — from ordinary addition.

**Matrix multiplication** is the consequential operation, and it works nothing like addition. The product AB multiplies the i-th row of A by the j-th column of B using a **dot product**: (AB)ᵢⱼ = Σₖ Aᵢₖ Bₖⱼ. For this to be defined, the number of columns in A must equal the number of rows in B. An (m × p) matrix times a (p × n) matrix produces an (m × n) matrix — the inner dimensions p must match and the outer dimensions m, n survive. The reason for this rule becomes clear when you think about what multiplication will later be shown to represent: applying one linear transformation followed by another. Composing a transformation from ℝᵖ → ℝᵐ with one from ℝⁿ → ℝᵖ produces a transformation from ℝⁿ → ℝᵐ.

The most important property to internalize is **non-commutativity**: in general, AB ≠ BA. Sometimes one product is defined and the other is not (if A is 2×3 and B is 3×4, then AB is 2×4, but BA requires a 4×3 times a 2×3 — impossible). Even when both are defined and square, the results typically differ. Think of the physical analogy: rotating an object and then flipping it produces a different orientation than flipping first and then rotating. Matrix multiplication encodes this kind of ordered sequential action.

The **transpose** operation Aᵀ swaps rows and columns: (Aᵀ)ᵢⱼ = Aⱼᵢ. It converts an m×n matrix into an n×m matrix. A key identity is that transposing a product reverses the order: (AB)ᵀ = BᵀAᵀ. This reversal matters — it is not AᵀBᵀ. Symmetric matrices, where Aᵀ = A, play a special role throughout linear algebra, and the transpose appears constantly in formulas for projections, least squares, and quadratic forms. Mastering these three operations — addition, multiplication, and transpose — is the prerequisite for every matrix computation that follows.
