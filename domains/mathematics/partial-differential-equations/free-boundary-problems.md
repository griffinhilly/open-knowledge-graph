---
id: free-boundary-problems
title: Free Boundary Problems
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: variational-methods-pdes
  type: hard
- id: elliptic-regularity-theory
  type: hard
- id: maximum-principles-advanced
  type: soft
tags: [pde, free-boundary, obstacle-problem, stefan-problem, variational-inequality]
stage: expert
status: validated
---
# Free Boundary Problems

## Core Idea
In a free boundary problem, the domain on which the PDE holds is not given in advance but is itself part of the unknown, determined simultaneously with the solution. The classic examples are the obstacle problem (find u ≥ ψ minimizing ∫|∇u|²dx, where the contact set {u = ψ} has an unknown boundary) and the Stefan problem (modeling ice-water phase transitions, where the interface between phases moves according to the heat flux jump). The mathematical challenge is that the PDE holds only on an unknown region, and the free boundary must satisfy additional conditions coupling it to the solution.

## Questions
```yaml
- question: "In the obstacle problem, the free boundary is:"
  type: multiple-choice
  options:
    - "The boundary of the contact set where the solution touches the obstacle"
    - "The boundary of the domain Ω"
    - "Any level set of the solution"
    - "The set where the solution is maximum"
  answer: 0
  explanation: "The obstacle problem seeks u ≥ ψ (above the obstacle ψ) that minimizes the Dirichlet energy. The solution coincides with ψ on the contact set and is harmonic (Δu = 0) elsewhere. The free boundary ∂{u = ψ} separates the contact region from the region where u lifts off the obstacle."
- question: "The Stefan problem models the melting of ice, where the free boundary represents the ice-water interface."
  type: true-false
  answer: true
  explanation: "In the Stefan problem, the temperature satisfies the heat equation in each phase (ice and water), and the interface moves according to the Stefan condition: the velocity of the interface equals the jump in heat flux across it. This conservation law ensures that the latent heat of fusion is accounted for."
- question: "What regularity does the free boundary in the obstacle problem typically have?"
  type: short-answer
  answer: "C^{1,α} (continuously differentiable with Holder continuous first derivatives) at regular points, with possible singular points"
  explanation: "Caffarelli's fundamental work (1977-1998) showed that the free boundary in the obstacle problem is C^{1,α} near 'regular' points (where the solution grows quadratically away from the obstacle) and has a stratified structure at singular points. The singular set has Hausdorff dimension at most n-1."
- question: "Free boundary problems can be reformulated as variational inequalities."
  type: true-false
  answer: true
  explanation: "The obstacle problem is equivalent to finding u ∈ K = {v ∈ H¹₀ : v ≥ ψ} such that ∫∇u·∇(v-u)dx ≥ ∫f(v-u)dx for all v ∈ K. This variational inequality formulation avoids explicitly tracking the free boundary and is the basis for both theoretical analysis and numerical computation."
```

## Explainer
Free boundary problems are among the most challenging and physically important problems in PDE theory. Unlike standard boundary value problems where the equation is posed on a fixed domain, in a free boundary problem the domain itself must be determined as part of the solution. This introduces a fundamental nonlinearity even when the underlying PDE is linear: the Laplacian is a linear operator, but the obstacle problem (where we solve Δu = 0 on an unknown region determined by u ≥ ψ) is nonlinear because the domain depends on the solution.

The obstacle problem is the canonical free boundary problem. A membrane (modeled by its displacement u) is pushed against an obstacle ψ from below. Where the membrane lifts off, it is free and satisfies Δu = 0; where it touches, u = ψ. The variational formulation seeks u minimizing ∫|∇u|²dx subject to u ≥ ψ, which is a constrained optimization problem in H¹. The Euler-Lagrange condition becomes a variational inequality: ∫∇u·∇(v-u)dx ≥ 0 for all v ≥ ψ. Existence and uniqueness follow from the theory of variational inequalities (Lions-Stampacchia).

The regularity of the free boundary is the central mathematical question. Caffarelli's groundbreaking work established that the free boundary ∂{u > ψ} is a C^{1,α} surface near regular points—points where the solution detaches from the obstacle in a non-degenerate way (quadratic growth). At degenerate points, cusps and singularities can form, but Caffarelli showed the singular set has codimension at least 1. This regularity theory uses a blow-up analysis: one rescales the solution near a free boundary point and studies the limiting profiles, which are classified as either half-plane solutions (regular points) or polynomial solutions (singular points).

The Stefan problem for phase transitions is another fundamental free boundary problem. The temperature satisfies the heat equation in each phase (solid and liquid), and the interface Γ(t) between phases moves according to the Stefan condition: V_n = [∂T/∂n], where V_n is the normal velocity and [∂T/∂n] is the jump in heat flux. The weak (enthalpy) formulation avoids tracking the interface explicitly and is the basis for existence theory, while the classical formulation provides regularity results for the interface. Modern free boundary problems arise in fluid mechanics (water waves, Hele-Shaw flow), finance (American option pricing), and biology (tumor growth models).
