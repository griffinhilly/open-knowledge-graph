---
id: stoichiometry-calculations
title: 'Stoichiometric Calculations: From Balanced Equations'
domain: chemistry
course: general-chemistry
prerequisites:
- id: chemical-equations-and-balancing
  type: hard
- id: molar-mass-and-conversions
  type: hard
- id: ratios
  type: soft
builds-toward:
- limiting-reagent-determination
- percent-yield-calculations
tags:
- stoichiometry
- mole ratios
- conversions
- mass-to-mass
stage: formal-systems
status: draft
---

# Stoichiometric Calculations: From Balanced Equations

## Core Idea
Balanced equation coefficients represent mole ratios of reactants and products. Stoichiometry uses these ratios as conversion factors to calculate amounts of any substance from known amounts of others. Conversions typically follow the path: grams → moles → moles of target → grams. Stoichiometry assumes all reactants are present in stoichiometric proportions.

## Questions

```yaml
- question: "In the reaction 2H₂ + O₂ → 2H₂O, if you start with 4.0 mol of H₂ and excess O₂, how many moles of H₂O are produced?"
  type: multiple-choice
  options:
    - "2.0 mol"
    - "4.0 mol"
    - "8.0 mol"
    - "1.0 mol"
  answer: 1
  explanation: "The balanced equation shows a 2:2 (i.e., 1:1) mole ratio between H₂ and H₂O. So 4.0 mol H₂ × (2 mol H₂O / 2 mol H₂) = 4.0 mol H₂O. A common error is using the coefficient 2 as a multiplier rather than reading the ratio correctly."

- question: "The coefficients in a balanced chemical equation represent mass ratios and can be used to convert grams of one substance directly to grams of another."
  type: true-false
  answer: false
  explanation: "Coefficients represent mole ratios, not mass ratios. Different substances have different molar masses, so a 2:1 mole ratio does not mean a 2:1 mass ratio. The correct pathway always converts grams to moles first, applies the mole ratio, then converts back to grams using the target substance's molar mass."

- question: "Describe the four-step conversion pathway used to calculate grams of product from grams of a known reactant in a stoichiometry problem."
  type: short-answer
  answer: "Convert grams of the given substance to moles (divide by its molar mass), use the balanced equation's mole ratio to find moles of the target substance, then convert moles of the target to grams (multiply by its molar mass)."
  explanation: "Stoichiometry always routes through moles because the balanced equation speaks in moles. Molar mass is the bridge between the mass world (grams) and the counting world (moles). Skipping any step — especially the mole ratio — is the most common source of errors in stoichiometry calculations."
```

## Explainer

A balanced chemical equation is more than a description of what reacts with what — it is a quantitative ratio map. When you write 2H₂ + O₂ → 2H₂O, the coefficients say that exactly 2 moles of hydrogen react with 1 mole of oxygen to produce 2 moles of water. These are not suggestions; they are fixed ratios enforced by the conservation of atoms. Stoichiometry is the art of reading those ratios and using them to predict amounts.

The key insight is that the mole is the unit that makes these ratios usable. You learned from molar mass calculations that grams and moles are interconvertible for any substance. Stoichiometry links substances to each other through their mole ratios in the balanced equation. The general four-step path is always: (1) convert your given quantity from grams to moles, (2) apply the mole ratio from the balanced equation, (3) convert the result to grams using the molar mass of the target substance. Every stoichiometry calculation — however complex — follows this road.

A persistent misconception is that you can use the coefficients directly as mass ratios. You cannot. Consider 2H₂ + O₂ → 2H₂O: the 2:1:2 ratio is in moles. In grams, 2 mol H₂ weighs 4 g, 1 mol O₂ weighs 32 g, and 2 mol H₂O weighs 36 g — a completely different ratio. This is why converting through moles is not a bureaucratic formality; it is what makes the calculation chemically meaningful.

It is also worth noting what stoichiometry assumes: that all reactants are present in exactly the proportions required by the equation (stoichiometric proportions), and that the reaction goes to completion. In real chemistry, one reactant often runs out first (the limiting reagent) while another is in excess — that complication is the subject of the next topic. For now, practice the gram–mole–mole–gram pathway until the logic is automatic: write out the unit analysis at each step, confirm units cancel correctly, and you will rarely make an arithmetic error that survives close inspection.
