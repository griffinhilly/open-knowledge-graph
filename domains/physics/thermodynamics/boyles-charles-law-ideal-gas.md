---
id: boyles-charles-law-ideal-gas
title: Boyle's and Charles' Laws for Ideal Gases
domain: physics
course: thermodynamics
prerequisites:
- id: proportions
  type: soft
builds-toward:
- ideal-gas-law
tags:
- gas-laws
- ideal-gas
- pv-behavior
stage: formal-systems
status: validated
---

# Boyle's and Charles' Laws for Ideal Gases

## Core Idea
Boyle's law states that for a fixed amount of gas at constant temperature, pressure is inversely proportional to volume (PV = constant). Charles' law states that volume is directly proportional to absolute temperature at constant pressure (V/T = constant). Together, these empirical laws reveal how gases respond to pressure and temperature changes.

## How It's Best Learned
Start with simple numerical problems fixing one variable and solving for another. Use graphs (P vs V, V vs T) to visualize the relationships.

## Common Misconceptions
- Using Celsius instead of Kelvin for temperature breaks the proportionality.
- Confusing which variable remains constant in each law.

## Questions

```yaml
- question: "A gas at 50°C is heated to 100°C at constant pressure. A student doubles the volume, reasoning that the temperature doubled. Is the student correct?"
  type: multiple-choice
  options:
    - "Yes — the temperature doubled from 50 to 100, so volume doubles by Charles' Law"
    - "No — Charles' Law only applies when pressure changes, not temperature"
    - "No — the Kelvin temperatures are 323 K and 373 K, so volume increases by a factor of 373/323, not 2"
    - "No — Boyle's Law applies here, not Charles' Law"
  answer: 2
  explanation: "The student made the classic Celsius mistake. Charles' Law requires absolute temperature (Kelvin). 50°C = 323 K and 100°C = 373 K. The temperature did NOT double — it increased by a factor of 373/323 ≈ 1.15. Only on the Kelvin scale does doubling temperature actually represent a doubling of molecular kinetic energy, making the proportionality V/T = constant valid. Using Celsius breaks the direct proportionality because 0°C is not the true zero of thermal energy."

- question: "A gas is stored in a sealed, rigid container. The container is heated. What happens to the gas pressure, and which law applies?"
  type: multiple-choice
  options:
    - "Pressure stays constant — Boyle's Law holds because volume is fixed"
    - "Boyle's Law does not apply here — it requires constant temperature, and this scenario involves changing temperature"
    - "Pressure doubles as temperature doubles, per Charles' Law"
    - "Pressure decreases as the molecules slow down and spread out"
  answer: 1
  explanation: "Boyle's Law (PV = constant) holds only when temperature is fixed. In this scenario, temperature is changing, so Boyle's Law is inapplicable. The correct framework is Gay-Lussac's Law (P/T = constant at fixed volume), which is the natural extension of Charles' Law to rigid containers. This question targets a common confusion: students sometimes apply the wrong law because they remember 'gas + pressure' without checking which variable is held constant."

- question: "A gas compressed to half its original volume at constant temperature will have twice its original pressure."
  type: true-false
  answer: true
  explanation: "This is a direct application of Boyle's Law: PV = constant (at fixed temperature and fixed amount of gas). If V is halved, then P must double to keep the product PV constant. The intuition is that the same number of molecules now occupy half the space, so they collide with the walls twice as often per unit area, doubling the pressure."

- question: "Charles' Law predicts that a gas at 0°C has zero volume."
  type: true-false
  answer: false
  explanation: "This is the Celsius trap. 0°C is NOT absolute zero — it is 273 K. Charles' Law (V/T = constant with T in Kelvin) predicts zero volume only at 0 K (absolute zero, −273°C), where molecular motion theoretically ceases. A gas at 0°C still has substantial thermal energy and a nonzero volume. The error reveals exactly why Kelvin is required: using Celsius produces nonsensical predictions because 0°C does not represent the absence of thermal energy."

- question: "Why must temperature be expressed in Kelvin rather than Celsius when applying Charles' Law?"
  type: short-answer
  answer: "Charles' Law states that volume is directly proportional to absolute temperature (V/T = constant). This proportionality only holds when temperature is measured from true zero — the point of zero thermal energy (0 K, or −273°C). The Kelvin scale starts at this absolute zero. Celsius is an offset scale where 0°C = 273 K, so ratios of Celsius temperatures don't reflect ratios of thermal energy. Doubling from 10°C to 20°C does not double the thermal energy — it corresponds to only a 3.6% increase in Kelvin."
  explanation: "The deeper point is that Charles' Law is a statement about the relationship between molecular kinetic energy and volume. Kinetic energy scales with absolute temperature, not Celsius temperature. Only when you use Kelvin does 'twice the temperature' mean 'twice the thermal energy' — and therefore predict 'twice the volume.' Any gas law involving T as a direct proportionality requires Kelvin."
```

## Explainer

You know from proportions that two quantities are inversely proportional if their product is constant, and directly proportional if their ratio is constant. Boyle's Law and Charles' Law each apply one of these relationships to a gas, and together they build the foundation for the ideal gas law.

**Boyle's Law** (1662) holds the temperature and amount of gas fixed while varying pressure and volume: PV = constant. Imagine a syringe sealed at one end. Push the plunger in — you halve the volume — and the pressure doubles. Release it and the gas pushes back. The intuition is simple: the same number of gas molecules bouncing around in half the space will hit the walls twice as often, doubling the force per unit area. Graphing P against V gives a hyperbola (P = k/V); graphing P against 1/V gives a straight line through the origin. Either graph confirms the inverse proportionality.

**Charles' Law** (1787) holds pressure and amount fixed while varying temperature and volume: V/T = constant, where T is the **absolute temperature in Kelvin**. This is the critical point: Celsius does not work here. At 0°C (273 K), doubling the temperature to 546 K should double the volume — and it does, when measured in Kelvin. If you mistakenly used Celsius, "doubling" from 0°C to 0°C is nonsensical. The Kelvin scale is the natural zero for thermal energy: 0 K is where molecular motion would theoretically cease, so V is truly proportional to T_K. The intuition is that hotter molecules move faster and push the container walls outward until equilibrium is restored at a larger volume.

Together, Boyle's and Charles' Laws say that PV/T = constant for a fixed amount of gas. Adding Avogadro's Law — that equal volumes of gas at the same T and P contain equal numbers of molecules — completes the picture and yields PV = nRT, the ideal gas law that this topic builds directly toward. Both laws are approximations that hold best at low pressures and high temperatures, where gas molecules are far apart and interactions between them are negligible. The "ideal" in ideal gas means exactly this: molecules that ignore each other except during elastic collisions.
