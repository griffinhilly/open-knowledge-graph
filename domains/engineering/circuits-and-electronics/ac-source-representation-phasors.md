---
id: ac-source-representation-phasors
title: AC Sources and Phasor Representation
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-variables-and-elements
  type: hard
- id: complex-numbers-intro
  type: hard
- id: complex-exponential-function
  type: soft
- id: complex-exponential-form
  type: hard
builds-toward:
- phasor-algebra-complex-impedance
- ac-circuit-analysis-methods
tags:
- ac-sources
- phasors
- ac-analysis
stage: formal-systems
status: draft
---

# AC Sources and Phasor Representation

## Core Idea
AC sources produce sinusoidal voltage and current: v(t) = V_m·sin(ωt + φ). Phasor representation converts sinusoidal signals to complex numbers in the frequency domain: V = V_m∠φ = V_m·e^(jφ). This transformation converts differential equations to algebraic equations, making AC circuit analysis practical. Phasors assume all signals operate at the same frequency, a reasonable assumption for circuits with one source frequency.

## Explainer

You've worked with DC circuits where voltages and currents are constant. AC circuits introduce a new complication: voltages and currents vary sinusoidally with time. A sinusoidal voltage v(t) = V_m·sin(ωt + φ) has three properties you need to track simultaneously: its **amplitude** V_m (peak value), its **angular frequency** ω (how fast it oscillates, in radians per second), and its **phase** φ (where in its cycle it starts at t = 0). Analyzing circuits with reactive elements under sinusoidal excitation means solving differential equations — the current through a capacitor is C·dv/dt, the voltage across an inductor is L·di/dt. Doing this from scratch for every circuit would be prohibitively tedious.

**Phasor representation** is the key simplification. If you know that every signal in a circuit oscillates at the same frequency ω — a reasonable assumption when there is one AC source — then the only information that distinguishes one signal from another is its amplitude and phase. The phasor for v(t) = V_m·sin(ωt + φ) is simply the complex number V = V_m∠φ = V_m·e^(jφ). You have encoded all the relevant information into a single complex number, stripping away the time-varying factor e^(jωt) that is identical for every signal in the circuit.

The power of this representation becomes apparent when you differentiate. In the time domain, differentiating a sinusoid gives another sinusoid at the same frequency but with shifted phase and scaled amplitude. In the phasor domain, this corresponds to multiplying by jω — a purely algebraic operation. This is the central insight: **differential equations in the time domain become algebraic equations in the phasor domain**. Kirchhoff's voltage and current laws still hold, but now applied to complex numbers rather than time-varying functions. Series and parallel combinations, voltage dividers, node voltage analysis — all of the techniques you know from resistive circuits carry over to AC circuits once you replace resistances with complex **impedances**: R for resistors, 1/(jωC) for capacitors, and jωL for inductors.

The connection to complex exponentials (your prerequisite) is what makes this rigorous rather than a computational trick. Euler's formula gives e^(jθ) = cos(θ) + j·sin(θ), so a sinusoid is the real part of a rotating complex exponential: V_m·cos(ωt + φ) = Re{V_m·e^(jφ)·e^(jωt)}. The phasor V = V_m·e^(jφ) is the complex amplitude — the "snapshot" of the rotating vector at t = 0. When you solve a circuit in the phasor domain and want the time-domain answer, you attach e^(jωt) back and take the real part. This formal grounding ensures that phasor analysis gives exactly the same answers as solving the differential equations directly — just far more efficiently.
