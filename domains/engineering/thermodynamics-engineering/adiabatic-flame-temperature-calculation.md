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
stage: formal-systems
status: validated
---

# Adiabatic Flame Temperature

## Core Idea
Adiabatic flame temperature is the maximum temperature achievable by combustion with no heat loss. It depends on fuel type, stoichiometry, and reactant preheat. Calculated from energy balance: ΔH_combustion = Σn_i*c_p,i*(T_flame - T_ref). Actual flame temperatures in engines are lower due to incomplete combustion, heat transfer, and dissociation at high temperatures.

## Questions

```yaml
- question: "A combustion engineer increases the fuel-air equivalence ratio from 1.0 (stoichiometric) to 1.2 (rich) while keeping the reactant inlet temperature and pressure constant. What happens to the adiabatic flame temperature?"
  type: multiple-choice
  options:
    - "It increases, because more fuel releases more total chemical energy"
    - "It stays the same, because total enthalpy of combustion is conserved"
    - "It decreases, because unburned excess fuel absorbs heat without contributing combustion energy"
    - "It increases up to equivalence ratio 1.2 before decreasing at higher ratios"
  answer: 2
  explanation: "At stoichiometric (φ = 1.0), all fuel burns and the released energy heats only the minimum product mass — AFT is maximized. Above stoichiometric (rich), the excess fuel cannot burn due to insufficient oxygen. This unburned fuel is still present in the products and absorbs sensible heat without releasing combustion energy, diluting the temperature. The intuitive error is thinking 'more fuel = more energy = higher temperature' — but the temperature depends on energy per unit product mass, not total energy."

- question: "Why is the adiabatic flame temperature calculation typically iterative rather than solvable in a single step?"
  type: multiple-choice
  options:
    - "Because the stoichiometric air-fuel ratio changes with flame temperature"
    - "Because the heat of combustion (ΔH_combustion) is temperature-dependent and must be updated each iteration"
    - "Because the specific heats (cp) of product species like CO₂ and H₂O vary significantly with temperature, so H_products(T) is nonlinear in T"
    - "Because dissociation at all temperatures introduces unknown product concentrations that must be solved simultaneously"
  answer: 2
  explanation: "The energy balance H_products(T_flame) = H_reactants requires evaluating ∫cp dT for each product species from reference to T_flame. Because cp for CO₂ and H₂O varies significantly over the relevant temperature range (500–3000 K), H_products is a nonlinear function of T_flame with no closed-form inverse. The procedure is therefore: guess T_flame, compute H_products, compare to H_reactants, adjust, repeat. Dissociation (option D) introduces additional complexity at very high temperatures, but even without dissociation the cp variation alone necessitates iteration."

- question: "At flame temperatures above approximately 1800 K, molecular dissociation of CO₂ and H₂O causes the actual flame temperature to exceed the simple adiabatic flame temperature prediction."
  type: true-false
  answer: false
  explanation: "Dissociation is endothermic — breaking chemical bonds absorbs energy. When CO₂ and H₂O partially dissociate into CO, O₂, H₂, OH, and atomic species at high temperatures, they consume energy that would otherwise go into raising the temperature. This acts as a thermostatic effect, limiting peak temperature. The actual AFT is lower than the simple cp-based prediction, not higher. Correctly accounting for dissociation requires solving chemical equilibrium equations simultaneously with the energy balance, typically reducing AFT by 100–300 K."

- question: "Preheating the combustion air (e.g., using exhaust gas in a recuperator) increases the adiabatic flame temperature for a stoichiometric mixture."
  type: true-false
  answer: true
  explanation: "Preheating the air raises the enthalpy of the reactants entering the combustion process. Since energy balance requires H_products(T_flame) = H_reactants(T_preheat), a higher reactant enthalpy means the products must reach a higher temperature to satisfy the balance. Physically: less of the combustion energy must be 'spent' heating the air from ambient to flame temperature, so more is available to push the products to a higher final temperature. This is why recuperators improve efficiency in industrial furnaces and gas turbines."

- question: "Why is the adiabatic flame temperature maximized at the stoichiometric mixture ratio, and why does both excess air and excess fuel reduce it?"
  type: short-answer
  answer: "At stoichiometric, all fuel burns completely and the released energy heats exactly the minimum product mass — the ratio of energy released to mass heated is at its maximum. Excess air introduces additional N₂ and O₂ into the products that must be heated by the same combustion energy but contribute none themselves, reducing energy per unit mass and thus temperature. Excess fuel leaves unburned hydrocarbons in the products that absorb sensible heat without contributing combustion energy, also diluting the temperature. Only stoichiometric combustion avoids both dilution effects."
  explanation: "This question tests whether students understand AFT as energy per unit product mass, not total energy. Adding more air adds more mass to heat; adding more fuel adds unreacted material that acts as a heat sink. The stoichiometric point is a maximum because it is the only ratio where every molecule of oxidizer and fuel is consumed productively. In practice, engines often run slightly lean (excess air) to ensure complete combustion and reduce emissions, accepting the AFT penalty in exchange for reliability."
```

## Explainer

When fuel burns in an adiabatic (perfectly insulated) container with just enough air for complete combustion, all the chemical energy released by the reaction goes into raising the temperature of the products. No heat escapes to the surroundings, no work is done, and the combustion is complete. The resulting temperature is the **adiabatic flame temperature (AFT)** — a theoretical upper bound on how hot that fuel-air mixture can become. It is the thermodynamic ceiling for combustion-driven processes, and it sets limits on engine performance, material selection, and emissions formation.

The calculation is a direct application of the first law of thermodynamics for an open (or closed) adiabatic system: the enthalpy of the products at T_flame equals the enthalpy of the reactants at their initial conditions T_ref. In practice, you write: H_products(T_flame) = H_reactants(T_ref). Your prerequisite knowledge of fuel combustion products analysis gives you the product species and their molar quantities (CO₂, H₂O, N₂, and possibly excess O₂ if lean). The enthalpy of each product species at temperature T is h°_f + ∫c_p dT from reference to T. You set the sum equal to the known enthalpy of the reactants and solve for T_flame. Because c_p varies with temperature (especially strongly for CO₂ and H₂O at high temperatures), this is generally an **iterative calculation**: guess T_flame, compute H_products, check the energy balance, adjust, and repeat until convergence.

Stoichiometry has a large and intuitive effect on AFT. At the **stoichiometric ratio** (exactly enough air for complete combustion), AFT is maximized — all combustion energy heats only the minimum necessary product mass. Add excess air (lean mixture) and you dilute the products: the same energy now heats a larger mass of gas, reducing the final temperature. Add excess fuel (rich mixture) and you have unburned fuel that absorbs heat without contributing to it, again reducing AFT. Preheating the reactants raises AFT proportionally, which is why recuperators and regenerators in industrial furnaces improve performance — the incoming air arrives hot, requiring less chemical energy to reach any target temperature.

At very high temperatures (above about 1800 K for hydrocarbons), the real AFT diverges from this simple calculation because of **dissociation**: stable product molecules like CO₂ and H₂O partially break apart into CO, O₂, H₂, OH, and atomic species. Dissociation is endothermic — it absorbs energy — which means it acts as a thermostat that limits the peak temperature. A rigorous AFT calculation at high temperature requires equilibrium chemistry: you must solve the chemical equilibrium equations simultaneously with the energy balance, using equilibrium constants or Gibbs free energy minimization. This significantly complicates the calculation and typically reduces the predicted AFT by 100–300 K compared to the simple c_p-based formula. The simple formula is adequate for preliminary calculations; detailed combustion design requires the equilibrium treatment.
