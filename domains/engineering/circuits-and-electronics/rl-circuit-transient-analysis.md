---
id: rl-circuit-transient-analysis
title: RL Circuit Transient Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: inductive-elements-behavior-properties
  type: hard
- id: voltage-and-current-source-characteristics
  type: hard
- id: circuit-laws-kvl-and-kcl
  type: hard
builds-toward:
- rlc-circuit-transient-analysis-overview
tags:
- transient-response
- RL-circuits
- exponential-growth
stage: formal-systems
status: draft
---

# RL Circuit Transient Analysis

## Core Idea
When a voltage source is applied to an RL circuit, the inductor resists current change; the current grows exponentially as i(t) = (V/R)(1 − e^(−t/τ)), where τ = L/R. The inductor produces a voltage spike when the circuit is opened. RL transients model inductive kick and switching transients in real circuits.

## Questions

```yaml
- question: "A series RL circuit has reached DC steady state with constant current flowing. What is the voltage across the inductor at this moment?"
  type: multiple-choice
  options:
    - "Equal to the source voltage V — the inductor carries all the voltage at steady state"
    - "Equal to IR — the same as the resistor voltage, since they share current"
    - "Zero — because current is constant, di/dt = 0, and v_L = L(di/dt)"
    - "Equal to L/R — the time constant expressed as a voltage"
  answer: 2
  explanation: "The inductor's defining equation is v_L = L(di/dt). At DC steady state, current is not changing — di/dt = 0 — so the voltage across the inductor is zero regardless of its inductance. The inductor acts as a short circuit (a wire) at DC steady state. All the source voltage appears across the resistor, giving steady-state current I = V/R by Ohm's law. A common mistake is to think the inductor 'holds' voltage permanently — it does not."

- question: "An RL circuit has L = 2 H and R = 4 Ω. A 12 V source is suddenly switched in. What are the time constant τ and the final steady-state current?"
  type: multiple-choice
  options:
    - "τ = 8 s, I_final = 3 A"
    - "τ = 0.5 s, I_final = 3 A"
    - "τ = 2 s, I_final = 12 A"
    - "τ = 0.5 s, I_final = 48 A"
  answer: 1
  explanation: "The time constant is τ = L/R = 2/4 = 0.5 s. The final steady-state current is I_final = V/R = 12/4 = 3 A (at steady state the inductor is a short circuit, so all voltage is across R). At t = τ = 0.5 s, the current has reached about 63% of 3 A ≈ 1.89 A. Option A has the wrong formula (τ = LR instead of L/R); option C has a wrong final current; option D compounds both errors."

- question: "Placing a flyback diode across an inductor (e.g., a motor coil or relay) protects circuit components by giving the inductor current a path to flow and dissipate safely when a switch opens."
  type: true-false
  answer: true
  explanation: "When a switch opens abruptly in a circuit carrying steady current through an inductor, the inductor resists the sudden change: v_L = L(di/dt) becomes very large as di/dt spikes. Without a path for the current, this voltage spike can destroy the switch or other components. A flyback diode provides a low-impedance loop for the inductor current to circulate and decay, limiting the voltage spike to the diode's forward voltage (≈0.7 V). This is standard protection for any inductive load."

- question: "When a DC source is suddenly connected to a series RL circuit, the current immediately jumps to its final value V/R and then remains constant."
  type: true-false
  answer: false
  explanation: "The inductor resists any instantaneous change in current — this is its fundamental property. At the instant the switch closes (t = 0), the current is zero (assuming it was zero before). It then grows exponentially: i(t) = (V/R)(1 − e^(−t/τ)), reaching V/R only asymptotically. At t = 5τ it is within 1% of V/R and considered at steady state. An instantaneous jump to V/R would require infinite di/dt and thus infinite voltage across the inductor, which is physically impossible."

- question: "Why does an inductor produce a large voltage spike when a switch suddenly opens a circuit carrying steady current? Use the inductor's defining equation to explain."
  type: short-answer
  answer: "The inductor's defining equation is v_L = L(di/dt). When a switch opens abruptly, the current through the inductor tries to drop from its steady value I₀ to zero in an extremely short time Δt. This means di/dt = −I₀/Δt, which is a very large negative number. Multiplied by L, this produces a very large voltage spike across the inductor — large enough to arc across the switch or destroy components. The inductor is 'fighting' to maintain the current by generating whatever voltage is necessary."
  explanation: "This is the dual of the capacitor's behavior: a capacitor resists instantaneous voltage changes (v = Q/C), while an inductor resists instantaneous current changes (v = L di/dt). The inductive kick is the practical consequence of this resistance: suddenly removing the current path forces v_L to become enormous. Flyback diodes and snubber circuits in motor drives, relay coils, and solenoids are all designed to manage this effect safely."
```

## Explainer

From your prerequisites, you know two things that directly produce the RL transient equation. First, Kirchhoff's Voltage Law (KVL): the voltages around a closed loop must sum to zero. Second, the inductor's defining relationship: v_L = L(di/dt). Combine these for a series RL circuit with a DC voltage source V, a resistor R, and an inductor L: the source voltage must equal the voltage drop across R plus the voltage drop across L. That gives V = Ri + L(di/dt). This is a first-order linear ordinary differential equation in i(t), and its solution is the exponential growth formula i(t) = (V/R)(1 − e^(−t/τ)), where **τ = L/R** is the **time constant**.

The time constant τ is the single most important number characterizing the transient. At t = τ, the current has reached about 63% of its final value V/R. At t = 5τ, it is within 1% of V/R and the circuit is considered to have reached **steady state**. Physically, τ = L/R says the larger the inductance (more energy to store), the slower the approach to steady state; the larger the resistance (more dissipation), the faster the stored magnetic energy is converted to heat and the faster the circuit settles. The final current V/R is just Ohm's law — at DC steady state the inductor is a short circuit (zero voltage drop), so all the source voltage appears across R.

The **inductive kick** is the more dramatic transient — and the one that damages real components. If you open a switch in a circuit carrying steady current I₀ through an inductor, the current cannot instantaneously drop to zero (the inductor resists current change). Instead, v = L(di/dt) produces an enormous spike of voltage as di/dt becomes very large. In a circuit with a switch and a DC source, this spike can easily reach hundreds of volts even from a small battery. This is why motors, solenoids, and relay coils require **flyback diodes** across them — the diode provides a path for the inductor current to flow and dissipate safely rather than producing a destructive voltage spike across the switch.

The RL transient is the inductive counterpart of the RC transient you may have seen with capacitors. In the RC case, it was voltage that grew exponentially (the capacitor charges up); here it is current that grows exponentially (the inductor builds up its magnetic field). The mathematics is structurally identical — same first-order ODE, same exponential solution, same time-constant concept — with the roles of voltage and current exchanged. This parallel is a concrete instance of the capacitor-inductor duality: any analysis technique you apply to one type of circuit can be mirrored for the other by swapping L↔C, V↔I, and R↔G (conductance).
