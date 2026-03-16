---
id: ohms-law-circuits
title: Ohm's Law and Circuit Elements
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: resistance-resistivity-temperature
  type: hard
builds-toward:
- electromotive-force-batteries
- kirchhoff-circuit-laws-rules
tags:
- ohms-law
- circuit-element
- voltage-current
stage: formal-systems
status: draft
---

# Ohm's Law and Circuit Elements

## Core Idea
Ohm's law states V = IR, relating voltage across a resistor to current through it and resistance R. Resistors dissipate power P = I²R = V²/R. Ideal wires have R = 0; ideal insulators have R → ∞.

## Explainer

You already know from resistance and resistivity that a material's resistance comes from its geometry and microscopic properties: R = ρL/A, where ρ is resistivity, L is length, and A is cross-sectional area. **Ohm's law**, V = IR, connects this material property to circuit behavior. It says that if you apply a voltage V across a resistor, a current I = V/R flows through it. Equivalently, if a current I flows, it requires a voltage V = IR to drive it. The relationship is linear: double the voltage, double the current. This linearity is what makes Ohm's law so useful — and also what makes it a *special case* that only holds for ohmic materials.

The circuit element picture simplifies analysis enormously. An **ideal wire** has R = 0, meaning any current flows through it with zero voltage drop — it's a perfect conductor that connects two points at identical potential. An **ideal insulator** has R → ∞, meaning no current flows regardless of voltage — it's an open circuit. Real resistors fall between these extremes, and the V = IR relationship lets you predict exactly how much current flows for any applied voltage. The power dissipated is P = IV = I²R = V²/R, which you can derive by combining P = IV with V = IR.

Ohm's law is not a fundamental law of physics — it's an empirical approximation that holds for many materials over wide ranges. It breaks down for semiconductors (where resistance depends on current direction in diodes), for non-linear elements like transistors, and at extreme temperatures where resistance changes dramatically. The deeper foundation is the Drude model: free electrons in a metal accelerate under an electric field but scatter frequently off lattice ions, reaching a terminal drift velocity proportional to E. This gives J = σE (current density proportional to field), which in macroscopic terms is V = IR.

The power formulas P = I²R and P = V²/R are the two most commonly used in circuit design. P = I²R is natural when current is the known quantity (a series circuit forces the same I through every element). P = V²/R is natural when voltage is known (parallel elements share the same V). Both are correct for any ohmic resistor — they're the same formula in different variables, related by V = IR. The energy delivered to a resistor per unit time becomes heat, which is Joule heating — the same physics expressed as a circuit relationship.
