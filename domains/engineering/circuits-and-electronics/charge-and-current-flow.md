---
id: charge-and-current-flow
title: Charge, Current, and Continuity
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: electric-field
  type: hard
- id: electric-charge-and-coulombs-law
  type: hard
builds-toward:
- electric-potential-and-voltage
- ohms-law-and-conductance
tags:
- fundamentals
- charge
- current
- conservation
stage: formal-systems
status: draft
---

# Charge, Current, and Continuity

## Core Idea
Electric current is the time rate of charge flow (I = dQ/dt) through a conductor. Charge conservation ensures current continuity: the same current flows through all series elements, a consequence of charge accumulation being impossible under steady-state conditions. Understanding conventional current direction (positive charge flow) versus electron flow is essential for circuit analysis.

## Explainer

From your study of Coulomb's law and electric fields, you know that charges exert forces on each other and that a charge placed in an electric field experiences a force proportional to the field strength. In a conductor — a material with free electrons — this force causes charges to move continuously along the material. **Electric current** quantifies that movement: the amount of charge passing through a cross-section per unit time, I = dQ/dt. The unit is the **ampere** (A), equal to one coulomb per second. A wire carrying 1 A has roughly 6.24 × 10¹⁸ electrons passing any cross-section each second.

A conceptual subtlety to resolve immediately: **conventional current direction** is defined as the direction positive charges would flow — from higher electric potential to lower, out of the positive terminal of a source. In physical reality, metals conduct via free electrons, which carry negative charge and flow in the opposite direction. Engineers almost universally work with conventional current, so circuit diagram arrows point against the actual electron flow. This historical convention (from before the electron was discovered) is harmless provided you apply it consistently — the mathematics and predictions are identical either way.

**Charge conservation** is what makes circuit analysis tractable. Charge can be neither created nor destroyed, and in a conductor at steady state, charge cannot accumulate at any interior point — if it did, the resulting electric field would immediately redistribute it. This constraint means that whatever charge per second flows into a node must equal the charge per second flowing out. This is the physical basis for **Kirchhoff's Current Law (KCL)**: the sum of currents entering a node equals the sum leaving. In a series circuit, the same current flows through every element — not because of some coincidence, but as a direct consequence of charge conservation and the impossibility of steady-state accumulation.

The rate interpretation (I = dQ/dt) also connects directly to energy. Current doesn't get "used up" passing through a resistor — the same charge exits as enters. What changes is the energy carried by those charges, quantified as voltage. Energy is transferred from the charges to the resistor (as heat) while the charge count remains unchanged. This distinction — current is conserved, voltage drops — is the conceptual foundation for all the circuit analysis techniques you'll develop next.
