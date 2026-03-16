---
id: percent-yield-and-limiting-reagent-analysis
title: Percent Yield and Theoretical Yield Calculations
domain: chemistry
course: general-chemistry
prerequisites:
- id: stoichiometry-calculations
  type: hard
- id: limiting-reagent-calculations
  type: hard
builds-toward:
- gas-stoichiometry
- analytical-chemistry-intro
tags:
- percent yield
- theoretical yield
- actual yield
stage: formal-systems
status: draft
---

# Percent Yield and Theoretical Yield Calculations

## Core Idea
Theoretical yield is the maximum product mass calculated from stoichiometry assuming complete reaction. Percent yield compares actual yield to theoretical yield, accounting for losses in real reactions.

## How It's Best Learned
Calculate theoretical yield first, then use the limiting reagent to find actual yield constraints.

## Common Misconceptions
Assuming percent yield is always 100%; forgetting to account for the limiting reagent.

## Explainer

From stoichiometry, you know how to use a balanced equation to convert between moles of reactants and products. From limiting reagent calculations, you know how to identify which reactant runs out first and therefore determines how much product can form. **Percent yield** ties these skills together by asking: of all the product we *could* have made (according to stoichiometry), how much did we *actually* get?

The calculation has three stages. First, you determine the **theoretical yield** — the maximum mass of product that could form if the reaction went perfectly to completion and the limiting reagent were entirely consumed. This is a pure stoichiometry calculation: identify the limiting reagent, convert its moles to moles of product using the balanced equation's mole ratio, then convert to grams. Second, you measure the **actual yield** — the mass of product you actually isolate after performing the reaction in the lab. Third, you compute percent yield: (actual yield / theoretical yield) × 100%. A reaction that theoretically should produce 10.0 g of product but actually yields 7.8 g has a percent yield of 78%.

Percent yield is virtually never 100% in real chemistry, and understanding why is important. Losses come from many sources: some product may remain dissolved in the solvent and not crystallize out; side reactions may consume some reactant to form unwanted byproducts; transferring materials between containers inevitably leaves small amounts behind; some reactions simply do not go to completion because they reach equilibrium before all reactant is consumed. A percent yield above 90% is generally considered excellent for most laboratory syntheses, while complex organic reactions with multiple steps may have much lower yields — and when steps are sequential, the overall yield is the product of the individual step yields, which can drop alarmingly fast.

The conceptual trap to avoid is confusing theoretical yield with expected yield. The theoretical yield assumes *perfect* conditions — complete reaction, no losses, no side products. It is a ceiling, not a prediction. In practice, experienced chemists use known percent yields from the literature to plan how much starting material they need. If a reaction historically gives 75% yield and you need 15 g of product, you should start with enough reagent to produce a theoretical yield of 20 g. This kind of practical reasoning — working backward from a desired actual yield through percent yield to the required starting quantities — is one of the most common calculations in synthetic chemistry and manufacturing.
