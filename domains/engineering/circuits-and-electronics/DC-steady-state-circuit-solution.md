---
id: DC-steady-state-circuit-solution
title: DC Steady-State Circuit Solutions
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-laws-kvl-and-kcl
  type: hard
- id: circuit-element-types-and-definitions
  type: hard
- id: voltage-and-current-source-characteristics
  type: hard
builds-toward:
- sinusoidal-steady-state-analysis
tags:
- DC-analysis
- steady-state
- circuit-solution
stage: formal-systems
status: validated
---

# DC Steady-State Circuit Solutions

## Core Idea
In DC steady state, capacitors act as open circuits and inductors act as short circuits; only resistors and sources remain. Nodal and mesh analysis, superposition, and Thévenin/Norton equivalents can find the operating point of the circuit. This is the foundation for understanding AC steady state where sources and elements vary sinusoidally.

## Questions

```yaml
- question: "In a DC steady-state circuit, what is the correct equivalent circuit model for a capacitor?"
  type: multiple-choice
  options:
    - "A short circuit — capacitors pass DC current freely once charged"
    - "An open circuit — no DC current flows through a capacitor in steady state"
    - "A resistor whose value is 1/(ωC), where ω is the DC frequency"
    - "A voltage source equal to the initial charge on the capacitor"
  answer: 1
  explanation: "A capacitor's current is I = C · dV/dt. In DC steady state, all voltages are constant, so dV/dt = 0 everywhere. Therefore I = 0: no current flows through the capacitor. A device that passes no current is by definition an open circuit. This substitution rule — replace capacitors with open circuits — is the key tool for DC steady-state analysis. Note that the capacitor can still have a non-zero voltage across it; the open-circuit substitution means no current flows, not that no voltage exists."

- question: "You want to find the voltage across a capacitor in a DC steady-state circuit. A classmate suggests solving the full differential equation for V(t) and then taking the limit as t → ∞. What is the faster correct approach?"
  type: multiple-choice
  options:
    - "Replace the capacitor with a short circuit and solve the resistor network for current through that branch"
    - "Replace the capacitor with an open circuit and solve the remaining resistor network for the voltage at those terminals"
    - "Use phasor analysis with ω = 0 to find the DC impedance of the capacitor"
    - "Apply the voltage divider rule using the capacitor's DC impedance"
  answer: 1
  explanation: "In DC steady state, a capacitor is simply an open circuit — no current flows through it. To find its voltage, replace it with an open circuit and solve the remaining resistor-source network for the open-circuit terminal voltage. Whatever voltage appears across those open terminals is the capacitor's steady-state voltage. This avoids solving any differential equation. Using a short circuit (option A) is the rule for inductors, not capacitors. Phasors and impedance (option C) are AC steady-state tools; at DC (ω = 0), capacitor impedance 1/jωC → ∞, which confirms the open-circuit result, but the direct substitution approach is far simpler."

- question: "In DC steady state, an inductor acts as a short circuit because V = L·dI/dt equals zero when current is not changing."
  type: true-false
  answer: true
  explanation: "True. An inductor's terminal voltage is V = L · dI/dt. In DC steady state, all currents are constant (no time variation), so dI/dt = 0 and therefore V = 0. A circuit element with zero voltage across it is a short circuit — it behaves like a wire. The inductor passes DC current freely with no voltage drop. This is the complement of the capacitor rule: capacitors → open circuits (no current), inductors → short circuits (no voltage). Both follow directly from the condition dV/dt = dI/dt = 0."

- question: "A capacitor in DC steady state cannot have a nonzero voltage across it, because capacitors block DC current and therefore can seldom store energy in a DC circuit."
  type: true-false
  answer: false
  explanation: "False. A capacitor in DC steady state can absolutely have a nonzero voltage across it — in fact, finding that voltage is often the goal of DC steady-state analysis. What is zero in steady state is the *current* through the capacitor (I = C dV/dt = 0). The capacitor holds whatever voltage was established during the transient charging phase. 'Blocks DC current' means zero steady-state current, not zero steady-state voltage. The stored energy ½CV² is nonzero whenever V ≠ 0."

- question: "Explain why a capacitor behaves as an open circuit in DC steady state, and state the physical condition that must hold for this to be true."
  type: short-answer
  answer: "A capacitor's current obeys I = C · dV/dt. In DC steady state, the circuit has reached a time-invariant condition where all voltages and currents are constant — therefore dV/dt = 0 everywhere. Substituting, I = C · 0 = 0: no current flows through the capacitor. By definition, an element through which no current flows is an open circuit. The physical condition that must hold is that the circuit has fully settled after all transients have decayed — no part of the circuit is still changing. During the transient (e.g., right after a switch closes), dV/dt ≠ 0 and the capacitor does carry current."
  explanation: "This is why DC steady-state analysis is sometimes called 'long-time analysis' — it only applies after t → ∞, once all exponential transients have died out. The substitution rules are not approximations; they are exact consequences of dV/dt = dI/dt = 0."
```

## Explainer

**DC steady state** is the condition a circuit reaches after all transients have died out and every voltage and current has settled to a constant value. The word "steady" means no time derivatives: dV/dt = 0 and dI/dt = 0 everywhere. This single condition transforms reactive elements into simple two-terminal devices. Recall from your study of circuit elements that a capacitor's current is I = C · dV/dt. If dV/dt = 0, then I = 0 — a capacitor carries no DC current. It therefore behaves exactly like an **open circuit**: current cannot flow through it, but it can sustain a voltage across it. By the same logic, an inductor's voltage is V = L · dI/dt. If dI/dt = 0, then V = 0 — the inductor drops no voltage and behaves like a **short circuit** (a wire) that passes current freely.

These substitution rules — cap→open, inductor→short — reduce any DC steady-state circuit to a resistor network with independent sources. Once the reactive elements are replaced, you apply the tools you know from KVL and KCL: nodal analysis, mesh analysis, superposition, and Thévenin/Norton reduction. For example, to find the voltage across a capacitor in DC steady state, replace the capacitor with an open circuit and solve the remaining resistor network for the voltage at that node — whatever appears across the open terminals is the capacitor's steady-state voltage. To find the current through an inductor, replace it with a short and solve for the current that flows through that branch.

Thévenin and Norton equivalents are especially powerful here. Any linear DC circuit connected to a load can be reduced to a single voltage source V_Th in series with a single resistance R_Th (or a Norton current source I_N in parallel with R_Th). Finding V_Th in DC steady state means open-circuiting the load and solving for the open-circuit terminal voltage; R_Th is found by zeroing all independent sources (voltage sources become short circuits, current sources become open circuits) and computing the resistance seen at the terminals. These techniques drastically simplify complex networks and will reappear in AC steady state — but there, instead of a resistance R_Th you will encounter a complex **impedance** Z_Th.

This DC steady-state framework is the conceptual bridge to AC analysis. In DC steady state, the "operating point" of the circuit is a single set of fixed voltages and currents. In AC steady state, the sources vary sinusoidally, and the voltages and currents throughout the circuit are also sinusoidal at the same frequency — but with their own amplitudes and phase shifts. The mathematical machinery of phasors and impedances recreates the same nodal/mesh/Thévenin approach in the frequency domain. Every skill you practice here — writing KCL equations, reducing networks, computing Thévenin equivalents — carries over directly, with complex numbers replacing real ones.
