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
- id: complex-numbers-intro
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
status: validated
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

## Explainer

You already know resistors from AC circuits: they oppose current in proportion to voltage with no frequency dependence. Capacitors and inductors are fundamentally different — they store energy and return it, and their effective opposition to current depends strongly on how fast the voltage oscillates. **Reactance** is the name for this frequency-dependent opposition in energy-storing elements, and it arises directly from the physics of how each component responds to a sinusoidal driving voltage.

For a capacitor, think through the limiting cases. At DC (ω = 0), the capacitor charges up and then no more current flows — it blocks DC completely, giving X_C = 1/(ωC) → ∞. At very high frequency, the voltage reverses before the capacitor can fully charge, so current flows nearly unimpeded: X_C → 0. For an inductor, the logic reverses. At DC, an inductor is just a wire — it carries current freely, X_L = ωL = 0. At high frequency, the rapidly changing current induces a large back-EMF (by Faraday's law), strongly opposing further change: X_L → ∞. This frequency-swapping character is the core intuition: **capacitors are transparent at high frequency and opaque at low; inductors are the opposite.**

**Impedance** Z unifies resistance and reactance into a single complex number. Writing Z = R + j(X_L − X_C) places resistance on the real axis and net reactance on the imaginary axis. The magnitude |Z| = √(R² + (X_L − X_C)²) is the ratio of voltage amplitude to current amplitude — the actual size of the total opposition. The **phase angle** φ = arctan((X_L − X_C)/R) tells you how far the current lags or leads the voltage: positive φ means an inductive circuit (current lags voltage); negative φ means a capacitive circuit (current leads voltage). Because reactors store and return energy on average with zero net power dissipation, only the resistive part R contributes to real power.

The practical payoff of this framework is **resonance**. When X_L = X_C — that is, ωL = 1/(ωC) — the imaginary parts of Z cancel and Z = R, purely real. At this frequency ω₀ = 1/√(LC), impedance is minimized and current amplitude is maximized. Resonance is not a coincidence: the inductor and capacitor are exchanging energy at exactly the right rate to reinforce each other, with the resistor as the only dissipation. Radio tuners exploit resonance to select a single station frequency; LC tank circuits generate oscillations in transmitters. In every case, impedance and reactance are the tools that make the analysis tractable.
