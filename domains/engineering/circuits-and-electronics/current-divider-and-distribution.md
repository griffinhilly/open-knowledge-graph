---
id: current-divider-and-distribution
title: Current Divider Principle and Applications
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: resistive-networks-combinations
  type: hard
- id: ohms-law-and-conductance
  type: hard
builds-toward:
- circuit-laws-kvl-and-kcl
tags:
- current-divider
- parallel-current
- distribution
- inverse-proportionality
stage: formal-systems
status: validated
---

# Current Divider Principle and Applications

## Core Idea
The current divider rule states I₂ = I_total(R₁/(R₁+R₂)) for parallel resistors, showing current distributes inversely with resistance. The rule applies when resistors share identical voltage and no external current injection occurs, revealing that lower-resistance branches carry higher currents.

## Questions

```yaml
- question: "Two resistors R₁ = 10 Ω and R₂ = 90 Ω are connected in parallel with total current I_total = 100 mA entering the node. What is the current through R₂?"
  type: multiple-choice
  options:
    - "90 mA — R₂ is larger so it carries the proportionally larger share of current"
    - "10 mA — the current divider formula gives I₂ = I_total × R₁/(R₁+R₂) = 100 × 10/100"
    - "50 mA — current splits equally between parallel branches regardless of resistance"
    - "9 mA — the formula is I₂ = I_total × R₂/(R₁+R₂) = 100 × 90/100"
  answer: 1
  explanation: "The current divider formula is I₂ = I_total × R₁/(R₁+R₂). Note that R₁ (the *other* resistor) appears in the numerator for I₂. Here: I₂ = 100 mA × 10/(10+90) = 100 × 0.1 = 10 mA. The remaining 90 mA flows through R₁. Current divides inversely with resistance: R₂ is 9× larger than R₁, so it carries 1/9 the current. Option D uses the wrong formula — placing the branch's own resistance in the numerator is the voltage divider pattern, not the current divider."

- question: "One branch of a parallel circuit has its resistance increased by a factor of 10. What happens to the current through the other branch?"
  type: multiple-choice
  options:
    - "The current through the other branch decreases because total current must be shared between fewer effective branches"
    - "The current through the other branch increases, since the high-resistance branch now diverts less current away"
    - "The current through the other branch is unchanged — parallel branches are completely independent"
    - "Both branches carry less current because increasing one resistance raises the total equivalent resistance"
  answer: 1
  explanation: "In a current-driven parallel circuit, total current is fixed. If one branch's resistance increases, that branch carries much less current. By KCL, all current entering the node must leave through some branch — so the remaining branches absorb more. The easier-path branch gets a larger fraction of total current when its competitor becomes harder. Option C is wrong: the branches share the same voltage, but the distribution of current between them shifts when resistance changes. Option D confuses a current source (fixed total current) with a voltage source scenario."

- question: "In a parallel circuit, the branch with the highest resistance carries the most current."
  type: true-false
  answer: false
  explanation: "Current divides *inversely* with resistance. Both parallel branches see the same terminal voltage V. By Ohm's law, I = V/R, so the branch with lower resistance carries more current. Higher resistance is a harder path for current to flow through, so less current takes that route. This is the defining feature of the current divider — it is the opposite of what intuition from series circuits might suggest, where higher resistance means more voltage drop."

- question: "The current divider formula I₂ = I_total × R₁/(R₁+R₂) uses R₁ in the numerator for branch 2's current because both branches share the same voltage, and R₁ determines how large that shared voltage is."
  type: true-false
  answer: true
  explanation: "The appearance of R₁ in the numerator for I₂ is not arbitrary — it reflects the underlying physics. The shared voltage V = I_total × R_eq = I_total × R₁R₂/(R₁+R₂). Since I₂ = V/R₂, substituting gives I₂ = I_total × R₁/(R₁+R₂). A larger R₁ means higher equivalent resistance and higher shared voltage, which drives more current through R₂. The 'other' resistance controls the voltage that in turn drives current through the branch of interest."

- question: "Explain in physical terms why the current divider formula places the opposite resistor's value in the numerator (I₂ involves R₁, not R₂)."
  type: short-answer
  answer: "Parallel branches share the same voltage. Current through any branch is I = V/R. Since both branches see identical voltage, the branch with lower resistance draws more current — it's the easier path. The formula I₂ = I_total × R₁/(R₁+R₂) naturally encodes this: if R₂ is small relative to R₁, the ratio R₁/(R₁+R₂) approaches 1, and branch 2 gets nearly all the current. If R₂ is large, the ratio is small, and branch 2 gets little current. R₁ in the numerator reflects that a large competing resistance means more voltage is available to drive current through branch 2."
  explanation: "The inversion makes sense from the limiting cases. If R₂ → 0 (short circuit), branch 2 should get all the current: R₁/(R₁+0) = 1, so I₂ = I_total. If R₂ → ∞ (open circuit), branch 2 should get no current: R₁/(R₁+∞) → 0, so I₂ = 0. The formula's behavior at extremes confirms the physical intuition — current takes the easiest available path."
```

## Explainer

You already know from Ohm's law that current through a resistor equals voltage divided by resistance: I = V/R. And from your study of resistive network combinations, you know that parallel resistors share the same voltage across their terminals. The current divider rule follows directly from combining these two facts: if the voltage across both parallel branches is identical, then the branch with lower resistance must carry more current, because I = V/R and R is smaller in that branch.

To derive the rule formally, consider two resistors R₁ and R₂ connected in parallel, with total current I_total entering the node. Since both resistors see the same terminal voltage V, the current through each is I₁ = V/R₁ and I₂ = V/R₂. The equivalent resistance of the combination is R_eq = R₁R₂/(R₁+R₂), so V = I_total × R_eq. Substituting into the expression for I₂: I₂ = V/R₂ = I_total × R_eq / R₂ = I_total × R₁/(R₁+R₂). This is the **current divider formula**: the fraction of total current in any branch equals the opposite resistance divided by the sum of resistances. Notice the inversion — R₁ appears in the numerator for I₂, not R₂. Current splits inversely with resistance.

This inverse relationship has a useful physical interpretation: resistance is a measure of how difficult a path is for current to flow. Given a choice between an easy path (small R) and a hard path (large R), current preferentially takes the easier route. If one branch has resistance ten times larger than the other, it carries one-tenth of the current. In the extreme, if one branch is a short circuit (R = 0), it carries all the current and the parallel branch carries none. If one branch is an open circuit (R → ∞), it carries no current and all current flows through the other branch.

The current divider generalizes beyond two branches. For N parallel resistors, the current through branch k is I_k = I_total × (G_k / G_total), where G_k = 1/R_k is the **conductance** of branch k and G_total is the sum of all conductances. This form shows that when working with parallel circuits, conductances add simply just as resistances add simply in series — the two formulations are duals of each other. Recognizing this duality between series (voltage divider, resistances sum) and parallel (current divider, conductances sum) circuits is a conceptual shortcut you will use throughout circuit analysis.
