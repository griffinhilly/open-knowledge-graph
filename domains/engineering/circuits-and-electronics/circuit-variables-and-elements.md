---
id: circuit-variables-and-elements
title: Circuit Variables and Ideal Circuit Elements
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: ohms-law
  type: hard
- id: electric-current-and-resistance
  type: hard
- id: electric-power
  type: soft
- id: capacitance
  type: soft
- id: inductance-and-inductors
  type: soft
builds-toward:
- node-voltage-method
- mesh-current-method
- capacitor-inductor-energy-storage
- phasor-representation
tags:
- circuit-elements
- voltage
- current
- power
- passive-sign-convention
stage: formal-systems
status: validated
---

# Circuit Variables and Ideal Circuit Elements

## Core Idea
Circuit analysis begins with precise definitions of voltage, current, power, and energy as circuit variables. Ideal circuit elements—resistors, capacitors, inductors, and independent or dependent sources—are mathematical models that approximate real component behavior. The passive sign convention establishes a consistent framework for assigning reference polarities and current directions. Power absorbed by an element equals voltage times current under the passive sign convention; energy is power integrated over time.

## How It's Best Learned
Practice assigning reference directions and applying the passive sign convention to multi-element circuits before writing any equations. Work through examples involving both independent and dependent sources, tracking polarity carefully. Draw complete circuit diagrams with all labeled variables as a habit.

## Common Misconceptions
- Confusing the reference direction (a mathematical choice) with the actual physical direction of current flow — they can differ.
- Assuming a voltage source fixes the current through it or a current source fixes the voltage across it — the other variable is determined by the circuit.
- Conflating power delivered by a source with power absorbed by a load; the sign convention distinguishes them.

## Questions

```yaml
- question: "Under the passive sign convention, an element has voltage V = 5 V across it and current I = -2 A entering the positive terminal. What is the power absorbed by the element?"
  type: multiple-choice
  options: ["-10 W", "10 W", "-2.5 W", "2.5 W"]
  answer: 0
  explanation: "Under the passive sign convention, P = V × I where I is defined as entering the positive terminal. P = (5)(−2) = −10 W. A negative absorbed power means the element is actually delivering 10 W to the circuit — it is a source, not a load."

- question: "An ideal voltage source generally determines both the voltage across it and the current through it."
  type: true-false
  answer: false
  explanation: "An ideal voltage source fixes the voltage across its terminals, but the current through it is determined by the rest of the circuit. Dually, an ideal current source fixes the current but the voltage across it is set by the surrounding network."

- question: "What is the purpose of assigning a reference direction (or reference polarity) to a circuit variable, and does it have to match the actual physical direction?"
  type: short-answer
  answer: "A reference direction is a mathematical convention chosen before writing equations; it gives a sign to the variable. The actual physical direction need not match — if the computed value comes out negative, it simply means the physical quantity flows opposite to the chosen reference."
  explanation: "Picking a reference direction is like choosing a positive x-axis: the axis itself is arbitrary, but once chosen it makes equations unambiguous. A negative result is meaningful information, not an error; it tells you the quantity opposes the reference you assumed."
```

## Explainer

Circuit analysis is built on three circuit variables — voltage, current, and power — and a set of idealized component models. Before you can write a single equation, you need to understand what these variables mean and how to keep their signs straight.

**Voltage** is the potential difference between two nodes — the energy per unit charge that a charge carrier gains or loses moving between them. **Current** is the rate at which charge flows past a cross-section, measured in amperes. These two quantities are independent: knowing the voltage across a resistor tells you the current (via Ohm's Law), but knowing the voltage across a capacitor tells you only the *rate of change* of current, not the current itself.

The **passive sign convention** is the bookkeeping rule that makes multi-element circuits tractable. For any element, you define a positive current direction and a positive voltage polarity together: current enters the terminal marked +. Then power absorbed equals P = V × I. If P comes out positive, the element is absorbing power (load behavior). If P is negative, the element is delivering power (source behavior). This single convention applies to every element — resistors, capacitors, inductors, and sources alike — eliminating the need for separate sign rules for each type.

Ideal circuit elements are mathematical abstractions. A resistor satisfies v = iR for all time and cannot store energy. A capacitor satisfies i = C dv/dt and stores energy in its electric field. An inductor satisfies v = L di/dt and stores energy in its magnetic field. **Independent sources** impose a fixed voltage or current regardless of what the rest of the circuit does. **Dependent sources** (controlled sources) impose a voltage or current proportional to some other circuit variable, and they appear in transistor models and op-amp circuits. A key point students miss: a voltage source fixes voltage but not current; a current source fixes current but not voltage. The unconstrained variable is determined entirely by the surrounding network.

Getting these fundamentals right — particularly the passive sign convention and the distinction between reference direction and actual direction — is what makes Kirchhoff's Voltage Law and Kirchhoff's Current Law work cleanly. Every node-voltage or mesh-current analysis you do later depends on applying these conventions consistently.
