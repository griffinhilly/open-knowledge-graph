---
id: zeroth-law-of-thermodynamics
title: Zeroth Law of Thermodynamics
domain: physics
course: thermodynamics
prerequisites:
- id: temperature-and-thermal-equilibrium
  type: hard
builds-toward:
- thermodynamic-equilibrium-mechanical-chemical
- state-variables-and-functions
tags:
- equilibrium
- temperature
- foundational
stage: formal-systems
status: draft
---

# Zeroth Law of Thermodynamics

## Core Idea
If two systems are each in thermal equilibrium with a third system, then they are in thermal equilibrium with each other. This establishes the transitivity of thermal equilibrium and justifies the use of temperature as a well-defined property. It is the logical foundation for the concept of temperature in thermodynamics.

## How It's Best Learned
Start with simple examples: thermometer measurement, heat flow between objects, reaching equilibrium. Then formalize the logical structure and implications for defining temperature scales.

## Common Misconceptions
- Thinking the zeroth law requires heat to flow between objects.
- Confusing it with the first law (energy conservation).
- Assuming it only applies to identical materials.

## Explainer

The zeroth law is about a deceptively simple observation: thermometers work. When you place a thermometer in a cup of hot tea, it reads the temperature of the tea — not some average of the tea's temperature and its own prior temperature, or anything else complicated. It reads the tea. This happens because the thermometer and the tea reach **thermal equilibrium** with each other, which from your prerequisite study you know means their temperatures equalize and net heat flow stops. The zeroth law tells us why this measurement is meaningful beyond just those two objects in contact.

The law states: if system A is in thermal equilibrium with system C, and system B is also in thermal equilibrium with system C, then A and B must be in thermal equilibrium with each other. This is the **transitivity of thermal equilibrium**. Think of it like equality in mathematics — if A = C and B = C, then A = B. In the thermometer analogy, the thermometer is system C. If it reads 75°C after contacting your tea, and later reads 75°C after contacting a bowl of soup, you know the tea and soup are at the same temperature — even if they never touched each other.

This seems obvious, but it carries a deep consequence: it justifies temperature as a real, intrinsic, well-defined property. Without the zeroth law, "temperature" would only be meaningful as a property of a specific pair of objects in direct contact — you'd have no grounds for saying two objects have "the same" temperature unless they had directly exchanged heat. The zeroth law makes temperature something that can be consistently measured and compared across different systems, materials, and contexts.

Notice that the zeroth law does not require heat to flow between the objects being compared (A and B) — they only need to each be in equilibrium with a common third system (the thermometer). This is precisely what makes thermometry possible. It also explains why temperature scales are universal: the reading on your mercury thermometer agrees with the reading on a digital thermocouple because both instruments have reached equilibrium with the same environment, and the zeroth law guarantees that their equilibrium states are equivalent. Every temperature measurement you will ever make rests on this foundational principle.
