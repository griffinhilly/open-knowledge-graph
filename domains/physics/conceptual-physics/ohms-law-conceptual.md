---
id: ohms-law-conceptual
title: "Ohm's Law: V = IR"
domain: physics
course: conceptual-physics
prerequisites:
- id: current-voltage-resistance
  type: hard
- id: one-step-equations
  type: hard
builds-toward:
- ohms-law
tags:
- ohms-law
- voltage
- current
- resistance
stage: abstract-reasoning
status: validated
---
# Ohm's Law: V = IR

## Core Idea
Ohm's Law states that the voltage across a component equals the current through it times its resistance: V = IR. This can be rearranged to find current (I = V/R) or resistance (R = V/I). The law tells you that increasing voltage increases current, while increasing resistance decreases current. It is the fundamental equation for analyzing electric circuits.

## How It's Best Learned
Build circuits with batteries and resistors, measuring voltage with a voltmeter and current with an ammeter. Change the voltage (add batteries) and observe the current increase. Change the resistance (swap resistors) and observe the current decrease. Plot voltage vs. current to see the linear relationship.

## Common Misconceptions
- Ohm's Law applies to all electrical devices equally. (Ohm's Law is exact for simple resistors. Some devices like diodes and LEDs have non-linear behavior where V/I is not constant.)
- Current causes voltage. (Voltage causes current to flow, not the other way around. The battery creates a voltage difference, which drives current through the circuit.)
- Resistance always stays the same. (The resistance of some materials changes with temperature. A light bulb filament has higher resistance when hot than when cold.)
- You need to memorize three different formulas. (V = IR, I = V/R, and R = V/I are all the same equation rearranged. Learn one, derive the rest.)

## Questions

```yaml
- question: "A 12 V battery is connected to a 4 Ω resistor. What current flows?"
  type: multiple-choice
  options: ["48 A", "3 A", "0.33 A", "16 A"]
  answer: 1
  explanation: "Using Ohm's Law: I = V/R = 12/4 = 3 A."

- question: "If the resistance in a circuit doubles while the voltage stays the same, the current is cut in half."
  type: true-false
  answer: true
  explanation: "From I = V/R, if R doubles and V stays constant, I becomes V/(2R) = half the original current."

- question: "A current of 2 A flows through a 10 Ω resistor. What is the voltage across it?"
  type: short-answer
  answer: "20 V, because V = IR = 2 × 10 = 20 V."
  explanation: "Applying Ohm's Law directly: voltage = current × resistance = 2 A × 10 Ω = 20 V."
```

## Explainer
Georg Simon Ohm discovered a beautifully simple relationship that governs how electricity flows through materials: **V = IR**. This equation says that the voltage (V) across a component equals the current (I) through it multiplied by its resistance (R). It is the single most important equation in basic circuit analysis.

Let us revisit the water pipe analogy. If voltage is water pressure and resistance is a narrow pipe, then Ohm's Law says: **more pressure (voltage) pushes more water (current) through the pipe, and a narrower pipe (more resistance) reduces the flow (current) for the same pressure.** Mathematically, doubling the voltage doubles the current (if resistance stays the same), and doubling the resistance halves the current (if voltage stays the same).

The equation can be rearranged to solve for any of the three quantities. Need to find current? Use **I = V/R**. A 9V battery connected to a 3 Ω resistor drives I = 9/3 = 3 A of current. Need to find resistance? Use **R = V/I**. If 6V produces 2A of current, the resistance is R = 6/2 = 3 Ω. You only need to remember one form and rearrange as needed.

Ohm's Law is not just a formula to memorize — it reveals the cause-and-effect structure of circuits. The **battery** provides voltage (the cause). The **resistance** of the circuit components determines how much current will flow (the effect). Want more current? Either increase the voltage or decrease the resistance. Want to limit current to protect a sensitive component? Add more resistance. This logic drives every circuit design, from the simplest flashlight to the most complex computer chip.

It is worth noting that Ohm's Law is perfectly accurate for simple resistors but is an approximation for some real-world devices. A light bulb's resistance changes as its filament heats up. Diodes only allow current in one direction. Complex electronic components have non-linear behavior. But for the vast majority of circuit problems at this level, Ohm's Law is your go-to tool, and building an intuition for it will serve you throughout all of electrical physics.
