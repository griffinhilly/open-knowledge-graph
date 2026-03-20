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
stage: advanced
status: draft
---

# Precipitation Reactions and the Common Ion Effect

## Core Idea
Precipitation occurs when the ionic product Q exceeds Ksp. The common ion effect describes how adding an ion common to a dissolution equilibrium shifts that equilibrium, decreasing the solubility of the original solid. For example, adding chloride ion to a saturated NaCl solution decreases NaCl solubility by shifting the equilibrium left.

## How It's Best Learned
Calculate Q and compare to Ksp to predict whether precipitation occurs. Apply Le Chatelier's principle to understand the common ion effect.

## Explainer

From your work with the solubility product constant (Ksp), you know that every sparingly soluble salt has a characteristic equilibrium expression — for example, AgCl(s) ⇌ Ag⁺(aq) + Cl⁻(aq), with Ksp = [Ag⁺][Cl⁻]. At equilibrium, the product of the ion concentrations equals Ksp. The critical question in practice is: given the actual ion concentrations in a solution, will a precipitate form? The answer comes from comparing the **reaction quotient** (Q) to Ksp.

Q has the same mathematical form as Ksp — it is the product of the current ion concentrations raised to their stoichiometric powers — but Q describes the system *right now*, not necessarily at equilibrium. If Q < Ksp, the solution is unsaturated and no precipitate forms; ions can still dissolve. If Q = Ksp, the solution is exactly saturated and at equilibrium. If Q > Ksp, the ion concentrations exceed what the equilibrium can support, and the excess ions must come out of solution as a solid precipitate until Q drops back to Ksp. This Q-versus-Ksp comparison is the single most important tool for predicting precipitation in any mixing problem.

The **common ion effect** adds an elegant twist. Suppose you have a saturated solution of AgCl at equilibrium, and you add NaCl. The chloride ions from NaCl increase [Cl⁻], which pushes Q above Ksp. The system responds — exactly as Le Chatelier's principle predicts — by shifting the equilibrium to the left: more AgCl precipitates out, reducing [Ag⁺] until the product [Ag⁺][Cl⁻] returns to Ksp. The net result is that AgCl is *less* soluble in a solution that already contains Cl⁻ than in pure water. The ion that both the added salt and the sparingly soluble salt have in common — chloride, in this case — is the **common ion**, and its presence always decreases the solubility of the sparingly soluble salt.

This principle has direct practical applications. In qualitative analysis, chemists exploit the common ion effect to selectively precipitate specific cations by adding the right anion in excess. In water treatment, adjusting ion concentrations controls which salts precipitate. And in biological systems, the balance between dissolved calcium and phosphate ions determines whether bones mineralize or kidney stones form — both governed by the same Q-versus-Ksp logic. Mastering this framework gives you a quantitative handle on solubility that goes far beyond memorizing solubility rules.
