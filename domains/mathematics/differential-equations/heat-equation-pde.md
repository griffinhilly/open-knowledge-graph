---
id: heat-equation-pde
title: The Heat Equation and Diffusion Problems
domain: mathematics
course: differential-equations
prerequisites:
- id: even-odd-extensions-fourier
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- separation-variables-pde
tags:
- heat-equation
- pde
- parabolic
stage: advanced
status: draft
---

# The Heat Equation and Diffusion Problems

## Core Idea
The heat equation ∂u/∂t = k∂²u/∂x² models temperature diffusion in a rod. It is parabolic (time derivative is first-order, space derivative second-order), causing solutions to smoothly approach a steady state. The diffusion coefficient k controls the equilibration speed. Boundary and initial conditions fully determine the problem. Solutions decay exponentially in time, approaching their boundary values.
