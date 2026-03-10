---
id: impedance-and-reactance
title: Impedance and Reactance
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: ac-circuits-fundamentals
  type: hard
- id: operations-with-complex-numbers
  type: soft
builds-toward:
- ac-power-and-resonance
tags:
- impedance
- reactance
- capacitive-reactance
- inductive-reactance
- phasor
stage: formal-systems
status: draft
---

# Impedance and Reactance

## Core Idea
Reactance is the AC analog of resistance for energy-storing elements. Capacitive reactance X_C = 1/(ωC) decreases with frequency; inductive reactance X_L = ωL increases with frequency. Impedance Z is the complex generalization: Z = R + j(X_L − X_C), with magnitude |Z| = √(R² + (X_L − X_C)²). Ohm's law generalizes to V = IZ, and the phase angle φ = arctan((X_L − X_C)/R) gives the phase difference between voltage and current.

## How It's Best Learned
Use phasor diagrams to represent Z as a vector in the complex plane: R along the real axis, reactances along the imaginary axis. Practice calculating |Z| and φ for series RLC circuits, then find current amplitude and phase for a given driving frequency.

## Common Misconceptions
- Reactance is not the same as resistance — reactors store and release energy (on average no net power), while resistors dissipate it.
- X_C → ∞ at DC (ω = 0): capacitors block DC. X_L → 0 at DC: inductors pass DC freely.
- Impedance is frequency-dependent; replacing Z by R gives wrong answers for AC circuits.
