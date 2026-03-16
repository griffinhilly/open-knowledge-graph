---
id: phasor-notation-and-complex-algebra
title: Phasor Notation and Complex Impedance
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: sinusoidal-steady-state-analysis
  type: hard
- id: complex-numbers-intro
  type: soft
builds-toward:
- resonance-quality-factor
tags:
- phasors
- complex-impedance
- reactance
- admittance
stage: formal-systems
status: draft
---

# Phasor Notation and Complex Impedance

## Core Idea
Phasors represent sinusoidal signals as complex numbers with magnitude representing amplitude and angle representing phase shift relative to a reference. Complex impedance Z = R + jX combines resistance and reactance, allowing Ohm's law V = ZI to apply in AC circuits. This representation enables use of all DC analysis techniques (nodal, mesh, Thévenin) in frequency domain with straightforward impedance substitution.

## Explainer

From your study of sinusoidal steady-state analysis, you encountered the core difficulty: in a circuit with reactive elements, voltage and current are both sinusoids but they are shifted in time relative to each other, and working with expressions like v(t) = V_m cos(ωt + φ) directly requires constantly keeping track of trig identities. The **phasor** is a mathematical shortcut that freezes this problem by exploiting a fact from your complex numbers prerequisite: a sinusoid is the real part of a rotating complex exponential.

The key idea: if every signal in the circuit is a sinusoid at the same frequency ω (which is true in steady state), then the time-varying factor e^(jωt) appears in every term of KVL and KCL and can be divided out. What remains is a complex number — the **phasor** — that encodes only the amplitude and phase of the sinusoid. The signal v(t) = V_m cos(ωt + φ) corresponds to the phasor **V** = V_m ∠φ, written in polar form as V_m e^(jφ). To recover the time-domain signal, multiply by e^(jωt) and take the real part. The phasor is not the signal; it is a compact representation that makes AC circuit arithmetic tractable.

**Complex impedance** extends Ohm's law to reactive elements. Recall that a resistor satisfies v = Ri at all times — same ratio regardless of signal frequency. An inductor satisfies v = L di/dt, and a capacitor satisfies i = C dv/dt. In phasor notation, differentiation with respect to time becomes multiplication by jω (because the time derivative of e^(jωt) is jω e^(jωt)). So the inductor's impedance is Z_L = jωL (purely imaginary, increases with frequency) and the capacitor's impedance is Z_C = 1/(jωC) = -j/(ωC) (purely imaginary, decreases with frequency). With these substitutions, every element has a complex impedance, and the phasor relationship **V** = Z **I** is exactly Ohm's law for AC.

The payoff is enormous: every DC circuit analysis technique — nodal analysis, mesh analysis, voltage divider, Thévenin equivalents — applies directly in the phasor domain with impedances replacing resistances. Series impedances add. Parallel impedances combine as Z_total = (Z_1 Z_2)/(Z_1 + Z_2). The only arithmetic is complex number multiplication and division rather than scalar arithmetic, which your complex numbers prerequisite prepared you for. This is why phasors are the central tool of AC circuit analysis: they convert differential equations into algebraic equations, and they do it without losing any information about amplitude or phase.
