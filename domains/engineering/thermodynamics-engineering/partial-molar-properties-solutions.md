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

## Questions

```yaml
- question: "One liter of ethanol is mixed with one liter of water at constant temperature and pressure. The resulting volume is approximately 1.93 liters, not 2 liters. Which concept directly explains this observation?"
  type: multiple-choice
  options:
    - "The density of water increases when ethanol is added, compressing the water into a smaller volume"
    - "The partial molar volumes of ethanol and water in the mixture differ from their respective pure-component molar volumes"
    - "Conservation of mass is violated when polar and nonpolar molecules mix"
    - "The activity coefficients are greater than 1, indicating positive deviations from Raoult's law"
  answer: 1
  explanation: "The partial molar volume V̄ᵢ is the actual effective volume contribution of component i in the context of the mixture — not the molar volume of the pure substance. When ethanol fits into the hydrogen-bonding network of water, the ethanol molecules occupy less effective space than they would in pure ethanol, and vice versa. This is precisely why partial molar properties exist: pure-component molar volumes are not additive in real solutions. Activity coefficients (option D) describe chemical potential deviations, not volume deviations directly."

- question: "At equilibrium between a vapor phase and a liquid phase in a two-component system, the chemical potential of component i must satisfy which condition?"
  type: multiple-choice
  options:
    - "μᵢ(liquid) > μᵢ(vapor), so that molecules are driven from liquid to vapor"
    - "μᵢ(liquid) = μᵢ(vapor) for each component, since no net transfer occurs at equilibrium"
    - "The chemical potential of each component equals zero in both phases"
    - "μᵢ depends only on temperature and is equal across phases only when T is uniform"
  answer: 1
  explanation: "The fundamental criterion for phase equilibrium is equal chemical potential across all coexisting phases: μᵢ(α) = μᵢ(β). Chemical potential is the partial molar Gibbs free energy, and systems at constant T and P minimize total G. If μᵢ is higher in one phase, molecules will spontaneously transfer to the lower-μ phase until equality is reached. This is the driving force behind distillation, extraction, and crystallization — not concentration gradients per se, but chemical potential gradients. Concentration equalization (option A's implication) and zero values (option C) are wrong; temperature alone (option D) doesn't determine μᵢ in mixtures."

- question: "The partial molar volume of a component in a mixture equals the molar volume of that component in its pure state."
  type: true-false
  answer: false
  explanation: "This is only true for ideal solutions. In general, V̄ᵢ = (∂V/∂nᵢ)_{T,P,nⱼ} — the rate of change of total volume when adding a differential amount of i to the mixture. In real solutions, the intermolecular interactions between unlike molecules change how each component's molecules pack together. Ethanol's partial molar volume in water (~55 mL/mol in water-rich mixtures) differs significantly from pure ethanol's molar volume (~58.4 mL/mol) precisely because it sits in a water hydrogen-bonding network rather than an ethanol environment."

- question: "For an ideal solution, mixing two components produces no change in total volume and no change in enthalpy."
  type: true-false
  answer: true
  explanation: "The defining properties of an ideal solution are ΔV_mix = 0 (no volume change) and ΔH_mix = 0 (no enthalpy change on mixing). This occurs when all molecular interactions — A–A, B–B, and A–B — are essentially identical, so molecules experience the same environment whether surrounded by like or unlike molecules (e.g., benzene-toluene mixtures). Note that the Gibbs energy of mixing is still negative (ΔG_mix < 0) due to the entropy of mixing — ideal solutions mix spontaneously even with no enthalpy driving force."

- question: "Why does the chemical potential of a component, rather than its molar concentration, determine when two phases are in equilibrium with each other?"
  type: short-answer
  answer: "Chemical potential μᵢ = (∂G/∂nᵢ)_{T,P} measures the tendency of component i to leave a phase — it incorporates both concentration and all intermolecular interaction effects (captured by the activity coefficient). Two phases can have equal concentrations of a component yet still not be in equilibrium if the molecular environments differ (e.g., a solute that strongly prefers one solvent over another). Equilibrium requires that the escaping tendency be equal in both phases; since chemical potential is the thermodynamic measure of escaping tendency, equality of μᵢ across phases is the correct criterion, not equality of concentrations."
  explanation: "Concentration-based criteria fail because the 'desirability' of a phase for a given molecule depends on molecular interactions, not just how crowded it is. A molecule surrounded by favorable neighbors (low activity coefficient, γ < 1) has a lower chemical potential and less tendency to escape than the same concentration in an unfavorable environment (γ > 1). The activity coefficient γᵢ captures this interaction effect, entering as μᵢ = μᵢ° + RT ln(γᵢxᵢ). Equal chemical potential ensures that no molecule has a net incentive to change phases — the true thermodynamic equilibrium condition."
```

## Explainer

From your work on gas mixtures and Dalton's Law, you already know that mixtures are more complex than pure components — each species contributes partial pressures, and the total pressure is their sum. But that additive picture works cleanly for ideal gases because gas molecules don't interact much. For liquid solutions, molecular interactions dominate, and the properties of a mixture are *not* simply the sum of the pure-component properties. A liter of ethanol mixed with a liter of water does not give two liters of solution — it gives about 1.93 liters, because ethanol and water molecules pack together differently than either pure fluid. The **partial molar property** framework exists to account for this reality.

The **partial molar volume** V̄ᵢ of component i is defined as V̄ᵢ = (∂V/∂nᵢ)_{T,P,nⱼ≠ᵢ} — the rate of change of total mixture volume when you add a differential amount of component i to the mixture at constant T, P, and all other amounts. This is not the same as the molar volume of pure i; it is the *effective* volume contribution of i in the presence of all the other molecules it's surrounded by. If the mixture is ethanol-water and you're in a water-rich region, V̄_ethanol reflects how ethanol molecules fit into the water network. The total volume is then exactly V = n₁V̄₁ + n₂V̄₂ — a general exact result, not an approximation. What's approximate is treating V̄ᵢ as equal to the pure-component molar volume Vᵢ° (which works only for ideal solutions).

The **chemical potential** μᵢ = (∂G/∂nᵢ)_{T,P,nⱼ≠ᵢ} is the partial molar Gibbs free energy and is by far the most important partial molar property. From your prerequisite on equations of state, you know that Gibbs free energy governs phase and chemical equilibrium: systems minimize G at constant T and P. For a mixture, equilibrium requires that the chemical potential of each component be equal across all phases. If μᵢ is higher in phase α than phase β, component i will spontaneously transfer from α to β. This is the driving force behind distillation, extraction, and absorption — all driven by differences in chemical potential until equality is reached.

For **ideal solutions**, V̄ᵢ = Vᵢ°, H̄ᵢ = Hᵢ°, and mixing produces no volume change or enthalpy change. This occurs when all molecular interactions are similar (e.g., benzene-toluene). For **real solutions**, deviations are captured by the **activity coefficient** γᵢ, which modifies the chemical potential as μᵢ = μᵢ° + RT ln(γᵢxᵢ). When γᵢ > 1, component i "wants to leave" the mixture more than ideal — it has positive deviations from Raoult's law. When γᵢ < 1, it prefers the mixture environment. Activity coefficients compress the full complexity of molecular interactions into a single correction factor, enabling phase equilibrium calculations with experimental data. Mastering partial molar properties is the prerequisite to understanding why distillation columns can or cannot separate certain mixtures and how to design separation processes for real industrial systems.
