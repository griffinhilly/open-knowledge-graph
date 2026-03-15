---
id: wave-equation-one-dimensional
title: The One-Dimensional Wave Equation
domain: physics
course: waves-and-optics
prerequisites:
- id: partial-derivatives
  type: hard
- id: chain-rule-multivariable
  type: hard
- id: wave-equation-pde
  type: hard
builds-toward:
- harmonic-wave-time-dependence
- plane-electromagnetic-waves
tags:
- waves
- pde
- mathematics
stage: formal-systems
status: draft
---

# The One-Dimensional Wave Equation

## Core Idea
The wave equation ∂²u/∂t² = v²∂²u/∂x² describes how wave displacement evolves in space and time. Any function of the form u(x,t) = f(x - vt) + g(x + vt) satisfies this equation, representing waves traveling in both directions at speed v. This fundamental equation emerges from Newton's laws applied to continuous media and is the basis for understanding all linear wave phenomena.

## How It's Best Learned
Derive it for a vibrating string using force balance on a small element. Then verify that sinusoidal and simple linear functions satisfy it.

## Common Misconceptions
The wave equation is not the same as the equation of motion for a simple harmonic oscillator—the double spatial derivative encodes how neighboring regions couple.
