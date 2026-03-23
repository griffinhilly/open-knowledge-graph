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
stage: formal-systems
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

## Questions

```yaml
- question: "Consider the reaction N₂ + 3H₂ → 2NH₃. A chemist mixes 2.0 mol N₂ with 3.0 mol H₂. Which is the limiting reagent?"
  type: multiple-choice
  options:
    - "N₂, because it is present in fewer moles"
    - "H₂, because it is present in more moles and will be consumed faster"
    - "H₂, because 2.0 mol N₂ requires 6.0 mol H₂ but only 3.0 mol H₂ is available"
    - "Neither — the reactants are in the correct stoichiometric ratio"
  answer: 2
  explanation: "The stoichiometric ratio requires 3 mol H₂ per mol N₂. For 2.0 mol N₂, you need 6.0 mol H₂, but only 3.0 mol is present — H₂ runs out first. Options A and B both make the common error of comparing raw amounts rather than checking against the required ratio. Option D is wrong: the ratio 2:3 ≠ 1:3 required by the equation."

- question: "In an experiment producing aspirin, a student obtains 4.2 g of product. The theoretical yield calculated from the limiting reagent is 3.8 g. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The student was exceptionally skilled and exceeded the maximum possible yield"
    - "The product contains impurities or retained solvent, making its measured mass artificially high"
    - "The limiting reagent calculation was done correctly but percent yield can legitimately exceed 100%"
    - "The excess reagent contributed additional mass to the product"
  answer: 1
  explanation: "Percent yield cannot exceed 100% in a correctly conducted experiment — the theoretical yield is the absolute ceiling set by conservation of mass and stoichiometry. A yield above 100% invariably means the product is not pure: residual solvent, unreacted reagents, or other impurities add mass. Options A and C both treat >100% yield as achievable, which is physically impossible. Excess reagent does not incorporate into the product."

- question: "The limiting reagent in a reaction is always the reactant present in the smallest number of moles."
  type: true-false
  answer: false
  explanation: "This is one of the most common misconceptions in stoichiometry. The limiting reagent is determined by comparing mole amounts to the stoichiometric coefficients — not by comparing mole amounts to each other. A reaction requiring 3 mol of A for every 1 mol of B could have A as the limiting reagent even if you have 10 mol of A and only 1 mol of B, if 10 mol of A is insufficient to react with 1 mol of B at the required ratio. Always divide available moles by the stoichiometric coefficient and compare."

- question: "Once the limiting reagent is fully consumed, the reaction stops even if other reactants remain in the flask."
  type: true-false
  answer: true
  explanation: "By definition, the limiting reagent is what limits the reaction. When it is gone, there are no more molecules of that species to react — even abundant excess reagent cannot drive the reaction further. This is exactly why identifying the limiting reagent first is essential: all yield calculations must be based on it, not on the excess reagent."

- question: "Why is it insufficient to simply compare the number of moles of each reactant to determine the limiting reagent? What must you compare instead, and why?"
  type: short-answer
  answer: "You must compare each reactant's available moles to the amount required by the stoichiometric ratio (i.e., available moles divided by its coefficient), or equivalently, calculate how much product each reactant could produce if fully consumed. Raw mole amounts are meaningless without knowing the ratio in which reactants combine. A reaction requiring 1:3 A:B means having twice as many moles of B as A still leaves B as the potentially limiting reagent — the balanced equation's coefficients define the 'recipe,' and the limiting reagent is whichever ingredient runs short relative to that recipe."
  explanation: "The sandwich analogy makes this concrete: 3 slices of cheese and 10 slices of bread for sandwiches requiring 2 bread + 1 cheese — cheese limits you to 3 sandwiches despite being present in fewer pieces, because the recipe calls for 2 bread per cheese and bread is abundant."
```

## Explainer

Stoichiometry — your prerequisite — taught you to convert between moles of reactants and products using the coefficients of a balanced equation. But those calculations assumed that reactants were present in perfect proportions, which almost never happens in practice. In real reactions, you typically have more of one reactant than you need, and the reaction stops when the first reactant runs out. The **limiting reagent** is the reactant that is completely consumed first, and it alone determines how much product can form.

Think of it like making sandwiches. If you have 10 slices of bread and 3 slices of cheese, each sandwich requiring 2 slices of bread and 1 slice of cheese, you can make only 3 sandwiches — the cheese limits you, even though you have plenty of bread. Four slices of bread are left over (the **excess reagent**). The same logic applies to chemical reactions: you must compare what you *have* to what the balanced equation *requires*, and the reactant that runs out first controls the outcome.

The systematic method works as follows. For each reactant, convert its given quantity (usually grams) to moles using the molar mass. Then, for each reactant, calculate how many moles of product it *could* produce if it were entirely consumed — use the mole ratio from the balanced equation. The reactant that produces the **least** product is the limiting reagent. The amount of product it can produce is the **theoretical yield** — the maximum possible under ideal conditions. For example, if you react 10.0 g of hydrogen with 80.0 g of oxygen to form water (2H₂ + O₂ → 2H₂O), convert both to moles: 10.0 g H₂ = 4.96 mol, 80.0 g O₂ = 2.50 mol. Hydrogen could produce 4.96 mol H₂O; oxygen could produce 5.00 mol H₂O. Hydrogen produces less, so it is the limiting reagent, and the theoretical yield is 4.96 mol H₂O (89.3 g).

In the laboratory, you rarely obtain the full theoretical yield due to side reactions, incomplete reactions, transfer losses, or purification steps. **Percent yield** quantifies this gap: %yield = (actual yield / theoretical yield) × 100. If you actually collected 78.0 g of water in the example above, your percent yield would be (78.0 / 89.3) × 100 = 87.3%. A critical check: if your calculated percent yield exceeds 100%, something is wrong — your product is likely impure, incompletely dried, or your mass measurements contain errors. Percent yield is how chemists evaluate the efficiency and quality of a reaction, and it depends entirely on correctly identifying the limiting reagent first.
