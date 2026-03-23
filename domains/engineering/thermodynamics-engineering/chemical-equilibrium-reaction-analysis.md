---
id: chemical-equilibrium-reaction-analysis
title: Chemical Equilibrium and Equilibrium Constant
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: thermodynamic-properties-and-equations-of-state
  type: hard
- id: chemical-equilibrium
  type: soft
builds-toward:
- adiabatic-flame-temperature
- chemical-exergy-fuel-combustion
tags:
- equilibrium-constant
- gibbs-free-energy
- reaction
- composition
stage: formal-systems
status: validated
---

# Chemical Equilibrium and Equilibrium Constant

## Core Idea
Chemical equilibrium at constant T and P is determined by minimizing Gibbs free energy; the equilibrium constant K_p relates partial pressures of reactants and products. K_p depends on temperature via d(ln K)/dT = ΔH_rxn/(RT²). Real combustion products contain incomplete combustion species (CO, OH, NO) in equilibrium, requiring iterative solution for composition.

## Questions

```yaml
- question: "A combustion engineer assumes that burning methane at 2500 K produces only CO₂ and H₂O. A more accurate equilibrium analysis reveals significant CO and OH in the products. What is the primary reason the simplified assumption fails?"
  type: multiple-choice
  options:
    - "Methane combustion is incomplete due to insufficient oxygen supply"
    - "At high temperatures, K_p for dissociation reactions becomes large enough that CO₂ and H₂O partially reverse to CO, OH, and other species"
    - "The reaction has not reached equilibrium at 2500 K"
    - "High pressure prevents complete conversion to CO₂ and H₂O"
  answer: 1
  explanation: "The van't Hoff equation shows that K_p increases with temperature for endothermic reactions. The dissociation of CO₂ → CO + ½O₂ and H₂O → OH + ½H₂ are endothermic, so at high combustion temperatures their K_p values become significant — the equilibrium composition includes substantial minor species. Assuming only CO₂ and H₂O ignores these equilibrium shifts, causing serious error in energy and emissions calculations."

- question: "For a reaction with ΔG° = −20 kJ/mol at 1000 K, which statement correctly describes K_p?"
  type: multiple-choice
  options:
    - "K_p = 0, meaning the reaction does not proceed"
    - "K_p < 1, meaning reactants are favored at equilibrium"
    - "K_p > 1, meaning products are favored at equilibrium"
    - "K_p = 1, meaning the mixture is at equal partial pressures"
  answer: 2
  explanation: "The relationship ΔG° = −RT ln K_p directly links standard Gibbs free energy to the equilibrium constant. A negative ΔG° means −RT ln K_p < 0, so ln K_p > 0, so K_p > 1 — products are thermodynamically favored. The quantitative relationship shows not just direction but how far toward products the equilibrium lies."

- question: "For an exothermic combustion reaction, increasing the reaction temperature will shift the equilibrium toward greater product yield."
  type: true-false
  answer: false
  explanation: "This is exactly backwards. The van't Hoff equation d(ln K_p)/dT = ΔH_rxn/(RT²) shows that for an exothermic reaction (ΔH_rxn < 0), K_p decreases as temperature rises. Le Chatelier's principle confirms this: adding heat to an exothermic reaction shifts equilibrium toward reactants. High combustion temperatures actually cause dissociation of CO₂ and H₂O back into intermediates — a critical consideration in combustor design."

- question: "The equilibrium composition of a reacting gas mixture at constant T and P corresponds to the minimum of the Gibbs free energy over all possible compositions."
  type: true-false
  answer: true
  explanation: "This is the fundamental thermodynamic principle underlying chemical equilibrium. At constant T and P, any spontaneous process decreases G, and the equilibrium state is the composition where G is minimized. Both the K_p approach and direct Gibbs minimization are computational implementations of this same physical principle — they yield identical equilibrium compositions."

- question: "Why does finding the equilibrium composition of real combustion products at high temperature require iterative numerical solution rather than a simple stoichiometric calculation?"
  type: short-answer
  answer: "Real combustion involves simultaneous equilibria among many species (CO₂, H₂O, CO, OH, H₂, O, NO, etc.). Each equilibrium is described by a nonlinear K_p expression, and all must be satisfied simultaneously along with atom-balance constraints. The resulting system of coupled nonlinear equations has no closed-form solution — compositions must be assumed, K_p equations and mass balances evaluated, adjustments made, and the process repeated until convergence."
  explanation: "Multiple equilibria are coupled: changing the amount of one species affects the partial pressures of all others, shifting every other equilibrium. Unlike a single-reaction problem solvable by a quadratic, real mixtures with many species require matrix-based or iterative methods such as Gibbs minimization with Lagrange multipliers."
```

