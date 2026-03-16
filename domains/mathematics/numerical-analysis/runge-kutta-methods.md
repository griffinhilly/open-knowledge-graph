---
id: runge-kutta-methods
title: Runge-Kutta Methods
domain: mathematics
course: numerical-analysis
prerequisites:
- id: eulers-method-convergence
  type: hard
builds-toward:
- multistep-methods-adams
- stiff-equations
tags:
- runge-kutta
- ode
- high-order
stage: abstract-reasoning
status: draft
---

# Runge-Kutta Methods

## Core Idea
Runge-Kutta methods use intermediate (stage) evaluations of f to improve accuracy. The classical 4th-order RK4 achieves error O(h⁵) with four function evaluations per step. RK methods are explicit (computing stages sequentially) or implicit (solving systems), with explicit methods simpler but sensitive to stiffness. RK methods are the workhorse of ODE solving due to their simplicity and effectiveness.

## Explainer

From Euler's method, you know the simplest approach: take a step of size h, evaluate f at the current point, and move in that direction. The local truncation error is O(h²) — accuracy improves only linearly as you reduce the step size. Euler's method is easy to understand but slow to converge. Runge-Kutta methods use the same idea but squeeze much more accuracy out of each step by evaluating f at several intermediate points within the step interval.

The strategy is analogous to numerical integration. Euler's method is like the rectangle rule — it approximates the area under a curve using only the left endpoint. Higher-order methods sample f at more points within [tₙ, tₙ + h] and combine those samples with carefully chosen weights, like Simpson's rule uses three points for better accuracy. Each evaluation of f at an intermediate point is called a **stage**. The classical **RK4** method uses four stages:

- k₁ = f(tₙ, yₙ) — slope at the start
- k₂ = f(tₙ + h/2, yₙ + h·k₁/2) — slope at the midpoint, estimated using k₁
- k₃ = f(tₙ + h/2, yₙ + h·k₂/2) — slope at the midpoint, refined using k₂
- k₄ = f(tₙ + h, yₙ + h·k₃) — slope at the endpoint, estimated using k₃

The update is yₙ₊₁ = yₙ + (h/6)(k₁ + 2k₂ + 2k₃ + k₄). This weighted average of four slopes achieves local error O(h⁵) and global error O(h⁴) — hence "4th-order." Halving the step size reduces the error by a factor of 16, compared to a factor of 2 for Euler's method.

The design of RK4 is not arbitrary. It's engineered so that a Taylor expansion of yₙ₊₁ matches the true solution's Taylor series through the h⁴ term. The weights (1, 2, 2, 1)/6 echo Simpson's rule exactly — no coincidence, since both are solving the same approximation problem. **Explicit** RK methods (like RK4) compute each stage directly from previously computed stages. **Implicit** methods allow stages to depend on each other, requiring a small system to be solved at each step — more expensive, but essential for **stiff equations** where explicit methods require prohibitively small step sizes to remain stable. RK4 is the default tool for smooth, non-stiff ODEs: four evaluations per step, no linear algebra, and accuracy that handles most practical problems with reasonable step sizes.
