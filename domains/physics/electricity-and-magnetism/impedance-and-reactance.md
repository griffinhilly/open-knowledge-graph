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

## Questions

```yaml
- question: "At very high frequency (ω → ∞), a capacitor in an AC circuit behaves most like:"
  type: multiple-choice
  options:
    - "An open circuit, blocking current completely"
    - "A short circuit, passing current with almost no opposition"
    - "A resistor whose resistance equals 1/C"
    - "An inductor, since both store energy"
  answer: 1
  explanation: "Capacitive reactance X_C = 1/(ωC). As ω → ∞, X_C → 0, so the capacitor presents negligible opposition to current — it behaves like a short circuit. The common misconception is the opposite: students often think capacitors 'fill up and block' at high frequency. That intuition applies to DC or low frequency. At high frequency the voltage reverses before the capacitor can charge significantly, so current flows nearly unimpeded."

- question: "In a series RLC circuit driven at the resonant frequency ω₀ = 1/√(LC), which statement correctly describes the total impedance?"
  type: multiple-choice
  options:
    - "Impedance is zero because the inductive and capacitive reactances exactly cancel each other"
    - "Impedance equals R (purely real); the inductive and capacitive reactances cancel, leaving only resistance"
    - "Impedance is purely imaginary because the reactive elements dominate at resonance"
    - "Impedance is at its maximum because both reactive elements reinforce each other"
  answer: 1
  explanation: "At resonance X_L = X_C, so the imaginary part of Z = R + j(X_L − X_C) becomes j(0) = 0, leaving Z = R — purely real. Impedance is not zero (it equals R); current amplitude is maximized (not impedance). The confusion arises from thinking that 'cancellation' means everything disappears — only the reactive parts cancel."

- question: "Reactance and resistance both dissipate electrical energy, so a purely reactive circuit (mainly capacitors and inductors, no resistors) still consumes net power."
  type: true-false
  answer: false
  explanation: "Reactive elements store and return energy — capacitors store energy in electric fields, inductors in magnetic fields — but on average over a complete cycle, neither dissipates net power. Real power (average power) P = ½|I|²R depends only on resistance. A purely reactive circuit has zero average power consumption. Only resistance converts electrical energy to heat."

- question: "An inductor acts like a short circuit at DC (ω = 0) and presents increasing opposition to current as frequency rises."
  type: true-false
  answer: true
  explanation: "Inductive reactance X_L = ωL. At DC (ω = 0), X_L = 0 — an ideal inductor is just a wire and carries current freely. As frequency increases, the rapidly changing current induces a larger back-EMF (by Faraday's law), increasing opposition. This is the opposite behavior from a capacitor: capacitors are opaque at low frequency, inductors at high frequency."

- question: "Explain why a capacitor blocks DC but passes high-frequency AC, using the concept of reactance."
  type: short-answer
  answer: "Capacitive reactance is X_C = 1/(ωC). At DC (ω = 0), X_C is infinite — no steady current can flow because the capacitor charges to the applied voltage and stops. At high frequency, ω is large so X_C approaches zero, meaning current flows with almost no opposition."
  explanation: "Thinking through the physics: at DC the capacitor charges until the voltage across it equals the source voltage, at which point the electric field inside the dielectric exactly opposes further current flow. At high AC frequency, the voltage reverses direction before the capacitor can fully charge, so the capacitor is always in a transient state and never stops conducting. The mathematical expression X_C = 1/(ωC) captures this precisely: infinite opposition at zero frequency, zero opposition at infinite frequency."
```

## Explainer

You already know resistors from AC circuits: they oppose current in proportion to voltage with no frequency dependence. Capacitors and inductors are fundamentally different — they store energy and return it, and their effective opposition to current depends strongly on how fast the voltage oscillates. **Reactance** is the name for this frequency-dependent opposition in energy-storing elements, and it arises directly from the physics of how each component responds to a sinusoidal driving voltage.

For a capacitor, think through the limiting cases. At DC (ω = 0), the capacitor charges up and then no more current flows — it blocks DC completely, giving X_C = 1/(ωC) → ∞. At very high frequency, the voltage reverses before the capacitor can fully charge, so current flows nearly unimpeded: X_C → 0. For an inductor, the logic reverses. At DC, an inductor is just a wire — it carries current freely, X_L = ωL = 0. At high frequency, the rapidly changing current induces a large back-EMF (by Faraday's law), strongly opposing further change: X_L → ∞. This frequency-swapping character is the core intuition: **capacitors are transparent at high frequency and opaque at low; inductors are the opposite.**

**Impedance** Z unifies resistance and reactance into a single complex number. Writing Z = R + j(X_L − X_C) places resistance on the real axis and net reactance on the imaginary axis. The magnitude |Z| = √(R² + (X_L − X_C)²) is the ratio of voltage amplitude to current amplitude — the actual size of the total opposition. The **phase angle** φ = arctan((X_L − X_C)/R) tells you how far the current lags or leads the voltage: positive φ means an inductive circuit (current lags voltage); negative φ means a capacitive circuit (current leads voltage). Because reactors store and return energy on average with zero net power dissipation, only the resistive part R contributes to real power.

The practical payoff of this framework is **resonance**. When X_L = X_C — that is, ωL = 1/(ωC) — the imaginary parts of Z cancel and Z = R, purely real. At this frequency ω₀ = 1/√(LC), impedance is minimized and current amplitude is maximized. Resonance is not a coincidence: the inductor and capacitor are exchanging energy at exactly the right rate to reinforce each other, with the resistor as the only dissipation. Radio tuners exploit resonance to select a single station frequency; LC tank circuits generate oscillations in transmitters. In every case, impedance and reactance are the tools that make the analysis tractable.
