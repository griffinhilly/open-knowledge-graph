---
id: electric-power
title: Electric Power
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: ohms-law
  type: hard
- id: work-and-energy
  type: hard
builds-toward:
- dc-circuits-series-parallel
- ac-power-and-resonance
tags:
- power
- energy
- joule-heating
- circuits
stage: formal-systems
status: validated
---

# Electric Power

## Core Idea
Electric power is the rate at which electrical energy is converted to other forms: P = IV, measured in watts (W = J/s). For a resistor, this becomes P = I²R = V²/R using Ohm's law. Power dissipated as heat in a resistor (Joule heating) is always positive regardless of current direction. Over time, energy E = Pt is consumed; utility companies bill in kilowatt-hours (kWh), where 1 kWh = 3.6 MJ.

## How It's Best Learned
Derive the three forms of the power formula from P = IV and V = IR. Apply to real-world problems: light bulb wattage, household circuits, and transmission line losses to understand why high-voltage transmission is efficient.

## Common Misconceptions
- Power is not the same as energy; it is the rate of energy use.
- P = V²/R applies when V is fixed (parallel connection); P = I²R when I is fixed (series connection).
- Joule heating is irreversible energy dissipation, not stored potential energy.

## Explainer

From your study of work and energy, you know that power is the rate of doing work: P = dW/dt, measured in watts. In a circuit, charges are the carriers of energy. When a charge q moves through a potential difference V, the work done on it is W = qV. Dividing both sides by time, the rate at which energy is delivered is P = (q/t) × V = IV, where I = q/t is the current. This gives the fundamental formula **P = IV**: power equals current times voltage. Every watt delivered to a circuit element represents one joule of energy per second flowing into it.

For a resistor obeying Ohm's law (V = IR), you can substitute to get two equivalent forms. Replacing V with IR gives P = I × (IR) = I²R; replacing I with V/R gives P = (V/R) × V = V²/R. All three formulas — P = IV, P = I²R, P = V²/R — are equivalent for a resistor, but they differ in which variable is held fixed. In a series circuit, the same current flows through all elements, so **P = I²R** is most useful; resistance increases power dissipation. In a parallel circuit, all elements share the same voltage, so **P = V²/R** is most useful; resistance decreases power dissipation. Choosing the wrong formula when the context implies the other is a common error.

The energy converted in a resistor appears as heat — this is **Joule heating**. It is irreversible: unlike energy stored in a capacitor or compressed spring, the heat dissipated cannot be converted back to electrical energy by the resistor. The total energy consumed over time t is E = Pt. Electric utility companies measure this in **kilowatt-hours**: a device drawing 1 kW for one hour consumes 1 kWh = 3.6 MJ. A 100 W light bulb running for 10 hours uses 1 kWh.

Understanding power also explains long-distance electrical transmission. Moving a given amount of power P at high voltage V requires only a small current I = P/V. Since transmission line losses scale as I²R (the Joule heating formula with fixed line resistance R), halving the current cuts losses by a factor of four. This is why power plants step voltage up to hundreds of thousands of volts for transmission, then step it back down for residential use. The physics is P = I²R: reduce I to reduce wasted heat in the lines.
