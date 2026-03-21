---
id: gas-laws-ideal-gas
title: Gas Laws and the Ideal Gas Equation
domain: chemistry
course: general-chemistry
prerequisites:
- id: states-of-matter-phase-changes
  type: hard
- id: kinetic-molecular-theory
  type: soft
builds-toward:
- gas-stoichiometry
- kinetic-molecular-theory
tags:
- gas laws
- ideal gas equation
- PV = nRT
- pressure
- volume
stage: advanced
status: draft
---

# Gas Laws and the Ideal Gas Equation

## Core Idea
The ideal gas law, PV = nRT, relates pressure (P), volume (V), moles (n), and temperature (T) using the gas constant R. At constant conditions, Boyle's law (P ∝ 1/V), Charles's law (V ∝ T), and Avogadro's law (V ∝ n) follow. The ideal gas model assumes no intermolecular forces and negligible particle volume, valid for most gases at moderate conditions.

## Questions

```yaml
- question: "A student wants to find the volume of 1.0 mol of gas at 27°C and 1.0 atm. She plugs in T = 27 into PV = nRT and gets V = (1.0)(0.08206)(27)/(1.0) = 2.22 L. A classmate uses T = 300 K and gets V = 24.6 L. Who is correct, and why?"
  type: multiple-choice
  options:
    - "The first student — Celsius is more precise and the gas constant was measured in Celsius"
    - "The classmate — temperature must be in Kelvin because the proportionalities in the gas laws require an absolute scale"
    - "Both are valid approximations depending on the context; at room temperature the difference is negligible"
    - "Neither — the calculation requires converting to Fahrenheit first when using the R = 0.08206 constant"
  answer: 1
  explanation: "Temperature must always be in Kelvin when using the ideal gas law. Charles's law says V ∝ T — this proportionality only holds when T is on an absolute scale starting at absolute zero (0 K = −273°C). If T = 0°C were substituted, V = 0 would be predicted, which is nonsensical. The Celsius scale's zero is arbitrary, not physically meaningful. 27°C = 300 K is the correct conversion, giving V ≈ 24.6 L, close to the 22.4 L/mol benchmark at 0°C (273 K)."

- question: "Under which conditions does the ideal gas law become least accurate, and what physical properties of real gases cause the deviations?"
  type: multiple-choice
  options:
    - "At high temperature and low pressure — molecules move too fast for the model to apply"
    - "At low temperature and high pressure — molecules are close enough that their own volume matters and intermolecular attractions become significant"
    - "At high temperature and high pressure — the gas constant R changes at extreme conditions"
    - "The ideal gas law is equally accurate at all conditions for monatomic gases like helium"
  answer: 1
  explanation: "The ideal gas law assumes two things: molecules occupy negligible volume compared to the container, and there are no intermolecular forces. Both assumptions break down at high pressure (molecules are squeezed together, so their own volume is no longer negligible) and low temperature (molecules move slowly enough that attractive forces significantly influence behavior). Real gases deviate most from ideality under these conditions, which is why van der Waals corrections add terms for molecular volume (b) and intermolecular attraction (a)."

- question: "A gas at high temperature and low pressure behaves more like a real gas (deviates from ideal behavior) than the same gas at low temperature and high pressure."
  type: true-false
  answer: false
  explanation: "It's the opposite: high temperature and low pressure is where ideal gas behavior is most accurate. At high temperature, molecules have enough kinetic energy to overcome intermolecular attractions (making attractions negligible). At low pressure, molecules are far apart, so their own volume is negligible compared to container volume. Low temperature and high pressure bring molecules close together, where both their finite volume and mutual attractions become significant deviations from the ideal assumptions."

- question: "Boyle's law (P ∝ 1/V), Charles's law (V ∝ T), and Avogadro's law (V ∝ n) are all special cases of PV = nRT obtained by holding different variables constant."
  type: true-false
  answer: true
  explanation: "The ideal gas law unifies all three: hold n and T constant and you get PV = constant (Boyle's law); hold n and P constant and you get V/T = constant (Charles's law); hold P and T constant and you get V/n = constant (Avogadro's law). They are not separate empirical laws — they are mathematical consequences of the same equation under different constrained conditions. This is why they all fail under the same conditions: when the ideal gas assumptions break down, all three fail simultaneously."

- question: "Why must temperature be expressed in Kelvin — not Celsius or Fahrenheit — when using the ideal gas law? What goes wrong mathematically and physically if you use Celsius?"
  type: short-answer
  answer: "The gas laws express direct proportionalities: V ∝ T (Charles's law) and PV ∝ T (ideal gas law). These proportionalities only hold on an absolute scale where zero means zero molecular kinetic energy. Kelvin is that scale: 0 K corresponds to no thermal motion. If you substitute T = 0°C into PV = nRT, you get V = 0 (gas disappears) — physically nonsensical. If you double the Celsius temperature from 10°C to 20°C, the ideal gas law predicts volume increases by a factor of 293/283 ≈ 1.035, not 2 — because you must double the Kelvin temperature (286 K to 572 K) to double the volume. Using Celsius gives the wrong proportionality and a numerically wrong answer."
  explanation: "This is the most common calculation error with gas laws. The Celsius scale's zero is arbitrary (the freezing point of water), not physically meaningful. Kelvin zero is physically grounded. Any time you see T in a thermodynamics formula expressing proportionality or ratio, it means Kelvin."
```

## Explainer

From your study of states of matter, you know that gases are distinguished by their ability to expand to fill any container, their compressibility, and the large distances between their particles. The gas laws put numbers on these behaviors by describing the mathematical relationships among four measurable quantities: **pressure (P)**, **volume (V)**, **amount in moles (n)**, and **absolute temperature (T)**.

The individual gas laws each hold one or two variables constant and describe how the remaining ones relate. **Boyle's law** says that at constant temperature and amount, pressure and volume are inversely proportional — squeeze a gas into half the volume and its pressure doubles, because the same number of molecules now hits the walls in half the space. **Charles's law** says that at constant pressure, volume is directly proportional to absolute temperature — heat a gas and it expands, because faster-moving molecules push the walls outward. **Avogadro's law** says that at constant temperature and pressure, volume is proportional to the number of moles — add more gas and the container must expand (or the pressure must rise). Each of these is a special case of a single unifying equation.

The **ideal gas law**, PV = nRT, combines all three relationships into one equation. R is the universal gas constant (0.08206 L·atm/mol·K, or 8.314 J/mol·K), and T must be in kelvins — using Celsius will give nonsensical results because the proportionalities require an absolute scale where zero means zero molecular motion. To use the equation, identify which variables are known, solve algebraically for the unknown, and plug in values with consistent units. For example, to find the volume of 2.0 moles of gas at 1.0 atm and 273 K: V = nRT/P = (2.0)(0.08206)(273)/(1.0) = 44.8 L. At standard temperature and pressure (STP: 0°C, 1 atm), one mole of any ideal gas occupies 22.4 L — a useful benchmark worth memorizing.

The ideal gas law works because it assumes two simplifications: gas molecules have **no intermolecular attractions** and occupy **negligible volume** compared to their container. These assumptions hold well at moderate temperatures and low pressures, where molecules are far apart and moving fast. They break down at high pressures (molecules are squeezed close enough that their own volume matters) and low temperatures (molecules move slowly enough that attractive forces become significant). Real gases under these conditions require corrections — the van der Waals equation adds terms for molecular volume and intermolecular attraction — but for most general chemistry problems, the ideal gas law is accurate and sufficient.
