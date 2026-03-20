---
id: qr-algorithm
title: QR Algorithm
domain: mathematics
course: numerical-analysis
prerequisites:
- id: power-method-eigenvalues
  type: hard
tags:
- qr-algorithm
- eigenvalues
- qr-decomposition
stage: formal-systems
status: draft
---

# QR Algorithm

## Core Idea
The QR algorithm iteratively computes QR decomposition A_k = Q_k R_k and sets A_{k+1} = R_k Q_k, creating a sequence similar to A_k. This sequence converges to a Schur form (upper triangular for real matrices), revealing all eigenvalues on the diagonal. The QR algorithm is highly efficient, stable, and the foundation of modern eigenvalue solvers.

## Explainer

The power method you already know is conceptually elegant: multiply by A repeatedly, normalize, and converge to the dominant eigenvector. But it has a critical limitation — it finds only the largest eigenvalue. If you want all eigenvalues of a matrix, you need a different strategy. The **QR algorithm** applies a sequence of similarity transformations to the entire matrix until it converges to a form that reveals all eigenvalues at once.

The algorithm's core iteration is: factor A_k = Q_k R_k (QR decomposition: Q orthogonal, R upper triangular), then set A_{k+1} = R_k Q_k (swap the factors). Notice that A_{k+1} = R_k Q_k = Q_k^T A_k Q_k, since A_k = Q_k R_k implies R_k = Q_k^T A_k. So A_{k+1} is *similar* to A_k — they have identical eigenvalues, just in a different basis. The sequence A₀, A₁, A₂, ... all share the same eigenvalues. What changes is the structure: off-diagonal entries diminish, and the sequence converges to an **upper triangular (Schur) form** with eigenvalues on the diagonal.

Why does convergence happen? The intuition connects directly to the power method. Each QR iteration implicitly runs the power method on multiple invariant subspaces simultaneously. The subspace spanned by the first k columns of Q₁Q₂···Qₙ converges toward the invariant subspace corresponding to the k largest eigenvalues (by magnitude). The QR factorization is the mechanism for extracting this subspace information orthogonally at every step — think of it as running the power method on all eigenspaces at once while keeping them orthogonal to each other.

In practice, two refinements make the algorithm efficient. First, reduce A to **Hessenberg form** (upper triangular plus one subdiagonal) before iteration; this makes each QR factorization cost O(n²) instead of O(n³). Second, introduce **shifts**: apply QR to (A_k − σI) where σ is chosen to approximate an eigenvalue (e.g., the bottom-right entry). Shifts accelerate convergence from linear to cubic near the end of each deflation step. With both refinements, the QR algorithm finds all eigenvalues of an n×n matrix in O(n³) operations with excellent numerical stability — it is the algorithm behind the `eig` function in every numerical computing environment.
