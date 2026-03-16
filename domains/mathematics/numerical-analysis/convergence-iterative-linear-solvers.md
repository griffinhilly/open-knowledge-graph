---
id: convergence-iterative-linear-solvers
title: Convergence of Iterative Methods
domain: mathematics
course: numerical-analysis
prerequisites:
- id: successive-over-relaxation-sor
  type: soft
- id: eigenvalues-and-eigenvectors
  type: hard
tags:
- convergence-analysis
- spectral-radius
- iteration-matrix
stage: advanced
status: draft
---

# Convergence of Iterative Methods

## Core Idea
Iterative methods for linear systems converge if and only if the spectral radius ρ(G) of the iteration matrix G is less than 1. The convergence rate depends on ρ(G); smaller spectral radius means faster convergence. Different splittings (Jacobi, Gauss-Seidel, SOR) produce different iteration matrices with different spectral radii, explaining their varying convergence speeds.

## Explainer

Every stationary iterative method for solving Ax = b can be written in the form x_{k+1} = Gx_k + c, where G is the **iteration matrix** (determined by how you split A) and c is a fixed vector. If x* is the exact solution, it satisfies x* = Gx* + c. Subtracting, the error e_k = x_k - x* evolves by e_{k+1} = G · e_k. After k iterations, e_k = G^k · e_0. Convergence means G^k → 0 as k → ∞ — the question is entirely about the powers of G.

This is where **eigenvalues** (your hard prerequisite) become decisive. Recall that if v is an eigenvector of G with eigenvalue λ, then G^k v = λ^k v. If we decompose the initial error e_0 in the eigenbasis of G (assuming G is diagonalizable), each component is multiplied by the corresponding λ^k at each step. For the error to vanish, every |λ^k| must go to zero — meaning every eigenvalue must satisfy |λ| < 1. The **spectral radius** ρ(G) = max |λ_i| is the radius of the largest eigenvalue. The theorem is clean: G^k → 0 if and only if ρ(G) < 1. If even one eigenvalue has |λ| ≥ 1, that component of the error never decays.

The convergence rate is controlled by the dominant eigenvalue. After k steps, ||e_k|| ≈ C · ρ(G)^k, a geometric decay. To reduce the error by a factor of 10, you need approximately log(10) / log(1/ρ(G)) iterations. This makes the dependence on ρ(G) very sensitive: decreasing ρ from 0.99 to 0.9 cuts the required iterations per order of magnitude from roughly 230 to 22 — a 10× speedup.

Different splittings of A produce different iteration matrices. For Jacobi, G_J uses only the diagonal of A. For Gauss-Seidel, G_GS uses the lower triangular part, incorporating newly computed values immediately. For many common problem classes (e.g., tridiagonal matrices from discretized PDEs), one can show ρ(G_GS) = ρ(G_J)², making Gauss-Seidel converge in half as many iterations as Jacobi. Successive Over-Relaxation (SOR) introduces a relaxation parameter ω to reduce ρ(G_SOR) further still. The entire art of iterative method selection is choosing a splitting that makes ρ(G) as small as possible for the structure of A at hand.
