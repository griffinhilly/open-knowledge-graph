---
id: successive-over-relaxation
title: Successive Over-Relaxation (SOR)
domain: mathematics
course: numerical-analysis
prerequisites:
- id: gauss-seidel-method
  type: hard
builds-toward:
- convergence-iterative-methods
tags:
- sor
- over-relaxation
- iterative
stage: formal-systems
status: validated
---

# Successive Over-Relaxation (SOR)

## Core Idea
SOR accelerates Gauss-Seidel by introducing a relaxation parameter ω: x_i^{(k+1)} = (1-ω)x_i^{(k)} + ω·(Gauss-Seidel step). For 0 < ω < 2, SOR can significantly reduce iterations needed for convergence. The optimal ω depends on the matrix eigenvalues; poor choice of ω can slow or even prevent convergence.

## Questions

```yaml
- question: "SOR is applied with ω = 1.5 to solve a linear system. At one update step, the Gauss-Seidel formula gives x_i^{GS} = 3.0 and the current value is x_i^{(k)} = 2.0. What is x_i^{(k+1)}?"
  type: multiple-choice
  options:
    - "3.0 — SOR with ω > 1 just accepts the Gauss-Seidel update directly"
    - "3.5 — SOR extrapolates past the Gauss-Seidel update in the direction of improvement"
    - "2.5 — SOR averages the current value and the Gauss-Seidel update"
    - "1.5 — SOR scales the Gauss-Seidel update by ω"
  answer: 1
  explanation: "Applying the SOR formula: x_i^{(k+1)} = (1 − ω)x_i^{(k)} + ω·x_i^{GS} = (1 − 1.5)(2.0) + (1.5)(3.0) = (−0.5)(2.0) + (1.5)(3.0) = −1.0 + 4.5 = 3.5. With ω = 1.5, SOR overshoots the Gauss-Seidel value: the current value is 2.0, G-S says go to 3.0 (a step of +1.0), and SOR goes to 3.5 (a step of +1.5 = ω × the G-S step). This extrapolation is the essence of over-relaxation — it 'leaps' further in the direction Gauss-Seidel is heading, betting that direction is toward the solution."

- question: "Why is finding the optimal relaxation parameter ω difficult for general matrices in practice?"
  type: multiple-choice
  options:
    - "The SOR formula becomes unstable for arbitrary ω, so numerical experiments are too risky"
    - "The optimal ω formula requires the spectral radius of the Gauss-Seidel iteration matrix, which is only analytically available for matrices with special structure (like Property A)"
    - "General matrices require ω < 1 (under-relaxation), which is never beneficial"
    - "The optimal ω depends on the right-hand side vector b, which changes with each problem"
  answer: 1
  explanation: "The formula ω_opt = 2 / (1 + √(1 − ρ²)) requires knowing ρ, the spectral radius of the Gauss-Seidel iteration matrix. For special matrix structures — like those arising from the five-point stencil discretization of Poisson's equation — ρ can be computed analytically. For general sparse matrices, no such formula exists. In practice, ω must be estimated by running several iterations and measuring the observed convergence rate, or through adaptive algorithms. This is why SOR is most powerful when the matrix has exploitable structure."

- question: "Setting ω = 1 in the SOR update formula x_i^{(k+1)} = (1−ω)x_i^{(k)} + ω·x_i^{GS} recovers plain Gauss-Seidel iteration."
  type: true-false
  answer: true
  explanation: "Substituting ω = 1: x_i^{(k+1)} = (1 − 1)x_i^{(k)} + 1·x_i^{GS} = 0 + x_i^{GS} = x_i^{GS}. The current value is ignored and the update is exactly the Gauss-Seidel step. This shows that SOR is a generalization of Gauss-Seidel, with ω = 1 as the special case. The ω parameter blends the current value with the Gauss-Seidel update, and ω = 1 means 'take the G-S update with weight 1 and the current value with weight 0.'"

- question: "SOR is very likely to converge for any positive value of ω, provided the system Ax = b has a unique solution."
  type: true-false
  answer: false
  explanation: "SOR is only guaranteed to converge when 0 < ω < 2. Outside this range — particularly for ω ≥ 2 — the iteration diverges regardless of the matrix properties. Within (0, 2), convergence still depends on the matrix (diagonal dominance or positive definiteness are sufficient conditions). The bound ω < 2 is a hard theoretical requirement, not a practical guideline. Choosing ω = 2.1, for example, will cause the iterates to grow without bound even for well-conditioned systems."

- question: "Why does over-relaxation (ω > 1) speed up convergence compared to plain Gauss-Seidel, and what property of the iteration determines the optimal ω?"
  type: short-answer
  answer: "Convergence rate is governed by the spectral radius ρ of the iteration matrix — the magnitude of its largest eigenvalue. For Gauss-Seidel applied to problems like discretized PDEs, ρ is close to 1, meaning slow convergence. Over-relaxation with the optimal ω reduces ρ substantially: the optimal SOR iteration matrix has a much smaller spectral radius, cutting the number of iterations needed from O(N²) to O(N) for an N×N grid. Geometrically, over-relaxation 'leaps' further in the direction of improvement at each step, reducing the number of steps needed to reach the solution to within tolerance."
  explanation: "The key insight is that Gauss-Seidel is already moving in the right direction — toward the solution. SOR asks: if we know the direction is right, why not take a bigger step? The answer is that bigger steps reduce the spectral radius of the iteration matrix, which is the mathematical quantity governing how quickly errors shrink. The optimal ω makes the spectral radius as small as possible, which is why knowing ρ of the Gauss-Seidel matrix is the key to computing ω_opt."
```

