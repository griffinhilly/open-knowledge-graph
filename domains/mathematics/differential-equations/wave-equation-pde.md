---
id: wave-equation-pde
title: The Wave Equation and Vibrating Strings
domain: mathematics
course: differential-equations
prerequisites:
- id: separation-variables-pde
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- laplaces-equation
tags:
- wave-equation
- pde
- hyperbolic
stage: advanced
status: draft
---

# The Wave Equation and Vibrating Strings

## Core Idea
The wave equation ∂²u/∂t² = c²∂²u/∂x² models vibrating string displacement u(x,t) with wave speed c. It is hyperbolic, with solutions exhibiting finite propagation speed (revealed by d'Alembert's formula). Initial conditions specify u and ∂u/∂t at t = 0; boundary conditions model fixed or free ends. Solutions consist of rightward and leftward traveling waves that reflect at boundaries.

## Explainer

You've used separation of variables to turn a PDE into two ODEs, and you know how to take partial derivatives. The **wave equation** ∂²u/∂t² = c²∂²u/∂x² is the classic hyperbolic PDE, modeling how disturbances — on a string, in air, in an electromagnetic field — propagate through space at a finite speed c. The unknown u(x, t) is the displacement at position x and time t; the constant c is the wave speed, determined by physical properties like string tension and density.

The most illuminating solution is **d'Alembert's formula**: every solution can be written as u(x, t) = φ(x + ct) + ψ(x − ct) for arbitrary twice-differentiable functions φ and ψ. This says the general solution is a superposition of two waves — one traveling left (x + ct grows as t increases for fixed observer moving left) and one traveling right. Plug in initial conditions u(x, 0) = f(x) and ∂u/∂t(x, 0) = g(x): you get φ + ψ = f and c(φ′ − ψ′) = g, which you can solve algebraically for φ and ψ. The finite propagation speed c is built in: a disturbance at x = 0 at t = 0 only reaches position x at time t = |x|/c. This is fundamentally different from the heat equation, where a disturbance at one point instantaneously affects all others.

On a bounded domain — say a string fixed at x = 0 and x = L — the boundary conditions u(0, t) = 0 and u(L, t) = 0 restrict which solutions exist. The separation of variables approach writes u(x, t) = X(x)T(t), divides through by X(x)T(t), and separates: X″/X = T″/(c²T) = −λ. The boundary conditions on X force λ = (nπ/L)² for n = 1, 2, 3, ..., giving spatial modes Xₙ(x) = sin(nπx/L). Each temporal part is Tₙ(t) = Aₙ cos(nπct/L) + Bₙ sin(nπct/L). These **normal modes** are the natural frequencies of the string: the n = 1 mode vibrates at frequency c/(2L), and higher modes vibrate at integer multiples.

The full solution is a superposition of all normal modes: u(x, t) = Σ [Aₙ sin(nπx/L) cos(nπct/L) + Bₙ sin(nπx/L) sin(nπct/L)]. The coefficients Aₙ and Bₙ are determined by matching the initial displacement f(x) and initial velocity g(x) via Fourier series. This decomposition reveals the physics: the "timbre" of a vibrating string — its harmonic content — is encoded in these coefficients. A string plucked gently near its center excites mainly low harmonics; plucked sharply near the end excites many harmonics. The wave equation and its normal mode decomposition underlie acoustics, optics, and quantum mechanics, making it one of the most consequential PDEs in all of physics.
