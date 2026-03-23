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
stage: formal-systems
status: draft
---

# Solution Stoichiometry and Dilution Calculations

## Core Idea
Solution stoichiometry uses molarity and volume to relate quantities in solution reactions. Dilution is calculated using M₁V₁ = M₂V₂, which assumes the number of moles remains constant.

## How It's Best Learned
Practice dilution problems before moving to reaction stoichiometry in solution.

## Questions

```yaml
- question: "You have 25.0 mL of 4.0 M HCl and dilute it to a final volume of 100 mL. What is the new concentration?"
  type: multiple-choice
  options:
    - "16 M — you divided 4.0 by 0.25 because the volume ratio increased"
    - "1.0 M — using M₁V₁ = M₂V₂: (4.0)(25) = M₂(100)"
    - "0.25 M — you multiplied the original molarity by the volume ratio"
    - "4.0 M — dilution doesn't change concentration, only volume"
  answer: 1
  explanation: "M₁V₁ = M₂V₂ gives (4.0 M)(25 mL) = M₂(100 mL), so M₂ = 1.0 M. The moles of HCl before dilution are 0.10 mol; they are still 0.10 mol after — just spread through 4× more solvent. Option D reflects the misconception that dilution doesn't change concentration; option A inverts the ratio. The key is that moles are conserved, not concentration."

- question: "Which statement best describes what happens during a dilution?"
  type: multiple-choice
  options:
    - "The number of moles of solute decreases as more solvent is added, lowering the concentration"
    - "Both moles and molarity stay constant; only the volume of solvent changes"
    - "The number of moles of solute stays constant while the volume increases, so molarity decreases"
    - "The solute chemically reacts with the added water, producing a less concentrated species"
  answer: 2
  explanation: "Dilution is a physical process: you add solvent, increasing volume, but the solute molecules themselves are unchanged and uncreated/undestroyed. The same moles spread through more liquid — hence lower molarity. Option A is the most common misconception (students think 'less concentrated means fewer moles'). Option D confuses dilution with a chemical reaction, which is the other critical distinction in this topic."

- question: "When 50.0 mL of 0.10 M NaOH is mixed with 50.0 mL of 0.10 M HCl, the resulting solution contains NaOH at a concentration of 0.05 M."
  type: true-false
  answer: false
  explanation: "This is a reaction, not a dilution. NaOH + HCl → NaCl + H₂O. Both reactants are present in equal moles (0.0050 mol each), so they completely neutralize each other. The resulting solution contains NaCl and water — essentially no NaOH remains. The M₁V₁ = M₂V₂ equation applies to dilution (adding solvent), not to mixing reactive solutions, where solute is chemically consumed."

- question: "In the equation M₁V₁ = M₂V₂, the equality holds because the number of moles of solute is the same before and after dilution."
  type: true-false
  answer: true
  explanation: "This is exactly right, and understanding why makes the formula trivial: moles = M × V, so if moles are conserved, M₁V₁ must equal M₂V₂. The formula isn't magic — it's just a restatement of moles in = moles out for a process where no solute is added or removed. Contrast this with a reaction, where moles are not conserved and M₁V₁ = M₂V₂ does not apply."

- question: "Explain the key difference between diluting a solution and mixing it with a reactive solute, and why this distinction matters for solving problems."
  type: short-answer
  answer: "In dilution, only solvent is added — the solute molecules are unchanged, so moles of solute are conserved and M₁V₁ = M₂V₂ applies. When a reactive solute is added, a chemical reaction occurs: solute molecules are consumed and new species form, so moles are not conserved and a different approach (stoichiometry with mole ratios) is required."
  explanation: "Confusing these two processes is the most common error in solution stoichiometry. The conceptual test is: does the solute change chemically? If you add water to HCl, HCl is still HCl — dilution, use M₁V₁ = M₂V₂. If you add NaOH to HCl, the acid and base react — stoichiometry, find the limiting reactant, calculate what remains."
```

## Explainer

You already know how to use mole ratios from balanced equations to predict how much product forms from a given amount of reactant — that is stoichiometry. You also know that **molarity** (M = moles of solute per liter of solution) is the standard way to express concentration in solution. Solution stoichiometry combines these two ideas: instead of starting with grams and converting to moles via molar mass, you start with volume and molarity and convert to moles via the relationship moles = M × V. This single equation is the bridge between the liquid in a beaker and the mole ratios in a balanced equation.

**Dilution** is the simplest application. When you add solvent to a solution, you increase volume but do not change the number of moles of solute — you are just spreading the same molecules through more liquid. The relationship **M₁V₁ = M₂V₂** captures this directly: the moles before dilution (M₁ × V₁) equal the moles after dilution (M₂ × V₂). For example, if you have 50 mL of 6.0 M HCl and dilute it to 300 mL, the new concentration is (6.0 × 50)/300 = 1.0 M. The proportion skills you have from math make this algebra second nature — it is just cross-multiplication with units attached.

For reactions in solution, the workflow is: (1) convert volume and molarity to moles for each reactant, (2) use the mole ratio from the balanced equation to identify the limiting reactant, and (3) calculate the moles (and then the concentration or mass) of product. Consider mixing 25.0 mL of 0.10 M AgNO₃ with 15.0 mL of 0.10 M NaCl. You have 0.0025 mol Ag⁺ and 0.0015 mol Cl⁻. The reaction Ag⁺ + Cl⁻ → AgCl is 1:1, so Cl⁻ is limiting and 0.0015 mol AgCl precipitates. The excess Ag⁺ remaining is 0.0010 mol in a total volume of 40.0 mL, giving [Ag⁺] = 0.025 M. Every solution stoichiometry problem follows this same pattern.

One common pitfall is forgetting that volumes are not always additive and that the total volume after mixing is what matters for calculating final concentrations. Another is confusing dilution (adding solvent) with neutralization or reaction (adding another reactant). In dilution, the solute does not change chemically — you are only changing how spread out it is. In a reaction, solute molecules are consumed and new species form. Keeping these two processes distinct — physical dilution versus chemical reaction — prevents errors in both setup and calculation.
