---
id: gauss-seidel-method
title: Gauss-Seidel Method
domain: mathematics
course: numerical-analysis
prerequisites:
- id: jacobi-iterative-method
  type: hard
builds-toward:
- successive-over-relaxation
- convergence-iterative-methods
tags:
- gauss-seidel
- iterative
- linear-systems
stage: formal-systems
status: validated
---

# Gauss-Seidel Method

## Core Idea
The Gauss-Seidel method improves Jacobi by using updated values immediately: x_i^{(k+1)} = (b_i - Σ_{j<i} A_{ij}x_j^{(k+1)} - Σ_{j>i} A_{ij}x_j^{(k)})/A_{ii}. By exploiting the latest available values, Gauss-Seidel typically converges roughly twice as fast as Jacobi. The trade-off is that updates must be sequential, making parallelization difficult.

## Questions

```yaml
- question: "In one sweep of Gauss-Seidel on a 4×4 system, you have just computed x₁^(k+1) = 3.2 and x₂^(k+1) = 1.7. When computing x₃^(k+1), which values do you use for x₁ and x₂?"
  type: multiple-choice
  options:
    - "x₁^(k) and x₂^(k) — the previous iteration's values, to keep the sweep consistent"
    - "x₁^(k+1) = 3.2 and x₂^(k+1) = 1.7 — the freshly updated values"
    - "The average of old and new values for each variable"
    - "Either old or new values — Gauss-Seidel allows either"
  answer: 1
  explanation: "This is the defining feature of Gauss-Seidel: once a variable is updated within a sweep, its new value is immediately used for all subsequent updates in that same sweep. When computing x₃, the already-updated x₁^(k+1) and x₂^(k+1) are used, not the old values. Jacobi would use x₁^(k) and x₂^(k) here. This 'use it as soon as you have it' approach is exactly why Gauss-Seidel typically converges faster."

- question: "A team wants to implement an iterative solver on a GPU with thousands of parallel processing units. They compare Jacobi and Gauss-Seidel. Which is better suited for this architecture, and why?"
  type: multiple-choice
  options:
    - "Gauss-Seidel, because it converges faster and will therefore use fewer cores overall"
    - "Jacobi, because each update depends only on previous-iteration values and all updates can be computed simultaneously"
    - "Gauss-Seidel, because its sequential structure maps naturally to GPU thread ordering"
    - "Both are equally suited — parallelizability does not depend on the update strategy"
  answer: 1
  explanation: "Jacobi's update for x_i^(k+1) depends only on old values x^(k), which are all fixed at the start of a sweep. This means all n updates can be computed simultaneously with no dependencies — ideal for massive parallelism. Gauss-Seidel's update for x_i depends on freshly updated x_j for j < i, creating a sequential dependency chain. This is the core trade-off: Gauss-Seidel needs fewer iterations but cannot be parallelized within a sweep; Jacobi is slower per sweep but trivially parallel."

- question: "If Gauss-Seidel converges for a given system, it will require more iterations than Jacobi to reach the same level of accuracy."
  type: true-false
  answer: false
  explanation: "Gauss-Seidel typically converges *faster* than Jacobi — roughly half as many sweeps to reach the same accuracy — because each update incorporates the most current available information rather than stale previous-iteration values. The cost is sequential dependency within each sweep (no parallelism within a sweep), but in terms of iteration count, Gauss-Seidel is the more efficient method. The statement reverses the relationship between the two."

- question: "For Gauss-Seidel to converge, the matrix A must be symmetric positive definite."
  type: true-false
  answer: false
  explanation: "Diagonal dominance is the more general condition that guarantees Gauss-Seidel convergence. Symmetric positive definite (SPD) matrices are a special case where convergence is guaranteed, but SPD is not necessary. Many diagonally dominant systems that are not SPD also converge under Gauss-Seidel. Knowing the sufficient conditions matters: diagonal dominance and SPD are both sufficient; neither is strictly necessary in practice, but they are the standard convergence guarantees to cite."

- question: "Explain in your own words why Gauss-Seidel typically converges faster than Jacobi, and what you give up in exchange."
  type: short-answer
  answer: "Gauss-Seidel uses updated values immediately within each sweep: once x₁ is updated, the new value is used when computing x₂, and so on. Every variable update benefits from all information computed so far in that sweep, incorporating more accurate estimates than Jacobi's 'use only old values' approach. The result is roughly half as many sweeps to converge. The trade-off is that each x_i update depends on the freshly updated x_j for j < i, so all updates must run sequentially — unlike Jacobi where all updates are independent and can run in parallel."
  explanation: "This trade-off is at the heart of iterative solver design: more information per iteration vs. more parallelism per iteration. For large systems on modern hardware, Jacobi's parallelizability can outweigh its slower per-sweep convergence. For sequential computation, Gauss-Seidel wins. Successive over-relaxation (SOR) extends Gauss-Seidel further by extrapolating each update with a factor ω, accelerating convergence even more."
```

## Explainer

You've already studied the Jacobi method, which solves a linear system Ax = b iteratively by isolating each variable and updating using all values from the *previous* iteration. The key insight of Jacobi is that if the matrix A is diagonally dominant, this process converges: each sweep brings the current estimate closer to the true solution. The Gauss-Seidel method asks a simple question: once you've computed the updated x_1 in this sweep, why wait to use it when computing x_2?

In Jacobi, all updates for iteration k+1 are computed using only iteration-k values — a batch update. In Gauss-Seidel, you update x_1 first and immediately use the fresh x_1 when computing x_2, then use both updated x_1 and x_2 for x_3, and so on through all n variables. The update formula x_i^{(k+1)} = (b_i − Σ_{j<i} A_{ij}x_j^{(k+1)} − Σ_{j>i} A_{ij}x_j^{(k)}) / A_{ii} makes this explicit: the first sum uses already-updated values (j < i), the second uses old values (j > i). Each component update incorporates the best available information.

Intuitively, Jacobi is like a committee where everyone polls the previous meeting's results before submitting new opinions; Gauss-Seidel is like an assembly line where each person's update immediately informs the next person's decision. The more current information flows through each sweep, and the result is roughly twice as many iterations eliminated per unit of computation. For the same convergence criterion, Gauss-Seidel typically requires about half as many sweeps as Jacobi.

The convergence conditions are similar: **diagonal dominance** guarantees convergence for both methods, and for symmetric positive definite matrices Gauss-Seidel always converges. The cost is sequential dependency: because each x_i update depends on freshly updated x_j for j < i, all n updates must run in order within each sweep. Jacobi's "stale" values, counterintuitively, are an advantage when parallel hardware is available — each Jacobi update can be computed independently, while Gauss-Seidel must wait. This trade-off between convergence speed and parallelizability motivates further methods like **successive over-relaxation** (SOR), which extrapolates each Gauss-Seidel update by a factor ω to accelerate convergence even further.
