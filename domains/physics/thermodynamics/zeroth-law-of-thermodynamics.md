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
status: validated
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

## Questions

```yaml
- question: "A thermometer reads 80°C after being placed in a pot of soup, then reads 80°C after being placed in a cup of tea. The soup and tea have never been in direct contact. What does the zeroth law allow you to conclude?"
  type: multiple-choice
  options:
    - "Nothing — the zeroth law only applies when objects exchange heat directly"
    - "The soup and tea are at the same temperature and would be in thermal equilibrium with each other"
    - "The thermometer absorbed heat from both, so 80°C is an average of their temperatures"
    - "The soup and tea are at different temperatures, because different materials require different amounts of heat to reach 80°C"
  answer: 1
  explanation: "The zeroth law states: if A is in thermal equilibrium with C, and B is in thermal equilibrium with C, then A and B are in thermal equilibrium with each other. Here the thermometer (C) equilibrated with the soup (A) at 80°C, and with the tea (B) at 80°C. By the zeroth law, soup and tea are in thermal equilibrium — at the same temperature — even though they never contacted each other. This is precisely how a thermometer works as a universal temperature comparator."

- question: "Why does the zeroth law make temperature a 'well-defined' property rather than just a property of a specific pair of interacting objects?"
  type: multiple-choice
  options:
    - "Because it defines a numerical scale (Celsius, Kelvin) for temperature"
    - "Because it establishes transitivity of thermal equilibrium, allowing temperature to be consistently compared across different systems via a common reference"
    - "Because it states that heat flows from hot to cold, giving temperature a direction"
    - "Because it equates temperature with internal energy, making it a fundamental quantity"
  answer: 1
  explanation: "Without the zeroth law, you could only say that two objects 'have the same temperature' if they had directly exchanged heat and reached equilibrium. There would be no transitive chain connecting non-contacting objects. The zeroth law's transitivity means any object at thermal equilibrium with a reference system (a thermometer) is equivalent in temperature to all other objects at equilibrium with that reference — making temperature a consistent, universally comparable property, not a relational one."

- question: "The zeroth law requires heat to flow directly between the two objects being temperature-compared for the comparison to be valid."
  type: true-false
  answer: false
  explanation: "This is a key misconception. The zeroth law specifically describes a situation where A and B are each in thermal equilibrium with a third system C (the thermometer), but A and B need not interact directly. It is the transitivity of equilibrium — not direct heat exchange — that allows temperature comparison. In fact, the practical value of the zeroth law is precisely that it allows temperature measurement without A and B ever touching."

- question: "The zeroth law is the logical foundation that justifies using a thermometer to assign a numerical temperature to any object."
  type: true-false
  answer: true
  explanation: "The thermometer works by reaching thermal equilibrium with the object being measured (the thermometer's reading corresponds to its own equilibrium state with C). The zeroth law then guarantees that any two objects both at equilibrium with the thermometer at the same reading are at equilibrium with each other. This gives temperature its meaning as an objective, transitive property — every thermometer-based temperature measurement relies on this reasoning, whether explicitly stated or not."

- question: "Explain how the zeroth law justifies using a thermometer to compare the temperatures of two objects that never directly contact each other."
  type: short-answer
  answer: "The zeroth law establishes that thermal equilibrium is transitive. If object A reaches thermal equilibrium with the thermometer (both settle at the same temperature, no net heat flow), and object B separately reaches thermal equilibrium with the thermometer at the same reading, then by the zeroth law, A and B are in thermal equilibrium with each other — meaning they are at the same temperature. The thermometer acts as the 'common third system' that the law describes. A and B never need to touch; their shared equilibrium with the thermometer is sufficient."
  explanation: "Without transitivity, each temperature comparison would require the two objects to exchange heat directly, making universal temperature measurement impossible. The zeroth law is what lets a single thermometer serve as a universal comparator across all materials and systems."
```

## Explainer

The zeroth law is about a deceptively simple observation: thermometers work. When you place a thermometer in a cup of hot tea, it reads the temperature of the tea — not some average of the tea's temperature and its own prior temperature, or anything else complicated. It reads the tea. This happens because the thermometer and the tea reach **thermal equilibrium** with each other, which from your prerequisite study you know means their temperatures equalize and net heat flow stops. The zeroth law tells us why this measurement is meaningful beyond just those two objects in contact.

The law states: if system A is in thermal equilibrium with system C, and system B is also in thermal equilibrium with system C, then A and B must be in thermal equilibrium with each other. This is the **transitivity of thermal equilibrium**. Think of it like equality in mathematics — if A = C and B = C, then A = B. In the thermometer analogy, the thermometer is system C. If it reads 75°C after contacting your tea, and later reads 75°C after contacting a bowl of soup, you know the tea and soup are at the same temperature — even if they never touched each other.

This seems obvious, but it carries a deep consequence: it justifies temperature as a real, intrinsic, well-defined property. Without the zeroth law, "temperature" would only be meaningful as a property of a specific pair of objects in direct contact — you'd have no grounds for saying two objects have "the same" temperature unless they had directly exchanged heat. The zeroth law makes temperature something that can be consistently measured and compared across different systems, materials, and contexts.

Notice that the zeroth law does not require heat to flow between the objects being compared (A and B) — they only need to each be in equilibrium with a common third system (the thermometer). This is precisely what makes thermometry possible. It also explains why temperature scales are universal: the reading on your mercury thermometer agrees with the reading on a digital thermocouple because both instruments have reached equilibrium with the same environment, and the zeroth law guarantees that their equilibrium states are equivalent. Every temperature measurement you will ever make rests on this foundational principle.
