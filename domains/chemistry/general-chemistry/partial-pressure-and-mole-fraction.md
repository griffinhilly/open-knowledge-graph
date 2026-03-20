---
id: partial-pressure-and-mole-fraction
title: Dalton's Law of Partial Pressures
domain: chemistry
course: general-chemistry
prerequisites:
- id: gas-pressure-from-kinetic-theory
  type: hard
- id: gas-stoichiometry
  type: soft
builds-toward:
- henrys-law-gas-solubility
tags:
- partial-pressure
- daltons-law
- gas-mixtures
- mole-fraction
stage: advanced
status: draft
---

# Dalton's Law of Partial Pressures

## Core Idea
In a gas mixture, each gas exerts its own partial pressure as if it occupied the container alone; total pressure is the sum of all partial pressures. Partial pressure of a gas equals its mole fraction times the total pressure. This principle explains vapor pressure above solutions and gas collection over water.

## Explainer

From kinetic molecular theory, you know that gas pressure results from molecules colliding with container walls. In a mixture of gases — say, nitrogen and oxygen in a flask — each type of molecule bounces off the walls independently of the others. Nitrogen molecules do not "know" oxygen is present, and vice versa. **Dalton's law of partial pressures** formalizes this insight: the total pressure of a gas mixture equals the sum of the individual **partial pressures**, where each gas's partial pressure is the pressure it would exert if it alone occupied the entire container. Mathematically: P_total = P₁ + P₂ + P₃ + ...

The bridge between partial pressure and composition is the **mole fraction** (χ). The mole fraction of gas A in a mixture is simply the moles of A divided by the total moles of all gases: χ_A = n_A / n_total. Because pressure is proportional to the number of moles (from the ideal gas law, PV = nRT), the partial pressure of gas A is its mole fraction times the total pressure: P_A = χ_A × P_total. If air is 78% nitrogen by moles and atmospheric pressure is 1.00 atm, then the partial pressure of nitrogen is 0.78 × 1.00 = 0.78 atm. Note that all mole fractions in a mixture must sum to 1, and all partial pressures must sum to the total pressure — these are useful checks on your arithmetic.

A classic application is **collecting a gas over water**. When you produce hydrogen gas in a reaction and collect it by displacing water in an inverted bottle, the gas in the bottle is not pure hydrogen — it is a mixture of hydrogen and water vapor. The total pressure inside the bottle (equal to atmospheric pressure) is the sum of the partial pressure of hydrogen and the **vapor pressure of water** at the experimental temperature. To find the partial pressure of the dry hydrogen, you subtract the water's vapor pressure (looked up in a table) from the total: P_H₂ = P_total − P_H₂O. From there, you can use the ideal gas law with the partial pressure of hydrogen alone to calculate the moles of H₂ collected.

Dalton's law appears throughout chemistry and beyond. In respiratory physiology, the partial pressure of oxygen decreases at high altitude because total atmospheric pressure drops — even though the mole fraction of O₂ remains 21%. This is why climbers need supplemental oxygen. In scuba diving, increased total pressure at depth raises the partial pressure of nitrogen, increasing the amount that dissolves in blood — a direct setup for Henry's law, which you will study next. Mastering the relationship between mole fraction, partial pressure, and total pressure gives you a versatile tool for any situation involving gas mixtures.
