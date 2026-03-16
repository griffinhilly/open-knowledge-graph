---
id: sinusoidal-AC-steady-state-fundamentals
title: Sinusoidal AC Steady-State Fundamentals
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: DC-steady-state-circuit-solution
  type: hard
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- phasor-conversion-and-representation
- AC-power-calculation-and-factor
tags:
- AC-analysis
- sinusoidal-sources
- steady-state
- RMS
stage: formal-systems
status: draft
---

# Sinusoidal AC Steady-State Fundamentals

## Core Idea
AC steady-state refers to the response of circuits to sinusoidal sources v(t) = V_m cos(ωt + φ). The RMS (root-mean-square) value relates peak amplitude to equivalent DC power. Capacitors and inductors exhibit frequency-dependent behavior in AC circuits, with impedance given by Z_C = 1/(jωC) and Z_L = jωL, respectively.

## Explainer

In DC steady state, you replaced capacitors with open circuits and inductors with short circuits, then solved a resistor network. That worked because all voltages and currents were constant — time derivatives were zero. Now the sources vary sinusoidally: v_s(t) = V_m cos(ωt + φ). In **AC steady state**, the circuit has been running long enough that all transients have died out, and every voltage and current is also sinusoidal at the same frequency ω — only the amplitude and phase angle differ from node to node. This is the critical insight: linearity guarantees that a sinusoidal input at frequency ω produces a sinusoidal output at the same ω. Only amplitude scaling and phase shifting occur.

Rather than tracking sin and cos functions through every calculation, engineers represent sinusoids as **phasors**: complex numbers that encode amplitude and phase but suppress the time dependence. The sinusoid V_m cos(ωt + φ) is represented by the phasor **V** = V_m ∠φ = V_m e^{jφ}. To recover the time-domain signal, multiply by e^{jωt} and take the real part. The power of phasors is that differentiation in the time domain becomes multiplication by jω in the phasor domain. Since a capacitor's current is I = C · dV/dt, in phasor terms this becomes **I** = jωC · **V**, or equivalently **V** = (1/jωC) · **I**. This is Ohm's law with a complex "resistance" — the **impedance** Z_C = 1/(jωC). Similarly, an inductor's voltage V = L · dI/dt becomes **V** = jωL · **I**, giving Z_L = jωL.

With impedances in hand, capacitors and inductors become two-terminal elements obeying Ohm's law in the phasor domain: **V** = Z · **I**. This means every circuit analysis technique you learned for DC circuits — nodal analysis, mesh analysis, superposition, Thévenin/Norton — applies directly to AC circuits, with complex impedances replacing real resistances. Resistors have impedance Z_R = R (purely real, no phase shift). Capacitors have Z_C = 1/(jωC) = −j/(ωC), which is purely imaginary and decreases as frequency increases (capacitors pass high-frequency signals easily). Inductors have Z_L = jωL, which is purely imaginary and increases with frequency (inductors block high-frequency signals). This frequency dependence is what makes AC analysis rich: by varying ω, you can design circuits that filter, amplify, or phase-shift signals selectively.

The **RMS value** bridges AC and DC for power calculations. The RMS voltage V_rms = V_m / √2 is the DC voltage that would deliver the same average power to a resistor. Average power in AC is P = V_rms · I_rms · cos(θ), where θ is the phase angle between voltage and current — the power factor. A pure resistor has θ = 0 and absorbs real power; a pure capacitor or inductor has θ = ±90° and absorbs no average power (energy is stored and returned each cycle). Learning to work in phasors and impedances is the entry point to everything that follows in circuits: filters, resonance, transformers, and power systems all build directly on this framework.
