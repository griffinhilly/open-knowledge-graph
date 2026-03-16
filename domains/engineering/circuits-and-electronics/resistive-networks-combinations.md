---
id: resistive-networks-combinations
title: Series, Parallel, and Combined Resistor Networks
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: ohms-law-and-conductance
  type: hard
- id: ideal-voltage-and-current-sources
  type: hard
builds-toward:
- voltage-divider-and-attenuation
- current-divider-and-distribution
tags:
- resistor-networks
- series
- parallel
- combinations
- simplification
stage: formal-systems
status: draft
---

# Series, Parallel, and Combined Resistor Networks

## Core Idea
Series resistors have identical current and R_total = R₁ + R₂ + ... Parallel resistors have identical voltage and 1/R_total = 1/R₁ + 1/R₂ + ... or G_total = G₁ + G₂ + ... Combinations can be analyzed recursively and are foundational for network simplification before detailed analysis.

## Explainer

From Ohm's law, you know that voltage, current, and resistance are related by V = IR for a single resistor. When multiple resistors are connected together, the same law still governs each element — the question is just how current and voltage distribute across the network. Two fundamental configurations answer this, and understanding each one physically before doing the algebra makes the formulas stick.

In a **series** connection, the resistors are strung end-to-end so that every electron must pass through each one in turn. There is only one path for current, so all resistors carry the same current I. Each resistor drops a portion of the total voltage according to its own Ohm's law: V₁ = IR₁, V₂ = IR₂, and so on. By Kirchhoff's voltage law, these voltage drops must sum to the source voltage: V = I(R₁ + R₂ + ...). The equivalent resistance is the sum: **R_total = R₁ + R₂ + ...**. Physically, series resistors are like adding more obstacles to a single road — each one impedes the same flow, and the total impedance accumulates.

In a **parallel** connection, resistors share the same two nodes, so the voltage across each is identical. Current from the source can split and take any of the parallel branches. By Kirchhoff's current law, the total current is the sum of branch currents: I = V/R₁ + V/R₂ + ... = V(1/R₁ + 1/R₂ + ...). The equivalent conductance adds directly — **G_total = G₁ + G₂ + ...** — and the equivalent resistance is the reciprocal of that sum. Parallel resistors are like adding more lanes to a highway: each new path reduces the overall resistance by providing an easier route for current.

Real networks mix both configurations. The strategy is to identify sub-networks that are purely series or purely parallel, replace them with their equivalent single resistor, and repeat until the entire network collapses to a single element. This recursive simplification only works when the network is a **ladder** (series-parallel reducible); some networks (like a bridge or Wheatstone circuit) cannot be reduced this way and require Kirchhoff's laws directly. For the reducible cases, however, this technique is the fastest path to finding total current, source power, and individual element voltages or currents — and it is the foundation for understanding voltage dividers and current dividers, which are the standard building blocks of electronic signal conditioning.
