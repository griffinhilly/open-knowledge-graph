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
- id: network-circuit-analysis-methods
  type: soft
builds-toward:
- transient-response-rlc-circuits
- first-order-transient-circuits
tags:
- transients
- rc-circuits
- time-domain
stage: formal-systems
status: validated
---

# Transient Response in RC Circuits

## Core Idea
RC transients describe how voltage and current evolve when capacitors charge or discharge through resistors. The voltage across a charging capacitor in a series RC circuit follows v(t) = V_f + (V_i - V_f)·exp(-t/τ), where τ = RC is the time constant. Understanding these exponential responses is critical for analyzing circuit startup behavior, filter transients, and timing circuits.

## How It's Best Learned
Build a simple RC circuit with a battery, resistor, and capacitor. Measure or calculate the charging voltage at several time intervals and verify the exponential curve. Observe how doubling the resistance or capacitance changes the time constant.

## Common Misconceptions
Students often assume the capacitor charges to full voltage instantly or linearly rather than exponentially. Some confuse the time constant τ with the total charging time—the capacitor theoretically charges forever, reaching about 63% at t = τ and 95% at t = 3τ.

## Questions

```yaml
- question: "A capacitor in a series RC circuit is initially uncharged (V_i = 0). A 12V source is switched in at t = 0, with R = 10 kΩ and C = 100 μF. What is the capacitor voltage at t = τ?"
  type: multiple-choice
  options:
    - "12 V — the capacitor fully charges after one time constant"
    - "6 V — the capacitor charges linearly, reaching half-voltage at τ"
    - "Approximately 7.58 V — the capacitor covers about 63% of the gap from 0 V to 12 V"
    - "0 V — no significant charging occurs until t = 2τ"
  answer: 2
  explanation: "At t = τ, the capacitor has covered 1 − e⁻¹ ≈ 63.2% of the gap between initial (0 V) and final (12 V): 0.632 × 12 ≈ 7.58 V. Option A is the most common misconception — τ is not the time to full charge. The charging curve is exponential (not linear), asymptotically approaching 12 V. At t = 5τ the capacitor is within ~0.7% of 12 V; it theoretically never reaches it in finite time."

- question: "In a series RC circuit, both R and C are doubled. How does the time constant τ change?"
  type: multiple-choice
  options:
    - "τ is halved — larger capacitance and larger resistance have opposing effects"
    - "τ is doubled — only capacitance affects τ; resistance is irrelevant"
    - "τ is quadrupled — since τ = RC and both factors double, the product quadruples"
    - "τ is unchanged — the ratio of R to C stays the same"
  answer: 2
  explanation: "τ = RC. Doubling both gives τ_new = (2R)(2C) = 4RC = 4τ. Both factors independently increase τ: resistance limits the current that can flow into the capacitor (slowing charging), and capacitance requires more charge to reach the final voltage (also slowing charging). These effects multiply, not cancel. The unit check confirms it: Ω × F = (V/A)(C/V) = C/A = seconds."

- question: "A capacitor in an RC circuit reaches its final voltage exactly at t = 5τ seconds."
  type: true-false
  answer: false
  explanation: "The capacitor voltage v_C(t) = V_f + (V_i − V_f)·e^(−t/τ) approaches V_f asymptotically — the term e^(−t/τ) never reaches exactly zero for finite t. At t = 5τ, it is within 1 − e⁻⁵ ≈ 99.3% of V_f, close enough for most engineering purposes, but the exact final value is only reached in the mathematical limit as t → ∞. The common claim 'fully charged after 5τ' is a practical approximation, not an exact statement."

- question: "To find the complete time-domain voltage response for any first-order RC circuit, it is sufficient to know three quantities: the initial capacitor voltage, the final capacitor voltage, and the Thévenin resistance seen by the capacitor."
  type: true-false
  answer: true
  explanation: "The solution is fully determined by v_C(t) = V_f + (V_i − V_f)·e^(−t/τ), where τ = R_Thévenin × C. V_i comes from energy continuity (capacitor voltage cannot jump at the switching instant). V_f comes from DC steady-state analysis (treat the fully charged capacitor as an open circuit). τ comes from the Thévenin resistance seen by the capacitor after switching. These three numbers, and nothing more, determine the exponential transient completely."

- question: "Why can't the voltage across a capacitor change instantaneously when a switch opens or closes in a circuit?"
  type: short-answer
  answer: "Because instantaneous voltage change would require infinite current. The capacitor's constitutive relation is i = C·(dv/dt): current equals capacitance times the rate of voltage change. If voltage changed instantaneously, dv/dt would be infinite, which would require infinite current — impossible in a circuit with finite resistance. The energy stored in the capacitor's electric field must be redistributed gradually through the resistive network, producing the exponential transient."
  explanation: "This energy-continuity principle is what fixes the initial condition V_i: at the moment of switching (t = 0⁺), the capacitor voltage equals what it was just before switching (t = 0⁻), even though the circuit topology has changed. The rest of the circuit may change instantaneously, but the capacitor voltage cannot. This initial condition, combined with the new steady-state and the time constant, fully specifies the exponential transient that follows."
```

## Explainer

In DC steady state — your prerequisite — a fully charged capacitor is an open circuit: voltage is constant and no current flows. But circuits are not always at steady state. Every time a switch opens or closes, or a source changes, the circuit must transition from one equilibrium to another. That transition is the **transient response**, and understanding it means understanding how stored energy redistributes itself through the circuit over time.

The governing equation comes from applying Kirchhoff's voltage law to a series RC circuit with a step voltage source. Summing voltages: V_s = iR + v_C, and since i = C·dv_C/dt, this gives RC·(dv_C/dt) + v_C = V_s. This is a first-order linear ODE with constant coefficients — the same mathematical structure as exponential decay in physics or population models. Its complete solution is v(t) = V_f + (V_i − V_f)·e^(−t/τ), where V_i is the initial capacitor voltage (at t = 0⁻), V_f is the final steady-state voltage (as t → ∞), and **τ = RC** is the **time constant**. Three physical facts determine the solution: the initial voltage, set by energy continuity (capacitor voltage cannot jump at t = 0); the final voltage, found by treating the capacitor as an open circuit in the new DC steady state; and the rate of transition, set by τ.

The time constant τ = RC controls the speed of the transient. At t = τ, the capacitor has covered 1 − e^(−1) ≈ 63% of the gap between initial and final voltage. At t = 2τ it has covered 86%, at t = 3τ about 95%, and at t = 5τ it is within 1% of the final value — effectively settled. A larger resistance limits the current flowing into the capacitor, slowing the charge rate. A larger capacitance requires more charge to reach the final voltage, also slowing the transient. Both effects are captured in the product τ = RC: resistance (Ω = V/A) times capacitance (F = C/V = A·s/V) gives seconds, which is exactly the right unit for a characteristic time.

To solve any RC transient problem systematically, you need exactly three quantities: the initial condition V_i (from energy continuity at the switching instant), the final condition V_f (from DC steady-state analysis with the capacitor open), and the time constant τ (from the Thevenin equivalent resistance seen by the capacitor after switching). With these three, the solution is fully determined: v_C(t) = V_f + (V_i − V_f)·e^(−t/τ). Current follows by differentiation: i(t) = C·dv_C/dt = [(V_i − V_f)/R]·e^(−t/τ). This three-number framework — initial value, final value, time constant — generalizes to RL circuits and is the complete toolkit for all first-order transient analysis. The exponential is not an approximation; it is the exact solution to the physics of energy redistribution through a linear resistive network.
