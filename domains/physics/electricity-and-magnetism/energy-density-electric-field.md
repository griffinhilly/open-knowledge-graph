---
id: energy-density-electric-field
title: Energy Density in Electric Fields
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: potential-energy-systems
  type: hard
- id: dielectric-susceptibility-constant
  type: soft
builds-toward:
- electric-current-definition
tags:
- energy
- density
- field
stage: formal-systems
status: validated
---

# Energy Density in Electric Fields

## Core Idea
Energy density in an electric field is u = ½ε₀εᵣE². Total energy stored in a capacitor is U = ½CV² = ½QV = Q²/(2C), which can be recovered as field energy integrated over volume.

## Questions

```yaml
- question: "A parallel-plate capacitor is charged to voltage V and then disconnected from the battery. The plates are pulled apart, doubling the separation d. What happens to the stored energy?"
  type: multiple-choice
  options:
    - "It stays the same because the charge Q on the plates is conserved"
    - "It doubles, because U = Q²/(2C) and C = ε₀A/d, so halving C doubles U"
    - "It halves, because the electric field E = Q/(ε₀A) weakens as the plates move further apart"
    - "It stays the same because U = ½CV² and V doesn't change after disconnection"
  answer: 1
  explanation: "When disconnected, Q is fixed (no path for charge to flow). The right formula is U = Q²/(2C). Pulling the plates apart doubles d, which halves C = ε₀A/d. With Q fixed and C halved, U = Q²/(2C) doubles. Note: option A is wrong because conserved charge does not mean conserved energy — work is done by the electric field as the plates separate. Option D is wrong because V = Q/C does change when C changes and Q is fixed — disconnecting fixes Q, not V."

- question: "Where is the energy of a charged capacitor physically stored?"
  type: multiple-choice
  options:
    - "In the chemical potential of the battery that originally charged it"
    - "In the electric field occupying the space between the plates, as energy per unit volume u = ½ε₀E²"
    - "In the surface charge distribution on the capacitor plates"
    - "In the connecting wires as kinetic energy of electrons"
  answer: 1
  explanation: "This is the conceptual leap at the heart of field theory. When you charge a capacitor, you do work against the repulsion of existing charges. That work is stored in the electric field itself — every cubic meter of space with field strength E contains ½ε₀E² joules of energy. This is not a metaphor or accounting convenience. The field-energy view is confirmed by the fact that electromagnetic waves (with no charges present) carry energy through empty space, described by the same field-energy density expression."

- question: "Any region of space that contains an electric field contains real, physically stored energy proportional to the square of the field strength."
  type: true-false
  answer: true
  explanation: "This is the meaning of u = ½ε₀E². The energy is in the field, not in the charges. This perspective generalizes beyond capacitors: the electric field between any charged objects, the field around a point charge, and even the oscillating fields of electromagnetic waves all carry energy described by this density. The field is a real physical entity, not just a mathematical tool for calculating forces."

- question: "The three formulas U = ½CV², U = ½QV, and U = Q²/(2C) give different values for the same capacitor and the user should choose the most accurate one."
  type: true-false
  answer: false
  explanation: "All three formulas are exactly equivalent for a given capacitor — they describe the same quantity using different pairs of variables. The choice between them is about which variables are known or held constant, not accuracy. Use ½CV² when voltage V is given (e.g., charged from a fixed battery). Use Q²/(2C) when charge Q is held fixed (e.g., after disconnecting from the battery). Use ½QV as a bridge form. They will always give the same numerical answer for the same physical situation."

- question: "Why is it significant that energy is stored in the electric field rather than in the charge configuration? What does this perspective enable?"
  type: short-answer
  answer: "If energy were only a property of charge configurations, it would be impossible to account for energy transfer through empty space — there are no charges in the space between a distant transmitter and receiver. The field-energy perspective reveals that fields are real physical entities that carry energy independently. This generalizes to magnetic fields (u = ½μ₀⁻¹B²), to electromagnetic waves (which are propagating field energy described by the Poynting vector), and ultimately to quantum field theory, where all particles are excitations of fields. Starting from the capacitor, the field-energy view is the conceptual seed that grows into all of classical and quantum electromagnetism."
  explanation: "The factor ½ε₀E² is directly analogous to ½kx² for a spring — both represent the work done in building up the field (or displacement) against a restoring force. This analogy shows that field energy is not exotic; it follows the same pattern as mechanical potential energy stored in elastic systems. The leap is recognizing that space itself can be the 'spring.'"
```

## Explainer

When you push charges onto a capacitor against the repulsion of charges already there, you do work. Where does that energy go? Not into heat — there is no dissipation. It goes into the electric field itself. This is a conceptual leap worth dwelling on: **energy can be stored in a field**, not just in the configuration of particles. The field between the capacitor plates is a real physical entity that carries energy.

The energy density u = ½ε₀E² (in vacuum) tells you how much energy is packed into each cubic meter of space where the field has strength E. The factor of ½ appears for the same reason it does in spring potential energy ½kx² — both represent a linear restoring force integrated over displacement. For a parallel-plate capacitor with plate area A, separation d, and uniform field E = V/d, integrating the energy density over the volume between the plates gives U = ½ε₀E² · Ad = ½(ε₀A/d)V² = ½CV². You have rederived the capacitor energy formula from field energy — these are equivalent descriptions of the same stored energy.

The three equivalent forms U = ½CV² = ½QV = Q²/(2C) are useful in different situations. Use ½CV² when voltage is the given quantity (charging from a battery at fixed V). Use Q²/(2C) when charge is held fixed — for instance, calculating how the energy changes when you pull the plates apart while disconnected from any source. Use ½QV as a bridge when relating both. For dielectrics, the energy density becomes u = ½ε₀εᵣE², where εᵣ is the relative permittivity. A dielectric material amplifies how much energy is stored at a given field strength, which is why inserting a dielectric increases a capacitor's capacitance and stored energy at fixed voltage.

The field-energy perspective is more powerful than the circuit perspective because it generalizes. Magnetic fields carry energy density ½μ₀⁻¹B². Electromagnetic waves carry energy through empty space, described by the Poynting vector E⃗ × H⃗. The recognition that fields themselves carry energy — not merely the charges that create them — is foundational to all of classical electromagnetism and, eventually, to quantum field theory, where particle interactions are mediated by field quanta.
