---
id: rl-transient-response
title: Transient Response in RL Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: self-inductance
  type: hard
builds-toward:
- ac-impedance
tags:
- rl-circuit
- transient
- inductance
stage: formal-systems
status: draft
---

# Transient Response in RL Circuits

## Core Idea
In an RL circuit, current grows as I(t) = (V/R)(1 − e^(−t/τ)) when voltage is applied, where τ = L/R is the time constant. Inductance opposes current changes, so initial current is zero and voltage across the inductor is V_L = L dI/dt. At large times, current approaches V/R as inductance effects become negligible. Time constant scales with inductance and inversely with resistance.

## Explainer

From self-inductance, you know that an inductor resists changes in current — its back-EMF is V_L = L dI/dt. When you connect a battery to an RL circuit at t = 0, the inductor doesn't let the current jump instantly to V/R the way a purely resistive circuit would. Instead, the inductor demands that current change gradually. To see why, apply Kirchhoff's voltage law around the loop: V = IR + L dI/dt. This is a first-order linear differential equation, and its solution is I(t) = (V/R)(1 − e^(−t/τ)) where τ = L/R is the **time constant**.

Trace the physics through time. At t = 0, current is zero (the inductor enforces this — any instantaneous jump would require infinite voltage). All of the battery voltage appears across the inductor: V_L = V, while V_R = 0. As current slowly builds, the voltage across the resistor IR grows, so the inductor's share V_L = V − IR shrinks. The inductor's opposition weakens as the rate of change dI/dt decreases. At large times, dI/dt → 0 and the inductor looks like a plain wire: the final current is simply V/R and all the voltage is across the resistor. The exponential curve traces this smooth handoff of voltage from inductor to resistor.

A useful analogy is the RC circuit's transient response, which you may know: a capacitor charges toward its final voltage exponentially with time constant τ = RC, while the resistor voltage decays. The RL circuit is its dual — the inductor's current builds up while the inductor voltage decays. In both cases, the time constant measures the same thing: "how long does the transient last?" After one τ, the current reaches 63% of its final value; after 5τ, it's within 1% and considered steady-state. Large L means slow current rise (the inductor fights harder); large R means fast rise (the resistor dissipates energy quickly, reducing the current overshoot problem).

This transient behavior is why inductors appear in switching power supplies, relay circuits, and motor control — anywhere the sudden interruption or application of current would otherwise cause voltage spikes. When you open a switch in an RL circuit (forcing I → 0 suddenly), the inductor attempts to maintain current by generating a large voltage spike — V_L = L dI/dt with a very large dI/dt. Engineers exploit this in boost converters and must protect against it in relay drivers using flyback diodes. The time constant τ = L/R is the single parameter governing how much time is available to manage these transitions.
