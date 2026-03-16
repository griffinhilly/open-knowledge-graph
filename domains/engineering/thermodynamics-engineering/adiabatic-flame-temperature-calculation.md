---
id: adiabatic-flame-temperature-calculation
title: Adiabatic Flame Temperature
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: adiabatic-flame-temperature
  type: hard
- id: fuel-combustion-products-analysis
  type: hard
builds-toward:
- brayton-gas-turbine-cycles
tags:
- combustion
- flame-temperature
- adiabatic
- energy-balance
stage: advanced
status: draft
---

# Adiabatic Flame Temperature

## Core Idea
Adiabatic flame temperature is the maximum temperature achievable by combustion with no heat loss. It depends on fuel type, stoichiometry, and reactant preheat. Calculated from energy balance: ΔH_combustion = Σn_i*c_p,i*(T_flame - T_ref). Actual flame temperatures in engines are lower due to incomplete combustion, heat transfer, and dissociation at high temperatures.

## Explainer

When fuel burns in an adiabatic (perfectly insulated) container with just enough air for complete combustion, all the chemical energy released by the reaction goes into raising the temperature of the products. No heat escapes to the surroundings, no work is done, and the combustion is complete. The resulting temperature is the **adiabatic flame temperature (AFT)** — a theoretical upper bound on how hot that fuel-air mixture can become. It is the thermodynamic ceiling for combustion-driven processes, and it sets limits on engine performance, material selection, and emissions formation.

The calculation is a direct application of the first law of thermodynamics for an open (or closed) adiabatic system: the enthalpy of the products at T_flame equals the enthalpy of the reactants at their initial conditions T_ref. In practice, you write: H_products(T_flame) = H_reactants(T_ref). Your prerequisite knowledge of fuel combustion products analysis gives you the product species and their molar quantities (CO₂, H₂O, N₂, and possibly excess O₂ if lean). The enthalpy of each product species at temperature T is h°_f + ∫c_p dT from reference to T. You set the sum equal to the known enthalpy of the reactants and solve for T_flame. Because c_p varies with temperature (especially strongly for CO₂ and H₂O at high temperatures), this is generally an **iterative calculation**: guess T_flame, compute H_products, check the energy balance, adjust, and repeat until convergence.

Stoichiometry has a large and intuitive effect on AFT. At the **stoichiometric ratio** (exactly enough air for complete combustion), AFT is maximized — all combustion energy heats only the minimum necessary product mass. Add excess air (lean mixture) and you dilute the products: the same energy now heats a larger mass of gas, reducing the final temperature. Add excess fuel (rich mixture) and you have unburned fuel that absorbs heat without contributing to it, again reducing AFT. Preheating the reactants raises AFT proportionally, which is why recuperators and regenerators in industrial furnaces improve performance — the incoming air arrives hot, requiring less chemical energy to reach any target temperature.

At very high temperatures (above about 1800 K for hydrocarbons), the real AFT diverges from this simple calculation because of **dissociation**: stable product molecules like CO₂ and H₂O partially break apart into CO, O₂, H₂, OH, and atomic species. Dissociation is endothermic — it absorbs energy — which means it acts as a thermostat that limits the peak temperature. A rigorous AFT calculation at high temperature requires equilibrium chemistry: you must solve the chemical equilibrium equations simultaneously with the energy balance, using equilibrium constants or Gibbs free energy minimization. This significantly complicates the calculation and typically reduces the predicted AFT by 100–300 K compared to the simple c_p-based formula. The simple formula is adequate for preliminary calculations; detailed combustion design requires the equilibrium treatment.
