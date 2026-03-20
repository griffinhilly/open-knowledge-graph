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
stage: advanced
status: draft
---

# Complex Impedance in AC Networks

## Core Idea
Impedance Z = R + jX extends Ohm's law to AC circuits: V̅ = Z I̅. The real part R is resistance; the imaginary part X is reactance (inductive or capacitive). Series impedances add; parallel admittances (Y = 1/Z) add. This allows AC circuits to be analyzed using the same techniques as DC circuits, but in the complex plane.

## Explainer

You know how to analyze DC circuits using Ohm's law (V = IR) and Kirchhoff's laws. You also know from phasor representation that sinusoidal voltages and currents can be written as complex numbers that encode both amplitude and phase. **Impedance** unifies these two ideas: it extends Ohm's law to AC circuits by treating all three passive elements through a single complex quantity Z, so that V̅ = Z·I̅ works in the phasor domain exactly as V = IR works in DC.

Each element type has a characteristic impedance. A **resistor** has Z_R = R — purely real, no phase shift, just as in DC. A **capacitor** has Z_C = 1/(jωC), which is purely imaginary and negative; current leads voltage by 90°. An **inductor** has Z_L = jωL, purely imaginary and positive; voltage leads current by 90°. The imaginary part X is called **reactance**: capacitive (X_C = −1/ωC) and inductive (X_L = ωL). The full impedance Z = R + jX captures both the resistive and reactive character of a network.

The combination rules carry over from DC without modification — just use complex arithmetic. Series impedances add: Z_total = Z₁ + Z₂ + ··· For parallel combinations, it's often easier to work with **admittance** Y = 1/Z (the AC generalization of conductance). Parallel admittances add: Y_total = Y₁ + Y₂ + ···, then Z_total = 1/Y_total. Voltage divider and current divider rules are identical to DC — replace R with Z throughout. This is the payoff of phasor analysis: an AC circuit with any mix of R, L, C elements becomes a DC-style resistor network in the complex domain.

The magnitude |Z| gives the ratio of voltage amplitude to current amplitude; the angle ∠Z gives the phase difference. For Z = 3 + 4j Ω, the magnitude is 5 Ω and the phase is arctan(4/3) ≈ 53°, meaning voltage leads current by 53°. This single complex number encodes the full sinusoidal relationship between V and I. Everything in AC circuit analysis — resonance, filters, power factor, Thevenin equivalents — begins with impedance as the fundamental building block.
