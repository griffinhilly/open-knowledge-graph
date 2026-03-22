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

## Questions

```yaml
- question: "A capacitor has been connected to a 9V DC source long enough to fully charge. How much current is flowing through the capacitor?"
  type: multiple-choice
  options:
    - "9 × C amperes, where C is the capacitance in farads"
    - "Zero, because dv/dt = 0 when voltage is constant"
    - "A small but nonzero leakage current equal to V/R"
    - "A current that has decayed exponentially to a negligible value"
  answer: 1
  explanation: "The voltage-current relationship is i = C(dv/dt). At DC steady state, voltage is constant, so dv/dt = 0 and therefore i = 0. The capacitor acts as an open circuit — no current flows through it. This is the fundamental reason capacitors block DC."

- question: "A capacitor with capacitance C is charged to voltage V, storing energy U = ½CV². The voltage is then doubled to 2V. By what factor does the stored energy change?"
  type: multiple-choice
  options:
    - "2× — stored energy is proportional to voltage"
    - "4× — stored energy scales with voltage squared"
    - "√2× — stored energy scales with the square root of voltage"
    - "The stored energy is unchanged; only the charge distribution shifts"
  answer: 1
  explanation: "U = ½CV². Doubling V gives U = ½C(2V)² = ½C·4V² = 4·(½CV²). Energy quadruples. This nonlinear relationship matters practically: a capacitor at twice the voltage stores four times as much energy — and releases it just as suddenly if discharged."

- question: "A capacitor with higher capacitance always stores more energy than one with lower capacitance."
  type: true-false
  answer: false
  explanation: "Stored energy is U = ½CV² — it depends on both capacitance and voltage. A small capacitor at high voltage can easily outstore a large capacitor at low voltage. For example, C = 1 μF at 1000V stores ½J; C = 1 F at 1V stores only 0.5J as well, but at 0.1V stores only 5 mJ. Capacitance alone does not determine stored energy."

- question: "In an AC circuit, a capacitor's impedance decreases as frequency increases, so high-frequency signals pass through more easily than low-frequency ones."
  type: true-false
  answer: true
  explanation: "Impedance Z_C = 1/(jωC). As frequency ω increases, Z_C decreases — the capacitor opposes high-frequency signals less. At DC (ω = 0), impedance is infinite (open circuit). At very high frequency, impedance approaches zero (short circuit). This frequency-dependent behavior is why capacitors are used to block DC bias while passing AC signal components."

- question: "Why does a capacitor block DC but allow AC signals to pass? Explain in terms of the voltage-current relationship i = C(dv/dt)."
  type: short-answer
  answer: "DC means constant voltage — dv/dt = 0 — so the current i = C·0 = 0. No current flows; the capacitor is an open circuit. AC means continuously changing voltage, so dv/dt ≠ 0 and current flows. The higher the frequency, the faster the voltage changes, and the larger the current for the same voltage amplitude — which is why high-frequency signals encounter lower impedance."
  explanation: "The key is that current through a capacitor reflects the rate of voltage change, not voltage level. A steady voltage, no matter how large, produces no current. A rapidly oscillating voltage, even if small in amplitude, produces large current. This is the physical basis of capacitive coupling and high-pass filtering."
```

## Explainer

From your study of charge, current, and voltage, you know that moving charge requires a potential difference, and that current is the rate of flow of charge. A **capacitor** is a device that exploits those fundamentals to store energy: two conducting plates, separated by an insulating **dielectric**, accumulate opposite charges on their surfaces when a voltage is applied across them. The electric field between the plates stores the energy, and the charge Q that accumulates is directly proportional to the applied voltage V. That proportionality constant is the **capacitance**: C = Q/V, measured in farads (F).

The capacitance is determined entirely by geometry and material — plate area A, separation distance d, and the dielectric constant ε of the insulating material: C = εA/d. A larger plate area captures more charge for the same voltage; a thinner dielectric brings the charges closer together, strengthening the field and increasing capacitance; a high-ε dielectric concentrates the field more effectively. This means you can tune C by changing the physical structure of the device without changing the circuit it connects to.

The behavior that makes capacitors useful in circuits comes from the voltage-current relationship: **i = C(dv/dt)**. Current flows into a capacitor only when its voltage is changing — if voltage is constant (DC steady state), dv/dt = 0, so current is zero. The capacitor acts like an open circuit for DC. But when voltage is changing rapidly (high-frequency AC), large currents flow even for small voltage swings. This is why capacitors block DC and pass AC, and why their impedance Z_C = 1/(jωC) decreases as frequency ω increases: at high frequency, the capacitor barely resists the changing signal at all.

A practical analogy: think of a capacitor as a spring in a mechanical system, or as a reservoir in a water system. Just as a reservoir stores water and releases it when pressure drops, a capacitor stores charge and releases it when voltage demands it. This energy-storage role is why capacitors are used in power supply filtering (smoothing out voltage ripples), in timing circuits (charging at a predictable rate), and in signal processing (separating AC signal components from DC bias). The key number to internalize is the energy stored: U = ½CV². Double the voltage and the stored energy quadruples — a fact that matters whenever capacitors discharge suddenly.
