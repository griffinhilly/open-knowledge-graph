---
id: phasor-algebra-complex-impedance
title: Phasor Algebra and Complex Impedance
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: ac-source-representation-phasors
  type: hard
- id: complex-numbers-intro
  type: soft
- id: complex-exponential-form
  type: hard
builds-toward:
- impedance-admittance-networks
- ac-power-analysis-circuits
- series-resonance-characteristics
- parallel-resonance-characteristics
tags:
- phasors
- impedance
- ac-analysis
stage: formal-systems
status: draft
---

# Phasor Algebra and Complex Impedance

## Core Idea
Impedance Z = R + jX generalizes resistance to AC circuits, where X is reactance. Resistive impedance is purely real (Z = R), capacitive is Z = -j/(ωC), and inductive is Z = jωL. Using complex arithmetic, Kirchhoff's laws apply directly to phasors, and series/parallel impedance rules follow resistor rules: series impedances sum, parallel impedances combine reciprocally.

## Explainer

You've already learned to represent sinusoidal signals as rotating phasors in the complex plane, and you know from the complex exponential form that e^{jωt} = cos(ωt) + j·sin(ωt). The power of phasor analysis is that it converts differential equations into algebraic ones. Instead of solving v(t) = L·di/dt for a time-domain sinusoid — which requires solving a differential equation — you replace every signal with its phasor (complex amplitude) and replace d/dt with multiplication by jω. The circuit then behaves like a resistor network, but with complex-valued "resistances" called **impedances**.

**Impedance** Z = R + jX is the generalization of resistance to AC. The real part R is ordinary resistance — it dissipates energy as heat. The imaginary part X is **reactance** — it captures how an element stores and returns energy rather than consuming it. For a resistor, Z_R = R (purely real, no phase shift, voltage and current in phase). For an inductor, Z_L = jωL (purely imaginary, positive; magnitude grows with frequency because inductors resist fast current changes, and voltage *leads* current by 90°). For a capacitor, Z_C = 1/(jωC) = −j/(ωC) (purely imaginary, negative; magnitude shrinks with frequency because capacitors pass fast signals easily, and voltage *lags* current by 90°). These behaviors follow directly from the energy storage physics you already know.

Once impedances are assigned, all the DC circuit analysis techniques transfer unchanged. Kirchhoff's voltage and current laws hold for phasors. **Series impedances add**: Z_total = Z_1 + Z_2 + ..., exactly like series resistors. **Parallel impedances combine reciprocally**: 1/Z_total = 1/Z_1 + 1/Z_2 + ..., exactly like parallel resistors. Voltage dividers and current dividers use the same formulas. This is the central payoff of phasor analysis: the entire toolkit you built for DC circuits works for AC, with the single substitution of complex Z for real R.

The practical skill is fluency with complex arithmetic applied to circuit results. When you compute V = I·Z, you obtain a complex number whose magnitude is the voltage amplitude and whose angle is the phase of the voltage relative to the current. A result like Z = 1.77 + j1.77 Ω tells you immediately that the load is resistive-inductive (both R and positive X are present) with a 45° phase angle — voltage leads current by 45°. The magnitude |Z| = 2.5 Ω gives the ratio of voltage to current amplitudes. Reading impedance in polar form (magnitude and angle) builds the intuition you'll need immediately in AC power analysis, where the phase angle φ between voltage and current is precisely the quantity that determines how much power is consumed versus stored.
