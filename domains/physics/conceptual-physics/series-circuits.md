---
id: series-circuits
title: Series Circuits
domain: physics
course: conceptual-physics
prerequisites:
- id: ohms-law-conceptual
  type: hard
- id: simple-circuits
  type: hard
builds-toward:
- dc-circuits-series-parallel
tags:
- series
- circuit
- resistance
stage: abstract-reasoning
status: draft
---
# Series Circuits

## Core Idea
In a series circuit, all components are connected in a single loop so that current has only one path to follow. The same current flows through every component. The total resistance equals the sum of all individual resistances (R_total = R₁ + R₂ + R₃ + ...). The voltage from the battery is divided among the components, with larger resistors getting a larger share of the voltage.

## How It's Best Learned
Connect two light bulbs in series with a battery and observe that they are dimmer than a single bulb. Remove one bulb and watch both go out (the circuit breaks). Use a multimeter to verify that current is the same everywhere and that the voltages across individual components add up to the battery voltage.

## Common Misconceptions
- Current is used up by the first component, leaving less for the second. (Current is the same through every component in a series circuit. It is voltage that gets divided.)
- Adding more resistors in series makes the circuit brighter. (Adding more resistance in series reduces the total current, making everything dimmer.)
- If one component breaks in a series circuit, the rest still work. (A break anywhere in a series circuit stops all current flow — all components stop working, like old Christmas lights.)
- The voltage is split equally among all components. (Voltage is divided proportionally to resistance. A larger resistor gets a larger fraction of the total voltage.)

## Questions

```yaml
- question: "Three resistors of 2 Ω, 3 Ω, and 5 Ω are connected in series. What is the total resistance?"
  type: multiple-choice
  options: ["10 Ω", "0.97 Ω", "3.33 Ω", "30 Ω"]
  answer: 0
  explanation: "In series, total resistance is the sum: R_total = 2 + 3 + 5 = 10 Ω."

- question: "In a series circuit, the current through every component is the same."
  type: true-false
  answer: true
  explanation: "There is only one path for current in a series circuit, so all charge must flow through every component. The current is identical everywhere in the loop."

- question: "A 12 V battery is connected to two resistors in series: 3 Ω and 6 Ω. What is the voltage across the 6 Ω resistor?"
  type: short-answer
  answer: "8 V. Total resistance = 9 Ω, current = 12/9 = 4/3 A, voltage across 6 Ω = IR = (4/3)(6) = 8 V."
  explanation: "Find total R (3 + 6 = 9 Ω), then total I = V/R = 12/9 A. The voltage across the 6 Ω resistor is V = IR = (12/9)(6) = 8 V. The remaining 4 V is across the 3 Ω resistor."
```

## Explainer
A **series circuit** is the simplest way to connect components: everything is wired in a single loop, one after the other. Imagine a racetrack with only one lane — every car must follow the same path, pass through every checkpoint, and no one can skip ahead. Similarly, in a series circuit, charge must flow through every component in order. There are no shortcuts or alternative routes.

This single-path structure leads to the defining rule: **current is the same through every component**. If 2 amps flows out of the battery, then 2 amps flows through the first resistor, the second resistor, the light bulb, and back to the battery. Nothing is lost along the way. Charge is conserved — what goes in must come out.

Resistance adds up in a simple way in series: **R_total = R₁ + R₂ + R₃ + ...**. Three 10 Ω resistors in series create a total resistance of 30 Ω. This makes intuitive sense — each resistor is another obstacle the current must push through, so the total resistance increases. Adding more components in series always increases resistance and therefore always decreases current (for a given voltage).

**Voltage** in a series circuit behaves differently from current. The total voltage provided by the battery is divided among the components, with each one getting a share proportional to its resistance. This is called a **voltage divider** effect. If you have a 2 Ω and an 8 Ω resistor in series with a 10 V battery, the 2 Ω resistor gets 20% of the voltage (2 V) and the 8 Ω resistor gets 80% (8 V). The shares add up to the full battery voltage.

Series circuits have an important practical consequence: if any single component breaks or is removed, the entire circuit stops working. The single path is broken, current cannot flow, and everything shuts off. This is why old-style Christmas lights would all go dark when one bulb burned out — they were wired in series. Modern designs use parallel wiring to avoid this problem, which is the subject of the next topic.
