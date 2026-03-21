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

## Questions

```yaml
- question: "A 100Ω resistor and a 200Ω resistor are connected in parallel to the same 12V battery. Which resistor dissipates more power?"
  type: multiple-choice
  options:
    - "The 200Ω resistor — more resistance means more power dissipated"
    - "The 100Ω resistor — in a parallel circuit with fixed voltage, lower resistance draws more current and dissipates more power"
    - "Both dissipate equal power — they are connected to the same voltage source"
    - "The 200Ω resistor — it allows less current to flow, which concentrates the energy"
  answer: 1
  explanation: "In a parallel circuit, all branches share the same voltage (12V here). The appropriate power formula is P = V²/R: with fixed V, power decreases as resistance increases. P₁₀₀ = 144/100 = 1.44W; P₂₀₀ = 144/200 = 0.72W. The 100Ω resistor dissipates twice as much power. The critical misconception (option A) is that 'more resistance = more power' — this is true in a series circuit where current is fixed (P = I²R), but exactly backwards in a parallel circuit where voltage is fixed. Choosing the wrong formula because you forgot which quantity is held constant is the most common error in power calculations."

- question: "A high-voltage power transmission line carries 1000 MW of power at 500,000 V. If the transmission voltage were cut to 50,000 V (one-tenth as high) while delivering the same power, what would happen to resistive losses in the transmission lines?"
  type: multiple-choice
  options:
    - "Losses would decrease by a factor of 10 — lower voltage means less electrical stress on the insulation"
    - "Losses would stay the same — the same amount of power is being delivered regardless of voltage"
    - "Losses would increase by a factor of 100 — the required current increases tenfold, and losses scale as I²"
    - "Losses would double — current doubles when voltage halves"
  answer: 2
  explanation: "Power = IV, so delivering the same power at one-tenth the voltage requires ten times the current (I = P/V). Resistive losses in the transmission lines scale as I²R. If I increases by 10×, then I² increases by 100×, so losses increase by a factor of 100. This is precisely why power is transmitted at very high voltages — the I²R relationship means small reductions in current produce large reductions in transmission loss. Halving current cuts losses by 75%; the 500kV → 50V comparison here is a 100-fold increase in losses, making lower-voltage long-distance transmission economically and physically impractical."

- question: "In Joule heating, reversing the direction of current through a resistor causes the resistor to absorb heat rather than generate it."
  type: true-false
  answer: false
  explanation: "Joule heating always generates heat regardless of current direction, because power dissipated is P = I²R — the current is squared, so it's always positive. Whether current flows left-to-right or right-to-left, the resistor converts electrical energy to heat. This distinguishes Joule heating from energy storage elements: a capacitor stores energy (charge/discharge), and an inductor stores energy (magnetic field build-up/collapse), but a resistor always dissipates — it can never return electrical energy to the circuit. Joule heating is irreversible by nature."

- question: "Electric power and electric energy are different quantities: power is the rate at which energy is consumed, while energy is the total amount consumed over time."
  type: true-false
  answer: true
  explanation: "Power (P, measured in watts) and energy (E, measured in joules or kilowatt-hours) are related by E = P × t. A 100W light bulb operating for 10 hours consumes E = 100W × 10h = 1000 Wh = 1 kWh of energy. The distinction matters practically: utility companies bill for energy (kWh), not power (watts). A device with a high wattage rating but short usage time may consume less total energy than a low-wattage device running continuously. Confusing the two leads to errors in circuit analysis — a 60W bulb doesn't 'use' 60 joules; it converts 60 joules per second."

- question: "Why is the statement 'P = I²R means more resistance always dissipates more power' sometimes correct and sometimes exactly backwards? Explain when each case applies."
  type: short-answer
  answer: "P = I²R applies when current I is fixed — typically in a series circuit, where all elements carry the same current. With fixed I, doubling R doubles power. P = V²/R applies when voltage V is fixed — typically in a parallel circuit, where all elements share the same voltage. With fixed V, doubling R halves power. The direction of the relationship reverses depending on what the circuit holds constant. 'More resistance = more power' is true in series (fixed I), and 'more resistance = less power' is true in parallel (fixed V)."
  explanation: "This is the most important nuance in power calculations. Both P = I²R and P = V²/R are always mathematically true for a resistor, but they give different intuitions because they assume different variables are held constant. In a series circuit, current is the same through all elements (Kirchhoff's current law for a single loop), so I²R is the natural formula. In a parallel circuit, voltage is the same across all branches, so V²/R is the natural formula. Using the wrong one doesn't give a math error — it gives a valid calculation for the wrong scenario."
```

## Explainer

From your study of work and energy, you know that power is the rate of doing work: P = dW/dt, measured in watts. In a circuit, charges are the carriers of energy. When a charge q moves through a potential difference V, the work done on it is W = qV. Dividing both sides by time, the rate at which energy is delivered is P = (q/t) × V = IV, where I = q/t is the current. This gives the fundamental formula **P = IV**: power equals current times voltage. Every watt delivered to a circuit element represents one joule of energy per second flowing into it.

For a resistor obeying Ohm's law (V = IR), you can substitute to get two equivalent forms. Replacing V with IR gives P = I × (IR) = I²R; replacing I with V/R gives P = (V/R) × V = V²/R. All three formulas — P = IV, P = I²R, P = V²/R — are equivalent for a resistor, but they differ in which variable is held fixed. In a series circuit, the same current flows through all elements, so **P = I²R** is most useful; resistance increases power dissipation. In a parallel circuit, all elements share the same voltage, so **P = V²/R** is most useful; resistance decreases power dissipation. Choosing the wrong formula when the context implies the other is a common error.

The energy converted in a resistor appears as heat — this is **Joule heating**. It is irreversible: unlike energy stored in a capacitor or compressed spring, the heat dissipated cannot be converted back to electrical energy by the resistor. The total energy consumed over time t is E = Pt. Electric utility companies measure this in **kilowatt-hours**: a device drawing 1 kW for one hour consumes 1 kWh = 3.6 MJ. A 100 W light bulb running for 10 hours uses 1 kWh.

Understanding power also explains long-distance electrical transmission. Moving a given amount of power P at high voltage V requires only a small current I = P/V. Since transmission line losses scale as I²R (the Joule heating formula with fixed line resistance R), halving the current cuts losses by a factor of four. This is why power plants step voltage up to hundreds of thousands of volts for transmission, then step it back down for residential use. The physics is P = I²R: reduce I to reduce wasted heat in the lines.
