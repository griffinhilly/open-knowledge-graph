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
status: draft
---

# Laplace's Equation and Boundary Value Problems

## Core Idea
Laplace's equation ∇²u = 0 (in 2D: ∂²u/∂x² + ∂²u/∂y² = 0) governs steady-state temperature, electric potential, and gravitational fields. It is elliptic with no time evolution; solutions depend entirely on boundary conditions (Dirichlet, Neumann, or Robin). Unlike parabolic and hyperbolic PDEs, elliptic equations require simultaneous solving over the entire domain, making them computationally different but essential for equilibrium problems.

## Explainer

**Laplace's equation** ∇²u = 0 describes the state a system reaches after all transients have died away — the equilibrium. Think of a metal plate with its edges held at fixed temperatures. Initially, the temperature distribution throughout the plate changes over time (governed by the heat equation, a parabolic PDE). But as t → ∞, the plate reaches a steady state where ∂u/∂t = 0 and the temperature distribution no longer evolves. That steady-state distribution is exactly a solution to Laplace's equation. The same mathematics governs electric potential in a charge-free region, gravitational potential outside massive bodies, and steady fluid flow.

The contrast with the wave equation (your prerequisite) is instructive. The wave equation ∂²u/∂t² = c²∇²u involves two time derivatives and describes propagation: disturbances travel outward, and the current state of the system depends on how it started and evolved. Laplace's equation has no time variable at all. It is **elliptic**: information about the solution at any point depends on conditions everywhere on the boundary simultaneously, not just nearby or upstream. This is the key structural difference — you cannot march a Laplace solution forward in time or from one boundary. You must specify conditions on the entire boundary and solve everywhere at once.

The three types of **boundary conditions** specify different physical information. **Dirichlet conditions** specify the value of u on the boundary (e.g., fixed temperature). **Neumann conditions** specify the normal derivative ∂u/∂n (e.g., heat flux through the boundary). **Robin conditions** mix both. For Laplace's equation in a bounded domain, a Dirichlet or Neumann boundary condition on a closed boundary uniquely determines the solution (by the maximum principle: harmonic functions achieve their max and min on the boundary, not in the interior).

Solving Laplace's equation analytically typically uses **separation of variables**, which you've already seen for the wave equation. For example, in a rectangle, assume u(x,y) = X(x)Y(y); substituting gives X''/X = −Y''/Y = constant. This splits into two ordinary differential equations, each solved by sinusoidal or exponential functions depending on the sign of the constant. Applying boundary conditions selects which eigenfunctions are permitted and determines their coefficients via Fourier series. On more complex geometries (circles, spheres), the same method leads to Bessel functions or Legendre polynomials — different families of eigenfunctions appropriate to the geometry. The essential idea is always the same: decompose the boundary data into modes, solve for each mode separately, and superpose.
