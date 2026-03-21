---
id: solubility-equilibria
title: Solubility Equilibria
domain: chemistry
course: general-chemistry
prerequisites:
- id: chemical-equilibrium
  type: hard
- id: ionic-bonding
  type: soft
builds-toward:
- electrochemistry-basics
tags:
- Ksp
- solubility-product
- molar-solubility
- common-ion-effect
- precipitation
- ion-product
stage: advanced
status: draft
---
# Solubility Equilibria

## Core Idea
Sparingly soluble ionic compounds establish an equilibrium between the solid and its dissolved ions. The solubility product constant Ksp equals the product of the ion concentrations each raised to their stoichiometric coefficients. Comparing the ion product Q to Ksp predicts whether precipitation occurs: if Q > Ksp, the solution is supersaturated and a precipitate forms; if Q < Ksp, the solution is unsaturated and more solid can dissolve. The common ion effect reduces solubility — adding an ion already present in the equilibrium shifts it toward the solid, decreasing the amount that dissolves.

## How It's Best Learned
Set up ICE tables for dissolution equilibria, being careful with stoichiometric coefficients (e.g., Ca₃(PO₄)₂ produces 3 Ca²⁺ and 2 PO₄³⁻). Practice comparing Q to Ksp with mixing problems where two solutions are combined and you must predict whether a precipitate forms.

## Common Misconceptions
- A small Ksp does not mean nothing dissolves — it means the equilibrium heavily favors the solid, but some ions are always present in solution.
- Ksp values can only be directly compared for salts with the same stoichiometric formula type (e.g., 1:1 salts like AgCl vs PbS). Comparing Ksp across different formula types (1:1 vs 1:2) requires calculating molar solubility.

## Questions

```yaml
- question: "A student dissolves NaCl in water to give a solution containing 0.050 M Cl⁻. She then adds AgNO₃ until [Ag⁺] = 2.0 × 10⁻⁹ M. The Ksp of AgCl is 1.8 × 10⁻¹⁰. Does a precipitate form?"
  type: multiple-choice
  options:
    - "Yes, because Q = [Ag⁺][Cl⁻] = (2.0×10⁻⁹)(0.050) = 1.0×10⁻¹⁰, which is less than Ksp"
    - "No, because Q = 1.0×10⁻¹⁰ < Ksp = 1.8×10⁻¹⁰, so the solution is still unsaturated"
    - "Yes, because Q = (2.0×10⁻⁹)(0.050) = 1.0×10⁻¹⁰ > Ksp = 1.8×10⁻¹⁰"
    - "No, because the common ion (Cl⁻) from NaCl prevents any AgCl from precipitating"
  answer: 1
  explanation: "Q = [Ag⁺][Cl⁻] = (2.0×10⁻⁹)(0.050) = 1.0×10⁻¹⁰. Since Q = 1.0×10⁻¹⁰ < Ksp = 1.8×10⁻¹⁰, the solution is undersaturated and no precipitate forms. Precipitation only occurs when Q > Ksp (supersaturated). Option 4 is a common misconception: the common ion effect does not prevent precipitation — it shifts the equilibrium toward solid, which means a common ion makes precipitation more likely (lowering the threshold for Q > Ksp), not less."

- question: "A student looks up Ksp values: AgCl has Ksp = 1.8×10⁻¹⁰ and PbI₂ has Ksp = 9.8×10⁻⁹. She concludes that PbI₂ is more soluble because its Ksp is larger. Is her reasoning correct?"
  type: multiple-choice
  options:
    - "Yes — a larger Ksp always means greater molar solubility, regardless of salt formula"
    - "No — Ksp values can only be directly compared for salts with the same stoichiometric formula type; she must calculate molar solubility (x) for each salt individually"
    - "Yes — both are sparingly soluble salts, so their Ksp values are directly comparable"
    - "No — Ksp comparisons are only meaningful for salts that share a common ion"
  answer: 1
  explanation: "For AgCl (1:1 formula): Ksp = x², so x = √(1.8×10⁻¹⁰) ≈ 1.3×10⁻⁵ M. For PbI₂ (1:2 formula): Ksp = (x)(2x)² = 4x³, so x = (Ksp/4)^(1/3) = (9.8×10⁻⁹/4)^(1/3) ≈ 1.3×10⁻³ M. PbI₂ is indeed about 100 times more soluble — but this is because the different stoichiometry changes the relationship between Ksp and x, not simply because the Ksp is larger. A 1:2 salt can have a larger Ksp than a 1:1 salt yet still be less soluble, depending on the specific values. You must always solve for molar solubility."

- question: "Adding NaCl to a saturated AgCl solution at equilibrium will cause additional AgCl to precipitate out of solution."
  type: true-false
  answer: true
  explanation: "This is the common ion effect, a direct application of Le Chatelier's principle. The dissolution equilibrium is AgCl(s) ⇌ Ag⁺(aq) + Cl⁻(aq). Adding NaCl introduces additional Cl⁻ ions, increasing [Cl⁻] above the equilibrium value and making Q > Ksp. The system responds by shifting left — toward the solid — until equilibrium is re-established at a lower [Ag⁺]. The Ksp does not change, but the solubility of AgCl (the amount that dissolves per liter) decreases substantially. This is why ionic compounds are far less soluble in solutions containing a common ion than in pure water."

- question: "A compound with a very small Ksp (e.g., 10⁻³⁰) releases no detectable ions into solution — it is effectively insoluble."
  type: true-false
  answer: false
  explanation: "No ionic compound is truly insoluble — equilibrium always requires some dissolved ions to be present. For AgI with Ksp ≈ 8×10⁻¹⁷, the molar solubility in pure water is √(8×10⁻¹⁷) ≈ 9×10⁻⁹ M — extremely small but not zero. Even compounds with Ksp ~ 10⁻³⁰ have some ions in solution at equilibrium, just at concentrations far below what is analytically detectable. 'Sparingly soluble' and 'slightly soluble' are the correct technical terms; 'insoluble' is a practical simplification, not a physical truth. This distinction matters in contexts like selective precipitation, where tiny differences in solubility are exploited analytically."

- question: "Explain why AgCl dissolves to a much smaller extent in a 0.10 M NaCl solution than in pure water, even though the Ksp of AgCl has not changed."
  type: short-answer
  answer: "Ksp is a constant: [Ag⁺][Cl⁻] must equal Ksp = 1.8×10⁻¹⁰ at equilibrium. In pure water, both ions come only from AgCl dissolution, so [Ag⁺] = [Cl⁻] = x ≈ 1.3×10⁻⁵ M. In 0.10 M NaCl, the solution already contains [Cl⁻] = 0.10 M from the salt. To satisfy Ksp, [Ag⁺] = Ksp/[Cl⁻] = 1.8×10⁻¹⁰/0.10 = 1.8×10⁻⁹ M. The solubility of AgCl has dropped from 1.3×10⁻⁵ M to 1.8×10⁻⁹ M — about 7,000-fold reduction. The Ksp is unchanged; what changes is how much AgCl needs to dissolve to reach equilibrium when one ion is already present at high concentration."
  explanation: "This is the common ion effect expressed quantitatively. Le Chatelier's principle describes the direction (equilibrium shifts toward solid), and the Ksp expression gives the magnitude (the ion product must still equal Ksp). The key conceptual point is that Ksp constrains the product of ion concentrations, so if one concentration is forced high by an external source, the other must be proportionally low — meaning less of the compound can dissolve."
```

