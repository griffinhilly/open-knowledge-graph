---
id: partial-molar-properties-solutions
title: Partial Molar Properties and Solution Thermodynamics
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: thermodynamic-properties-and-equations-of-state
  type: hard
- id: gas-mixtures-partial-pressures-daltons-law
  type: hard
builds-toward:
- gibbs-phase-rule-multicomponent
- ideal-solution-thermodynamics
tags:
- partial-molar
- solution
- component-properties
- chemical-potential
stage: advanced
status: draft
---

# Partial Molar Properties and Solution Thermodynamics

## Core Idea
Partial molar properties (V̄ᵢ, H̄ᵢ, S̄ᵢ) describe how each component contributes to total mixture properties. The chemical potential μᵢ = (∂G/∂nᵢ)_{T,P} is the partial molar Gibbs free energy. Ideal solutions satisfy additivity: V = ΣxᵢV̄ᵢ; real solutions exhibit deviations characterized by activity coefficients, essential for phase equilibrium and separation process design.

## Explainer

From your work on gas mixtures and Dalton's Law, you already know that mixtures are more complex than pure components — each species contributes partial pressures, and the total pressure is their sum. But that additive picture works cleanly for ideal gases because gas molecules don't interact much. For liquid solutions, molecular interactions dominate, and the properties of a mixture are *not* simply the sum of the pure-component properties. A liter of ethanol mixed with a liter of water does not give two liters of solution — it gives about 1.93 liters, because ethanol and water molecules pack together differently than either pure fluid. The **partial molar property** framework exists to account for this reality.

The **partial molar volume** V̄ᵢ of component i is defined as V̄ᵢ = (∂V/∂nᵢ)_{T,P,nⱼ≠ᵢ} — the rate of change of total mixture volume when you add a differential amount of component i to the mixture at constant T, P, and all other amounts. This is not the same as the molar volume of pure i; it is the *effective* volume contribution of i in the presence of all the other molecules it's surrounded by. If the mixture is ethanol-water and you're in a water-rich region, V̄_ethanol reflects how ethanol molecules fit into the water network. The total volume is then exactly V = n₁V̄₁ + n₂V̄₂ — a general exact result, not an approximation. What's approximate is treating V̄ᵢ as equal to the pure-component molar volume Vᵢ° (which works only for ideal solutions).

The **chemical potential** μᵢ = (∂G/∂nᵢ)_{T,P,nⱼ≠ᵢ} is the partial molar Gibbs free energy and is by far the most important partial molar property. From your prerequisite on equations of state, you know that Gibbs free energy governs phase and chemical equilibrium: systems minimize G at constant T and P. For a mixture, equilibrium requires that the chemical potential of each component be equal across all phases. If μᵢ is higher in phase α than phase β, component i will spontaneously transfer from α to β. This is the driving force behind distillation, extraction, and absorption — all driven by differences in chemical potential until equality is reached.

For **ideal solutions**, V̄ᵢ = Vᵢ°, H̄ᵢ = Hᵢ°, and mixing produces no volume change or enthalpy change. This occurs when all molecular interactions are similar (e.g., benzene-toluene). For **real solutions**, deviations are captured by the **activity coefficient** γᵢ, which modifies the chemical potential as μᵢ = μᵢ° + RT ln(γᵢxᵢ). When γᵢ > 1, component i "wants to leave" the mixture more than ideal — it has positive deviations from Raoult's law. When γᵢ < 1, it prefers the mixture environment. Activity coefficients compress the full complexity of molecular interactions into a single correction factor, enabling phase equilibrium calculations with experimental data. Mastering partial molar properties is the prerequisite to understanding why distillation columns can or cannot separate certain mixtures and how to design separation processes for real industrial systems.
