---
id: voltage-divider-circuit
title: Voltage Divider Principle
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: kirchhoff-voltage-law
  type: hard
builds-toward:
- series-parallel-resistor-analysis
- impedance-admittance-networks
tags:
- circuit-analysis
- resistive-circuits
- fundamental
stage: formal-systems
status: draft
---

# Voltage Divider Principle

## Core Idea
The voltage divider principle describes how voltage distributes across series resistors: the voltage across any resistor is proportional to its resistance relative to the total. For series resistors R₁ and R₂ with applied voltage V, the voltage across R₁ is V × (R₁/(R₁+R₂)). This technique simplifies circuit analysis and is widely used in sensor signal conditioning and biasing circuits.

## Questions

```yaml
- question: "Resistors R₁ = 3 kΩ and R₂ = 1 kΩ are connected in series across a 12 V supply. What is the voltage across R₂?"
  type: multiple-choice
  options:
    - "9 V — R₁ is larger so it takes more voltage, leaving only the remainder for R₂"
    - "6 V — two resistors always split the voltage equally"
    - "3 V — the voltage across each resistor is proportional to its fraction of the total resistance"
    - "12 V — each element in a series circuit sees the full supply voltage"
  answer: 2
  explanation: "Applying the voltage divider formula: V₂ = V × R₂/(R₁+R₂) = 12 × 1/(3+1) = 12 × 0.25 = 3 V. The voltage distributes proportionally to resistance: R₂ is 25% of the total resistance (1 kΩ out of 4 kΩ), so it gets 25% of the applied voltage. R₁ gets 75%, or 9 V. Option B reflects the common misconception that equal current means equal voltage; current is equal in a series circuit, but voltage depends on V = IR, so larger resistance means larger voltage drop."

- question: "You design a voltage divider to produce 3.3 V from a 5 V supply for a sensor circuit. When you connect a microcontroller input with 10 kΩ input impedance to the output node, what happens to the output voltage?"
  type: multiple-choice
  options:
    - "It stays at 3.3 V — the divider formula is independent of what is connected to the output"
    - "It drops below 3.3 V — the load in parallel with the lower resistor reduces the effective lower resistance and shifts the voltage ratio"
    - "It rises above 3.3 V — the microcontroller provides additional current that adds to the divider's output"
    - "It oscillates unpredictably — connecting a load creates a resonant feedback loop"
  answer: 1
  explanation: "The loading effect: when a resistive load is connected in parallel with R₂, it reduces the effective resistance of the lower leg. The voltage divider formula V₂ = V × R₂/(R₁+R₂) assumed no current drawn from the output — the full current through R₁ flows through R₂. With a load, some current diverts through the load, the effective lower resistance drops, and the output voltage falls below the predicted 3.3 V. The formula only holds when the load impedance is much larger than R₂. Microcontroller inputs often have high impedance (10 kΩ–1 MΩ), which is why voltage dividers work reasonably well as biasing circuits into op-amp or ADC inputs."

- question: "In a voltage divider, the resistor with the larger resistance value always receives the larger share of the applied voltage."
  type: true-false
  answer: true
  explanation: "In a series circuit, the same current I flows through every element (Kirchhoff's Current Law). The voltage across each resistor is V = IR. Since I is identical for both resistors, the voltage is directly proportional to resistance: larger resistance → larger voltage drop. A resistor representing 70% of the total series resistance receives 70% of the applied voltage. This is the core principle of voltage division and directly follows from Ohm's Law applied to a series circuit."

- question: "The voltage divider formula V₁ = V × R₁/(R₁ + R₂) remains accurate regardless of what circuit is connected to the output node."
  type: true-false
  answer: false
  explanation: "The formula assumes no current is drawn from the output — the 'load' has infinite impedance. Any finite load in parallel with R₂ changes the effective lower resistance, altering the voltage ratio. The formula becomes an approximation that degrades as load impedance decreases relative to R₂. For the formula to be accurate in practice, the load impedance must be much larger than R₂ (typically 10× or more). This loading effect is why voltage dividers are most reliable as references into high-impedance inputs, not as general-purpose voltage sources."

- question: "Explain why connecting a load to the output node of a voltage divider changes the output voltage, and under what conditions the loading effect can be safely ignored."
  type: short-answer
  answer: "The voltage divider formula assumes the entire current through R₁ also flows through R₂. When a load is connected in parallel with R₂, current splits between R₂ and the load. The parallel combination of R₂ and R_load is less than R₂ alone, so the effective lower resistance decreases, and the voltage ratio shifts downward. The loading effect can be safely ignored when R_load >> R₂ (typically 10× or more), because then almost all current still flows through R₂ and the parallel combination is nearly equal to R₂. High-impedance inputs like op-amp or ADC inputs (megaohm range) typically satisfy this condition when R₂ is in the kilohm range."
  explanation: "Understanding the loading effect is what separates a student who can apply the formula from one who can design real circuits. The formula gives the right answer only in the idealized condition of zero output current; real circuits violate this assumption to varying degrees, and a designer must know when that violation matters enough to account for it — often by using a buffer (op-amp voltage follower) between the divider output and the load."
```

## Explainer

You already know from Kirchhoff's Voltage Law (KVL) that in a series loop, the voltages across all elements must sum to the applied voltage. The voltage divider is what that law implies when two resistors share the same current. In a series circuit, the same current I flows through every element — there is nowhere else for it to go. That means the voltage drop across each resistor is V = IR, and since I is the same for both, the drops are proportional to the resistances. A bigger resistor gets a bigger share of the applied voltage, in exact proportion to its fraction of the total resistance.

Working through the math confirms this. With resistors R₁ and R₂ in series across voltage V, the total resistance is R₁ + R₂, so the current is I = V / (R₁ + R₂). The voltage across R₁ is then V₁ = I · R₁ = V · R₁/(R₁ + R₂). This is the **voltage divider formula**: V₁ = V · (R₁ / (R₁ + R₂)). Notice the structure — V₁ is a fraction of V, and the fraction is determined entirely by the ratio of resistances. If R₁ = R₂, each gets exactly half. If R₁ is 90% of the total resistance, it gets 90% of the voltage.

A resistive sensor like a **thermistor** or **potentiometer** makes this immediately practical. A thermistor changes resistance with temperature; if you put it in series with a fixed resistor connected to a known voltage, the output voltage across the fixed resistor shifts as temperature changes. The voltage divider converts a resistance change into a voltage change, which is easy to measure with an ADC. This is one of the most common signal conditioning circuits in electronics, and it works because the divider formula gives you a predictable, linear-in-resistance output.

The important caveat is that the divider formula assumes no current is drawn from the output node — it assumes the "load" connected to the output has infinitely high resistance. In practice, connecting a load in parallel with R₂ changes the effective bottom resistance and throws off the predicted output voltage. This **loading effect** is why voltage dividers are most useful as bias circuits or signal conditioners into high-impedance inputs (like op-amp or ADC inputs), and why understanding the formula is just the starting point — accounting for load impedance is the next step in real circuit design.
