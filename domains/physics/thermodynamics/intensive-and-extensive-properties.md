---
id: intensive-and-extensive-properties
title: Intensive and Extensive Properties
domain: physics
course: thermodynamics
prerequisites:
- id: thermodynamic-processes
  type: soft
builds-toward:
- state-variables-and-functions
- molar-heat-capacities
tags:
- scaling
- properties
- composition
stage: formal-systems
status: draft
---

# Intensive and Extensive Properties

## Core Idea
Intensive properties (like temperature and pressure) are independent of the amount of substance in a system and remain unchanged when the system is divided into smaller parts. Extensive properties (like mass, volume, and internal energy) scale proportionally with the amount of substance and are additive for subsystems. Understanding this distinction is crucial for scaling laws and for defining specific (per-unit-mass) or molar quantities.

## How It's Best Learned
Imagine dividing a system in half: which properties remain the same? Which double? Explore molar quantities (U_m, V_m) and specific quantities (u, v). Use homogeneity of thermodynamic functions.

## Common Misconceptions
- Thinking entropy is always extensive (it is, but entropy density is intensive).
- Confusing density (intensive) with mass (extensive).
- Assuming all measurable quantities are either intensive or extensive.

## Questions

```yaml
- question: "You have a 2-liter sample of water at 50°C. You divide it into two equal 1-liter portions. Which statement correctly describes what happens?"
  type: multiple-choice
  options:
    - "Both temperature and volume remain the same in each portion"
    - "Temperature stays at 50°C in each portion; volume becomes 1 liter in each"
    - "Both temperature and volume are halved in each portion"
    - "Temperature doubles in each portion to compensate for the reduced volume"
  answer: 1
  explanation: "This is the bisection test in action. Temperature is intensive — it characterizes the state of matter at a point and does not depend on how much material is present, so each portion remains at 50°C. Volume is extensive — it scales with the amount of substance — so each portion has 1 liter. The most common mistake is thinking intensive properties also change when the system is divided."

- question: "Which of the following is an intensive property?"
  type: multiple-choice
  options:
    - "Mass"
    - "Internal energy"
    - "Entropy"
    - "Pressure"
  answer: 3
  explanation: "Pressure is intensive — it has the same value throughout a uniform system regardless of system size, and remains unchanged when you apply the bisection test. Mass, internal energy, and entropy are all extensive: they scale proportionally with the amount of substance and are halved when the system is halved. A common confusion is entropy — while entropy is extensive (total entropy scales with size), entropy density (entropy per unit volume) or molar entropy (per mole) are intensive."

- question: "If you combine two identical systems, the temperature of the combined system is twice that of each individual system."
  type: true-false
  answer: false
  explanation: "Temperature is intensive — it is independent of system size and does not add when systems are combined. If two identical 50°C water samples are combined, the result is still 50°C. Contrast this with volume, mass, or internal energy (all extensive): combining two identical systems does double those quantities. The bisection test makes this clear: temperature in each half equals the original temperature, so doubling the system can't double it either."

- question: "Entropy is an extensive property of a thermodynamic system."
  type: true-false
  answer: true
  explanation: "Entropy S is extensive: it is additive for subsystems and scales proportionally with the amount of substance. If you double the size of a system (holding intensive variables constant), the entropy doubles. This is directly expressed in the Euler relation U = TS − PV + μN, where S appears as an extensive variable multiplied by its intensive conjugate T. The common confusion is with entropy density or molar entropy (S/n), which are intensive — but those are derived quantities, not entropy itself."

- question: "Using the bisection test, explain why temperature is an intensive property while internal energy is an extensive property."
  type: short-answer
  answer: "When a system is mentally divided in half, intensive properties remain the same in each half while extensive properties are halved. Temperature characterizes the average kinetic energy per particle — this does not change when you split the system, because each half has the same molecular motion. Internal energy is the total energy of all particles; with half the particles, each half contains half the total energy. Temperature is a property of the state of matter at a point; internal energy is a property of the entire collection."
  explanation: "The bisection test is the clearest operational definition of the intensive/extensive distinction. Temperature, pressure, density, and chemical potential are intensive — they describe local state. Volume, mass, entropy, and internal energy are extensive — they describe how much. Understanding this distinction is essential for using thermodynamic equations correctly: the Euler relation and equations of state like PV = nRT can be written in intensive (per-mole) form precisely because intensive variables are independent of system size."
```

## Explainer

From your introduction to **thermodynamic processes**, you have been working with quantities like temperature, pressure, volume, and energy. Now it is time to notice a fundamental difference in how these quantities behave when you scale a system. The distinction between **extensive** and **intensive** properties is not a bookkeeping detail — it is a structural feature of thermodynamics that constrains the form every thermodynamic equation can take.

The clearest way to see the difference is the **bisection test**: mentally cut your system in half and ask what happens to each property. Temperature? Same in both halves — it does not depend on how much material is present. Pressure? Same. These are **intensive** properties: they characterize the state of matter at a point and are independent of system size. Now ask about volume: each half has half the original volume. Internal energy U? Also halved. Entropy S? Halved. Mass? Halved. These are **extensive** properties: they add up when you combine subsystems and scale proportionally with the amount of substance. Mathematically, an extensive quantity X satisfies X(λN, λV, λS, ...) = λX(N, V, S, ...) for any scale factor λ — it is a homogeneous function of degree 1 in the extensive variables.

This scaling property has a powerful consequence known as the **Euler relation** for thermodynamics. Differentiating U(λS, λV, λN) = λU with respect to λ and setting λ = 1 gives: U = TS − PV + μN, where T = ∂U/∂S, P = −∂U/∂V, and μ = ∂U/∂N are the intensive conjugate variables. This equation — expressing the total internal energy in terms of intensive variables times their extensive conjugates — holds for any simple system and is a direct consequence of extensivity. Notice that the intensive variables (T, P, μ) are the partial derivatives of the extensive variable U with respect to the other extensive variables.

In practice, you will often work with **molar quantities** (dividing an extensive property by the number of moles n) or **specific quantities** (dividing by mass m). Molar volume V_m = V/n, molar entropy S_m = S/n, and specific internal energy u = U/m are all intensive — they describe a property per unit of substance rather than of the whole system. This is why equations of state (like the ideal gas law PV = nRT) are often written as Pv = RT, where v = V/n is the molar volume: intensive variables relate to each other in equations that do not depend on how much gas you have. The intensive-versus-extensive classification is how thermodynamics achieves scale independence: the same equations describe a teaspoon of gas and a planet's atmosphere.
