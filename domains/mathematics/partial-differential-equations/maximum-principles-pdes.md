---
id: maximum-principles-pdes
title: Maximum Principles (Elliptic and Parabolic)
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: pde-classification
  type: hard
- id: laplaces-equation
  type: hard
tags: [pde, maximum-principle, elliptic, parabolic, comparison]
stage: advanced
status: validated
---
# Maximum Principles (Elliptic and Parabolic)

## Core Idea
Maximum principles state that solutions to elliptic and parabolic PDEs achieve their extreme values on the boundary of the domain (or at the initial time for parabolic equations), not in the interior. For harmonic functions (solutions to Laplace's equation), this means the maximum and minimum occur on the boundary. For the heat equation, the maximum of u over a space-time cylinder occurs on the parabolic boundary (the initial time or the spatial boundary). These principles are fundamental tools for proving uniqueness, comparison results, and a priori estimates.

## Questions
```yaml
- question: "If u is harmonic in a bounded domain Ω and continuous on its closure, where does u attain its maximum?"
  type: multiple-choice
  options:
    - "On the boundary ∂Ω"
    - "At a critical point in the interior"
    - "At the center of the domain"
    - "It could be anywhere"
  answer: 0
  explanation: "The strong maximum principle for harmonic functions states that if u attains its maximum in the interior, then u must be constant throughout Ω. So a non-constant harmonic function achieves its maximum strictly on the boundary."
- question: "The maximum principle directly implies uniqueness for the Dirichlet problem for Laplace's equation."
  type: true-false
  answer: true
  explanation: "If u₁ and u₂ both solve Δu = 0 with the same boundary data, then w = u₁ - u₂ is harmonic with w = 0 on the boundary. By the maximum principle, w ≤ 0 in Ω, and by the minimum principle, w ≥ 0. So w ≡ 0 and the solution is unique."
- question: "What is the parabolic boundary of the cylinder Ω × (0,T]?"
  type: short-answer
  answer: "The set (Ω × {0}) ∪ (∂Ω × [0,T]), consisting of the initial time slice and the lateral spatial boundary"
  explanation: "For parabolic equations, the maximum principle states extrema occur on the parabolic boundary—the bottom (t=0) and sides (∂Ω) of the space-time cylinder, but not the top (t=T). Information flows forward in time, so the solution at time T is controlled by earlier data."
- question: "For which type of PDE do maximum principles generally fail?"
  type: multiple-choice
  options:
    - "Elliptic"
    - "Parabolic"
    - "Hyperbolic"
    - "Both parabolic and hyperbolic"
  answer: 2
  explanation: "Hyperbolic equations like the wave equation do not satisfy a maximum principle. The solution u_tt = c²u_xx can achieve interior extrema that exceed the boundary values, as waves can constructively interfere."
```

## Explainer
The maximum principle is perhaps the single most important qualitative property of elliptic and parabolic PDEs. In its simplest form for Laplace's equation, it states: if u is harmonic in a connected open set Ω and achieves its maximum at an interior point, then u is constant. The proof uses the mean value property—the value of a harmonic function at any point equals its average over any surrounding sphere—which makes it impossible for a strict interior maximum to exist.

The weak maximum principle says max_Ω u = max_∂Ω u; the strong maximum principle strengthens this to say that if the maximum is achieved in the interior, u must be identically constant. The strong version is considerably more useful: it gives uniqueness of the Dirichlet problem (two solutions with the same boundary data must be identical), continuous dependence on boundary data, and comparison principles (if one solution dominates another on the boundary, it dominates everywhere).

For parabolic equations like the heat equation u_t = Δu, the maximum principle takes a modified form. On a space-time cylinder Q = Ω × (0,T], the maximum of u occurs on the parabolic boundary ∂_p Q = (Ω × {0}) ∪ (∂Ω × [0,T])—the bottom and sides, but not the top. This asymmetry reflects the irreversibility of diffusion: the future is determined by the past, not vice versa. Physically, it says that without internal heat sources, the hottest point is always on the boundary or at the initial time.

Maximum principles extend far beyond the Laplacian. For a general second-order elliptic operator Lu = -a^{ij}u_{ij} + b^i u_i + cu, the maximum principle holds when c ≥ 0 (no internal sources). The Alexandrov-Bakelman-Pucci (ABP) maximum principle provides quantitative bounds relating the maximum of u to the L^n norm of the right-hand side. These refined maximum principles are essential tools in the regularity theory for nonlinear elliptic and parabolic equations, providing the a priori estimates needed to prove existence of solutions.
