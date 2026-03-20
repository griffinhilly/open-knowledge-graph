---
id: solution-stoichiometry-dilution
title: Solution Stoichiometry and Dilution Calculations
domain: chemistry
course: general-chemistry
prerequisites:
- id: solution-concentration
  type: hard
- id: stoichiometry-calculations
  type: hard
- id: proportions
  type: hard
builds-toward:
- acid-base-titration
- redox-titration
tags:
- dilution
- solution stoichiometry
- molarity calculations
stage: advanced
status: draft
---

# Solution Stoichiometry and Dilution Calculations

## Core Idea
Solution stoichiometry uses molarity and volume to relate quantities in solution reactions. Dilution is calculated using M₁V₁ = M₂V₂, which assumes the number of moles remains constant.

## How It's Best Learned
Practice dilution problems before moving to reaction stoichiometry in solution.

## Explainer

You already know how to use mole ratios from balanced equations to predict how much product forms from a given amount of reactant — that is stoichiometry. You also know that **molarity** (M = moles of solute per liter of solution) is the standard way to express concentration in solution. Solution stoichiometry combines these two ideas: instead of starting with grams and converting to moles via molar mass, you start with volume and molarity and convert to moles via the relationship moles = M × V. This single equation is the bridge between the liquid in a beaker and the mole ratios in a balanced equation.

**Dilution** is the simplest application. When you add solvent to a solution, you increase volume but do not change the number of moles of solute — you are just spreading the same molecules through more liquid. The relationship **M₁V₁ = M₂V₂** captures this directly: the moles before dilution (M₁ × V₁) equal the moles after dilution (M₂ × V₂). For example, if you have 50 mL of 6.0 M HCl and dilute it to 300 mL, the new concentration is (6.0 × 50)/300 = 1.0 M. The proportion skills you have from math make this algebra second nature — it is just cross-multiplication with units attached.

For reactions in solution, the workflow is: (1) convert volume and molarity to moles for each reactant, (2) use the mole ratio from the balanced equation to identify the limiting reactant, and (3) calculate the moles (and then the concentration or mass) of product. Consider mixing 25.0 mL of 0.10 M AgNO₃ with 15.0 mL of 0.10 M NaCl. You have 0.0025 mol Ag⁺ and 0.0015 mol Cl⁻. The reaction Ag⁺ + Cl⁻ → AgCl is 1:1, so Cl⁻ is limiting and 0.0015 mol AgCl precipitates. The excess Ag⁺ remaining is 0.0010 mol in a total volume of 40.0 mL, giving [Ag⁺] = 0.025 M. Every solution stoichiometry problem follows this same pattern.

One common pitfall is forgetting that volumes are not always additive and that the total volume after mixing is what matters for calculating final concentrations. Another is confusing dilution (adding solvent) with neutralization or reaction (adding another reactant). In dilution, the solute does not change chemically — you are only changing how spread out it is. In a reaction, solute molecules are consumed and new species form. Keeping these two processes distinct — physical dilution versus chemical reaction — prevents errors in both setup and calculation.
