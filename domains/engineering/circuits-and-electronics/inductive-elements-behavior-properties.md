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
status: validated
---

# Inductive Elements: Behavior and Properties

## Core Idea
An inductor stores energy in a magnetic field; its inductance L relates magnetic flux to current: λ = Li. The voltage across an inductor is proportional to the rate of change of current: v = L(di/dt). Inductors oppose sudden changes in current and act as short circuits to DC steady state but block high-frequency signals.

## How It's Best Learned
Examine how inductors behave in RL circuits by measuring voltage spikes when switches open. Derive Faraday's law application: v = L(di/dt) from first principles using magnetic flux concepts.

## Common Misconceptions
- An inductor blocks all AC signals; it only blocks high frequencies with significant impedance. - Inductors have zero resistance; real coils have wire resistance. - Inductance is always constant; it varies with current in nonlinear inductors and depends on frequency in real components.

## Questions

```yaml
- question: "A switch in series with an inductor and a battery is suddenly opened, attempting to drive the current to zero instantaneously. What happens immediately after the switch opens?"
  type: multiple-choice
  options:
    - "The current drops to zero instantly, since no complete path for current remains"
    - "The inductor generates a large voltage spike (back-EMF) opposing the sudden change in current, which can arc across the switch contacts"
    - "The inductor begins storing energy in an electric field, like a charging capacitor"
    - "The current reverses direction to maintain continuity through the inductor"
  answer: 1
  explanation: "From v = L(di/dt): if current tries to drop to zero instantaneously, di/dt → ∞, so the induced voltage → ∞. The inductor generates a large back-EMF opposing the change — Lenz's law in circuit form. In practice, this voltage spike can far exceed the supply voltage and arc across the open switch contacts, destroying components. This is why real inductive circuits (motor drivers, relay coils) use freewheeling diodes: they provide a controlled discharge path so the inductor releases its stored energy gradually, limiting the spike."

- question: "A circuit reaches DC steady state with both a capacitor and an inductor in different branches. For the purposes of steady-state DC analysis, what are their equivalent circuit elements?"
  type: multiple-choice
  options:
    - "Both act as open circuits — neither allows sustained DC current flow"
    - "Both act as short circuits — both pass DC current without impedance"
    - "The inductor acts as a short circuit; the capacitor acts as an open circuit"
    - "The capacitor acts as a short circuit; the inductor acts as an open circuit"
  answer: 2
  explanation: "At DC steady state, all currents and voltages are constant. For the inductor: di/dt = 0, so v = L(di/dt) = 0 — zero voltage drop with current flowing means it behaves as a wire (short circuit). For the capacitor: dv/dt = 0, so i = C(dv/dt) = 0 — zero current flow means it behaves as an open circuit. These are the complementary DC behaviors: inductors short at DC, capacitors open at DC. This duality is also why LC circuits can oscillate — the two elements respond oppositely to frequency."

- question: "An inductor stores energy in its magnetic field that can be returned to the circuit; none of this stored energy is dissipated by an ideal inductor."
  type: true-false
  answer: true
  explanation: "The energy stored in an inductor is E = ½LI², held in the magnetic field around the coil. An ideal inductor has zero resistance, so it dissipates nothing — energy flows in as current increases and flows back out as current decreases. This is directly analogous to a capacitor storing energy in its electric field. When an inductor and capacitor exchange energy in an LC circuit, oscillation persists indefinitely in the ideal case; only resistance damps the oscillation by converting stored energy to heat."

- question: "An ideal inductor in DC steady state behaves like an open circuit, preventing current from flowing through it."
  type: true-false
  answer: false
  explanation: "This is the opposite of correct behavior and a common confusion with capacitors. In DC steady state, current through an inductor is constant and nonzero; di/dt = 0, so v = L(di/dt) = 0. Zero voltage drop with current flowing is the behavior of a short circuit (wire), not an open circuit. Capacitors block DC (open circuit at steady state); inductors pass DC freely (short circuit at steady state). At high frequencies the roles reverse: inductors impede high-frequency signals (Z_L = jωL grows with ω) while capacitors pass them."

- question: "Explain why v = L(di/dt) means inductors oppose sudden changes in current. What physically happens to the voltage when current tries to change instantaneously?"
  type: short-answer
  answer: "If current changes instantaneously, di/dt → ∞, and since v = L(di/dt), the voltage across the inductor would become infinite — physically impossible in any real circuit. To prevent this, the inductor generates a back-EMF (induced voltage) opposing whatever is driving the current change. Current through an inductor must therefore change continuously over time; it cannot jump discontinuously. The inductor acts as inertia for current, analogous to how mechanical inertia resists sudden changes in velocity."
  explanation: "The physical mechanism is Faraday's law: a changing current creates a changing magnetic flux, which induces a voltage that opposes the change (Lenz's law). The equation v = L(di/dt) is not just a formula — it is a physical constraint. The inductor will generate whatever voltage is necessary to prevent a discontinuous current jump. This property is exploited in switching power supplies: once an inductor is energized, it tends to maintain its current even as the supply switches, smoothing current delivery to the load."
```

## Explainer

Capacitors store energy in an electric field between two charged plates; inductors are their magnetic dual. When current flows through a coil of wire, it creates a magnetic field threading the coil. The **inductance** L of the coil quantifies how efficiently it concentrates that field: the **magnetic flux linkage** λ = Li tells you how much total flux (field strength × area × turns) exists per ampere of current. When the current changes, the flux changes, and by Faraday's law — which you know from electromagnetism — a changing magnetic flux induces a voltage. That induced voltage is **v = L(di/dt)**: the voltage across an inductor equals inductance times the rate of change of current.

This single equation determines how inductors behave in every circuit context. If current is constant (DC steady state), di/dt = 0, so v = 0 — the inductor is electrically indistinguishable from a wire (short circuit). This is exactly symmetric to the capacitor's DC behavior: a capacitor accumulates charge until its voltage matches the source, at which point current stops flowing (open circuit). At DC steady state, inductors are shorts and capacitors are opens. If current through an inductor changes rapidly — as when a switch opens and tries to drive current to zero instantly — di/dt is large and the induced voltage is very large. This is Lenz's law in action: the inductor resists the change by generating a back-EMF opposing it. In practice, opening a switch in an inductive circuit can generate voltage spikes hundreds of times the supply voltage, which is why relay and motor-driver circuits use **freewheeling diodes** to provide a controlled discharge path.

The **energy stored** in an inductor's magnetic field is E = ½LI². This is not dissipated — it's held in the field and can be returned to the circuit. An inductor and capacitor exchanging energy back and forth (with no resistance to dissipate it) would oscillate indefinitely; this is the basis for LC resonance. In real circuits, resistance damps this oscillation, which you'll analyze quantitatively in RLC transient and resonance topics.

In AC circuits, the inductor's impedance is frequency-dependent: **inductive reactance** X_L = ωL, so the complex impedance is Z_L = jωL. At low frequencies, ωL is small and the inductor barely impedes current; at high frequencies, ωL is large and the inductor strongly blocks current. This is the exact inverse of capacitive behavior (Z_C = 1/jωC: large at low frequency, small at high frequency). The opposing frequency dependencies of L and C are what make resonance possible — at one particular frequency, their impedances cancel exactly, a phenomenon you'll study next.
