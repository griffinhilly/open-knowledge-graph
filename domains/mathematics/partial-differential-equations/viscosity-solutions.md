---
id: viscosity-solutions
title: Viscosity Solutions
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: maximum-principles-pdes
  type: hard
- id: weak-solutions-rigorous
  type: hard
tags: [pde, viscosity-solution, nonlinear, hamilton-jacobi, comparison-principle]
stage: expert
status: validated
---
# Viscosity Solutions

## Core Idea
Viscosity solutions are a notion of weak solution for fully nonlinear PDEs F(x, u, Du, D²u) = 0 that do not have a variational or divergence structure. Unlike weak solutions defined by integration against test functions, viscosity solutions are defined using a comparison principle with smooth test functions that touch the solution from above or below. A function u is a viscosity subsolution if, whenever a smooth function φ touches u from above at a point x₀, then F(x₀, u(x₀), Dφ(x₀), D²φ(x₀)) ≤ 0. This definition requires only continuity of u and yields a powerful uniqueness and stability theory.

## Questions
```yaml
- question: "Viscosity solutions are defined using:"
  type: multiple-choice
  options:
    - "Smooth test functions touching the solution from above (subsolution) or below (supersolution)"
    - "Integration against test functions (as in weak solutions)"
    - "Limits of smooth approximate solutions"
    - "Characteristic curves of the PDE"
  answer: 0
  explanation: "The viscosity definition replaces derivatives of u (which may not exist) with derivatives of smooth test functions that touch u tangentially. If φ ≥ u near x₀ with φ(x₀) = u(x₀), then Dφ and D²φ at x₀ serve as 'proxy derivatives' for u."
- question: "Viscosity solutions require the solution to be differentiable."
  type: true-false
  answer: false
  explanation: "Viscosity solutions need only be continuous—no derivatives of any order are required. The definition cleverly extracts differential information from smooth functions that touch u, bypassing the need for u itself to be differentiable."
- question: "For which class of equations are viscosity solutions particularly important?"
  type: short-answer
  answer: "Fully nonlinear PDEs (like Hamilton-Jacobi equations and Bellman equations) that lack divergence structure"
  explanation: "The weak formulation (integration by parts) requires the PDE to be in divergence form. Fully nonlinear equations F(x, u, Du, D²u) = 0 generally are not, so Sobolev-space weak solutions are not available. Viscosity solutions fill this gap."
- question: "The comparison principle for viscosity solutions states that if u is a subsolution and v is a supersolution with u ≤ v on the boundary, then:"
  type: multiple-choice
  options:
    - "u ≤ v throughout the domain"
    - "u = v throughout the domain"
    - "u and v differ by a constant"
    - "u + v is a solution"
  answer: 0
  explanation: "The comparison principle is the fundamental uniqueness tool for viscosity solutions. It says subsolutions lie below supersolutions, which immediately gives uniqueness (if u is both a sub- and supersolution with the same boundary data, comparison gives u ≤ u, i.e., uniqueness) and stability."
```

## Explainer
Viscosity solutions, introduced by Crandall and Lions in the early 1980s, revolutionized the theory of fully nonlinear PDEs. The classical weak solution theory based on Sobolev spaces and integration by parts requires the PDE to have a divergence structure—the operator must be expressible as div(something). But many important equations, including Hamilton-Jacobi equations |∇u| = f, the Monge-Ampere equation det(D²u) = f, and Bellman equations from optimal control, are fully nonlinear and lack this structure. Viscosity solutions provide a weak solution concept for these equations.

The definition is motivated by the maximum principle. If u is a smooth solution of F(x, u, Du, D²u) = 0 and φ is a smooth function with φ ≥ u near x₀ and φ(x₀) = u(x₀), then u - φ has a maximum at x₀, so Du = Dφ and D²u ≤ D²φ at x₀. If F is degenerate elliptic (non-decreasing in D²u), then F(x₀, u, Dφ, D²φ) ≤ F(x₀, u, Du, D²u) = 0. For a non-smooth u, we DEFINE u to be a viscosity subsolution if this inequality holds for every smooth function φ touching u from above. A viscosity supersolution reverses the inequality and the direction of touching. A viscosity solution is both a sub- and supersolution.

The power of viscosity solutions lies in three properties: stability (limits of viscosity solutions are viscosity solutions), comparison (subsolutions lie below supersolutions), and existence (Perron's method constructs solutions from barriers). Stability under uniform limits is immediate from the definition and is crucial for numerical analysis—it means that convergent numerical schemes automatically produce viscosity solutions. The comparison principle requires more work (the doubling-of-variables technique of Crandall-Ishii-Lions) but provides the uniqueness and continuous dependence that make the theory complete.

Viscosity solutions have become the standard framework for Hamilton-Jacobi equations in optimal control and differential games, for level-set methods in computational geometry (tracking moving interfaces), and for stochastic control problems (Hamilton-Jacobi-Bellman equations). They are also central to the modern theory of fully nonlinear elliptic equations, where Evans-Krylov theory provides C^{2,α} regularity for convex equations, and Caffarelli's theory establishes regularity for more general operators. The viscosity framework has been extended to equations on manifolds, to degenerate equations, and to stochastic PDEs, making it one of the most influential developments in PDE theory in the past fifty years.
