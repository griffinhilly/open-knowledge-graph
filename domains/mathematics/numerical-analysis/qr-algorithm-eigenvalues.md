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

## Questions

```yaml
- question: "At each step of the QR algorithm, matrix A_k is factored as A_k = Q_k R_k and the next iterate is formed. Which expression correctly gives A_{k+1}, and why does this choice preserve eigenvalues?"
  type: multiple-choice
  options:
    - "A_{k+1} = Q_k R_k, because repeating the factorization maintains the matrix structure"
    - "A_{k+1} = R_k Q_k, because this equals Q_k^T A_k Q_k — an orthogonal similarity transformation"
    - "A_{k+1} = Q_k^T R_k, because transposing Q restores symmetry"
    - "A_{k+1} = R_k^T Q_k, because reversing both factors ensures convergence"
  answer: 1
  explanation: "The reversed product A_{k+1} = R_k Q_k is the key. Since A_k = Q_k R_k, we can write R_k Q_k = Q_k^T (Q_k R_k) Q_k = Q_k^T A_k Q_k — a similarity transformation by the orthogonal matrix Q_k. Orthogonal similarity transformations preserve all eigenvalues, so every iterate has the same spectrum as the original A. Setting A_{k+1} = Q_k R_k (option A) would just repeat the factorization without any transformation."

- question: "The naive QR algorithm without any optimizations is applied to a dense n×n matrix. What is the dominant cost bottleneck, and how do practical implementations resolve it?"
  type: multiple-choice
  options:
    - "Each QR factorization costs O(n²), which is acceptable; the bottleneck is the number of iterations needed"
    - "Each QR factorization costs O(n³), making total cost O(n³ × iterations); resolved by pre-reducing to Hessenberg form so each step costs O(n²)"
    - "Each QR factorization costs O(n log n) using FFT-based methods; shifts are applied to guarantee convergence"
    - "The bottleneck is forming Q_k explicitly; resolved by working with implicit Q representations throughout"
  answer: 1
  explanation: "A full QR factorization of a dense n×n matrix costs O(n³). With potentially O(n) iterations, the naive total cost is O(n⁴) or worse. The solution is a one-time O(n³) pre-reduction to upper Hessenberg form (zero below the first subdiagonal). Once in Hessenberg form, each subsequent QR step costs only O(n²), and with shifts ensuring rapid convergence, the total becomes O(n³). This is why practical eigensolvers (LAPACK's dgehrd/dlahqr, MATLAB's eig) always begin with Hessenberg reduction."

- question: "The QR algorithm preserves the eigenvalues of the original matrix at every iteration."
  type: true-false
  answer: true
  explanation: "Yes — this is the fundamental invariant. Each iterate A_{k+1} = R_k Q_k = Q_k^T A_k Q_k is obtained by an orthogonal similarity transformation. Orthogonal similarity transformations are a subset of general similarity transformations, which always preserve eigenvalues (since det(A - λI) = det(Q^T(A - λI)Q) = det(Q^T A Q - λI)). The sequence converges toward upper triangular (Schur) form, at which point eigenvalues appear explicitly on the diagonal — but they were there all along."

- question: "The QR algorithm converges to all eigenvalues simultaneously at the same rate, regardless of whether the eigenvalues are close to each other in magnitude."
  type: true-false
  answer: false
  explanation: "Convergence is not uniform — it is geometric with rate |λ_{i+1}/λ_i| for adjacent eigenvalues ordered by magnitude. Eigenvalues close in magnitude (|λ_{i+1}/λ_i| ≈ 1) converge very slowly. This is why shifts are critical: by subtracting a shift σ near a target eigenvalue, the relevant ratio becomes |(λ_{i+1} - σ)/(λ_i - σ)|, which can be made very small near convergence. The Francis double-step shift achieves near-cubic local convergence for this reason."

- question: "Why does the QR algorithm converge to upper triangular (Schur) form, and what does this reveal about the relationship between the QR algorithm and the power method?"
  type: short-answer
  answer: "Each QR iteration implicitly applies the power method simultaneously to all columns of the identity, then re-orthogonalizes via the QR factorization. The dominant eigenvector is captured first (the (1,1) entry converges to λ₁), then the next most dominant, and so on — deflating the problem one eigenvalue at a time. This simultaneous subspace iteration perspective shows the QR algorithm as a generalization of power iteration: instead of converging to one eigenvector, it converges to the full Schur decomposition."
  explanation: "The equivalence to simultaneous subspace (Krylov) iteration is what makes the QR algorithm conceptually deep. Power iteration with a random starting vector picks out the largest eigenvalue because repeated multiplication by A amplifies the component in the dominant eigenvector direction. The QR algorithm does the same thing for all eigenvalues at once by working with the entire orthonormal basis and re-orthogonalizing at each step. The convergence rate |λ_{i+1}/λ_i| matches power method: adjacent eigenvalues that are close in magnitude require many iterations to separate."
```

## Explainer

You've likely studied the **power method**, which finds the dominant eigenvalue by repeatedly multiplying a matrix by a vector and normalizing. It finds one eigenvalue at a time and requires the dominant eigenvalue to be strictly largest in magnitude. The QR algorithm is a profound generalization: it finds *all* eigenvalues simultaneously and converges even for matrices with multiple or complex eigenvalues. Understanding why it works reveals deep connections between orthogonality, similarity transformations, and subspace iteration.

The algorithm is deceptively simple to state. Start with A₀ = A; then at each step, compute the **QR factorization** Aₖ = QₖRₖ (Q orthogonal, R upper triangular), and form the next iterate Aₖ₊₁ = RₖQₖ (note the reversed order). The critical observation is that Aₖ₊₁ = RₖQₖ = Qₖᵀ(QₖRₖ)Qₖ = Qₖᵀ AₖQₖ, so each iteration is an **orthogonal similarity transformation** — it preserves all eigenvalues while rotating the basis. The sequence {Aₖ} therefore has the same eigenvalues as A at every step but converges (under mild conditions on eigenvalue separations) to upper triangular form, with eigenvalues appearing on the diagonal. This target is called the **Schur form**.

Why does it converge? Intuitively, the QR iteration is equivalent to simultaneously applying the power method to each column of the identity matrix, then re-orthogonalizing at each step. The dominant eigenvector is captured first (the top-left entry stabilizes to λ₁), then the next, and so on. This can be made precise: the QR iteration implicitly performs simultaneous iteration on a nested sequence of **Krylov subspaces**, and its convergence rate is geometric with ratio |λᵢ₊₁/λᵢ| for adjacent eigenvalues — close eigenvalues converge slowly.

Practical implementations use two key optimizations that transform the naive O(n³ × iterations) cost to O(n³) total. First, A is pre-reduced to **upper Hessenberg form** (zero below the first subdiagonal) using Householder reflectors — a one-time O(n³) operation that makes each subsequent QR step O(n²) instead of O(n³). Second, **shifts** are applied: rather than factoring Aₖ, one factors Aₖ − σₖI for a carefully chosen shift σₖ near an eigenvalue, which dramatically accelerates convergence near that eigenvalue. The **Francis double-step shift** applies two shifts implicitly in a single real arithmetic step, achieving near-cubic convergence without ever forming complex matrices. These optimizations make the QR algorithm the standard method for dense eigenvalue computation, embedded in LAPACK and behind MATLAB's `eig` function.
