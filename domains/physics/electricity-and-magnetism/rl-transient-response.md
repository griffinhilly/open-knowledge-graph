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
