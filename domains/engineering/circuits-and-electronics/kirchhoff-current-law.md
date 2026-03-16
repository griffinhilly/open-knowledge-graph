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
status: draft
---

# Kirchhoff's Current Law (KCL)

## Core Idea
Kirchhoff's Current Law states that the sum of currents entering a node equals the sum of currents leaving the node. Based on charge conservation, this principle is essential for analyzing circuits with multiple branches. KCL is the foundation for nodal analysis, a systematic method for finding voltages in complex circuits.

## Explainer

From your study of circuit variables and elements, you understand that current is the flow of electric charge through a conductor. Kirchhoff's Current Law (KCL) is the direct consequence of a simple physical fact: charge cannot accumulate at a node in a steady-state circuit. A **node** is any point in a circuit where two or more wires connect. If more charge flowed in than out, charge would pile up at that junction — which doesn't happen in normal circuit operation. Therefore, whatever flows in must flow out.

Written mathematically, KCL says that the algebraic sum of all currents at a node equals zero: Σ I = 0. The sign convention is yours to choose — you might define currents entering the node as positive and leaving as negative, or vice versa — but you must be consistent. With three branches meeting at a node carrying currents I1, I2, and I3, if I1 flows in and I2 and I3 flow out, then I1 = I2 + I3. This is the water-pipe analogy made rigorous: whatever flow enters a junction must leave through the other pipes.

The power of KCL becomes apparent when you apply it systematically to find unknown currents. In a circuit with multiple loops and branches, directly tracking where current goes by inspection quickly becomes confusing. KCL turns the tracking problem into algebra. Label each branch current with a variable and a reference direction (the arrow can point anywhere — if the current flows opposite to your arrow, the solution will give a negative number, which is perfectly valid). Write a KCL equation at each node: sum of currents in = sum of currents out. Each equation is one constraint on the unknowns.

KCL alone gives you current-balance equations, but not enough to solve for everything. Ohm's law provides the additional relationship between current and voltage within each resistor. This is why KCL and KVL (Kirchhoff's Voltage Law) work together as a system: KCL governs what happens at nodes, KVL governs what happens around loops, and Ohm's law links the two. The nodal analysis method you will encounter next is essentially the disciplined application of KCL at every node in the circuit, using Ohm's law to express branch currents in terms of node voltages, until you have a solvable system of equations.
