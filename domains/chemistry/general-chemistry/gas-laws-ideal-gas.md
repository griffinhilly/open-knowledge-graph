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
stage: formal-systems
status: draft
---

# Gas Laws and the Ideal Gas Equation

## Core Idea
The ideal gas law, PV = nRT, relates pressure (P), volume (V), moles (n), and temperature (T) using the gas constant R. At constant conditions, Boyle's law (P ∝ 1/V), Charles's law (V ∝ T), and Avogadro's law (V ∝ n) follow. The ideal gas model assumes no intermolecular forces and negligible particle volume, valid for most gases at moderate conditions.

## Explainer

From your study of states of matter, you know that gases are distinguished by their ability to expand to fill any container, their compressibility, and the large distances between their particles. The gas laws put numbers on these behaviors by describing the mathematical relationships among four measurable quantities: **pressure (P)**, **volume (V)**, **amount in moles (n)**, and **absolute temperature (T)**.

The individual gas laws each hold one or two variables constant and describe how the remaining ones relate. **Boyle's law** says that at constant temperature and amount, pressure and volume are inversely proportional — squeeze a gas into half the volume and its pressure doubles, because the same number of molecules now hits the walls in half the space. **Charles's law** says that at constant pressure, volume is directly proportional to absolute temperature — heat a gas and it expands, because faster-moving molecules push the walls outward. **Avogadro's law** says that at constant temperature and pressure, volume is proportional to the number of moles — add more gas and the container must expand (or the pressure must rise). Each of these is a special case of a single unifying equation.

The **ideal gas law**, PV = nRT, combines all three relationships into one equation. R is the universal gas constant (0.08206 L·atm/mol·K, or 8.314 J/mol·K), and T must be in kelvins — using Celsius will give nonsensical results because the proportionalities require an absolute scale where zero means zero molecular motion. To use the equation, identify which variables are known, solve algebraically for the unknown, and plug in values with consistent units. For example, to find the volume of 2.0 moles of gas at 1.0 atm and 273 K: V = nRT/P = (2.0)(0.08206)(273)/(1.0) = 44.8 L. At standard temperature and pressure (STP: 0°C, 1 atm), one mole of any ideal gas occupies 22.4 L — a useful benchmark worth memorizing.

The ideal gas law works because it assumes two simplifications: gas molecules have **no intermolecular attractions** and occupy **negligible volume** compared to their container. These assumptions hold well at moderate temperatures and low pressures, where molecules are far apart and moving fast. They break down at high pressures (molecules are squeezed close enough that their own volume matters) and low temperatures (molecules move slowly enough that attractive forces become significant). Real gases under these conditions require corrections — the van der Waals equation adds terms for molecular volume and intermolecular attraction — but for most general chemistry problems, the ideal gas law is accurate and sufficient.
