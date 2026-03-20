---
id: standard-enthalpy-formation
title: Standard Enthalpy of Formation and Bond Energies
domain: chemistry
course: general-chemistry
prerequisites:
- id: hess-law-enthalpy-of-reaction
  type: hard
- id: thermochemistry-enthalpy
  type: hard
builds-toward:
- entropy-disorder-randomness-fundamentals
tags:
- enthalpy-of-formation
- bond-energy
- thermochemistry
- standard-state
stage: advanced
status: draft
---

# Standard Enthalpy of Formation and Bond Energies

## Core Idea
Standard enthalpy of formation (ΔH°f) is the enthalpy change when one mole of a compound is formed from its elements in their standard states. ΔH°rxn = Σ(ΔH°f products) − Σ(ΔH°f reactants). Bond dissociation energy (BDE) is the energy required to break a bond; bonds break endothermically and form exothermically, so ΔH ≈ (BDE broken) − (BDE formed).

## Explainer

From Hess's law, you know that enthalpy change depends only on the initial and final states, not the path. **Standard enthalpy of formation** (ΔH°f) exploits this by defining a universal reference point: elements in their most stable forms at 25°C and 1 atm. The ΔH°f of a compound is the enthalpy change for forming exactly one mole of that compound from those elemental building blocks. For example, the ΔH°f of liquid water is the enthalpy change for H₂(g) + ½O₂(g) → H₂O(l). By definition, ΔH°f of any element in its standard state is zero — it is already at the reference point.

This convention transforms Hess's law from a theoretical principle into a practical calculation tool. To find the enthalpy change for any reaction, you treat it as if the reactants decompose back into their elements (costing −ΣΔH°f of reactants) and then those elements recombine into products (releasing ΣΔH°f of products). The formula ΔH°rxn = Σ(ΔH°f products) − Σ(ΔH°f reactants) follows directly. You never need to find a stepwise path between reactants and products — the formation values provide a shortcut through the elements as an intermediate.

**Bond dissociation energies** (BDEs) offer a complementary approach. A BDE is the energy required to homolytically break one specific bond in a gaseous molecule — always a positive number, since breaking bonds requires energy input. To estimate a reaction's enthalpy, you sum the energy needed to break all bonds in the reactants and subtract the energy released when forming all bonds in the products: ΔH ≈ Σ(BDE broken) − Σ(BDE formed). If more energy is released in forming new bonds than was consumed in breaking old ones, the reaction is exothermic.

The two methods are not redundant — they have different strengths. Formation enthalpies give exact values for specific compounds and are tabulated from careful calorimetry. Bond energies are averages across many molecules (the C–H bond energy in methane differs slightly from the C–H in ethane), so BDE calculations are estimates. Use ΔH°f values when they are available and precision matters; use BDEs when you need a quick approximation or when formation data is unavailable, especially for comparing reaction pathways in organic chemistry where you are evaluating which bonds break and form.
