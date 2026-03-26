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
status: validated
---

# Solubility Product Constant (Ksp)

## Core Idea
The solubility product Ksp is the equilibrium constant for dissolution of a sparingly soluble salt. Ksp depends only on temperature; comparing the ionic product to Ksp predicts whether precipitation will occur.

## How It's Best Learned
Calculate Ksp from solubility data, then use Ksp to predict precipitation.

## Common Misconceptions
Confusing Ksp with solubility in g/L; forgetting to include stoichiometric coefficients.

## Questions

```yaml
- question: "Salt X has the formula MX (1:1 stoichiometry, like AgCl) with Ksp = 1.0 × 10⁻¹⁰. Salt Y has the formula MY₂ (1:2 stoichiometry, like CaF₂) with Ksp = 1.0 × 10⁻¹⁰. Which salt has the greater molar solubility?"
  type: multiple-choice
  options:
    - "Salt X, because lower molar solubility always corresponds to smaller Ksp"
    - "Salt Y, because the 1:2 stoichiometry increases the number of ions produced"
    - "Salt Y, because Ksp = 4s³ for 1:2 salts — solving gives a higher s than for Ksp = s² in 1:1 salts"
    - "They are equal, because they have the same Ksp"
  answer: 2
  explanation: "For salt X (MX): Ksp = s² = 1.0 × 10⁻¹⁰, so s = 1.0 × 10⁻⁵ M. For salt Y (MY₂): Ksp = s(2s)² = 4s³ = 1.0 × 10⁻¹⁰, so s = (2.5 × 10⁻¹¹)^(1/3) ≈ 2.9 × 10⁻⁴ M. Salt Y is roughly 30 times more soluble despite having the same Ksp! This is the key insight: identical Ksp values do not mean identical solubilities when stoichiometries differ. The stoichiometric coefficient becomes an exponent in Ksp and a multiplier in the ion concentration, making the relationship between Ksp and molar solubility highly dependent on the formula."

- question: "You mix 50 mL of 0.010 M AgNO₃ with 50 mL of 0.010 M NaCl. Ksp for AgCl = 1.8 × 10⁻¹⁰. What happens?"
  type: multiple-choice
  options:
    - "No precipitate forms because both solutions are dilute"
    - "A precipitate of AgCl forms because Q > Ksp after mixing"
    - "No precipitate forms because Q < Ksp after mixing"
    - "A precipitate forms only if the temperature is above 25°C"
  answer: 1
  explanation: "After mixing equal volumes, concentrations are halved: [Ag⁺] = [Cl⁻] = 0.0050 M. The reaction quotient Q = [Ag⁺][Cl⁻] = (0.0050)(0.0050) = 2.5 × 10⁻⁵. Since Q = 2.5 × 10⁻⁵ >> Ksp = 1.8 × 10⁻¹⁰, the solution is far supersaturated and AgCl will precipitate until the ion product equals Ksp. This is precisely how Q vs. Ksp comparison works: Q > Ksp means the system must shift left (precipitation) to reach equilibrium. Temperature (option D) affects the value of Ksp but is not the determining factor here."

- question: "Two salts can have identical Ksp values but very different molar solubilities if their dissolution stoichiometries differ."
  type: true-false
  answer: true
  explanation: "This is a critical point that students frequently miss. Ksp is a product of ion concentrations raised to stoichiometric powers. For AgCl, Ksp = s². For CaF₂, Ksp = 4s³. If both had Ksp = 1.0 × 10⁻¹⁰, AgCl would have s = 1.0 × 10⁻⁵ M while CaF₂ would have s ≈ 2.9 × 10⁻⁴ M — nearly 30 times more soluble. You cannot rank solubilities simply by comparing Ksp values across salts with different formulas; you must solve for s in each case."

- question: "A salt with a smaller Ksp generally has a lower molar solubility than a salt with a larger Ksp."
  type: true-false
  answer: false
  explanation: "This is false when the salts have different dissolution stoichiometries. The relationship between Ksp and molar solubility s depends on the formula: for MX (1:1), Ksp = s²; for MX₂ (1:2), Ksp = 4s³. A salt with formula MX₂ and Ksp = 1 × 10⁻¹⁰ has s ≈ 2.9 × 10⁻⁴ M, while a salt with formula MX and Ksp = 1 × 10⁻⁸ (a larger Ksp) has s = 1 × 10⁻⁴ M. The 1:2 salt is actually more soluble despite having the smaller Ksp. Direct Ksp comparison is only valid for salts with the same stoichiometry."

- question: "A solution contains 0.050 M Ca²⁺ ions. You slowly add fluoride ions. Using Ksp for CaF₂ = 3.9 × 10⁻¹¹, explain how you would determine the fluoride concentration at which CaF₂ begins to precipitate."
  type: short-answer
  answer: "Precipitation begins when the ion product Q exceeds Ksp. For CaF₂: Q = [Ca²⁺][F⁻]². Set Q = Ksp to find the threshold fluoride concentration: 3.9 × 10⁻¹¹ = (0.050)[F⁻]², so [F⁻]² = 7.8 × 10⁻¹⁰, giving [F⁻] = 2.8 × 10⁻⁵ M. When the fluoride concentration exceeds 2.8 × 10⁻⁵ M, Q > Ksp and precipitation begins."
  explanation: "The reaction quotient Q is evaluated using the actual (current) ion concentrations, while Ksp is the equilibrium value. As long as Q < Ksp, the solution is unsaturated and no precipitation occurs. The moment Q > Ksp, the system is supersaturated and will precipitate until equilibrium is restored. Notice that the fluoride concentration appears squared because of the 1:2 stoichiometry — forgetting this exponent is one of the most common calculation errors with Ksp."
```

