---
id: molar-heat-capacities
title: Molar Heat Capacities and Their Relations
domain: physics
course: thermodynamics
prerequisites:
- id: heat-capacity-of-gases
  type: hard
- id: degrees-of-freedom-polyatomic
  type: soft
- id: intensive-and-extensive-properties
  type: soft
builds-toward:
  - third-law-absolute-entropy
tags:
- heat-capacity
- properties
- measurement
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "You add 1000 J of heat to 1 mol of an ideal monatomic gas at constant volume, then repeat the experiment at constant pressure. Which process produces a larger temperature increase?"
  type: multiple-choice
  options:
    - "Constant pressure — the gas is free to expand, so it absorbs heat more efficiently"
    - "Constant volume — all the heat goes into raising internal energy with none lost to work"
    - "Both processes produce the same temperature increase because the same heat is added"
    - "Constant pressure — higher pressure means higher temperature at any given energy input"
  answer: 1
  explanation: "At constant volume no expansion work is done, so all 1000 J raises internal energy and temperature: ΔT = Q/(nC_V). At constant pressure, the gas expands and does PdV work on its surroundings; only the fraction that goes into internal energy raises temperature. Since C_P = C_V + R > C_V, the same 1000 J produces a smaller ΔT = Q/(nC_P). The common misconception is that 'free to expand' sounds like an advantage — in fact, the expansion leaks energy away from temperature increase."

- question: "The relation C_P − C_V = R for an ideal gas arises because at constant pressure, the gas must:"
  type: multiple-choice
  options:
    - "Overcome stronger intermolecular attractions that resist heating"
    - "Do additional work against the surroundings as it expands, requiring extra heat beyond what raises internal energy"
    - "Absorb more photons due to the increased collision frequency at constant pressure"
    - "Partially convert heat into potential energy stored in the pressure field"
  answer: 1
  explanation: "For an ideal gas at constant pressure, the first law gives dQ = dU + PdV. Since PV = RT for one mole, PdV = R dT at constant pressure. Therefore dQ = C_V dT + R dT, giving C_P = C_V + R. The extra R worth of heat per mole per kelvin compensates for the PdV work done against the surroundings. For real substances (solids, liquids) α is very small so C_P ≈ C_V, but for gases the R correction is essential."

- question: "For an ideal gas, heating at constant pressure and heating at constant volume by the same amount of energy produce the same temperature rise."
  type: true-false
  answer: false
  explanation: "False. At constant pressure, some of the energy goes into PdV work as the gas expands, so less is available to raise the temperature. The temperature rise at constant pressure is ΔT = Q/(nC_P), while at constant volume it is ΔT = Q/(nC_V). Since C_P > C_V (by exactly R for ideal gases), constant-pressure heating produces a smaller temperature rise for the same heat input."

- question: "The ratio γ = C_P/C_V is greater than 1 for all ideal gases."
  type: true-false
  answer: true
  explanation: "True. Since C_P = C_V + R and R > 0, we always have C_P > C_V, so γ > 1 for any ideal gas. For monatomic ideal gases (3 translational degrees of freedom), C_V = (3/2)R and γ = 5/3 ≈ 1.67. For diatomic gases at moderate temperatures (5 degrees of freedom), C_V = (5/2)R and γ = 7/5 = 1.4. The value of γ matters for adiabatic processes and determines the speed of sound in a gas."

- question: "Explain physically why heating one mole of an ideal gas at constant pressure requires more energy than heating the same gas by the same temperature increment at constant volume."
  type: short-answer
  answer: "At constant volume, no expansion work is done — all added heat goes directly into raising the internal energy and temperature of the gas. At constant pressure, the gas expands as it heats, and that expanding gas does work (PdV) on the surroundings. This work output must be supplied in addition to the energy that goes into raising the temperature, so the total heat required is larger. The extra energy cost per mole per kelvin is exactly R — the gas constant — giving C_P = C_V + R."
  explanation: "The first law ΔU = Q − W makes this concrete: at constant volume W = 0, so Q = ΔU = nC_V ΔT. At constant pressure W = PΔV = nRΔT, so Q = ΔU + W = nC_V ΔT + nR ΔT = n(C_V + R)ΔT = nC_P ΔT. The R term is the work done on the surroundings. This is why an open beaker (constant pressure) requires more heat to reach the same temperature than a sealed rigid vessel (constant volume)."
```

## Explainer

From heat capacity of gases, you know that C_V is the heat required to raise one mole's temperature by one degree at constant volume, and C_P is the same at constant pressure. You probably computed C_V = (3/2)R for a monatomic ideal gas and C_P = (5/2)R. The gap of R between them has a clean physical origin, and understanding it reveals something important about what heat actually does.

At **constant volume**, all the heat you add goes directly into raising the internal energy: dU = nC_V dT, with no expansion work done. At **constant pressure**, the gas expands as it heats, and the expanding gas does work on its surroundings: dQ = dU + PdV. For one mole of ideal gas, PV = RT, so at constant pressure PdV = RdT. Therefore dQ = C_V dT + R dT, giving **C_P = C_V + R**. The extra R worth of heat at constant pressure goes into work against the atmosphere, not into raising the temperature. This is why heating a gas in an open container (constant pressure) is less efficient at raising temperature than heating it in a sealed rigid container (constant volume).

For **real substances** the relation generalizes to C_P − C_V = TVα²/κ_T, where α is the isobaric thermal expansion coefficient and κ_T is the isothermal compressibility. For solids and liquids, α is small, making C_P ≈ C_V — practical tables for condensed phases often list only C_P (which is what calorimetry measures at atmospheric pressure) and treat it as identical to C_V. For gases, the full R correction matters. The **ratio γ = C_P/C_V** (the adiabatic index) determines the speed of sound and the behavior of adiabatic compression: for monatomic ideal gas γ = 5/3, for diatomic γ = 7/5 at moderate temperatures.

The temperature dependence of molar heat capacities is where classical theory breaks down and quantum mechanics becomes essential. The **Einstein model** treated each atom in a solid as an independent harmonic oscillator of frequency ω, giving a heat capacity that correctly approaches 3R at high T (the Dulong-Petit law) and drops to zero as T → 0 — consistent with the third law of thermodynamics, which requires C → 0 as T → 0 (otherwise S = ∫(C/T)dT would diverge). The **Debye model** improves this by treating the solid as a spectrum of phonon modes, getting the correct low-T behavior C ∝ T³. At very low temperatures in metals, electronic contributions add a linear term, giving C = γ_el T + A T³ — the linear term comes from the quantum Fermi gas of electrons, not classical equipartition.
