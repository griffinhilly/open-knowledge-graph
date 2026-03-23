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

## Questions

```yaml
- question: "A capacitor has impedance Z_C = −j/(ωC). An engineer says 'voltage lags current by 90° in this capacitor.' Which explanation correctly connects the complex impedance to the phase relationship?"
  type: multiple-choice
  options:
    - "The imaginary part of Z_C is negative, meaning the voltage phasor is rotated −90° relative to the current phasor, so voltage lags current by 90°"
    - "Because the capacitor stores charge, it delays the voltage by exactly half a period relative to the current"
    - "The impedance magnitude |Z_C| decreases with frequency, so the phase lag also decreases as frequency rises"
    - "Capacitors block DC, which means at all AC frequencies, the voltage is exactly 90° behind in time"
  answer: 0
  explanation: "In phasor analysis, V = IZ. If Z = −j/(ωC) = |Z_C|∠(−90°), then multiplying the current phasor by Z rotates it by −90°. The voltage phasor is 90° behind the current phasor in the complex plane, meaning voltage lags current by 90°. Option B conflates a time-domain intuition with a phase-domain statement; option C confuses magnitude with phase (|Z_C| decreases with frequency, but the phase is always −90° for an ideal capacitor regardless of frequency). Reading the phase angle directly from the angle of Z is the correct phasor technique."

- question: "Which statement correctly identifies the core advantage of representing AC circuits with complex impedances?"
  type: multiple-choice
  options:
    - "Impedances allow you to ignore the frequency dependence of circuit elements, simplifying analysis"
    - "All DC circuit analysis techniques — Kirchhoff's laws, series/parallel combination rules, voltage and current dividers — apply directly to phasors using complex impedances, converting differential equations into algebraic ones"
    - "Complex impedances eliminate the need to know the amplitude of signals; only phase relationships matter"
    - "Impedance analysis is only valid for sinusoidal signals at a single fixed frequency; it cannot handle circuits with multiple frequency components"
  answer: 1
  explanation: "The central payoff of phasor analysis is the transfer of the entire DC toolkit to AC. KVL holds for phasors (sum of phasor voltages around a loop = 0), KCL holds for phasors (sum of phasor currents at a node = 0), series impedances sum, parallel impedances combine reciprocally, and voltage/current dividers use the identical formulas as for resistors. This works because replacing d/dt with jω converts the underlying differential equations into linear algebraic equations with complex coefficients — the same structure as DC circuits with real resistances. Option D notes a real limitation (impedance analysis applies at a single frequency), but this does not negate the advantage stated in option B."

- question: "The magnitude of a complex impedance |Z| gives the ratio of the voltage amplitude to the current amplitude in an AC circuit."
  type: true-false
  answer: true
  explanation: "From Ohm's law in phasor form, V = IZ. The phasor V has magnitude |V| (voltage amplitude) and the phasor I has magnitude |I| (current amplitude). Since |V| = |I| × |Z|, we have |Z| = |V|/|I|. The angle of Z gives the phase of V relative to I. So a complex impedance Z = R + jX encodes both the amplitude ratio (|Z| = √(R² + X²)) and the phase relationship (∠Z = arctan(X/R)) between voltage and current. This is why reading impedance in polar form — magnitude and angle — immediately gives you both pieces of AC circuit information you care about."

- question: "An inductor (Z_L = jωL) and a capacitor (Z_C = −j/(ωC)) in series have impedances that always cancel, giving zero total reactance for any AC circuit containing both components."
  type: true-false
  answer: false
  explanation: "The total impedance of an inductor and capacitor in series is Z = jωL − j/(ωC) = j(ωL − 1/(ωC)). This is zero only when ωL = 1/(ωC), i.e., at the resonant frequency ω₀ = 1/√(LC). At other frequencies, the net reactance is nonzero — inductive above resonance (net positive imaginary) and capacitive below resonance (net negative imaginary). The cancellation is frequency-specific, not universal. This is the basis of resonant circuits: at exactly one frequency, the series LC combination has zero reactance (minimum impedance), which is why series resonant circuits are used as frequency-selective filters."

- question: "Explain why replacing resistance R with complex impedance Z allows all DC circuit analysis techniques to work directly for AC circuits, even though AC circuits involve time-varying signals and differential equations."
  type: short-answer
  answer: "In AC steady state, all voltages and currents are sinusoids at the same frequency ω. Representing them as phasors (complex amplitudes) and replacing d/dt with multiplication by jω converts the circuit's differential equations into linear algebraic equations with complex coefficients. For a resistor, v = Ri becomes V = RI. For an inductor, v = L di/dt becomes V = jωL·I = Z_L·I. For a capacitor, i = C dv/dt becomes I = jωC·V, so V = I/(jωC) = Z_C·I. In every case, the element law takes the algebraic form V = ZI — exactly Ohm's law with Z replacing R. Since KVL and KCL are linear (they sum voltages or currents at nodes), they hold equally for the complex phasor equations. The algebraic structure is identical to DC circuits, so all the DC solution techniques follow immediately."
  explanation: "The key move is recognizing that for sinusoidal excitation, d/dt ↔ ×jω is an exact substitution that converts differential operators into algebraic constants. This is essentially the circuit-theory version of Fourier or Laplace analysis restricted to steady-state sinusoids. The power of the substitution is that it makes the multi-element AC circuit problem as straightforward as the DC resistor circuit problem — once you accept complex arithmetic."
```

