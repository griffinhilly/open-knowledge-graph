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

## Explainer

You've learned KVL, KCL, and series-parallel resistor analysis — the complete toolkit for solving resistive circuits. DC steady-state analysis extends those tools to circuits containing capacitors and inductors, but does so by exploiting a key physical insight: in a circuit powered by a constant (DC) source, all voltages and currents eventually stop changing. This "settled" condition is the **DC steady state**, and it dramatically simplifies the math.

The key is understanding what capacitors and inductors do when nothing is changing. A capacitor's current is i = C(dV/dt) — the current through a capacitor is proportional to the *rate of change* of voltage across it. In DC steady state, voltages aren't changing (dV/dt = 0), so capacitor current = 0. No current flows through it — it behaves exactly like a wire break, or an **open circuit**. Intuitively: the capacitor has charged up to whatever voltage the circuit imposes on it, and no current is needed to maintain that charge. An inductor's voltage is V = L(di/dt) — voltage is proportional to the *rate of change* of current through it. In steady state, currents aren't changing (di/dt = 0), so inductor voltage = 0. Zero voltage across a component means it behaves like a **short circuit**, or an ideal wire. These two rules — capacitor → open, inductor → short — reduce any DC steady-state circuit to a purely resistive one, which you already know how to solve with KVL and KCL.

Consider a concrete example: a DC source connected to a series RC circuit (resistor and capacitor). When you first connect the source, current flows and charges the capacitor. Eventually the capacitor charges to the source voltage, current drops to zero, and the circuit reaches steady state. Apply the rule: replace the capacitor with an open circuit. Now the circuit is just the source with an open wire — no current flows (consistent with what we just said), and the capacitor voltage equals the full source voltage (confirmed by KVL: all voltage appears across the open circuit element). A series RL circuit in steady state: replace the inductor with a short circuit. Now the circuit is the source connected to the resistor in series with a wire — current flows as I = V/R, and the voltage across the "wire" (inductor) is zero.

The value of DC steady-state analysis extends beyond the steady state itself. For amplifier circuits — which you'll study soon — every transistor has an **operating point** (bias point) determined by DC conditions. The small-signal behavior of the amplifier depends critically on where this DC operating point sits on the transistor's characteristic curves. DC analysis tells you the quiescent voltages and currents; AC analysis (using superposition, assuming DC sources are off) tells you how signals get amplified around that point. The DC steady state is not a special-case curiosity — it is the foundation on which all transient and AC analysis rests.
