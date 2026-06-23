---
id: capacitance
title: Capacitance and Capacitors
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-potential
  type: hard
- id: conductors-in-electrostatics
  type: soft
- id: conductors-electrostatic-behavior
  type: soft
- id: potential-difference-voltage
  type: hard
builds-toward:
- dielectrics
- rc-circuits
- energy-stored-in-fields
tags:
- capacitance
- capacitors
- charge-storage
- parallel-plate
stage: formal-systems
status: validated
---

# Capacitance and Capacitors

## Core Idea
A capacitor is a device that stores electric charge and energy by maintaining a potential difference between two conductors. Capacitance C = Q/V measures how much charge is stored per unit voltage, with unit farads (F). For a parallel-plate capacitor with plate area A and separation d, C = ε₀A/d. Capacitors in series combine as 1/C_total = Σ(1/Cᵢ), and in parallel as C_total = ΣCᵢ.

## How It's Best Learned
Derive the parallel-plate formula from Gauss's law + potential difference integral. Then practice series/parallel combinations and energy storage U = ½CV² = Q²/(2C) = ½QV in varied circuit configurations.

## Common Misconceptions
- Capacitance depends only on geometry and material, not on the charge or voltage applied.
- Capacitors in series store less charge than any individual capacitor; in parallel, more.
- The energy is stored in the electric field between the plates, not in the charges themselves.

## Questions

```yaml
- question: "A parallel-plate capacitor is charged by a battery to 12V, then disconnected. The plate separation is then doubled. What happens to the capacitance?"
  type: multiple-choice
  options:
    - "Capacitance doubles because the electric field spreads over a larger region"
    - "Capacitance halves because C = ε₀A/d and d doubled"
    - "Capacitance stays the same because the voltage across the plates didn't change"
    - "Capacitance stays the same because the charge on the plates didn't change"
  answer: 1
  explanation: "Capacitance C = ε₀A/d depends only on geometry — plate area A, separation d, and permittivity ε₀. Doubling d halves C, regardless of charge or voltage. Options C and D reflect the common misconception that capacitance depends on operating conditions. It doesn't: C is a property of the physical geometry, like resistance is a property of a resistor's material and dimensions. After disconnecting from the battery, Q is fixed, but C still changes — meaning V must change to satisfy Q = CV."

- question: "Two identical capacitors, each with capacitance C, are connected in series. What is the total capacitance of the combination?"
  type: multiple-choice
  options:
    - "2C — the capacitances add together"
    - "C — series combination equals one capacitor"
    - "C/2 — series combination is smaller than either individual capacitor"
    - "4C — charge builds up across both gaps"
  answer: 2
  explanation: "Series capacitors combine as 1/C_total = 1/C₁ + 1/C₂. For two identical capacitors C: 1/C_total = 2/C, so C_total = C/2. Series combination is always smaller than the smallest individual capacitor. This surprises students who expect series to work like series resistors (which add). The physical reason: in series, the same charge Q sits on each capacitor, but the voltages add — you need more voltage per unit charge, which means less capacitance. Parallel is where capacitances add: C_parallel = C₁ + C₂."

- question: "The energy stored in a charged capacitor resides on the charged plates themselves."
  type: true-false
  answer: false
  explanation: "The energy is stored in the electric field between the plates, not on the charges. The energy density in an electric field is u = ½ε₀E², and integrating over the volume between the plates gives exactly U = ½CV². This is more than semantic: it anticipates a deeper principle in electrodynamics that fields are real physical entities carrying energy and momentum. The charges are the source of the field, but the energy belongs to the field."

- question: "Increasing the plate area of a parallel-plate capacitor while keeping the separation fixed will increase its capacitance."
  type: true-false
  answer: true
  explanation: "From C = ε₀A/d, capacitance is directly proportional to plate area A. Larger plates can accumulate more charge for the same voltage because a larger surface area holds more charge while maintaining the same surface charge density σ = Q/A. More facing area means more 'storage space' for charge without increasing the electric field strength, so more charge can be stored per volt applied."

- question: "Why does the formula C = ε₀A/d show that capacitance is a geometric property, and what does this mean for how capacitance changes when voltage is applied?"
  type: short-answer
  answer: "C = ε₀A/d contains only geometric quantities (plate area A, separation d) and a material constant (ε₀). Voltage and charge do not appear because capacitance is defined as the ratio C = Q/V — it is constant for a given capacitor regardless of how much charge you put on it or what voltage you apply. Changing the voltage changes Q proportionally so that Q/V stays fixed. Capacitance only changes if you physically alter the geometry: resize the plates, change the separation, or insert a dielectric material."
  explanation: "This geometric nature of capacitance is analogous to resistance being a property of a resistor's material and dimensions, not of the current flowing through it. Just as R = ρL/A doesn't contain current, C = ε₀A/d doesn't contain charge or voltage. This is why the common misconceptions — that capacitance depends on charge or voltage — are so fundamental: they confuse a fixed property of the device with the variable state of the circuit."
```

## Explainer

A **capacitor** is essentially a charge reservoir: it accepts charge on one conductor and induces an equal but opposite charge on the facing conductor, building up a potential difference between them. You already know from electric potential that moving charge against an electric field costs energy — that energy is what gets stored. The ratio C = Q/V, called **capacitance**, tells you how much charge you can store per volt of potential difference. A large capacitance means the geometry is favorable for accumulating charge without requiring a large voltage.

The parallel-plate capacitor is the cleanest geometry to analyze. You know from Gauss's law that a uniformly charged plate produces a uniform field E = σ/ε₀ between the plates (where σ = Q/A is surface charge density). The voltage across the gap is just V = Ed = σd/ε₀. Plugging Q = σA back in gives C = Q/V = ε₀A/d. This result captures the geometry intuitively: a larger plate area stores more charge for the same field, increasing C; a larger gap requires a larger voltage for the same field, decreasing C. Everything about capacitor geometry follows this pattern — larger facing area and smaller separation always increase capacitance.

When capacitors are combined in circuits, the combination rules follow directly from how charge and voltage behave. In **series**, the same charge Q sits on each capacitor (charge has nowhere else to go), but the voltages add: V_total = Q/C₁ + Q/C₂ = Q(1/C₁ + 1/C₂). So 1/C_series = Σ(1/Cᵢ) — series combination is always smaller than any individual capacitor. In **parallel**, both capacitors see the same voltage V, so their charges add: Q_total = C₁V + C₂V = (C₁ + C₂)V. Thus C_parallel = ΣCᵢ — parallel combination just pools the storage capacity.

The energy stored in a capacitor takes three equivalent forms: U = ½CV² = Q²/2C = ½QV. But the most physically revealing form comes from asking where the energy lives. The energy density in an electric field is u = ½ε₀E². Integrating this over the volume between the plates (volume = Ad) gives exactly U = ½CV² — the energy is distributed throughout the field, not sitting on the charges. This is a preview of a deeper principle: in electrodynamics, fields are real physical entities that carry energy, momentum, and more.
