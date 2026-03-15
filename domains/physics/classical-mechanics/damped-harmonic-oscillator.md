---
id: damped-harmonic-oscillator
title: Damped Harmonic Oscillator
domain: physics
course: classical-mechanics
prerequisites:
- id: simple-harmonic-motion
  type: hard
- id: friction-forces
  type: soft
- id: higher-order-linear-odes
  type: hard
- id: second-order-linear-homogeneous-odes
  type: hard
- id: characteristic-equation-method
  type: hard
- id: differential-equations-intro
  type: hard
- id: exponential-functions-and-graphs
  type: soft
- id: complex-roots-oscillatory-solutions
  type: hard
- id: complex-numbers-intro
  type: soft
builds-toward:
- driven-harmonic-oscillator
tags:
- oscillations
- damping
- friction
- differential-equations
stage: formal-systems
status: draft
---

# Damped Harmonic Oscillator

## Core Idea
A damped oscillator experiences a restoring force (−kx) and velocity-dependent friction (−bv). The equation m d²x/dt² + b dx/dt + kx = 0 exhibits three regimes: underdamped (oscillates while decaying), critically damped (no oscillation, fastest return to equilibrium), and overdamped (slow decay without oscillation). Damping reduces the oscillation frequency compared to the undamped case.
