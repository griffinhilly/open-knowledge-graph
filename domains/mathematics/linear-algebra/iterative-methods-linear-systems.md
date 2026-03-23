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
status: validated
---

# Iterative Methods for Linear Systems

## Core Idea
Iterative methods like Jacobi and Gauss-Seidel solve Ax = b as a fixed-point iteration x^(k+1) = (I − D⁻¹A)x^(k) + D⁻¹b. They converge when ||I − D⁻¹A|| < 1 and are useful for sparse or large systems. Convergence rate depends on spectral radius. Conjugate gradient (CG) converges faster for symmetric positive definite matrices.

## Questions

```yaml
- question: "Jacobi iteration is applied to a 10,000 × 10,000 sparse linear system. After many iterations, the residual does not decrease — the error stays roughly constant or oscillates. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The matrix is too large; Jacobi only works for systems with fewer than 1,000 unknowns"
    - "The spectral radius of the Jacobi iteration matrix is greater than or equal to 1, so the iteration does not converge"
    - "The right-hand side vector b contains numerical errors that prevent convergence"
    - "Jacobi requires a symmetric matrix; the system must not be symmetric"
  answer: 1
  explanation: "Convergence of Jacobi iteration depends entirely on the spectral radius ρ(M) of the iteration matrix M = I − D⁻¹A, where D is the diagonal of A. If ρ(M) ≥ 1, the iteration diverges or fails to contract the error, regardless of system size. Matrix size, symmetry, or right-hand side accuracy are not the governing factors — the spectral radius is. A large sparse system is actually the use case for which iterative methods are designed; the problem here is the structure of A, not its size."

- question: "Why is the conjugate gradient method typically preferred over Jacobi or Gauss-Seidel for large symmetric positive definite (SPD) systems?"
  type: multiple-choice
  options:
    - "Conjugate gradient does not require storing the matrix A, while Jacobi and Gauss-Seidel both require dense factorizations"
    - "Conjugate gradient converges in at most n steps in exact arithmetic and selects optimal update directions from a Krylov subspace, while Jacobi and Gauss-Seidel use simple component-wise updates with slower convergence rates"
    - "Conjugate gradient is the only iterative method guaranteed to work on sparse matrices"
    - "Jacobi and Gauss-Seidel cannot handle SPD matrices because the diagonal is always positive"
  answer: 1
  explanation: "For SPD systems, conjugate gradient builds its updates from a growing Krylov subspace, selecting at each step the direction that most efficiently reduces the error. This gives a convergence rate governed by the condition number κ(A) — well-conditioned SPD systems converge in very few iterations. Jacobi and Gauss-Seidel use simple component-wise updates that do not exploit the global structure of A in this way, leading to slower convergence. All three methods share the key advantage of preserving sparsity by working only with matrix-vector products."

- question: "Gauss-Seidel typically converges faster than Jacobi on the same system because it uses the most recently computed values of x immediately within each iteration sweep."
  type: true-false
  answer: true
  explanation: "This is the defining algorithmic difference between the two methods. In Jacobi, the entire new iterate x^(k+1) is computed using only values from x^(k). In Gauss-Seidel, as soon as a component x_i^(k+1) is updated, it is used immediately to compute x_{i+1}^(k+1). This means Gauss-Seidel is implicitly using fresher information throughout the sweep. For many matrix structures (diagonally dominant, SPD) this accelerates convergence at no additional computational cost per iteration. The convergence rate depends on the spectral radius of Gauss-Seidel's iteration matrix, which is typically smaller than Jacobi's."

- question: "Iterative methods are always preferable to direct methods (like Gaussian elimination) for solving large linear systems, since direct methods are too slow for any system of practical size."
  type: true-false
  answer: false
  explanation: "The choice depends on the structure of the system. Direct methods like Gaussian elimination are O(n³) and fill in zeros during elimination, destroying sparsity — this makes them impractical for very large sparse systems. But for small or moderately sized systems, or for systems that must be solved exactly rather than to a tolerance, direct methods are often preferable because they always succeed and require no convergence analysis. Iterative methods are the right choice specifically for large sparse systems where matrix-vector products are cheap and a solution to moderate precision is acceptable. Neither class is universally superior."

- question: "Explain why the spectral radius ρ(M) of the iteration matrix governs convergence of an iterative method, and what happens geometrically when ρ(M) ≥ 1."
  type: short-answer
  answer: "Each iteration applies the matrix M to the error vector e^(k) = x^(k) − x*, so e^(k) = M^k e^(0). The spectral radius is the largest absolute eigenvalue of M, which governs the long-run behavior of M^k. If ρ(M) < 1, repeated multiplication by M shrinks every component of the error in the directions of the eigenvectors, driving the error to zero. If ρ(M) ≥ 1, at least one eigencomponent of the error does not shrink — it stays constant or grows — so the iteration fails to converge. Geometrically, ρ(M) < 1 means the iteration is a contraction mapping on the error, pulling successive iterates toward the fixed point x*; ρ(M) ≥ 1 means the mapping is not a contraction and the iterates may spiral outward or oscillate."
  explanation: "The connection between spectral radius and convergence is the discrete analogue of asking whether a differential equation's solution decays (negative eigenvalue → decay) or grows (positive eigenvalue → growth). The iteration matrix M encodes exactly how much the error is scaled in each direction per step; ρ(M) is the worst-case scaling factor. Preconditioning works by transforming M into a matrix with smaller spectral radius, accelerating convergence."
```

