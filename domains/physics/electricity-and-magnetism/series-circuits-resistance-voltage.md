---
id: series-circuits-resistance-voltage
title: 'Series Circuits: Resistance and Voltage Division'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: circuit-topology-and-elements
  type: hard
- id: kirchhoffs-rules
  type: hard
builds-toward:
- combination-series-parallel-networks
tags:
- circuit analysis
- series circuits
- resistance
stage: formal-systems
status: draft
---

# Series Circuits: Resistance and Voltage Division

## Core Idea
In series circuits, the same current flows through all elements. Total resistance is R_total = R₁ + R₂ + .... Voltage divides among resistors proportionally: V_i = I·R_i. Series circuits are useful for current control and voltage distribution across multiple elements.

## Explainer

From Kirchhoff's rules, you know two fundamental constraints: **KCL** (currents into a node must sum to zero) and **KVL** (voltages around a closed loop must sum to zero). Series circuits are where these two rules cooperate to produce especially clean results. In a series connection, components are chained end to end — there is only one path for current to travel. KCL immediately tells you the punchline: since there are no branch points, the same current I must flow through every element in the chain. The first resistor does not "use up" current; charge that enters one end exits the other, unchanged in amount.

KVL handles the voltages. Trace around the loop: the battery supplies a voltage V_source, and each resistor "drops" some voltage. The sum of the drops must equal the supply: V_source = I·R₁ + I·R₂ + ... = I(R₁ + R₂ + ...). This shows that the **equivalent resistance** is simply the sum R_total = R₁ + R₂ + .... Physically, resistors in series are like narrow pipes in sequence: each one impedes the same flow, and the total obstruction is additive. A chain of 10 resistors with R = 100 Ω each presents exactly 1000 Ω to the circuit, passing a tenth of the current that a single 100 Ω resistor would.

The voltage across each individual resistor follows directly: V_i = I·R_i, where I = V_source / R_total is the single shared current. This is the **voltage divider** principle — the total voltage is apportioned among resistors in proportion to their resistance. A resistor that is 30% of the total resistance takes 30% of the total voltage. Formally: V_i = V_source · (R_i / R_total). Two-resistor voltage dividers appear constantly in electronics as a way to produce a precise fraction of a supply voltage, for example to bias a transistor or set a reference level for a comparator.

The failure mode to watch for is this: adding more resistors in series always *increases* total resistance, always *reduces* current, and always *reduces* the voltage available to any one element. If you wire three light bulbs in series and one burns out (becomes an open circuit), the current drops to zero and all three go dark — this is why old-style Christmas light strings would go completely dark when one bulb failed. Series circuits trade simplicity for interdependence: each element's behavior depends on every other element in the chain.
