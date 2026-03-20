---
id: limiting-reagent-calculations
title: Limiting Reagent Calculations
domain: chemistry
course: general-chemistry
prerequisites:
- id: stoichiometry-calculations
  type: hard
- id: ratios
  type: soft
- id: optimization-problems
  type: soft
builds-toward:
- gas-stoichiometry
tags:
- limiting-reagent
- excess-reagent
- theoretical-yield
- percent-yield
- stoichiometry
stage: advanced
status: draft
---
# Limiting Reagent Calculations

## Core Idea
When reactants are not present in exact stoichiometric proportions, one reactant is consumed first — the limiting reagent — and determines the maximum amount of product (theoretical yield). The other reactant(s) remain in excess. Percent yield compares the actual yield obtained experimentally to the theoretical yield: %yield = (actual/theoretical) × 100. Identifying the limiting reagent requires converting all reactant quantities to moles and comparing their mole ratios to the balanced equation's coefficients.

## How It's Best Learned
For each reactant, calculate how much product it could produce if it were completely consumed. The reactant that produces the least product is the limiting reagent. Practice with two-reactant problems first, then extend to three or more. Always check your answer by verifying the excess reactant is not fully consumed.

## Common Misconceptions
- The limiting reagent is not necessarily the one present in the smallest mass or smallest number of moles — it is the one that runs out first relative to the stoichiometric ratio.
- Percent yield can never exceed 100% in a properly conducted experiment. Values above 100% indicate impurities, incomplete drying, or measurement error.

## Explainer

Stoichiometry — your prerequisite — taught you to convert between moles of reactants and products using the coefficients of a balanced equation. But those calculations assumed that reactants were present in perfect proportions, which almost never happens in practice. In real reactions, you typically have more of one reactant than you need, and the reaction stops when the first reactant runs out. The **limiting reagent** is the reactant that is completely consumed first, and it alone determines how much product can form.

Think of it like making sandwiches. If you have 10 slices of bread and 3 slices of cheese, each sandwich requiring 2 slices of bread and 1 slice of cheese, you can make only 3 sandwiches — the cheese limits you, even though you have plenty of bread. Four slices of bread are left over (the **excess reagent**). The same logic applies to chemical reactions: you must compare what you *have* to what the balanced equation *requires*, and the reactant that runs out first controls the outcome.

The systematic method works as follows. For each reactant, convert its given quantity (usually grams) to moles using the molar mass. Then, for each reactant, calculate how many moles of product it *could* produce if it were entirely consumed — use the mole ratio from the balanced equation. The reactant that produces the **least** product is the limiting reagent. The amount of product it can produce is the **theoretical yield** — the maximum possible under ideal conditions. For example, if you react 10.0 g of hydrogen with 80.0 g of oxygen to form water (2H₂ + O₂ → 2H₂O), convert both to moles: 10.0 g H₂ = 4.96 mol, 80.0 g O₂ = 2.50 mol. Hydrogen could produce 4.96 mol H₂O; oxygen could produce 5.00 mol H₂O. Hydrogen produces less, so it is the limiting reagent, and the theoretical yield is 4.96 mol H₂O (89.3 g).

In the laboratory, you rarely obtain the full theoretical yield due to side reactions, incomplete reactions, transfer losses, or purification steps. **Percent yield** quantifies this gap: %yield = (actual yield / theoretical yield) × 100. If you actually collected 78.0 g of water in the example above, your percent yield would be (78.0 / 89.3) × 100 = 87.3%. A critical check: if your calculated percent yield exceeds 100%, something is wrong — your product is likely impure, incompletely dried, or your mass measurements contain errors. Percent yield is how chemists evaluate the efficiency and quality of a reaction, and it depends entirely on correctly identifying the limiting reagent first.
