---
id: phasor-conversion-and-representation
title: Phasor Conversion and Representation
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: sinusoidal-AC-steady-state-fundamentals
  type: hard
- id: complex-exponential-form
  type: hard
builds-toward:
- complex-impedance-networks-ac
- AC-Kirchhoff-laws-phasor-domain
tags:
- phasors
- complex-representation
- frequency-domain
stage: formal-systems
status: draft
---

# Phasor Conversion and Representation

## Core Idea
A phasor is a complex number representing the amplitude and phase of a sinusoid. The transformation v(t) = Re[V̅ e^(jωt)] converts time-domain sinusoids to frequency-domain phasors V̅ = |V|e^(jφ). This greatly simplifies AC circuit analysis by converting differential equations into algebraic equations.

## How It's Best Learned
Practice converting between time-domain and phasor domains. Use Euler's formula e^(jθ) = cos(θ) + j sin(θ) to move between rectangular and polar forms. Verify using circuit simulations.

## Common Misconceptions
- Phasors only apply to single-frequency signals. - A phasor magnitude is the same as peak voltage; RMS values are used in phasors. - Phasor addition in the complex plane is vector addition, not scalar addition.