## Explainer

You've already learned to represent sinusoidal signals as rotating phasors in the complex plane, and you know from the complex exponential form that e^{jωt} = cos(ωt) + j·sin(ωt). The power of phasor analysis is that it converts differential equations into algebraic ones. Instead of solving v(t) = L·di/dt for a time-domain sinusoid — which requires solving a differential equation — you replace every signal with its phasor (complex amplitude) and replace d/dt with multiplication by jω. The circuit then behaves like a resistor network, but with complex-valued "resistances" called **impedances**.

**Impedance** Z = R + jX is the generalization of resistance to AC. The real part R is ordinary resistance — it dissipates energy as heat. The imaginary part X is **reactance** — it captures how an element stores and returns energy rather than consuming it. For a resistor, Z_R = R (purely real, no phase shift, voltage and current in phase). For an inductor, Z_L = jωL (purely imaginary, positive; magnitude grows with frequency because inductors resist fast current changes, and voltage *leads* current by 90°). For a capacitor, Z_C = 1/(jωC) = −j/(ωC) (purely imaginary, negative; magnitude shrinks with frequency because capacitors pass fast signals easily, and voltage *lags* current by 90°). These behaviors follow directly from the energy storage physics you already know.

Once impedances are assigned, all the DC circuit analysis techniques transfer unchanged. Kirchhoff's voltage and current laws hold for phasors. **Series impedances add**: Z_total = Z_1 + Z_2 + ..., exactly like series resistors. **Parallel impedances combine reciprocally**: 1/Z_total = 1/Z_1 + 1/Z_2 + ..., exactly like parallel resistors. Voltage dividers and current dividers use the same formulas. This is the central payoff of phasor analysis: the entire toolkit you built for DC circuits works for AC, with the single substitution of complex Z for real R.

The practical skill is fluency with complex arithmetic applied to circuit results. When you compute V = I·Z, you obtain a complex number whose magnitude is the voltage amplitude and whose angle is the phase of the voltage relative to the current. A result like Z = 1.77 + j1.77 Ω tells you immediately that the load is resistive-inductive (both R and positive X are present) with a 45° phase angle — voltage leads current by 45°. The magnitude |Z| = 2.5 Ω gives the ratio of voltage to current amplitudes. Reading impedance in polar form (magnitude and angle) builds the intuition you'll need immediately in AC power analysis, where the phase angle φ between voltage and current is precisely the quantity that determines how much power is consumed versus stored.
