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
stage: formal-systems
status: validated
---

# Numerical Least Squares

## Core Idea
Least squares solves overdetermined systems Ax = b (more equations than unknowns) by minimizing ‖Ax - b‖². The normal equations A^T Ax = A^T b can be ill-conditioned; stable alternatives use QR decomposition or SVD. Understanding numerical least squares is critical for robust data fitting and statistical applications.

## How It's Best Learned
Implement least squares using both normal equations and QR decomposition on an overdetermined system, comparing accuracy and conditioning.

## Common Misconceptions
- Thinking normal equations are always acceptable; large condition number of A^T A can destroy accuracy.
- Assuming any orthogonal factorization works equally well; QR and SVD have different numerical properties.

## Questions

```yaml
- question: "A numerical analyst uses the normal equations A^T A x = A^T b to solve a least squares problem. She checks and finds that A has condition number κ(A) = 10^6. What condition number should she expect for A^T A?"
  type: multiple-choice
  options:
    - "10^6 — the condition number does not change when forming A^T A"
    - "10^3 — the square root, because the matrix is now symmetric"
    - "10^12 — the condition number squares"
    - "It depends on the specific values in A"
  answer: 2
  explanation: "κ(A^T A) = κ(A)^2, so a condition number of 10^6 becomes 10^12. In double precision arithmetic (which gives about 16 significant digits), a condition number of 10^12 means you lose 12 digits of accuracy — leaving only 4 reliable digits in the solution. This squaring of the condition number is the fundamental numerical hazard of the normal equations approach, and why QR decomposition is preferred for ill-conditioned problems."

- question: "Why is QR decomposition preferred over normal equations for numerically solving least squares problems?"
  type: multiple-choice
  options:
    - "QR is always faster, making it preferred for large problems"
    - "QR avoids forming A^T A, so the condition number is not squared; orthogonal transformations preserve lengths and the problem reduces to a triangular solve"
    - "QR finds the exact solution to Ax = b, while normal equations only approximate it"
    - "QR is preferred only when A is square; for overdetermined systems, normal equations are still best"
  answer: 1
  explanation: "The key advantage of QR is numerical stability: factoring A = QR and solving Rx = Q^T b never forms A^T A, so the condition number remains κ(A) rather than κ(A)^2. Since Q is orthogonal, multiplying by Q^T is a rotation/reflection that preserves vector lengths. Both methods find the same least squares solution; QR just computes it more accurately when A is ill-conditioned. Option A is false (QR is often slower than forming normal equations for tall matrices); option D reverses the reality."

- question: "The normal equations always give an accurate least squares solution as long as A has full column rank."
  type: true-false
  answer: false
  explanation: "Full column rank guarantees A^T A is invertible and a unique solution exists, but it does not guarantee numerical accuracy. If A has a large condition number, forming A^T A squares it, amplifying rounding errors far beyond what QR would produce. The issue is purely numerical: even when the mathematical problem is well-defined, the normal equations approach can produce a computed solution far from the true solution due to floating-point error accumulation."

- question: "SVD provides the minimum-norm least squares solution when A is rank-deficient (has linearly dependent columns)."
  type: true-false
  answer: true
  explanation: "When A is rank-deficient, the least squares problem has infinitely many solutions. SVD via the pseudoinverse x* = V Σ^+ U^T b selects the one with minimum 2-norm among all solutions that minimize ‖Ax − b‖². Setting near-zero singular values' reciprocals to zero also regularizes the solution, preventing it from blowing up due to numerical rank deficiency. This is what makes SVD the most complete tool for least squares, especially in rank-deficient or near-rank-deficient cases."

- question: "Explain why the condition number of A^T A matters for the accuracy of the least squares solution, and describe a numerically stable alternative to using the normal equations."
  type: short-answer
  answer: "Solving the normal equations requires inverting (or factoring) A^T A, and accuracy degrades proportionally to its condition number. Since κ(A^T A) = κ(A)^2, a moderately ill-conditioned A can produce a disastrously ill-conditioned normal equations system, wiping out many digits of accuracy. QR decomposition avoids this: it factors A = QR directly, reducing the problem to solving Rx = Q^T b. Because Q is orthogonal (length-preserving), this transformation does not amplify errors, and the condition number of the triangular system R is κ(A), not κ(A)^2."
  explanation: "The condition number measures how much a small change in input amplifies into a change in output. For a system with condition number κ, you lose approximately log_10(κ) digits of accuracy. Squaring the condition number doubles the digit loss — catastrophic for even mildly ill-conditioned problems. QR via Householder reflections is the standard workhorse for least squares in numerical software (LAPACK's dgelsd uses QR or SVD depending on rank), precisely because it avoids this squaring."
```

## Explainer

From **linear regression**, you know the goal: given n data points and a model with p parameters, find the parameters that minimize the sum of squared residuals. The matrix formulation makes this precise. Arrange your data into a matrix A (n × p, with n > p rows of input features) and a vector b (n observations). You want to find x such that Ax ≈ b, but because you have more equations than unknowns, no exact solution exists — the system is **overdetermined**. The least squares solution minimizes ‖Ax − b‖², the sum of squared differences between predictions and observations.

From **matrix operations**, you know about projections. The least squares solution x* satisfies: Ax* is the projection of b onto the column space of A. Geometrically, the residual b − Ax* is orthogonal to every column of A. Writing this orthogonality condition gives AᵀA x = Aᵀb — the **normal equations**. This derivation is elegant, and for well-conditioned problems it works fine. The normal equations can be solved with Gaussian elimination, giving an O(p³ + np²) algorithm.

The numerical trap is that forming AᵀA squares the condition number: κ(AᵀA) = κ(A)². If A already has condition number 10⁴, then AᵀA has condition number 10⁸ — and solving the normal equations loses 8 digits of accuracy in double precision. The alternative is **QR decomposition**: factor A = QR where Q is orthogonal (Qᵀ = Q⁻¹) and R is upper triangular. Because ‖Ax − b‖² = ‖QRx − b‖² = ‖Rx − Qᵀb‖² (orthogonal transformations preserve lengths), the least squares problem reduces to solving the triangular system Rx = Qᵀb — no squaring of the condition number. QR via Householder reflections is the standard numerically stable method.

**Singular value decomposition (SVD)** goes further still: A = UΣVᵀ, where the least squares solution is x* = VΣ⁺Uᵀb (Σ⁺ replaces each nonzero singular value σᵢ with 1/σᵢ). SVD handles rank-deficient A gracefully — if some columns are nearly linearly dependent, small singular values signal this, and truncating them (setting their reciprocals to zero) gives a regularized solution. SVD costs more than QR but provides the most complete numerical diagnosis: the singular values directly reveal how ill-conditioned the problem is, and the pseudoinverse gives the minimum-norm solution when the solution is not unique.
