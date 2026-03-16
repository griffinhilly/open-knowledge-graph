---
id: jacobi-iterative-method
title: Jacobi Iterative Method
domain: mathematics
course: numerical-analysis
prerequisites:
- id: fixed-point-iteration
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- gauss-seidel-method
- convergence-iterative-methods
tags:
- jacobi
- iterative
- linear-systems
stage: abstract-reasoning
status: draft
---

# Jacobi Iterative Method

## Core Idea
The Jacobi method solves Ax = b by iterating x^{(k+1)} = D⁻¹(b - (L+U)x^{(k)}), where D is A's diagonal and L, U are its lower and upper parts. Each component is updated simultaneously using values from the previous iteration. Jacobi is simple to implement and parallelize but converges slowly unless A is diagonally dominant or well-conditioned.

## Explainer

The Jacobi method applies the **fixed-point iteration** idea you already know to the problem of solving a linear system Ax = b. In fixed-point iteration, you rearrange an equation into the form x = g(x) and then repeatedly apply g. The Jacobi method does exactly this for linear systems: for each equation i, solve for xᵢ in terms of the other variables: xᵢ = (bᵢ − Σⱼ≠ᵢ aᵢⱼ xⱼ) / aᵢᵢ. This gives a map g(x), and Jacobi iterates x^{(k+1)} = g(x^{(k)}).

The matrix formulation makes the structure transparent. Write A = D + L + U, where D is the diagonal of A, L is the strictly lower triangular part, and U is the strictly upper triangular part — all operations you know from matrix decompositions. Then Ax = b becomes Dx = b − (L + U)x, so x = D⁻¹(b − (L + U)x). The Jacobi iteration is x^{(k+1)} = D⁻¹(b − (L + U)x^{(k)}): invert the diagonal (trivial — just divide each component by the diagonal entry), then apply the off-diagonal parts to the old iterate. The **key feature** is that all components of x^{(k+1)} are computed simultaneously using only values from x^{(k)}, never from freshly computed components of the current sweep. This "all-old" update rule is what distinguishes Jacobi from Gauss-Seidel.

Convergence depends on the **spectral radius** ρ of the iteration matrix D⁻¹(L + U): the iteration converges if and only if ρ < 1. A sufficient condition you can check directly from A's entries is **diagonal dominance**: A is diagonally dominant if |aᵢᵢ| > Σⱼ≠ᵢ |aᵢⱼ| for every row i. Intuitively, when the diagonal is large, each update is dominated by the correct term bᵢ/aᵢᵢ, and the off-diagonal corrections are small perturbations. The system "self-corrects" at each step.

Jacobi's practical advantage over direct methods like Gaussian elimination is that it never needs to form or store a factorization — you only need to multiply by A once per iteration. For large sparse systems (many zeros), this can save enormous memory and computation. The trade-off is slow convergence: each iteration reduces the error by only a factor of ρ, which may be close to 1 for nearly-singular or poorly-conditioned systems. The Gauss-Seidel method improves this by using fresh component values as soon as they are computed within a sweep, typically halving the number of iterations required for the same accuracy.
