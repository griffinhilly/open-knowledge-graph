---
id: energy-stored-in-fields
title: Energy Stored in Electric and Magnetic Fields
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: capacitance
  type: hard
- id: inductance-and-inductors
  type: hard
builds-toward:
- electromagnetic-waves
- maxwells-equations-overview
tags:
- field-energy
- energy-density
- capacitor
- inductor
stage: formal-systems
status: validated
---

# Energy Stored in Electric and Magnetic Fields

## Core Idea
Electric and magnetic fields carry energy with volume densities u_E = ½ε₀E² and u_B = B²/(2μ₀) respectively. For a parallel-plate capacitor, the total stored energy ½CV² equals the integral of u_E over the volume between the plates. Similarly, ½LI² equals the integral of u_B over the solenoid volume. These energy density expressions are fundamental — they show that the electromagnetic field itself is a physical entity that carries energy, not just a mathematical tool.

## How It's Best Learned
Derive u_E from the capacitor energy formula and the relationship C = ε₀A/d, E = V/d. Then derive u_B from the solenoid. These derivations solidify the idea that energy resides in the field, a conceptual cornerstone for electromagnetic waves.

## Common Misconceptions
- The energy is stored in the field throughout the volume, not at the capacitor plates or inductor wire.
- Energy density is proportional to E² and B², not to E or B themselves.
- These expressions are valid for static fields; electromagnetic waves carry energy through both oscillating fields simultaneously.

## Explainer

From your study of capacitors, you know that charging a capacitor requires work — you must push charge onto the plate against the growing electric field. That work has to go somewhere: it goes into the electric field itself. From inductors, you know that building up current through an inductor requires work against the back-EMF the inductor generates. That work goes into the magnetic field. The deep insight here is that **the field is a physical entity that stores energy**, not just a mathematical shorthand for forces between charges.

To find how much energy is stored, derive the **electric energy density** from what you already know. For a parallel-plate capacitor: U = ½CV², and with C = ε₀A/d and E = V/d, substituting gives U = ½ε₀E² × (Ad). The quantity Ad is just the volume between the plates, so the energy per unit volume is u_E = ½ε₀E². The energy isn't locked in the plates — it's spread uniformly through the field-filled volume between them. Perform the analogous derivation for a solenoid: U = ½LI², with L = μ₀n²Al and B = μ₀nI, and you get u_B = B²/(2μ₀) for the magnetic energy density. Same structure, same logic.

These two expressions have an elegant symmetry. Both are proportional to the square of the field — doubling E quadruples u_E, not just doubles it. This nonlinearity matters: a capacitor storing twice the voltage stores four times the energy. The constant out front, ε₀ for electric and 1/μ₀ for magnetic, encodes how "easy" it is for each field type to store energy in vacuum. Note also that you can compute total stored energy by integrating these densities over all space — you don't need to know anything about the charge or current distribution, only the field distribution.

Why does this matter beyond capacitors and inductors? Because electromagnetic waves consist of oscillating electric and magnetic fields propagating through space — and those fields carry energy with them, calculated using exactly these formulas. In a plane wave in vacuum, u_E = u_B at every point: the electric and magnetic fields store equal energy densities, which travel together at speed c. The Poynting vector (energy flux) follows directly from these density expressions. Every time you ask "how much energy is in this electromagnetic field?" — whether it's sunlight, a radio wave, or the field of a charged particle — you are computing an integral of u_E and u_B over the relevant volume.
