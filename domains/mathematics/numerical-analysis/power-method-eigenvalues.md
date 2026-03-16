---
id: power-method-eigenvalues
title: Power Method for Eigenvalues
domain: mathematics
course: numerical-analysis
prerequisites:
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- qr-algorithm
tags:
- power-method
- eigenvalues
- iteration
stage: abstract-reasoning
status: draft
---

# Power Method for Eigenvalues

## Core Idea
The power method finds the largest (in absolute value) eigenvalue and its eigenvector by repeatedly multiplying a random vector by the matrix: v^{(k+1)} = Av^{(k)} / ‖Av^{(k)}‖. Convergence is geometric with rate determined by the ratio of the two largest eigenvalues. Simple to implement, the power method is practical for large sparse matrices but slow when eigenvalues are close.

## Explainer

You already know that eigenvalues and eigenvectors satisfy Av = λv: multiplying a matrix by its eigenvector just scales that vector by λ. The power method exploits this property directly. Start with any random vector v⁰, multiply repeatedly by A, and normalize after each step. After many iterations, the direction of v^(k) converges to the **dominant eigenvector** — the eigenvector corresponding to the largest absolute eigenvalue λ₁.

The reason this works becomes clear when you decompose the starting vector in the eigenvector basis. Write v⁰ = c₁v₁ + c₂v₂ + ... + cₙvₙ. After k applications of A: Aᵏv⁰ = c₁λ₁ᵏv₁ + c₂λ₂ᵏv₂ + ... = λ₁ᵏ(c₁v₁ + c₂(λ₂/λ₁)ᵏv₂ + ...). Since |λ₂/λ₁| < 1 (λ₁ is strictly dominant), every term except the first shrinks to zero. The iteration is dominated by the v₁ component, which is exactly the eigenvector you want. The normalization at each step prevents the vector from growing to infinity or shrinking to zero — it keeps the direction visible.

The **convergence rate** is |λ₂/λ₁|: the ratio of the second-largest to the largest eigenvalue. If this ratio is small (eigenvalues well-separated), convergence is fast. If it is close to 1 (eigenvalues nearly equal), convergence is very slow — the second component decays slowly and the iteration must work longer to wash it out. The **Rayleigh quotient** μ = (v^(k))ᵀ A v^(k) / (v^(k))ᵀ v^(k) gives an estimate of λ₁ at each step and converges quadratically once the eigenvector direction is approximately right.

For large sparse matrices from real applications — finite element models, network graphs, Google's PageRank — A might be millions by millions, but applying A to a vector is cheap (only the nonzero entries matter). This is where the power method shines: each iteration requires only a single matrix-vector multiply. The method can be extended via **deflation**: once λ₁ and v₁ are found, project out v₁ from the matrix and apply the method again to find the next eigenvalue. The QR algorithm — a much more sophisticated technique — can be understood in part as a way of applying power-method logic to all eigenvalues simultaneously and efficiently.
