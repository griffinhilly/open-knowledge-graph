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
status: validated
---

# Phasor Notation and Complex Impedance

## Core Idea
Phasors represent sinusoidal signals as complex numbers with magnitude representing amplitude and angle representing phase shift relative to a reference. Complex impedance Z = R + jX combines resistance and reactance, allowing Ohm's law V = ZI to apply in AC circuits. This representation enables use of all DC analysis techniques (nodal, mesh, Thévenin) in frequency domain with straightforward impedance substitution.

## Questions

```yaml
- question: "The complex impedance of a capacitor is Z_C = 1/(jωC). What does this formula imply about capacitor behavior at very low frequencies compared to very high frequencies?"
  type: multiple-choice
  options:
    - "At low frequencies Z_C is small (near zero), so capacitors pass low-frequency signals; at high frequencies Z_C is large, blocking them"
    - "At high frequencies Z_C is small (near zero), so capacitors pass high-frequency signals; at low frequencies Z_C is large, blocking them"
    - "Z_C is constant across all frequencies, so capacitors behave identically at low and high frequencies"
    - "At resonance frequency only, Z_C becomes real (purely resistive); at all other frequencies it blocks all signals equally"
  answer: 1
  explanation: "As ω → 0 (DC), Z_C = 1/(ωC) → ∞: the capacitor is an open circuit, blocking DC. As ω → ∞, Z_C → 0: the capacitor is nearly a short circuit, passing high-frequency signals freely. Physically, a capacitor cannot sustain DC current (charge just accumulates), but at high frequencies charge oscillates so rapidly that effective impedance is very small. This high-pass character is the opposite of an inductor, whose impedance Z_L = jωL increases with frequency."

- question: "A student states: 'The phasor V = 5∠30° is the voltage in the circuit.' What correction does this statement require?"
  type: multiple-choice
  options:
    - "The phasor should include the imaginary unit j to represent time-varying behavior"
    - "V = 5∠30° is a complex number encoding amplitude (5) and phase offset (30°) at frequency ω; the actual time-domain voltage is v(t) = 5cos(ωt + 30°), recovered by multiplying by e^(jωt) and taking the real part"
    - "Phasors only represent current, not voltage; different notation is required for voltage"
    - "The angle 30° must be converted to radians before the phasor can be used in any calculation"
  answer: 1
  explanation: "A phasor is a compact representation, not the signal itself. V = 5∠30° tells you amplitude (5) and phase offset (30°) relative to a reference sinusoid at frequency ω. To recover the time-domain signal you must know ω and compute v(t) = Re{V · e^(jωt)} = 5cos(ωt + 30°). The phasor analysis 'freezes' the e^(jωt) factor that is common to every voltage and current in steady-state single-frequency circuits."

- question: "Phasor analysis is only valid when all sources in the circuit operate at the same single frequency, because the transformation relies on the e^(jωt) factor being identical for every signal."
  type: true-false
  answer: true
  explanation: "The phasor method works by dividing out e^(jωt) from every voltage and current in KVL and KCL. This is only valid if all signals share the same ω — otherwise different e^(jωt) factors cannot be canceled. For multi-frequency sources (a DC offset plus an AC component, or a distorted waveform), you must use superposition: decompose into frequency components, solve each phasor problem separately, and add the time-domain results."

- question: "An inductor has higher impedance at low frequencies than at high frequencies, so inductors block low-frequency signals and pass high-frequency ones."
  type: true-false
  answer: false
  explanation: "An inductor's impedance is Z_L = jωL, which increases with frequency. At low ω, Z_L is small — the inductor is nearly a short circuit and passes low-frequency signals. At high ω, Z_L is large — the inductor opposes rapid current changes and blocks high-frequency signals. Inductors are low-pass elements; capacitors are high-pass elements. These complementary behaviors are why LC circuits create selective resonance at the frequency where the two impedances are equal in magnitude."

- question: "Explain why differentiation in the time domain corresponds to multiplication by jω in the phasor domain, and how this transforms circuit equations."
  type: short-answer
  answer: "Any steady-state signal has the form A cos(ωt + φ) = Re{A e^(jφ) e^(jωt)}. Taking the time derivative gives jω · A e^(jφ) e^(jωt) — simply multiplied by jω. Since phasors factor out e^(jωt), differentiation becomes multiplication by jω in the phasor domain. For an inductor (v = L di/dt), this gives V = jωL · I, so Z_L = jωL. For a capacitor (i = C dv/dt), it gives I = jωC · V, so Z_C = 1/(jωC). Differential equations governing reactive elements become algebraic equations."
  explanation: "Without phasors, AC circuit analysis requires solving differential equations and manually tracking trig identities and phase shifts. Phasors reduce this to complex arithmetic, letting every DC technique — Ohm's law, nodal analysis, mesh analysis, Thévenin equivalents, voltage dividers — apply directly in the frequency domain. The only additional step is converting back to the time domain at the end, which usually means reading off the amplitude and phase from the final phasor."
```

## Explainer

From your study of sinusoidal steady-state analysis, you encountered the core difficulty: in a circuit with reactive elements, voltage and current are both sinusoids but they are shifted in time relative to each other, and working with expressions like v(t) = V_m cos(ωt + φ) directly requires constantly keeping track of trig identities. The **phasor** is a mathematical shortcut that freezes this problem by exploiting a fact from your complex numbers prerequisite: a sinusoid is the real part of a rotating complex exponential.

The key idea: if every signal in the circuit is a sinusoid at the same frequency ω (which is true in steady state), then the time-varying factor e^(jωt) appears in every term of KVL and KCL and can be divided out. What remains is a complex number — the **phasor** — that encodes only the amplitude and phase of the sinusoid. The signal v(t) = V_m cos(ωt + φ) corresponds to the phasor **V** = V_m ∠φ, written in polar form as V_m e^(jφ). To recover the time-domain signal, multiply by e^(jωt) and take the real part. The phasor is not the signal; it is a compact representation that makes AC circuit arithmetic tractable.

**Complex impedance** extends Ohm's law to reactive elements. Recall that a resistor satisfies v = Ri at all times — same ratio regardless of signal frequency. An inductor satisfies v = L di/dt, and a capacitor satisfies i = C dv/dt. In phasor notation, differentiation with respect to time becomes multiplication by jω (because the time derivative of e^(jωt) is jω e^(jωt)). So the inductor's impedance is Z_L = jωL (purely imaginary, increases with frequency) and the capacitor's impedance is Z_C = 1/(jωC) = -j/(ωC) (purely imaginary, decreases with frequency). With these substitutions, every element has a complex impedance, and the phasor relationship **V** = Z **I** is exactly Ohm's law for AC.

The payoff is enormous: every DC circuit analysis technique — nodal analysis, mesh analysis, voltage divider, Thévenin equivalents — applies directly in the phasor domain with impedances replacing resistances. Series impedances add. Parallel impedances combine as Z_total = (Z_1 Z_2)/(Z_1 + Z_2). The only arithmetic is complex number multiplication and division rather than scalar arithmetic, which your complex numbers prerequisite prepared you for. This is why phasors are the central tool of AC circuit analysis: they convert differential equations into algebraic equations, and they do it without losing any information about amplitude or phase.
