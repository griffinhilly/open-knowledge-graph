---
id: determinant-properties
title: Determinant Properties and Computation
domain: mathematics
course: linear-algebra
prerequisites:
- id: determinants-2x2-3x3
  type: hard
builds-toward:
- matrix-inverses
- characteristic-polynomial
- rank-and-nullity-theorem
tags:
- determinant
- properties
- computation
- cofactors
stage: formal-systems
status: draft
---

# Determinant Properties and Computation

## Core Idea
Determinants satisfy key properties: det(AB) = det(A)det(B), det(Aᵀ) = det(A), det(A⁻¹) = 1/det(A), and multiplying a row by c multiplies the determinant by c. Row operations can simplify computation: swapping rows negates det, adding a multiple of one row to another preserves det. Cofactor expansion allows recursive computation for any size.
