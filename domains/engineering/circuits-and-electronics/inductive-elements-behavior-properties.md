---
id: inductive-elements-behavior-properties
title: 'Inductive Elements: Behavior and Properties'
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-element-types-and-definitions
  type: hard
builds-toward:
- rl-circuit-transient-analysis
- rlc-circuit-transient-analysis-overview
- complex-impedance-networks-ac
tags:
- inductors
- energy-storage
- reactive-elements
stage: formal-systems
status: draft
---

# Inductive Elements: Behavior and Properties

## Core Idea
An inductor stores energy in a magnetic field; its inductance L relates magnetic flux to current: λ = Li. The voltage across an inductor is proportional to the rate of change of current: v = L(di/dt). Inductors oppose sudden changes in current and act as short circuits to DC steady state but block high-frequency signals.

## How It's Best Learned
Examine how inductors behave in RL circuits by measuring voltage spikes when switches open. Derive Faraday's law application: v = L(di/dt) from first principles using magnetic flux concepts.

## Common Misconceptions
- An inductor blocks all AC signals; it only blocks high frequencies with significant impedance. - Inductors have zero resistance; real coils have wire resistance. - Inductance is always constant; it varies with current in nonlinear inductors and depends on frequency in real components.

## Explainer

Capacitors store energy in an electric field between two charged plates; inductors are their magnetic dual. When current flows through a coil of wire, it creates a magnetic field threading the coil. The **inductance** L of the coil quantifies how efficiently it concentrates that field: the **magnetic flux linkage** λ = Li tells you how much total flux (field strength × area × turns) exists per ampere of current. When the current changes, the flux changes, and by Faraday's law — which you know from electromagnetism — a changing magnetic flux induces a voltage. That induced voltage is **v = L(di/dt)**: the voltage across an inductor equals inductance times the rate of change of current.

This single equation determines how inductors behave in every circuit context. If current is constant (DC steady state), di/dt = 0, so v = 0 — the inductor is electrically indistinguishable from a wire (short circuit). This is exactly symmetric to the capacitor's DC behavior: a capacitor accumulates charge until its voltage matches the source, at which point current stops flowing (open circuit). At DC steady state, inductors are shorts and capacitors are opens. If current through an inductor changes rapidly — as when a switch opens and tries to drive current to zero instantly — di/dt is large and the induced voltage is very large. This is Lenz's law in action: the inductor resists the change by generating a back-EMF opposing it. In practice, opening a switch in an inductive circuit can generate voltage spikes hundreds of times the supply voltage, which is why relay and motor-driver circuits use **freewheeling diodes** to provide a controlled discharge path.

The **energy stored** in an inductor's magnetic field is E = ½LI². This is not dissipated — it's held in the field and can be returned to the circuit. An inductor and capacitor exchanging energy back and forth (with no resistance to dissipate it) would oscillate indefinitely; this is the basis for LC resonance. In real circuits, resistance damps this oscillation, which you'll analyze quantitatively in RLC transient and resonance topics.

In AC circuits, the inductor's impedance is frequency-dependent: **inductive reactance** X_L = ωL, so the complex impedance is Z_L = jωL. At low frequencies, ωL is small and the inductor barely impedes current; at high frequencies, ωL is large and the inductor strongly blocks current. This is the exact inverse of capacitive behavior (Z_C = 1/jωC: large at low frequency, small at high frequency). The opposing frequency dependencies of L and C are what make resonance possible — at one particular frequency, their impedances cancel exactly, a phenomenon you'll study next.
