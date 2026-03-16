---
id: transient-response-rc-circuits
title: Transient Response in RC Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: series-parallel-capacitor-networks
  type: hard
- id: dc-analysis-steady-state
  type: hard
builds-toward:
- transient-response-rlc-circuits
- first-order-transient-circuits
tags:
- transients
- rc-circuits
- time-domain
stage: formal-systems
status: draft
---

# Transient Response in RC Circuits

## Core Idea
RC transients describe how voltage and current evolve when capacitors charge or discharge through resistors. The voltage across a charging capacitor in a series RC circuit follows v(t) = V_f + (V_i - V_f)·exp(-t/τ), where τ = RC is the time constant. Understanding these exponential responses is critical for analyzing circuit startup behavior, filter transients, and timing circuits.

## How It's Best Learned
Build a simple RC circuit with a battery, resistor, and capacitor. Measure or calculate the charging voltage at several time intervals and verify the exponential curve. Observe how doubling the resistance or capacitance changes the time constant.

## Common Misconceptions
Students often assume the capacitor charges to full voltage instantly or linearly rather than exponentially. Some confuse the time constant τ with the total charging time—the capacitor theoretically charges forever, reaching about 63% at t = τ and 95% at t = 3τ.

## Explainer

In DC steady state — your prerequisite — a fully charged capacitor is an open circuit: voltage is constant and no current flows. But circuits are not always at steady state. Every time a switch opens or closes, or a source changes, the circuit must transition from one equilibrium to another. That transition is the **transient response**, and understanding it means understanding how stored energy redistributes itself through the circuit over time.

The governing equation comes from applying Kirchhoff's voltage law to a series RC circuit with a step voltage source. Summing voltages: V_s = iR + v_C, and since i = C·dv_C/dt, this gives RC·(dv_C/dt) + v_C = V_s. This is a first-order linear ODE with constant coefficients — the same mathematical structure as exponential decay in physics or population models. Its complete solution is v(t) = V_f + (V_i − V_f)·e^(−t/τ), where V_i is the initial capacitor voltage (at t = 0⁻), V_f is the final steady-state voltage (as t → ∞), and **τ = RC** is the **time constant**. Three physical facts determine the solution: the initial voltage, set by energy continuity (capacitor voltage cannot jump at t = 0); the final voltage, found by treating the capacitor as an open circuit in the new DC steady state; and the rate of transition, set by τ.

The time constant τ = RC controls the speed of the transient. At t = τ, the capacitor has covered 1 − e^(−1) ≈ 63% of the gap between initial and final voltage. At t = 2τ it has covered 86%, at t = 3τ about 95%, and at t = 5τ it is within 1% of the final value — effectively settled. A larger resistance limits the current flowing into the capacitor, slowing the charge rate. A larger capacitance requires more charge to reach the final voltage, also slowing the transient. Both effects are captured in the product τ = RC: resistance (Ω = V/A) times capacitance (F = C/V = A·s/V) gives seconds, which is exactly the right unit for a characteristic time.

To solve any RC transient problem systematically, you need exactly three quantities: the initial condition V_i (from energy continuity at the switching instant), the final condition V_f (from DC steady-state analysis with the capacitor open), and the time constant τ (from the Thevenin equivalent resistance seen by the capacitor after switching). With these three, the solution is fully determined: v_C(t) = V_f + (V_i − V_f)·e^(−t/τ). Current follows by differentiation: i(t) = C·dv_C/dt = [(V_i − V_f)/R]·e^(−t/τ). This three-number framework — initial value, final value, time constant — generalizes to RL circuits and is the complete toolkit for all first-order transient analysis. The exponential is not an approximation; it is the exact solution to the physics of energy redistribution through a linear resistive network.
