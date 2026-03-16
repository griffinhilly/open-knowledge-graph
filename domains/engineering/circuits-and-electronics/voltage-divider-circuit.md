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

## Explainer

You already know from Kirchhoff's Voltage Law (KVL) that in a series loop, the voltages across all elements must sum to the applied voltage. The voltage divider is what that law implies when two resistors share the same current. In a series circuit, the same current I flows through every element — there is nowhere else for it to go. That means the voltage drop across each resistor is V = IR, and since I is the same for both, the drops are proportional to the resistances. A bigger resistor gets a bigger share of the applied voltage, in exact proportion to its fraction of the total resistance.

Working through the math confirms this. With resistors R₁ and R₂ in series across voltage V, the total resistance is R₁ + R₂, so the current is I = V / (R₁ + R₂). The voltage across R₁ is then V₁ = I · R₁ = V · R₁/(R₁ + R₂). This is the **voltage divider formula**: V₁ = V · (R₁ / (R₁ + R₂)). Notice the structure — V₁ is a fraction of V, and the fraction is determined entirely by the ratio of resistances. If R₁ = R₂, each gets exactly half. If R₁ is 90% of the total resistance, it gets 90% of the voltage.

A resistive sensor like a **thermistor** or **potentiometer** makes this immediately practical. A thermistor changes resistance with temperature; if you put it in series with a fixed resistor connected to a known voltage, the output voltage across the fixed resistor shifts as temperature changes. The voltage divider converts a resistance change into a voltage change, which is easy to measure with an ADC. This is one of the most common signal conditioning circuits in electronics, and it works because the divider formula gives you a predictable, linear-in-resistance output.

The important caveat is that the divider formula assumes no current is drawn from the output node — it assumes the "load" connected to the output has infinitely high resistance. In practice, connecting a load in parallel with R₂ changes the effective bottom resistance and throws off the predicted output voltage. This **loading effect** is why voltage dividers are most useful as bias circuits or signal conditioners into high-impedance inputs (like op-amp or ADC inputs), and why understanding the formula is just the starting point — accounting for load impedance is the next step in real circuit design.
