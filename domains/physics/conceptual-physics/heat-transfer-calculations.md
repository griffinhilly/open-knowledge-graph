---
id: heat-transfer-calculations
title: "Heat Transfer Calculations: Q = mcΔT"
domain: physics
course: conceptual-physics
prerequisites:
- id: specific-heat-capacity-conceptual
  type: hard
- id: two-step-equations
  type: hard
builds-toward:
- specific-heat-capacity
- calorimetry
tags:
- heat-transfer
- calculation
stage: abstract-reasoning
status: validated
---
# Heat Transfer Calculations: Q = mcΔT

## Core Idea
The heat energy transferred to or from an object is calculated using Q = mcΔT, where Q is heat in joules, m is mass in kilograms, c is specific heat capacity in J/(kg·°C), and ΔT is the change in temperature in °C. This equation lets you calculate how much energy is needed to heat something up, or how much energy a cooling object releases. The formula works in both directions — heating (positive Q) and cooling (negative Q).

## How It's Best Learned
Calculate how much energy is needed to heat a pot of water from room temperature to boiling. Compare the energy needed to heat the same mass of water vs. aluminum to the same temperature. Work through problems where two substances at different temperatures are mixed and find the final temperature.

## Common Misconceptions
- ΔT means the final temperature. (ΔT is the change in temperature: T_final - T_initial. A 20°C rise in temperature has a ΔT of 20, regardless of the starting temperature.)
- More mass always means higher final temperature. (More mass means more energy is needed to achieve the same temperature change. With a fixed amount of heat, more mass results in a smaller temperature rise.)
- You can use this formula to calculate the temperature during a phase change. (During phase changes like melting or boiling, temperature stays constant even as heat is added. Q = mcΔT only works when temperature is changing.)
- Negative Q means the calculation is wrong. (Negative Q simply means the object is releasing heat — cooling down rather than heating up.)

## Questions

```yaml
- question: "How much heat is needed to raise the temperature of 2 kg of water from 20°C to 70°C? (c_water = 4,186 J/kg·°C)"
  type: multiple-choice
  options: ["418,600 J", "8,372 J", "293,020 J", "585,040 J"]
  answer: 0
  explanation: "Q = mcΔT = 2 × 4,186 × (70 - 20) = 2 × 4,186 × 50 = 418,600 J."

- question: "If Q is negative in the equation Q = mcΔT, it means the object is losing heat energy."
  type: true-false
  answer: true
  explanation: "A negative Q indicates the object's temperature decreased (negative ΔT), meaning it released heat energy to its surroundings."

- question: "0.5 kg of iron (c = 450 J/kg·°C) absorbs 9,000 J of heat. What is its temperature change?"
  type: short-answer
  answer: "40°C, because ΔT = Q/(mc) = 9,000/(0.5 × 450) = 9,000/225 = 40°C."
  explanation: "Rearranging Q = mcΔT gives ΔT = Q/(mc) = 9,000/(0.5 × 450) = 40°C."
```

## Explainer
Now that you understand specific heat capacity — the idea that different materials need different amounts of energy per kilogram per degree — the formula **Q = mcΔT** puts that idea into precise mathematical form. This single equation lets you calculate the heat energy involved in any temperature change.

Let us break it down. **Q** is the heat energy in joules (the energy transferred into or out of the substance). **m** is the mass of the substance in kilograms. **c** is the specific heat capacity (a number you look up for each material). **ΔT** (delta T) is the temperature change — final temperature minus initial temperature. If the object heats up, ΔT is positive and Q is positive (energy flows in). If the object cools down, ΔT is negative and Q is negative (energy flows out).

Here is a practical example. Suppose you want to heat 1.5 kg of water from 25°C to 100°C for cooking. The specific heat of water is 4,186 J/(kg·°C), and the temperature change is ΔT = 100 - 25 = 75°C. Plugging in: Q = 1.5 × 4,186 × 75 = **470,925 J** — nearly half a million joules just to boil a pot of water. This is why electric kettles draw so much power and why it takes several minutes to boil water on a stove.

The equation can be rearranged to find any unknown. Need the final temperature? Solve for ΔT = Q/(mc), then add ΔT to the initial temperature. Need to find the specific heat of an unknown material? Measure Q, m, and ΔT, then calculate c = Q/(mΔT). This rearrangement is the basis of **calorimetry** — the science of measuring heat.

One of the most common applications involves mixing two substances at different temperatures. If you pour 0.5 kg of hot water (80°C) into 0.5 kg of cold water (20°C), the hot water loses heat and the cold water gains heat until they reach the same final temperature. By conservation of energy, the heat lost by the hot water equals the heat gained by the cold water: m₁c₁ΔT₁ = m₂c₂ΔT₂. Since both are water (same c and same m), they meet in the middle at 50°C. If the masses or materials differ, the final temperature shifts toward the substance with more thermal "capacity" — either more mass or higher specific heat.

Remember that Q = mcΔT only works when the substance is changing temperature, not when it is changing phase (melting, boiling, or freezing). During a phase change, temperature stays constant even as heat flows in or out. That situation requires a different equation, which you will encounter in the topic on phase changes and energy.
