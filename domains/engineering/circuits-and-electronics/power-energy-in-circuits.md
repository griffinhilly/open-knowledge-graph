---
id: power-energy-in-circuits
title: Power and Energy Conservation
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: electric-potential-and-voltage
  type: hard
- id: charge-and-current-flow
  type: hard
builds-toward:
- ohms-law-and-conductance
- ideal-voltage-and-current-sources
tags:
- power
- energy
- conservation
- dissipation
stage: formal-systems
status: draft
---

# Power and Energy Conservation

## Core Idea
Instantaneous power P = VI represents the rate of energy transfer. Power is positive when energy flows into a component, negative when energy flows out. Energy conservation requires that total power supplied by sources equals total power dissipated in resistors plus power stored in reactive elements, a direct consequence of Kirchhoff's voltage law.

## Questions

```yaml
- question: "A circuit element has 8V across it and 3A flowing into its positive terminal. Using the passive sign convention, P = +24W. What does this mean?"
  type: multiple-choice
  options:
    - "The element supplies 24W to the rest of the circuit — it is acting as a source"
    - "The element absorbs 24W — it is a load converting electrical energy to another form"
    - "The element stores 24W — it is a reactive element like a capacitor or inductor"
    - "The sign is ambiguous without knowing whether the element is a resistor or a source"
  answer: 1
  explanation: "Under the passive sign convention, current entering the positive terminal with positive voltage gives P = +VI > 0, meaning the element *absorbs* power (it is a load: resistor, motor, etc.). P < 0 would indicate a source supplying power. Many students invert this, thinking positive power means the element is 'doing work on' the circuit — but positive power means work is being done *on* the element. A battery or generator would show negative P under this convention."

- question: "A transmission line has resistance 2 Ω and must deliver 10 kW of power. Compare the resistive power loss when transmitting at 100V versus at 10,000V."
  type: multiple-choice
  options:
    - "The loss is the same at both voltages — only total power and resistance determine it"
    - "At 100V the current is 100A giving I²R = 20,000W loss; at 10,000V the current is 1A giving I²R = 2W loss"
    - "At higher voltage, I²R loss increases because both voltage and current contribute"
    - "The loss depends only on the voltage across the line, not the current through it"
  answer: 1
  explanation: "P = IV, so for fixed power P, current I = P/V. At 100V: I = 100A → loss = I²R = 10,000 × 2 = 20,000W (exceeding the intended delivery). At 10,000V: I = 1A → loss = 1 × 2 = 2W — negligible. Resistive losses scale as I², so the ratio of losses is (100/1)² = 10,000-fold. This is why the power grid transmits at high voltage: high voltage forces low current, and I²R loss is exquisitely sensitive to current."

- question: "Kirchhoff's voltage law (the sum of voltages around any closed loop equals zero) is mathematically equivalent to energy conservation in that loop."
  type: true-false
  answer: true
  explanation: "KVL states ΣV = 0 around any closed loop. Multiplying each term by the common loop current I gives Σ(VI) = ΣP = 0 — total power in the loop is zero. This means sources supply exactly as much power as loads absorb. KVL and energy conservation are two expressions of the same underlying constraint, which is why both are always satisfied simultaneously in a valid circuit."

- question: "A resistor can supply power to a circuit if a sufficiently large current is forced through it by an external source."
  type: true-false
  answer: false
  explanation: "Resistors can only dissipate (absorb) power — they can never supply it. The power dissipated is P = I²R = V²/R, which is always non-negative regardless of the direction or magnitude of current. The I² term ensures the result is always positive. Physically, a resistor converts electrical energy to heat; there is no mechanism by which it can return energy to the circuit. Only sources (batteries, generators, dependent sources) supply power."

- question: "Why do power transmission lines operate at high voltage and low current rather than low voltage and high current? Use P = I²R in your explanation."
  type: short-answer
  answer: "For a fixed amount of power to be delivered (P = IV is constant), choosing high voltage means the current must be low (I = P/V). The power dissipated as heat in the transmission line's resistance is P_loss = I²R. Because the loss scales with the *square* of current, even a modest reduction in current dramatically reduces losses: doubling the voltage halves the current and cuts resistive losses by a factor of four. High-voltage transmission therefore minimizes wasted energy over long distances."
  explanation: "This is why the power grid steps up voltage to hundreds of kilovolts for long-distance transmission and then steps it back down near homes and businesses. The I²R formula makes the design principle clear: line resistance is fixed, so minimizing I is the only way to minimize losses. The quadratic dependence makes high-voltage transmission especially efficient at scale."
```

## Explainer

You already know that voltage is energy per unit charge and that current is charge per unit time. Multiply them and you get energy per unit time — that is, power. The relation **P = V · I** is not a new law but a logical consequence of the definitions you already have. If 5 volts is the energy cost per coulomb of charge passing through a component, and 2 amperes is 2 coulombs passing per second, then 10 joules are transferred per second — 10 watts of power.

The sign convention — positive power means energy flows into the component, negative means energy flows out — is a bookkeeping choice that makes the conservation law clean. By convention, if you define current entering the positive terminal of a component's voltage reference as positive, then P = +VI means the component absorbs power (a load: resistor, motor) and P = −VI means it supplies power (a source: battery, generator). This **passive sign convention** keeps the accounting consistent: sum all the P = VI products around a circuit, and the total must be zero by energy conservation. Sources supply exactly as much as loads absorb.

For resistors specifically, Ohm's law (V = IR) lets you write power in two equivalent forms: P = V²/R = I²R. Both are always positive for a resistor because resistors can only dissipate (convert to heat), never supply, energy. The I²R form is particularly intuitive for wires: even a small resistance in a high-current path dissipates significant power, which is why power lines operate at high voltage (and therefore low current) to minimize resistive losses over long distances.

Energy is simply power integrated over time: E = ∫P dt. For constant power, E = P · t. This integral form connects circuit behavior to physical reality: the heat generated in a resistor, the charge stored in a capacitor, the mechanical work done by a motor — all are energy quantities, computed by integrating the instantaneous power. Kirchhoff's voltage law, which you know as the constraint that voltages around any loop sum to zero, is mathematically equivalent to saying total power in the loop is zero — the voltage law and energy conservation are two views of the same underlying constraint.
