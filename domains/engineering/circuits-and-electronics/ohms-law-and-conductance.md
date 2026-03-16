---
id: ohms-law-and-conductance
title: Ohm's Law and Resistance
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: electric-potential-and-voltage
  type: hard
- id: charge-and-current-flow
  type: hard
builds-toward:
- resistive-networks-combinations
- circuit-laws-kvl-and-kcl
tags:
- ohms-law
- resistance
- conductance
- linearity
stage: formal-systems
status: draft
---

# Ohm's Law and Resistance

## Core Idea
Ohm's law states V = IR for a resistor, establishing linear proportionality between voltage and current. Resistance quantifies opposition to current flow and is material and geometry dependent. Power dissipated is P = I²R = V²/R. Conductance G = 1/R simplifies parallel circuit analysis.

## Explainer

From your study of electric potential and current, you know that **voltage** (V) is the energy per unit charge—the electrical "pressure" that pushes charges through a circuit—and that **current** (I) is the rate of charge flow. **Ohm's Law**, V = IR, connects them through a third quantity: **resistance** (R), which measures how strongly a material opposes the flow of current. A large resistance means a large voltage is required to drive even a modest current; a small resistance allows large currents at low voltages.

The proportionality in V = IR is the key insight: for an ohmic material, doubling the voltage exactly doubles the current. This linearity makes resistors the most mathematically tractable circuit element. Resistance depends on the material's **resistivity** (ρ) and its geometry: R = ρL/A, where L is the length of the conductor and A is its cross-sectional area. A long, thin wire has much higher resistance than a short, thick one of the same material. Metals have low resistivity (good conductors); rubber and glass have high resistivity (good insulators). This geometry dependence is why wiring gauge matters in practical circuits—undersized wire for a given current is a fire hazard.

**Power dissipation** follows directly from combining V = IR with the definition of power P = VI. Substituting V = IR gives P = I²R; substituting I = V/R gives P = V²/R. Both forms are useful—use P = I²R when you know the current (typical in series circuits), and P = V²/R when you know the voltage (typical in parallel circuits). This power becomes heat in the resistor, which is the physical basis for toaster wires, electric heaters, and incandescent light bulbs. Every real component has a maximum power rating; exceeding it causes failure, so power calculations are as important as voltage and current calculations in any real design.

**Conductance** G = 1/R, measured in Siemens (S), is simply resistance inverted: it measures how *easily* current flows. When resistors are connected in parallel, their conductances add directly (G_total = G_1 + G_2 + ...), just as resistances add directly in series. This symmetry is not coincidence—it reflects the duality of series and parallel analysis. Choosing to work in resistance or conductance is a matter of which topology dominates: series-heavy circuits favor resistance arithmetic, parallel-heavy circuits favor conductance arithmetic. Both are just different lenses on the same physical relationship V = IR.
