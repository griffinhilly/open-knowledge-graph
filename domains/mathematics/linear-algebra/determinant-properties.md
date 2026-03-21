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

## Questions

```yaml
- question: "Matrix A is a 3×3 matrix with det(A) = 5. What is det(3A)?"
  type: multiple-choice
  options:
    - "15 — multiply det(A) by the scalar 3"
    - "45 — multiply det(A) by 3², since there are two dimensions affected"
    - "135 — multiply det(A) by 3³, since scaling a 3×3 matrix by 3 scales each of three dimensions"
    - "5 — scalar multiplication of a matrix doesn't affect its determinant"
  answer: 2
  explanation: "det(cA) = cⁿ det(A) for an n×n matrix. For a 3×3 matrix, det(3A) = 3³ · det(A) = 27 · 5 = 135. The geometric explanation: the determinant measures volume. Scaling every entry by 3 scales each of the three spatial dimensions by 3, so volume scales by 3 × 3 × 3 = 27. The most common error is option A — treating det as a linear function of the scalar, which ignores the n-dimensional nature of the volume scaling."

- question: "During Gaussian elimination on matrix A, you perform these operations in order: swap two rows, multiply one row by 5, add a multiple of one row to another. How does each operation affect det(A)?"
  type: multiple-choice
  options:
    - "Swap negates det; scaling by 5 multiplies det by 5; row addition multiplies det by the row multiple used"
    - "Swap negates det; scaling by 5 multiplies det by 5; row addition leaves det unchanged"
    - "All three operations are elementary row operations and therefore all leave det unchanged"
    - "Swap does not affect det; scaling multiplies by 5; row addition leaves det unchanged"
  answer: 1
  explanation: "Row swap negates the determinant (reverses orientation of the parallelogram/parallelepiped). Scaling a row by c multiplies det by c (stretches one edge, scaling the volume proportionally). Adding a multiple of one row to another is a shear — it distorts the shape but preserves area/volume, so det is unchanged. This is precisely why Gaussian elimination computes determinants efficiently: track only the row swaps (sign changes) and scalings, and multiply the final triangular diagonal."

- question: "det(Aᵀ) = det(A) for any square matrix A, meaning a matrix and its transpose always have the same determinant."
  type: true-false
  answer: true
  explanation: "This is a fundamental property. It reflects a deep symmetry: rows and columns contribute equally to the determinant's geometric meaning. One consequence is that every column property of determinants has an equivalent row property — for example, det is zero if any row is a zero row OR if any column is a zero column, and linear dependence in rows implies the same as linear dependence in columns."

- question: "If det(A) = 0, it means matrix A has no eigenvalues, which is why A is not invertible."
  type: true-false
  answer: false
  explanation: "This reverses the relationship. det(A) = 0 means 0 IS an eigenvalue of A — there exists a nonzero vector v such that Av = 0·v = 0, meaning A maps v to the zero vector. This nontrivial null space is exactly what makes A non-invertible. The correct statement is: det(A) = 0 implies 0 is an eigenvalue, not that A lacks eigenvalues. (A matrix always has eigenvalues over the complex numbers, and most non-invertible matrices have many nonzero eigenvalues in addition to zero.)"

- question: "Why does adding a multiple of one row to another row leave the determinant unchanged, even though it alters the entries of the matrix?"
  type: short-answer
  answer: "Adding a multiple of one row to another is geometrically a shear transformation. Shearing a parallelogram (or parallelepiped) distorts its shape — edges tilt — but preserves its area (or volume), because the base length and perpendicular height remain the same. Since the determinant measures signed volume, and shear preserves volume, the determinant is unchanged. This is analogous to how you can shear a rectangle into a parallelogram without changing its area as long as the base and height stay constant."
  explanation: "Understanding this geometrically rather than algebraically is what makes the rule intuitive rather than arbitrary. It also explains why Gaussian elimination (which consists of row operations, including shears) can compute the determinant without changing its magnitude — you only need to track the sign changes from row swaps and the multiplicative factor from row scaling."
```

## Explainer

From computing determinants, you learned the mechanics — cofactor expansion, the rule of Sarrus for 3×3 matrices. Now the question becomes: what does the determinant *mean*, and how do its algebraic properties reflect that meaning? The geometric interpretation is the foundation: **det(A) measures the signed scaling factor that the linear transformation A applies to volume**. For a 2×2 matrix, it measures the area of the parallelogram spanned by the columns (or rows); for a 3×3 matrix, the volume of the parallelepiped. The sign tells you whether the transformation preserves or reverses orientation.

This geometric picture makes the properties intuitive. **det(AB) = det(A)det(B)** says that applying transformation B then A scales volume first by det(B), then by det(A) — and scaling factors multiply. If B stretches area by factor 3 and A stretches area by factor 2, the composition AB stretches area by factor 6. **det(A^T) = det(A)** reflects the deeper symmetry that a matrix and its transpose define the same transformation up to the swap of rows and columns, which doesn't change volume. **det(cA) = cⁿ det(A)** says scaling every entry by c scales each of the n dimensions by c, so n-dimensional volume scales by cⁿ — hence the n in the exponent.

The row operation rules come from the same geometric logic. **Swapping two rows negates the determinant**: swapping rows reverses the orientation of the parallelogram/parallelepiped, flipping the sign without changing the magnitude. **Scaling a row by c multiplies the determinant by c**: scaling one edge of the parallelogram by c scales its area by c. **Adding a multiple of one row to another doesn't change the determinant**: this is a "shear" — it distorts shape but preserves area/volume, just as shearing a parallelogram into a rectangle preserves base times height. These three rules are exactly what makes Gaussian elimination a determinant-preserving tool (aside from tracked sign changes and scaling), which is why you can compute det(A) efficiently by row-reducing to a triangular matrix and multiplying the diagonal.

The invertibility criterion — **A is invertible if and only if det(A) ≠ 0** — also flows from geometry. If det(A) = 0, the transformation collapses all of n-dimensional space into a lower-dimensional subspace (a line, a plane, etc.), destroying volume. Once space is collapsed, there is no way to recover the original configuration, so the transformation has no inverse. If det(A) ≠ 0, volume is scaled but not destroyed, and the transformation is reversible. This connects directly to eigenvalues: det(A) = 0 means 0 is an eigenvalue, meaning A has a nontrivial null space, which is exactly what makes it non-invertible.
