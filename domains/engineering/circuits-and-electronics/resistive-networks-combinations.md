---
id: resistive-networks-combinations
title: Series, Parallel, and Combined Resistor Networks
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: ohms-law-and-conductance
  type: hard
- id: ideal-voltage-and-current-sources
  type: hard
builds-toward:
- voltage-divider-and-attenuation
- current-divider-and-distribution
tags:
- resistor-networks
- series
- parallel
- combinations
- simplification
stage: formal-systems
status: draft
---

# Series, Parallel, and Combined Resistor Networks

## Core Idea
Series resistors have identical current and R_total = R₁ + R₂ + ... Parallel resistors have identical voltage and 1/R_total = 1/R₁ + 1/R₂ + ... or G_total = G₁ + G₂ + ... Combinations can be analyzed recursively and are foundational for network simplification before detailed analysis.

## Questions

```yaml
- question: "Two resistors R₁ = 6 Ω and R₂ = 3 Ω are connected in parallel across a 12 V source. A third resistor R₃ = 4 Ω is then added in series with this parallel combination. What is the total resistance of the circuit?"
  type: multiple-choice
  options:
    - "13 Ω"
    - "6 Ω"
    - "2 Ω"
    - "4 Ω"
  answer: 1
  explanation: "First reduce the parallel combination: 1/R_parallel = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2, so R_parallel = 2 Ω. Then add the series resistor: R_total = 2 + 4 = 6 Ω. The recursive strategy — simplify sub-networks, then combine — is the key technique. Option A (13 Ω) comes from incorrectly adding all three resistances directly."

- question: "In a purely series circuit, if one resistor has a much larger resistance than the others, which of the following is true?"
  type: multiple-choice
  options:
    - "The large resistor carries more current than the smaller ones"
    - "The large resistor drops more voltage than the smaller ones"
    - "The large resistor has less power dissipated through it than the smaller ones"
    - "The large resistor reduces the current through the smaller ones"
  answer: 1
  explanation: "In series, all resistors carry the same current I. Each resistor drops voltage V = IR, so the largest R drops the most voltage. Option A is the most common misconception — students sometimes think a resistor 'uses up' more current. Current is not consumed; it is the same throughout a series loop (Kirchhoff's current law). The large resistor does dissipate more power (P = I²R), not less, contradicting option C."

- question: "Adding more resistors in parallel to an existing parallel combination always decreases the total resistance of the network."
  type: true-false
  answer: true
  explanation: "Each additional parallel branch adds a new path for current to flow, increasing total conductance G_total = G₁ + G₂ + .... Since R_total = 1/G_total, higher conductance means lower resistance. Even adding a very large resistor (very small conductance) still adds a positive amount to G_total, so R_total strictly decreases. This is the physical intuition: more lanes on a highway means less overall congestion."

- question: "In a series circuit with three resistors of different values, the resistor with the highest resistance carries more current than the others."
  type: true-false
  answer: false
  explanation: "In a series connection, there is only one path for current — all electrons must pass through each resistor in sequence. Kirchhoff's current law requires the same current to flow through every element. The resistors differ in how much voltage they drop (V = IR), not in how much current they carry. A student who thinks current 'gets used up' or 'distributed' will get this wrong."

- question: "Explain physically why the equivalent resistance formula differs between series and parallel: R_total = R₁ + R₂ + ... for series, but 1/R_total = 1/R₁ + 1/R₂ + ... for parallel."
  type: short-answer
  answer: "In series, resistors share the same current and their voltage drops add (Kirchhoff's voltage law), giving R_total = V_total/I = (V₁ + V₂ + ...)/I = R₁ + R₂ + .... In parallel, resistors share the same voltage and their currents add (Kirchhoff's current law), giving G_total = I_total/V = (I₁ + I₂ + ...)/V = G₁ + G₂ + ..., so conductances add and resistances combine as reciprocals."
  explanation: "The formulas aren't arbitrary — each follows directly from which quantity is shared (current in series, voltage in parallel) and which adds. Conductance is the natural quantity for parallel resistors because it measures how much current each branch passes per unit voltage. Recognizing which KVL/KCL applies is the physical key to the algebra."
```

## Explainer

From Ohm's law, you know that voltage, current, and resistance are related by V = IR for a single resistor. When multiple resistors are connected together, the same law still governs each element — the question is just how current and voltage distribute across the network. Two fundamental configurations answer this, and understanding each one physically before doing the algebra makes the formulas stick.

In a **series** connection, the resistors are strung end-to-end so that every electron must pass through each one in turn. There is only one path for current, so all resistors carry the same current I. Each resistor drops a portion of the total voltage according to its own Ohm's law: V₁ = IR₁, V₂ = IR₂, and so on. By Kirchhoff's voltage law, these voltage drops must sum to the source voltage: V = I(R₁ + R₂ + ...). The equivalent resistance is the sum: **R_total = R₁ + R₂ + ...**. Physically, series resistors are like adding more obstacles to a single road — each one impedes the same flow, and the total impedance accumulates.

In a **parallel** connection, resistors share the same two nodes, so the voltage across each is identical. Current from the source can split and take any of the parallel branches. By Kirchhoff's current law, the total current is the sum of branch currents: I = V/R₁ + V/R₂ + ... = V(1/R₁ + 1/R₂ + ...). The equivalent conductance adds directly — **G_total = G₁ + G₂ + ...** — and the equivalent resistance is the reciprocal of that sum. Parallel resistors are like adding more lanes to a highway: each new path reduces the overall resistance by providing an easier route for current.

Real networks mix both configurations. The strategy is to identify sub-networks that are purely series or purely parallel, replace them with their equivalent single resistor, and repeat until the entire network collapses to a single element. This recursive simplification only works when the network is a **ladder** (series-parallel reducible); some networks (like a bridge or Wheatstone circuit) cannot be reduced this way and require Kirchhoff's laws directly. For the reducible cases, however, this technique is the fastest path to finding total current, source power, and individual element voltages or currents — and it is the foundation for understanding voltage dividers and current dividers, which are the standard building blocks of electronic signal conditioning.
