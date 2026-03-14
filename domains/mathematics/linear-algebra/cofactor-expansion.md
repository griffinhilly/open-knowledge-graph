---
id: cofactor-expansion
title: Cofactor Expansion and n×n Determinants
domain: mathematics
course: linear-algebra
prerequisites:
- id: determinants-2x2-3x3
  type: hard
builds-toward:
- determinant-properties
- characteristic-polynomial
- cramers-rule
tags:
- cofactor
- minor
- Laplace expansion
- n-by-n determinant
- recursive
stage: formal-systems
status: validated
---

# Cofactor Expansion and n×n Determinants

## Core Idea
The cofactor expansion (Laplace expansion) generalizes determinant computation to n×n matrices recursively: det(A) = Σⱼ aᵢⱼ Cᵢⱼ where Cᵢⱼ = (−1)^(i+j) Mᵢⱼ is the signed (i,j) minor and Mᵢⱼ is the determinant of the (n−1)×(n−1) submatrix formed by deleting row i and column j. This expansion can be performed along any row or column, and choosing a row or column with many zeros minimizes computation. The checkerboard sign pattern of cofactors (alternating + and −) is a key feature. For large n, cofactor expansion is computationally expensive but conceptually fundamental.

## How It's Best Learned
Practice expanding along different rows and columns of the same matrix to verify you get the same determinant. Choose expansions along rows with zeros to reduce work. Build up from 3×3 to 4×4 manually before trusting computational tools.

## Common Misconceptions
- Students forget the checkerboard sign pattern; the (i,j) cofactor has sign (−1)^(i+j), not always positive.
- The row chosen for expansion is arbitrary — all choices give the same result, but strategic choices reduce arithmetic.
- Cofactor expansion is recursive; each minor is itself a determinant that may require further expansion.
