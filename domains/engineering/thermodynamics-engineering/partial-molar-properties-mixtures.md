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
- absorption-refrigeration-cycles
tags:
- partial-molar
- solutions
- mixtures
- interactions
stage: formal-systems
status: validated
---

# Partial Molar Properties and Solutions

## Core Idea
Partial molar properties (V̄_i, H̄_i, S̄_i) represent each component's contribution to total mixture properties, accounting for intermolecular interactions. Gibbs-Duhem equation constrains these at constant T,P: Σ x_i*dM̄_i = 0. Partial molar enthalpies drive phase equilibrium and are essential for distillation, absorption, and liquid-solution thermodynamics.

## Questions

```yaml
- question: "You carefully measure 500 mL of ethanol and 500 mL of water and mix them together at constant temperature. What total volume do you expect?"
  type: multiple-choice
  options:
    - "Exactly 1000 mL — volume must be conserved by mass balance"
    - "Slightly less than 1000 mL — partial molar volumes in the mixture differ from pure molar volumes due to intermolecular interactions"
    - "Slightly more than 1000 mL — the exothermic mixing heat causes thermal expansion"
    - "Exactly 1000 mL, but only if both liquids are at the same initial temperature"
  answer: 1
  explanation: "Ethanol-water is the classic example of non-ideal mixing. The mixture volume is about 3–4% less than the sum of the pure component volumes at certain compositions. This happens because ethanol and water molecules interact differently with each other than with molecules of their own kind — the packing is more efficient in the mixture, reducing the total volume. Mass is conserved (no atoms are created or destroyed), but volume is not, because volume depends on how molecules pack together. The partial molar volumes capture this: each component's volumetric contribution in the mixture differs from its contribution as a pure liquid."

- question: "The Gibbs-Duhem equation (Σ x_i dM̄_i = 0 at constant T and P) implies which constraint on partial molar properties?"
  type: multiple-choice
  options:
    - "All partial molar properties in a mixture are constant at fixed composition"
    - "The partial molar properties of components in a mixture can be chosen independently — one does not constrain the others"
    - "In a binary mixture, if the partial molar volume of one component increases with composition, the partial molar volume of the other must decrease in a constrained way"
    - "Partial molar enthalpy is always equal to the pure-component molar enthalpy"
  answer: 2
  explanation: "The Gibbs-Duhem equation is a constraint that couples the partial molar properties of all components at fixed T and P. In a binary mixture (components 1 and 2), it states x₁ dV̄₁ + x₂ dV̄₂ = 0, meaning you cannot independently specify how both partial molar volumes vary with composition — if one changes, the other must adjust accordingly. This is why knowing the partial molar property of one component as a function of composition in a binary system is sufficient to calculate the other via integration. It reduces the experimental measurement burden and ensures thermodynamic consistency."

- question: "In a real liquid mixture, the partial molar volume of a component can in principle be smaller than its pure molar volume, and in extreme cases can even be negative."
  type: true-false
  answer: true
  explanation: "The partial molar volume V̄_i = (∂V/∂n_i) at constant T, P, and fixed amounts of other components is a differential quantity — it measures the marginal contribution of adding a tiny bit of component i to the existing mixture. When strong attractive interactions exist between unlike molecules (or when the added component fits compactly into the existing liquid structure), the mixture can contract upon addition of i, making its effective volumetric contribution less than zero. Negative partial molar volumes are uncommon but physically real and thermodynamically permitted. This starkly illustrates why you cannot treat mixture properties as simple sums of pure-component properties."

- question: "For an ideal solution, the partial molar enthalpy of each component equals zero, because ideal components do not interact with each other."
  type: true-false
  answer: false
  explanation: "This is a subtle but important error. For an ideal solution, the partial molar enthalpy of component i equals the pure molar enthalpy of i: H̄_i = H°_m,i. This is NOT zero — it is whatever enthalpy the pure component has. What is zero for an ideal solution is the enthalpy of mixing (ΔH_mix = 0), meaning no heat is released or absorbed when the components are blended. But each component still carries its own enthalpy content. Setting H̄_i = 0 would mean the mixture has no enthalpy at all, which is physically nonsensical."

- question: "Why must the total volume of a real liquid mixture be calculated using partial molar volumes rather than simply summing the pure-component molar volumes weighted by moles? What physical reality do partial molar volumes capture?"
  type: short-answer
  answer: "Pure molar volumes describe how much volume each component occupies when surrounded only by molecules of its own kind. In a mixture, molecules of different species interact with each other — through different intermolecular forces, packing geometries, and structural effects. These interactions change how much space each molecule effectively occupies. The partial molar volume V̄_i captures this: it measures the actual incremental volume change when one more mole of i is added to the mixture at that specific composition. When interactions between unlike molecules are stronger (or packing is more efficient) than between like molecules, V̄_i < V°_m,i and the total mixture volume is less than the sum of pure volumes. Simple summation ignores these interaction effects entirely and gives the wrong answer for real systems."
  explanation: "This is the conceptual heart of partial molar properties: they replace the pure-component properties with composition-dependent effective contributions that encode intermolecular interaction information. The same logic applies to H̄_i, Ḡ_i, and S̄_i — all can deviate from pure-component values, and those deviations (excess properties) are the quantitative signatures of non-ideal solution behavior."
```

