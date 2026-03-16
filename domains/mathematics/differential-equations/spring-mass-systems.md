---
id: spring-mass-systems
title: Spring-Mass Systems and Mechanical Vibrations
domain: mathematics
course: differential-equations
prerequisites:
- id: complex-roots-oscillatory-solutions
  type: hard
- id: second-order-linear-homogeneous-odes
  type: hard
builds-toward:
- resonance-and-damping
tags:
- applications
- mechanics
- vibrations
stage: formal-systems
status: draft
---

# Spring-Mass Systems and Mechanical Vibrations

## Core Idea
A spring-mass system with mass m, spring constant k, and damping c is governed by m(d²x/dt²) + c(dx/dt) + kx = F(t). Solutions are underdamped (oscillatory decay), critically damped (limiting case), or overdamped (non-oscillatory decay). The natural frequency ω₀ = √(k/m) characterizes unforced motion. This model is foundational across engineering and physics.

## Explainer

You've solved second-order linear homogeneous ODEs with constant coefficients, and you know that complex characteristic roots produce oscillatory solutions involving sine and cosine. The spring-mass system is the physical model that motivated the entire theory — a mass on a spring is the archetypal oscillator, and its equation of motion is exactly the second-order ODE you've been studying in the abstract.

**Newton's second law** applied to a mass m on a spring gives three contributions to net force. The spring exerts a restoring force -kx proportional to displacement (Hooke's Law, k > 0). A damper (friction, air resistance) exerts a force -c(dx/dt) proportional to velocity and opposing motion (c ≥ 0). An external driver contributes F(t). Summing: m·x'' = -kx - c·x' + F(t), which rearranges to **m·x'' + c·x' + kx = F(t)**. For unforced motion (F = 0), the characteristic equation is mr² + cr + k = 0. The discriminant Δ = c² - 4mk determines which regime you're in.

The three regimes correspond directly to the three cases of characteristic roots. **Underdamping** (c² < 4mk): complex roots r = -c/(2m) ± iω_d where ω_d = √(k/m - c²/(4m²)) is the **damped natural frequency**. The solution is e^(-ct/2m)[A cos(ω_d t) + B sin(ω_d t)] — oscillation with exponentially decaying amplitude. A car suspension, a pendulum in air, or a clock spring are all underdamped. **Critical damping** (c² = 4mk): repeated real root r = -c/(2m), solution (A + Bt)e^(-ct/2m). The mass returns to equilibrium as fast as possible without oscillating — the ideal behavior for door closers and high-performance shock absorbers. **Overdamping** (c² > 4mk): two distinct negative real roots, solution decays without oscillating, but more sluggishly than critical damping.

The **natural frequency** ω₀ = √(k/m) tells you how fast an undamped system would oscillate: heavier mass means slower oscillation, stiffer spring means faster oscillation. With no damping and no forcing, the solution is pure sinusoidal — x(t) = A cos(ω₀t) + B sin(ω₀t) — perpetual oscillation at ω₀. This idealized model is the foundation for every mechanical vibration problem in engineering. The same ODE structure, the same three damping regimes, and the same natural frequency concept appear in electrical circuits (where inductance, resistance, and capacitance replace mass, damping, and spring constant), structural analysis, acoustics, and quantum mechanics.
