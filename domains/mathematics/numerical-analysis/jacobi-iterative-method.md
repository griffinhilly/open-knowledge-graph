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
stage: formal-systems
status: draft
---

# Jacobi Iterative Method

## Core Idea
The Jacobi method solves Ax = b by iterating x^{(k+1)} = D⁻¹(b - (L+U)x^{(k)}), where D is A's diagonal and L, U are its lower and upper parts. Each component is updated simultaneously using values from the previous iteration. Jacobi is simple to implement and parallelize but converges slowly unless A is diagonally dominant or well-conditioned.

## Questions

```yaml
- question: "During a Jacobi iteration sweep, component x₁^(k+1) has just been computed. When computing x₂^(k+1), which value of x₁ is used?"
  type: multiple-choice
  options:
    - "The freshly computed x₁^(k+1) from this sweep"
    - "The old value x₁^(k) from the previous iteration"
    - "The average of x₁^(k) and x₁^(k+1)"
    - "Whichever value accelerates convergence"
  answer: 1
  explanation: "Jacobi's defining rule is that all components of x^(k+1) are computed simultaneously using only values from the previous iterate x^(k). No freshly computed component is used within the same sweep. This 'all-old' update is what distinguishes Jacobi from Gauss-Seidel, which immediately uses fresh values as they are computed. It also enables parallel computation of all components, since they are mutually independent within a sweep."

- question: "A linear system Ax = b has a coefficient matrix A where each diagonal entry is strictly larger in magnitude than the sum of the absolute values of all other entries in its row. What can you conclude about Jacobi iteration on this system?"
  type: multiple-choice
  options:
    - "Jacobi will diverge because the diagonal dominates and suppresses off-diagonal corrections"
    - "Jacobi is guaranteed to converge because A is diagonally dominant"
    - "Convergence cannot be determined without computing the spectral radius explicitly"
    - "Jacobi will converge only if A is also symmetric"
  answer: 1
  explanation: "Diagonal dominance — |aᵢᵢ| > Σⱼ≠ᵢ |aᵢⱼ| for every row — is a sufficient condition for Jacobi convergence. It guarantees the spectral radius of the iteration matrix D⁻¹(L+U) is less than 1. Intuitively, when the diagonal entry dominates, each update is controlled primarily by the correct term bᵢ/aᵢᵢ, and the off-diagonal perturbations are small enough that the iteration self-corrects. Note this is sufficient but not necessary — Jacobi can converge for some non-dominant matrices too."

- question: "The Jacobi method can be parallelized more easily than Gauss-Seidel because all component updates within a single sweep are independent of each other."
  type: true-false
  answer: true
  explanation: "True. Because Jacobi only uses values from the previous iteration (x^(k)) to compute all components of x^(k+1), every component update is independent — no component depends on another freshly-computed component in the same sweep. This makes Jacobi trivially parallelizable. Gauss-Seidel, by contrast, immediately uses freshly computed values, creating data dependencies that prevent straightforward parallel execution."

- question: "If the Jacobi method fails to converge for a given linear system, then Gauss-Seidel will also fail to converge on the same system."
  type: true-false
  answer: false
  explanation: "False. Jacobi and Gauss-Seidel have different convergence properties and different iteration matrices. It is possible for Jacobi to diverge while Gauss-Seidel converges on the same system (and in rare cases, the reverse). The two methods share the decomposition A = D + L + U but use different update rules, resulting in different spectral radii for their respective iteration matrices. Diagonal dominance guarantees convergence for both, but outside that condition the methods can behave differently."

- question: "Why does the Jacobi method use only values from the previous iteration when computing updates, and what practical advantage does this 'all-old' rule provide?"
  type: short-answer
  answer: "The all-old update rule means each component x_i^(k+1) = (b_i − Σ_{j≠i} a_{ij} x_j^(k)) / a_{ii} depends only on the previous iterate, not on freshly computed values from the current sweep. This makes all n component updates mutually independent within a single sweep, enabling them to be computed simultaneously on parallel hardware. The trade-off is slower convergence compared to Gauss-Seidel, which uses fresh values immediately and typically halves the iteration count for the same accuracy."
  explanation: "The design reflects a deliberate choice: sacrifice convergence speed for parallelism and implementation simplicity. In large sparse systems — common in scientific computing — the ability to distribute all n updates across many processors at once can more than compensate for the extra iterations required compared to Gauss-Seidel."
```

## Explainer

The Jacobi method applies the **fixed-point iteration** idea you already know to the problem of solving a linear system Ax = b. In fixed-point iteration, you rearrange an equation into the form x = g(x) and then repeatedly apply g. The Jacobi method does exactly this for linear systems: for each equation i, solve for xᵢ in terms of the other variables: xᵢ = (bᵢ − Σⱼ≠ᵢ aᵢⱼ xⱼ) / aᵢᵢ. This gives a map g(x), and Jacobi iterates x^{(k+1)} = g(x^{(k)}).

The matrix formulation makes the structure transparent. Write A = D + L + U, where D is the diagonal of A, L is the strictly lower triangular part, and U is the strictly upper triangular part — all operations you know from matrix decompositions. Then Ax = b becomes Dx = b − (L + U)x, so x = D⁻¹(b − (L + U)x). The Jacobi iteration is x^{(k+1)} = D⁻¹(b − (L + U)x^{(k)}): invert the diagonal (trivial — just divide each component by the diagonal entry), then apply the off-diagonal parts to the old iterate. The **key feature** is that all components of x^{(k+1)} are computed simultaneously using only values from x^{(k)}, never from freshly computed components of the current sweep. This "all-old" update rule is what distinguishes Jacobi from Gauss-Seidel.

Convergence depends on the **spectral radius** ρ of the iteration matrix D⁻¹(L + U): the iteration converges if and only if ρ < 1. A sufficient condition you can check directly from A's entries is **diagonal dominance**: A is diagonally dominant if |aᵢᵢ| > Σⱼ≠ᵢ |aᵢⱼ| for every row i. Intuitively, when the diagonal is large, each update is dominated by the correct term bᵢ/aᵢᵢ, and the off-diagonal corrections are small perturbations. The system "self-corrects" at each step.

Jacobi's practical advantage over direct methods like Gaussian elimination is that it never needs to form or store a factorization — you only need to multiply by A once per iteration. For large sparse systems (many zeros), this can save enormous memory and computation. The trade-off is slow convergence: each iteration reduces the error by only a factor of ρ, which may be close to 1 for nearly-singular or poorly-conditioned systems. The Gauss-Seidel method improves this by using fresh component values as soon as they are computed within a sweep, typically halving the number of iterations required for the same accuracy.
