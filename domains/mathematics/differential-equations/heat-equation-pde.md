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

## Questions

```yaml
- question: "A rod's initial temperature profile is a sharp spike near the center, with both endpoints held at 0°C. After a long time, what does the temperature distribution look like?"
  type: multiple-choice
  options:
    - "The spike migrates toward one endpoint and stays there"
    - "The temperature oscillates symmetrically around zero, never fully settling"
    - "The temperature smoothly decays to zero everywhere as all modes die out"
    - "The spike broadens but retains its shape indefinitely"
  answer: 2
  explanation: "With zero-temperature boundary conditions, the steady-state solution is u = 0 everywhere. Every term in the Fourier series solution carries an exponential time factor e^(−k(nπ/L)²t) that decays to zero. The spike, however sharp, is composed of many Fourier modes — each one decays exponentially, so the entire profile smoothly flattens to zero. There is no mode that sustains itself; all decay. Option D is the classic misconception: diffusion does spread the spike, but it does not preserve it — the peak amplitude also continuously shrinks."

- question: "In the heat equation solution u(x,t) = Σ bₙ sin(nπx/L) e^(−k(nπ/L)²t), why does a fine-grained initial temperature pattern smooth out faster than a broad one?"
  type: multiple-choice
  options:
    - "Fine-grained patterns have larger Fourier coefficients bₙ, so they dominate initially"
    - "Fine-grained patterns correspond to higher-n modes, whose decay rate k(nπ/L)² grows as n², making them decay much faster"
    - "Fine-grained patterns create larger temperature gradients that drive faster conduction"
    - "The diffusion constant k is larger for high-spatial-frequency components"
  answer: 1
  explanation: "The decay rate of each mode is k(nπ/L)², which grows as n² — the decay rate of the n=10 mode is 100 times that of the n=1 mode. Fine-grained patterns are dominated by large-n terms, so they decay rapidly. Broad, smooth patterns are dominated by n=1 and n=2 terms, which decay slowly. This is the mathematical reason why diffusion is a smoothing process: it preferentially destroys spatial detail. Option C is physically intuitive but does not explain the mechanism — the n² scaling in the exponent is the precise cause."

- question: "The heat equation ∂u/∂t = k∂²u/∂x² is time-reversible: if u(x,t) solves it, then u(x,−t) also solves it."
  type: true-false
  answer: false
  explanation: "This is false. Substituting t → −t gives ∂u/∂(−t) = k∂²u/∂x², i.e., −∂u/∂t = k∂²u/∂x², which is a different equation (heat flow in reverse). Physical diffusion irreversibly spreads heat from hotter to colder regions — you cannot unscramble a smoothed temperature profile by 'running it backward.' This asymmetry reflects the second law of thermodynamics. The wave equation, by contrast, IS time-reversible; this is a key distinction between parabolic (heat) and hyperbolic (wave) PDEs."

- question: "If a rod has insulated endpoints (no heat escapes), the appropriate Fourier series for the solution uses sine functions."
  type: true-false
  answer: false
  explanation: "Insulated endpoints impose the Neumann condition ∂u/∂x = 0 at x = 0 and x = L, meaning zero flux (no heat flow out). Cosine functions satisfy this condition because their derivatives at 0 and L are zero. Sine functions satisfy Dirichlet conditions (u = 0 at the endpoints, corresponding to endpoints held at zero temperature). The choice between sine and cosine series is dictated by the physical boundary conditions — a key link between the PDE, its boundary conditions, and the Fourier representation."

- question: "Explain why the solution method 'separation of variables' works for the heat equation, and what the resulting Fourier coefficients represent physically."
  type: short-answer
  answer: "Separation of variables assumes u(x,t) = X(x)T(t), substituting into the PDE and dividing produces X''/X = T'/(kT) = −λ (a constant, since both sides depend on different variables). This separates into two ODEs. The spatial ODE with boundary conditions yields a discrete set of eigenfunctions X_n(x) (e.g., sines for zero-endpoint conditions) — the natural spatial 'modes' of the rod. The temporal ODE gives exponential decay T_n(t) = e^(−kλ_n t). The Fourier coefficients bₙ represent the initial amplitude of each spatial mode — how much of the initial temperature profile f(x) 'projects onto' each eigenfunction. Each mode evolves independently, decaying at its own rate."
  explanation: "The key physical picture: any initial condition can be decomposed into spatial modes (via the Fourier representation). Once decomposed, each mode evolves independently and exponentially decays. This decomposition is possible because the heat equation is linear — modes do not interact. The Fourier coefficients bₙ are found by matching u(x,0) = f(x) to the Fourier series, which is exactly the Fourier analysis technique from the prerequisite course."
```

## Explainer

You have studied Fourier series and learned how to represent functions as sums of sines and cosines, using even and odd extensions to match boundary conditions. The heat equation is where Fourier series earn their keep: they provide the explicit solution to one of the most important partial differential equations in mathematical physics, and the choice of sine or cosine series is dictated directly by the physical boundary conditions.

The heat equation ∂u/∂t = k∂²u/∂x² models how temperature u in a thin rod evolves over time. The left side ∂u/∂t is the rate of change of temperature at a fixed location. The right side, k times the second spatial derivative, captures the curvature of the temperature profile: temperature changes fastest where the profile is most "bent" — where neighboring points differ most from the current one. A sharp hot peak spreads outward; a cold valley fills in. The equation encodes this universal flattening tendency, and k controls how quickly it occurs.

The equation is called **parabolic** because it is first-order in time and second-order in space. This asymmetry is physically meaningful: heat flows forward in time, not backward. Specifying an **initial condition** u(x, 0) = f(x) (the initial temperature profile) and **boundary conditions** (e.g., the endpoints of the rod held at fixed temperatures, or insulated so no heat escapes) fully determines the solution for all future times t > 0. Zero-temperature endpoints suggest a sine series (an odd extension); insulated endpoints suggest a cosine series (an even extension).

The solution method uses **separation of variables**: assume u(x, t) = X(x)T(t), substitute into the PDE, and separate. The spatial ODE X'' + λX = 0 with the boundary conditions produces a discrete set of **eigenvalues** λ_n and **eigenfunctions** X_n(x) = sin(nπx/L). Each eigenfunction gets its own time factor T_n(t) = e^(−k(nπ/L)²t), so the general solution is u(x, t) = Σ bₙ sin(nπx/L) e^(−k(nπ/L)²t), where the coefficients bₙ come from the Fourier sine series of the initial condition f(x). The exponential time factors reveal why the solution smoothly approaches steady state: each mode decays at its own rate, with higher-frequency modes (larger n) decaying much faster than low-frequency ones.