## Explainer

From thermodynamic properties and equations of state, you know how to characterize the state of a pure substance or a gas mixture — enthalpy, entropy, Gibbs free energy. Now those tools answer a question about *chemical reactions*: given reactants at temperature T and pressure p, which direction does the reaction go, and where does it stop? The organizing principle is Gibbs free energy minimization: at constant T and p, any spontaneous process decreases G, and the system reaches equilibrium when G is minimized over all possible compositions.

For a reaction aA + bB ⇌ cC + dD, the **equilibrium constant** K_p is defined as K_p = (p_C^c × p_D^d) / (p_A^a × p_B^b), where each partial pressure is measured relative to a standard reference pressure (1 atm or 1 bar). At the G-minimizing composition, thermodynamics requires ΔG° = −RT ln K_p, where ΔG° = ΔH° − TΔS° is the **standard Gibbs free energy of reaction**, computable from tabulated enthalpies and entropies of formation. A large K_p (K_p >> 1) means ΔG° << 0 — the reaction strongly favors products at temperature T. A small K_p means reactants are favored. K_p = 1 means neither side is preferred, and the mixture composition is near equal partial pressures.

The temperature dependence of K_p follows the **van't Hoff equation**: d(ln K_p)/dT = ΔH_rxn / (RT²). Integrating: ln(K_p(T₂) / K_p(T₁)) ≈ −(ΔH_rxn/R)(1/T₂ − 1/T₁), valid when ΔH_rxn is approximately constant over the temperature range. For **exothermic reactions** (ΔH_rxn < 0), K_p decreases as temperature rises — consistent with Le Chatelier's principle: heating an exothermic reaction shifts equilibrium toward reactants. For **endothermic reactions**, K_p increases with temperature. In combustion engineering, this matters enormously: high-temperature products have K_p values that force significant dissociation of CO₂ and H₂O back into CO, OH, H, and O.

The practical challenge is that real combustion products are not simply CO₂ and H₂O. At temperatures above roughly 1500 K, minor species — CO, OH, H₂, O, NO — exist in thermodynamic equilibrium at concentrations that cannot be ignored for accurate energy and emissions calculations. Finding the mixture composition requires solving a system of simultaneous equilibrium equations (one K_p expression per independent reaction) coupled with atom-balance constraints (carbon, hydrogen, oxygen, and nitrogen atom counts must match the reactant totals). The system is nonlinear and requires **iterative solution**: assume a composition, evaluate all K_p expressions, check balances, adjust, and repeat until converged.

An equivalent and often more computationally tractable approach is **Gibbs free energy minimization** subject to atom-balance constraints, using Lagrange multipliers. Instead of writing K_p equations, you minimize G(T, p, n₁, n₂, …) where n_i are the mole numbers of each species. This approach scales naturally to dozens or hundreds of species — it's the method used by NASA's Chemical Equilibrium with Applications (CEA) code and similar thermochemical solvers. Both approaches yield the same equilibrium composition; the choice is architectural, not conceptual. Understanding K_p and the van't Hoff equation gives you intuition for *why* composition shifts with temperature; Gibbs minimization gives you the machinery to *compute* it in complex realistic mixtures.
