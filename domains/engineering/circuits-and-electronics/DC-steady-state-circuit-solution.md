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
- sinusoidal-AC-steady-state-fundamentals
tags:
- DC-analysis
- steady-state
- circuit-solution
stage: formal-systems
status: draft
---

# DC Steady-State Circuit Solutions

## Core Idea
In DC steady state, capacitors act as open circuits and inductors act as short circuits; only resistors and sources remain. Nodal and mesh analysis, superposition, and Thévenin/Norton equivalents can find the operating point of the circuit. This is the foundation for understanding AC steady state where sources and elements vary sinusoidally.

## Explainer

**DC steady state** is the condition a circuit reaches after all transients have died out and every voltage and current has settled to a constant value. The word "steady" means no time derivatives: dV/dt = 0 and dI/dt = 0 everywhere. This single condition transforms reactive elements into simple two-terminal devices. Recall from your study of circuit elements that a capacitor's current is I = C · dV/dt. If dV/dt = 0, then I = 0 — a capacitor carries no DC current. It therefore behaves exactly like an **open circuit**: current cannot flow through it, but it can sustain a voltage across it. By the same logic, an inductor's voltage is V = L · dI/dt. If dI/dt = 0, then V = 0 — the inductor drops no voltage and behaves like a **short circuit** (a wire) that passes current freely.

These substitution rules — cap→open, inductor→short — reduce any DC steady-state circuit to a resistor network with independent sources. Once the reactive elements are replaced, you apply the tools you know from KVL and KCL: nodal analysis, mesh analysis, superposition, and Thévenin/Norton reduction. For example, to find the voltage across a capacitor in DC steady state, replace the capacitor with an open circuit and solve the remaining resistor network for the voltage at that node — whatever appears across the open terminals is the capacitor's steady-state voltage. To find the current through an inductor, replace it with a short and solve for the current that flows through that branch.

Thévenin and Norton equivalents are especially powerful here. Any linear DC circuit connected to a load can be reduced to a single voltage source V_Th in series with a single resistance R_Th (or a Norton current source I_N in parallel with R_Th). Finding V_Th in DC steady state means open-circuiting the load and solving for the open-circuit terminal voltage; R_Th is found by zeroing all independent sources (voltage sources become short circuits, current sources become open circuits) and computing the resistance seen at the terminals. These techniques drastically simplify complex networks and will reappear in AC steady state — but there, instead of a resistance R_Th you will encounter a complex **impedance** Z_Th.

This DC steady-state framework is the conceptual bridge to AC analysis. In DC steady state, the "operating point" of the circuit is a single set of fixed voltages and currents. In AC steady state, the sources vary sinusoidally, and the voltages and currents throughout the circuit are also sinusoidal at the same frequency — but with their own amplitudes and phase shifts. The mathematical machinery of phasors and impedances recreates the same nodal/mesh/Thévenin approach in the frequency domain. Every skill you practice here — writing KCL equations, reducing networks, computing Thévenin equivalents — carries over directly, with complex numbers replacing real ones.
