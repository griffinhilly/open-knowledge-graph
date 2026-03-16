---
id: node-voltage-systematic-solution
title: Nodal Analysis Method
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-laws-kvl-and-kcl
  type: hard
- id: ohms-law-and-conductance
  type: hard
builds-toward:
- circuit-theorems-linearity
tags:
- nodal-analysis
- node-voltage
- systematic-method
stage: formal-systems
status: draft
---

# Nodal Analysis Method

## Core Idea
Nodal analysis solves circuits by applying KCL at each node and expressing currents via Ohm's law in terms of node voltages. One node is chosen as ground reference, and the resulting system of linear equations yields all node voltages. This method is efficient for circuits with many voltage sources and few independent loops.

## Explainer

You already know KCL: the sum of currents flowing into any node equals the sum flowing out. Nodal analysis turns this into a systematic algorithm by expressing every branch current in terms of **node voltages** — the voltages at each node measured with respect to a chosen **ground (reference) node**. The ground node has voltage V = 0 by definition. Every other node has an unknown voltage V₁, V₂, …, Vₙ to be found. Once you know all node voltages, every branch voltage is a difference of node voltages (V_AB = V_A − V_B), and every branch current through a resistor follows from Ohm's law: I = (V_A − V_B) / R.

The procedure is mechanical. First, identify all nodes and pick one as ground — typically the node with the most connections, or one that simplifies the algebra. Second, for each non-reference node, write a KCL equation: sum of currents leaving that node = 0. For each resistor connecting node i to node j, the current leaving node i is (Vᵢ − Vⱼ) / R. For a current source delivering current into node i, that source contributes a known term. Third, collect the equations — there will be exactly as many equations as unknown node voltages — and solve the linear system. The result is every node voltage in the circuit.

Consider a simple example: two resistors R₁ and R₂ in a circuit with a voltage source V_s and a current source I_s. If you label the top node V₁ and the ground at the bottom, KCL at V₁ might read: (V₁ − V_s) / R₁ + V₁ / R₂ − I_s = 0. Rearranging groups all V₁ terms on one side and known quantities on the other, giving a one-equation, one-unknown system. With more nodes, the system grows but the structure is the same: each equation is linear in the node voltages, so standard linear algebra solves it.

**Supernodes** arise when a voltage source connects two non-reference nodes. You can't write KCL at either node independently because the current through an ideal voltage source is unknown. The technique is to enclose both nodes in a "supernode" boundary, write KCL for the combined region (treating the interior sources as transparent), and add the voltage source's constraint equation (V_A − V_B = V_source) as an additional equation. The count of unknowns and equations stays equal. Nodal analysis with supernodes handles any linear circuit, and in AC analysis the same procedure applies with complex impedances replacing resistances — the only difference is that V and I become phasors and R becomes Z.
