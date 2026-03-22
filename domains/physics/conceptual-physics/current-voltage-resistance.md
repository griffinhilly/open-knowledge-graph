---
id: current-voltage-resistance
title: "Current, Voltage, and Resistance"
domain: physics
course: conceptual-physics
prerequisites:
- id: simple-circuits
  type: hard
- id: electric-charge-conceptual
  type: hard
- id: ratios
  type: hard
builds-toward:
- electric-current-and-resistance
tags:
- current
- voltage
- resistance
stage: abstract-reasoning
status: draft
---
# Current, Voltage, and Resistance

## Core Idea
Current is the flow of electric charge through a circuit, measured in amperes (A). Voltage is the electrical "pressure" that pushes charge through the circuit, measured in volts (V). Resistance is how much a material opposes the flow of charge, measured in ohms (Ω). These three quantities are the foundation of all circuit analysis — voltage drives current, and resistance limits it.

## How It's Best Learned
Use a water analogy: voltage is like water pressure, current is like the flow rate, and resistance is like a narrow pipe. Build a simple circuit with a battery, bulb, and wires, then swap in batteries of different voltages and bulbs of different resistances to see how brightness changes.

## Common Misconceptions
- Current is "used up" as it flows through a circuit. (Current is the same everywhere in a simple series loop. It is energy that gets used, not current.)
- Voltage is the same as current. (Voltage is the energy per unit charge — the "push." Current is the actual flow of charges. They are related but different.)
- Thicker wires have more resistance. (Thicker wires have less resistance because there is more room for electrons to flow, like a wider pipe allowing more water through.)
- Batteries store current. (Batteries store chemical energy. They create a voltage difference that drives current through a circuit.)

## Questions

```yaml
- question: "In the water pipe analogy for circuits, what does water pressure represent?"
  type: multiple-choice
  options: ["Current", "Resistance", "Voltage", "Power"]
  answer: 2
  explanation: "Voltage is the electrical 'pressure' that drives charge through the circuit, analogous to water pressure driving water through pipes."

- question: "Current is used up as it flows through a light bulb."
  type: true-false
  answer: false
  explanation: "Current entering a light bulb equals current leaving it. The bulb converts electrical energy to light and heat, but the flow of charge (current) is not consumed."

- question: "What three factors are needed to describe the basic behavior of any electric circuit?"
  type: short-answer
  answer: "Current (the flow of charge, in amps), voltage (the electrical push, in volts), and resistance (the opposition to flow, in ohms)."
  explanation: "These three quantities — current, voltage, and resistance — are the fundamental building blocks of circuit analysis, connected by Ohm's Law: V = IR."
```

## Explainer
Understanding electricity starts with three key concepts: **current**, **voltage**, and **resistance**. A helpful way to grasp all three is a water analogy. Imagine water flowing through a system of pipes. The water flow rate is like current, the water pressure is like voltage, and any narrow sections or blockages in the pipes are like resistance.

**Current** (I) is the flow of electric charge, specifically the rate at which charge passes a point in the circuit. It is measured in **amperes** (amps, A). One amp means one coulomb of charge passes by every second. In metal wires, it is electrons that flow. An important fact that surprises many students: current is not "used up" by devices in the circuit. The same current that enters a light bulb exits it. What the bulb uses is electrical energy, not the flowing charges themselves.

**Voltage** (V) is the electrical potential difference between two points — it is the energy available per unit of charge. Think of it as the "push" that drives electrons through the circuit. A 9V battery provides more push per charge than a 1.5V battery, just like a high-pressure water pump pushes water harder than a low-pressure one. Without voltage, there is no reason for charges to flow, just like water in a horizontal pipe with no pressure difference sits still.

**Resistance** (R) is the opposition a material offers to the flow of current, measured in **ohms** (Ω). A thin wire has more resistance than a thick one (less room for electrons). A long wire has more resistance than a short one (more material to push through). Materials like copper have very low resistance (good **conductors**), while materials like rubber have very high resistance (good **insulators**). The filament in an incandescent light bulb is made of high-resistance wire so that the electrical energy converts to heat and light.

These three quantities are deeply interconnected. More voltage pushes more current through the same resistance. More resistance reduces the current for the same voltage. This relationship is captured precisely by **Ohm's Law** (V = IR), which you will explore in the next topic. For now, the essential insight is that circuits are systems where voltage provides the driving force, current is the resulting flow, and resistance determines how much flow occurs for a given push.