## Explainer

When you mix ethanol and water, the total volume of the mixture is *less* than the sum of the volumes of the pure components — up to about 4% less at certain compositions. This non-additivity reflects molecular interactions: ethanol and water molecules pack together differently than they do in pure form. The **partial molar volume** V̄_i of component i in a mixture is defined as (∂V/∂n_i) at constant T, P, and constant amounts of all other components. It captures the actual volumetric contribution of adding an infinitesimal amount of i to the mixture at that composition. For pure i, V̄_i equals V_m,i (the molar volume of pure i). In a mixture, V̄_i can be larger, smaller, or even negative — a concept that initially seems paradoxical but is simply the consequence of intermolecular interactions.

The reason partial molar properties matter so much is the **Euler relation** for extensive properties: V = Σ n_i V̄_i, and similarly for G, H, S. This says the total mixture property is exactly reconstructed by summing each component's partial molar contribution weighted by its moles — but only at a fixed composition. You cannot simply add molar properties of pure components; you must use the composition-dependent partial molar values. The **Gibbs-Duhem equation** (Σ x_i dM̄_i = 0 at constant T, P) is the companion constraint: if you change the partial molar property of one component, the others must adjust accordingly. You cannot independently specify all partial molar properties at a given composition — they are coupled. This is why measuring partial molar properties in a binary system only requires data for one component: the other follows from Gibbs-Duhem.

The most important partial molar property in phase equilibrium is the **partial molar Gibbs free energy**, which equals the **chemical potential** μ_i = Ḡ_i. Phase equilibrium between two phases (say liquid and vapor) requires that the chemical potential of each component be equal in both phases: μ_i^L = μ_i^V. This condition, applied with models for how μ_i depends on composition, gives you VLE (vapor-liquid equilibrium) calculations for distillation design. The partial molar enthalpy H̄_i determines the **heat of mixing** — how much heat is absorbed or released when you blend components. For ideal solutions, H̄_i = H_m,i (pure molar enthalpy) and there is no heat of mixing. For real solutions, the deviation of H̄_i from its pure-component value is the **enthalpy of mixing**, a measurable and important quantity in heat exchanger and reactor design.

Connecting back to your prerequisite knowledge of Dalton's law and gas mixture thermodynamics: for ideal gases, all partial molar properties equal the pure-component values at the same T and P. Dalton's law (P_total = Σ P_i) and Amagat's law (V_total = Σ V_i) are both consequences of ideal gas behavior where components do not interact. Liquid mixtures rarely behave ideally, and the partial molar framework is precisely the generalization that handles real interaction effects. Activity coefficients and fugacity coefficients emerge as the quantitative measures of how far the partial molar Gibbs free energy deviates from ideal — and those deviations are what make real separation processes either much easier or much harder than ideal calculations would predict.