## Explainer

From the Gauss-Seidel method, you know that solving Ax = b iteratively means updating each variable x_i in turn using the latest available values of the other variables. Gauss-Seidel converges faster than Jacobi because it uses fresh updates immediately, but for large sparse systems — especially those arising from discretized PDEs — even Gauss-Seidel can require thousands of iterations. SOR's insight is simple: if Gauss-Seidel is moving in the right direction, why not take a bigger step in that direction?

The **relaxation parameter** ω controls the step size. At each update, the SOR formula is x_i^{(k+1)} = (1 − ω) x_i^{(k)} + ω · x_i^{GS}, where x_i^{GS} is the Gauss-Seidel update. When ω = 1, you recover plain Gauss-Seidel. When ω > 1, you **over-relax**: you move past the Gauss-Seidel update by interpolating (or extrapolating) further in that direction, attempting to "leap" toward the solution. When ω < 1 (under-relaxation), you take a smaller step — useful for stabilizing a method that would otherwise diverge, though not the typical application of SOR.

Why does over-relaxation help? The convergence rate of iterative methods is governed by the **spectral radius** of the iteration matrix — the largest eigenvalue in absolute value. For Gauss-Seidel applied to problems with a known structure (like the five-point stencil for Laplace's equation on a rectangle), the spectral radius ρ is close to 1, meaning convergence is slow. The optimal SOR parameter is ω_opt = 2 / (1 + √(1 − ρ²)), which can reduce the spectral radius from something near 1 to something near 1 − O(h) where h is the grid spacing. In practice, this accelerates convergence by an order of magnitude: where Gauss-Seidel might need O(N²) iterations for an N × N grid, optimal SOR needs only O(N).

The critical challenge is choosing ω. The formula ω_opt requires knowing the spectral radius of the Gauss-Seidel iteration matrix, which is only analytically available for special matrix structures (those with a "Property A" and consistent ordering). For general matrices, ω must be estimated experimentally — by running a few iterations and observing the convergence rate — or by more sophisticated adaptive methods. Choosing ω poorly (say, ω > 2) causes divergence, since the SOR iteration is guaranteed to converge only for 0 < ω < 2. SOR laid the groundwork for understanding **preconditioning** and **multigrid** methods, which address the same slow-convergence problem through more powerful approaches.
