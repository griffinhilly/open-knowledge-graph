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
