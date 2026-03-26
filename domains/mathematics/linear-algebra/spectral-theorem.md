---
id: spectral-theorem
title: The Spectral Theorem
domain: mathematics
course: linear-algebra
prerequisites:
- id: symmetric-matrices
  type: hard
- id: diagonalization
  type: hard
- id: orthonormal-bases
  type: hard
tags:
- spectral theorem
- orthogonal diagonalization
- principal axes
- eigendecomposition
- symmetric
stage: formal-systems
status: validated
---

# The Spectral Theorem

## Core Idea
The Spectral Theorem states that every real symmetric matrix A is orthogonally diagonalizable: there exists an orthogonal matrix Q (with Qᵀ = Q⁻¹) and diagonal matrix D such that A = QDQᵀ. The columns of Q are orthonormal eigenvectors of A and D contains the corresponding real eigenvalues. This is stronger than ordinary diagonalization in two ways: the diagonalizing matrix Q is orthogonal (not just invertible), and real eigenvectors always exist. The spectral decomposition A = Σ λᵢuᵢuᵢᵀ writes A as a sum of rank-1 orthogonal projections, one per eigenvalue, revealing the geometric structure of the transformation.

## How It's Best Learned
Orthogonally diagonalize a 2×2 symmetric matrix, verify Q is orthogonal, and reconstruct A = QDQᵀ. Then interpret the eigenvectors as the 'principal axes' of the quadratic form xᵀAx — an ellipse aligned with the eigenvectors.

## Common Misconceptions
- The Spectral Theorem applies to SYMMETRIC matrices; it does not hold for general (non-symmetric) matrices, which may not be diagonalizable or may require complex eigenvectors.
- 'Spectral' refers to the spectrum (set of eigenvalues) of A, not to visible-light spectra.
- Orthogonal diagonalization requires Gram-Schmidt within each eigenspace when an eigenvalue has geometric multiplicity > 1; distinct eigenvalue eigenvectors are already orthogonal but may need normalization.

## Questions

