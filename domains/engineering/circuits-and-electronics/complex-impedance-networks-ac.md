---
id: complex-impedance-networks-ac
title: Complex Impedance in AC Networks
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: phasor-conversion-and-representation
  type: hard
- id: sinusoidal-AC-steady-state-fundamentals
  type: hard
- id: complex-numbers-intro
  type: hard
builds-toward:
- AC-Kirchhoff-laws-phasor-domain
- circuit-resonance-concepts
tags:
- impedance
- admittance
- reactive-networks
stage: formal-systems
status: draft
---

# Complex Impedance in AC Networks

## Core Idea
Impedance Z = R + jX extends Ohm's law to AC circuits: V̅ = Z I̅. The real part R is resistance; the imaginary part X is reactance (inductive or capacitive). Series impedances add; parallel admittances (Y = 1/Z) add. This allows AC circuits to be analyzed using the same techniques as DC circuits, but in the complex plane.

## Questions

```yaml
- question: "A capacitor has impedance Z_C = 1/(jωC). As frequency increases from 100 Hz to 10,000 Hz, what happens to the capacitor's impedance magnitude, and what does this mean for current flow?"
  type: multiple-choice
  options:
    - "Impedance increases — the capacitor becomes harder to drive at higher frequencies, limiting current"
    - "Impedance decreases — the capacitor passes high-frequency signals more easily, as |Z_C| = 1/(ωC) shrinks with increasing ω"
    - "Impedance stays constant — frequency does not affect the capacitor's opposition to current"
    - "Impedance becomes purely resistive at high frequencies as the imaginary part cancels"
  answer: 1
  explanation: "The magnitude of capacitive impedance is |Z_C| = 1/(ωC). As ω increases, the denominator grows, so |Z_C| decreases. Physically, at higher frequencies the capacitor charges and discharges more rapidly, presenting less opposition to current flow. This is why capacitors block DC (ω = 0, |Z_C| → ∞) but pass high-frequency AC — the opposite behavior from inductors. This frequency dependence is what makes capacitors and inductors useful as filters."

- question: "A series RC circuit has R = 3 Ω and capacitive reactance X_C = −4 Ω. What are the impedance magnitude and the phase angle between voltage and current?"
  type: multiple-choice
  options:
    - "|Z| = 7 Ω, phase angle = −53° (current leads voltage by 53°)"
    - "|Z| = 5 Ω, phase angle = −53° (current leads voltage by 53°)"
    - "|Z| = 5 Ω, phase angle = +53° (voltage leads current by 53°)"
    - "|Z| = 1 Ω, phase angle = −53° (current leads voltage by 53°)"
  answer: 1
  explanation: "Z = R + jX = 3 + j(−4) = 3 − 4j. The magnitude is |Z| = √(3² + 4²) = √25 = 5 Ω. The phase angle is ∠Z = arctan(−4/3) ≈ −53°. A negative phase angle on Z means voltage lags current (or equivalently, current leads voltage) — expected for a capacitive circuit. Series impedances add directly: 3 Ω + (−4j) Ω = (3 − 4j) Ω. This is the same arithmetic as adding DC resistors, but complex."

- question: "In AC circuit analysis, working with admittance Y = 1/Z is useful for parallel combinations because parallel admittances add, just as parallel conductances add in DC circuits."
  type: true-false
  answer: true
  explanation: "For parallel branches, the total admittance Y_total = Y₁ + Y₂ + ···, then Z_total = 1/Y_total. This mirrors DC: for parallel resistors, G_total = G₁ + G₂ (conductances add) and R_total = 1/G_total. Admittance Y = G + jB has a real part (conductance G = R/|Z|²) and an imaginary part (susceptance B). The parallel admittance rule lets you analyze complex AC networks using the same step-by-step reduction that works for DC resistor networks."

- question: "An inductor and a capacitor in series always have zero total impedance because their reactances have opposite signs and cancel completely."
  type: true-false
  answer: false
  explanation: "Inductive reactance X_L = ωL and capacitive reactance X_C = −1/(ωC) are opposite in sign, so they partially cancel in series. But they are equal in magnitude only at the resonant frequency ω₀ = 1/√(LC). At that specific frequency, X_L + X_C = 0 and total reactance is zero (series resonance). At any other frequency, the magnitudes differ and a net reactance remains. Well above resonance, the inductor dominates (Z ≈ jωL); well below resonance, the capacitor dominates (Z ≈ 1/jωC). Zero total impedance is a special case, not the general rule."

- question: "A DC-trained engineer says 'For AC circuits, I just replace every R with Z and use all the same DC formulas.' Explain why this works, and what the complex nature of Z adds that DC analysis cannot capture."
  type: short-answer
  answer: "It works because Kirchhoff's voltage and current laws are linear equations, and linearity is the only property that the DC derivations of Ohm's law, voltage dividers, current dividers, Thevenin equivalents, and superposition actually require. These derivations never assumed V and I were constant — only that V = IR. Replacing R with Z (and V, I with phasors V̅, I̅) is valid because phasors are complex representations of sinusoidal signals, and impedance is the generalized proportionality constant. What complex Z adds: it encodes both amplitude ratio (|Z| = peak voltage / peak current) and phase relationship (∠Z = phase lead of voltage over current) in a single quantity. DC analysis captures only magnitude; AC with complex impedance captures magnitude and phase simultaneously, which is essential for power factor, filter design, and resonance analysis."
  explanation: "This replacement principle — that all DC techniques extend to AC by replacing R with Z — is one of the most powerful tools in circuit analysis. It is not a trick or approximation; it is mathematically exact for linear circuits in sinusoidal steady state. The complex arithmetic handles the phase bookkeeping automatically."
```

## Explainer

You know how to analyze DC circuits using Ohm's law (V = IR) and Kirchhoff's laws. You also know from phasor representation that sinusoidal voltages and currents can be written as complex numbers that encode both amplitude and phase. **Impedance** unifies these two ideas: it extends Ohm's law to AC circuits by treating all three passive elements through a single complex quantity Z, so that V̅ = Z·I̅ works in the phasor domain exactly as V = IR works in DC.

Each element type has a characteristic impedance. A **resistor** has Z_R = R — purely real, no phase shift, just as in DC. A **capacitor** has Z_C = 1/(jωC), which is purely imaginary and negative; current leads voltage by 90°. An **inductor** has Z_L = jωL, purely imaginary and positive; voltage leads current by 90°. The imaginary part X is called **reactance**: capacitive (X_C = −1/ωC) and inductive (X_L = ωL). The full impedance Z = R + jX captures both the resistive and reactive character of a network.

The combination rules carry over from DC without modification — just use complex arithmetic. Series impedances add: Z_total = Z₁ + Z₂ + ··· For parallel combinations, it's often easier to work with **admittance** Y = 1/Z (the AC generalization of conductance). Parallel admittances add: Y_total = Y₁ + Y₂ + ···, then Z_total = 1/Y_total. Voltage divider and current divider rules are identical to DC — replace R with Z throughout. This is the payoff of phasor analysis: an AC circuit with any mix of R, L, C elements becomes a DC-style resistor network in the complex domain.

The magnitude |Z| gives the ratio of voltage amplitude to current amplitude; the angle ∠Z gives the phase difference. For Z = 3 + 4j Ω, the magnitude is 5 Ω and the phase is arctan(4/3) ≈ 53°, meaning voltage leads current by 53°. This single complex number encodes the full sinusoidal relationship between V and I. Everything in AC circuit analysis — resonance, filters, power factor, Thevenin equivalents — begins with impedance as the fundamental building block.
