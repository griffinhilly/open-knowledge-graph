---
id: hess-law-enthalpy-of-reaction
title: Hess's Law and Enthalpy Calculations
domain: chemistry
course: general-chemistry
prerequisites:
- id: thermochemistry-enthalpy
  type: hard
- id: chemical-equations-balancing
  type: hard
- id: conservation-of-energy
  type: hard
builds-toward:
- standard-enthalpy-formation
tags:
- hess-law
- enthalpy
- thermochemistry
- calculation
stage: advanced
status: draft
---

# Hess's Law and Enthalpy Calculations

## Core Idea
Hess's law states that enthalpy change depends only on reactants and products, not the pathway. Enthalpy changes of reactions are additive: a reaction can be written as a sum of simpler reactions whose ΔH values combine. This principle allows calculation of hard-to-measure ΔH values from known thermochemical data.

## How It's Best Learned
Practice manipulating and combining thermochemical equations (reversing, multiplying) to yield target reactions, tracking ΔH changes appropriately.

## Explainer

From thermochemistry, you know that every chemical reaction involves an energy change — specifically a change in **enthalpy (ΔH)** at constant pressure, which you can measure as heat released or absorbed. From conservation of energy, you know that energy cannot be created or destroyed. **Hess's law** is the direct consequence of applying conservation of energy to chemical reactions: because enthalpy is a state function (it depends only on the current state of the system, not on how it got there), the total enthalpy change for a reaction is the same regardless of whether the reaction happens in one step or in a series of steps.

Here is a concrete way to think about it. Suppose you want to know the enthalpy change for converting carbon and oxygen into carbon dioxide: C(s) + O₂(g) → CO₂(g). You could measure this directly by burning graphite in pure oxygen in a calorimeter. But suppose instead you only have data for two other reactions: C(s) + ½O₂(g) → CO(g) with ΔH₁ = −110.5 kJ, and CO(g) + ½O₂(g) → CO₂(g) with ΔH₂ = −283.0 kJ. Hess's law says you can simply add these two equations together — the CO produced in the first reaction is consumed in the second, and the net result is C(s) + O₂(g) → CO₂(g) with ΔH = ΔH₁ + ΔH₂ = −393.5 kJ. The intermediate species cancels out, and the enthalpy changes add up, just as distances along a detour must sum to the same displacement as the direct route.

The practical power of Hess's law comes from two manipulation rules. First, if you **reverse** a reaction, the sign of ΔH flips — an exothermic forward reaction becomes an endothermic reverse reaction by the same magnitude. Second, if you **multiply** a reaction by a coefficient, ΔH scales by the same factor — doubling the reaction doubles the heat. These rules let you algebraically combine known thermochemical equations to construct any target reaction. The technique is essentially simultaneous equations: you arrange and scale your known reactions so that all unwanted intermediate species cancel, leaving only the reactants and products of the reaction you care about.

This approach is what makes Hess's law indispensable in chemistry. Many reactions cannot be performed cleanly in a calorimeter — they may be too slow, produce side products, or involve unstable intermediates. But if you can find a set of measurable reactions that, when combined, give the same overall transformation, you can calculate the enthalpy change with confidence. This is also the conceptual foundation for standard enthalpies of formation: by defining ΔH°f as the enthalpy change for forming one mole of a compound from its elements in their standard states, you create a reference system where any reaction's ΔH can be calculated as ΔH°rxn = ΣΔH°f(products) − ΣΔH°f(reactants) — which is itself just Hess's law applied systematically.
