---
id: phase-changes-and-energy
title: Phase Changes and Energy
domain: physics
course: conceptual-physics
prerequisites:
- id: heat-transfer-calculations
  type: hard
- id: temperature-vs-heat
  type: hard
- id: energy-conservation-quantitative
  type: soft
builds-toward:
- latent-heat
- phase-transitions
tags:
- phase-change
- melting
- boiling
- latent-heat
stage: abstract-reasoning
status: validated
---
# Phase Changes and Energy

## Core Idea
When a substance changes phase (solid to liquid, liquid to gas, or the reverse), it absorbs or releases energy without changing temperature. This energy, called latent heat, is used to break or form bonds between particles rather than to increase their speed. The heat of fusion is the energy needed to melt a substance, and the heat of vaporization is the energy needed to boil it. For water, vaporization requires about seven times more energy than melting.

## How It's Best Learned
Heat ice from well below 0°C and graph its temperature over time. Observe the flat plateaus where temperature stays constant during melting (0°C) and boiling (100°C) even though heat is being added continuously. Calculate the energy needed for each stage of the process.

## Common Misconceptions
- Temperature always rises when you add heat. (During a phase change, temperature stays constant. All added energy goes into changing the particle arrangement, not increasing kinetic energy.)
- Boiling water is hotter than 100°C. (At standard atmospheric pressure, water boils at 100°C and stays at 100°C throughout the boiling process, no matter how long you heat it.)
- Steam at 100°C and water at 100°C have the same energy. (Steam has much more energy because of the latent heat of vaporization absorbed during boiling — this is why steam burns are worse than hot water burns.)
- Melting and boiling require the same amount of energy. (For water, the heat of vaporization (2,260 kJ/kg) is about 6.7 times greater than the heat of fusion (334 kJ/kg). Breaking molecules completely apart requires far more energy than just loosening them.)

## Questions

```yaml
- question: "While ice is melting at 0°C, what happens to the heat energy being added?"
  type: multiple-choice
  options: ["It increases the temperature of the ice", "It escapes to the surroundings", "It breaks bonds between water molecules, changing solid to liquid", "It is stored as kinetic energy in the ice"]
  answer: 2
  explanation: "During melting, added heat energy goes into breaking the intermolecular bonds that hold the solid structure together. Temperature remains at 0°C until all the ice has melted."

- question: "Steam at 100°C can cause a worse burn than liquid water at 100°C."
  type: true-false
  answer: true
  explanation: "Steam carries additional latent heat energy (2,260 kJ/kg) that it releases when it condenses on your skin. Liquid water at 100°C does not carry this extra energy."

- question: "How much energy is needed to melt 2 kg of ice at 0°C? (Heat of fusion of water = 334 kJ/kg)"
  type: short-answer
  answer: "668 kJ, because Q = mL = 2 × 334 = 668 kJ."
  explanation: "The energy for a phase change is Q = mL, where L is the latent heat. For melting: Q = 2 kg × 334 kJ/kg = 668 kJ. This energy melts the ice without changing its temperature."
```

## Explainer
If you put a pot of ice on a stove and track its temperature with a thermometer, you will notice something surprising. The temperature rises steadily through the frozen phase, then **stops rising** when the ice begins to melt. Heat keeps flowing in from the stove, but the temperature stays stubbornly at 0°C until every last bit of ice has melted. Then the temperature starts climbing again through the liquid phase — until it reaches 100°C, where it stops once more as the water boils. Temperature holds at 100°C until all the liquid has become steam.

Those flat spots on the temperature graph reveal one of the most important ideas in thermal physics: **energy and temperature are not the same thing**. During a phase change, all the heat energy you add goes into rearranging how the molecules are connected — breaking the rigid bonds of a solid to create the flowing structure of a liquid, or tearing molecules completely free from each other to create a gas. This energy is called **latent heat** (from the Latin word for "hidden") because it is absorbed without any visible temperature change.

The energy required to melt a substance is called the **heat of fusion** (L_f). For water, it is about **334 kJ/kg** — meaning it takes 334,000 joules to melt 1 kg of ice at 0°C into water at 0°C. The energy required to boil a substance is the **heat of vaporization** (L_v). For water, this is a whopping **2,260 kJ/kg** — nearly seven times more than melting. The formula for phase-change energy is simple: **Q = mL**, where m is mass and L is the appropriate latent heat.

Why does vaporization require so much more energy? When ice melts, molecules loosen from their fixed positions but remain close together, still attracted to one another. Only some bonds are broken. When water boils, molecules must completely separate and fly apart, overcoming all remaining attractive forces. Tearing molecules completely free takes far more energy than merely loosening them.

This has practical consequences. **Steam burns** are far worse than hot water burns because when steam at 100°C condenses on your skin, it releases all that latent heat of vaporization directly into your tissue — on top of then being hot water at 100°C. Similarly, sweating cools you so effectively because each gram of sweat that evaporates absorbs about 2,260 joules of heat from your skin. Phase changes are nature's most powerful way of absorbing and releasing large quantities of energy, and understanding them is essential for everything from weather prediction to cooking to industrial cooling systems.
