---
id: molar-heat-capacities
title: Molar Heat Capacities and Their Relations
domain: physics
course: thermodynamics
prerequisites:
- id: heat-capacity-of-gases
  type: hard
builds-toward:
- degrees-of-freedom-polyatomic
- third-law-absolute-entropy
tags:
- heat-capacity
- properties
- measurement
stage: formal-systems
status: draft
---

# Molar Heat Capacities and Their Relations

## Core Idea
Molar heat capacity C_m = dQ/(n dT) is the heat required per mole to raise temperature by one degree; C_p (constant pressure) and C_v (constant volume) are the two most important forms. The relation C_p - C_v = R for ideal gases and more generally C_p - C_v = -T(∂P/∂T)_V^2/(∂P/∂V)_T holds for all substances. Molar heat capacities are temperature-dependent for real substances and are essential for calculating energy transfers in thermodynamic processes.

## How It's Best Learned
Measure C_p and C_v for common gases and liquids. Verify the relation C_p - C_v = R experimentally. Plot temperature dependence of heat capacities.

## Common Misconceptions
- Assuming C_p and C_v are always constant (they vary with temperature).
- Confusing molar heat capacity C_m with specific heat capacity c = C_m/M.
- Thinking C_p > C_v always (true, but the difference size varies greatly).

## Explainer

From heat capacity of gases, you know that C_V is the heat required to raise one mole's temperature by one degree at constant volume, and C_P is the same at constant pressure. You probably computed C_V = (3/2)R for a monatomic ideal gas and C_P = (5/2)R. The gap of R between them has a clean physical origin, and understanding it reveals something important about what heat actually does.

At **constant volume**, all the heat you add goes directly into raising the internal energy: dU = nC_V dT, with no expansion work done. At **constant pressure**, the gas expands as it heats, and the expanding gas does work on its surroundings: dQ = dU + PdV. For one mole of ideal gas, PV = RT, so at constant pressure PdV = RdT. Therefore dQ = C_V dT + R dT, giving **C_P = C_V + R**. The extra R worth of heat at constant pressure goes into work against the atmosphere, not into raising the temperature. This is why heating a gas in an open container (constant pressure) is less efficient at raising temperature than heating it in a sealed rigid container (constant volume).

For **real substances** the relation generalizes to C_P − C_V = TVα²/κ_T, where α is the isobaric thermal expansion coefficient and κ_T is the isothermal compressibility. For solids and liquids, α is small, making C_P ≈ C_V — practical tables for condensed phases often list only C_P (which is what calorimetry measures at atmospheric pressure) and treat it as identical to C_V. For gases, the full R correction matters. The **ratio γ = C_P/C_V** (the adiabatic index) determines the speed of sound and the behavior of adiabatic compression: for monatomic ideal gas γ = 5/3, for diatomic γ = 7/5 at moderate temperatures.

The temperature dependence of molar heat capacities is where classical theory breaks down and quantum mechanics becomes essential. The **Einstein model** treated each atom in a solid as an independent harmonic oscillator of frequency ω, giving a heat capacity that correctly approaches 3R at high T (the Dulong-Petit law) and drops to zero as T → 0 — consistent with the third law of thermodynamics, which requires C → 0 as T → 0 (otherwise S = ∫(C/T)dT would diverge). The **Debye model** improves this by treating the solid as a spectrum of phonon modes, getting the correct low-T behavior C ∝ T³. At very low temperatures in metals, electronic contributions add a linear term, giving C = γ_el T + A T³ — the linear term comes from the quantum Fermi gas of electrons, not classical equipartition.
