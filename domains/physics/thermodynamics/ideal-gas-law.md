---
id: ideal-gas-law
title: The Ideal Gas Law
domain: physics
course: thermodynamics
prerequisites:
- id: temperature-and-thermal-equilibrium
  type: hard
- id: proportional-relationships
  type: soft
builds-toward:
- kinetic-theory-of-gases
- work-in-thermodynamic-processes
- thermodynamic-processes
tags:
- ideal-gas
- gas-law
- PV-nRT
- boyles-law
- charles-law
stage: abstract-reasoning
status: validated
---

# The Ideal Gas Law

## Core Idea
The ideal gas law, PV = nRT, relates the pressure P, volume V, amount n (in moles), and absolute temperature T of an ideal gas, where R = 8.314 J/mol·K is the universal gas constant. It combines Boyle's law (P ∝ 1/V at constant T), Charles's law (V ∝ T at constant P), and Avogadro's law (V ∝ n at constant T and P). An ideal gas assumes no intermolecular forces and negligible molecular volume — a good approximation for real gases at low pressure and high temperature.

## How It's Best Learned
Derive each component law from PV = nRT by holding two variables constant at a time. Apply to practical problems like tire pressure changes with temperature and breathing mechanics. Always use absolute temperature (Kelvin) — using Celsius is a common and consequential error.

## Common Misconceptions
- Temperature in gas law calculations must be in Kelvin, not Celsius — doubling Celsius temperature does not double volume.
- The ideal gas law fails for real gases at high pressures or low temperatures where intermolecular interactions become significant.
- Increasing pressure alone does not change temperature without additional constraints on the system.

## Questions

```yaml
- question: "A sealed container of gas at 20°C is heated until its volume doubles while pressure stays constant. What must the final temperature be?"
  type: multiple-choice
  options: ["40°C", "313°C", "40 K", "293 K"]
  answer: 3
  explanation: "Charles's law (V ∝ T at constant P) requires absolute temperature. 20°C = 293 K. To double volume, temperature must double to 586 K — which is 313°C, not 40°C. Using Celsius directly is the classic mistake; doubling 20°C to 40°C would only increase volume by about 7%, not double it."

- question: "According to the ideal gas law, if you double both the pressure and the absolute temperature of a fixed amount of gas, the volume stays the same."
  type: true-false
  answer: true
  explanation: "From PV = nRT, V = nRT/P. If both T and P double, the ratio T/P is unchanged, so V is unchanged. This is a non-obvious result that highlights why all four variables must be considered together."

- question: "Why does the ideal gas law become inaccurate for real gases at very high pressures or very low temperatures?"
  type: short-answer
  answer: "At high pressures, gas molecules are packed close enough that their own volume is no longer negligible, and intermolecular attractive forces become significant — both effects the ideal gas model ignores."
  explanation: "The two core assumptions of the ideal gas model are that molecules occupy zero volume and exert no forces on each other. These hold well when molecules are far apart (low pressure, high temperature), but break down when molecules are crowded together."
```

## Explainer

You already know that temperature describes how 'hot' something is and that proportional relationships link two quantities that scale together. The ideal gas law, PV = nRT, is essentially three proportional relationships bundled into one equation: pressure and volume are inversely proportional (Boyle's Law), volume and absolute temperature are directly proportional (Charles's Law), and volume and moles of gas are directly proportional (Avogadro's Law). The constant R = 8.314 J/mol·K ties them all together into a single clean expression.

The most important thing to understand is what "ideal" means. An ideal gas is a model, not a real substance. It assumes molecules have no size and exert no forces on each other — they are just point particles bouncing around. Real gases behave like this when molecules are far apart, which happens at low pressures and high temperatures. Under those conditions, PV = nRT is remarkably accurate. When molecules are crowded together (high pressure) or moving slowly enough for attractions to matter (low temperature), the ideal model breaks down.

The single most common error in calculations is using Celsius instead of Kelvin. This is not a rounding issue — it produces completely wrong answers. Charles's Law says V doubles when T doubles, but "doubling" only makes physical sense for an absolute scale. 20°C doubled is not 40°C (a small change); it is 586 K (293 K × 2 = 586 K), which is 313°C. Always convert to Kelvin first: K = °C + 273.

To use PV = nRT in practice, identify which variables are changing and which are held constant. If n and T are fixed, you get Boyle's Law: P₁V₁ = P₂V₂. If n and P are fixed, you get Charles's Law: V₁/T₁ = V₂/T₂. If all variables change, use the full equation. The units must be consistent: pressure in Pascals, volume in cubic meters, n in moles, and T in Kelvin give energy in Joules through R.
