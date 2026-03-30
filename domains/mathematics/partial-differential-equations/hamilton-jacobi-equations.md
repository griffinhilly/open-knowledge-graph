---
id: hamilton-jacobi-equations
title: Hamilton-Jacobi Equations
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: viscosity-solutions
  type: hard
- id: method-of-characteristics
  type: hard
- id: calculus-of-variations-euler-lagrange
  type: soft
tags: [pde, hamilton-jacobi, optimal-control, viscosity, characteristics]
stage: expert
status: validated
---
# Hamilton-Jacobi Equations

## Core Idea
Hamilton-Jacobi (HJ) equations are first-order nonlinear PDEs of the form u_t + H(x, ∇u) = 0, where H is the Hamiltonian. They arise in classical mechanics (Hamilton-Jacobi theory connects the action principle to wave-like evolution), optimal control (the value function satisfies an HJ equation), and geometric optics (wavefront propagation). Classical solutions typically break down in finite time as characteristics cross, and viscosity solutions provide the correct framework for global-in-time solutions. The Hopf-Lax formula gives an explicit representation for convex Hamiltonians.

## Questions
```yaml
- question: "The Hamilton-Jacobi equation u_t + H(∇u) = 0 with convex H has the Hopf-Lax solution formula:"
  type: multiple-choice
  options:
    - "u(x,t) = min_y {u₀(y) + t·L((x-y)/t)}, where L is the Legendre transform of H"
    - "u(x,t) = u₀(x - H'(0)t)"
    - "u(x,t) = ∫H(ξ)û₀(ξ)e^{iξx}dξ"
    - "u(x,t) = max_y {u₀(y) - |x-y|²/(2t)}"
  answer: 0
  explanation: "The Hopf-Lax formula gives the viscosity solution as a minimum over all 'paths' from initial data to the point (x,t). L = H* is the Legendre-Fenchel transform (convex conjugate) of H, playing the role of the Lagrangian in the variational principle. For H(p) = |p|²/2, this gives u(x,t) = min_y{u₀(y) + |x-y|²/(2t)}."
- question: "Hamilton-Jacobi equations are closely connected to optimal control theory."
  type: true-false
  answer: true
  explanation: "The value function V(x,t) = inf over controls of {cost + terminal value} satisfies the Hamilton-Jacobi-Bellman equation V_t + H(x, ∇V) = 0, where H(x,p) = min_a{f(x,a)·p + L(x,a)}. This connects PDE theory to dynamic programming: solving the HJ equation is equivalent to solving the optimization problem."
- question: "Why do classical solutions of Hamilton-Jacobi equations break down?"
  type: short-answer
  answer: "Characteristics carrying different initial slopes cross in finite time, causing the gradient ∇u to become multi-valued"
  explanation: "For H(p) = |p|²/2, characteristics are straight lines with slopes depending on ∇u₀. When the initial data has varying slope, faster characteristics overtake slower ones, and the classical solution ceases to exist. The viscosity solution develops corners (kinks) where ∇u is discontinuous."
- question: "The eikonal equation |∇u| = 1 is a stationary Hamilton-Jacobi equation whose viscosity solution is:"
  type: multiple-choice
  options:
    - "The distance function to the boundary"
    - "A harmonic function"
    - "The Green's function"
    - "A constant"
  answer: 0
  explanation: "The viscosity solution of |∇u| = 1 in Ω with u = 0 on ∂Ω is u(x) = dist(x, ∂Ω), the distance to the boundary. The gradient of the distance function has magnitude 1 wherever it is differentiable, and it satisfies the equation in the viscosity sense everywhere."
```

## Explainer
Hamilton-Jacobi equations sit at the intersection of classical mechanics, optimal control, and PDE theory. In mechanics, the Hamilton-Jacobi equation u_t + H(x, ∇u) = 0 describes the evolution of the action function, and its characteristics are the trajectories of Hamilton's equations (the equations of motion). Solving the HJ equation is equivalent to finding all trajectories simultaneously—a powerful reformulation that transforms particle mechanics into wave mechanics and lies at the historical foundation of quantum mechanics.

In optimal control, the value function V(x,t) measuring the minimum cost to reach a target from state x at time t satisfies the Hamilton-Jacobi-Bellman (HJB) equation. The Hamiltonian H(x,p) encodes the optimization: H(x,p) = min_a{f(x,a)·p + L(x,a)}, where f is the dynamics and L is the running cost. The optimal control is recovered from ∇V via the minimizing argument in H. This connection, formalized by Bellman's dynamic programming principle, makes HJ equations central to robotics, economics, and engineering.

Classical solutions of HJ equations break down because characteristics cross. For the equation u_t + ½|∇u|² = 0 with initial data u₀(x) = -|x|, the characteristics emanating from the origin fan out while those from far away converge, and the solution develops a corner (non-differentiable point) in finite time. The viscosity solution framework resolves this: it selects the physically correct solution by requiring that the equation is satisfied in an appropriate limiting sense. The Hopf-Lax formula u(x,t) = min_y{u₀(y) + tL((x-y)/t)} provides an explicit representation for convex Hamiltonians.

The eikonal equation |∇u| = f(x), the stationary HJ equation, describes wavefront propagation in geometric optics. The solution is the arrival time of a wavefront moving with speed 1/f(x). Its viscosity solution can be computed efficiently by the Fast Marching Method (O(N log N)), making it practical for applications in computational geometry, image segmentation, and path planning. The theory of HJ equations continues to develop: weak KAM theory (Fathi) connects HJ equations to dynamical systems and ergodic theory, while mean-field games couple HJ equations with Fokker-Planck equations to model large populations of interacting rational agents.
