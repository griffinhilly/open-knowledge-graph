---
id: precipitation-equilibrium-and-common-ion
title: Precipitation Reactions and the Common Ion Effect
domain: chemistry
course: general-chemistry
prerequisites:
- id: solubility-product-constant-ksp-calculations
  type: hard
builds-toward:
- analytical-chemistry-intro
- qualitative-analysis
tags:
- precipitation
- ksp
- common-ion-effect
- solubility
stage: formal-systems
status: draft
---

# Precipitation Reactions and the Common Ion Effect

## Core Idea
Precipitation occurs when the ionic product Q exceeds Ksp. The common ion effect describes how adding an ion common to a dissolution equilibrium shifts that equilibrium, decreasing the solubility of the original solid. For example, adding chloride ion to a saturated NaCl solution decreases NaCl solubility by shifting the equilibrium left.

## How It's Best Learned
Calculate Q and compare to Ksp to predict whether precipitation occurs. Apply Le Chatelier's principle to understand the common ion effect.

## Questions

```yaml
- question: "A saturated solution of AgCl is prepared in pure water. You then dissolve NaCl (a soluble salt) into this solution. What happens and why?"
  type: multiple-choice
  options:
    - "More AgCl dissolves because the additional Na⁺ ions disrupt the existing equilibrium"
    - "The AgCl solubility is unaffected because Cl⁻ is already present in the solution"
    - "AgCl precipitates further because the increased [Cl⁻] pushes Q above Ksp, forcing the equilibrium left"
    - "The Ksp of AgCl increases to accommodate the extra Cl⁻ ions"
  answer: 2
  explanation: "Adding NaCl introduces Cl⁻ into a solution already at equilibrium for AgCl. This raises [Cl⁻], making Q = [Ag⁺][Cl⁻] exceed Ksp. The system restores equilibrium by shifting left — Ag⁺ and Cl⁻ ions combine to form more solid AgCl, reducing [Ag⁺] until Q returns to Ksp. The AgCl is now less soluble than in pure water. Note that Ksp is a constant at fixed temperature and cannot change — only the equilibrium position shifts."

- question: "You mix 100 mL of 0.001 M AgNO₃ with 100 mL of 0.001 M NaCl. The Ksp of AgCl is 1.8 × 10⁻¹⁰. What do you predict?"
  type: multiple-choice
  options:
    - "No precipitate forms because both solutions are dilute"
    - "A precipitate forms because Q > Ksp after mixing"
    - "No precipitate forms because Q = Ksp after mixing"
    - "The solution becomes supersaturated but no precipitate forms until heated"
  answer: 1
  explanation: "After mixing, concentrations are halved: [Ag⁺] = 5 × 10⁻⁴ M and [Cl⁻] = 5 × 10⁻⁴ M. Q = (5 × 10⁻⁴)(5 × 10⁻⁴) = 2.5 × 10⁻⁷, which far exceeds Ksp = 1.8 × 10⁻¹⁰. Since Q > Ksp, the solution is supersaturated and AgCl precipitates until the ion product drops to Ksp. The diluteness of the starting solutions is irrelevant — what matters is whether the product of the mixed concentrations exceeds Ksp."

- question: "The common ion effect decreases the solubility of a sparingly soluble salt by lowering the Ksp of that salt."
  type: true-false
  answer: false
  explanation: "Ksp is a thermodynamic equilibrium constant that depends only on temperature — it cannot be changed by adding ions to the solution. The common ion effect decreases solubility by shifting the dissolution equilibrium to the left (toward more solid), not by altering Ksp itself. The same Ksp is maintained; what changes is the equilibrium position between dissolved ions and solid. This is a Le Chatelier's principle effect on the position of equilibrium, not a change in the equilibrium constant."

- question: "If Q < Ksp for a sparingly soluble salt, more of that salt will dissolve into the solution if added."
  type: true-false
  answer: true
  explanation: "Q < Ksp means the solution is unsaturated — the ion product is below the equilibrium value, so the system has not yet reached saturation. The dissolution reaction proceeds forward (dissolving more solid) to increase ion concentrations until Q = Ksp. Only when Q = Ksp does the rate of dissolution equal the rate of precipitation and net dissolution ceases. If Q > Ksp, the system is supersaturated and precipitation occurs instead."

- question: "Explain the conceptual role of Q (the reaction quotient) in predicting whether a precipitate will form when two solutions are mixed."
  type: short-answer
  answer: "Q is calculated from the actual ion concentrations immediately after mixing, using the same mathematical form as Ksp. Comparing Q to Ksp indicates the system's direction of change: if Q < Ksp the solution is unsaturated and no precipitate forms; if Q = Ksp the solution is at equilibrium; if Q > Ksp the ion product exceeds what equilibrium can sustain, and solid precipitates until ion concentrations decrease enough that Q equals Ksp. Q is the snapshot of the system's current state, while Ksp is the target equilibrium state."
  explanation: "The Q-vs-Ksp comparison generalizes across all equilibria, not just precipitation. In the context of sparingly soluble salts, it provides a quantitative prediction that memorized solubility rules cannot. Any mixing problem — whether two solutions are combined or a common ion is added to a saturated solution — can be handled by calculating Q and comparing it to Ksp."
```

## Explainer

From your work with the solubility product constant (Ksp), you know that every sparingly soluble salt has a characteristic equilibrium expression — for example, AgCl(s) ⇌ Ag⁺(aq) + Cl⁻(aq), with Ksp = [Ag⁺][Cl⁻]. At equilibrium, the product of the ion concentrations equals Ksp. The critical question in practice is: given the actual ion concentrations in a solution, will a precipitate form? The answer comes from comparing the **reaction quotient** (Q) to Ksp.

Q has the same mathematical form as Ksp — it is the product of the current ion concentrations raised to their stoichiometric powers — but Q describes the system *right now*, not necessarily at equilibrium. If Q < Ksp, the solution is unsaturated and no precipitate forms; ions can still dissolve. If Q = Ksp, the solution is exactly saturated and at equilibrium. If Q > Ksp, the ion concentrations exceed what the equilibrium can support, and the excess ions must come out of solution as a solid precipitate until Q drops back to Ksp. This Q-versus-Ksp comparison is the single most important tool for predicting precipitation in any mixing problem.

The **common ion effect** adds an elegant twist. Suppose you have a saturated solution of AgCl at equilibrium, and you add NaCl. The chloride ions from NaCl increase [Cl⁻], which pushes Q above Ksp. The system responds — exactly as Le Chatelier's principle predicts — by shifting the equilibrium to the left: more AgCl precipitates out, reducing [Ag⁺] until the product [Ag⁺][Cl⁻] returns to Ksp. The net result is that AgCl is *less* soluble in a solution that already contains Cl⁻ than in pure water. The ion that both the added salt and the sparingly soluble salt have in common — chloride, in this case — is the **common ion**, and its presence always decreases the solubility of the sparingly soluble salt.

This principle has direct practical applications. In qualitative analysis, chemists exploit the common ion effect to selectively precipitate specific cations by adding the right anion in excess. In water treatment, adjusting ion concentrations controls which salts precipitate. And in biological systems, the balance between dissolved calcium and phosphate ions determines whether bones mineralize or kidney stones form — both governed by the same Q-versus-Ksp logic. Mastering this framework gives you a quantitative handle on solubility that goes far beyond memorizing solubility rules.
