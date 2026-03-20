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
status: draft
---

# Convergence of Iterative Methods

## Core Idea
For iterative methods like Jacobi and Gauss-Seidel, convergence occurs if and only if the spectral radius (largest absolute eigenvalue) of the iteration matrix is less than 1. The spectral radius determines the asymptotic convergence rate: smaller spectral radius means faster convergence. This theorem connects linear algebra to iterative algorithm design.

## How It's Best Learned
For simple 2×2 systems, compute the iteration matrix and its eigenvalues, predicting convergence behavior analytically and comparing to numerical results.

## Common Misconceptions
- Thinking diagonal dominance guarantees fast convergence; it only guarantees convergence, possibly slowly.
- Confusing spectral radius with condition number; they measure different aspects of matrix behavior.

## Explainer

When you solve a linear system Ax = b by an iterative method like Jacobi or Gauss-Seidel, you start with a guess and refine it step by step rather than solving directly. Each iterative method rewrites the update as x^(k+1) = Mx^(k) + c for some **iteration matrix** M derived from A. Whether the iteration converges to the true solution x* depends entirely on the eigenvalues of M — your core prerequisite.

The key quantity is the **spectral radius** ρ(M), defined as the largest absolute eigenvalue: ρ(M) = max |λᵢ|. The theorem states that the iteration converges for any starting point if and only if ρ(M) < 1. Here's the intuition: the error e^(k) = x^(k) − x* satisfies e^(k+1) = Me^(k). After k steps, e^(k) = Mᵏe^(0). Decompose the initial error in the eigenvector basis: e^(0) = c₁v₁ + c₂v₂ + ... Then Mᵏe^(0) = c₁λ₁ᵏv₁ + c₂λ₂ᵏv₂ + .... If every |λᵢ| < 1, every term shrinks to zero and the error vanishes. If any |λᵢ| ≥ 1, the error in that eigenvector direction stays constant or grows — no convergence.

The **convergence rate** is geometric with ratio ρ(M): after k iterations, the error magnitude is proportional to ρ(M)^k times the initial error. A spectral radius of 0.9 reduces error by 10% per step — after 100 steps, the error is (0.9)^100 ≈ 0.000027 of the original. A spectral radius of 0.5 converges far faster: (0.5)^20 ≈ 10⁻⁶ after only 20 steps. This is why the spectral radius is the right measure of convergence speed, not the condition number (which measures how sensitive the solution is to perturbations in the data — a different property entirely).

Diagonally dominant matrices guarantee ρ(M) < 1 for both Jacobi and Gauss-Seidel — convergence is assured. But the spectral radius might be close to 1, meaning convergence could be slow. Successive over-relaxation (SOR) introduces a tunable parameter ω to try to push the spectral radius lower, and for certain structured problems (like those arising from elliptic PDEs on a grid), the optimal ω can be computed analytically, yielding spectacular speedups. The entire framework for choosing and analyzing iterative linear solvers — which method converges, how fast, and how to accelerate it — reduces to computing or bounding the spectral radius of the iteration matrix.
