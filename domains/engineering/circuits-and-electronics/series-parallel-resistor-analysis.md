---
id: series-parallel-resistor-analysis
title: Series and Parallel Resistor Networks
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: kirchhoff-voltage-law
  type: hard
- id: kirchhoff-current-law
  type: hard
builds-toward:
- dc-analysis-steady-state
- series-parallel-capacitor-networks
- series-parallel-inductor-networks
- impedance-admittance-networks
tags:
- circuit-topology
- resistive-circuits
- network-analysis
stage: formal-systems
status: draft
---

# Series and Parallel Resistor Networks

## Core Idea
Resistors in series sum their resistances: R_eq = R₁ + R₂ + ... Resistors in parallel sum reciprocals: 1/R_eq = 1/R₁ + 1/R₂ + ... Real circuits often contain both series and parallel sections, which can be simplified by iteratively combining adjacent elements. This systematic reduction technique simplifies analysis while preserving circuit behavior.

## Explainer

You know from KVL that voltages sum to zero around any closed loop, and from KCL that currents sum to zero at any node. These two laws are the foundation for understanding why series and parallel resistors combine the way they do — the combination rules are not arbitrary formulas to memorize but direct consequences of the laws you already know.

For **series resistors**, all the same current flows through each element (KCL — there are no branching nodes). KVL around the loop says the source voltage equals the sum of voltage drops: V = I×R₁ + I×R₂ = I(R₁+R₂). By definition, the equivalent resistance is V/I, so R_eq = R₁ + R₂. The more resistors you stack in series, the harder it is for current to flow — resistance accumulates. You can think of series resistors as a single long pipe: each segment adds to the total friction against flow.

For **parallel resistors**, both elements share the same two terminal nodes, so they see the same voltage (KVL — the voltage around any loop containing just those two elements is zero). But KCL says the total current from the source splits between the branches: I_total = V/R₁ + V/R₂ = V(1/R₁ + 1/R₂). The equivalent resistance satisfies I_total = V/R_eq, so 1/R_eq = 1/R₁ + 1/R₂. Adding a parallel branch always reduces the equivalent resistance — you are giving current an additional path, making the overall circuit easier to drive. For two resistors, the result simplifies to R_eq = R₁R₂/(R₁+R₂), always less than the smaller of the two.

Real circuits combine both structures. The technique for analysis is **iterative reduction**: find the innermost series or parallel group, replace it with its equivalent, redraw the circuit, and repeat until you are left with a single equivalent resistance. The order of operations matters — you can only combine elements that are strictly in series (same current, no other branches between them) or strictly in parallel (same terminal voltage, connected to the same two nodes). A common error is combining resistors that look geometrically adjacent on a schematic but are not electrically series or parallel; always trace the current path and node connections carefully. Once you have the equivalent resistance and the total current or voltage from the source, you can work backward through the reductions — reintroducing original elements and applying Ohm's law at each stage — to find the current and voltage at every element in the original network. This backward-tracing technique, combined with the voltage divider and current divider rules, gives you a complete toolkit for analyzing any resistive circuit without writing large systems of equations.
