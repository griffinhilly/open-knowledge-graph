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
status: validated
---

# Series Circuits: Resistance and Voltage Division

## Core Idea
In series circuits, the same current flows through all elements. Total resistance is R_total = R₁ + R₂ + .... Voltage divides among resistors proportionally: V_i = I·R_i. Series circuits are useful for current control and voltage distribution across multiple elements.

## Questions

```yaml
- question: "Three resistors — R₁ = 10 Ω, R₂ = 30 Ω, R₃ = 60 Ω — are connected in series to a 12 V battery. What is the voltage across R₃?"
  type: multiple-choice
  options:
    - "4 V — each of the three resistors gets an equal share of the total voltage"
    - "7.2 V — R₃ is 60% of the total resistance, so it takes 60% of the voltage"
    - "12 V — the largest resistor takes the full supply voltage"
    - "3.6 V — the voltage is divided equally between R₂ and R₃ since they are the larger resistors"
  answer: 1
  explanation: "R_total = 10 + 30 + 60 = 100 Ω. Current I = 12 V / 100 Ω = 0.12 A (the same through all three resistors). V₃ = I · R₃ = 0.12 A × 60 Ω = 7.2 V. Equivalently, V₃ = 12 V × (60 Ω / 100 Ω) = 7.2 V. Voltage divides proportionally to resistance — R₃ is 60% of the total resistance, so it gets 60% of the voltage. The equal-share answer (4 V each) is the classic misconception: voltage divides proportionally, not equally."

- question: "Three light bulbs are connected in series. One bulb burns out and becomes an open circuit. A student argues: 'The other two bulbs should still light up — the broken bulb isn't absorbing any current, so current just skips past it.' What is wrong?"
  type: multiple-choice
  options:
    - "Nothing — the two intact bulbs will continue to operate at higher brightness with the broken one removed"
    - "In a series circuit there is only one path for current. An open circuit anywhere in the loop breaks that path entirely, dropping current to zero throughout — all three bulbs go dark"
    - "The student is partially right — the two intact bulbs will flicker but remain on"
    - "The student is correct, but only if the bulbs have identical resistance"
  answer: 1
  explanation: "This is the defining failure mode of series circuits: there is one current path and no alternatives. An open circuit (infinite resistance) anywhere in the series chain makes R_total infinite, dropping current I = V / R_total to exactly zero throughout the entire loop. Every element in the chain goes dark, regardless of whether it is itself broken. This is why old Christmas light strings (wired in series) would go completely dark when a single bulb burned out. Current does not 'skip past' an open circuit — it stops everywhere."

- question: "In a series circuit, the current through each resistor is identical, regardless of the individual resistance values."
  type: true-false
  answer: true
  explanation: "True — this is the defining property of a series circuit and follows directly from KCL. Because all components are connected end to end in a single chain with no branch points, there is only one path for charge to flow. KCL states that current into any node equals current out; with no branches, the same current I passes through every element. The resistors do not 'use up' current; charge that enters one end exits the other in the same quantity. Each resistor's resistance affects the voltage drop across it (V = IR), but not the current, which is set by the total resistance and supply voltage."

- question: "Adding more resistors in series usually increases the total voltage available to each existing component in the circuit."
  type: true-false
  answer: false
  explanation: "False — adding resistors in series increases total resistance, which reduces the total current (I = V_source / R_total). Since the voltage across each existing component is V = I · R_component, a smaller I means less voltage across every existing element. Each new series resistor 'steals' some of the supply voltage, reducing what is available to the others. The only way to increase voltage across a component is to decrease total series resistance (remove other resistors) or increase the supply voltage."

- question: "A voltage divider has R₁ = 1 kΩ and R₂ = 2 kΩ in series across a 9 V supply. What is the voltage across R₂, and why is this circuit useful?"
  type: short-answer
  answer: "R_total = 3 kΩ. Current I = 9 V / 3000 Ω = 3 mA (same through both). Voltage across R₂: V₂ = I × R₂ = 3 mA × 2000 Ω = 6 V. Equivalently, V₂ = 9 V × (2 kΩ / 3 kΩ) = 6 V. The voltage divider is useful because it produces a precise, stable fraction of the supply voltage using only resistors — no separate voltage source required. This makes it ideal for setting reference voltages, biasing transistors, and scaling signal levels in electronics. The output fraction equals R₂ / (R₁ + R₂), which is easily set by choosing the resistor ratio."
  explanation: "Voltage dividers are ubiquitous in electronics precisely because they are simple and predictable. The voltage divider formula V_out = V_in × R₂ / (R₁ + R₂) is a direct consequence of the single shared current and Ohm's law — no more is needed. Understanding that the division is proportional to resistance (not arbitrary or equal) is the key insight that makes the formula derivable rather than memorized."
```

## Explainer

From Kirchhoff's rules, you know two fundamental constraints: **KCL** (currents into a node must sum to zero) and **KVL** (voltages around a closed loop must sum to zero). Series circuits are where these two rules cooperate to produce especially clean results. In a series connection, components are chained end to end — there is only one path for current to travel. KCL immediately tells you the punchline: since there are no branch points, the same current I must flow through every element in the chain. The first resistor does not "use up" current; charge that enters one end exits the other, unchanged in amount.

KVL handles the voltages. Trace around the loop: the battery supplies a voltage V_source, and each resistor "drops" some voltage. The sum of the drops must equal the supply: V_source = I·R₁ + I·R₂ + ... = I(R₁ + R₂ + ...). This shows that the **equivalent resistance** is simply the sum R_total = R₁ + R₂ + .... Physically, resistors in series are like narrow pipes in sequence: each one impedes the same flow, and the total obstruction is additive. A chain of 10 resistors with R = 100 Ω each presents exactly 1000 Ω to the circuit, passing a tenth of the current that a single 100 Ω resistor would.

The voltage across each individual resistor follows directly: V_i = I·R_i, where I = V_source / R_total is the single shared current. This is the **voltage divider** principle — the total voltage is apportioned among resistors in proportion to their resistance. A resistor that is 30% of the total resistance takes 30% of the total voltage. Formally: V_i = V_source · (R_i / R_total). Two-resistor voltage dividers appear constantly in electronics as a way to produce a precise fraction of a supply voltage, for example to bias a transistor or set a reference level for a comparator.

The failure mode to watch for is this: adding more resistors in series always *increases* total resistance, always *reduces* current, and always *reduces* the voltage available to any one element. If you wire three light bulbs in series and one burns out (becomes an open circuit), the current drops to zero and all three go dark — this is why old-style Christmas light strings would go completely dark when one bulb failed. Series circuits trade simplicity for interdependence: each element's behavior depends on every other element in the chain.
