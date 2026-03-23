---
id: kirchhoff-current-law
title: Kirchhoff's Current Law (KCL)
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-variables-and-elements
  type: hard
builds-toward:
- current-divider-circuit
- series-parallel-resistor-analysis
- dc-analysis-steady-state
- node-voltage-method
tags:
- kirchhoff-laws
- circuit-analysis
- fundamental
stage: formal-systems
status: validated
---

# Kirchhoff's Current Law (KCL)

## Core Idea
Kirchhoff's Current Law states that the sum of currents entering a node equals the sum of currents leaving the node. Based on charge conservation, this principle is essential for analyzing circuits with multiple branches. KCL is the foundation for nodal analysis, a systematic method for finding voltages in complex circuits.

## Questions

```yaml
- question: "Three branches meet at a node. I₁ = 4 A flows into the node and I₂ = 7 A flows into the node. I₃ is defined as flowing out of the node. What is I₃?"
  type: multiple-choice
  options:
    - "3 A (I₂ − I₁)"
    - "−11 A (indicating current flows inward)"
    - "11 A (I₁ + I₂ must leave)"
    - "It cannot be determined without knowing the resistances"
  answer: 2
  explanation: "KCL states that current entering a node equals current leaving it. I₁ + I₂ = 4 + 7 = 11 A enters, so 11 A must leave through I₃. Option D is wrong because KCL is independent of resistances — it's a conservation law, not Ohm's law. Option B would be correct if I₃ were defined as entering (the solution being negative would mean it actually exits), but since I₃ is defined as leaving, the answer is simply +11 A."

- question: "Which physical principle directly underlies KCL?"
  type: multiple-choice
  options:
    - "Conservation of energy — total power delivered to a node must equal zero"
    - "Conservation of charge — charge cannot accumulate at a node in steady state"
    - "Ohm's law — current at a node is proportional to the local voltage"
    - "Conservation of momentum — the net force on charge carriers at a junction is zero"
  answer: 1
  explanation: "KCL is a direct consequence of charge conservation. In steady-state circuit operation, charge cannot pile up at a node — every coulomb that flows in must flow out. This is entirely independent of what circuit elements are present. Ohm's law (option C) relates current to voltage within a resistor; it's a material property, not a conservation law, and is not what KCL expresses."

- question: "If you assign a reference direction to a branch current and the circuit solution yields a negative value for that current, the result is invalid and you must re-assign the direction."
  type: true-false
  answer: false
  explanation: "A negative value is perfectly valid — it simply means the actual current flows opposite to your chosen reference direction. This is one of the strengths of KCL-based analysis: you can assign reference directions arbitrarily, write the equations, solve, and let the algebra determine the true direction. Requiring re-assignment would destroy the systematic algebraic approach and is not necessary."

- question: "In a circuit, a resistor 'uses up' some of the current flowing through it, so the current exiting a resistor is less than the current entering it."
  type: true-false
  answer: false
  explanation: "This is one of the most persistent misconceptions in introductory circuits. Resistors do not consume current — they convert electrical energy into heat, but the same current that enters a resistor exits it. What the resistor does consume is voltage (electrical potential energy). KCL guarantees that current is conserved at every node, including both terminals of a resistor. A light bulb glowing brightly has the same current flowing in and out; it's the voltage drop (and thus power P = IV) that represents energy dissipation."

- question: "Explain why the sum of all currents at a node must equal zero, using the concept of charge conservation."
  type: short-answer
  answer: "A node is a connection point with no capacity to store charge. If more charge flowed in than out over any time interval, charge would accumulate at the node — but this doesn't happen in steady-state operation. Since charge is conserved and cannot pile up, the rate of charge flowing in must equal the rate flowing out. Current is defined as charge per unit time (I = dq/dt), so equal charge flow rates mean equal currents. Expressing this with a sign convention (positive for entering, negative for leaving), the algebraic sum of all branch currents at any node equals zero."
  explanation: "The argument generalizes beyond steady state through charge neutrality: in normal circuit conductors, charge accumulation would build up an electric field that opposes further accumulation, making the transient extremely short-lived. KCL is therefore an excellent approximation for any circuit analysis at frequencies well below those where capacitive effects at wire junctions matter."
```

## Explainer

From your study of circuit variables and elements, you understand that current is the flow of electric charge through a conductor. Kirchhoff's Current Law (KCL) is the direct consequence of a simple physical fact: charge cannot accumulate at a node in a steady-state circuit. A **node** is any point in a circuit where two or more wires connect. If more charge flowed in than out, charge would pile up at that junction — which doesn't happen in normal circuit operation. Therefore, whatever flows in must flow out.

Written mathematically, KCL says that the algebraic sum of all currents at a node equals zero: Σ I = 0. The sign convention is yours to choose — you might define currents entering the node as positive and leaving as negative, or vice versa — but you must be consistent. With three branches meeting at a node carrying currents I1, I2, and I3, if I1 flows in and I2 and I3 flow out, then I1 = I2 + I3. This is the water-pipe analogy made rigorous: whatever flow enters a junction must leave through the other pipes.

The power of KCL becomes apparent when you apply it systematically to find unknown currents. In a circuit with multiple loops and branches, directly tracking where current goes by inspection quickly becomes confusing. KCL turns the tracking problem into algebra. Label each branch current with a variable and a reference direction (the arrow can point anywhere — if the current flows opposite to your arrow, the solution will give a negative number, which is perfectly valid). Write a KCL equation at each node: sum of currents in = sum of currents out. Each equation is one constraint on the unknowns.

KCL alone gives you current-balance equations, but not enough to solve for everything. Ohm's law provides the additional relationship between current and voltage within each resistor. This is why KCL and KVL (Kirchhoff's Voltage Law) work together as a system: KCL governs what happens at nodes, KVL governs what happens around loops, and Ohm's law links the two. The nodal analysis method you will encounter next is essentially the disciplined application of KCL at every node in the circuit, using Ohm's law to express branch currents in terms of node voltages, until you have a solvable system of equations.
