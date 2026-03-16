---
id: thermochemistry-formation-properties
title: Thermochemistry and Standard Formation Properties
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: chemical-equilibrium-reaction-analysis
  type: hard
builds-toward:
- chemical-exergy-fuel-combustion
tags:
- thermochemistry
- formation
- enthalpy-formation
- entropy-formation
- standard-state
stage: advanced
status: draft
---

# Thermochemistry and Standard Formation Properties

## Core Idea
Standard formation properties (ΔH°_f, ΔS°_f, ΔG°_f) reference pure elements at 25°C, 1 atm. Reaction enthalpy is ΔH°_rxn = Σ(ν_p ΔH°_f,p) - Σ(ν_r ΔH°_f,r). Temperature dependence uses Kirchhoff's law: (∂ΔH_rxn/∂T)_p = ΔC_p. Reaction spontaneity depends on ΔG°_rxn; tabulated formation properties enable rapid calculation of combustion energy and reaction equilibrium without measurement.

## Explainer

From your study of chemical equilibrium, you know that ΔG°_rxn = −RT ln K, connecting the standard Gibbs free energy change to the equilibrium constant. But where does ΔG°_rxn come from in practice? You cannot measure absolute enthalpy or Gibbs free energy — only differences. Thermochemistry solves this by establishing a universal **reference state**: pure elements in their most stable form at 25°C (298.15 K) and 1 atm pressure are assigned zero formation enthalpy by convention. From this baseline, every compound is characterized by its **standard enthalpy of formation** ΔH°_f — the heat released or absorbed when exactly one mole of that compound is formed from its elements under standard conditions.

The payoff of this convention is **Hess's law in numerical form**. Because enthalpy is a state function (a concept from the first law), the enthalpy change of any reaction depends only on the initial and final states, not the path. You can therefore construct any reaction by algebraically combining formation reactions: ΔH°_rxn = Σ(νᵢ ΔH°_f,products) − Σ(νⱼ ΔH°_f,reactants), where ν are stoichiometric coefficients. Physically, you are "unforming" all the reactants back to elements (negative ΔH°_f terms) and then "forming" the products from those elements (positive ΔH°_f terms). The same algebra applies to entropy and Gibbs free energy, giving you ΔG°_rxn directly from tabulated data — no direct measurement of the actual reaction required.

A critical subtlety: **elements in their reference form have ΔH°_f = 0 by definition**, not because they have no energy, but because they are the chosen reference. O₂(g), N₂(g), C(graphite), and H₂(g) all have zero formation enthalpy. O(g) (atomic oxygen) and C(diamond), however, do not — they are not the most stable reference forms, so forming them from O₂ and graphite requires energy. Getting these reference-form conventions right is essential; using the wrong allotrope or molecular state is a common source of error.

For reactions at temperatures other than 25°C, **Kirchhoff's law** provides the correction: (∂ΔH_rxn/∂T)_P = ΔCₚ, where ΔCₚ is the difference in heat capacities of products minus reactants (weighted by stoichiometry). Integrating this gives ΔH_rxn(T) = ΔH°_rxn + ∫₂₉₈^T ΔCₚ dT. For many engineering combustion problems, ΔCₚ is small and this correction is modest. For high-temperature furnace reactions or industrial processes operating well above 300°C, however, the correction matters significantly and using room-temperature formation data without adjustment introduces real error. The same approach applies to ΔG°_rxn via the Gibbs-Helmholtz equation, connecting thermochemical tables to equilibrium predictions at any temperature.
