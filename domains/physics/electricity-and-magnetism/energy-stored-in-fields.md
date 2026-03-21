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

## Questions

```yaml
- question: "According to the electric energy density formula u_E = ½ε₀E², what happens to the energy stored in a region of electric field if the field strength is doubled?"
  type: multiple-choice
  options:
    - "The stored energy doubles, because energy is proportional to field strength"
    - "The stored energy increases by a factor of 4, because energy is proportional to E²"
    - "The stored energy increases by a factor of √2, because energy density is the square root of field strength"
    - "The stored energy is unchanged if the volume of the field region does not change"
  answer: 1
  explanation: "Energy density is u_E = ½ε₀E², so it scales as the square of the field. Doubling E replaces E² with (2E)² = 4E², quadrupling the energy density — and therefore the total stored energy in any fixed volume. This nonlinearity has practical consequences: a capacitor charged to twice the voltage stores four times the energy, not twice. The quadratic dependence on field strength (or voltage) is a fundamental feature of field energy, not a curiosity."

- question: "Where is the energy stored in a charged parallel-plate capacitor?"
  type: multiple-choice
  options:
    - "In the electric charges on the surface of the plates"
    - "In the electric potential difference measured across the terminals"
    - "In the electric field distributed throughout the volume between the plates"
    - "Equally split between the conductor material of the plates and the space between them"
  answer: 2
  explanation: "The deep insight is that the field itself is a physical entity that stores energy. The energy is not 'in the charges' or 'at the terminals' — it is spread throughout the space where the field exists. This is made concrete by the derivation: U = ½CV² = ½ε₀E² × (volume between the plates). The quantity (volume) × (energy density) gives the total energy, and the energy density ½ε₀E² is uniform between ideal parallel plates. This distinction matters for electromagnetic waves: a wave propagates through space carrying energy in its oscillating fields, with no charges present at all."

- question: "Doubling the electric field strength in a region doubles the electric energy stored in that region."
  type: true-false
  answer: false
  explanation: "The electric energy density is u_E = ½ε₀E², which is proportional to E squared, not E. Doubling E quadruples u_E (and therefore the total stored energy in that volume). This is the same nonlinearity that makes capacitors store four times the energy at twice the voltage. A student who memorizes 'energy is related to the field' but misses the squared dependence will consistently underestimate how rapidly field energy grows."

- question: "In an electromagnetic wave propagating through vacuum, the electric and magnetic fields carry equal energy densities at every point."
  type: true-false
  answer: true
  explanation: "In a plane wave in vacuum, u_E = ½ε₀E² and u_B = B²/(2μ₀) are equal at every point and moment. This is not a coincidence — it follows from the relationship between E and B in a wave (E = cB, with c = 1/√(ε₀μ₀)) and the symmetry of Maxwell's equations. The total energy flux (Poynting vector) is carried equally by both field components. This result makes sense conceptually: neither field can sustain itself without the other, so they contribute equally to the wave's energy."

- question: "Why is it physically meaningful to say that energy is 'stored in the electromagnetic field' rather than 'stored in the capacitor plates' or 'stored in the circuit'? What conceptual work does this distinction do?"
  type: short-answer
  answer: "Saying energy resides in the field rather than the plates or wires means that the field is a physical entity in its own right — one that can carry energy through space even in the absence of charges or conductors. This becomes essential for electromagnetic waves: a radio wave propagates through empty space and delivers energy to a distant antenna, with no physical connection between transmitter and receiver. If energy were stored only in charges or conductors, this would be impossible to explain. The field-energy formulation allows you to calculate how much energy a wave carries using u_E and u_B integrated over the wave's volume."
  explanation: "This distinction is also the conceptual bridge to the Poynting vector and the full theory of electromagnetic radiation. It represents a shift from 'action at a distance' thinking (charges reach out and affect other charges) to field thinking (charges create fields, fields carry energy and momentum, fields interact with other charges). The field becomes the primary physical reality, not just a bookkeeping device."
```

## Explainer

From your study of capacitors, you know that charging a capacitor requires work — you must push charge onto the plate against the growing electric field. That work has to go somewhere: it goes into the electric field itself. From inductors, you know that building up current through an inductor requires work against the back-EMF the inductor generates. That work goes into the magnetic field. The deep insight here is that **the field is a physical entity that stores energy**, not just a mathematical shorthand for forces between charges.

To find how much energy is stored, derive the **electric energy density** from what you already know. For a parallel-plate capacitor: U = ½CV², and with C = ε₀A/d and E = V/d, substituting gives U = ½ε₀E² × (Ad). The quantity Ad is just the volume between the plates, so the energy per unit volume is u_E = ½ε₀E². The energy isn't locked in the plates — it's spread uniformly through the field-filled volume between them. Perform the analogous derivation for a solenoid: U = ½LI², with L = μ₀n²Al and B = μ₀nI, and you get u_B = B²/(2μ₀) for the magnetic energy density. Same structure, same logic.

These two expressions have an elegant symmetry. Both are proportional to the square of the field — doubling E quadruples u_E, not just doubles it. This nonlinearity matters: a capacitor storing twice the voltage stores four times the energy. The constant out front, ε₀ for electric and 1/μ₀ for magnetic, encodes how "easy" it is for each field type to store energy in vacuum. Note also that you can compute total stored energy by integrating these densities over all space — you don't need to know anything about the charge or current distribution, only the field distribution.

Why does this matter beyond capacitors and inductors? Because electromagnetic waves consist of oscillating electric and magnetic fields propagating through space — and those fields carry energy with them, calculated using exactly these formulas. In a plane wave in vacuum, u_E = u_B at every point: the electric and magnetic fields store equal energy densities, which travel together at speed c. The Poynting vector (energy flux) follows directly from these density expressions. Every time you ask "how much energy is in this electromagnetic field?" — whether it's sunlight, a radio wave, or the field of a charged particle — you are computing an integral of u_E and u_B over the relevant volume.
