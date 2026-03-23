---
id: orthogonal-projections-least-squares
title: Orthogonal Projections and Least Squares Approximation
domain: mathematics
course: linear-algebra
prerequisites:
- id: gram-schmidt-orthogonalization
  type: hard
builds-toward:
- linear-regression
tags:
- projection
- least-squares
- approximation
stage: formal-systems
status: validated
---

# Orthogonal Projections and Least Squares Approximation

## Core Idea
The orthogonal projection of b onto a subspace W is proj_W(b), the point in W closest to b. For orthonormal basis {u₁, ..., uₖ}, proj_W(b) = Σ⟨b,uᵢ⟩uᵢ. For subspace spanned by columns of A, proj_W(b) = A(AᵀA)⁻¹Aᵀb. Least squares minimizes ||Ax − b||²; the optimal solution x* satisfies the normal equations AᵀAx* = Aᵀb, found via projection.

## Questions

```yaml
- question: "A student is told the least-squares solution x* minimizes ||Ax − b||². She concludes that Ax* must equal b. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "There is no error — minimizing the squared error means the minimum value is zero"
    - "Ax* is the orthogonal projection of b onto the column space of A, which equals b only if b already lies in that column space"
    - "She confused the row space with the column space of A"
    - "Minimizing ||Ax − b||² requires calculus, not linear algebra"
  answer: 1
  explanation: "The least-squares problem arises precisely when Ax = b has no exact solution — meaning b lies outside the column space of A. The minimizer x* gives Ax* = proj_{col(A)}(b), the closest point to b in col(A). This point is not equal to b unless b happens to be in col(A) already. The minimum value of ||Ax − b||² is the squared distance from b to its projection, not zero."

- question: "When does the least-squares problem Ax = b have a unique solution x* = (AᵀA)⁻¹Aᵀb?"
  type: multiple-choice
  options:
    - "When b lies in the column space of A"
    - "When A is a square matrix"
    - "When A has linearly independent columns, ensuring AᵀA is invertible"
    - "When the rows of A are orthonormal"
  answer: 2
  explanation: "Linear independence of the columns of A is precisely the condition that makes AᵀA invertible, giving a unique minimizer x*. Option A describes when the exact solution exists (Ax = b is consistent), not when least squares is unique. Option B is insufficient — a square singular matrix has linearly dependent columns and AᵀA is still not invertible."

- question: "The normal equations AᵀAx = Aᵀb arise because we want the residual vector b − Ax* to be perpendicular to the column space of A."
  type: true-false
  answer: true
  explanation: "This is the geometric heart of least squares. The closest point in a subspace to b is the point where the error vector is orthogonal to the subspace. 'Perpendicular to every column of A' means Aᵀ(b − Ax*) = 0, which rearranges directly to AᵀAx* = Aᵀb — the normal equations. The word 'normal' in 'normal equations' refers to this perpendicularity condition."

- question: "The projection matrix P = A(AᵀA)⁻¹Aᵀ satisfies P² = P because applying the projection twice is equivalent to applying it once."
  type: true-false
  answer: true
  explanation: "Once a vector is projected onto a subspace, the result already lies in that subspace. Projecting it again does not move it. Algebraically: P² = A(AᵀA)⁻¹Aᵀ · A(AᵀA)⁻¹Aᵀ = A(AᵀA)⁻¹(AᵀA)(AᵀA)⁻¹Aᵀ = A(AᵀA)⁻¹Aᵀ = P. This idempotent property P² = P, together with symmetry Pᵀ = P, completely characterizes orthogonal projection matrices."

- question: "Explain geometrically why the least-squares solution minimizes ||Ax − b||²."
  type: short-answer
  answer: "The set of all vectors of the form Ax (as x varies over all vectors) is the column space of A. The problem asks: which point in col(A) is closest to b? The closest point to b in any subspace is its orthogonal projection onto that subspace — the unique point where the error vector b − Ax* is perpendicular to the entire subspace. Minimizing the squared distance ||Ax − b||² is equivalent to finding this projection. The normal equations encode the perpendicularity condition: Aᵀ(b − Ax*) = 0."
  explanation: "This geometric view unifies the algebra. The normal equations are not an arbitrary algebraic trick — they encode exactly one geometric condition: the error must be orthogonal to the subspace we're projecting onto. This is why least squares appears everywhere from linear regression to signal processing: in each case, you want the best approximation to something you can't represent exactly, and orthogonal projection gives the unique closest point."
```

## Explainer

From Gram-Schmidt, you know how to convert a basis into an **orthonormal basis** — a set of mutually perpendicular unit vectors. Orthogonal projections are what makes those orthonormal bases so powerful. The idea is geometric: given a vector **b** and a subspace W, the **orthogonal projection** proj_W(**b**) is the unique point in W that is closest to **b**. "Closest" means the error vector **b** − proj_W(**b**) is perpendicular to every vector in W.

When W has an orthonormal basis {**u**₁, ..., **u**_k}, the projection formula is remarkably clean: proj_W(**b**) = Σ⟨**b**, **u**ᵢ⟩**u**ᵢ. Each term ⟨**b**, **u**ᵢ⟩**u**ᵢ is the shadow of **b** onto one basis direction, and the full projection just sums these shadows. This works because orthonormality decouples the directions — there is no "cross-talk" between basis vectors, so you can handle each coordinate independently. This is exactly what Gram-Schmidt was buying you all along.

Least squares is what happens when you want to solve **Ax = b** but no exact solution exists — the right-hand side **b** lies outside the column space of A. Since you cannot hit **b** exactly, the best you can do is find the **x** that makes **Ax** as close to **b** as possible. The closest point in the column space of A to **b** is exactly the orthogonal projection of **b** onto that column space. The minimizer x* satisfies the **normal equations** AᵀAx* = Aᵀb, which you obtain by projecting **b** onto col(A). When A has linearly independent columns, AᵀA is invertible and x* = (AᵀA)⁻¹Aᵀb uniquely.

The matrix P = A(AᵀA)⁻¹Aᵀ is called the **projection matrix** (or hat matrix in statistics). It satisfies P² = P (applying the projection twice gives the same result) and Pᵀ = P (it is symmetric). These two properties — **idempotent** and symmetric — completely characterize orthogonal projection matrices. Any time you see a matrix satisfying P² = P and Pᵀ = P, you know it is projecting onto some subspace. Least squares is ubiquitous: it underlies linear regression, Fourier series approximation, and signal processing, wherever you need the best approximation to something you cannot represent exactly.
