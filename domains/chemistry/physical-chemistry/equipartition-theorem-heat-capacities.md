---
id: equipartition-theorem-heat-capacities
title: Equipartition Theorem and Molecular Heat Capacities
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-partition-functions-theory
  type: hard
- id: heat-capacity-calorimetry
  type: soft
tags:
- statistical
- thermodynamics
- heat-capacity
- energy
stage: advanced
status: draft
---

# Equipartition Theorem and Molecular Heat Capacities

## Core Idea
The equipartition theorem states that each quadratic degree of freedom (translational, rotational, vibrational) contributes ½kT to average energy, hence ½R to molar heat capacity. This classical result explains why C_V ≈ (5/2)R for diatomic gases at room temperature (3 translational + 2 rotational). Vibrational degrees of freedom only activate at high T when kT approaches vibrational quantization energy.

## Explainer

From your work with partition functions, you know how to connect molecular energy levels to thermodynamic quantities like internal energy and heat capacity. The **equipartition theorem** provides a powerful shortcut for the classical (high-temperature) limit: each independent quadratic term in the energy expression contributes exactly ½kT to the average energy per molecule, or equivalently ½R to the molar heat capacity at constant volume. "Quadratic" means the energy depends on the square of some coordinate or momentum — translational kinetic energy (½mv²), rotational kinetic energy (½Iω²), and both the kinetic and potential terms of vibration all qualify.

Consider a **monatomic ideal gas** like argon. Each atom has three translational degrees of freedom (motion in x, y, z), each contributing ½kT. The total average energy is 3 × ½kT = (3/2)kT per molecule, and C_V = (3/2)R = 12.5 J/(mol·K). There are no rotational or vibrational modes because a single atom has no internal structure to rotate around or vibrate along. This prediction matches experiment perfectly — monatomic gases are the cleanest test case for equipartition.

A **diatomic molecule** like N₂ has more options. It still has three translational degrees of freedom, contributing (3/2)R. It can rotate about two axes perpendicular to the bond axis (rotation about the bond axis itself contributes negligibly because the moment of inertia is tiny). These two rotational modes add 2 × ½R = R. So at moderate temperatures, C_V = (3/2)R + R = (5/2)R ≈ 20.8 J/(mol·K), which agrees well with measurements of N₂ and O₂ at room temperature. But the molecule also has one vibrational mode (bond stretching), which contributes two quadratic terms — one kinetic (½μv²) and one potential (½kx²) — for a total of R. If all modes were fully active, C_V would be (7/2)R ≈ 29.1 J/(mol·K). So why is the room-temperature value only (5/2)R?

This is where the classical equipartition theorem reveals its limits and connects back to quantum mechanics. Vibrational energy levels are quantized, with spacings of hν that are typically much larger than kT at room temperature. When kT << hν, the vibrational mode is effectively **frozen out** — there is not enough thermal energy to populate excited vibrational states, so the mode contributes nothing to the heat capacity. As temperature rises and kT approaches hν, the vibrational contribution gradually "thaws" and approaches the classical R per mode. This is why the heat capacity of H₂ rises from (3/2)R at very low temperatures (only translation active) through (5/2)R at room temperature (translation + rotation) toward (7/2)R at thousands of kelvin (all modes active). Equipartition gives you the ceiling for each mode; quantum statistics tells you when each mode actually reaches that ceiling.
