---
id: iterative-methods-linear-systems
title: Iterative Methods for Linear Systems
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrix-norms-conditioning
  type: soft
builds-toward:
- applications-linear-algebra-modeling
tags:
- iterative-methods
- jacobi
- gauss-seidel
stage: formal-systems
status: draft
---

# Iterative Methods for Linear Systems

## Core Idea
Iterative methods like Jacobi and Gauss-Seidel solve Ax = b as a fixed-point iteration x^(k+1) = (I − D⁻¹A)x^(k) + D⁻¹b. They converge when ||I − D⁻¹A|| < 1 and are useful for sparse or large systems. Convergence rate depends on spectral radius. Conjugate gradient (CG) converges faster for symmetric positive definite matrices.

## Explainer

Direct methods for solving Ax = b — like Gaussian elimination — work well for small or dense systems, but for large, sparse systems (think: a 100,000 × 100,000 matrix where most entries are zero) they are prohibitively expensive. Gaussian elimination requires O(n³) operations and fills in the zeros during the process, destroying sparsity. **Iterative methods** exploit sparsity by never forming dense intermediate matrices — instead, they improve a current guess x^(k) toward the true solution using only matrix-vector products.

The core idea is to reformulate Ax = b as a **fixed-point problem**: find x such that x = f(x). Starting with an initial guess x^(0), you repeatedly apply x^(k+1) = f(x^(k)), hoping the sequence converges to the true solution. For **Jacobi's method**, split A into its diagonal part D and the remainder R = A − D. Then Ax = b becomes Dx = b − Rx, so x = D⁻¹(b − Rx), which directly defines the iteration x^(k+1) = D⁻¹(b − Rx^(k)). Each component of x is updated using all components from the previous iteration. **Gauss-Seidel** improves on this by using the most recently updated values immediately: as soon as x₁^(k+1) is computed, it is used when computing x₂^(k+1), and so on. This typically accelerates convergence without any extra cost.

Whether these iterations converge depends on the structure of the matrix. The key quantity is the **spectral radius** ρ(M) of the iteration matrix M = I − D⁻¹A — the largest absolute eigenvalue. If ρ(M) < 1, the iteration converges; if ρ(M) ≥ 1, it diverges or oscillates. From your study of matrix norms and conditioning, you know that eigenvalues govern how matrices act on vectors under repeated multiplication. The spectral radius is precisely the long-run amplification factor: ρ(M) < 1 means repeated multiplication by M shrinks the error, driving x^(k) toward the true solution. A well-conditioned system tends to have a small spectral radius and fast convergence; a poorly conditioned one converges slowly or not at all.

For **symmetric positive definite (SPD)** matrices — a common class in physics, engineering, and machine learning — the **conjugate gradient method (CG)** typically converges far faster than Jacobi or Gauss-Seidel. Rather than a simple fixed-point iteration, CG at each step selects the best update direction from a growing Krylov subspace, guaranteeing convergence in at most n steps in exact arithmetic. In practice with floating-point numbers, CG reaches machine precision in far fewer iterations for well-conditioned systems. The convergence rate depends on the **condition number** κ(A): a smaller condition number means fewer iterations, which is why **preconditioning** — transforming Ax = b into an equivalent system with better conditioning — is essential in large-scale scientific computing. The interplay between iteration scheme, spectral radius, and conditioning is what makes iterative methods both a rich theory and a practical engineering discipline.
