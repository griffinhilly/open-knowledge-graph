---
id: convergence-iterative-methods
title: Convergence of Iterative Methods
domain: mathematics
course: numerical-analysis
prerequisites:
- id: successive-over-relaxation
  type: soft
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- power-method-eigenvalues
tags:
- convergence
- iterative-methods
- spectral-radius
stage: formal-systems
status: validated
---

# Convergence of Iterative Methods

## Core Idea
For iterative methods like Jacobi and Gauss-Seidel, convergence occurs if and only if the spectral radius (largest absolute eigenvalue) of the iteration matrix is less than 1. The spectral radius determines the asymptotic convergence rate: smaller spectral radius means faster convergence. This theorem connects linear algebra to iterative algorithm design.

## How It's Best Learned
For simple 2×2 systems, compute the iteration matrix and its eigenvalues, predicting convergence behavior analytically and comparing to numerical results.

## Common Misconceptions
- Thinking diagonal dominance guarantees fast convergence; it only guarantees convergence, possibly slowly.
- Confusing spectral radius with condition number; they measure different aspects of matrix behavior.

## Questions

```yaml
- question: "An engineer runs Jacobi iteration on a diagonally dominant system with condition number 50,000. After 200 iterations, convergence is extremely slow. They conclude the large condition number is preventing convergence. What is wrong with this diagnosis?"
  type: multiple-choice
  options:
    - "Jacobi iteration only applies to symmetric matrices, making diagonal dominance irrelevant"
    - "The condition number measures sensitivity of the solution to data perturbations, not convergence speed — the spectral radius of the iteration matrix, which may be close to 1, determines convergence rate"
    - "200 iterations is simply insufficient; diagonal dominance guarantees convergence but requires at least 1,000 iterations"
    - "Diagonal dominance guarantees fast convergence for Jacobi, so the slow convergence must be a software error"
  answer: 1
  explanation: "The condition number κ(A) measures how sensitively the solution responds to small changes in input data — a property of the original system, not the iteration process. The spectral radius ρ(M) of the iteration matrix determines whether and how fast the iterative method converges. Diagonal dominance guarantees ρ(M) < 1 (convergence is assured), but the spectral radius might be 0.99 — painfully slow. The fix is to reduce ρ(M) through better methods like SOR, not to blame the condition number."

- question: "For the iterative scheme x^(k+1) = Mx^(k) + c, which condition is BOTH necessary AND sufficient for convergence from any starting point?"
  type: multiple-choice
  options:
    - "M is symmetric positive definite"
    - "The spectral radius ρ(M) = max|λ_i| < 1"
    - "A is strictly diagonally dominant"
    - "The condition number κ(A) < 10"
  answer: 1
  explanation: "ρ(M) < 1 is the necessary and sufficient condition. The error satisfies e^(k+1) = Me^(k), so e^(k) = M^k e^(0). Decomposing in the eigenvector basis, each component decays as λ_i^k. All components vanish if and only if all |λ_i| < 1, i.e., ρ(M) < 1. Symmetric positive definiteness and diagonal dominance are sufficient in specific contexts but not necessary. The condition number concerns A, not the iteration matrix M, and is irrelevant to whether iteration converges."

- question: "If the spectral radius of an iteration matrix is 0.5, the error after 20 iterations is approximately 10^(−6) of the initial error."
  type: true-false
  answer: true
  explanation: "Error decays geometrically: after k iterations, error ≈ ρ(M)^k × initial error. With ρ = 0.5 and k = 20: 0.5^20 = 1/2^20 ≈ 9.5 × 10^(−7) ≈ 10^(−6). Compare with ρ = 0.9: 0.9^20 ≈ 0.12, barely reduced after 20 steps. The spectral radius is the right tool precisely because this geometric decay rate is what practitioners care about when choosing or tuning iterative methods."

- question: "The spectral radius of the iteration matrix and the condition number of A both measure the same underlying property — how difficult a linear system is to solve."
  type: true-false
  answer: false
  explanation: "They measure completely different things. The condition number κ(A) = ‖A‖·‖A^(−1)‖ measures how sensitively the solution responds to small perturbations in the input — relevant when you care about accuracy of a solution you already have. The spectral radius ρ(M) measures whether and how fast the iterative scheme converges — relevant when you care about the iteration process. A system can have a large condition number but a small spectral radius (converges fast, but the solution is sensitive to noise), or vice versa."

- question: "Why is the spectral radius of the iteration matrix, rather than the condition number of A, the correct tool for predicting whether an iterative method converges?"
  type: short-answer
  answer: "The iteration generates error vectors satisfying e^(k+1) = M·e^(k), so e^(k) = M^k·e^(0). For the error to vanish, M^k must go to zero — which happens if and only if all eigenvalues of M satisfy |λ| < 1, i.e., ρ(M) < 1. The condition number κ(A) concerns the original matrix A and measures solution sensitivity to input perturbations — a completely different question. The iteration matrix M is derived from A but is a separate object, and its eigenvalues govern the iterative dynamics entirely."
  explanation: "This distinction separates two concerns: (1) once you have a solution, how accurate is it given noisy input? — answered by the condition number; (2) will the iterative process reach a solution and how fast? — answered by the spectral radius of M. A common error is using the condition number as a general proxy for 'difficulty.' For iterative solvers, the spectral radius is the correct diagnostic — and it points toward the right remedies, like SOR, that actually reduce ρ(M)."
```

## Explainer

When you solve a linear system Ax = b by an iterative method like Jacobi or Gauss-Seidel, you start with a guess and refine it step by step rather than solving directly. Each iterative method rewrites the update as x^(k+1) = Mx^(k) + c for some **iteration matrix** M derived from A. Whether the iteration converges to the true solution x* depends entirely on the eigenvalues of M — your core prerequisite.

The key quantity is the **spectral radius** ρ(M), defined as the largest absolute eigenvalue: ρ(M) = max |λᵢ|. The theorem states that the iteration converges for any starting point if and only if ρ(M) < 1. Here's the intuition: the error e^(k) = x^(k) − x* satisfies e^(k+1) = Me^(k). After k steps, e^(k) = Mᵏe^(0). Decompose the initial error in the eigenvector basis: e^(0) = c₁v₁ + c₂v₂ + ... Then Mᵏe^(0) = c₁λ₁ᵏv₁ + c₂λ₂ᵏv₂ + .... If every |λᵢ| < 1, every term shrinks to zero and the error vanishes. If any |λᵢ| ≥ 1, the error in that eigenvector direction stays constant or grows — no convergence.

The **convergence rate** is geometric with ratio ρ(M): after k iterations, the error magnitude is proportional to ρ(M)^k times the initial error. A spectral radius of 0.9 reduces error by 10% per step — after 100 steps, the error is (0.9)^100 ≈ 0.000027 of the original. A spectral radius of 0.5 converges far faster: (0.5)^20 ≈ 10⁻⁶ after only 20 steps. This is why the spectral radius is the right measure of convergence speed, not the condition number (which measures how sensitive the solution is to perturbations in the data — a different property entirely).

Diagonally dominant matrices guarantee ρ(M) < 1 for both Jacobi and Gauss-Seidel — convergence is assured. But the spectral radius might be close to 1, meaning convergence could be slow. Successive over-relaxation (SOR) introduces a tunable parameter ω to try to push the spectral radius lower, and for certain structured problems (like those arising from elliptic PDEs on a grid), the optimal ω can be computed analytically, yielding spectacular speedups. The entire framework for choosing and analyzing iterative linear solvers — which method converges, how fast, and how to accelerate it — reduces to computing or bounding the spectral radius of the iteration matrix.
