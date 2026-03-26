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
status: validated
---

# RC Circuit Charging and Discharging

## Core Idea
When a voltage source is applied to an RC circuit, the capacitor charges exponentially according to v_C(t) = V(1 − e^(−t/τ)), where τ = RC is the time constant. The capacitor voltage and current change according to first-order differential equations. Understanding RC transients is crucial for analyzing step responses, filters, and timing circuits.

## Questions

```yaml
- question: "An RC circuit has R = 10 kΩ and C = 100 μF. The capacitor starts uncharged and is connected to a 10 V source. Approximately how long does it take for the capacitor voltage to reach 6.3 V?"
  type: multiple-choice
  options:
    - "1 ms"
    - "100 ms"
    - "1 s — one time constant τ = RC"
    - "10 s"
  answer: 2
  explanation: "τ = RC = (10 × 10³ Ω)(100 × 10⁻⁶ F) = 1 s. After one time constant, v_C = V(1 − e⁻¹) ≈ 10 × 0.632 = 6.32 V ≈ 6.3 V. The time constant is the product of resistance and capacitance — R controls how much current flows for a given voltage difference, and C controls how much charge is needed for a given voltage rise. Both a larger R and a larger C independently slow the transient."

- question: "Why does a capacitor's voltage increase exponentially rather than linearly when connected to a constant voltage source through a resistor?"
  type: multiple-choice
  options:
    - "Because the capacitor's capacitance decreases as it charges, reducing its ability to store more charge"
    - "Because as v_C rises, the voltage difference (V − v_C) across the resistor decreases, reducing current flow and progressively slowing the charging rate"
    - "Because the resistance increases as current heats the resistor, limiting the charging rate"
    - "Because KVL only applies during steady state, not during transient charging"
  answer: 1
  explanation: "The charging current is i = (V − v_C)/R. At t = 0, v_C = 0 so i = V/R (maximum). As the capacitor charges and v_C rises, the voltage available to drive current through R shrinks. Less current means slower charging, which means the rate of voltage rise decreases over time. This self-limiting feedback produces the exponential shape: the closer v_C gets to V, the more slowly it approaches. The process is asymptotic — theoretically never quite reaching V, though for practical purposes it is 'done' after 5τ."

- question: "After one time constant τ = RC, a charging RC circuit has reached approximately 63% of its final voltage, regardless of the specific values of R, C, or the source voltage."
  type: true-false
  answer: true
  explanation: "v_C(τ) = V(1 − e⁻¹) = V × 0.6321... ≈ 63.2% of V, always. The universality comes from the normalized form of the solution — the time constant τ = RC is the natural unit of time for any RC circuit, and after exactly one such unit, the exponent is −1 regardless of what the actual second-count is. This is why τ is so useful: a large RC circuit and a small RC circuit both reach 63% of their final voltage after exactly one of their respective time constants."

- question: "Increasing primarily the capacitance in an RC circuit speeds up the transient response, since a larger capacitor stores more energy and charges faster."
  type: true-false
  answer: false
  explanation: "Increasing C slows the transient — τ = RC increases proportionally. A larger capacitor requires more charge to reach the same voltage (Q = CV), and since the charging current is limited by R, it takes longer. Thinking of C as 'storing more energy' is not wrong, but it leads to the wrong intuition here: more storage capacity at the same charging rate means it takes longer to fill, not shorter. To speed up an RC circuit, you must decrease R, decrease C, or both."

- question: "Explain in physical terms why an RC circuit charges exponentially rather than linearly. What causes the charging rate to decrease over time?"
  type: short-answer
  answer: "Charging rate is proportional to the current flowing into the capacitor, which by Ohm's law equals (V_source − v_C)/R. As the capacitor charges, its voltage v_C rises, reducing the voltage difference available to drive current through R. Less current means charge accumulates more slowly, which means voltage rises more slowly — which in turn reduces the driving current further. This positive-feedback-in-reverse (a self-limiting process) produces the characteristic exponential decay of the charging rate and exponential rise of the voltage."
  explanation: "The governing differential equation RC(dv_C/dt) + v_C = V has the form 'rate of change is proportional to the remaining gap' — dv_C/dt = (V − v_C)/RC. Whenever the rate of change of a quantity is proportional to how far it is from its final value, the solution is exponential. Linear charging would require constant current, which would require a constant voltage across R, which would require v_C to stay constant — a contradiction. The exponential is not an approximation; it is the exact solution to the physics."
```

## Explainer

From your study of capacitors, you know that a capacitor stores energy in an electric field and obeys the relationship i = C·(dv/dt): current flows only when voltage is *changing*, not when it is constant. From KVL and KCL, you know how to write equations relating voltages and currents around a loop. The RC circuit brings these together: applying KVL around a series circuit with a resistor R, a capacitor C, and a step voltage source V gives V = v_R + v_C = i·R + v_C. Since i = C·(dv_C/dt), substituting produces a **first-order linear differential equation**: RC·(dv_C/dt) + v_C = V. This single equation contains the entire transient behavior of the circuit.

The solution to this equation is **v_C(t) = V(1 − e^(−t/τ))** for a capacitor initially uncharged, where **τ = RC** is the **time constant**. The intuition: at t = 0, the capacitor looks like a short circuit (zero voltage, maximum current i = V/R). As charge accumulates, the capacitor voltage rises and opposes the source, reducing the current. The charging current decays exponentially while the voltage rises exponentially toward its final value V. The process is self-limiting — as v_C approaches V, the voltage difference driving current shrinks, slowing the charging. This is why the approach to the final value is asymptotic rather than linear.

The **time constant τ = RC** sets the pace of this approach. After one time constant, v_C has reached 63.2% of its final value (since 1 − e^(−1) ≈ 0.632). After 2τ it is at 86.5%, after 3τ at 95%, after 5τ at 99.3% — effectively fully charged. A larger resistance means less current flows for a given voltage difference, so charging is slower. A larger capacitance means more charge must accumulate for a given voltage rise, also slowing things down. Decreasing either R or C speeds up the transient. This is why RC circuits are used as **timing circuits**: the time constant determines how long a capacitor takes to reach a threshold voltage, which can trigger other circuit actions.

**Discharging** is the mirror process. If a charged capacitor (initial voltage V₀) is connected to a resistor with no source, KVL gives v_C(t) = V₀·e^(−t/τ) — an exponential decay to zero at the same rate τ = RC. The current flows in the opposite direction as the capacitor releases its stored energy into the resistor. The general solution for any initial condition and final value is v_C(t) = v_C(∞) + [v_C(0) − v_C(∞)]·e^(−t/τ), which unifies charging and discharging into a single formula: start at the initial value, exponentially approach the final value, at a rate set by τ. This general form applies to all first-order circuits and is the foundation for understanding more complex RLC transients and filter frequency responses.
