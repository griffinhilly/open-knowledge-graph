---
id: phasor-representation
title: Phasors and Sinusoidal Steady-State Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: capacitor-inductor-energy-storage
  type: hard
- id: complex-numbers-intro
  type: hard
- id: operations-with-complex-numbers
  type: hard
- id: ac-circuits-fundamentals
  type: soft
builds-toward:
- impedance-analysis
- ac-circuit-analysis-methods
tags:
- phasors
- sinusoidal-steady-state
- complex-numbers
- frequency-domain
- Euler-formula
stage: formal-systems
status: draft
---

# Phasors and Sinusoidal Steady-State Analysis

## Core Idea
A phasor is a complex number encoding the amplitude and phase of a sinusoid, transforming time-domain differential equations into algebraic equations. The sinusoid v(t) = Vm·cos(ωt + φ) corresponds to the phasor V = Vm∠φ = Vm·e^(jφ). Differentiation in the time domain (d/dt) becomes multiplication by jω in the phasor domain, eliminating differential equations for sinusoidal steady-state analysis. Phasors represent only the steady-state response after transients have decayed; they do not capture the natural response.

## How It's Best Learned
Convert several sinusoids to phasors and back. Verify using Euler's formula: e^(jθ) = cos(θ) + j·sin(θ). Practice adding phasors graphically using phasor diagrams before applying them to circuits with multiple elements.

## Common Misconceptions
- Mixing peak-value phasors and RMS phasors in the same calculation — choose one convention and maintain it throughout.
- Applying phasors to transient analysis — phasors yield only the sinusoidal steady-state response.
- Confusing the phasor angle with frequency — the phasor angle is phase, while ω is a fixed parameter of the analysis.
