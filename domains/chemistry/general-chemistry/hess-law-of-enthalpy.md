---
id: hess-law-of-enthalpy
title: Hess's Law and Enthalpy Calculation
domain: chemistry
course: general-chemistry
prerequisites:
- id: thermochemistry-enthalpy
  type: hard
- id: chemical-equations-and-balancing
  type: hard
builds-toward:
  - reaction-coordinate-diagrams
tags:
- Hess's Law
- enthalpy
- reaction pathways
stage: formal-systems
status: validated
---
# Hess's Law and Enthalpy Calculation

## Core Idea
Hess's Law states that enthalpy change is the same regardless of the reaction pathway taken. Reactions can be combined algebraically to calculate ΔH for a target reaction.

## How It's Best Learned
Practice manipulating given reactions (reversing, multiplying) to target a desired reaction and sum their ΔH values.

## Common Misconceptions
Forgetting to reverse the sign of ΔH when reversing a reaction; not adjusting ΔH when multiplying a reaction.

## Questions

```yaml
- question: "The reaction CO(g) + ½O₂(g) → CO₂(g) has ΔH = −283.0 kJ. You need to use this reaction in reverse (CO₂ → CO + ½O₂) in a Hess's Law calculation. What ΔH do you assign to the reversed reaction?"
  type: multiple-choice
  options:
    - "−283.0 kJ, because ΔH is a property of the reaction, not the direction"
    - "+283.0 kJ, because reversing the reaction flips the sign of ΔH"
    - "−141.5 kJ, because reversal halves the enthalpy change"
    - "0 kJ, because the CO₂ that forms is immediately consumed"
  answer: 1
  explanation: "When you reverse a reaction, you reverse the direction of heat flow: a reaction that releases 283.0 kJ now requires 283.0 kJ. Mathematically, ΔH_reverse = −ΔH_forward. This follows directly from enthalpy being a state function — the enthalpy difference between two states has equal magnitude but opposite sign depending on which direction you traverse it. The most common error in Hess's Law problems is forgetting to flip the sign when reversing, leading to incorrect final ΔH values."

- question: "A chemist needs ΔH for the reaction: 2C(s) + 2H₂(g) → C₂H₄(g). This reaction is difficult to measure directly because combustion of carbon always produces CO₂ rather than pure ethylene. Why can Hess's Law solve this problem?"
  type: multiple-choice
  options:
    - "Hess's Law allows the chemist to estimate ΔH from bond energies alone, without using any measured data"
    - "Because enthalpy is a state function, ΔH depends only on the initial and final states — so the target ΔH can be calculated by combining measured ΔH values of other reactions in which the same substances appear"
    - "The chemist can run the reaction at very high pressure to force complete conversion to ethylene and measure ΔH directly"
    - "Hess's Law applies only to combustion reactions, so it is not directly applicable here"
  answer: 1
  explanation: "Hess's Law works because enthalpy is a state function: it depends on the identities and states of reactants and products, not on the pathway connecting them. This means ΔH for 2C + 2H₂ → C₂H₄ is fixed regardless of how you get there — including imaginary multi-step paths through measurable intermediate reactions (combustion of carbon, combustion of hydrogen, combustion of ethylene). As long as the measurable reactions can be combined so that intermediate species cancel and only 2C, 2H₂, and C₂H₄ remain, their summed ΔH values equal the target reaction's ΔH. The path is irrelevant; only the endpoint states matter."

- question: "Multiplying a balanced chemical equation by a factor of 3 requires multiplying its ΔH by 3 as well."
  type: true-false
  answer: true
  explanation: "ΔH is an extensive property — it scales with the amount of matter reacting. If the reaction A + B → C has ΔH = −100 kJ, this means 100 kJ is released per mole of reaction as written. If you triple the equation (3A + 3B → 3C), three times as many moles react and three times as much heat is released: ΔH = −300 kJ. This scaling is essential in Hess's Law calculations: when you multiply a reaction to cancel an intermediate, you must apply the same multiplier to ΔH."

- question: "Hess's Law only applies when reactions proceed through the same intermediate steps, since the intermediate compounds must cancel for the law to work."
  type: true-false
  answer: false
  explanation: "This reverses the logic of Hess's Law. The law states that ΔH is the same regardless of the pathway — including any imaginary multi-step paths through intermediates that don't exist in the actual reaction mechanism. The intermediates in a Hess's Law calculation are mathematical constructs used to connect known measurable reactions to the target reaction; they need not reflect any actual reaction mechanism. In fact, the whole power of Hess's Law is that you can construct a purely mathematical path through convenient intermediates specifically to cancel them out algebraically, without those intermediates ever appearing in the real reaction."

- question: "Why does the state-function nature of enthalpy make it possible to calculate ΔH for any reaction from a set of known reactions, even if the target reaction has never been performed?"
  type: short-answer
  answer: "A state function depends only on the current state of the system (temperature, pressure, composition), not on the history of how it got there. For enthalpy, this means ΔH for going from state A to state B is fixed — it equals H(B) − H(A) regardless of whether you go directly from A to B or via states C, D, and E along the way. This allows any multi-step path to serve as a proxy for the unmeasurable direct path. As long as you can construct a series of reactions — by reversing some and multiplying others — such that everything except the target reactants and products cancels algebraically, the sum of their ΔH values equals the ΔH of the direct (unmeasurable) reaction. You are simply exploiting the fact that H is a well-defined function of state, not of path."
  explanation: "The contrast with a path-dependent quantity is illuminating. If you drove from city A to city B via different routes, the distance traveled would vary by route — distance is path-dependent. But the change in altitude from A to B is path-independent — you gain the same net elevation regardless of which road you take. Enthalpy is analogous to altitude: only the start and end states matter, not the route. Hess's Law is the direct application of this path-independence to thermochemical calculations."
```