## Explainer

You already know that equilibrium constants describe the ratio of products to reactants at equilibrium, and that sparingly soluble salts establish a dynamic equilibrium between the solid and its dissolved ions. The **solubility product constant (Ksp)** is simply the equilibrium constant for that specific dissolution process. For a salt like silver chloride dissolving as AgCl(s) ⇌ Ag⁺(aq) + Cl⁻(aq), the Ksp expression is [Ag⁺][Cl⁻]. The solid does not appear in the expression because, as with all equilibrium constants, pure solids have an activity of 1. A very small Ksp (AgCl has Ksp ≈ 1.8 × 10⁻¹⁰) means vanishingly little dissolves — exactly what "sparingly soluble" means quantitatively.

The stoichiometry matters enormously and is where many errors arise. Consider calcium fluoride: CaF₂(s) ⇌ Ca²⁺(aq) + 2 F⁻(aq). The Ksp expression is [Ca²⁺][F⁻]², and if the molar solubility is s, then [Ca²⁺] = s and [F⁻] = 2s, giving Ksp = s(2s)² = 4s³. Notice this is not simply s² — the coefficient of 2 on fluoride becomes an exponent in the Ksp expression and a multiplier in the concentration. Converting between Ksp and molar solubility requires careful attention to these stoichiometric relationships. Two salts can have identical Ksp values yet very different molar solubilities if their dissolution stoichiometries differ.

The real power of Ksp comes from prediction. You learned about the reaction quotient Q — the same expression as Ksp but evaluated with current (not equilibrium) ion concentrations. Comparing Q to Ksp tells you which direction the system will shift. If Q < Ksp, the solution is unsaturated and more solid can dissolve. If Q > Ksp, the solution is supersaturated and precipitation will occur until Q drops back to Ksp. This is exactly how you predict whether mixing two solutions will produce a precipitate: calculate Q from the initial ion concentrations after mixing, then compare to the tabulated Ksp.

One important subtlety: Ksp tells you about the equilibrium position, not the rate of dissolution or precipitation. A salt with a tiny Ksp is thermodynamically very insoluble, but it might dissolve slowly or quickly depending on kinetics. Also, Ksp applies strictly to the dissolution of a pure ionic solid — it does not account for side reactions like complex ion formation or pH effects on basic anions, both of which can dramatically increase the apparent solubility beyond what Ksp alone would predict.
