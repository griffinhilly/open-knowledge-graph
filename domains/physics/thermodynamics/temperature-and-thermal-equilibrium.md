---
id: temperature-and-thermal-equilibrium
title: Temperature and Thermal Equilibrium
domain: physics
course: thermodynamics
prerequisites: []
builds-toward:
- thermal-expansion
- heat-and-internal-energy
- ideal-gas-law
- heat-transfer-conduction
tags:
- temperature
- thermal-equilibrium
- zeroth-law
- thermometry
stage: concrete-operations
status: validated
---

# Temperature and Thermal Equilibrium

## Core Idea
Temperature is a measure of the average thermal energy of particles in a system, and two objects in thermal contact will eventually reach the same temperature — a state called thermal equilibrium. The Zeroth Law of Thermodynamics formalizes this: if object A is in thermal equilibrium with object B, and B is in equilibrium with C, then A and C are also in equilibrium with each other. This law provides the logical foundation for thermometry. Common temperature scales include Celsius, Fahrenheit, and the absolute Kelvin scale, where 0 K is absolute zero.

## How It's Best Learned
Compare thermometer readings in different scales and practice converting between Celsius, Fahrenheit, and Kelvin. Think carefully about why temperature is not the same as heat — a large cold lake has more total thermal energy than a small cup of boiling water, yet the cup is at a higher temperature.

## Common Misconceptions
- Temperature and heat are not the same quantity; temperature is an intensive property (independent of amount), while heat is energy in transit.
- Absolute zero (0 K) is not just 'very cold' — it represents the theoretical minimum of thermal energy; no object can reach it in practice.
- 'Hotter' does not mean 'more energy stored' without knowing the mass and material.

## Questions

```yaml
- question: "A large lake at 10°C and a small cup of water at 100°C are compared. Which contains more total thermal energy?"
  type: multiple-choice
  options: ["The cup, because it is at a higher temperature", "The lake, because it has far more mass", "They have the same energy because energy is conserved", "It is impossible to say without knowing the cup material"]
  answer: 1
  explanation: "Temperature is an intensive property — it measures the average thermal energy per particle, not the total. The lake contains an enormous number of molecules, each carrying thermal energy, so its total thermal energy vastly exceeds that of the small hot cup. This distinction between temperature (intensive) and total thermal energy (extensive) is fundamental to thermodynamics."

- question: "Temperature and heat are the same physical quantity, just measured in different units."
  type: true-false
  answer: false
  explanation: "Temperature and heat are entirely different concepts. Temperature is an intensive property describing the average kinetic energy of particles in a system — it does not depend on the amount of material. Heat is energy in transit: it flows from a hotter object to a cooler one during thermal contact. You can raise temperature without adding heat (by doing work on a system), and you can add heat without changing temperature (during a phase change like melting ice)."

- question: "What does the Zeroth Law of Thermodynamics establish, and why is it called 'zeroth' rather than 'first'?"
  type: short-answer
  answer: "The Zeroth Law states that if A is in thermal equilibrium with B, and B is in thermal equilibrium with C, then A and C are in thermal equilibrium. It is called 'zeroth' because it was identified after the First and Second Laws were already named, yet it is logically prior to both — it is what makes temperature a consistent, transitive property and gives thermometry its foundation."
  explanation: "Without the Zeroth Law, thermometers would not work reliably: the whole premise of a thermometer is that it reaches equilibrium with whatever it touches, and its reading can then be compared to readings from other objects. The Zeroth Law formalizes the transitivity of thermal equilibrium that underpins all temperature measurement."
```

## Explainer

Temperature is something you experience constantly — you know a hot stove is hotter than a cold room — but the physical definition is more precise than intuition suggests. Temperature measures the average kinetic energy of the particles in a substance. In a gas, this is the average energy of molecules bouncing around; in a solid, it is the average energy of atoms vibrating in place. Because it is an average per particle, temperature does not depend on how much of the substance you have: a single drop of boiling water and a full pot of boiling water are both at 100°C, even though the pot contains vastly more total energy.

This is the key distinction between temperature (intensive — does not scale with amount) and heat (energy in transit). When two objects at different temperatures are brought into contact, energy flows from the hotter to the cooler object as heat, until both reach the same temperature. That endpoint is thermal equilibrium. The Zeroth Law of Thermodynamics formalizes this into a transitivity principle: if A is in equilibrium with B, and B is in equilibrium with C, then A and C must also be in equilibrium. This seemingly obvious statement is actually what justifies thermometry — a thermometer works because it reaches equilibrium with whatever it touches, and the reading can be meaningfully compared across measurements.

Temperature scales all agree on the physical state they mark, but differ in their zero points and step sizes. Celsius sets 0° at the freezing point and 100° at the boiling point of water. Fahrenheit uses a different zero and a smaller step size. The Kelvin scale is the scientifically fundamental one: its zero point, 0 K (−273.15°C), is absolute zero — the theoretical state where particles have minimum possible thermal energy. No real object can reach 0 K, and in practice objects can only approach it asymptotically. Converting between Kelvin and Celsius is simple: K = °C + 273.15. Many physics equations require temperature in Kelvin, so knowing this conversion is essential.

A persistent misconception is that a hotter object always contains more energy. The massive cold lake example makes this concrete: even though the lake is much cooler than a cup of boiling water, its sheer mass gives it far more total thermal energy. When you encounter temperature in future topics — ideal gas law, heat transfer, thermodynamic cycles — always ask whether you need the intensive property (temperature) or the total energy content, because they answer different questions.
