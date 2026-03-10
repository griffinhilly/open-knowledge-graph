---
id: circuit-variables-and-elements
title: Circuit Variables and Ideal Circuit Elements
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: ohms-law
  type: hard
- id: electric-current-and-resistance
  type: hard
- id: electric-power
  type: soft
- id: capacitance
  type: soft
- id: inductance-and-inductors
  type: soft
builds-toward:
- node-voltage-method
- mesh-current-method
- capacitor-inductor-energy-storage
- phasor-representation
tags:
- circuit-elements
- voltage
- current
- power
- passive-sign-convention
stage: formal-systems
status: draft
---

# Circuit Variables and Ideal Circuit Elements

## Core Idea
Circuit analysis begins with precise definitions of voltage, current, power, and energy as circuit variables. Ideal circuit elements—resistors, capacitors, inductors, and independent or dependent sources—are mathematical models that approximate real component behavior. The passive sign convention establishes a consistent framework for assigning reference polarities and current directions. Power absorbed by an element equals voltage times current under the passive sign convention; energy is power integrated over time.

## How It's Best Learned
Practice assigning reference directions and applying the passive sign convention to multi-element circuits before writing any equations. Work through examples involving both independent and dependent sources, tracking polarity carefully. Draw complete circuit diagrams with all labeled variables as a habit.

## Common Misconceptions
- Confusing the reference direction (a mathematical choice) with the actual physical direction of current flow — they can differ.
- Assuming a voltage source fixes the current through it or a current source fixes the voltage across it — the other variable is determined by the circuit.
- Conflating power delivered by a source with power absorbed by a load; the sign convention distinguishes them.
