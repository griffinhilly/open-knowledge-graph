---
id: capacitor-definition-properties
title: Capacitors and Capacitance
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: charge-and-current-flow
  type: hard
- id: electric-potential-and-voltage
  type: hard
- id: capacitance
  type: hard
builds-toward:
- energy-storage-elements-l-and-c
- series-parallel-rc-and-rl-networks
tags:
- capacitors
- capacitance
- charge-storage
- dielectric
stage: formal-systems
status: draft
---

# Capacitors and Capacitance

## Core Idea
A capacitor stores charge and energy in an electric field between conductors. Capacitance C = Q/V depends only on geometry and dielectric properties. The voltage-current relationship i = C(dv/dt) shows capacitors block DC and pass AC signals, with impedance Z_C = 1/(jωC) in AC circuits.

## Explainer

From your study of charge, current, and voltage, you know that moving charge requires a potential difference, and that current is the rate of flow of charge. A **capacitor** is a device that exploits those fundamentals to store energy: two conducting plates, separated by an insulating **dielectric**, accumulate opposite charges on their surfaces when a voltage is applied across them. The electric field between the plates stores the energy, and the charge Q that accumulates is directly proportional to the applied voltage V. That proportionality constant is the **capacitance**: C = Q/V, measured in farads (F).

The capacitance is determined entirely by geometry and material — plate area A, separation distance d, and the dielectric constant ε of the insulating material: C = εA/d. A larger plate area captures more charge for the same voltage; a thinner dielectric brings the charges closer together, strengthening the field and increasing capacitance; a high-ε dielectric concentrates the field more effectively. This means you can tune C by changing the physical structure of the device without changing the circuit it connects to.

The behavior that makes capacitors useful in circuits comes from the voltage-current relationship: **i = C(dv/dt)**. Current flows into a capacitor only when its voltage is changing — if voltage is constant (DC steady state), dv/dt = 0, so current is zero. The capacitor acts like an open circuit for DC. But when voltage is changing rapidly (high-frequency AC), large currents flow even for small voltage swings. This is why capacitors block DC and pass AC, and why their impedance Z_C = 1/(jωC) decreases as frequency ω increases: at high frequency, the capacitor barely resists the changing signal at all.

A practical analogy: think of a capacitor as a spring in a mechanical system, or as a reservoir in a water system. Just as a reservoir stores water and releases it when pressure drops, a capacitor stores charge and releases it when voltage demands it. This energy-storage role is why capacitors are used in power supply filtering (smoothing out voltage ripples), in timing circuits (charging at a predictable rate), and in signal processing (separating AC signal components from DC bias). The key number to internalize is the energy stored: U = ½CV². Double the voltage and the stored energy quadruples — a fact that matters whenever capacitors discharge suddenly.
