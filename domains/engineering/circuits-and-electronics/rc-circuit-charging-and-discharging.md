---
id: rc-circuit-charging-and-discharging
title: RC Circuit Charging and Discharging
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: capacitive-elements-behavior-properties
  type: hard
- id: voltage-and-current-source-characteristics
  type: hard
- id: circuit-laws-kvl-and-kcl
  type: hard
builds-toward:
- rlc-circuit-transient-analysis-overview
- first-order-passive-filters
tags:
- transient-response
- RC-circuits
- exponential-decay
stage: formal-systems
status: draft
---

# RC Circuit Charging and Discharging

## Core Idea
When a voltage source is applied to an RC circuit, the capacitor charges exponentially according to v_C(t) = V(1 − e^(−t/τ)), where τ = RC is the time constant. The capacitor voltage and current change according to first-order differential equations. Understanding RC transients is crucial for analyzing step responses, filters, and timing circuits.

## Explainer

From your study of capacitors, you know that a capacitor stores energy in an electric field and obeys the relationship i = C·(dv/dt): current flows only when voltage is *changing*, not when it is constant. From KVL and KCL, you know how to write equations relating voltages and currents around a loop. The RC circuit brings these together: applying KVL around a series circuit with a resistor R, a capacitor C, and a step voltage source V gives V = v_R + v_C = i·R + v_C. Since i = C·(dv_C/dt), substituting produces a **first-order linear differential equation**: RC·(dv_C/dt) + v_C = V. This single equation contains the entire transient behavior of the circuit.

The solution to this equation is **v_C(t) = V(1 − e^(−t/τ))** for a capacitor initially uncharged, where **τ = RC** is the **time constant**. The intuition: at t = 0, the capacitor looks like a short circuit (zero voltage, maximum current i = V/R). As charge accumulates, the capacitor voltage rises and opposes the source, reducing the current. The charging current decays exponentially while the voltage rises exponentially toward its final value V. The process is self-limiting — as v_C approaches V, the voltage difference driving current shrinks, slowing the charging. This is why the approach to the final value is asymptotic rather than linear.

The **time constant τ = RC** sets the pace of this approach. After one time constant, v_C has reached 63.2% of its final value (since 1 − e^(−1) ≈ 0.632). After 2τ it is at 86.5%, after 3τ at 95%, after 5τ at 99.3% — effectively fully charged. A larger resistance means less current flows for a given voltage difference, so charging is slower. A larger capacitance means more charge must accumulate for a given voltage rise, also slowing things down. Decreasing either R or C speeds up the transient. This is why RC circuits are used as **timing circuits**: the time constant determines how long a capacitor takes to reach a threshold voltage, which can trigger other circuit actions.

**Discharging** is the mirror process. If a charged capacitor (initial voltage V₀) is connected to a resistor with no source, KVL gives v_C(t) = V₀·e^(−t/τ) — an exponential decay to zero at the same rate τ = RC. The current flows in the opposite direction as the capacitor releases its stored energy into the resistor. The general solution for any initial condition and final value is v_C(t) = v_C(∞) + [v_C(0) − v_C(∞)]·e^(−t/τ), which unifies charging and discharging into a single formula: start at the initial value, exponentially approach the final value, at a rate set by τ. This general form applies to all first-order circuits and is the foundation for understanding more complex RLC transients and filter frequency responses.
