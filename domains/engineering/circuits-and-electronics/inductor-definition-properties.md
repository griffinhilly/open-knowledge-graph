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
status: draft
---

# Inductors and Inductance

## Core Idea
An inductor stores energy in a magnetic field created by current flow. Inductance L depends on coil geometry and material. The voltage-current relationship v = L(di/dt) shows inductors oppose current changes and block AC signals, with impedance Z_L = jωL in AC circuits. Inductors are dual to capacitors in circuit theory.

## Explainer

You already know from your prerequisites that current flowing through a conductor creates a magnetic field around it. An **inductor** — typically a coil of wire — is specifically designed to maximize this magnetic energy storage by concentrating the field through many turns of wire. The measure of how effectively a coil does this is **inductance L**, measured in henries (H). A larger inductance means more magnetic energy stored per unit of current, and the value depends on the geometry of the coil (number of turns, cross-sectional area, length) and the magnetic permeability of the material in its core.

The defining voltage-current relationship is v = L(di/dt). Read this carefully: the voltage across an inductor is proportional to the *rate of change* of current, not the current itself. If the current through an inductor is constant (DC), di/dt = 0, so the voltage is zero — the inductor looks like a short circuit (a perfect wire) for DC. But if the current is changing rapidly, a large voltage appears. This is the key behavioral rule: **inductors resist changes in current**. You cannot instantaneously change the current through an inductor; doing so would require infinite voltage. This property is why inductors are used to smooth current in power supplies and why they produce voltage spikes when circuits are abruptly switched.

In AC circuits, the rate of change of current is proportional to frequency. A sinusoidal current i(t) = I₀sin(ωt) has di/dt = ωI₀cos(ωt), so the induced voltage is proportional to ω. This gives the inductor's **impedance** Z_L = jωL: at low frequencies, the impedance is small (the inductor barely resists current); at high frequencies, the impedance is large (the inductor strongly opposes current). This frequency-dependent behavior makes inductors high-pass filters for current and explains their use in RF circuits, transformers, and filtering applications.

The **duality** with capacitors is worth internalizing: every property of a capacitor has a mirror image in an inductor. Capacitors store energy in an electric field; inductors in a magnetic field. Capacitors resist voltage changes (i = C·dv/dt); inductors resist current changes (v = L·di/dt). Capacitor impedance Z_C = 1/(jωC) decreases with frequency; inductor impedance Z_L = jωL increases with frequency. The energy stored in a capacitor is ½CV²; in an inductor it is ½LI². Understanding this symmetry lets you transfer your intuition about one element directly to the other, and it underlies the oscillatory behavior of LC circuits — where energy sloshes back and forth between electric and magnetic fields.
