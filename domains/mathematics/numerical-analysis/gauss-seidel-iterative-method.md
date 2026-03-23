---
id: gauss-seidel-iterative-method
title: Gauss-Seidel Iterative Method
domain: mathematics
course: numerical-analysis
prerequisites:
- id: jacobi-iterative-method
  type: hard
builds-toward:
- successive-over-relaxation-sor
- convergence-iterative-linear-solvers
tags:
- gauss-seidel
- iterative-solver
- fast-convergence
stage: formal-systems
status: draft
---

# Gauss-Seidel Iterative Method

## Core Idea
Gauss-Seidel improves Jacobi by using updated variable values immediately as they become available within each iteration. The method typically converges twice as fast as Jacobi for the same problems. Convergence is guaranteed for symmetric positive-definite matrices and diagonally dominant matrices, making it a practical alternative to direct methods for large sparse systems.

## Questions

```yaml
- question: "What is the single key difference between Gauss-Seidel and Jacobi when solving Ax = b iteratively?"
  type: multiple-choice
  options:
    - "Gauss-Seidel requires the matrix to be symmetric; Jacobi works for any matrix"
    - "Gauss-Seidel updates each variable using the most recently computed values within the same sweep, while Jacobi uses only values from the previous iteration"
    - "Gauss-Seidel applies a relaxation factor ω to accelerate convergence; Jacobi uses no relaxation"
    - "Gauss-Seidel converges for all non-singular matrices; Jacobi only converges for diagonally dominant matrices"
  answer: 1
  explanation: "The defining distinction is the update policy. Jacobi computes all new values simultaneously from the previous iteration — like reading a snapshot then updating. Gauss-Seidel feeds each updated value forward immediately: once x₁ is updated, the new x₁ is used when computing x₂, and so on. This greedy reuse of information is what drives faster convergence. Option C describes Successive Over-Relaxation (SOR), which is a further enhancement of Gauss-Seidel. Option D overstates Gauss-Seidel's convergence guarantee."

- question: "A Gauss-Seidel sweep over a 4-variable system has just computed an improved value for x₂. When computing x₃, which values does Gauss-Seidel use?"
  type: multiple-choice
  options:
    - "The old values of x₁, x₂, and x₄ from the previous iteration — like Jacobi"
    - "The new values of x₁ and x₂ (computed this sweep) and the old value of x₄ (not yet updated)"
    - "Only the old value of x₂, since x₃ depends primarily on its immediate neighbor"
    - "The new value of x₂ and the old values of x₁ and x₄, regardless of ordering"
  answer: 1
  explanation: "In Gauss-Seidel, when computing xᵢ, you use the most current available values: the already-updated values for j < i (computed earlier in this sweep) and the holdover values for j > i (not yet updated in this sweep). So when computing x₃, x₁ and x₂ have already been updated this sweep and are used immediately; x₄ hasn't been computed yet, so the old value from the previous iteration is used. This mixed-sweep update is exactly what distinguishes Gauss-Seidel from Jacobi."

- question: "Gauss-Seidel always converges whenever Jacobi converges for the same matrix."
  type: true-false
  answer: false
  explanation: "Gauss-Seidel and Jacobi are not strictly comparable in convergence for general matrices. Each can converge when the other diverges, and vice versa. What is true is that for the most common practical matrix classes — symmetric positive-definite (SPD) and strictly diagonally dominant matrices — both converge, and Gauss-Seidel converges faster (roughly in half as many iterations). But there exist matrices where Jacobi converges and Gauss-Seidel diverges, and vice versa. The convergence guarantee applies to the matrix class, not to one method being universally superior."

- question: "Because Gauss-Seidel uses the latest values immediately, it is always a better choice than Jacobi for parallel computing environments."
  type: true-false
  answer: false
  explanation: "Gauss-Seidel is harder to parallelize than Jacobi, not easier. Jacobi's simultaneous update policy means all variables can be computed independently in parallel using only old values — perfectly suited to multi-processor or GPU computation. Gauss-Seidel's sequential dependency structure (x₂ must wait for the new x₁, x₃ must wait for the new x₂, etc.) creates a data dependency chain that prevents straightforward parallelization. For parallel computing, Jacobi or block-Jacobi variants are often preferred, even though Gauss-Seidel converges faster serially."

- question: "Explain in your own words why Gauss-Seidel typically converges faster than Jacobi, and what tradeoff this creates."
  type: short-answer
  answer: "Gauss-Seidel converges faster because it uses more up-to-date information during each sweep. As soon as x₁ is improved, that improvement feeds into the computation of x₂, which feeds into x₃, etc. By the end of a single sweep, later variables have benefited from all the updates made earlier in that same sweep — not just the updates from the previous iteration. This 'greedy' reuse roughly halves the number of iterations needed compared to Jacobi. The tradeoff is sequential dependency: since each update depends on the previous one in the sweep, the computation cannot be easily parallelized across processors."
  explanation: "The deeper point is that Jacobi treats one iteration as an atomic unit (compute all, then update all), while Gauss-Seidel dissolves that unit into a continuous stream of improvements. For serial computation this is always at least as good and usually better; for parallel computation the sequential dependency is a real cost that can outweigh the iteration-count advantage when many processors are available."
```

## Explainer

In the Jacobi method you studied, each new iteration computes all updated values simultaneously from the previous iteration's values. It's like updating a spreadsheet where every cell reads only the old values, then all cells refresh at once. **Gauss-Seidel** makes one conceptually simple change: as soon as you compute an updated value for variable x₁, you immediately use that new value when computing x₂, and so on through the system. Within a single sweep, each variable is computed using the most current estimates available.

To see why this helps, consider a 3×3 system. In Jacobi, when you compute the new x₂, you use the old x₁ even though you just computed a better x₁. Gauss-Seidel feeds the improved x₁ forward immediately. This isn't just slightly faster — it typically means the error shrinks in roughly half as many iterations. The spectral radius of the Gauss-Seidel iteration matrix is approximately the square of the Jacobi spectral radius for many common matrix types, which translates directly into faster convergence. In practice, this halving of iteration count often matters more than theoretical constants.

The convergence conditions for Gauss-Seidel are the same as for Jacobi: **strict diagonal dominance** (each diagonal entry is larger in absolute value than the sum of the other entries in its row) guarantees convergence, and so does **symmetric positive-definiteness**. However, Gauss-Seidel can converge even when Jacobi diverges, and vice versa — they are not strictly comparable in general, though for the most practically important matrix classes (SPD and diagonally dominant), Gauss-Seidel wins. One important limitation: the method is inherently sequential, since each update depends on the previous update in the same sweep. This makes parallelization harder than for Jacobi.

The update formula for Gauss-Seidel solving Ax = b is: for each i, set xᵢ ← (bᵢ − Σ_{j<i} aᵢⱼxⱼ^{new} − Σ_{j>i} aᵢⱼxⱼ^{old}) / aᵢᵢ. The left sum uses already-updated values from this sweep; the right sum uses holdovers from the previous sweep. This single formula captures the key idea: Gauss-Seidel is Jacobi with a greedy update policy. For large, sparse, well-conditioned linear systems — such as those arising in finite element methods or discretized PDEs — Gauss-Seidel is a practical first choice before turning to more sophisticated preconditioned Krylov methods.
