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

## Explainer

From your prerequisites, you know two things that directly produce the RL transient equation. First, Kirchhoff's Voltage Law (KVL): the voltages around a closed loop must sum to zero. Second, the inductor's defining relationship: v_L = L(di/dt). Combine these for a series RL circuit with a DC voltage source V, a resistor R, and an inductor L: the source voltage must equal the voltage drop across R plus the voltage drop across L. That gives V = Ri + L(di/dt). This is a first-order linear ordinary differential equation in i(t), and its solution is the exponential growth formula i(t) = (V/R)(1 − e^(−t/τ)), where **τ = L/R** is the **time constant**.

The time constant τ is the single most important number characterizing the transient. At t = τ, the current has reached about 63% of its final value V/R. At t = 5τ, it is within 1% of V/R and the circuit is considered to have reached **steady state**. Physically, τ = L/R says the larger the inductance (more energy to store), the slower the approach to steady state; the larger the resistance (more dissipation), the faster the stored magnetic energy is converted to heat and the faster the circuit settles. The final current V/R is just Ohm's law — at DC steady state the inductor is a short circuit (zero voltage drop), so all the source voltage appears across R.

The **inductive kick** is the more dramatic transient — and the one that damages real components. If you open a switch in a circuit carrying steady current I₀ through an inductor, the current cannot instantaneously drop to zero (the inductor resists current change). Instead, v = L(di/dt) produces an enormous spike of voltage as di/dt becomes very large. In a circuit with a switch and a DC source, this spike can easily reach hundreds of volts even from a small battery. This is why motors, solenoids, and relay coils require **flyback diodes** across them — the diode provides a path for the inductor current to flow and dissipate safely rather than producing a destructive voltage spike across the switch.

The RL transient is the inductive counterpart of the RC transient you may have seen with capacitors. In the RC case, it was voltage that grew exponentially (the capacitor charges up); here it is current that grows exponentially (the inductor builds up its magnetic field). The mathematics is structurally identical — same first-order ODE, same exponential solution, same time-constant concept — with the roles of voltage and current exchanged. This parallel is a concrete instance of the capacitor-inductor duality: any analysis technique you apply to one type of circuit can be mirrored for the other by swapping L↔C, V↔I, and R↔G (conductance).
