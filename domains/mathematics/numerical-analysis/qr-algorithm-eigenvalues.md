---
id: qr-algorithm-eigenvalues
title: QR Algorithm for Eigenvalues
domain: mathematics
course: numerical-analysis
prerequisites:
- id: power-method-eigenvalues
  type: soft
tags:
- qr-algorithm
- eigenvalue-algorithm
- convergence
stage: advanced
status: draft
---

# QR Algorithm for Eigenvalues

## Core Idea
The QR algorithm repeatedly factors A_k = Q_k R_k and sets A_{k+1} = R_k Q_k, preserving eigenvalues while converging to upper triangular form with eigenvalues on the diagonal. This method is more robust than power method, converging to all eigenvalues simultaneously. Shifted and Hessenberg variants improve efficiency.

## Explainer

You've likely studied the **power method**, which finds the dominant eigenvalue by repeatedly multiplying a matrix by a vector and normalizing. It finds one eigenvalue at a time and requires the dominant eigenvalue to be strictly largest in magnitude. The QR algorithm is a profound generalization: it finds *all* eigenvalues simultaneously and converges even for matrices with multiple or complex eigenvalues. Understanding why it works reveals deep connections between orthogonality, similarity transformations, and subspace iteration.

The algorithm is deceptively simple to state. Start with A₀ = A; then at each step, compute the **QR factorization** Aₖ = QₖRₖ (Q orthogonal, R upper triangular), and form the next iterate Aₖ₊₁ = RₖQₖ (note the reversed order). The critical observation is that Aₖ₊₁ = RₖQₖ = Qₖᵀ(QₖRₖ)Qₖ = Qₖᵀ AₖQₖ, so each iteration is an **orthogonal similarity transformation** — it preserves all eigenvalues while rotating the basis. The sequence {Aₖ} therefore has the same eigenvalues as A at every step but converges (under mild conditions on eigenvalue separations) to upper triangular form, with eigenvalues appearing on the diagonal. This target is called the **Schur form**.

Why does it converge? Intuitively, the QR iteration is equivalent to simultaneously applying the power method to each column of the identity matrix, then re-orthogonalizing at each step. The dominant eigenvector is captured first (the top-left entry stabilizes to λ₁), then the next, and so on. This can be made precise: the QR iteration implicitly performs simultaneous iteration on a nested sequence of **Krylov subspaces**, and its convergence rate is geometric with ratio |λᵢ₊₁/λᵢ| for adjacent eigenvalues — close eigenvalues converge slowly.

Practical implementations use two key optimizations that transform the naive O(n³ × iterations) cost to O(n³) total. First, A is pre-reduced to **upper Hessenberg form** (zero below the first subdiagonal) using Householder reflectors — a one-time O(n³) operation that makes each subsequent QR step O(n²) instead of O(n³). Second, **shifts** are applied: rather than factoring Aₖ, one factors Aₖ − σₖI for a carefully chosen shift σₖ near an eigenvalue, which dramatically accelerates convergence near that eigenvalue. The **Francis double-step shift** applies two shifts implicitly in a single real arithmetic step, achieving near-cubic convergence without ever forming complex matrices. These optimizations make the QR algorithm the standard method for dense eigenvalue computation, embedded in LAPACK and behind MATLAB's `eig` function.
