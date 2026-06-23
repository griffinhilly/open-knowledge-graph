---
id: electric-current-and-resistance
title: Electric Current and Resistance
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-charge-and-coulombs-law
  type: hard
- id: electric-potential
  type: hard
- id: current-voltage-resistance
  type: soft
- id: simple-circuits
  type: soft
builds-toward:
- ohms-law
- electric-power
- dc-circuits-series-parallel
tags:
- current
- resistance
- resistivity
- drift-velocity
stage: formal-systems
status: validated
---

# Electric Current and Resistance

## Core Idea
Electric current I is the rate of charge flow through a cross-section: I = dQ/dt, measured in amperes (A = C/s). In a conductor, current arises from the drift of free electrons under an applied electric field; the drift velocity is surprisingly slow (~10⁻⁴ m/s) even though the signal propagates near the speed of light. Resistance R = ρL/A, where ρ is the material's resistivity, L is length, and A is cross-sectional area, quantifying how strongly a conductor opposes current flow.

## How It's Best Learned
Use the microscopic model (drift velocity, charge carrier density) to derive R = ρL/A from first principles. Then practice calculating R for wires of varied geometry and connect to macroscopic Ohm's law V = IR.

## Common Misconceptions
- Current is not the speed of electrons — electrons drift slowly; it is the electric field that propagates fast.
- Resistance is a property of the conductor, not the circuit. Resistivity is a property of the material.
- Conventional current direction (positive charge flow) is opposite to actual electron flow.

## Questions

```yaml
- question: "If electrons in a copper wire drift at roughly 10⁻⁴ m/s, why does a light switch appear to work instantaneously?"
  type: multiple-choice
  options:
    - "Electrons near the bulb travel faster to compensate for those farther away."
    - "The electric field propagates through the wire at near light speed, setting all free electrons in motion nearly simultaneously."
    - "Conventional current flows at light speed in the opposite direction."
    - "Only a small number of fast electrons carry all the energy."
  answer: 1
  explanation: "Current is not the speed of individual electrons — it is the rate of charge flow driven by an electric field. The field itself propagates at close to the speed of light, so all free electrons throughout the circuit begin drifting almost at once. The slow drift velocity only tells you how far each electron moves, not how quickly the signal reaches the bulb."

- question: "Doubling the cross-sectional area of a wire (keeping length and material constant) will double the wire's resistance."
  type: true-false
  answer: false
  explanation: "Resistance is R = ρL/A. Doubling the cross-sectional area A divides the resistance by two, not doubles it. A wider wire provides more parallel paths for charge flow, reducing opposition. This is directly analogous to widening a pipe to reduce flow resistance."

- question: "What is the distinction between resistivity and resistance, and why does it matter in practice?"
  type: short-answer
  answer: "Resistivity (ρ) is an intrinsic material property — it depends only on the substance and its temperature, not the shape of the conductor. Resistance (R = ρL/A) depends on both the material and the geometry. The distinction matters because you choose a material based on its resistivity, then engineer the geometry (length and area) to achieve the desired resistance for a specific application."
  explanation: "Mixing up the two leads to errors like claiming 'copper has low resistance' — copper has low resistivity, but a kilometer of thin copper wire can still have substantial resistance. Resistivity is the fundamental quantity; resistance is derived from it."
```

## Explainer

You already know from electric potential that a voltage difference (potential difference) across two points in a conductor creates an electric field inside it. That field exerts a force on the free electrons in the metal, pushing them along — but not freely. The electrons constantly collide with the vibrating lattice of metal ions, which slows them down. This perpetual collision is the microscopic origin of electrical resistance.

Because of these collisions, electrons don't accelerate indefinitely; they reach a steady average drift velocity — surprisingly slow, on the order of 10⁻⁴ m/s. Yet when you flip a light switch, the bulb responds instantly. The reason is that the electric field, not the electrons themselves, is what propagates — and it does so at nearly the speed of light. Every free electron in the entire circuit starts drifting almost simultaneously. Current, I = dQ/dt, measures how much charge passes a cross-section per second; it is a collective property of the flow, not the speed of any individual electron.

The geometry of a conductor determines how strongly it resists that flow. A longer wire means electrons must navigate more collision-prone material: R increases with length. A wider wire provides more parallel paths for electrons to travel: R decreases with cross-sectional area. Combined with the material's intrinsic resistivity ρ, these factors give the formula R = ρL/A. Resistivity is a material constant — copper has low ρ, rubber has high ρ — while resistance is a property of a specific piece of conductor with a specific shape.

One persistent source of confusion is the direction of current. By historical convention, current is defined as the direction positive charges would flow — from high to low potential. In metallic conductors, the actual charge carriers are electrons, which are negative and drift in the opposite direction. This "conventional current" convention was established before the electron was discovered, and it persists because the mathematics works out the same way. Always be explicit about which convention you are using, especially when analyzing semiconductor or electrochemical systems where positive carriers do exist.

When you encounter Ohm's law (V = IR) in the next topic, you will see resistance as the proportionality constant linking voltage and current. The groundwork you have here — that resistance arises from material properties and geometry, and that current is a flow rate rather than a particle speed — makes Ohm's law a logical consequence rather than a formula to memorize.
