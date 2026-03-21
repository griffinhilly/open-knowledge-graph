---
id: dc-analysis-steady-state
title: DC Steady-State Circuit Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: kirchhoff-voltage-law
  type: hard
- id: kirchhoff-current-law
  type: hard
- id: series-parallel-resistor-analysis
  type: hard
builds-toward:
- transient-response-rc-circuits
- transient-response-rl-circuits
tags:
- dc-analysis
- circuit-analysis
- steady-state
stage: formal-systems
status: draft
---

# DC Steady-State Circuit Analysis

## Core Idea
In DC steady state, capacitors act as open circuits (no current flows through them) and inductors act as short circuits (zero voltage across them). Under these conditions, DC circuits reduce to purely resistive networks analyzable with KVL, KCL, voltage dividers, and current dividers. Steady-state analysis provides the quiescent operating point essential for understanding transient behavior.

## Questions

```yaml
- question: "A DC source is connected in series with a 10 kΩ resistor and a capacitor. After a long time (DC steady state), what is the current through the circuit?"
  type: multiple-choice
  options:
    - "I = V/R — the resistor limits the current just as in a resistive circuit"
    - "I = 0 — in steady state the capacitor acts as an open circuit, blocking DC current"
    - "I = V/Xc — the capacitive reactance limits current at DC"
    - "I depends on the capacitance C and how long the circuit has been running"
  answer: 1
  explanation: "In DC steady state, the capacitor has fully charged to the source voltage (via KVL: all voltage drops across the open circuit element). Once charged, no current flows — the capacitor acts as a wire break (open circuit). A student who answered A is applying the AC or transient model, where Xc = 1/ωC gives a finite impedance. At DC (ω = 0), Xc → ∞ — truly open. Answer D describes the transient phase that precedes steady state."

- question: "An inductor L is in series with a resistor R connected to a DC source V. In DC steady state, what is the voltage across the inductor?"
  type: multiple-choice
  options:
    - "V_L = L × I, where I is the steady-state current"
    - "V_L = V (the source voltage) — the inductor stores it as magnetic energy"
    - "V_L = 0 — the inductor acts as a short circuit (ideal wire) in steady state"
    - "V_L = V − IR, where I = V/L"
  answer: 2
  explanation: "In DC steady state, current is constant (di/dt = 0). The inductor's voltage is V = L(di/dt) = L × 0 = 0. Zero voltage across a component means it behaves like a short circuit — an ideal wire. The steady-state current is then I = V/R (the inductor wire and resistor in series from a voltage source). Option A confuses the inductance formula with resistor behavior. Option B incorrectly applies the transient energy-storage behavior to the steady state."

- question: "In DC steady state, a capacitor behaves like an open circuit because it has fully charged and no longer allows current to flow through it."
  type: true-false
  answer: true
  explanation: "True. The capacitor's current equation is i = C(dV/dt). In steady state, nothing is changing — voltages are constant — so dV/dt = 0 and i = 0. No current through a component means it behaves like a wire break (open circuit). The capacitor has charged to whatever voltage the rest of the circuit imposes on it (determined by KVL after replacing it with an open), and it sustains that voltage indefinitely without requiring further current."

- question: "In DC steady state, a capacitor has zero voltage across it, because no current flows through it."
  type: true-false
  answer: false
  explanation: "False — this is a critical misconception. The capacitor has zero *current*, not zero voltage. It acts as an open circuit, so the full source voltage (or whatever KVL distributes to it) appears across it. In a simple series RC circuit in steady state, the capacitor charges up to the source voltage: all of V appears across the open-circuit capacitor, not across the resistor (since no current means no resistive voltage drop). Confusing 'open circuit' with 'zero voltage' leads to incorrect operating point calculations."

- question: "Explain physically why a capacitor acts as an open circuit in DC steady state. Use the relationship i = C(dV/dt) in your answer."
  type: short-answer
  answer: "A capacitor's current is i = C(dV/dt) — it only allows current to flow when the voltage across it is changing. In DC steady state, all voltages and currents have reached constant values (by definition). With dV/dt = 0, the current through the capacitor is exactly zero. A component through which no current flows is — by definition — an open circuit. Physically, the capacitor has charged to the voltage the circuit imposes on it; once charged to that voltage, there is no net electric field driving further charge transfer, so current stops."
  explanation: "The contrast with an inductor is instructive: an inductor's voltage is V = L(di/dt), which is zero when current is constant — making it a short circuit. Capacitor: blocks DC (open circuit). Inductor: passes DC (short circuit). Both rules follow directly from the defining equations of each element, applied at steady state where all time derivatives are zero."
```

## Explainer

You've learned KVL, KCL, and series-parallel resistor analysis — the complete toolkit for solving resistive circuits. DC steady-state analysis extends those tools to circuits containing capacitors and inductors, but does so by exploiting a key physical insight: in a circuit powered by a constant (DC) source, all voltages and currents eventually stop changing. This "settled" condition is the **DC steady state**, and it dramatically simplifies the math.

The key is understanding what capacitors and inductors do when nothing is changing. A capacitor's current is i = C(dV/dt) — the current through a capacitor is proportional to the *rate of change* of voltage across it. In DC steady state, voltages aren't changing (dV/dt = 0), so capacitor current = 0. No current flows through it — it behaves exactly like a wire break, or an **open circuit**. Intuitively: the capacitor has charged up to whatever voltage the circuit imposes on it, and no current is needed to maintain that charge. An inductor's voltage is V = L(di/dt) — voltage is proportional to the *rate of change* of current through it. In steady state, currents aren't changing (di/dt = 0), so inductor voltage = 0. Zero voltage across a component means it behaves like a **short circuit**, or an ideal wire. These two rules — capacitor → open, inductor → short — reduce any DC steady-state circuit to a purely resistive one, which you already know how to solve with KVL and KCL.

Consider a concrete example: a DC source connected to a series RC circuit (resistor and capacitor). When you first connect the source, current flows and charges the capacitor. Eventually the capacitor charges to the source voltage, current drops to zero, and the circuit reaches steady state. Apply the rule: replace the capacitor with an open circuit. Now the circuit is just the source with an open wire — no current flows (consistent with what we just said), and the capacitor voltage equals the full source voltage (confirmed by KVL: all voltage appears across the open circuit element). A series RL circuit in steady state: replace the inductor with a short circuit. Now the circuit is the source connected to the resistor in series with a wire — current flows as I = V/R, and the voltage across the "wire" (inductor) is zero.

The value of DC steady-state analysis extends beyond the steady state itself. For amplifier circuits — which you'll study soon — every transistor has an **operating point** (bias point) determined by DC conditions. The small-signal behavior of the amplifier depends critically on where this DC operating point sits on the transistor's characteristic curves. DC analysis tells you the quiescent voltages and currents; AC analysis (using superposition, assuming DC sources are off) tells you how signals get amplified around that point. The DC steady state is not a special-case curiosity — it is the foundation on which all transient and AC analysis rests.
