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
