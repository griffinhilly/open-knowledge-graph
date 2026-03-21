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

## Questions

```yaml
- question: "In the QR algorithm, why do all iterates A₀, A₁, A₂, ... share the same eigenvalues?"
  type: multiple-choice
  options:
    - "The QR decomposition preserves eigenvalues because Q is unitary"
    - "Each A_{k+1} = R_k Q_k is similar to A_k via A_{k+1} = Q_k^T A_k Q_k, and similar matrices have identical eigenvalues"
    - "The iterates are all equal to A₀ scaled by different constants"
    - "Eigenvalues are preserved because R_k is upper triangular"
  answer: 1
  explanation: "Since A_k = Q_k R_k, we have R_k = Q_k^T A_k (because Q_k is orthogonal). Therefore A_{k+1} = R_k Q_k = Q_k^T A_k Q_k — a similarity transformation. Similar matrices represent the same linear transformation in different bases and always have identical eigenvalues. Every QR iteration is a similarity transformation, so eigenvalues are invariants of the entire sequence."

- question: "After many iterations of the QR algorithm, what form does the sequence converge toward, and what does it reveal?"
  type: multiple-choice
  options:
    - "A diagonal matrix with eigenvectors on the diagonal"
    - "A lower triangular form with eigenvalues on the sub-diagonal"
    - "An upper triangular (Schur) form with eigenvalues on the main diagonal"
    - "The zero matrix, because repeated factorization reduces all entries"
  answer: 2
  explanation: "The QR algorithm converges to an upper triangular Schur form (or block upper triangular for matrices with complex eigenvalue pairs). In this form, the eigenvalues appear on the main diagonal. The convergence is driven by the same mechanism as the power method — subspaces corresponding to dominant eigenvalues are progressively revealed — but applied simultaneously to all eigenvalues at once."

- question: "The QR algorithm can find only the largest eigenvalue of a matrix, similar to the power method."
  type: true-false
  answer: false
  explanation: "False. This is exactly the limitation the QR algorithm was designed to overcome. The power method finds only the dominant eigenvalue (largest in magnitude). The QR algorithm generalizes this: each iteration implicitly runs a power-method-like process on all invariant subspaces simultaneously, keeping them orthogonal to each other via QR factorization. The result is convergence to all eigenvalues at once — it is the algorithm behind the 'eig' function in every numerical computing environment."

- question: "Each iterate A_k in the QR algorithm is similar to the original matrix A, meaning all iterates share the same eigenvalues."
  type: true-false
  answer: true
  explanation: "True. A_{k+1} = Q_k^T A_k Q_k is a similarity transformation of A_k, so A_{k+1} is similar to A_k. By transitivity, every A_k is similar to A₀ = A. Since similar matrices have identical eigenvalues, all iterates share the same eigenvalues as A. This is the key structural guarantee of the algorithm: eigenvalues are invariants of the sequence, even as the off-diagonal entries diminish toward zero."

- question: "What property makes the step A_{k+1} = R_k Q_k the right choice in the QR algorithm, and why does this guarantee the eigenvalues are preserved?"
  type: short-answer
  answer: "Swapping factors to R_k Q_k ensures A_{k+1} is similar to A_k: since A_k = Q_k R_k and Q_k is orthogonal, R_k = Q_k^T A_k, so A_{k+1} = R_k Q_k = Q_k^T A_k Q_k — a similarity transformation. Similar matrices have identical eigenvalues, so every iterate preserves the eigenvalues of the original matrix A while the off-diagonal entries converge toward zero."
  explanation: "The insight is that similarity transformations preserve eigenvalues while changing the representation basis. By repeatedly applying QR-based similarity transformations, we drive the matrix toward a basis in which eigenvalues are revealed on the diagonal — without ever changing what those eigenvalues are."
```

## Explainer

The power method you already know is conceptually elegant: multiply by A repeatedly, normalize, and converge to the dominant eigenvector. But it has a critical limitation — it finds only the largest eigenvalue. If you want all eigenvalues of a matrix, you need a different strategy. The **QR algorithm** applies a sequence of similarity transformations to the entire matrix until it converges to a form that reveals all eigenvalues at once.

The algorithm's core iteration is: factor A_k = Q_k R_k (QR decomposition: Q orthogonal, R upper triangular), then set A_{k+1} = R_k Q_k (swap the factors). Notice that A_{k+1} = R_k Q_k = Q_k^T A_k Q_k, since A_k = Q_k R_k implies R_k = Q_k^T A_k. So A_{k+1} is *similar* to A_k — they have identical eigenvalues, just in a different basis. The sequence A₀, A₁, A₂, ... all share the same eigenvalues. What changes is the structure: off-diagonal entries diminish, and the sequence converges to an **upper triangular (Schur) form** with eigenvalues on the diagonal.

Why does convergence happen? The intuition connects directly to the power method. Each QR iteration implicitly runs the power method on multiple invariant subspaces simultaneously. The subspace spanned by the first k columns of Q₁Q₂···Qₙ converges toward the invariant subspace corresponding to the k largest eigenvalues (by magnitude). The QR factorization is the mechanism for extracting this subspace information orthogonally at every step — think of it as running the power method on all eigenspaces at once while keeping them orthogonal to each other.

In practice, two refinements make the algorithm efficient. First, reduce A to **Hessenberg form** (upper triangular plus one subdiagonal) before iteration; this makes each QR factorization cost O(n²) instead of O(n³). Second, introduce **shifts**: apply QR to (A_k − σI) where σ is chosen to approximate an eigenvalue (e.g., the bottom-right entry). Shifts accelerate convergence from linear to cubic near the end of each deflation step. With both refinements, the QR algorithm finds all eigenvalues of an n×n matrix in O(n³) operations with excellent numerical stability — it is the algorithm behind the `eig` function in every numerical computing environment.
