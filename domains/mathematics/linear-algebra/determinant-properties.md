---
id: determinant-properties
title: Properties of Determinants
domain: mathematics
course: linear-algebra
prerequisites:
- id: determinant-computation
  type: hard
builds-toward:
- cramers-rule
- eigenvalues-eigenvectors
tags:
- determinants
- properties
- linear algebra
stage: formal-systems
status: draft
---

# Properties of Determinants

## Core Idea
Key properties: det(AB) = det(A)det(B), det(A^T) = det(A), det(cA) = c^n det(A). Row operations: swapping rows negates det; scaling a row by c multiplies det by c; adding row multiples doesn't change det. A matrix is invertible iff det(A) ≠ 0.

## Explainer

From computing determinants, you learned the mechanics — cofactor expansion, the rule of Sarrus for 3×3 matrices. Now the question becomes: what does the determinant *mean*, and how do its algebraic properties reflect that meaning? The geometric interpretation is the foundation: **det(A) measures the signed scaling factor that the linear transformation A applies to volume**. For a 2×2 matrix, it measures the area of the parallelogram spanned by the columns (or rows); for a 3×3 matrix, the volume of the parallelepiped. The sign tells you whether the transformation preserves or reverses orientation.

This geometric picture makes the properties intuitive. **det(AB) = det(A)det(B)** says that applying transformation B then A scales volume first by det(B), then by det(A) — and scaling factors multiply. If B stretches area by factor 3 and A stretches area by factor 2, the composition AB stretches area by factor 6. **det(A^T) = det(A)** reflects the deeper symmetry that a matrix and its transpose define the same transformation up to the swap of rows and columns, which doesn't change volume. **det(cA) = cⁿ det(A)** says scaling every entry by c scales each of the n dimensions by c, so n-dimensional volume scales by cⁿ — hence the n in the exponent.

The row operation rules come from the same geometric logic. **Swapping two rows negates the determinant**: swapping rows reverses the orientation of the parallelogram/parallelepiped, flipping the sign without changing the magnitude. **Scaling a row by c multiplies the determinant by c**: scaling one edge of the parallelogram by c scales its area by c. **Adding a multiple of one row to another doesn't change the determinant**: this is a "shear" — it distorts shape but preserves area/volume, just as shearing a parallelogram into a rectangle preserves base times height. These three rules are exactly what makes Gaussian elimination a determinant-preserving tool (aside from tracked sign changes and scaling), which is why you can compute det(A) efficiently by row-reducing to a triangular matrix and multiplying the diagonal.

The invertibility criterion — **A is invertible if and only if det(A) ≠ 0** — also flows from geometry. If det(A) = 0, the transformation collapses all of n-dimensional space into a lower-dimensional subspace (a line, a plane, etc.), destroying volume. Once space is collapsed, there is no way to recover the original configuration, so the transformation has no inverse. If det(A) ≠ 0, volume is scaled but not destroyed, and the transformation is reversible. This connects directly to eigenvalues: det(A) = 0 means 0 is an eigenvalue, meaning A has a nontrivial null space, which is exactly what makes it non-invertible.
