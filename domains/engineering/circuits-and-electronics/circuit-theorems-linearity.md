---
id: circuit-theorems-linearity
title: Linearity, Superposition, and Scaling
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: node-voltage-systematic-solution
  type: soft
- id: mesh-current-systematic-solution
  type: soft
- id: ohms-law-and-conductance
  type: hard
builds-toward:
- thevenin-circuit-equivalent
- norton-circuit-equivalent
tags:
- linearity
- superposition
- homogeneity
- additivity
stage: formal-systems
status: draft
---

# Linearity, Superposition, and Scaling

## Core Idea
Linear circuits satisfy superposition: response to multiple sources equals the sum of individual responses. Linearity requires homogeneity (scaling input scales output) and additivity (sum of inputs produces sum of outputs). These properties hold for circuits with R, L, C, and independent sources, enabling efficient analysis and design techniques.

## Explainer

From Ohm's law, you already know a fundamental fact: the voltage across a resistor is proportional to the current through it, V = IR. That proportionality is the seed of everything in this topic. A circuit made of resistors, capacitors, and inductors is a **linear** system — meaning the relationship between any input (source) and any output (current or voltage anywhere) is proportional and can be broken apart. This linearity is what makes circuit analysis tractable.

Linearity has two components. **Homogeneity** (also called scaling) means that if you double every source in a circuit, every voltage and current response doubles as well. **Additivity** means that if circuit A has sources S1 and circuit B has sources S2, then the combined circuit with both S1 and S2 produces the sum of the two responses. Together, these define the **superposition principle**: the response due to multiple independent sources equals the algebraic sum of the responses due to each source acting alone.

To apply superposition, you "turn off" all sources except one — replacing voltage sources with short circuits (wires) and current sources with open circuits (gaps) — and calculate the response due to that single source. You repeat for every source, then add all partial responses. This can seem like more work than solving the full circuit directly, but the power comes when individual sub-circuits are simpler to analyze than the combined system, or when you want to understand each source's separate contribution. Node-voltage and mesh-current methods solve everything simultaneously; superposition solves things piecewise.

A critical limitation: superposition applies only to **linear** responses — currents and voltages. **Power** is not linear (P = I²R involves a square), so you cannot superpose power contributions from different sources. You must find the actual currents and voltages first, then compute power from those. This is the most common error when students first apply the theorem. The linearity property is also what makes Thévenin and Norton equivalents possible — they are direct consequences of the fact that any linear subcircuit, viewed from two terminals, behaves like a single source and a single resistor.
