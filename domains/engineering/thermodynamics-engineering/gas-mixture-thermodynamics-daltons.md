---
id: gas-mixture-thermodynamics-daltons
title: Gas Mixture Thermodynamics and Dalton's Law
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: gas-mixtures-partial-pressures-daltons-law
  type: hard
- id: ideal-real-gas-equations-state
  type: soft
builds-toward:
- partial-molar-properties-mixtures
- humid-air-thermodynamic-properties
- combustion-stoichiometry-energy-release
tags:
- mixtures
- daltons-law
- partial-pressure
- mole-fraction
stage: advanced
status: draft
---

# Gas Mixture Thermodynamics and Dalton's Law

## Core Idea
For ideal gases, Dalton's law states total pressure P = Σ P_i (partial pressures), and mole fraction x_i = P_i/P. Mixture properties are molar averages: M_mix = Σ x_i*M_i, R_mix = R_u/M_mix, c_p,mix = Σ x_i*c_p,i. For real gases this becomes complex; mixing rules depend on the equation of state. Combustion, HVAC, and gas separation all rely on mixture thermodynamics.

## Explainer

Your prerequisite on partial pressures established the central fact about ideal gas mixtures: each component behaves as if it were alone in the container, occupying the full volume at the temperature of the mixture. **Dalton's law** formalizes this as P_total = Σ P_i, where each **partial pressure** P_i = x_i × P_total is the pressure that component i would exert if it alone occupied the volume at the same temperature. The **mole fraction** x_i = n_i/n_total is the key composition variable — it is simultaneously the volume fraction and the partial-pressure fraction for ideal gases.

The mixture properties you need for thermodynamic calculations follow from treating the mixture as a single pure substance with molar-averaged properties. The **mixture molecular weight** M_mix = Σ x_i M_i is a straightforward molar average — heavier components pull it up, lighter ones pull it down. From M_mix you get the specific gas constant R_mix = R_u / M_mix (where R_u = 8.314 J/mol·K is the universal gas constant), which you can plug directly into the ideal gas law PV = m R_mix T to work in mass-based units. Similarly, the **mixture heat capacity** c_p,mix = Σ x_i c_p,i lets you compute enthalpy changes for the mixture just as you would for a pure gas. All of this works because ideal gas components do not interact — mixing them does not change their individual enthalpies, internal energies, or entropies beyond the entropy of mixing (which matters for chemical equilibrium but not for energy balances in most engineering calculations).

A practical example anchors the arithmetic. Dry air is approximately 21% O₂ and 79% N₂ by mole. The mixture molecular weight is M_air = 0.21×32 + 0.79×28 = 6.72 + 22.12 = 28.84 g/mol, giving R_air = 8314/28.84 ≈ 287 J/(kg·K) — the familiar specific gas constant for air. The partial pressure of O₂ at sea level (101.3 kPa) is 0.21 × 101.3 = 21.3 kPa. This is why oxygen partial pressure matters for aviation physiology and why altitude affects combustion — as you climb, P_total falls and with it P_O₂, reducing oxygen availability even though the mole fraction stays the same.

For **real gas mixtures**, the ideal treatment breaks down because intermolecular forces between unlike species differ from forces between like species, producing volume and enthalpy changes on mixing. Real gas equations of state like van der Waals or Peng-Robinson require **mixing rules** for their parameters — empirical or theoretically motivated formulas for the cross-interaction parameters a_ij (attraction) and b_ij (size). These are more involved and depend on the specific gas pair. For engineering work at moderate pressures (combustion products below ~10 bar, HVAC systems at atmospheric conditions), the ideal mixture treatment is accurate to within a few percent and is almost universally used. Real-gas corrections become important in natural gas pipelines at high pressure, supercritical processes, and precision measurements where small departures from ideality matter.
