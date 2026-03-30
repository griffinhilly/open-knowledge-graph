---
id: conservation-laws-weak-solutions-intro
title: Conservation Laws and Weak Solutions (Introduction)
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: method-of-characteristics
  type: hard
- id: divergence-theorem
  type: soft
tags: [pde, conservation-law, weak-solution, shock, entropy]
stage: advanced
status: validated
---
# Conservation Laws and Weak Solutions (Introduction)

## Core Idea
Conservation laws are PDEs of the form u_t + f(u)_x = 0 expressing that some quantity (mass, momentum, energy) is locally conserved. Even with smooth initial data, nonlinear conservation laws develop discontinuities (shock waves) in finite time, as faster-moving parts of the solution overtake slower parts. Classical (smooth) solutions cease to exist, necessitating the concept of weak solutions—functions that satisfy the PDE in an integral sense rather than pointwise. Since weak solutions are generally non-unique, additional entropy conditions are required to select the physically relevant one.

## Questions
```yaml
- question: "Why do smooth solutions of nonlinear conservation laws break down in finite time?"
  type: multiple-choice
  options:
    - "Characteristics converge and cross, making the solution multi-valued"
    - "Energy is not conserved"
    - "The equation has no solutions for large t"
    - "Boundary conditions become inconsistent"
  answer: 0
  explanation: "For u_t + f(u)_x = 0, characteristics carry constant values of u but their speeds f'(u) depend on u. When f is nonlinear, different values travel at different speeds, causing characteristics to converge and eventually cross. At the crossing time, no single-valued smooth solution exists."
- question: "A weak solution of a conservation law satisfies the PDE pointwise everywhere."
  type: true-false
  answer: false
  explanation: "A weak solution satisfies the PDE in an integral (distributional) sense: ∫∫[uφ_t + f(u)φ_x]dxdt = 0 for all smooth test functions φ with compact support. This formulation allows discontinuities where the equation is not satisfied pointwise."
- question: "What is the Rankine-Hugoniot condition?"
  type: short-answer
  answer: "The speed s of a shock discontinuity satisfies s = [f(u)]/[u], the ratio of the jump in flux to the jump in the conserved quantity"
  explanation: "When a weak solution has a discontinuity along a curve x = x(t), conservation requires that the shock speed s = dx/dt satisfies s(u_R - u_L) = f(u_R) - f(u_L), where u_L and u_R are the left and right states. This is derived from the integral form of the conservation law."
- question: "Entropy conditions are needed because weak solutions to conservation laws are generally unique."
  type: true-false
  answer: false
  explanation: "Weak solutions are generally NOT unique—multiple piecewise functions can satisfy the integral formulation. Entropy conditions (such as the Lax entropy condition or the viscosity criterion) select the physically relevant weak solution by requiring that shocks dissipate entropy rather than create it."
```

## Explainer
Conservation laws are among the most important PDEs in applied mathematics, modeling fluid dynamics (Euler equations), traffic flow, gas dynamics, and many other phenomena. The simplest example is Burgers' equation u_t + uu_x = 0, where the flux function f(u) = u²/2 makes the wave speed depend on the solution itself. This nonlinearity is the source of the fundamental difficulty: characteristics carrying different values of u travel at different speeds, and when faster waves overtake slower ones, the characteristics cross and a smooth solution cannot persist.

The resolution is the concept of a weak solution: a bounded measurable function u that satisfies ∫∫[uφ_t + f(u)φ_x]dxdt + ∫u(x,0)φ(x,0)dx = 0 for all smooth test functions φ vanishing at large x and t. This integral formulation is equivalent to the PDE where u is smooth but also meaningful where u has jumps. At a jump discontinuity, the integral formulation yields the Rankine-Hugoniot condition relating the shock speed to the jumps in u and f(u). This condition is the mathematical expression of conservation across a discontinuity.

The central difficulty with weak solutions is non-uniqueness. Given initial data that develops a shock, there are infinitely many weak solutions—some physically reasonable (shock waves) and others not (rarefaction shocks that spontaneously create discontinuities). The entropy condition resolves this by imposing an additional selection principle. The Lax entropy condition requires that characteristics enter a shock from both sides (information is absorbed, not created). Equivalently, the viscosity criterion selects the weak solution that is the limit of solutions to u_t + f(u)_x = εu_xx as ε → 0, the solution obtained by adding a small amount of physical dissipation.

The theory of conservation laws extends to systems (such as the Euler equations of gas dynamics) where the situation becomes considerably richer and more difficult. Systems support multiple wave families—shocks, rarefactions, and contact discontinuities—and the interaction of these waves produces complex behavior. The Riemann problem (piecewise constant initial data) serves as the fundamental building block, and Glimm's existence theorem shows that solutions exist for systems with small data. Modern research continues on large-data existence, uniqueness, and the development of efficient numerical schemes (Godunov, WENO) that correctly capture shocks.
