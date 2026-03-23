---
id: laplaces-equation
title: Laplace's Equation and Boundary Value Problems
domain: mathematics
course: differential-equations
prerequisites:
- id: wave-equation-pde
  type: hard
- id: partial-derivatives
  type: hard
tags:
- laplace-equation
- pde
- elliptic
- boundary-value
stage: advanced
status: validated
---

# Laplace's Equation and Boundary Value Problems

## Core Idea
Laplace's equation ∇²u = 0 (in 2D: ∂²u/∂x² + ∂²u/∂y² = 0) governs steady-state temperature, electric potential, and gravitational fields. It is elliptic with no time evolution; solutions depend entirely on boundary conditions (Dirichlet, Neumann, or Robin). Unlike parabolic and hyperbolic PDEs, elliptic equations require simultaneous solving over the entire domain, making them computationally different but essential for equilibrium problems.

## Questions

```yaml
- question: "Why can't Laplace's equation ∇²u = 0 be solved by specifying an initial condition u(x,y,0) and marching forward in time?"
  type: multiple-choice
  options:
    - "Because Laplace's equation requires Fourier series, which are defined only on bounded domains"
    - "Because Laplace's equation has no time variable — it describes a steady state, and the solution at any interior point depends on the entire boundary simultaneously"
    - "Because Laplace's equation is nonlinear, making time-marching unstable"
    - "Because time-marching only fails near the boundaries; interior points can be solved sequentially"
  answer: 1
  explanation: "Laplace's equation is elliptic: it has no time derivative and describes equilibrium, not evolution. The solution at any interior point depends on conditions on the entire boundary, not on an initial state. This is structurally different from parabolic PDEs (heat equation) or hyperbolic PDEs (wave equation), which have time derivatives and can be stepped forward from initial data. For elliptic PDEs, boundary conditions on the entire closed boundary must be specified and the whole domain solved simultaneously."

- question: "A metal plate has its edges held at fixed temperatures. After a very long time, the temperature distribution no longer changes. Which statement correctly describes the governing equation at steady state?"
  type: multiple-choice
  options:
    - "The heat equation ∂u/∂t = α∇²u still applies, but with ∂u/∂t ≈ 0 for practical purposes"
    - "The temperature satisfies ∇²u = 0 exactly — the steady-state distribution is a harmonic function"
    - "The wave equation governs the steady state because temperature disturbances propagate outward"
    - "No differential equation applies at steady state; the temperature is simply whatever the boundary conditions dictate"
  answer: 1
  explanation: "At steady state, ∂u/∂t = 0 exactly. Substituting into the heat equation gives α∇²u = 0, which (since α ≠ 0) reduces to Laplace's equation ∇²u = 0. The steady-state temperature is precisely a harmonic function. This is how Laplace's equation arises physically: it is what remains of the heat equation after all transients die away and time evolution has stopped."

- question: "A solution to Laplace's equation on a bounded domain can achieve its maximum value at an interior point of the domain."
  type: true-false
  answer: false
  explanation: "The maximum principle states that harmonic functions achieve their maximum and minimum values on the boundary of the domain, not in the interior — unless the function is constant throughout. Physically, the temperature at any interior point of a steady-state plate is a weighted average of nearby temperatures and cannot exceed the maximum boundary temperature. This principle also explains why Dirichlet boundary conditions uniquely determine the solution: the boundary controls the interior completely."

- question: "Laplace's equation can be understood as the time-independent limit of the heat equation, representing the distribution that the heat equation approaches as t → ∞."
  type: true-false
  answer: true
  explanation: "The heat equation ∂u/∂t = α∇²u describes evolution from an initial distribution. As t → ∞, the distribution converges to a steady state where ∂u/∂t = 0, yielding ∇²u = 0 — Laplace's equation. This connection is general: Laplace's equation characterizes the equilibrium of any diffusive process. The same relationship holds for the Poisson equation ∇²u = f, which describes steady states with sources."

- question: "Explain why Laplace's equation requires boundary conditions on the entire closed boundary, whereas the wave equation requires initial conditions at a single time. What structural difference accounts for this?"
  type: short-answer
  answer: "The wave equation is hyperbolic: it has two time derivatives, and disturbances propagate at finite speed from initial data. Specifying u and ∂u/∂t at t=0 determines the future because information flows forward. Laplace's equation is elliptic: it has no time variable, and the value at any interior point depends on conditions in all directions simultaneously. The solution is not built from one boundary inward — it is determined by a global balance. Specifying conditions on only part of the boundary leaves the problem underdetermined; the entire boundary must be constrained."
  explanation: "This structural difference — hyperbolic vs. elliptic — determines computational strategy as well. A hyperbolic problem can be solved step by step in time; an elliptic problem requires solving a large coupled system simultaneously. Numerically, Laplace's equation leads to sparse linear systems (finite difference or finite element methods), while wave equations can use explicit time-stepping. The physics matches the math: equilibrium is a global property, while propagation is a local, sequential one."
```

## Explainer

**Laplace's equation** ∇²u = 0 describes the state a system reaches after all transients have died away — the equilibrium. Think of a metal plate with its edges held at fixed temperatures. Initially, the temperature distribution throughout the plate changes over time (governed by the heat equation, a parabolic PDE). But as t → ∞, the plate reaches a steady state where ∂u/∂t = 0 and the temperature distribution no longer evolves. That steady-state distribution is exactly a solution to Laplace's equation. The same mathematics governs electric potential in a charge-free region, gravitational potential outside massive bodies, and steady fluid flow.

The contrast with the wave equation (your prerequisite) is instructive. The wave equation ∂²u/∂t² = c²∇²u involves two time derivatives and describes propagation: disturbances travel outward, and the current state of the system depends on how it started and evolved. Laplace's equation has no time variable at all. It is **elliptic**: information about the solution at any point depends on conditions everywhere on the boundary simultaneously, not just nearby or upstream. This is the key structural difference — you cannot march a Laplace solution forward in time or from one boundary. You must specify conditions on the entire boundary and solve everywhere at once.

The three types of **boundary conditions** specify different physical information. **Dirichlet conditions** specify the value of u on the boundary (e.g., fixed temperature). **Neumann conditions** specify the normal derivative ∂u/∂n (e.g., heat flux through the boundary). **Robin conditions** mix both. For Laplace's equation in a bounded domain, a Dirichlet or Neumann boundary condition on a closed boundary uniquely determines the solution (by the maximum principle: harmonic functions achieve their max and min on the boundary, not in the interior).

Solving Laplace's equation analytically typically uses **separation of variables**, which you've already seen for the wave equation. For example, in a rectangle, assume u(x,y) = X(x)Y(y); substituting gives X''/X = −Y''/Y = constant. This splits into two ordinary differential equations, each solved by sinusoidal or exponential functions depending on the sign of the constant. Applying boundary conditions selects which eigenfunctions are permitted and determines their coefficients via Fourier series. On more complex geometries (circles, spheres), the same method leads to Bessel functions or Legendre polynomials — different families of eigenfunctions appropriate to the geometry. The essential idea is always the same: decompose the boundary data into modes, solve for each mode separately, and superpose.
