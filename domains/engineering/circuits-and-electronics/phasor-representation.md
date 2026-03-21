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

## Questions

```yaml
- question: "A sinusoidal source has been driving an RC circuit for a very long time. A student wants to find the current amplitude and phase. Which approach is appropriate?"
  type: multiple-choice
  options:
    - "Solve the full differential equation including both transient and steady-state terms"
    - "Phasor analysis — the transient has decayed and only the sinusoidal steady-state response remains"
    - "Phasor analysis combined with Laplace transforms to capture the complete response"
    - "DC analysis using the source's peak voltage as a constant"
  answer: 1
  explanation: "After a circuit has run for a long time, transients (the natural response driven by initial energy storage) have decayed to zero. What remains is exactly the sinusoidal steady-state response — which phasors are designed to compute. There is no need for a full differential equation or Laplace analysis. Option A is correct in general but unnecessary here. Options C and D are incorrect: Laplace is needed for the complete response including transients; DC analysis ignores reactance entirely."

- question: "Why does phasor analysis convert differential equations into algebraic equations?"
  type: multiple-choice
  options:
    - "Phasors average over time, so the time derivative vanishes"
    - "In steady state, voltages and currents are constant, so their derivatives are zero"
    - "Differentiation in the time domain corresponds to multiplication by jω in the phasor domain"
    - "Complex numbers encode phase information, eliminating the need to solve for initial conditions"
  answer: 2
  explanation: "The algebraic key is that d/dt[Re{V·e^(jωt)}] = Re{jω·V·e^(jωt)}. Differentiation in time maps to multiplication by jω on the phasor. This means the voltage-current relationship for a capacitor (i = C·dv/dt) becomes I = jωC·V in the phasor domain — an algebraic equation. Similarly, inductors become V = jωL·I. Every reactive element gets an impedance Z = V/I, and the entire DC analysis toolkit (Kirchhoff's laws, superposition, Thevenin) applies directly. Options A and B are wrong: phasors don't average over time, and in sinusoidal steady state, voltages are not constant — they oscillate."

- question: "Phasor analysis gives the complete response of a circuit, capturing both the transient behavior immediately after switching and the long-term steady-state behavior."
  type: true-false
  answer: false
  explanation: "Phasors yield only the sinusoidal steady-state (particular) solution — the response after all transients have decayed. The complete response is the sum of the particular solution (phasor) and the homogeneous solution (natural response, which decays over time). Immediately after a source is switched on, energy stored in capacitors and inductors drives transient currents that are not captured by phasors. Using a phasor solution to describe circuit behavior right after switching is a consequential error."

- question: "A capacitor with impedance 1/(jωC) presents lower opposition to current at higher frequencies, behaving more like a short circuit as frequency increases."
  type: true-false
  answer: true
  explanation: "The magnitude of the capacitor's impedance is |Z_C| = 1/(ωC). As frequency ω increases, this magnitude decreases toward zero — a short circuit. Intuitively, a capacitor blocks DC (ω = 0, infinite impedance) but passes high-frequency signals easily. This frequency-dependent behavior is why capacitors are used in filters: they block low frequencies and pass high ones. The dual behavior holds for inductors: Z_L = jωL increases with frequency, so inductors short low frequencies and block high ones."

- question: "A student analyzes an RC circuit with a phasor method immediately after a switch is closed at t = 0. What is wrong with this approach, and under what conditions would phasor analysis give correct results?"
  type: short-answer
  answer: "Phasors describe only the sinusoidal steady-state response — the behavior after all transients have decayed. Immediately after the switch closes, the capacitor has an initial voltage (or zero charge) that drives a transient current governed by the circuit's time constant τ = RC. This transient is the homogeneous solution to the circuit's differential equation and is not captured by phasors. Phasor analysis gives correct results only after t >> τ, when the transient has decayed to negligible amplitude and the circuit's response is dominated by the forced sinusoidal response."
  explanation: "The complete response is: v(t) = v_transient(t) + v_steady-state(t). Phasors compute only the second term. For many engineering applications — power systems at 60 Hz operating in steady state, audio circuits processing continuous signals — the transient is brief and phasors are sufficient. But for circuits that switch on and off repeatedly, or for precise timing applications, the transient response must be computed separately."
```

## Explainer

The problem phasors solve is fundamental: circuits containing capacitors and inductors obey differential equations. Apply a sinusoidal voltage to an RC circuit and the current doesn't follow the voltage instantaneously — it leads or lags depending on the elements and frequency. Solving these differential equations from scratch for every circuit is technically correct but operationally tedious. Phasors provide a systematic shortcut that converts the entire problem into complex algebra, exploiting the mathematical structure of sinusoids.

Start with Euler's formula from your prerequisites: e^(jθ) = cos(θ) + j·sin(θ). A sinusoid v(t) = Vm·cos(ωt + φ) is the real part of Vm·e^(j(ωt+φ)) = Vm·e^(jφ)·e^(jωt). The factor e^(jωt) is identical for every signal in a single-frequency circuit — it's the shared "carrier." The **phasor** V = Vm∠φ = Vm·e^(jφ) captures the distinctive information: amplitude and phase. When you want the actual time-domain signal back, you multiply by e^(jωt) and take the real part. The phasor is a compressed representation, and the compression is lossless for single-frequency analysis.

The reason phasors eliminate differential equations is a single algebraic fact. If v(t) = Re{V·e^(jωt)}, then dv/dt = Re{jω·V·e^(jωt)}. In the phasor domain, **differentiation becomes multiplication by jω** — a purely algebraic operation. This means voltage-current relationships for reactive elements simplify into Ohm's-law-like forms: for a capacitor, I = jωC·V; for an inductor, V = jωL·I. You can define **impedance** Z = V/I for any element — R for a resistor, 1/(jωC) for a capacitor, jωL for an inductor — and then apply every tool from resistive circuit analysis: series and parallel combinations, voltage dividers, mesh currents, node voltages. The entire DC analysis toolkit transfers to AC circuits through this substitution.

One boundary requires careful attention: **phasors describe only the sinusoidal steady state**. When a source is first connected, the circuit passes through a transient phase as it settles toward the sinusoidal response. This transient, driven by the circuit's natural response (energy stored in capacitors and inductors), decays on the timescale of the circuit's time constants. Phasor analysis does not capture this period — it describes the behavior *after* transients have died out. For many engineering applications — power systems, audio circuits, radio frequency analysis — the transient is brief and the steady state is what matters. But using a phasor solution to describe a circuit's behavior immediately after switching is a consequential error. The complete response is the sum of the particular (phasor) solution and the homogeneous (natural) response, and phasors give only the first part.
