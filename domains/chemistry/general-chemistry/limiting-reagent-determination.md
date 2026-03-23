---
id: limiting-reagent-determination
title: Limiting Reagent and Theoretical Yield
domain: chemistry
course: general-chemistry
prerequisites:
- id: stoichiometry-calculations
  type: hard
builds-toward:
- percent-yield-calculations
tags:
- limiting reagent
- excess reagent
- theoretical yield
stage: formal-systems
status: validated
---

# Limiting Reagent and Theoretical Yield

## Core Idea
In most reactions, one reactant (limiting reagent) is completely consumed while others remain (excess reagents). The limiting reagent determines the maximum amount of product (theoretical yield). Theoretical yield assumes 100% reaction completion. To find the limiting reagent, compare mole amounts to stoichiometric ratios.

## Questions

```yaml
- question: "You combine 10 grams of hydrogen gas (H₂, MW = 2 g/mol) and 10 grams of oxygen gas (O₂, MW = 32 g/mol) for the reaction 2H₂ + O₂ → 2H₂O. Which is the limiting reagent?"
  type: multiple-choice
  options:
    - "Hydrogen, because it has a smaller molecular weight and reacts in a 2:1 ratio with oxygen"
    - "Oxygen, because despite equal masses, it provides far fewer moles and the mole-to-coefficient ratio is much smaller"
    - "Neither — equal masses of reactants means they are mixed in stoichiometric proportions"
    - "Hydrogen, because it is consumed in a 2:1 ratio and you always need more of the reactant with the larger coefficient"
  answer: 1
  explanation: "Convert to moles first: H₂ = 10 g ÷ 2 g/mol = 5 mol; O₂ = 10 g ÷ 32 g/mol = 0.3125 mol. Divide by stoichiometric coefficient: H₂ = 5/2 = 2.5; O₂ = 0.3125/1 = 0.3125. The smaller ratio identifies the limiting reagent — O₂ at 0.3125. Despite equal masses, oxygen runs out far sooner: the 5 mol of H₂ would need only 2.5 mol O₂, but only 0.3125 mol O₂ is present. This illustrates why mass comparison is meaningless — you must compare mole-to-coefficient ratios."

- question: "For the reaction N₂ + 3H₂ → 2NH₃, you have 2 mol N₂ and 3 mol H₂. What is the theoretical yield of NH₃?"
  type: multiple-choice
  options:
    - "4 mol NH₃ — based on 2 mol N₂ reacting fully"
    - "2 mol NH₃ — based on 3 mol H₂ as the limiting reagent"
    - "6 mol NH₃ — based on total moles of reactant"
    - "3 mol NH₃ — based on the average of what each reactant could produce"
  answer: 1
  explanation: "First identify the limiting reagent: divide each by its stoichiometric coefficient — N₂: 2/1 = 2; H₂: 3/3 = 1. H₂ has the smaller ratio, so H₂ is limiting. Calculate yield from the limiting reagent: 3 mol H₂ × (2 mol NH₃ / 3 mol H₂) = 2 mol NH₃. Theoretical yield is always calculated from the limiting reagent's moles. Using 2 mol N₂ would give 4 mol NH₃, but that assumes N₂ is limiting — it is not; H₂ runs out first, preventing more than 2 mol NH₃ from forming."

- question: "If you have more grams of Reactant A than Reactant B in a reaction mixture, Reactant B must be the limiting reagent."
  type: true-false
  answer: false
  explanation: "Grams alone cannot determine the limiting reagent. A large mass of a high-molecular-weight substance may represent far fewer moles than a small mass of a light substance. For example, 100 g of iron (MW = 56) provides 1.79 mol, while 10 g of hydrogen (MW = 2) provides 5 mol. You must always convert to moles and compare mole-to-coefficient ratios. The limiting reagent has the smallest ratio of (moles available)/(stoichiometric coefficient) — which cannot be determined from mass alone."

- question: "The theoretical yield is calculated using the stoichiometry of the limiting reagent, because that is the reactant that determines the maximum amount of product that can form."
  type: true-false
  answer: true
  explanation: "Theoretical yield is the maximum amount of product assuming the limiting reagent reacts completely and with 100% efficiency. Once the limiting reagent is consumed, the reaction stops regardless of how much excess reagent remains. Using stoichiometry from the limiting reagent's mole amount gives the ceiling on product formation. Using the excess reagent's moles would overestimate yield — the reaction cannot produce more product than the limiting reagent allows, since excess reagent has leftover material that never reacts."

- question: "Why must you compare mole-to-coefficient ratios rather than simply comparing masses to identify the limiting reagent?"
  type: short-answer
  answer: "The balanced chemical equation specifies the ratios in which substances react in *moles*, not grams — because moles count actual numbers of molecules, and molecules of different substances have very different masses. Comparing masses directly ignores this: 32 grams of oxygen and 2 grams of hydrogen contain the same number of moles (1 mol each), but the equation 2H₂ + O₂ → 2H₂O requires a 2:1 mole ratio of H₂ to O₂. To find which reactant runs out first, divide each reactant's available moles by its stoichiometric coefficient — this tells you how many 'complete recipe sets' each reactant can provide. The one with the fewest sets is the limiting reagent."
  explanation: "The sandwich analogy captures this: if each sandwich requires 2 slices of bread and 1 slice of cheese, dividing by the recipe coefficient (bread: n/2, cheese: n/1) immediately reveals which ingredient limits production. The same logic applies to reactions, which have their own 'recipe' specified by the balanced equation. Always convert to moles first — the equation speaks in moles, and so must you."
```

## Explainer

From stoichiometry, you know that a balanced equation tells you the exact mole ratios in which reactants combine and products form. But in the real world, you rarely mix reactants in those perfect ratios. When you combine 3 moles of hydrogen with 2 moles of nitrogen for the reaction N₂ + 3H₂ → 2NH₃, the equation demands a 1:3 ratio — you have exactly enough H₂ for 1 mole of N₂, but you have 2 moles of N₂ available. Hydrogen runs out first. The reactant that is completely consumed is the **limiting reagent**, and it determines how much product you can make. The reactant left over is the **excess reagent**.

The systematic way to identify the limiting reagent is to convert each reactant's amount to moles (if not already), then divide each by its stoichiometric coefficient. The reactant with the *smallest* ratio is the limiting reagent. Think of it like assembling sandwiches: if a sandwich requires 2 slices of bread and 1 slice of cheese, and you have 10 slices of bread and 3 slices of cheese, you can only make 3 sandwiches (limited by cheese) even though you have bread for 5. Dividing each ingredient by its "recipe coefficient" — 10/2 = 5 for bread, 3/1 = 3 for cheese — immediately reveals which runs out first.

Once you have identified the limiting reagent, you calculate the **theoretical yield** by using stoichiometry starting *from the limiting reagent's moles*. This is the maximum amount of product the reaction can produce, assuming every molecule of the limiting reagent reacts perfectly. In practice, side reactions, incomplete mixing, and losses during purification mean you get less — the **actual yield** — but the theoretical yield sets the upper bound. You can also calculate how much excess reagent remains by determining how much of it was consumed (using stoichiometry from the limiting reagent) and subtracting from the starting amount.

A common mistake is comparing the *masses* of reactants instead of their mole-to-coefficient ratios. Having more grams of one reactant does not make it the excess reagent — a small mass of a low-molecular-weight substance can represent more moles than a large mass of a heavy substance. Always convert to moles first. This discipline carries forward into percent yield calculations, solution stoichiometry, and every quantitative problem in chemistry: the balanced equation speaks in moles, so you must too.