```yaml
- question: "A matrix A is diagonalizable (A = PDP⁻¹) with real eigenvalues, but A is not symmetric. What does the Spectral Theorem say about orthogonal diagonalizability?"
  type: multiple-choice
  options:
    - "A can still be orthogonally diagonalized since its eigenvalues are real"
    - "A cannot be orthogonally diagonalized in general — that requires symmetry"
    - "The Spectral Theorem guarantees orthogonal diagonalizability for all diagonalizable matrices"
    - "A's eigenvectors are automatically orthogonal if the eigenvalues are distinct"
  answer: 1
  explanation: "The Spectral Theorem applies specifically to symmetric matrices — it does NOT hold for general diagonalizable matrices. A non-symmetric matrix can have real eigenvalues and be diagonalizable without being orthogonally diagonalizable. Orthogonal diagonalizability (A = QDQᵀ with Qᵀ = Q⁻¹) is a strictly stronger guarantee. Option D is the key misconception: real distinct eigenvalues do not force eigenvector orthogonality unless A is symmetric."

- question: "A real symmetric matrix has eigenvalues λ₁ = 3 and λ₂ = 5 with corresponding eigenvectors u₁ and u₂. Without computing u₁ and u₂ explicitly, what can you conclude about their dot product?"
  type: multiple-choice
  options:
    - "Some nonzero value determined by the specific entries of A"
    - "Zero — they must be orthogonal"
    - "One — eigenvectors are normalized by convention"
    - "Undefined without knowing the specific entries of A"
  answer: 1
  explanation: "The Spectral Theorem guarantees that eigenvectors of a real symmetric matrix corresponding to *distinct* eigenvalues are always orthogonal. The proof uses symmetry: if Au = λu and Av = μv with λ ≠ μ, then ⟨u,v⟩ = 0 follows from uᵀAv = (Aᵀu)ᵀv = (Au)ᵀv. This holds regardless of the specific entries — it is a consequence of symmetry, not of the particular values of A."

- question: "Nearly every real matrix with distinct eigenvalues is orthogonally diagonalizable."
  type: true-false
  answer: false
  explanation: "Distinct real eigenvalues guarantee diagonalizability (enough linearly independent eigenvectors to write A = PDP⁻¹), but not orthogonal diagonalizability. A non-symmetric matrix with distinct real eigenvalues has eigenvectors that may not be orthogonal — you can write A = PDP⁻¹ but cannot write A = QDQᵀ with Q orthogonal. The Spectral Theorem's guarantee of orthogonal diagonalizability is exclusive to symmetric matrices."

- question: "The columns of Q in the decomposition A = QDQᵀ are orthonormal eigenvectors of A."
  type: true-false
  answer: true
  explanation: "This is a direct statement of orthogonal diagonalizability. Q is orthogonal (Qᵀ = Q⁻¹), which means its columns are mutually orthogonal unit vectors. Each column is an eigenvector of A (by the structure of the diagonalization), and together they form an orthonormal basis for ℝⁿ. The diagonal entries of D are the corresponding real eigenvalues. This is what the Spectral Theorem guarantees: not just any diagonalizing matrix, but one whose columns form a complete orthonormal eigenbasis."

- question: "Why does the symmetry condition Aᵀ = A force eigenvectors corresponding to different eigenvalues to be orthogonal? Sketch the key step of the argument."
  type: short-answer
  answer: "Suppose Au = λu and Av = μv with λ ≠ μ. Compute uᵀAv two ways: uᵀ(Av) = uᵀ(μv) = μ(uᵀv), and (Aᵀu)ᵀv = (Au)ᵀv = (λu)ᵀv = λ(uᵀv), using Aᵀ = A. So μ(uᵀv) = λ(uᵀv), giving (μ − λ)(uᵀv) = 0. Since λ ≠ μ, we conclude uᵀv = 0."
  explanation: "Symmetry does the crucial work: it lets you move A from one side of the inner product to the other (uᵀAv = (Aᵀu)ᵀv = (Au)ᵀv when Aᵀ = A). This algebraic identity, combined with the two eigenvalue equations, forces the inner product of distinct eigenvectors to be zero. Without symmetry, this step fails — which is why non-symmetric matrices can have non-orthogonal eigenvectors even with distinct eigenvalues."
```

## Explainer

You already know that a matrix can be diagonalized — written as PDP⁻¹ — when it has enough linearly independent eigenvectors. The Spectral Theorem says something far stronger holds for **symmetric matrices**: not just diagonalizable, but *orthogonally* diagonalizable. The diagonalizing matrix Q is not merely invertible — its columns are mutually perpendicular unit vectors. This means Qᵀ = Q⁻¹, so the decomposition A = QDQᵀ is both elegant and computationally stable.

Why does symmetry force this? Two deep facts work together. First, all eigenvalues of a real symmetric matrix are **real** — no complex numbers arise, even though the characteristic polynomial could in principle have complex roots. Second, eigenvectors corresponding to *distinct* eigenvalues are always **orthogonal to each other**. This is a theorem, not a coincidence: if Au = λu and Av = μv with λ ≠ μ, then ⟨u, v⟩ = 0 follows from the symmetry condition uᵀAv = (Au)ᵀv. Symmetric matrices represent transformations that act like "pure stretching" along perpendicular principal axes, with no rotational mixing.

The **spectral decomposition** A = Σ λᵢ uᵢuᵢᵀ is the most revealing form. Each term λᵢ uᵢuᵢᵀ is a rank-1 matrix that projects any vector onto the axis uᵢ and scales by λᵢ. When you multiply A**v** for any vector **v**, each projection extracts the component of **v** along uᵢ, scales it by λᵢ, and all the scaled components reassemble. The matrix acts as an independent stretch along each eigenvector axis — no cross-coupling between axes.

This **principal axes** interpretation becomes concrete with quadratic forms xᵀAx. A positive definite symmetric matrix defines an ellipsoid, and the eigenvectors of A give the orientation of that ellipsoid's principal axes while the eigenvalues give the stretching factors. Rotating to the eigenvector basis eliminates all cross-terms. This is the mathematical core of principal component analysis (PCA) in data science, spectral methods in graph theory, and the quantum mechanical treatment of observables.
