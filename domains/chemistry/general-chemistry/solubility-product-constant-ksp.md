---
id: solubility-product-constant-ksp
title: Solubility Product Constant (Ksp)
domain: chemistry
course: general-chemistry
prerequisites:
- id: solubility-equilibria
  type: hard
- id: reaction-quotient
  type: hard
builds-toward:
- common-ion-effect
- complexometric-titration
tags:
- solubility product
- Ksp
- precipitation equilibrium
stage: formal-systems
status: draft
---

# Solubility Product Constant (Ksp)

## Core Idea
The solubility product Ksp is the equilibrium constant for dissolution of a sparingly soluble salt. Ksp depends only on temperature; comparing the ionic product to Ksp predicts whether precipitation will occur.

## How It's Best Learned
Calculate Ksp from solubility data, then use Ksp to predict precipitation.

## Common Misconceptions
Confusing Ksp with solubility in g/L; forgetting to include stoichiometric coefficients.

## Explainer

You already know that equilibrium constants describe the ratio of products to reactants at equilibrium, and that sparingly soluble salts establish a dynamic equilibrium between the solid and its dissolved ions. The **solubility product constant (Ksp)** is simply the equilibrium constant for that specific dissolution process. For a salt like silver chloride dissolving as AgCl(s) ⇌ Ag⁺(aq) + Cl⁻(aq), the Ksp expression is [Ag⁺][Cl⁻]. The solid does not appear in the expression because, as with all equilibrium constants, pure solids have an activity of 1. A very small Ksp (AgCl has Ksp ≈ 1.8 × 10⁻¹⁰) means vanishingly little dissolves — exactly what "sparingly soluble" means quantitatively.

The stoichiometry matters enormously and is where many errors arise. Consider calcium fluoride: CaF₂(s) ⇌ Ca²⁺(aq) + 2 F⁻(aq). The Ksp expression is [Ca²⁺][F⁻]², and if the molar solubility is s, then [Ca²⁺] = s and [F⁻] = 2s, giving Ksp = s(2s)² = 4s³. Notice this is not simply s² — the coefficient of 2 on fluoride becomes an exponent in the Ksp expression and a multiplier in the concentration. Converting between Ksp and molar solubility requires careful attention to these stoichiometric relationships. Two salts can have identical Ksp values yet very different molar solubilities if their dissolution stoichiometries differ.

The real power of Ksp comes from prediction. You learned about the reaction quotient Q — the same expression as Ksp but evaluated with current (not equilibrium) ion concentrations. Comparing Q to Ksp tells you which direction the system will shift. If Q < Ksp, the solution is unsaturated and more solid can dissolve. If Q > Ksp, the solution is supersaturated and precipitation will occur until Q drops back to Ksp. This is exactly how you predict whether mixing two solutions will produce a precipitate: calculate Q from the initial ion concentrations after mixing, then compare to the tabulated Ksp.

One important subtlety: Ksp tells you about the equilibrium position, not the rate of dissolution or precipitation. A salt with a tiny Ksp is thermodynamically very insoluble, but it might dissolve slowly or quickly depending on kinetics. Also, Ksp applies strictly to the dissolution of a pure ionic solid — it does not account for side reactions like complex ion formation or pH effects on basic anions, both of which can dramatically increase the apparent solubility beyond what Ksp alone would predict.