## Explainer

Direct methods for solving Ax = b — like Gaussian elimination — work well for small or dense systems, but for large, sparse systems (think: a 100,000 × 100,000 matrix where most entries are zero) they are prohibitively expensive. Gaussian elimination requires O(n³) operations and fills in the zeros during the process, destroying sparsity. **Iterative methods** exploit sparsity by never forming dense intermediate matrices — instead, they improve a current guess x^(k) toward the true solution using only matrix-vector products.

The core idea is to reformulate Ax = b as a **fixed-point problem**: find x such that x = f(x). Starting with an initial guess x^(0), you repeatedly apply x^(k+1) = f(x^(k)), hoping the sequence converges to the true solution. For **Jacobi's method**, split A into its diagonal part D and the remainder R = A − D. Then Ax = b becomes Dx = b − Rx, so x = D⁻¹(b − Rx), which directly defines the iteration x^(k+1) = D⁻¹(b − Rx^(k)). Each component of x is updated using all components from the previous iteration. **Gauss-Seidel** improves on this by using the most recently updated values immediately: as soon as x₁^(k+1) is computed, it is used when computing x₂^(k+1), and so on. This typically accelerates convergence without any extra cost.

Whether these iterations converge depends on the structure of the matrix. The key quantity is the **spectral radius** ρ(M) of the iteration matrix M = I − D⁻¹A — the largest absolute eigenvalue. If ρ(M) < 1, the iteration converges; if ρ(M) ≥ 1, it diverges or oscillates. From your study of matrix norms and conditioning, you know that eigenvalues govern how matrices act on vectors under repeated multiplication. The spectral radius is precisely the long-run amplification factor: ρ(M) < 1 means repeated multiplication by M shrinks the error, driving x^(k) toward the true solution. A well-conditioned system tends to have a small spectral radius and fast convergence; a poorly conditioned one converges slowly or not at all.

For **symmetric positive definite (SPD)** matrices — a common class in physics, engineering, and machine learning — the **conjugate gradient method (CG)** typically converges far faster than Jacobi or Gauss-Seidel. Rather than a simple fixed-point iteration, CG at each step selects the best update direction from a growing Krylov subspace, guaranteeing convergence in at most n steps in exact arithmetic. In practice with floating-point numbers, CG reaches machine precision in far fewer iterations for well-conditioned systems. The convergence rate depends on the **condition number** κ(A): a smaller condition number means fewer iterations, which is why **preconditioning** — transforming Ax = b into an equivalent system with better conditioning — is essential in large-scale scientific computing. The interplay between iteration scheme, spectral radius, and conditioning is what makes iterative methods both a rich theory and a practical engineering discipline.
