---
id: potential-difference-voltage
title: Potential Difference and Voltage
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-potential
  type: hard
- id: electric-field
  type: hard
builds-toward:
- equipotential-surfaces
- capacitance
tags:
- electrostatics
- energy
- circuit concept
stage: formal-systems
status: draft
---

# Potential Difference and Voltage

## Core Idea
Potential difference between two points is the work per unit charge to move between them: V_AB = -(∫_B^A E·dl). Voltage is the practical term for potential difference. It is path-independent and depends only on endpoints, a consequence of the conservative nature of electrostatic fields.

## How It's Best Learned
Calculate potential difference for simple geometries by direct integration and by using potential functions. Measure voltages in circuits to build intuition for typical voltage scales.

## Common Misconceptions
- Potential and potential difference are the same (potential is absolute; difference is relative).
- Current flows from high to low potential magnitude (direction depends on charge sign).
- Voltage magnitude is always positive (sign depends on reference direction).

## Explainer

You already know that the electric potential V at a point is the potential energy per unit charge placed there, and that the electric field **E** at a point gives the force per unit charge. **Potential difference** is the physically measurable quantity connecting these two ideas: it is the work done by the electric field per unit positive charge as that charge moves between two specific points in space.

The formula V_AB = −∫(B to A) **E** · d**l** captures this. Imagine carrying a small positive test charge from point B to point A along any path you choose. The electric field either helps or hinders your journey at each step; the total work done by the field per unit charge, accumulated over the entire path, is the potential difference V_A − V_B. Because electrostatic fields are **conservative** — a consequence of their Coulomb origin that you studied when learning about electric potential — this work depends only on the starting and ending points, not on the route taken. A straight path, a curved detour, and a zigzag all give the same answer. This path-independence is what makes voltage a well-defined property of a pair of locations.

The word **voltage** is the practical term for potential difference. A 9-volt battery maintains a 9 V difference between its terminals, doing 9 joules of work per coulomb of charge that moves from the negative to the positive terminal inside it. That energy is then available to drive current through an external circuit — flowing from the high-potential terminal through resistors, LEDs, or motors, losing energy along the way, and returning to the low-potential terminal. Ohm's law connects voltage and current: the potential difference across a resistor equals the current through it times the resistance, V = IR.

A subtle but important distinction: potential (V at a single point) is only defined relative to an arbitrary reference, typically chosen to be zero at infinity or at a ground node. Potential difference (ΔV between two points) is absolute and physically meaningful regardless of that reference choice — you cannot measure absolute potential with a voltmeter, but you can always measure the difference between two probes. This is why voltage is the natural language of circuits: every component has a voltage *across* it, and the sum of voltage drops around any closed loop must equal zero (Kirchhoff's voltage law). The path-independence you establish here is the foundation for equipotential surfaces, capacitance, and eventually the relationship between **E** and **V** via the gradient.
