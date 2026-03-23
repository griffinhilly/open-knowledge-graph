---
id: matrix-representation-linear-map
title: Matrix Representation of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformation-definition
  type: hard
- id: basis-definition
  type: hard
builds-toward:
- kernel-image-rank
tags:
- transformations
- matrices
- representation
stage: formal-systems
status: validated
---

# Matrix Representation of Linear Transformations

## Core Idea
Every linear transformation from R^n to R^m can be represented by an m × n matrix A where T(x) = Ax. The columns of A are the images of the standard basis vectors. This correspondence lets us study transformations using matrices. Different bases give related but different matrix representations.

## Explainer

A linear transformation is determined entirely by what it does to a basis — and you already know this from studying basis-definition. If you know where each basis vector lands, linearity forces you to know where *every* vector lands, because every vector is a linear combination of basis vectors. The **matrix representation** is simply a way of recording that information in a convenient rectangular array.

To build the matrix for T: ℝⁿ → ℝᵐ with respect to the standard bases, apply T to each standard basis vector e₁, e₂, ..., eₙ in turn. Each output T(eᵢ) is a vector in ℝᵐ — write it as a column. Stack those columns side by side and you have your matrix A. Then for any input vector x = (x₁, ..., xₙ), the computation T(x) = Ax automatically sums up x₁ times the first column, x₂ times the second, and so on — exactly what linearity demands. The matrix is not separate from the transformation; it *is* the transformation, just written down.

The subtler point is what happens with non-standard bases. If you describe the same transformation using a different basis B for ℝⁿ and a different basis C for ℝᵐ, you get a *different* matrix — but one that represents the same geometric action. The change-of-basis formula, [T]_C = P⁻¹[T]_standard Q, tells you how the two matrices relate. This matters practically: for a given transformation, there is often a clever choice of basis that makes the matrix diagonal or nearly so — revealing the transformation's essential structure far more clearly than the standard-basis matrix would.

Think of it this way: the transformation T is an abstract geometric idea (stretching, rotating, projecting). The matrix A is a *coordinate description* of that idea, and changing coordinates changes the description without changing the underlying geometry. Studying transformations via matrices is powerful precisely because matrix arithmetic gives you tools — determinants, eigenvalues, rank — that have deep geometric meaning. Every result you will prove about linear maps (the rank-nullity theorem, the characterization of invertibility) is most naturally checked by working with the matrix representation you have just learned to construct.

## Questions

```yaml
- question: "T: ℝ² → ℝ² sends e₁ = (1,0) to (3,1) and e₂ = (0,1) to (-1,2). What is the standard matrix of T?"
  type: short-answer
  answer: "A = [[3, -1], [1, 2]] — the columns are T(e₁) and T(e₂) respectively."
  explanation: "The recipe is direct: apply T to each standard basis vector and write the result as a column. Column 1 = T(e₁) = (3,1)ᵀ, column 2 = T(e₂) = (-1,2)ᵀ. To check, verify that A·e₁ = (3,1)ᵀ and A·e₂ = (-1,2)ᵀ, which it does by construction."

- question: "If A is the matrix of T: ℝ³ → ℝ², what are the dimensions of A?"
  type: multiple-choice
  options:
    - "3 × 2"
    - "2 × 3"
    - "3 × 3"
    - "2 × 2"
  answer: 1
  explanation: "A has one column per input dimension and one row per output dimension. Input space is ℝ³ (3 dimensions → 3 columns), output space is ℝ² (2 dimensions → 2 rows). So A is 2 × 3. A common mistake is reversing this: remember the matrix shape is (output dim) × (input dim)."
```
