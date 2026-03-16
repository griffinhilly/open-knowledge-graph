---
id: capacitor-circuits-series-parallel
title: Capacitors in Series and Parallel
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: parallel-plate-capacitor-formula
  type: hard
builds-toward:
- energy-density-electric-field
- dielectric-materials-polarization
tags:
- circuit
- combination
- equivalent
stage: formal-systems
status: draft
---

# Capacitors in Series and Parallel

## Core Idea
Capacitors in parallel have same voltage; equivalent capacitance is C_eq = ΣC_i. In series, charge is same; 1/C_eq = Σ(1/C_i). Series capacitors divide voltage; parallel capacitors sum capacitances.

## How It's Best Learned
Draw circuits with parallel and series configurations, identify equivalent capacitances step-by-step, then verify with limiting cases.

## Explainer

You already know that a parallel-plate capacitor stores charge according to C = Q/V — the capacitance tells you how much charge accumulates per volt of applied voltage. When you combine capacitors in a circuit, the combination rules follow directly from this definition plus two inescapable constraints: voltage is single-valued around any loop, and charge cannot appear from nowhere on isolated conductors.

**Parallel capacitors** share the same two nodes, so they sit across the same voltage V. Each one independently accumulates charge: Q₁ = C₁V, Q₂ = C₂V, and so on. The total charge drawn from the source is Q_total = Q₁ + Q₂ + ... = (C₁ + C₂ + ...)V. Comparing with Q_total = C_eq × V gives C_eq = C₁ + C₂ + ... — capacitances add in parallel. Physically, you are increasing the total plate area that can store charge at the same voltage, so of course the combined device stores more.

**Series capacitors** present a subtler constraint. Consider two capacitors connected end-to-end with no other connections. The segment of conductor between them is electrically isolated — no charge can flow onto or off it from the external circuit. When a charge +Q builds up on the left plate of C₁, it repels an equal +Q off the right plate of C₁, which flows onto the left plate of C₂. By induction the isolated middle conductor redistributes so that each capacitor ends up with exactly the same charge Q. Their voltages differ — V₁ = Q/C₁ and V₂ = Q/C₂ — and the total voltage across the series combination is V = V₁ + V₂ = Q(1/C₁ + 1/C₂). Dividing both sides by Q: 1/C_eq = 1/C₁ + 1/C₂. Series combination reduces capacitance because you are effectively increasing the gap between the "outer" plates while the charge remains fixed.

A useful sanity check: two identical capacitors C in parallel give 2C; the same two in series give C/2. Parallel always increases equivalent capacitance; series always decreases it. For mixed networks, reduce step by step — identify series and parallel sub-groups, replace each with its equivalent, and repeat until one capacitor remains. The rules for capacitors are the algebraic mirror of resistors: the parallel rule for capacitors (add them) is the same form as the series rule for resistors, and vice versa. This swap happens because capacitors and resistors respond to the same circuit constraints (V and I/Q) but in opposite roles.
