---
id: heisenberg-uncertainty-principle
title: Heisenberg Uncertainty Principle
domain: physics
course: modern-physics
prerequisites:
- id: wave-particle-duality
  type: hard
- id: de-broglie-wavelength
  type: hard
builds-toward:
- wavefunction-and-probability
- quantum-tunneling
tags:
- quantum
- uncertainty
- position
- momentum
- measurement
stage: advanced
status: draft
---

# Heisenberg Uncertainty Principle

## Core Idea
Heisenberg's uncertainty principle states that the standard deviations of position and momentum satisfy Δx · Δp ≥ ℏ/2, and similarly for energy and time: ΔE · Δt ≥ ℏ/2. This is not a limitation of measurement technology but a fundamental property of quantum systems: a state with well-defined position has an inherently spread-out momentum distribution and vice versa. The principle follows from the wave nature of matter — a localized wave packet requires a superposition of many wavelengths (momenta).

## How It's Best Learned
Derive the position-momentum uncertainty from Fourier analysis: a narrow wave packet requires broad frequency (momentum) content. Apply to the ground-state energy of a particle in a box or the hydrogen atom to see that quantum confinement forces nonzero kinetic energy.

## Common Misconceptions
- The uncertainty principle is about disturbing the particle during measurement — that was Heisenberg's original heuristic but the true basis is Fourier mathematics, not disturbance.
- Better instruments could beat the uncertainty limit — no instrument can, even in principle; the limit is irreducible.
- Position and momentum are not the only conjugate pair — energy and time are another, and the time-energy form explains the natural linewidth of spectral lines.