## Explainer

From thermochemistry, you know that every chemical reaction has an associated enthalpy change (ΔH) — the heat absorbed or released at constant pressure. Some reactions are easy to perform in a calorimeter, but many are not: you cannot easily measure the enthalpy of forming carbon monoxide from graphite and oxygen without also producing some CO₂. **Hess's Law** says this does not matter. Because enthalpy is a **state function** — it depends only on the initial and final states, not the path between them — you can calculate ΔH for any reaction by combining other reactions whose ΔH values are already known.

The practical technique works like algebra. Suppose you need ΔH for the reaction A → C, but you only have data for A → B (ΔH₁) and B → C (ΔH₂). Since enthalpy does not care about the route, going from A to B and then from B to C gives the same total ΔH as going directly from A to C: ΔH = ΔH₁ + ΔH₂. This additivity extends to any number of steps. The rules for manipulating reactions are straightforward: if you **reverse** a reaction, the sign of ΔH flips (exothermic becomes endothermic and vice versa); if you **multiply** a reaction by a coefficient, ΔH scales by the same factor. Your skill at balancing chemical equations from prerequisite coursework is essential here — you need to manipulate the given reactions so that intermediate species cancel and only the target reactants and products remain.

Consider a concrete example. Suppose you want ΔH for: C(s) + ½O₂(g) → CO(g). You are given: (1) C(s) + O₂(g) → CO₂(g), ΔH₁ = −393.5 kJ, and (2) CO(g) + ½O₂(g) → CO₂(g), ΔH₂ = −283.0 kJ. The target reaction has CO as a product, but reaction (2) has CO as a reactant — so reverse reaction (2): CO₂(g) → CO(g) + ½O₂(g), ΔH = +283.0 kJ. Now add this to reaction (1): the CO₂ cancels on both sides, and ½O₂ on the product side partially cancels the O₂ on the reactant side, leaving C(s) + ½O₂(g) → CO(g) with ΔH = −393.5 + 283.0 = −110.5 kJ. The key insight is that you never needed to perform this reaction in isolation — Hess's Law let you reconstruct its enthalpy from reactions you could measure.
