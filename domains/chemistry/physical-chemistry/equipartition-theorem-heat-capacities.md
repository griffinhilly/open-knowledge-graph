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

## Questions

```yaml
- question: "The measured molar heat capacity at constant volume (C_V) for N₂ at room temperature is approximately (5/2)R, not (7/2)R. What is the best explanation?"
  type: multiple-choice
  options:
    - "N₂ only has 5 atoms, so it has fewer degrees of freedom than predicted"
    - "The vibrational degree of freedom is frozen out because the quantum energy spacing is much larger than kT at room temperature"
    - "Rotation about the bond axis is included in the (5/2)R value, accounting for the 'missing' (7/2)R"
    - "N₂ is not an ideal gas, so the equipartition theorem does not apply"
  answer: 1
  explanation: "Equipartition classically predicts (7/2)R for a diatomic: (3/2)R translational + R rotational + R vibrational. But vibrational energy levels are quantized with spacing hν. For N₂ at room temperature, kT ≈ 2.5 kJ/mol while the vibrational quantum for N₂ is much larger — the vibrational mode is 'frozen out' because thermal energy cannot populate excited vibrational states. So only translation and rotation contribute, giving (5/2)R. The classical theorem gives the high-temperature ceiling; quantum mechanics determines when each mode reaches it."

- question: "A monatomic noble gas like neon is heated. According to the equipartition theorem, what is its molar heat capacity C_V?"
  type: multiple-choice
  options:
    - "(1/2)R — only one translational mode"
    - "(3/2)R — three translational degrees of freedom, no rotational or vibrational modes"
    - "(5/2)R — three translational plus two rotational modes"
    - "R — one degree of freedom per atom"
  answer: 1
  explanation: "A monatomic atom has three translational degrees of freedom (motion along x, y, z), each contributing ½R, giving C_V = (3/2)R ≈ 12.5 J/(mol·K). It cannot rotate in the quantum-mechanically relevant sense (no internal axes with significant moment of inertia) and has no vibrational modes. This prediction matches experiment extremely well for noble gases — they are the cleanest test of equipartition because there are no complications from frozen modes or quantum corrections."

- question: "According to the equipartition theorem, each vibrational mode contributes ½R to the molar heat capacity of a molecule at room temperature."
  type: true-false
  answer: false
  explanation: "A fully active vibrational mode contributes R (not ½R) because each vibrational mode has two quadratic energy terms — one kinetic (½μv²) and one potential (½kx²), each contributing ½R. However, at room temperature most vibrational modes are frozen out by quantum effects (hν >> kT), so the actual contribution is essentially zero, not ½R. The ½R per quadratic term is the raw equipartition result, but vibration has two quadratic terms and is typically not thermally accessible anyway."

- question: "At very high temperatures (thousands of kelvin), a diatomic gas like H₂ should approach a C_V of (7/2)R as vibrational modes become thermally accessible."
  type: true-false
  answer: true
  explanation: "As temperature rises, kT eventually becomes comparable to the vibrational energy spacing hν, and the vibrational mode gradually 'thaws.' In the classical (high-T) limit, the vibrational mode contributes its full R (two quadratic terms), bringing C_V from (5/2)R (translation + rotation only) to (7/2)R (all modes active). For H₂, this transition begins noticeably above 1000 K. This is a striking experimental confirmation of quantum mechanics — the stepwise activation of modes as temperature increases is inexplicable in classical physics."

- question: "Why do rotational degrees of freedom contribute to the heat capacity of N₂ at room temperature while vibrational degrees of freedom do not, even though both are present?"
  type: short-answer
  answer: "Both are quantized, but their energy spacings are vastly different. Rotational energy levels are closely spaced (separation << kT at room temperature), so many excited rotational states are thermally populated and the mode behaves classically, contributing R (two modes). Vibrational energy levels are widely spaced (separation >> kT at room temperature) because bond stretching frequencies are much higher than rotational frequencies. The vibrational mode is frozen out — virtually all molecules are in the vibrational ground state — so it contributes essentially nothing to C_V."
  explanation: "The key is comparing the quantum energy spacing to the thermal energy kT. Rotational spacings scale as ℏ²/(2I); for heavy, long molecules like N₂, the moment of inertia I is large, giving small rotational spacings that are easily exceeded by kT at room temperature. Vibrational frequencies are much higher — stretching a chemical bond requires far more energy than rotating the molecule — so hν >> kT, and the Boltzmann factor suppresses excited-state population to negligible levels. This is a fundamental lesson: the equipartition theorem gives the classical (high-T) limit, but quantum mechanics controls which modes actually reach that limit."
```

## Explainer

From your work with partition functions, you know how to connect molecular energy levels to thermodynamic quantities like internal energy and heat capacity. The **equipartition theorem** provides a powerful shortcut for the classical (high-temperature) limit: each independent quadratic term in the energy expression contributes exactly ½kT to the average energy per molecule, or equivalently ½R to the molar heat capacity at constant volume. "Quadratic" means the energy depends on the square of some coordinate or momentum — translational kinetic energy (½mv²), rotational kinetic energy (½Iω²), and both the kinetic and potential terms of vibration all qualify.

Consider a **monatomic ideal gas** like argon. Each atom has three translational degrees of freedom (motion in x, y, z), each contributing ½kT. The total average energy is 3 × ½kT = (3/2)kT per molecule, and C_V = (3/2)R = 12.5 J/(mol·K). There are no rotational or vibrational modes because a single atom has no internal structure to rotate around or vibrate along. This prediction matches experiment perfectly — monatomic gases are the cleanest test case for equipartition.

A **diatomic molecule** like N₂ has more options. It still has three translational degrees of freedom, contributing (3/2)R. It can rotate about two axes perpendicular to the bond axis (rotation about the bond axis itself contributes negligibly because the moment of inertia is tiny). These two rotational modes add 2 × ½R = R. So at moderate temperatures, C_V = (3/2)R + R = (5/2)R ≈ 20.8 J/(mol·K), which agrees well with measurements of N₂ and O₂ at room temperature. But the molecule also has one vibrational mode (bond stretching), which contributes two quadratic terms — one kinetic (½μv²) and one potential (½kx²) — for a total of R. If all modes were fully active, C_V would be (7/2)R ≈ 29.1 J/(mol·K). So why is the room-temperature value only (5/2)R?

This is where the classical equipartition theorem reveals its limits and connects back to quantum mechanics. Vibrational energy levels are quantized, with spacings of hν that are typically much larger than kT at room temperature. When kT << hν, the vibrational mode is effectively **frozen out** — there is not enough thermal energy to populate excited vibrational states, so the mode contributes nothing to the heat capacity. As temperature rises and kT approaches hν, the vibrational contribution gradually "thaws" and approaches the classical R per mode. This is why the heat capacity of H₂ rises from (3/2)R at very low temperatures (only translation active) through (5/2)R at room temperature (translation + rotation) toward (7/2)R at thousands of kelvin (all modes active). Equipartition gives you the ceiling for each mode; quantum statistics tells you when each mode actually reaches that ceiling.
