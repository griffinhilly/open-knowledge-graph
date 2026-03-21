---
id: change-of-basis-matrices
title: Change of Basis and Coordinate Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformation-matrix-representation
  type: hard
- id: matrix-inverses-computation
  type: hard
builds-toward:
- eigenvalues-eigenvectors-introduction
- diagonalization-similar-matrices
tags:
- change-of-basis
- coordinates
- transformations
stage: formal-systems
status: draft
---

# Change of Basis and Coordinate Transformations

## Core Idea
If B and C are two bases for Rⁿ, the change-of-basis matrix P_C←B converts coordinates from B to C: [v]_C = P_C←B [v]_B. The matrix P has C-coordinates of B-basis vectors as columns. If A represents T in the standard basis, then A' = P⁻¹AP represents T relative to basis B, where P = [B]. Similar matrices represent the same transformation in different bases.

## Questions

```yaml
- question: "Matrix A represents linear transformation T in the standard basis. Matrix P has the B-basis vectors as its columns. What does the matrix P⁻¹AP represent?"
  type: multiple-choice
  options:
    - "A completely different linear transformation that happens to share eigenvalues with T"
    - "The matrix of T expressed relative to basis B — the same transformation, new coordinates"
    - "The inverse of T expressed in basis B"
    - "The composition of T with the change-of-basis operation"
  answer: 1
  explanation: "P⁻¹AP represents the same transformation T, but described using B-coordinates instead of standard coordinates. The operation is: convert from B to standard (multiply by P), apply T (multiply by A), then convert back to B (multiply by P⁻¹). The result encodes the same geometric action — only the coordinate system used to describe it has changed. This is the definition of matrix similarity: similar matrices represent the same transformation in different bases."

- question: "Two matrices A and B are similar (B = P⁻¹AP for some invertible P). What is the most precise statement about their relationship?"
  type: multiple-choice
  options:
    - "A and B encode the same linear transformation relative to different coordinate systems"
    - "A and B are identical up to rounding error"
    - "A and B have the same entries but in a different order"
    - "A and B define the same transformation only when applied to the same vector"
  answer: 0
  explanation: "Similar matrices are literally different matrices — their entries differ. What they share is that they represent the same underlying linear transformation, just expressed in different bases. This is why similar matrices have identical eigenvalues, determinants, and trace: these are properties of the transformation itself, which doesn't change when you relabel your coordinate system."

- question: "Changing the basis changes the underlying linear transformation that a matrix represents."
  type: true-false
  answer: false
  explanation: "Changing basis changes only the representation of the transformation — the matrix of numbers — not the transformation itself. The transformation T still acts the same way on vectors; we have just switched the coordinate language used to describe it. This is why similar matrices share eigenvalues, determinants, and rank: those are properties of T, not of the particular coordinate system chosen."

- question: "Similar matrices always have the same eigenvalues, because they represent the same linear transformation."
  type: true-false
  answer: true
  explanation: "Eigenvalues are intrinsic properties of the linear transformation, not of the coordinate representation. If B = P⁻¹AP, then det(B − λI) = det(P⁻¹AP − λI) = det(P⁻¹(A − λI)P) = det(A − λI), so A and B have identical characteristic polynomials and therefore identical eigenvalues. This is a direct consequence of similar matrices encoding the same transformation."

- question: "Why is the change-of-basis formula A' = P⁻¹AP rather than PAP⁻¹? Walk through the logic of the three operations."
  type: short-answer
  answer: "To compute the matrix of T in basis B, you need to: (1) start with a B-coordinate vector and convert it to standard coordinates — multiply by P; (2) apply the transformation T in standard coordinates — multiply by A; (3) convert the result back to B coordinates — multiply by P⁻¹. Reading right to left, the composition is P⁻¹(A(Pv_B)), giving A' = P⁻¹AP. The order matters: you must convert in before applying T, and convert out after."
  explanation: "The formula PAP⁻¹ would convert from standard to B first, then apply A, then convert back — which doesn't correspond to a meaningful B-basis description of T. The correct order follows the flow: B-coordinates → standard → apply T → back to B, which is P⁻¹AP."
```

## Explainer

From your prerequisites, you know that a **linear transformation** can be represented as a matrix — but only once you fix a basis. The matrix depends on which basis you use. The same transformation looks different in different coordinate systems, just as the same city can be described by different GPS coordinate systems. **Change of basis** is the translation dictionary between those coordinate systems.

Here's the concrete setup. Suppose B = {b₁, b₂} is a basis for ℝ², and a vector v has B-coordinates [v]_B = (3, 1) — meaning v = 3b₁ + b₂. To express v in the standard basis, multiply the B-coordinates by the matrix whose columns are b₁ and b₂. This matrix is sometimes written P or [B]. To go the other direction — from standard coordinates to B-coordinates — multiply by P⁻¹. This is why **matrix inverses** are a hard prerequisite: the reverse conversion requires the inverse to exist, which is guaranteed when B is a basis (the columns are linearly independent, so the matrix is invertible).

Now consider how a linear transformation T is affected. If A is the matrix of T in the standard basis, then to work with T using B-coordinates you must: convert from B to standard (multiply by P), apply T (multiply by A), then convert back to B (multiply by P⁻¹). The combined operation is P⁻¹AP. This is called the matrix of T **relative to basis B**, often written A'. The relationship A' = P⁻¹AP defines **matrix similarity** — two matrices are similar if one can be obtained from the other by this conjugation. Similar matrices represent the same linear transformation; they only differ in the choice of coordinate system.

The real power of change of basis is revealed by **diagonalization**, which you'll study next. Many transformations become diagonal matrices in a cleverly chosen basis — and diagonal matrices are trivial to work with (powers, exponentials, eigenvalue computations all become entry-wise operations). The eigenvectors of T form exactly this special basis. So the sequence of ideas is: find eigenvalues and eigenvectors → form P from eigenvectors → compute A' = P⁻¹AP → get a diagonal matrix that represents the same transformation far more simply. Change of basis is the bridge from a complicated matrix to its simplest equivalent form.
