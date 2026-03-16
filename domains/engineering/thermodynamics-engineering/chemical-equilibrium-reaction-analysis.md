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
stage: advanced
status: draft
---

# Chemical Equilibrium and Equilibrium Constant

## Core Idea
Chemical equilibrium at constant T and P is determined by minimizing Gibbs free energy; the equilibrium constant K_p relates partial pressures of reactants and products. K_p depends on temperature via d(ln K)/dT = ΔH_rxn/(RT²). Real combustion products contain incomplete combustion species (CO, OH, NO) in equilibrium, requiring iterative solution for composition.

## Explainer

From thermodynamic properties and equations of state, you know how to characterize the state of a pure substance or a gas mixture — enthalpy, entropy, Gibbs free energy. Now those tools answer a question about *chemical reactions*: given reactants at temperature T and pressure p, which direction does the reaction go, and where does it stop? The organizing principle is Gibbs free energy minimization: at constant T and p, any spontaneous process decreases G, and the system reaches equilibrium when G is minimized over all possible compositions.

For a reaction aA + bB ⇌ cC + dD, the **equilibrium constant** K_p is defined as K_p = (p_C^c × p_D^d) / (p_A^a × p_B^b), where each partial pressure is measured relative to a standard reference pressure (1 atm or 1 bar). At the G-minimizing composition, thermodynamics requires ΔG° = −RT ln K_p, where ΔG° = ΔH° − TΔS° is the **standard Gibbs free energy of reaction**, computable from tabulated enthalpies and entropies of formation. A large K_p (K_p >> 1) means ΔG° << 0 — the reaction strongly favors products at temperature T. A small K_p means reactants are favored. K_p = 1 means neither side is preferred, and the mixture composition is near equal partial pressures.

The temperature dependence of K_p follows the **van't Hoff equation**: d(ln K_p)/dT = ΔH_rxn / (RT²). Integrating: ln(K_p(T₂) / K_p(T₁)) ≈ −(ΔH_rxn/R)(1/T₂ − 1/T₁), valid when ΔH_rxn is approximately constant over the temperature range. For **exothermic reactions** (ΔH_rxn < 0), K_p decreases as temperature rises — consistent with Le Chatelier's principle: heating an exothermic reaction shifts equilibrium toward reactants. For **endothermic reactions**, K_p increases with temperature. In combustion engineering, this matters enormously: high-temperature products have K_p values that force significant dissociation of CO₂ and H₂O back into CO, OH, H, and O.

The practical challenge is that real combustion products are not simply CO₂ and H₂O. At temperatures above roughly 1500 K, minor species — CO, OH, H₂, O, NO — exist in thermodynamic equilibrium at concentrations that cannot be ignored for accurate energy and emissions calculations. Finding the mixture composition requires solving a system of simultaneous equilibrium equations (one K_p expression per independent reaction) coupled with atom-balance constraints (carbon, hydrogen, oxygen, and nitrogen atom counts must match the reactant totals). The system is nonlinear and requires **iterative solution**: assume a composition, evaluate all K_p expressions, check balances, adjust, and repeat until converged.

An equivalent and often more computationally tractable approach is **Gibbs free energy minimization** subject to atom-balance constraints, using Lagrange multipliers. Instead of writing K_p equations, you minimize G(T, p, n₁, n₂, …) where n_i are the mole numbers of each species. This approach scales naturally to dozens or hundreds of species — it's the method used by NASA's Chemical Equilibrium with Applications (CEA) code and similar thermochemical solvers. Both approaches yield the same equilibrium composition; the choice is architectural, not conceptual. Understanding K_p and the van't Hoff equation gives you intuition for *why* composition shifts with temperature; Gibbs minimization gives you the machinery to *compute* it in complex realistic mixtures.
