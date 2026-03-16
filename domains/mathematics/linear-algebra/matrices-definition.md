---
id: matrices-definition
title: 'Matrices: Definition, Notation, and Special Types'
domain: mathematics
course: linear-algebra
prerequisites: []
builds-toward:
- matrix-addition-subtraction
- matrix-multiplication
- systems-of-linear-equations
tags:
- matrices
- definition
- notation
stage: formal-systems
status: draft
---

# Matrices: Definition, Notation, and Special Types

## Core Idea
An m × n matrix is a rectangular array of m rows and n columns of scalars. Matrices are denoted A, B, etc., with entry a_ij in row i and column j. Special types include square matrices (m = n), diagonal, identity, triangular, and symmetric matrices. Matrices represent linear systems and transformations.

## Explainer

A **matrix** is simply a way of organizing numbers into a grid. An m × n matrix has m rows and n columns, so a 3 × 2 matrix has 3 rows and 2 columns. The entry in row i and column j is written a_ij — the row index always comes first. This double-subscript notation is the key to reading and writing matrix entries fluently: a_23 means row 2, column 3.

The power of the matrix format is that it packages a lot of information in a structured way that supports systematic computation. A system of two equations with three unknowns, for instance, can be represented as a 2 × 3 matrix of coefficients — the entire system fits in one object, and operations on the system become operations on the matrix. This is why matrices are the natural language for linear algebra: they translate between geometric transformations and numerical operations.

Several **special matrix types** appear constantly and deserve careful attention. A **square matrix** has equal numbers of rows and columns (m = n). The **identity matrix** I is a square matrix with 1s on the main diagonal and 0s everywhere else — it behaves like the number 1 in multiplication, leaving any matrix unchanged. A **diagonal matrix** has nonzero entries only on the main diagonal; these are the easiest matrices to work with because their properties are determined entirely by those diagonal entries. **Triangular matrices** (upper or lower) have zeros either below or above the main diagonal, which makes solving linear systems especially straightforward. A **symmetric matrix** satisfies A = Aᵀ, meaning it equals its own transpose — row i equals column i. Symmetric matrices arise throughout applied mathematics and have especially clean spectral properties.

Getting comfortable with the notation early pays large dividends. When you see a_ij, ask: which row? which column? When you see "m × n," remind yourself which dimension is which. The notation is designed to be consistent: matrix A is described as m × n (rows × columns), entry a_ij is (row i, column j), and this pattern never changes throughout linear algebra, regardless of the operation. Every computation you will do with matrices — addition, multiplication, inversion, decomposition — builds on fluency with this foundational bookkeeping.
