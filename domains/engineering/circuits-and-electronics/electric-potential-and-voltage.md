---
id: electric-potential-and-voltage
title: Electric Potential and Voltage
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: charge-and-current-flow
  type: hard
- id: electric-potential-and-potential-energy
  type: soft
builds-toward:
- power-energy-in-circuits
- ohms-law-and-conductance
tags:
- voltage
- potential
- potential-difference
- emf
stage: formal-systems
status: draft
---

# Electric Potential and Voltage

## Core Idea
Electric potential is the work per unit charge needed to move charge in an electric field. Voltage is the potential difference between two points and represents energy per unit charge provided by a source. In circuits, voltages are defined relative to a reference node (ground) and measured across components using two-point measurements.

## Explainer

You already understand charge and current flow — charges moving through a conductor constitute current. But what makes charges move in the first place? The answer is energy differences, and **electric potential** is the tool that quantifies that energy on a per-charge basis. Think of it as the "electrical height" of a point in a circuit: just as water flows downhill from high gravitational potential to low, positive charges tend to flow from high electric potential to low.

**Electric potential** at a point is defined as the work per unit charge required to bring a positive test charge from a reference point (usually infinity in field theory, or ground in circuit analysis) to that point. Its unit is the **volt** (V), which equals one joule per coulomb. When we say a point in a circuit is at 5 V, we mean that moving one coulomb of positive charge from ground to that point requires 5 joules of work done by an external agent against the electric field. The field itself would do that same 5 joules of work if the charge moved from that point back to ground — that's the energy available to do useful work.

**Voltage** — more precisely, **potential difference** — is what appears in circuit analysis. It is always the difference between the potentials at two points: V_AB = V_A − V_B. This matters because absolute potential has no physical meaning in circuits; only differences do. A 9-volt battery doesn't mean the positive terminal is at 9 V in some absolute sense — it means the positive terminal is 9 V higher than the negative terminal. By convention, we assign one node in the circuit the label **ground** (0 V) and express all other node potentials relative to it. This choice is arbitrary but necessary: it gives us a consistent reference for writing and solving circuit equations.

A crucial distinction is between a **voltage source** (which maintains a fixed potential difference between its terminals, doing whatever work is necessary to sustain it) and the **voltage across a passive component** (which is the result of current flowing through it and energy being dissipated or stored). When current flows through a resistor, the resistor has a voltage drop across it — work is done on the charge by the field, and that work is converted to heat. When current charges a capacitor, work is stored as electric field energy between the plates. In both cases, the potential difference is the bookkeeping tool that tracks how energy is distributed around the circuit. Kirchhoff's Voltage Law — the sum of voltage rises and drops around any closed loop equals zero — is simply conservation of energy stated in these potential-difference terms.


