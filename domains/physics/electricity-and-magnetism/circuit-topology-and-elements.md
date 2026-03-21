---
id: circuit-topology-and-elements
title: Circuit Topology and Basic Circuit Elements
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-current-and-resistance
  type: hard
- id: ohms-law
  type: hard
builds-toward:
- series-circuits-resistance-voltage
- parallel-circuits-conductance-current
tags:
- circuits
- network analysis
- components
stage: formal-systems
status: draft
---

# Circuit Topology and Basic Circuit Elements

## Core Idea
A circuit is a closed path for current flow containing sources and elements. Series connections have identical current; parallel connections have identical voltage. Ideal elements are characterized by simple voltage-current relationships: V = IR for resistors, Q = CV for capacitors, V = L(dI/dt) for inductors.

## Questions

```yaml
- question: "Three resistors are in a circuit. A student measures identical current flowing through each one. This tells you the resistors must be:"
  type: multiple-choice
  options:
    - "In parallel — all elements in parallel always share the same current"
    - "In series — there is only one path for current, so the same number of coulombs per second passes through each"
    - "In a mixed topology — equal current can occur in either configuration"
    - "Connected between two voltage sources that equalize current through each branch"
  answer: 1
  explanation: "In a series connection, there is exactly one path for charge to flow, so the same current must pass through every element. In a parallel connection, it is *voltage* — not current — that is identical across all branches. Current in parallel divides according to resistance. Option A reverses the defining property of each topology."

- question: "An inductor carries a steady 2 A of DC current. The voltage across it is measured to be zero. What does this tell you?"
  type: multiple-choice
  options:
    - "The inductor is broken — non-zero current must produce non-zero voltage"
    - "The current must be constant (DC steady state), since V = L(dI/dt) and dI/dt = 0 when current is unchanging"
    - "The inductor is behaving like a capacitor and storing charge"
    - "The circuit has no voltage source and no current should flow"
  answer: 1
  explanation: "An inductor's governing equation is V = L(dI/dt). Voltage appears across an inductor only when current is *changing*. Steady DC current means dI/dt = 0, so V = 0. An inductor in DC steady state looks like a short circuit (just a wire). This mirrors capacitor behavior in reverse: capacitors block DC (zero current in steady state); inductors pass DC (zero voltage in steady state)."

- question: "In a parallel circuit, the current through each branch is the same regardless of each branch's resistance."
  type: true-false
  answer: false
  explanation: "In parallel, *voltage* is identical across every branch — this is the defining feature. Current, however, divides: more current flows through lower-resistance branches (I = V/R). Only in a series circuit does each element carry the same current. Confusing which quantity is shared in each topology is the most common error in circuit analysis."

- question: "In a series circuit, adding more resistors in series increases the total resistance and reduces the current through every element in the loop."
  type: true-false
  answer: true
  explanation: "Series resistors add directly: R_total = R₁ + R₂ + R₃ + ... With a fixed source voltage, higher total resistance means lower current (I = V/R_total). Because current is identical everywhere in a series loop, this reduction affects every element. This is why Christmas lights wired in series all dim when you add more bulbs — total resistance rises and current falls through all."

- question: "A capacitor and a resistor are connected in series with a DC voltage source. After the circuit reaches steady state (voltage across the capacitor is constant), describe what happens to the current through the capacitor and explain why using i = C(dv/dt)."
  type: short-answer
  answer: "In DC steady state, the voltage across the capacitor stops changing (dv/dt = 0). Since i = C(dv/dt), the current becomes zero. The capacitor acts as an open circuit — it blocks DC in steady state. The resistor still has the full source voltage across it, but with zero current, no power is dissipated."
  explanation: "This is the key consequence of i = C(dv/dt): current flows only while voltage is changing. During charging, current flows as the capacitor voltage rises. Once the capacitor voltage equals the source voltage, no more current flows — the capacitor is 'full' and the circuit is in a stable, currentless steady state. This open-circuit behavior in DC is why capacitors are used to block DC while passing AC in signal processing."
```

## Explainer

From your study of Ohm's law and electric current, you know that current flows through a conducting path when a potential difference drives it, and that resistance quantifies how much a material opposes that flow. A **circuit** extends this idea into a network: instead of a single resistor, you have multiple components connected in a closed loop. The **topology** of that network — which elements connect to which — determines how current distributes and how voltages divide.

The two fundamental topologies are series and parallel. In a **series connection**, every element shares the same current — there is only one path for charge to flow, so the same number of coulombs per second must pass through each element. Voltages, however, add: the total voltage across the series chain equals the sum of individual drops. In a **parallel connection**, the situation inverts: every element shares the same voltage across its terminals, but current divides among the branches. Charge splits at the junction, with more flowing through lower-resistance paths. Recognizing which topology you are dealing with is the first step in any circuit analysis.

Beyond resistors, real circuits contain **capacitors** and **inductors** — components whose behavior depends on how voltages and currents change over time. A capacitor stores charge on two conducting plates separated by an insulator; the charge stored is proportional to the voltage across it: Q = CV, where C is the **capacitance** in farads. When voltage changes, the capacitor draws or supplies current to adjust its stored charge. An **inductor** — typically a coil of wire — stores energy in the magnetic field it creates when current flows. Its governing equation, V = L(dI/dt), tells you that a voltage appears across the inductor only when current is *changing*; it resists changes in current the same way a mass resists changes in velocity. Resistors, capacitors, and inductors are the three passive building blocks of virtually every circuit you will analyze.

The power of circuit topology is that it lets you apply a handful of rules — Ohm's law, Kirchhoff's voltage law (the sum of voltages around any closed loop is zero), and Kirchhoff's current law (the sum of currents into any junction is zero) — to predict behavior in arbitrarily complex networks. Whether analyzing a smartphone amplifier or a power grid, you are always identifying the topology first, labeling elements, then writing the governing equations. The series and parallel cases you study now are the building blocks that all network analysis reduces to.
