---
id: hess-law-of-enthalpy
title: Hess's Law and Enthalpy Calculation
domain: chemistry
course: general-chemistry
prerequisites:
- id: thermochemistry-enthalpy
  type: hard
- id: chemical-equations-balancing
  type: hard
builds-toward:
- bond-energy-and-enthaly
- reaction-coordinate-diagrams
tags:
- Hess's Law
- enthalpy
- reaction pathways
stage: formal-systems
status: draft
---

# Hess's Law and Enthalpy Calculation

## Core Idea
Hess's Law states that enthalpy change is the same regardless of the reaction pathway taken. Reactions can be combined algebraically to calculate ΔH for a target reaction.

## How It's Best Learned
Practice manipulating given reactions (reversing, multiplying) to target a desired reaction and sum their ΔH values.

## Common Misconceptions
Forgetting to reverse the sign of ΔH when reversing a reaction; not adjusting ΔH when multiplying a reaction.

## Explainer

From thermochemistry, you know that every chemical reaction has an associated enthalpy change (ΔH) — the heat absorbed or released at constant pressure. Some reactions are easy to perform in a calorimeter, but many are not: you cannot easily measure the enthalpy of forming carbon monoxide from graphite and oxygen without also producing some CO₂. **Hess's Law** says this does not matter. Because enthalpy is a **state function** — it depends only on the initial and final states, not the path between them — you can calculate ΔH for any reaction by combining other reactions whose ΔH values are already known.

The practical technique works like algebra. Suppose you need ΔH for the reaction A → C, but you only have data for A → B (ΔH₁) and B → C (ΔH₂). Since enthalpy does not care about the route, going from A to B and then from B to C gives the same total ΔH as going directly from A to C: ΔH = ΔH₁ + ΔH₂. This additivity extends to any number of steps. The rules for manipulating reactions are straightforward: if you **reverse** a reaction, the sign of ΔH flips (exothermic becomes endothermic and vice versa); if you **multiply** a reaction by a coefficient, ΔH scales by the same factor. Your skill at balancing chemical equations from prerequisite coursework is essential here — you need to manipulate the given reactions so that intermediate species cancel and only the target reactants and products remain.

Consider a concrete example. Suppose you want ΔH for: C(s) + ½O₂(g) → CO(g). You are given: (1) C(s) + O₂(g) → CO₂(g), ΔH₁ = −393.5 kJ, and (2) CO(g) + ½O₂(g) → CO₂(g), ΔH₂ = −283.0 kJ. The target reaction has CO as a product, but reaction (2) has CO as a reactant — so reverse reaction (2): CO₂(g) → CO(g) + ½O₂(g), ΔH = +283.0 kJ. Now add this to reaction (1): the CO₂ cancels on both sides, and ½O₂ on the product side partially cancels the O₂ on the reactant side, leaving C(s) + ½O₂(g) → CO(g) with ΔH = −393.5 + 283.0 = −110.5 kJ. The key insight is that you never needed to perform this reaction in isolation — Hess's Law let you reconstruct its enthalpy from reactions you could measure.
