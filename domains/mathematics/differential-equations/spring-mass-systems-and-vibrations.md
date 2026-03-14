---
id: spring-mass-systems-and-vibrations
title: Spring-Mass Systems and Mechanical Vibrations
domain: mathematics
course: differential-equations
prerequisites:
- id: second-order-linear-homogeneous-odes
  type: hard
- id: complex-roots-oscillatory-solutions
  type: hard
builds-toward:
- damping-and-resonance
tags:
- application
- mechanics
- modeling
stage: advanced
status: draft
---

# Spring-Mass Systems and Mechanical Vibrations

## Core Idea
A mass m attached to a spring with spring constant k obeys Newton's second law: m·y'' = -k·y (undamped) or m·y'' + c·y' + k·y = 0 (damped). These lead to harmonic oscillator ODEs, where the characteristic roots predict oscillatory or overdamped behavior.

## How It's Best Learned
Derive the ODE from F = ma using Hooke's law. Solve for undamped motion (simple harmonic) using complex roots. Compare against real oscillation to validate predictions.

## Common Misconceptions
- Confusing the damping coefficient c with damping ratio; the ratio ζ = c / (2√(mk)) determines the qualitative behavior. - Forgetting the sign conventions (restoring force points opposite to displacement). - Not recognizing that all terms have physical meaning (stiffness, damping, inertia).
