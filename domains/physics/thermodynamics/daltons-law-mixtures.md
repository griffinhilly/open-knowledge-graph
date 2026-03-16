---
id: daltons-law-mixtures
title: Dalton's Law of Partial Pressures
domain: physics
course: thermodynamics
prerequisites:
- id: ideal-gas-law
  type: hard
tags:
- gas-mixtures
- partial-pressure
- ideal-gas
stage: formal-systems
status: draft
---

# Dalton's Law of Partial Pressures

## Core Idea
Dalton's law states that the total pressure exerted by a mixture of ideal gases equals the sum of the partial pressures each gas would exert if it occupied the volume alone. This implies gases in a mixture behave independently and each obeys the ideal gas law with its own mole fraction.

## Explainer

From your study of the ideal gas law, you know that for a single pure gas: PV = nRT, where n is the number of moles. Pressure arises from the collective momentum transfer of gas molecules colliding with container walls. In an ideal gas, molecules are treated as point particles with no intermolecular forces — they interact only through elastic collisions. This last assumption is the key to understanding what happens when you mix two ideal gases in the same container.

Because ideal gas molecules have no intermolecular forces, the molecules of gas A are completely unaffected by the presence of molecules of gas B. Each species bounces around and hits the walls exactly as if the other species weren't there. The pressure contribution from species A depends only on how many A molecules there are and how fast they're moving — the B molecules are invisible to them. This independence is the molecular justification for Dalton's law: the total pressure is just the sum of contributions from each species, as if each were alone.

The **partial pressure** of species i is defined as Pᵢ = nᵢRT/V — the pressure that species i would exert alone in the same volume at the same temperature. Since P_total = ΣPᵢ = (Σnᵢ)RT/V = n_total·RT/V, the total pressure satisfies the ideal gas law with the total number of moles. The **mole fraction** xᵢ = nᵢ/n_total allows a clean rewrite: Pᵢ = xᵢ · P_total. For example, dry air is approximately 78% nitrogen and 21% oxygen by mole fraction. At atmospheric pressure (101.3 kPa), the partial pressure of N₂ is about 79 kPa and O₂ is about 21 kPa. These partial pressures are directly relevant to physiology — it is the partial pressure of O₂ in the alveoli that drives oxygen into the blood, not the total atmospheric pressure.

Dalton's law simplifies many practical calculations. When collecting a gas over water (a common lab technique), the collected gas is saturated with water vapor. The total pressure is P_gas + P_water vapor. Knowing the saturation vapor pressure at the collection temperature (from tables), you subtract it to find the partial pressure of the collected gas, then use PV = nRT to find the moles. Similarly, in respiratory physiology, scuba diving, and industrial gas handling, tracking partial pressures is essential — oxygen toxicity and nitrogen narcosis are partial-pressure effects, independent of whether other gases are present.

Dalton's law fails when the ideal gas approximation breaks down: at high pressures where molecular volumes and intermolecular attractions become significant, or when the gases react chemically. At high pressure, the molecules of different species do interact — through van der Waals forces or steric repulsion — and the partial pressures no longer add independently. Real gas equations of state (van der Waals, Peng-Robinson) introduce correction terms that capture these deviations. Dalton's law also cannot apply to gases that react, since the resulting mixture is chemically different from the components. But for ideal or nearly-ideal gases at moderate conditions, it is exact and extremely useful.


