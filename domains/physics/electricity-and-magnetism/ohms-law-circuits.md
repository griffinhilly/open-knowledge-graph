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

## Questions

```yaml
- question: "A set of light bulbs is wired in parallel across a 12V battery. You want to calculate the power dissipated by one bulb with resistance 60Ω. Which formula is most natural to apply, and why?"
  type: multiple-choice
  options:
    - "P = I²R, because current is always the most fundamental quantity in a circuit"
    - "P = V²/R, because all parallel elements share the same voltage"
    - "P = IV, but you must first use Ohm's law to find both I and V independently"
    - "P = I²R, because the same current flows through all parallel elements"
  answer: 1
  explanation: "In a parallel circuit, all branches share the same voltage (12V here). P = V²/R uses the known voltage directly: P = (12)²/60 = 2.4W. Option D describes a series circuit, not parallel — in a parallel circuit, each branch draws its own current according to its own resistance. P = I²R is more natural in series circuits, where the same current flows through every element."

- question: "A diode allows current to flow easily in one direction but blocks it in the other. Which statement correctly describes a diode in the context of Ohm's law?"
  type: multiple-choice
  options:
    - "A diode obeys Ohm's law but with a very small resistance in one direction and very large in the other"
    - "A diode is a non-ohmic element — its V-I relationship is not linear, so V = IR does not apply with a fixed constant R"
    - "A diode obeys Ohm's law at all voltages as long as you use the correct R for each direction"
    - "Ohm's law is universal and must apply to diodes just as to resistors"
  answer: 1
  explanation: "A diode is a non-ohmic element: its resistance is not a fixed constant but depends on voltage and current direction. The V-I relationship is exponential, not linear. Ohm's law V = IR only holds for ohmic materials where R is constant. Describing the diode's forward and reverse resistance as 'small' and 'large' (option A) approximates the non-linearity but misrepresents what Ohm's law means — R must be constant for the law to apply."

- question: "Ohm's law (V = IR) is a fundamental law of physics that holds for all materials under all conditions."
  type: true-false
  answer: false
  explanation: "Ohm's law is an empirical approximation that holds for ohmic materials over a useful range of conditions. It breaks down for semiconductors (diodes, transistors), for materials at extreme temperatures, and for non-linear elements. It is not derived from first principles but observed — the Drude model provides a physical explanation for why it holds in metals, not a proof that it holds universally. Many important circuit elements are deliberately non-ohmic."

- question: "In a series circuit, P = I²R is more natural than P = V²/R because the same current flows through every element."
  type: true-false
  answer: true
  explanation: "In a series circuit, the same current I flows through all elements, while voltage divides across them. When I is the known quantity, P = I²R directly gives power for each element without needing to find individual voltages. Conversely, in a parallel circuit where all elements share the same voltage, P = V²/R is more natural. Both formulas are algebraically equivalent for any ohmic resistor — the choice is about which variable is most directly available."

- question: "P = I²R and P = V²/R look like different formulas. Why are they actually the same formula, and when would you prefer one over the other?"
  type: short-answer
  answer: "Both are derived from P = IV combined with Ohm's law V = IR. Substituting V = IR into P = IV gives P = I²R. Substituting I = V/R gives P = V²/R. They encode the same physics — energy dissipation per unit time in an ohmic resistor — just with different variables expressed. Use P = I²R when current is the known quantity (series circuits). Use P = V²/R when voltage is known (parallel circuits, where all branches share the same V)."
  explanation: "The key insight is that these are not independent formulas — they are the same underlying relationship with Ohm's law substituted in different directions. Choosing between them is a matter of which quantity you already know, not which is more correct."
```

## Explainer

You already know from resistance and resistivity that a material's resistance comes from its geometry and microscopic properties: R = ρL/A, where ρ is resistivity, L is length, and A is cross-sectional area. **Ohm's law**, V = IR, connects this material property to circuit behavior. It says that if you apply a voltage V across a resistor, a current I = V/R flows through it. Equivalently, if a current I flows, it requires a voltage V = IR to drive it. The relationship is linear: double the voltage, double the current. This linearity is what makes Ohm's law so useful — and also what makes it a *special case* that only holds for ohmic materials.

The circuit element picture simplifies analysis enormously. An **ideal wire** has R = 0, meaning any current flows through it with zero voltage drop — it's a perfect conductor that connects two points at identical potential. An **ideal insulator** has R → ∞, meaning no current flows regardless of voltage — it's an open circuit. Real resistors fall between these extremes, and the V = IR relationship lets you predict exactly how much current flows for any applied voltage. The power dissipated is P = IV = I²R = V²/R, which you can derive by combining P = IV with V = IR.

Ohm's law is not a fundamental law of physics — it's an empirical approximation that holds for many materials over wide ranges. It breaks down for semiconductors (where resistance depends on current direction in diodes), for non-linear elements like transistors, and at extreme temperatures where resistance changes dramatically. The deeper foundation is the Drude model: free electrons in a metal accelerate under an electric field but scatter frequently off lattice ions, reaching a terminal drift velocity proportional to E. This gives J = σE (current density proportional to field), which in macroscopic terms is V = IR.

The power formulas P = I²R and P = V²/R are the two most commonly used in circuit design. P = I²R is natural when current is the known quantity (a series circuit forces the same I through every element). P = V²/R is natural when voltage is known (parallel elements share the same V). Both are correct for any ohmic resistor — they're the same formula in different variables, related by V = IR. The energy delivered to a resistor per unit time becomes heat, which is Joule heating — the same physics expressed as a circuit relationship.
