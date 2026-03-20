---
id: solubility-product-constant-ksp-calculations
title: Solubility Product Constant (Ksp) and Equilibrium
domain: chemistry
course: general-chemistry
prerequisites:
- id: dissolution-equilibrium-and-saturation
  type: hard
- id: chemical-equilibrium
  type: hard
builds-toward:
- precipitation-equilibrium-and-common-ion
tags:
- ksp
- solubility
- equilibrium
- ionic-compounds
stage: advanced
status: draft
---

# Solubility Product Constant (Ksp) and Equilibrium

## Core Idea
The solubility product constant (Ksp) is the equilibrium expression for a dissolution process of an ionic solid. For a sparingly soluble salt, Ksp = [ions]^stoichiometric coefficients at saturation. A small Ksp indicates low solubility; calculating Ksp from solubility data and using Ksp to predict precipitation are core skills.

## How It's Best Learned
Write Ksp expressions for various ionic compounds, calculate Ksp from solubility data, and use Ksp to find solubility. Verify with experimental data.

## Explainer

You already know that dissolving an ionic solid in water is a reversible process — at some point the rate of dissolution equals the rate of precipitation, and the solution is **saturated**. You also know how to write equilibrium expressions for reversible reactions. The solubility product constant, **Ksp**, is simply the equilibrium expression applied to that dissolution process. For a generic salt A_mB_n dissolving as A_mB_n(s) ⇌ mA^n+(aq) + nB^m−(aq), the Ksp expression is Ksp = [A^n+]^m · [B^m−]^n. The solid does not appear in the expression because its activity is constant — exactly the same rule you learned when writing equilibrium expressions for heterogeneous equilibria.

The numerical value of Ksp tells you how far the dissolution proceeds before equilibrium is reached. A very small Ksp (like 1.8 × 10⁻¹⁰ for AgCl) means the ions barely accumulate before the solution is saturated. A larger Ksp means more solid can dissolve. To calculate **molar solubility** from Ksp, define a variable *s* for the moles of salt that dissolve per liter, express each ion concentration in terms of *s* and its stoichiometric coefficient, substitute into the Ksp expression, and solve. For example, if PbCl₂ dissolves as PbCl₂ → Pb²⁺ + 2Cl⁻, then [Pb²⁺] = s and [Cl⁻] = 2s, giving Ksp = (s)(2s)² = 4s³. Solving for *s* yields the molar solubility.

The reverse calculation — finding Ksp from experimental solubility data — follows the same algebra in the opposite direction. If you know that 0.0015 mol of CaF₂ dissolves per liter, you can compute [Ca²⁺] = 0.0015 M and [F⁻] = 0.0030 M, then multiply: Ksp = (0.0015)(0.0030)² = 1.35 × 10⁻⁸. The stoichiometric coefficients matter enormously here — forgetting to double the fluoride concentration (or to square it in the Ksp expression) is the most common arithmetic error.

The real power of Ksp emerges when you compare the **ion product** Q to Ksp. The ion product is calculated identically to Ksp but uses the actual ion concentrations in solution rather than equilibrium values. If Q < Ksp, the solution is unsaturated and more solid can dissolve. If Q > Ksp, the solution is supersaturated and precipitation will occur until Q falls back to Ksp. This comparison is the foundation for predicting whether a precipitate forms when two solutions are mixed — a skill you will use extensively when you move on to precipitation equilibria and the common-ion effect.
