---
id: pde-classification
title: Classification of PDEs (Elliptic, Parabolic, Hyperbolic)
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: heat-equation-pde
  type: hard
- id: wave-equation-pde
  type: hard
- id: laplaces-equation
  type: hard
tags: [pde, classification, elliptic, parabolic, hyperbolic]
stage: advanced
status: validated
---
# Classification of PDEs (Elliptic, Parabolic, Hyperbolic)

## Core Idea
Second-order linear PDEs in two variables are classified as elliptic, parabolic, or hyperbolic based on the discriminant of their principal part, analogous to how the discriminant classifies conic sections. The classification determines the qualitative behavior of solutions: elliptic equations (like Laplace's equation) describe steady-state phenomena, parabolic equations (like the heat equation) describe diffusion processes, and hyperbolic equations (like the wave equation) describe propagation phenomena. This trichotomy governs which boundary and initial conditions produce well-posed problems.

## Questions
```yaml
- question: "For the PDE Au_xx + 2Bu_xy + Cu_yy + (lower order terms) = 0, how is the type determined?"
  type: multiple-choice
  options:
    - "By the sign of B² - AC"
    - "By the sign of A + C"
    - "By the sign of AC - B²"
    - "By whether A, B, C are positive"
  answer: 0
  explanation: "The discriminant B² - AC determines the type: positive gives hyperbolic, zero gives parabolic, and negative gives elliptic. This directly parallels the discriminant for conic sections."
- question: "The heat equation u_t = ku_xx is classified as parabolic."
  type: true-false
  answer: true
  explanation: "Written in standard form with x and t as the two independent variables, the heat equation has A = k, B = 0, C = 0, giving discriminant B² - AC = 0, which is the parabolic case."
- question: "What physical behavior is typically associated with hyperbolic PDEs?"
  type: short-answer
  answer: "Wave propagation with finite speed"
  explanation: "Hyperbolic PDEs describe phenomena where disturbances propagate at finite speeds along characteristic curves, such as sound waves, electromagnetic waves, and vibrating strings."
- question: "A PDE can change classification from one region of the domain to another."
  type: true-false
  answer: true
  explanation: "When the coefficients A, B, C depend on the spatial variables, the discriminant B² - AC can change sign across the domain. The Tricomi equation y·u_xx + u_yy = 0 is elliptic for y > 0, parabolic at y = 0, and hyperbolic for y < 0."
- question: "Which type of PDE requires specification of both initial conditions and boundary conditions for a well-posed problem on a bounded domain?"
  type: multiple-choice
  options:
    - "Elliptic"
    - "Parabolic"
    - "Hyperbolic"
    - "Both parabolic and hyperbolic"
  answer: 3
  explanation: "Both parabolic and hyperbolic PDEs are evolution equations that require initial conditions (specifying the state at t = 0) along with boundary conditions. Elliptic PDEs describe equilibrium states and require only boundary conditions."
```

## Explainer
The classification of second-order linear PDEs is one of the most important organizational principles in the theory. Given a general second-order PDE Au_xx + 2Bu_xy + Cu_yy + (lower order terms) = 0, the quantity D = B² - AC determines its type: elliptic if D < 0, parabolic if D = 0, and hyperbolic if D > 0. This is not merely a formal exercise—it reflects deep differences in the physical phenomena described and the mathematical behavior of solutions.

Elliptic PDEs, typified by Laplace's equation Δu = 0, describe steady-state or equilibrium phenomena. Their solutions are infinitely smooth in the interior of the domain (a regularity property), satisfy maximum principles (the solution achieves its extremes on the boundary), and are completely determined by boundary data alone. There are no characteristic curves, and information propagates in all directions simultaneously.

Parabolic PDEs, typified by the heat equation u_t = kΔu, describe diffusive processes that evolve in time. They have a single family of characteristic surfaces (the level sets of t), and information propagates with infinite speed—a disturbance at one point is instantly felt everywhere, though its effect decays rapidly with distance. Solutions smooth out immediately: even rough initial data produces smooth solutions for any t > 0.

Hyperbolic PDEs, typified by the wave equation u_tt = c²Δu, describe propagation phenomena. They have two families of real characteristic curves along which information travels at finite speed, creating a domain of dependence and a domain of influence for each point. Unlike elliptic and parabolic equations, hyperbolic equations preserve singularities in the initial data—waves maintain their shape as they propagate. This finite propagation speed is the defining physical feature of hyperbolic problems.

The classification extends to higher dimensions, though the analysis becomes more nuanced. For a PDE with n spatial variables, the principal symbol is an n×n matrix, and the equation is elliptic if all eigenvalues have the same sign, hyperbolic if exactly one differs, and parabolic if at least one eigenvalue is zero. Systems of PDEs and variable-coefficient equations can change type across the domain, leading to rich and challenging mathematical problems at the boundaries between regions of different type.