## Explainer

You already know from chemical equilibrium that reversible reactions reach a balance between forward and reverse processes, described by an equilibrium constant. Solubility equilibria apply that same framework to a specific situation: an ionic solid sitting in water, with some of its ions dissolving and some dissolved ions re-depositing onto the solid. The equilibrium expression for this dissolution is the **solubility product constant, Ksp**. For a salt like silver chloride, AgCl(s) ⇌ Ag⁺(aq) + Cl⁻(aq), the Ksp equals [Ag⁺][Cl⁻]. The solid itself does not appear in the expression — just as with any heterogeneous equilibrium, the activity of a pure solid is 1.

The power of Ksp is that it lets you calculate exactly how much of a sparingly soluble salt dissolves. You set up an ICE table just as you did for gaseous equilibria, but here the "initial" concentrations of the ions are often zero (pure water) and the change is defined by the stoichiometry of dissolution. For a 1:1 salt like AgCl, if x moles per liter dissolve, then [Ag⁺] = x and [Cl⁻] = x, so Ksp = x². For a 1:2 salt like PbCl₂, dissolution produces one Pb²⁺ and two Cl⁻ per formula unit, so Ksp = (x)(2x)² = 4x³. This stoichiometric difference is why you cannot simply compare Ksp values across different salt types to judge relative solubility — you must solve for x (the **molar solubility**) in each case.

The most practical application is predicting whether a precipitate forms when two solutions are mixed. You calculate the **ion product Q** — the same expression as Ksp but using the actual ion concentrations after mixing. If Q > Ksp, the solution is supersaturated and ions will crash out of solution as a solid precipitate until Q drops back to Ksp. If Q < Ksp, the solution can still dissolve more solid. This Q-versus-Ksp comparison is the decision rule for every precipitation problem.

The **common ion effect** is a direct consequence of Le Chatelier's principle applied to dissolution equilibria. If you dissolve AgCl in a solution that already contains Cl⁻ ions (say, from dissolved NaCl), the equilibrium shifts left — toward the solid. The Ksp does not change, but because [Cl⁻] is already elevated, [Ag⁺] must be smaller to maintain the product. In practice, this means AgCl is far less soluble in salt water than in pure water. This effect is widely exploited in qualitative analysis and industrial purification: adding a common ion drives a target compound out of solution selectively.
