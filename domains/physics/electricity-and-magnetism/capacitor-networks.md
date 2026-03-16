---
id: capacitor-networks
title: Capacitors in Series and Parallel
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: energy-stored-capacitors
  type: hard
builds-toward:
- dc-circuit-analysis
tags:
- series
- parallel
- combination
stage: formal-systems
status: draft
---

# Capacitors in Series and Parallel

## Core Idea
Capacitors in series experience the same charge Q but different voltages; total voltage: V_total = Q(1/C₁ + 1/C₂ + ...). Capacitors in parallel have the same voltage but different charges; total charge: Q_total = V(C₁ + C₂ + ...). For series: 1/C_eq = 1/C₁ + 1/C₂ + .... For parallel: C_eq = C₁ + C₂ + ....

## Explainer

From your study of energy stored in capacitors, you know that a capacitor with capacitance C charged to voltage V holds charge Q = CV and stores energy U = ½CV². When you connect capacitors together, the same fundamental constraint — Q = CV — applies to each device, but the network arrangement determines which quantities are shared and which differ.

**Parallel connection** is the simpler case to understand first. Connecting two capacitors in parallel means their terminals are wired together, so both capacitors face exactly the same voltage V across their plates. Each capacitor independently draws the charge it needs: Q₁ = C₁V and Q₂ = C₂V. The total charge drawn from the source is Q_total = Q₁ + Q₂ = (C₁ + C₂)V. From the source's perspective, this looks like a single capacitor with C_eq = C₁ + C₂. Adding capacitors in parallel simply adds their capacitances — intuitive because you are effectively increasing the total plate area available to store charge.

**Series connection** requires more careful reasoning. When you charge a series combination, charge cannot accumulate on the middle plates; every electron that arrives on the outer plate of C₁ repels an equal charge off the inner plate of C₁, which charges the inner plate of C₂. The result is that both capacitors end up with exactly the same charge Q, regardless of their individual capacitances. The voltages, however, differ: V₁ = Q/C₁ and V₂ = Q/C₂. The total voltage is V₁ + V₂ = Q(1/C₁ + 1/C₂), so 1/C_eq = 1/C₁ + 1/C₂. Notice that the equivalent capacitance is always smaller than either individual capacitor — series connection is like increasing the plate separation, which reduces C.

A useful memory anchor: series and parallel combination rules for capacitors are the *opposite* of the rules for resistors. Resistors in series add directly; capacitors in parallel add directly. This is not a coincidence — it reflects the dual relationship between charge storage and current flow. In real circuits, these combination rules let you replace any network of capacitors with a single equivalent capacitance, which enormously simplifies energy storage calculations and circuit analysis.
