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
status: validated
---

# Charge, Current, and Continuity

## Core Idea
Electric current is the time rate of charge flow (I = dQ/dt) through a conductor. Charge conservation ensures current continuity: the same current flows through all series elements, a consequence of charge accumulation being impossible under steady-state conditions. Understanding conventional current direction (positive charge flow) versus electron flow is essential for circuit analysis.

## Questions

```yaml
- question: "A 100Ω resistor and a 200Ω resistor are connected in series to a battery. How does the current through the 100Ω resistor compare to the current through the 200Ω resistor?"
  type: multiple-choice
  options:
    - "The current through the 100Ω resistor is twice as large, since it has less resistance"
    - "The current through the 200Ω resistor is twice as large, since it draws more power"
    - "The current is the same through both resistors"
    - "The current splits evenly between the two resistors"
  answer: 2
  explanation: "In a series circuit, the same current flows through every element — this is a direct consequence of charge conservation. Charge cannot accumulate inside a conductor at steady state, so every coulomb of charge that enters any cross-section must exit. The resistors have different resistances (and the voltage drops across them will differ), but the current — the rate of charge flow — is identical at every point in the series path. The common misconception is that more resistance 'uses up' more current; what changes is voltage, not current."

- question: "In a circuit diagram, the arrow representing conventional current in a wire points to the right. Which way are electrons actually moving?"
  type: multiple-choice
  options:
    - "To the right — conventional current and electron flow are in the same direction"
    - "To the left — conventional current is defined as positive charge flow, opposite to electron movement"
    - "In both directions simultaneously, since electrons oscillate"
    - "The diagram cannot tell us — conventional current says nothing about electron motion"
  answer: 1
  explanation: "Conventional current is defined as the direction positive charges would flow — from higher to lower potential. Electrons carry negative charge and flow from low to high potential, which is opposite to conventional current. So if conventional current arrows point right, electrons are moving left. This historical convention (established before the electron was discovered) is universally used in circuit analysis, and it produces correct results as long as applied consistently. The mathematics is identical regardless of which convention you use."

- question: "In a series circuit, the same current flows through every component because charge is conserved and cannot accumulate inside the conductor."
  type: true-false
  answer: true
  explanation: "This is the physical basis of Kirchhoff's Current Law. Charge cannot be created or destroyed, and at steady state, charge cannot build up at any interior point — the resulting electric field would immediately redistribute it. Therefore, the rate of charge flow (current) into any segment must equal the rate out. In a single-path (series) circuit, this means the current is identical everywhere in the loop."

- question: "When current passes through a resistor, some of the current is consumed — less current exits the resistor than enters it."
  type: true-false
  answer: false
  explanation: "This is one of the most common misconceptions in basic circuit theory. Current is not 'used up.' The same charge that enters a resistor exits it — the number of electrons is conserved. What changes is the energy carried by those charges: voltage drops across the resistor as the charges transfer energy to it (as heat). Current is conserved; voltage is not. The distinction between current (charge flow rate) and energy (what gets dissipated) is fundamental to all circuit analysis."

- question: "Why does charge conservation imply that the same current flows through all elements in a series circuit, even though those elements may have very different resistances?"
  type: short-answer
  answer: "At steady state, charge cannot accumulate inside a conductor. If more charge per second were entering a wire segment than leaving, charge would pile up, creating an electric field that would oppose further buildup and push charge forward until flow balanced. This self-correcting mechanism enforces equal current everywhere in a single-path circuit. Resistance affects how much voltage is required to drive a given current through a component, but it does not change the fact that charge is conserved and the same current must pass through each element in series."
  explanation: "The conceptual key is that current continuity is not a coincidence or a rule to memorize — it is an inescapable consequence of charge conservation combined with the impossibility of steady-state charge accumulation. Kirchhoff's Current Law is just this physical principle stated as a circuit rule: what flows in must flow out at every node."
```

## Explainer

From your study of Coulomb's law and electric fields, you know that charges exert forces on each other and that a charge placed in an electric field experiences a force proportional to the field strength. In a conductor — a material with free electrons — this force causes charges to move continuously along the material. **Electric current** quantifies that movement: the amount of charge passing through a cross-section per unit time, I = dQ/dt. The unit is the **ampere** (A), equal to one coulomb per second. A wire carrying 1 A has roughly 6.24 × 10¹⁸ electrons passing any cross-section each second.

A conceptual subtlety to resolve immediately: **conventional current direction** is defined as the direction positive charges would flow — from higher electric potential to lower, out of the positive terminal of a source. In physical reality, metals conduct via free electrons, which carry negative charge and flow in the opposite direction. Engineers almost universally work with conventional current, so circuit diagram arrows point against the actual electron flow. This historical convention (from before the electron was discovered) is harmless provided you apply it consistently — the mathematics and predictions are identical either way.

**Charge conservation** is what makes circuit analysis tractable. Charge can be neither created nor destroyed, and in a conductor at steady state, charge cannot accumulate at any interior point — if it did, the resulting electric field would immediately redistribute it. This constraint means that whatever charge per second flows into a node must equal the charge per second flowing out. This is the physical basis for **Kirchhoff's Current Law (KCL)**: the sum of currents entering a node equals the sum leaving. In a series circuit, the same current flows through every element — not because of some coincidence, but as a direct consequence of charge conservation and the impossibility of steady-state accumulation.

The rate interpretation (I = dQ/dt) also connects directly to energy. Current doesn't get "used up" passing through a resistor — the same charge exits as enters. What changes is the energy carried by those charges, quantified as voltage. Energy is transferred from the charges to the resistor (as heat) while the charge count remains unchanged. This distinction — current is conserved, voltage drops — is the conceptual foundation for all the circuit analysis techniques you'll develop next.
