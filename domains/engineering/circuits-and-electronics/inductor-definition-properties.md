---
id: inductor-definition-properties
title: Inductors and Inductance
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: charge-and-current-flow
  type: hard
- id: electric-potential-and-voltage
  type: hard
- id: inductance-and-inductors
  type: hard
builds-toward:
- energy-storage-elements-l-and-c
- series-parallel-rc-and-rl-networks
tags:
- inductors
- inductance
- magnetic-field
- flux-linkage
stage: formal-systems
status: validated
---

# Inductors and Inductance

## Core Idea
An inductor stores energy in a magnetic field created by current flow. Inductance L depends on coil geometry and material. The voltage-current relationship v = L(di/dt) shows inductors oppose current changes and block AC signals, with impedance Z_L = jωL in AC circuits. Inductors are dual to capacitors in circuit theory.

## Questions

```yaml
- question: "A 10 mH inductor carries a steady DC current of 2 A. What is the voltage across the inductor?"
  type: multiple-choice
  options:
    - "20 mV, calculated as L × I"
    - "0 V, because di/dt = 0 for constant current"
    - "200 V, because the inductor stores energy equal to ½LI²"
    - "It depends on the frequency of the AC source driving the circuit"
  answer: 1
  explanation: "The inductor's voltage-current relationship is v = L(di/dt). If current is constant (steady DC), then di/dt = 0 and v = 0. An ideal inductor with constant current looks like a short circuit — a perfect wire with no voltage drop. The stored energy ½LI² exists in the magnetic field, but energy storage doesn't produce a voltage; only *changing* current does. Option A (L × I) confuses the energy formula with the voltage formula."

- question: "As the frequency of an AC signal increases, how do the impedances of an inductor and a capacitor change relative to each other?"
  type: multiple-choice
  options:
    - "Both increase with frequency"
    - "Both decrease with frequency"
    - "Inductor impedance increases (Z_L = jωL); capacitor impedance decreases (Z_C = 1/jωC)"
    - "Inductor impedance decreases; capacitor impedance increases"
  answer: 2
  explanation: "The inductor and capacitor are duals with opposite frequency behavior. Z_L = jωL grows with ω — at high frequencies, the inductor strongly opposes current (high impedance). Z_C = 1/(jωC) shrinks with ω — at high frequencies, the capacitor offers little opposition (low impedance). This opposing behavior is what makes LC circuits oscillate: at high frequencies the capacitor is easy but the inductor is hard; at low frequencies the reverse is true. The balance point is the resonant frequency."

- question: "An ideal inductor carrying a constant DC current has zero voltage across its terminals."
  type: true-false
  answer: true
  explanation: "Since v = L(di/dt) and a constant DC current has di/dt = 0, the voltage is exactly zero. The inductor acts like a short circuit for DC. This is why ideal inductors are invisible to steady-state DC analysis — they appear as wires. The magnetic energy ½LI² is stored in the field but does not produce a terminal voltage unless the current is changing."

- question: "In a DC circuit, a capacitor and an inductor behave the same way — both appear as short circuits in steady state."
  type: true-false
  answer: false
  explanation: "They are opposites in DC steady state — a precise manifestation of their duality. A capacitor blocks DC current: in steady state, current stops flowing through it (i = C·dv/dt = 0 when v is constant), making it an open circuit. An inductor passes DC current freely: once current stabilizes, v = L·di/dt = 0, making it a short circuit. Confusing these two behaviors leads to serious errors in circuit analysis, particularly in power supply and filter design."

- question: "Explain why you cannot instantaneously change the current through an inductor, and what physical consequence occurs if a circuit attempts to do so."
  type: short-answer
  answer: "The inductor's voltage is v = L(di/dt). Instantaneously changing current requires di/dt → ∞, which would require infinite voltage — physically impossible. If a switch abruptly breaks a circuit carrying inductor current, the inductor briefly sustains the current by generating a large voltage spike (voltage as high as the circuit allows). In practice this can cause arcing across the switch or destroy unprotected components."
  explanation: "This property — current continuity — is the inductor's most important circuit behavior. It is the electromagnetic analog of mechanical inertia: just as you cannot instantaneously stop a moving mass, you cannot instantaneously stop current in an inductor. The stored magnetic energy ½LI² must go somewhere; if the circuit doesn't provide a path, the inductor creates one through a voltage spike. Freewheeling diodes in motor driver circuits exploit this principle to safely absorb the energy when current is switched off."
```

## Explainer

You already know from your prerequisites that current flowing through a conductor creates a magnetic field around it. An **inductor** — typically a coil of wire — is specifically designed to maximize this magnetic energy storage by concentrating the field through many turns of wire. The measure of how effectively a coil does this is **inductance L**, measured in henries (H). A larger inductance means more magnetic energy stored per unit of current, and the value depends on the geometry of the coil (number of turns, cross-sectional area, length) and the magnetic permeability of the material in its core.

The defining voltage-current relationship is v = L(di/dt). Read this carefully: the voltage across an inductor is proportional to the *rate of change* of current, not the current itself. If the current through an inductor is constant (DC), di/dt = 0, so the voltage is zero — the inductor looks like a short circuit (a perfect wire) for DC. But if the current is changing rapidly, a large voltage appears. This is the key behavioral rule: **inductors resist changes in current**. You cannot instantaneously change the current through an inductor; doing so would require infinite voltage. This property is why inductors are used to smooth current in power supplies and why they produce voltage spikes when circuits are abruptly switched.

In AC circuits, the rate of change of current is proportional to frequency. A sinusoidal current i(t) = I₀sin(ωt) has di/dt = ωI₀cos(ωt), so the induced voltage is proportional to ω. This gives the inductor's **impedance** Z_L = jωL: at low frequencies, the impedance is small (the inductor barely resists current); at high frequencies, the impedance is large (the inductor strongly opposes current). This frequency-dependent behavior makes inductors high-pass filters for current and explains their use in RF circuits, transformers, and filtering applications.

The **duality** with capacitors is worth internalizing: every property of a capacitor has a mirror image in an inductor. Capacitors store energy in an electric field; inductors in a magnetic field. Capacitors resist voltage changes (i = C·dv/dt); inductors resist current changes (v = L·di/dt). Capacitor impedance Z_C = 1/(jωC) decreases with frequency; inductor impedance Z_L = jωL increases with frequency. The energy stored in a capacitor is ½CV²; in an inductor it is ½LI². Understanding this symmetry lets you transfer your intuition about one element directly to the other, and it underlies the oscillatory behavior of LC circuits — where energy sloshes back and forth between electric and magnetic fields.
