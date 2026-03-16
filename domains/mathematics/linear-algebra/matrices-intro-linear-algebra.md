---
id: matrices-intro-linear-algebra
title: Matrices and Matrix Notation
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn
  type: soft
builds-toward:
- matrix-addition-subtraction
- matrix-multiplication
- systems-of-linear-equations
- linear-transformations
tags:
- matrices
- fundamentals
- notation
stage: formal-systems
status: draft
---

# Matrices and Matrix Notation

## Core Idea
A matrix is a rectangular array of numbers arranged in rows and columns; an m × n matrix has m rows and n columns. Matrices generalize vectors and are used to represent systems of equations, linear transformations, and quadratic forms. Matrix notation A = (aᵢⱼ) allows compact representation of data and operations.

## Explainer

If you already know vectors from Rⁿ, you can think of a matrix as a natural generalization: a vector is a single column of numbers, while a **matrix** packages multiple columns (or rows) together into one rectangular structure. An m × n matrix has m rows and n columns — the entry in row i and column j is written aᵢⱼ. The subscript convention is row first, column second, so a₂₃ lives in the second row and third column. A 3 × 1 matrix is just a column vector with three components; a 1 × 3 matrix is a row vector.

The power of matrix notation comes from what matrices *represent*. One of the most important interpretations is a system of linear equations. The system 2x + 3y = 7, x − y = 1 can be written as the matrix equation Ax = b, where A is the 2 × 2 coefficient matrix, x is a column vector of unknowns, and b is a column vector of right-hand sides. Packaging all the coefficients into A separates the structure of the system from the specific values, making it possible to reason about all systems of that shape at once.

A second fundamental interpretation is a **linear transformation**: a rule that maps every vector in Rⁿ to a vector in Rᵐ in a way that preserves addition and scalar multiplication. Every such transformation is completely determined by its m × n matrix — multiply the matrix by any input vector and you get the output. This connection between matrices and transformations is what makes linear algebra so broadly applicable: rotating points in 3D space, projecting onto a plane, stretching in one direction, and mixing audio channels are all matrix multiplications.

The notation A = (aᵢⱼ) is shorthand for describing the entire matrix by its generic entry. To specify a particular matrix, you write out the full array: a 2 × 3 example might be [[1, 2, 3], [4, 5, 6]]. Square matrices (m = n) arise most often in the theory — they represent transformations from a space back to itself and have additional structure like determinants and eigenvalues. As you move into matrix arithmetic (addition, multiplication) and then to systems and transformations, the rectangular array you learned here will serve as the common language connecting all those ideas.
