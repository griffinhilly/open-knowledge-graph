---
id: parallel-circuits-conductance-current
title: 'Parallel Circuits: Conductance and Current Division'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: circuit-topology-and-elements
  type: hard
- id: kirchhoffs-rules
  type: hard
builds-toward:
- combination-series-parallel-networks
tags:
- circuit analysis
- parallel circuits
- conductance
stage: formal-systems
status: draft
---

# Parallel Circuits: Conductance and Current Division

## Core Idea
In parallel circuits, the same voltage is across all elements. Total conductance G_total = G₁ + G₂ + ... where G = 1/R. Equivalently, 1/R_total = 1/R₁ + 1/R₂ + .... Current divides inversely with resistance: I_i = V/R_i. Parallel circuits are useful for voltage control and current distribution among branches.

## Explainer

From Kirchhoff's rules you know that the voltage drop across any element in a circuit can be computed by applying the loop rule. In a parallel configuration, all branches share the same two endpoints — the same pair of nodes — so by the loop rule, every branch must have exactly the same voltage across it. There is no ambiguity: connect a voltmeter across any branch in a parallel group and you get the same reading. This is the defining feature of parallel circuits, and everything else follows from it.

Since each branch i has the same voltage V and its own resistance R_i, Ohm's law gives I_i = V/R_i independently for each branch. By the junction rule, the total current from the source equals the sum of all branch currents: I_total = V/R₁ + V/R₂ + ... = V(1/R₁ + 1/R₂ + ...). Defining **conductance** G = 1/R (measured in siemens, S) makes this cleaner: I_total = V·G_total, where G_total = G₁ + G₂ + .... Conductances add directly in parallel, exactly as resistances add in series. This symmetry is worth noticing: series and parallel are duals — resistance is additive in series, conductance is additive in parallel.

The **current divider** formula follows immediately: each branch carries a fraction of the total current proportional to its conductance (not its resistance). The branchiest path — lowest resistance, highest conductance — carries the most current. For two resistors in parallel: I₁/I_total = G₁/(G₁ + G₂) = R₂/(R₁ + R₂). This counter-intuitive form (current through R₁ involves R₂ in the numerator) trips up beginners; the logic is that more current takes the path of least resistance, which is the one with the larger G.

The practical consequence is that adding more branches to a parallel network always decreases total resistance and increases total current drawn from the source. This is why household wiring is parallel: each appliance gets full mains voltage regardless of what else is plugged in, and their currents add at the breaker. A series circuit would force all devices to share a single current, dimming lights whenever a heater turns on. The conductance framework makes this additive behavior transparent and is the natural language for analyzing multi-branch current distribution.
