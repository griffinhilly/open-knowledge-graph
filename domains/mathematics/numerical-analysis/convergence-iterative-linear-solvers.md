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
status: validated
---

# Convergence of Iterative Methods

## Core Idea
Iterative methods for linear systems converge if and only if the spectral radius ρ(G) of the iteration matrix G is less than 1. The convergence rate depends on ρ(G); smaller spectral radius means faster convergence. Different splittings (Jacobi, Gauss-Seidel, SOR) produce different iteration matrices with different spectral radii, explaining their varying convergence speeds.

## Questions

```yaml
- question: "An iteration matrix G has eigenvalues 1.05, 0.3, 0.6, and −0.4. A student argues the method will converge because 'three of the four eigenvalues have magnitude less than 1.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — if most eigenvalues are small, the dominant behavior converges"
    - "The negative eigenvalue −0.4 causes oscillations that prevent convergence regardless of the others"
    - "Convergence requires ALL eigenvalues to have magnitude less than 1; ρ(G) = 1.05 ≥ 1 guarantees divergence"
    - "The method will converge, but only if the initial guess is already close enough to the solution"
  answer: 2
  explanation: "Convergence requires G^k → 0, which means every eigenvalue must satisfy |λ| < 1. If the initial error e_0 has any component in the direction of the eigenvector for λ = 1.05, that component grows by 5% per iteration — unboundedly. Even one eigenvalue with |λ| ≥ 1 is fatal. The spectral radius ρ(G) = max|λᵢ| = 1.05, and the convergence theorem states G^k → 0 if and only if ρ(G) < 1. The majority-vote reasoning is entirely incorrect."

- question: "An iterative method has spectral radius ρ(G) = 0.99. Approximately how many iterations are needed to reduce the initial error by a factor of 1000?"
  type: multiple-choice
  options:
    - "About 30 — the error roughly halves every 70 iterations, so 30 steps covers a factor of 1000"
    - "About 3 — one for each order of magnitude, since the method converges geometrically"
    - "About 690 — since (0.99)^690 ≈ 0.001"
    - "Impossible to determine without knowing the size of the initial error"
  answer: 2
  explanation: "The error decays geometrically as ρ(G)^k. To reduce error by a factor of 1000, we need ρ^k ≈ 0.001, so k ≈ log(0.001)/log(0.99) = −6.908/(−0.01005) ≈ 688 iterations. This illustrates a key insight: a spectral radius very close to 1 (like 0.99) means agonizingly slow convergence — nearly 700 iterations for three orders of magnitude. This is why reducing ρ(G) from 0.99 to 0.9 (achievable by changing the splitting or using SOR) dramatically accelerates convergence."

- question: "If the iteration matrix G has spectral radius ρ(G) = 0.7, the error after k iterations decays geometrically as approximately (0.7)^k."
  type: true-false
  answer: true
  explanation: "The error evolves as e_k = G^k e_0. Decomposing in the eigenbasis, each component scales as λᵢ^k. The dominant contribution comes from the largest |λᵢ| = ρ(G) = 0.7, so ||e_k|| ≈ C · (0.7)^k for large k. This geometric decay is exact (up to the constant C) for any ρ(G) < 1, and it is what makes spectral radius the central quantity for convergence analysis."

- question: "Different ways of splitting the matrix A — such as Jacobi versus Gauss-Seidel — yield the same iteration matrix G and therefore the same convergence rate."
  type: true-false
  answer: false
  explanation: "Different splittings produce entirely different iteration matrices. The Jacobi iteration matrix G_J uses only the diagonal of A; the Gauss-Seidel matrix G_GS uses the lower triangular part, incorporating newly computed values immediately. For many common problem classes (e.g., matrices from discretized PDEs), ρ(G_GS) = ρ(G_J)², making Gauss-Seidel converge in half as many iterations. SOR further reduces ρ by introducing a relaxation parameter. The entire purpose of comparing splittings is precisely that they lead to different spectral radii."

- question: "Explain why even a single eigenvalue with magnitude ≥ 1 causes an iterative method to fail to converge, regardless of how small all other eigenvalues are."
  type: short-answer
  answer: "The error evolves as e_k = G^k e_0. Decomposing the initial error in the eigenbasis of G, each component along eigenvector vᵢ is scaled by λᵢ^k at each step. If any eigenvalue has |λᵢ| ≥ 1, the corresponding component does not decay — it stays constant or grows. Since convergence requires the total error to go to zero, every component must vanish, which requires |λᵢ| < 1 for all i. Even a single non-decaying component prevents convergence, regardless of how fast the other components shrink."
  explanation: "This is the heart of the spectral radius criterion. The spectral radius ρ(G) = max|λᵢ| captures the worst-case eigenvalue. If ρ(G) ≥ 1, there exists at least one component of the error that never decays. The initial error will generically have a nonzero projection onto that eigenvector, so the method diverges (or at best fails to converge) for almost all starting points. This is why convergence is equivalent to ρ(G) < 1 — not just 'most eigenvalues < 1' or 'average eigenvalue < 1'."
```

## Explainer

Every stationary iterative method for solving Ax = b can be written in the form x_{k+1} = Gx_k + c, where G is the **iteration matrix** (determined by how you split A) and c is a fixed vector. If x* is the exact solution, it satisfies x* = Gx* + c. Subtracting, the error e_k = x_k - x* evolves by e_{k+1} = G · e_k. After k iterations, e_k = G^k · e_0. Convergence means G^k → 0 as k → ∞ — the question is entirely about the powers of G.

This is where **eigenvalues** (your hard prerequisite) become decisive. Recall that if v is an eigenvector of G with eigenvalue λ, then G^k v = λ^k v. If we decompose the initial error e_0 in the eigenbasis of G (assuming G is diagonalizable), each component is multiplied by the corresponding λ^k at each step. For the error to vanish, every |λ^k| must go to zero — meaning every eigenvalue must satisfy |λ| < 1. The **spectral radius** ρ(G) = max |λ_i| is the radius of the largest eigenvalue. The theorem is clean: G^k → 0 if and only if ρ(G) < 1. If even one eigenvalue has |λ| ≥ 1, that component of the error never decays.

The convergence rate is controlled by the dominant eigenvalue. After k steps, ||e_k|| ≈ C · ρ(G)^k, a geometric decay. To reduce the error by a factor of 10, you need approximately log(10) / log(1/ρ(G)) iterations. This makes the dependence on ρ(G) very sensitive: decreasing ρ from 0.99 to 0.9 cuts the required iterations per order of magnitude from roughly 230 to 22 — a 10× speedup.

Different splittings of A produce different iteration matrices. For Jacobi, G_J uses only the diagonal of A. For Gauss-Seidel, G_GS uses the lower triangular part, incorporating newly computed values immediately. For many common problem classes (e.g., tridiagonal matrices from discretized PDEs), one can show ρ(G_GS) = ρ(G_J)², making Gauss-Seidel converge in half as many iterations as Jacobi. Successive Over-Relaxation (SOR) introduces a relaxation parameter ω to reduce ρ(G_SOR) further still. The entire art of iterative method selection is choosing a splitting that makes ρ(G) as small as possible for the structure of A at hand.
