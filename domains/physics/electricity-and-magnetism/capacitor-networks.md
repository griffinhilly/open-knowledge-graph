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
status: validated
---

# Capacitors in Series and Parallel

## Core Idea
Capacitors in series experience the same charge Q but different voltages; total voltage: V_total = Q(1/C₁ + 1/C₂ + ...). Capacitors in parallel have the same voltage but different charges; total charge: Q_total = V(C₁ + C₂ + ...). For series: 1/C_eq = 1/C₁ + 1/C₂ + .... For parallel: C_eq = C₁ + C₂ + ....

## Questions

```yaml
- question: "Two capacitors C₁ = 3 μF and C₂ = 6 μF are connected in series and charged by a 9 V battery. What is the charge stored on C₂?"
  type: multiple-choice
  options:
    - "54 μC — C₂ sees the full battery voltage, so Q₂ = C₂ × V = 6 × 9"
    - "36 μC — in series, charge distributes proportionally to capacitance"
    - "18 μC — in series all capacitors carry the same charge: C_eq = 2 μF, so Q = C_eq × V = 18 μC"
    - "9 μC — the voltage splits equally between the two capacitors"
  answer: 2
  explanation: "In series, all capacitors carry the same charge Q regardless of their individual capacitances. C_eq = 1/(1/3 + 1/6) = 1/(1/2) = 2 μF. Q = C_eq × V = 2 × 9 = 18 μC — and this same 18 μC appears on both C₁ and C₂. Option A is the most tempting error: applying Q = CV to C₂ with the full 9 V, as if C₂ were connected directly across the battery. In reality, the voltage across C₂ is V₂ = Q/C₂ = 18/6 = 3 V, not 9 V. The voltage is split, not the charge."

- question: "Adding a capacitor in series always decreases C_eq below the value of either individual capacitor. What is the physical reason?"
  type: multiple-choice
  options:
    - "Series capacitors share the battery voltage, leaving less energy available for each"
    - "Series connection is analogous to increasing the total plate separation — greater separation reduces capacitance, just as in a single capacitor with wider plates"
    - "The inner plates of series capacitors carry opposite charges that partially cancel"
    - "The equivalent series resistance increases, reducing the effective capacitance"
  answer: 1
  explanation: "Capacitance C = ε₀A/d decreases when plate separation d increases. Connecting capacitors in series is physically equivalent to building one capacitor with the sum of their internal gaps — the total effective plate separation is the sum of the individual gaps. More separation → less capacitance → C_eq is smaller than either individual capacitor. Parallel connection does the opposite: it adds plate area (A increases → C increases → C_eq larger than either alone). This physical picture explains why the combination rules for C are the opposite of those for R."

- question: "Capacitors in parallel combine the same way resistors in series do: the equivalent value equals the direct sum of the individual values."
  type: true-false
  answer: true
  explanation: "Capacitors in parallel: C_eq = C₁ + C₂ + ... (direct sum). Resistors in series: R_eq = R₁ + R₂ + ... (direct sum). Both exhibit direct addition because the relevant quantity accumulates in the same direction: parallel capacitors add effective plate area, series resistors add path length for current. This is part of the broader duality between C and R: the combination rules for capacitors are exactly swapped relative to resistors, which the topic explicitly notes as a useful memory anchor."

- question: "When capacitors are connected in series, they all have the same voltage across their terminals."
  type: true-false
  answer: false
  explanation: "In series, all capacitors carry the same charge Q — not the same voltage. The voltage across each capacitor is V = Q/C, so capacitors with different capacitances will have different voltages. Specifically, smaller capacitors carry larger voltage drops (for the same Q, smaller C means larger V = Q/C). Equal voltage is the defining property of parallel connection, not series. Confusing which quantity is shared (charge in series, voltage in parallel) is the most common error in capacitor network problems."

- question: "Why do all capacitors in a series combination end up with the same charge, regardless of their individual capacitance values?"
  type: short-answer
  answer: "The inner plates of adjacent capacitors in a series combination are electrically isolated from the external circuit — no charge can flow onto or off them from outside. When the combination charges, charge accumulates on the outermost plates only. The electric field from those plates induces equal and opposite charges on the adjacent inner plates by polarization. Since each isolated inner conductor must have zero net charge (charge cannot build up on an isolated conductor), whatever charge appears on one face of an inner plate must be exactly balanced on the other face — forcing the same charge Q through every capacitor in the chain."
  explanation: "This is charge conservation applied to isolated internal conductors. If C₁ develops charge +Q on its outer plate, the field induces −Q on the inner face of C₁, which forces +Q on the near face of C₂, which induces −Q on C₂'s outer plate — and so on. Each capacitor receives the same Q regardless of its capacitance. The individual capacitances only determine how much voltage each capacitor 'needs' to accommodate that charge: V = Q/C. This is why a smaller capacitor in a series string has a larger voltage drop than a larger one."
```

## Explainer

From your study of energy stored in capacitors, you know that a capacitor with capacitance C charged to voltage V holds charge Q = CV and stores energy U = ½CV². When you connect capacitors together, the same fundamental constraint — Q = CV — applies to each device, but the network arrangement determines which quantities are shared and which differ.

**Parallel connection** is the simpler case to understand first. Connecting two capacitors in parallel means their terminals are wired together, so both capacitors face exactly the same voltage V across their plates. Each capacitor independently draws the charge it needs: Q₁ = C₁V and Q₂ = C₂V. The total charge drawn from the source is Q_total = Q₁ + Q₂ = (C₁ + C₂)V. From the source's perspective, this looks like a single capacitor with C_eq = C₁ + C₂. Adding capacitors in parallel simply adds their capacitances — intuitive because you are effectively increasing the total plate area available to store charge.

**Series connection** requires more careful reasoning. When you charge a series combination, charge cannot accumulate on the middle plates; every electron that arrives on the outer plate of C₁ repels an equal charge off the inner plate of C₁, which charges the inner plate of C₂. The result is that both capacitors end up with exactly the same charge Q, regardless of their individual capacitances. The voltages, however, differ: V₁ = Q/C₁ and V₂ = Q/C₂. The total voltage is V₁ + V₂ = Q(1/C₁ + 1/C₂), so 1/C_eq = 1/C₁ + 1/C₂. Notice that the equivalent capacitance is always smaller than either individual capacitor — series connection is like increasing the plate separation, which reduces C.

A useful memory anchor: series and parallel combination rules for capacitors are the *opposite* of the rules for resistors. Resistors in series add directly; capacitors in parallel add directly. This is not a coincidence — it reflects the dual relationship between charge storage and current flow. In real circuits, these combination rules let you replace any network of capacitors with a single equivalent capacitance, which enormously simplifies energy storage calculations and circuit analysis.
