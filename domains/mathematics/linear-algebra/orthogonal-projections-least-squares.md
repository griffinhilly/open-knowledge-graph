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
status: draft
---

# Orthogonal Projections and Least Squares Approximation

## Core Idea
The orthogonal projection of b onto a subspace W is proj_W(b), the point in W closest to b. For orthonormal basis {u₁, ..., uₖ}, proj_W(b) = Σ⟨b,uᵢ⟩uᵢ. For subspace spanned by columns of A, proj_W(b) = A(AᵀA)⁻¹Aᵀb. Least squares minimizes ||Ax − b||²; the optimal solution x* satisfies the normal equations AᵀAx* = Aᵀb, found via projection.

## Explainer

From Gram-Schmidt, you know how to convert a basis into an **orthonormal basis** — a set of mutually perpendicular unit vectors. Orthogonal projections are what makes those orthonormal bases so powerful. The idea is geometric: given a vector **b** and a subspace W, the **orthogonal projection** proj_W(**b**) is the unique point in W that is closest to **b**. "Closest" means the error vector **b** − proj_W(**b**) is perpendicular to every vector in W.

When W has an orthonormal basis {**u**₁, ..., **u**_k}, the projection formula is remarkably clean: proj_W(**b**) = Σ⟨**b**, **u**ᵢ⟩**u**ᵢ. Each term ⟨**b**, **u**ᵢ⟩**u**ᵢ is the shadow of **b** onto one basis direction, and the full projection just sums these shadows. This works because orthonormality decouples the directions — there is no "cross-talk" between basis vectors, so you can handle each coordinate independently. This is exactly what Gram-Schmidt was buying you all along.

Least squares is what happens when you want to solve **Ax = b** but no exact solution exists — the right-hand side **b** lies outside the column space of A. Since you cannot hit **b** exactly, the best you can do is find the **x** that makes **Ax** as close to **b** as possible. The closest point in the column space of A to **b** is exactly the orthogonal projection of **b** onto that column space. The minimizer x* satisfies the **normal equations** AᵀAx* = Aᵀb, which you obtain by projecting **b** onto col(A). When A has linearly independent columns, AᵀA is invertible and x* = (AᵀA)⁻¹Aᵀb uniquely.

The matrix P = A(AᵀA)⁻¹Aᵀ is called the **projection matrix** (or hat matrix in statistics). It satisfies P² = P (applying the projection twice gives the same result) and Pᵀ = P (it is symmetric). These two properties — **idempotent** and symmetric — completely characterize orthogonal projection matrices. Any time you see a matrix satisfying P² = P and Pᵀ = P, you know it is projecting onto some subspace. Least squares is ubiquitous: it underlies linear regression, Fourier series approximation, and signal processing, wherever you need the best approximation to something you cannot represent exactly.
