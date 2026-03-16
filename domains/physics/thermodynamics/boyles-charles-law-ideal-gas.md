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
status: draft
---

# Boyle's and Charles' Laws for Ideal Gases

## Core Idea
Boyle's law states that for a fixed amount of gas at constant temperature, pressure is inversely proportional to volume (PV = constant). Charles' law states that volume is directly proportional to absolute temperature at constant pressure (V/T = constant). Together, these empirical laws reveal how gases respond to pressure and temperature changes.

## How It's Best Learned
Start with simple numerical problems fixing one variable and solving for another. Use graphs (P vs V, V vs T) to visualize the relationships.

## Common Misconceptions
- Using Celsius instead of Kelvin for temperature breaks the proportionality.
- Confusing which variable remains constant in each law.

## Explainer

You know from proportions that two quantities are inversely proportional if their product is constant, and directly proportional if their ratio is constant. Boyle's Law and Charles' Law each apply one of these relationships to a gas, and together they build the foundation for the ideal gas law.

**Boyle's Law** (1662) holds the temperature and amount of gas fixed while varying pressure and volume: PV = constant. Imagine a syringe sealed at one end. Push the plunger in — you halve the volume — and the pressure doubles. Release it and the gas pushes back. The intuition is simple: the same number of gas molecules bouncing around in half the space will hit the walls twice as often, doubling the force per unit area. Graphing P against V gives a hyperbola (P = k/V); graphing P against 1/V gives a straight line through the origin. Either graph confirms the inverse proportionality.

**Charles' Law** (1787) holds pressure and amount fixed while varying temperature and volume: V/T = constant, where T is the **absolute temperature in Kelvin**. This is the critical point: Celsius does not work here. At 0°C (273 K), doubling the temperature to 546 K should double the volume — and it does, when measured in Kelvin. If you mistakenly used Celsius, "doubling" from 0°C to 0°C is nonsensical. The Kelvin scale is the natural zero for thermal energy: 0 K is where molecular motion would theoretically cease, so V is truly proportional to T_K. The intuition is that hotter molecules move faster and push the container walls outward until equilibrium is restored at a larger volume.

Together, Boyle's and Charles' Laws say that PV/T = constant for a fixed amount of gas. Adding Avogadro's Law — that equal volumes of gas at the same T and P contain equal numbers of molecules — completes the picture and yields PV = nRT, the ideal gas law that this topic builds directly toward. Both laws are approximations that hold best at low pressures and high temperatures, where gas molecules are far apart and interactions between them are negligible. The "ideal" in ideal gas means exactly this: molecules that ignore each other except during elastic collisions.
