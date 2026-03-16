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

## Explainer

You have studied Fourier series and learned how to represent functions as sums of sines and cosines, using even and odd extensions to match boundary conditions. The heat equation is where Fourier series earn their keep: they provide the explicit solution to one of the most important partial differential equations in mathematical physics, and the choice of sine or cosine series is dictated directly by the physical boundary conditions.

The heat equation ∂u/∂t = k∂²u/∂x² models how temperature u in a thin rod evolves over time. The left side ∂u/∂t is the rate of change of temperature at a fixed location. The right side, k times the second spatial derivative, captures the curvature of the temperature profile: temperature changes fastest where the profile is most "bent" — where neighboring points differ most from the current one. A sharp hot peak spreads outward; a cold valley fills in. The equation encodes this universal flattening tendency, and k controls how quickly it occurs.

The equation is called **parabolic** because it is first-order in time and second-order in space. This asymmetry is physically meaningful: heat flows forward in time, not backward. Specifying an **initial condition** u(x, 0) = f(x) (the initial temperature profile) and **boundary conditions** (e.g., the endpoints of the rod held at fixed temperatures, or insulated so no heat escapes) fully determines the solution for all future times t > 0. Zero-temperature endpoints suggest a sine series (an odd extension); insulated endpoints suggest a cosine series (an even extension).

The solution method uses **separation of variables**: assume u(x, t) = X(x)T(t), substitute into the PDE, and separate. The spatial ODE X'' + λX = 0 with the boundary conditions produces a discrete set of **eigenvalues** λ_n and **eigenfunctions** X_n(x) = sin(nπx/L). Each eigenfunction gets its own time factor T_n(t) = e^(−k(nπ/L)²t), so the general solution is u(x, t) = Σ bₙ sin(nπx/L) e^(−k(nπ/L)²t), where the coefficients bₙ come from the Fourier sine series of the initial condition f(x). The exponential time factors reveal why the solution smoothly approaches steady state: each mode decays at its own rate, with higher-frequency modes (larger n) decaying much faster than low-frequency ones.
