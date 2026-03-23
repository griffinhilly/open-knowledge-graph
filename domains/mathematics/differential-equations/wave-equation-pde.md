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
status: validated
---

# The Wave Equation and Vibrating Strings

## Core Idea
The wave equation ∂²u/∂t² = c²∂²u/∂x² models vibrating string displacement u(x,t) with wave speed c. It is hyperbolic, with solutions exhibiting finite propagation speed (revealed by d'Alembert's formula). Initial conditions specify u and ∂u/∂t at t = 0; boundary conditions model fixed or free ends. Solutions consist of rightward and leftward traveling waves that reflect at boundaries.

## Questions

```yaml
- question: "At time t=0, a violin string is displaced only near its midpoint and is undisturbed everywhere else. A student claims that the entire string, including the endpoints, will begin moving at the same instant t=0⁺ because it is a connected, continuous object. Is this consistent with the wave equation?"
  type: multiple-choice
  options:
    - "Yes — on a connected string, any local displacement instantaneously propagates everywhere."
    - "No — the wave equation has finite propagation speed c; points far from the disturbance are unaffected until the wavefront arrives at time t = distance/c."
    - "No — the wave equation predicts that disturbances do not propagate at all in a bounded medium."
    - "Yes, but only for an infinitely long string; on a finite string, reflections create instantaneous coupling."
  answer: 1
  explanation: "The wave equation is a hyperbolic PDE with finite propagation speed c. D'Alembert's formula makes this explicit: u(x,t) = φ(x+ct) + ψ(x−ct), meaning information travels at exactly speed c. A disturbance at x₀ at time 0 only reaches position x at time t = |x−x₀|/c. This is fundamentally different from the heat equation (parabolic), where a disturbance instantaneously affects all points — a common source of confusion between hyperbolic and parabolic PDEs."

- question: "D'Alembert's formula writes the general solution to the wave equation as u(x,t) = φ(x+ct) + ψ(x−ct). What is the correct physical interpretation of the two terms?"
  type: multiple-choice
  options:
    - "φ represents the amplitude envelope and ψ represents the frequency content of the wave."
    - "φ(x+ct) is a wave traveling in the negative x-direction and ψ(x−ct) is a wave traveling in the positive x-direction."
    - "Both terms represent standing waves that oscillate in place without net movement."
    - "φ and ψ are determined entirely by boundary conditions and carry no information about initial conditions."
  answer: 1
  explanation: "In φ(x+ct), as time t increases, the argument stays constant when x decreases — meaning the pattern moves in the negative x-direction (leftward) at speed c. In ψ(x−ct), the argument is constant when x increases with t — a rightward-traveling wave. Every solution to the wave equation is a superposition of these two counter-propagating traveling waves. Initial conditions (displacement and velocity at t=0) determine φ and ψ; boundary conditions then cause reflections."

- question: "A disturbance introduced at position x=0 at time t=0 in a medium governed by the wave equation with speed c cannot affect the displacement at position x=L until time t = L/c."
  type: true-false
  answer: true
  explanation: "This is the finite propagation speed property of the wave equation, encoded directly in d'Alembert's formula. The wavefront travels at exactly speed c. Before time L/c, the wave has not yet reached x=L, so the displacement there remains zero. This locality property distinguishes the wave equation (hyperbolic) from the heat equation (parabolic), where disturbances propagate instantaneously."

- question: "Like the heat equation, the wave equation predicts that a local disturbance propagates to all other positions instantaneously, though the effect diminishes rapidly with distance."
  type: true-false
  answer: false
  explanation: "This describes the heat equation (parabolic), not the wave equation (hyperbolic). The heat equation exhibits infinite propagation speed — a temperature change at one point mathematically affects all other points at any positive time t, though the effect decays exponentially with distance. The wave equation, by contrast, has strictly finite propagation speed c: a point at distance d is completely unaffected until time t = d/c. This distinction between hyperbolic and parabolic PDEs is one of the most important in mathematical physics."

- question: "What does d'Alembert's formula reveal about the structure of wave solutions on an infinite domain, and why is this more physically transparent than the normal mode (separation of variables) decomposition?"
  type: short-answer
  answer: "D'Alembert's formula u(x,t) = φ(x+ct) + ψ(x−ct) shows that every solution is a superposition of exactly two traveling waves — one moving left, one moving right — each maintaining its shape at speed c. The solution at (x,t) depends only on initial data in the interval [x−ct, x+ct], making the finite propagation speed and causal structure immediately visible. The normal mode decomposition expresses solutions as standing waves (sinusoids in space times sinusoids in time), which are useful for resonance and frequency analysis but obscure the fact that disturbances travel. D'Alembert's approach is better for understanding signal propagation and causality; normal modes are better for studying the harmonic content of bounded systems."
  explanation: "The key contrast is traveling waves (d'Alembert) vs. standing waves (separation of variables). Both are valid representations of the same solutions, but the traveling-wave picture makes causality and finite propagation speed transparent."
```

## Explainer

You've used separation of variables to turn a PDE into two ODEs, and you know how to take partial derivatives. The **wave equation** ∂²u/∂t² = c²∂²u/∂x² is the classic hyperbolic PDE, modeling how disturbances — on a string, in air, in an electromagnetic field — propagate through space at a finite speed c. The unknown u(x, t) is the displacement at position x and time t; the constant c is the wave speed, determined by physical properties like string tension and density.

The most illuminating solution is **d'Alembert's formula**: every solution can be written as u(x, t) = φ(x + ct) + ψ(x − ct) for arbitrary twice-differentiable functions φ and ψ. This says the general solution is a superposition of two waves — one traveling left (x + ct grows as t increases for fixed observer moving left) and one traveling right. Plug in initial conditions u(x, 0) = f(x) and ∂u/∂t(x, 0) = g(x): you get φ + ψ = f and c(φ′ − ψ′) = g, which you can solve algebraically for φ and ψ. The finite propagation speed c is built in: a disturbance at x = 0 at t = 0 only reaches position x at time t = |x|/c. This is fundamentally different from the heat equation, where a disturbance at one point instantaneously affects all others.

On a bounded domain — say a string fixed at x = 0 and x = L — the boundary conditions u(0, t) = 0 and u(L, t) = 0 restrict which solutions exist. The separation of variables approach writes u(x, t) = X(x)T(t), divides through by X(x)T(t), and separates: X″/X = T″/(c²T) = −λ. The boundary conditions on X force λ = (nπ/L)² for n = 1, 2, 3, ..., giving spatial modes Xₙ(x) = sin(nπx/L). Each temporal part is Tₙ(t) = Aₙ cos(nπct/L) + Bₙ sin(nπct/L). These **normal modes** are the natural frequencies of the string: the n = 1 mode vibrates at frequency c/(2L), and higher modes vibrate at integer multiples.

The full solution is a superposition of all normal modes: u(x, t) = Σ [Aₙ sin(nπx/L) cos(nπct/L) + Bₙ sin(nπx/L) sin(nπct/L)]. The coefficients Aₙ and Bₙ are determined by matching the initial displacement f(x) and initial velocity g(x) via Fourier series. This decomposition reveals the physics: the "timbre" of a vibrating string — its harmonic content — is encoded in these coefficients. A string plucked gently near its center excites mainly low harmonics; plucked sharply near the end excites many harmonics. The wave equation and its normal mode decomposition underlie acoustics, optics, and quantum mechanics, making it one of the most consequential PDEs in all of physics.
