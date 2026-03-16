---
id: numerical-least-squares
title: Numerical Least Squares
domain: mathematics
course: numerical-analysis
prerequisites:
- id: linear-regression
  type: soft
- id: matrix-operations
  type: hard
tags:
- least-squares
- linear-regression
- overdetermined
stage: abstract-reasoning
status: draft
---

# Numerical Least Squares

## Core Idea
Least squares solves overdetermined systems Ax = b (more equations than unknowns) by minimizing ‖Ax - b‖². The normal equations A^T Ax = A^T b can be ill-conditioned; stable alternatives use QR decomposition or SVD. Understanding numerical least squares is critical for robust data fitting and statistical applications.

## How It's Best Learned
Implement least squares using both normal equations and QR decomposition on an overdetermined system, comparing accuracy and conditioning.

## Common Misconceptions
- Thinking normal equations are always acceptable; large condition number of A^T A can destroy accuracy.
- Assuming any orthogonal factorization works equally well; QR and SVD have different numerical properties.

## Explainer

From **linear regression**, you know the goal: given n data points and a model with p parameters, find the parameters that minimize the sum of squared residuals. The matrix formulation makes this precise. Arrange your data into a matrix A (n × p, with n > p rows of input features) and a vector b (n observations). You want to find x such that Ax ≈ b, but because you have more equations than unknowns, no exact solution exists — the system is **overdetermined**. The least squares solution minimizes ‖Ax − b‖², the sum of squared differences between predictions and observations.

From **matrix operations**, you know about projections. The least squares solution x* satisfies: Ax* is the projection of b onto the column space of A. Geometrically, the residual b − Ax* is orthogonal to every column of A. Writing this orthogonality condition gives AᵀA x = Aᵀb — the **normal equations**. This derivation is elegant, and for well-conditioned problems it works fine. The normal equations can be solved with Gaussian elimination, giving an O(p³ + np²) algorithm.

The numerical trap is that forming AᵀA squares the condition number: κ(AᵀA) = κ(A)². If A already has condition number 10⁴, then AᵀA has condition number 10⁸ — and solving the normal equations loses 8 digits of accuracy in double precision. The alternative is **QR decomposition**: factor A = QR where Q is orthogonal (Qᵀ = Q⁻¹) and R is upper triangular. Because ‖Ax − b‖² = ‖QRx − b‖² = ‖Rx − Qᵀb‖² (orthogonal transformations preserve lengths), the least squares problem reduces to solving the triangular system Rx = Qᵀb — no squaring of the condition number. QR via Householder reflections is the standard numerically stable method.

**Singular value decomposition (SVD)** goes further still: A = UΣVᵀ, where the least squares solution is x* = VΣ⁺Uᵀb (Σ⁺ replaces each nonzero singular value σᵢ with 1/σᵢ). SVD handles rank-deficient A gracefully — if some columns are nearly linearly dependent, small singular values signal this, and truncating them (setting their reciprocals to zero) gives a regularized solution. SVD costs more than QR but provides the most complete numerical diagnosis: the singular values directly reveal how ill-conditioned the problem is, and the pseudoinverse gives the minimum-norm solution when the solution is not unique.
