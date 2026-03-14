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
