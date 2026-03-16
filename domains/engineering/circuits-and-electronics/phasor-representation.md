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
- id: amplitude-period-phase-shift
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
status: validated
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

## Explainer

The problem phasors solve is fundamental: circuits containing capacitors and inductors obey differential equations. Apply a sinusoidal voltage to an RC circuit and the current doesn't follow the voltage instantaneously — it leads or lags depending on the elements and frequency. Solving these differential equations from scratch for every circuit is technically correct but operationally tedious. Phasors provide a systematic shortcut that converts the entire problem into complex algebra, exploiting the mathematical structure of sinusoids.

Start with Euler's formula from your prerequisites: e^(jθ) = cos(θ) + j·sin(θ). A sinusoid v(t) = Vm·cos(ωt + φ) is the real part of Vm·e^(j(ωt+φ)) = Vm·e^(jφ)·e^(jωt). The factor e^(jωt) is identical for every signal in a single-frequency circuit — it's the shared "carrier." The **phasor** V = Vm∠φ = Vm·e^(jφ) captures the distinctive information: amplitude and phase. When you want the actual time-domain signal back, you multiply by e^(jωt) and take the real part. The phasor is a compressed representation, and the compression is lossless for single-frequency analysis.

The reason phasors eliminate differential equations is a single algebraic fact. If v(t) = Re{V·e^(jωt)}, then dv/dt = Re{jω·V·e^(jωt)}. In the phasor domain, **differentiation becomes multiplication by jω** — a purely algebraic operation. This means voltage-current relationships for reactive elements simplify into Ohm's-law-like forms: for a capacitor, I = jωC·V; for an inductor, V = jωL·I. You can define **impedance** Z = V/I for any element — R for a resistor, 1/(jωC) for a capacitor, jωL for an inductor — and then apply every tool from resistive circuit analysis: series and parallel combinations, voltage dividers, mesh currents, node voltages. The entire DC analysis toolkit transfers to AC circuits through this substitution.

One boundary requires careful attention: **phasors describe only the sinusoidal steady state**. When a source is first connected, the circuit passes through a transient phase as it settles toward the sinusoidal response. This transient, driven by the circuit's natural response (energy stored in capacitors and inductors), decays on the timescale of the circuit's time constants. Phasor analysis does not capture this period — it describes the behavior *after* transients have died out. For many engineering applications — power systems, audio circuits, radio frequency analysis — the transient is brief and the steady state is what matters. But using a phasor solution to describe a circuit's behavior immediately after switching is a consequential error. The complete response is the sum of the particular (phasor) solution and the homogeneous (natural) response, and phasors give only the first part.
