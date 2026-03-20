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

## Explainer

You already know from chemical equilibrium that reversible reactions reach a balance between forward and reverse processes, described by an equilibrium constant. Solubility equilibria apply that same framework to a specific situation: an ionic solid sitting in water, with some of its ions dissolving and some dissolved ions re-depositing onto the solid. The equilibrium expression for this dissolution is the **solubility product constant, Ksp**. For a salt like silver chloride, AgCl(s) ⇌ Ag⁺(aq) + Cl⁻(aq), the Ksp equals [Ag⁺][Cl⁻]. The solid itself does not appear in the expression — just as with any heterogeneous equilibrium, the activity of a pure solid is 1.

The power of Ksp is that it lets you calculate exactly how much of a sparingly soluble salt dissolves. You set up an ICE table just as you did for gaseous equilibria, but here the "initial" concentrations of the ions are often zero (pure water) and the change is defined by the stoichiometry of dissolution. For a 1:1 salt like AgCl, if x moles per liter dissolve, then [Ag⁺] = x and [Cl⁻] = x, so Ksp = x². For a 1:2 salt like PbCl₂, dissolution produces one Pb²⁺ and two Cl⁻ per formula unit, so Ksp = (x)(2x)² = 4x³. This stoichiometric difference is why you cannot simply compare Ksp values across different salt types to judge relative solubility — you must solve for x (the **molar solubility**) in each case.

The most practical application is predicting whether a precipitate forms when two solutions are mixed. You calculate the **ion product Q** — the same expression as Ksp but using the actual ion concentrations after mixing. If Q > Ksp, the solution is supersaturated and ions will crash out of solution as a solid precipitate until Q drops back to Ksp. If Q < Ksp, the solution can still dissolve more solid. This Q-versus-Ksp comparison is the decision rule for every precipitation problem.

The **common ion effect** is a direct consequence of Le Chatelier's principle applied to dissolution equilibria. If you dissolve AgCl in a solution that already contains Cl⁻ ions (say, from dissolved NaCl), the equilibrium shifts left — toward the solid. The Ksp does not change, but because [Cl⁻] is already elevated, [Ag⁺] must be smaller to maintain the product. In practice, this means AgCl is far less soluble in salt water than in pure water. This effect is widely exploited in qualitative analysis and industrial purification: adding a common ion drives a target compound out of solution selectively.
