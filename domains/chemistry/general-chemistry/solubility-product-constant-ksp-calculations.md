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

## Questions

```yaml
- question: "For PbCl₂ dissolving as PbCl₂(s) → Pb²⁺(aq) + 2Cl⁻(aq), if the molar solubility is s, which Ksp expression is correct?"
  type: multiple-choice
  options:
    - "Ksp = s × s = s²"
    - "Ksp = s × 2s = 2s²"
    - "Ksp = s × (2s)² = 4s³"
    - "Ksp = (2s)³ = 8s³"
  answer: 2
  explanation: "When s moles of PbCl₂ dissolve, [Pb²⁺] = s and [Cl⁻] = 2s (twice as much Cl⁻ because of the 2:1 stoichiometry). The Ksp expression is [Pb²⁺][Cl⁻]², giving s × (2s)² = s × 4s² = 4s³. The most common error is forgetting to square the chloride concentration — writing s × 2s = 2s² misses that the exponent in the Ksp expression equals the stoichiometric coefficient, not a multiplier."

- question: "A student mixes solutions of AgNO₃ and NaCl. The actual ion concentrations at the moment of mixing give an ion product Q = 5.0 × 10⁻⁸ for AgCl (Ksp = 1.8 × 10⁻¹⁰). What will happen?"
  type: multiple-choice
  options:
    - "No precipitate forms because Q is a small number"
    - "No precipitate forms because Q > Ksp means the solution is unsaturated"
    - "AgCl precipitates because Q > Ksp — the solution is supersaturated"
    - "AgCl precipitates because Q < Ksp — the solution is unsaturated"
  answer: 2
  explanation: "When Q > Ksp, the ion concentrations exceed equilibrium values and the system drives toward precipitation to reduce Q back to Ksp. Option B reverses the logic: Q > Ksp signals supersaturation (too many ions), not unsaturation. Option D has both the comparison and conclusion wrong. The ion product Q is calculated identically to Ksp but uses actual concentrations rather than equilibrium values — this comparison is the core tool for predicting whether precipitation occurs."

- question: "A salt with Ksp = 1.0 × 10⁻¹² (1:1 stoichiometry) is always more soluble than a salt with Ksp = 4.0 × 10⁻¹² (1:2 stoichiometry, like AB₂)."
  type: true-false
  answer: false
  explanation: "You cannot compare molar solubilities by comparing Ksp values alone when stoichiometries differ. For the 1:1 salt: Ksp = s², so s = 1.0 × 10⁻⁶ M. For the 1:2 salt: Ksp = 4s³, so s³ = 1.0 × 10⁻¹², giving s = 1.0 × 10⁻⁴ M — one hundred times more soluble despite its Ksp being only four times larger. The stoichiometric coefficient raises both the concentration and the exponent, making higher-stoichiometry salts relatively more soluble than their Ksp values suggest."

- question: "When Q < Ksp for a sparingly soluble salt, more solid will dissolve if present."
  type: true-false
  answer: true
  explanation: "Q < Ksp means the ion concentrations are below their equilibrium values — the solution is unsaturated. If undissolved solid is present, dissolution will continue (the forward reaction dominates) until ion concentrations rise to the point where Q = Ksp and saturation is reached. This is the direct application of Le Chatelier's principle to dissolution equilibria."

- question: "Why can you not determine which of two ionic salts is more soluble simply by comparing their Ksp values?"
  type: short-answer
  answer: "Ksp values are only directly comparable when the salts have the same stoichiometry (same ion ratio). When stoichiometries differ, the relationship between Ksp and molar solubility s involves different algebraic forms — for a 1:1 salt, Ksp = s²; for a 1:2 salt, Ksp = 4s³. A salt with a larger Ksp can therefore have lower actual solubility than a salt with a smaller Ksp if the stoichiometry raises both the concentration and the exponent in the Ksp expression."
  explanation: "The key is that Ksp is the product of ion concentrations raised to their stoichiometric powers — not just concentrations. A 1:2 salt (AB₂) has Ksp = [A²⁺][B⁻]² = 4s³, which grows much faster with s than does Ksp = s² for a 1:1 salt. So even a modest s value gives a large Ksp for a 1:2 salt. Always solve for s from the Ksp expression; never rank solubilities by Ksp alone unless stoichiometries match."
```

## Explainer

You already know that dissolving an ionic solid in water is a reversible process — at some point the rate of dissolution equals the rate of precipitation, and the solution is **saturated**. You also know how to write equilibrium expressions for reversible reactions. The solubility product constant, **Ksp**, is simply the equilibrium expression applied to that dissolution process. For a generic salt A_mB_n dissolving as A_mB_n(s) ⇌ mA^n+(aq) + nB^m−(aq), the Ksp expression is Ksp = [A^n+]^m · [B^m−]^n. The solid does not appear in the expression because its activity is constant — exactly the same rule you learned when writing equilibrium expressions for heterogeneous equilibria.

The numerical value of Ksp tells you how far the dissolution proceeds before equilibrium is reached. A very small Ksp (like 1.8 × 10⁻¹⁰ for AgCl) means the ions barely accumulate before the solution is saturated. A larger Ksp means more solid can dissolve. To calculate **molar solubility** from Ksp, define a variable *s* for the moles of salt that dissolve per liter, express each ion concentration in terms of *s* and its stoichiometric coefficient, substitute into the Ksp expression, and solve. For example, if PbCl₂ dissolves as PbCl₂ → Pb²⁺ + 2Cl⁻, then [Pb²⁺] = s and [Cl⁻] = 2s, giving Ksp = (s)(2s)² = 4s³. Solving for *s* yields the molar solubility.

The reverse calculation — finding Ksp from experimental solubility data — follows the same algebra in the opposite direction. If you know that 0.0015 mol of CaF₂ dissolves per liter, you can compute [Ca²⁺] = 0.0015 M and [F⁻] = 0.0030 M, then multiply: Ksp = (0.0015)(0.0030)² = 1.35 × 10⁻⁸. The stoichiometric coefficients matter enormously here — forgetting to double the fluoride concentration (or to square it in the Ksp expression) is the most common arithmetic error.

The real power of Ksp emerges when you compare the **ion product** Q to Ksp. The ion product is calculated identically to Ksp but uses the actual ion concentrations in solution rather than equilibrium values. If Q < Ksp, the solution is unsaturated and more solid can dissolve. If Q > Ksp, the solution is supersaturated and precipitation will occur until Q falls back to Ksp. This comparison is the foundation for predicting whether a precipitate forms when two solutions are mixed — a skill you will use extensively when you move on to precipitation equilibria and the common-ion effect.
