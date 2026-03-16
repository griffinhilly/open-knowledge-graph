---
id: change-of-basis
title: Change of Basis and Coordinate Systems
domain: mathematics
course: linear-algebra
prerequisites:
- id: basis-and-dimension
  type: hard
- id: matrix-inverses
  type: hard
- id: transformation-matrices
  type: soft
- id: matrix-composition
  type: soft
builds-toward:
- diagonalization
tags:
- change of basis
- coordinate vector
- transition matrix
- similarity
stage: formal-systems
status: validated
---
# Change of Basis and Coordinate Systems

## Core Idea
Given two bases B and C for the same vector space, the change-of-basis matrix P_{C←B} converts coordinate vectors from B-coordinates to C-coordinates. The columns of P_{C←B} are the B-basis vectors written in C-coordinates. The inverse P_{C←B}⁻¹ = P_{B←C} converts back. When a linear transformation T has matrix A relative to the standard basis, its matrix relative to basis B is B⁻¹AB (where B is the matrix with B-basis vectors as columns) — this is the similarity transformation. Similar matrices represent the same linear transformation from different perspectives.

## How It's Best Learned
Work explicitly with two bases in R²: write a vector in both coordinate systems and verify the change-of-basis matrix converts between them. Then use change-of-basis to simplify a linear transformation by choosing the basis of eigenvectors.

## Common Misconceptions
- The change-of-basis matrix has basis vectors as COLUMNS, not rows.
- P_{C←B} and P_{B←C} are inverses, not transposes (in general).
- Similar matrices A and B = P⁻¹AP represent the same transformation but are NOT equal as matrices unless P = I.

## Explainer

From your prerequisite on basis and dimension, you know a basis is a set of linearly independent vectors that spans a space — and every vector in the space has a unique representation as a linear combination of the basis vectors. Those coefficients are the **coordinate vector** of a point relative to that basis. The standard basis in Rⁿ gives you the familiar coordinates; a different basis gives you a different coordinate system for the same space. **Change of basis** is the machinery for converting coordinates from one description to another.

Think of a map analogy: the same physical location can be described in GPS coordinates, or in "blocks north and east of city hall." These are different coordinate systems for the same terrain. A change-of-basis matrix is the translation dictionary between them. If you know a vector's coordinates in basis B, and you want its coordinates in basis C, you apply the **transition matrix** P_{C←B}. Its columns are the B-basis vectors expressed in C-coordinates — this is the key construction. You're asking: "the first basis vector of B, described in C's language, is what?" That answer is the first column.

The inverse relationship follows naturally: P_{B←C} = (P_{C←B})⁻¹. Going from B to C and then back from C to B should return you to where you started, so the two matrices compose to the identity. This is why your prerequisite on matrix inverses is essential — the change-of-basis framework lives and breathes via matrix inversion.

The deepest application connects to **similarity transformations**. Suppose a linear transformation T has matrix A in standard coordinates. In basis B (whose vectors are the columns of matrix P), the same transformation is represented as P⁻¹AP. The two matrices A and P⁻¹AP are **similar** — they describe the same transformation, just in different coordinate languages. This is why diagonalization (which you'll encounter next) is so powerful: if you choose the basis of eigenvectors, P⁻¹AP becomes a diagonal matrix, making the transformation trivially easy to analyze. The same transformation that looked complicated in standard coordinates becomes transparent in the right basis — change of basis reveals structure by choosing the coordinate system that best matches the problem.
