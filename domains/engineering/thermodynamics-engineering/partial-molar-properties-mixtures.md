---
id: partial-molar-properties-mixtures
title: Partial Molar Properties and Solutions
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: partial-molar-properties-solutions
  type: hard
- id: gas-mixture-thermodynamics-daltons
  type: soft
builds-toward:
- phase-equilibrium-clausius-clapeyron-detailed
- absorption-refrigeration-systems
tags:
- partial-molar
- solutions
- mixtures
- interactions
stage: advanced
status: draft
---

# Partial Molar Properties and Solutions

## Core Idea
Partial molar properties (V̄_i, H̄_i, S̄_i) represent each component's contribution to total mixture properties, accounting for intermolecular interactions. Gibbs-Duhem equation constrains these at constant T,P: Σ x_i*dM̄_i = 0. Partial molar enthalpies drive phase equilibrium and are essential for distillation, absorption, and liquid-solution thermodynamics.

## Explainer

When you mix ethanol and water, the total volume of the mixture is *less* than the sum of the volumes of the pure components — up to about 4% less at certain compositions. This non-additivity reflects molecular interactions: ethanol and water molecules pack together differently than they do in pure form. The **partial molar volume** V̄_i of component i in a mixture is defined as (∂V/∂n_i) at constant T, P, and constant amounts of all other components. It captures the actual volumetric contribution of adding an infinitesimal amount of i to the mixture at that composition. For pure i, V̄_i equals V_m,i (the molar volume of pure i). In a mixture, V̄_i can be larger, smaller, or even negative — a concept that initially seems paradoxical but is simply the consequence of intermolecular interactions.

The reason partial molar properties matter so much is the **Euler relation** for extensive properties: V = Σ n_i V̄_i, and similarly for G, H, S. This says the total mixture property is exactly reconstructed by summing each component's partial molar contribution weighted by its moles — but only at a fixed composition. You cannot simply add molar properties of pure components; you must use the composition-dependent partial molar values. The **Gibbs-Duhem equation** (Σ x_i dM̄_i = 0 at constant T, P) is the companion constraint: if you change the partial molar property of one component, the others must adjust accordingly. You cannot independently specify all partial molar properties at a given composition — they are coupled. This is why measuring partial molar properties in a binary system only requires data for one component: the other follows from Gibbs-Duhem.

The most important partial molar property in phase equilibrium is the **partial molar Gibbs free energy**, which equals the **chemical potential** μ_i = Ḡ_i. Phase equilibrium between two phases (say liquid and vapor) requires that the chemical potential of each component be equal in both phases: μ_i^L = μ_i^V. This condition, applied with models for how μ_i depends on composition, gives you VLE (vapor-liquid equilibrium) calculations for distillation design. The partial molar enthalpy H̄_i determines the **heat of mixing** — how much heat is absorbed or released when you blend components. For ideal solutions, H̄_i = H_m,i (pure molar enthalpy) and there is no heat of mixing. For real solutions, the deviation of H̄_i from its pure-component value is the **enthalpy of mixing**, a measurable and important quantity in heat exchanger and reactor design.

Connecting back to your prerequisite knowledge of Dalton's law and gas mixture thermodynamics: for ideal gases, all partial molar properties equal the pure-component values at the same T and P. Dalton's law (P_total = Σ P_i) and Amagat's law (V_total = Σ V_i) are both consequences of ideal gas behavior where components do not interact. Liquid mixtures rarely behave ideally, and the partial molar framework is precisely the generalization that handles real interaction effects. Activity coefficients and fugacity coefficients emerge as the quantitative measures of how far the partial molar Gibbs free energy deviates from ideal — and those deviations are what make real separation processes either much easier or much harder than ideal calculations would predict.
