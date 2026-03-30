---
id: calculus-of-variations-euler-lagrange
title: Calculus of Variations and Euler-Lagrange Equations
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: variational-methods-pdes
  type: hard
- id: sobolev-spaces-pdes
  type: soft
tags: [pde, calculus-of-variations, euler-lagrange, functional, minimization]
stage: expert
status: validated
---
# Calculus of Variations and Euler-Lagrange Equations

## Core Idea
The calculus of variations studies the optimization of functionals—mappings from function spaces to real numbers. Given a functional J[u] = ∫L(x, u, ∇u)dx (the Lagrangian or action), a critical point satisfies the Euler-Lagrange equation: -div(∂L/∂(∇u)) + ∂L/∂u = 0. This transforms the optimization problem into a PDE. Many fundamental PDEs arise this way: Laplace's equation from the Dirichlet energy, minimal surface equations from area functionals, and the equations of elasticity from strain energy. The framework connects PDE theory to physics (principle of least action) and geometry (geodesics, minimal surfaces).

## Questions
```yaml
- question: "The Euler-Lagrange equation for the functional J[u] = ∫(½|∇u|² - fu)dx is:"
  type: multiple-choice
  options:
    - "-Δu = f (Poisson's equation)"
    - "Δu = f"
    - "-Δu + u = f"
    - "u = f"
  answer: 0
  explanation: "With L = ½|∇u|² - fu, we have ∂L/∂(∇u) = ∇u and ∂L/∂u = -f. The Euler-Lagrange equation is -div(∇u) + (-f) = 0, which gives -Δu = f."
- question: "The minimal surface equation arises from minimizing the area functional."
  type: true-false
  answer: true
  explanation: "The area of a graph z = u(x,y) is ∫∫√(1+|∇u|²)dxdy. The Euler-Lagrange equation is div(∇u/√(1+|∇u|²)) = 0, the minimal surface equation. Solutions describe soap films and surfaces of zero mean curvature."
- question: "What is the principle of least action in physics?"
  type: short-answer
  answer: "Physical trajectories are critical points of the action functional S = ∫L dt, where L is the Lagrangian (kinetic minus potential energy)"
  explanation: "Hamilton's principle states that the equations of motion (Newton's laws, Maxwell's equations, Einstein's field equations) are all Euler-Lagrange equations for appropriate Lagrangians. This variational formulation is the foundation of modern theoretical physics."
- question: "A minimizer of a convex functional always satisfies the Euler-Lagrange equation."
  type: true-false
  answer: true
  explanation: "For convex functionals, the Euler-Lagrange equation is both necessary and sufficient for a minimum. For non-convex functionals, the Euler-Lagrange equation characterizes all critical points (minima, maxima, and saddle points), and additional analysis is needed to determine which are minimizers."
```

## Explainer
The calculus of variations is the mathematical framework connecting optimization of functionals to PDEs. The central problem is: among all functions u satisfying given boundary conditions, find the one minimizing J[u] = ∫_Ω L(x, u, ∇u)dx. If u is a minimizer and φ is any perturbation vanishing on the boundary, then the function g(ε) = J[u + εφ] has a minimum at ε = 0, so g'(0) = 0. Computing this derivative (the first variation) and using integration by parts yields the Euler-Lagrange equation as the necessary condition for optimality.

For the Dirichlet energy J[u] = ½∫|∇u|²dx, the Euler-Lagrange equation is Laplace's equation Δu = 0. For the area functional J[u] = ∫√(1+|∇u|²)dx, it is the minimal surface equation. For the elastic energy of a beam J[u] = ∫u''²dx, it is the biharmonic equation Δ²u = 0. Each of these PDEs inherits a variational structure: solutions are characterized not just as satisfying a differential equation but as optimizing a geometric or physical quantity.

The direct method of the calculus of variations, perfected by Tonelli, provides existence of minimizers under general conditions. The key hypotheses are: (1) coercivity of J (J[u] → ∞ as ||u|| → ∞, ensuring minimizing sequences are bounded), (2) weak lower semicontinuity of J (the limit of a minimizing sequence achieves a value no larger than the limit of the energies), and (3) convexity of L in ∇u (which ensures weak lower semicontinuity). When L is not convex in ∇u—as occurs in phase transitions, microstructure, and shape memory alloys—minimizers may not exist, and the correct notion is the relaxation of J, replacing L with its convex envelope.

The second variation δ²J determines stability: a critical point is a (local) minimizer if δ²J > 0, which leads to the Jacobi equation and the theory of conjugate points. For multiple critical points of non-convex functionals, topological methods (mountain pass, Ljusternik-Schnirelman, Morse theory) provide existence results. Noether's theorem connects symmetries of the Lagrangian to conservation laws—translational symmetry gives momentum conservation, rotational symmetry gives angular momentum conservation, time symmetry gives energy conservation—providing a deep structural link between the variational formulation and the physics of the problem.
