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
status: validated
---

# Sinusoidal AC Steady-State Fundamentals

## Core Idea
AC steady-state refers to the response of circuits to sinusoidal sources v(t) = V_m cos(ωt + φ). The RMS (root-mean-square) value relates peak amplitude to equivalent DC power. Capacitors and inductors exhibit frequency-dependent behavior in AC circuits, with impedance given by Z_C = 1/(jωC) and Z_L = jωL, respectively.

## Questions

```yaml
- question: "A capacitor with impedance Z_C = 1/(jωC) is connected to an AC source. As the source frequency doubles, what happens to the magnitude of the capacitor's impedance?"
  type: multiple-choice
  options:
    - "It doubles — impedance is proportional to frequency"
    - "It halves — impedance is inversely proportional to frequency"
    - "It stays the same — impedance of a capacitor is constant like a resistor"
    - "It quadruples — the relationship is squared"
  answer: 1
  explanation: "|Z_C| = 1/(ωC). Doubling ω halves the impedance. This means capacitors pass high-frequency signals easily (low impedance at high ω) and block low-frequency signals (high impedance at low ω). This frequency dependence is what makes capacitors useful as filters. Contrast with inductors: Z_L = jωL, so inductors do the opposite — they block high frequencies and pass low ones."

- question: "In AC steady-state, a circuit is driven by a sinusoidal voltage source at frequency ω. What is guaranteed to be true of every voltage and current elsewhere in the circuit?"
  type: multiple-choice
  options:
    - "All voltages and currents are constant — 'steady state' means nothing is changing"
    - "All voltages and currents are sinusoidal at the same frequency ω, though with different amplitudes and phases"
    - "All voltages and currents are sinusoidal, but at various harmonic frequencies of ω"
    - "Voltages are sinusoidal at ω, but currents may be at different frequencies depending on component type"
  answer: 1
  explanation: "Linearity guarantees this. A linear circuit driven sinusoidally at frequency ω can only produce sinusoidal responses at the same frequency ω — no harmonics, no new frequencies. Only the amplitude and phase angle change from node to node. This is the critical insight that makes phasor analysis possible: since every quantity has the same ω, we can suppress e^{jωt} and work with complex amplitudes (phasors) using algebraic, not differential, equations."

- question: "A pure inductor connected to a sinusoidal voltage source absorbs net real power averaged over a complete cycle."
  type: true-false
  answer: false
  explanation: "False. An ideal inductor has impedance Z_L = jωL, which is purely imaginary. The phase angle between voltage and current is 90°, so the power factor cos(90°) = 0, and average real power P = V_rms · I_rms · cos(90°) = 0. The inductor stores energy in its magnetic field during one half-cycle and returns it during the next — it exchanges energy with the source but dissipates none. Only resistors (with real impedance) absorb net real power."

- question: "In AC steady-state analysis, if the source frequency is doubled, the frequency of the voltage across any component in the circuit also doubles."
  type: true-false
  answer: true
  explanation: "True. By the linearity of AC steady-state analysis, all voltages and currents in the circuit are sinusoidal at exactly the source frequency ω. If ω doubles, every response in the circuit doubles in frequency as well. Only the amplitudes and phases (encoded in the phasors) change — determined by the impedances at the new frequency. This is the defining property of linear time-invariant systems: sinusoidal input at frequency ω produces sinusoidal output at frequency ω."

- question: "Why can DC circuit analysis techniques — nodal analysis, mesh analysis, Thévenin equivalents — be applied directly to AC circuits in steady state?"
  type: short-answer
  answer: "Because phasors convert the differential equations governing capacitors and inductors into algebraic Ohm's-law relationships. A capacitor's equation I = C·dV/dt becomes I = jωC·V in the phasor domain, meaning Z_C = 1/(jωC). An inductor's V = L·dI/dt becomes V = jωL·I, giving Z_L = jωL. With complex impedances replacing real resistances, every element obeys V = Z·I, and all DC analysis techniques — which only require linearity and Ohm's law — apply unchanged."
  explanation: "The transformation from time domain to phasor domain converts differentiation into multiplication by jω. This eliminates the differential equations and leaves a purely algebraic system with complex numbers. Kirchhoff's laws still hold for phasors (since they hold at every instant in time), and every element obeys a complex version of Ohm's law. The mathematical structure is identical to DC resistor networks — just with complex-valued 'resistances.'"
```

## Explainer

In DC steady state, you replaced capacitors with open circuits and inductors with short circuits, then solved a resistor network. That worked because all voltages and currents were constant — time derivatives were zero. Now the sources vary sinusoidally: v_s(t) = V_m cos(ωt + φ). In **AC steady state**, the circuit has been running long enough that all transients have died out, and every voltage and current is also sinusoidal at the same frequency ω — only the amplitude and phase angle differ from node to node. This is the critical insight: linearity guarantees that a sinusoidal input at frequency ω produces a sinusoidal output at the same ω. Only amplitude scaling and phase shifting occur.

Rather than tracking sin and cos functions through every calculation, engineers represent sinusoids as **phasors**: complex numbers that encode amplitude and phase but suppress the time dependence. The sinusoid V_m cos(ωt + φ) is represented by the phasor **V** = V_m ∠φ = V_m e^{jφ}. To recover the time-domain signal, multiply by e^{jωt} and take the real part. The power of phasors is that differentiation in the time domain becomes multiplication by jω in the phasor domain. Since a capacitor's current is I = C · dV/dt, in phasor terms this becomes **I** = jωC · **V**, or equivalently **V** = (1/jωC) · **I**. This is Ohm's law with a complex "resistance" — the **impedance** Z_C = 1/(jωC). Similarly, an inductor's voltage V = L · dI/dt becomes **V** = jωL · **I**, giving Z_L = jωL.

With impedances in hand, capacitors and inductors become two-terminal elements obeying Ohm's law in the phasor domain: **V** = Z · **I**. This means every circuit analysis technique you learned for DC circuits — nodal analysis, mesh analysis, superposition, Thévenin/Norton — applies directly to AC circuits, with complex impedances replacing real resistances. Resistors have impedance Z_R = R (purely real, no phase shift). Capacitors have Z_C = 1/(jωC) = −j/(ωC), which is purely imaginary and decreases as frequency increases (capacitors pass high-frequency signals easily). Inductors have Z_L = jωL, which is purely imaginary and increases with frequency (inductors block high-frequency signals). This frequency dependence is what makes AC analysis rich: by varying ω, you can design circuits that filter, amplify, or phase-shift signals selectively.

The **RMS value** bridges AC and DC for power calculations. The RMS voltage V_rms = V_m / √2 is the DC voltage that would deliver the same average power to a resistor. Average power in AC is P = V_rms · I_rms · cos(θ), where θ is the phase angle between voltage and current — the power factor. A pure resistor has θ = 0 and absorbs real power; a pure capacitor or inductor has θ = ±90° and absorbs no average power (energy is stored and returned each cycle). Learning to work in phasors and impedances is the entry point to everything that follows in circuits: filters, resonance, transformers, and power systems all build directly on this framework.
