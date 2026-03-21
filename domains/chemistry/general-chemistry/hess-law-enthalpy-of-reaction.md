---
id: hess-law-enthalpy-of-reaction
title: Hess's Law and Enthalpy Calculations
domain: chemistry
course: general-chemistry
prerequisites:
- id: thermochemistry-enthalpy
  type: hard
- id: chemical-equations-balancing
  type: hard
- id: conservation-of-energy
  type: hard
builds-toward:
- standard-enthalpy-formation
tags:
- hess-law
- enthalpy
- thermochemistry
- calculation
stage: advanced
status: draft
---

# Hess's Law and Enthalpy Calculations

## Core Idea
Hess's law states that enthalpy change depends only on reactants and products, not the pathway. Enthalpy changes of reactions are additive: a reaction can be written as a sum of simpler reactions whose ΔH values combine. This principle allows calculation of hard-to-measure ΔH values from known thermochemical data.

## How It's Best Learned
Practice manipulating and combining thermochemical equations (reversing, multiplying) to yield target reactions, tracking ΔH changes appropriately.

## Questions

```yaml
- question: "You want ΔH for the reaction A → C, but only have thermochemical data for: A → B (ΔH₁ = −200 kJ) and C → B (ΔH₂ = −50 kJ). How do you correctly combine these to find ΔH for A → C?"
  type: multiple-choice
  options:
    - "Add them directly: ΔH = ΔH₁ + ΔH₂ = −250 kJ"
    - "Reverse the second reaction and add: ΔH = ΔH₁ − ΔH₂ = −200 − (−50) = −150 kJ"
    - "Average the two values: ΔH = (−200 + −50)/2 = −125 kJ"
    - "Subtract the first from the second: ΔH = ΔH₂ − ΔH₁ = −50 − (−200) = +150 kJ"
  answer: 1
  explanation: "To get A → C, you need B to cancel out. The first equation gives A → B. The second equation gives C → B, but you need B → C (to be consumed, not produced). Reversing C → B gives B → C with ΔH = +50 kJ. Now add: (A → B) + (B → C) = A → C, with ΔH = −200 + (+50) = −150 kJ. The rule: when you reverse a reaction, negate its ΔH. This is because enthalpy is a state function — the same energy that is released going forward must be absorbed going backward. Option A is the most tempting error: adding the raw values without recognizing that the second equation needs to be reversed."

- question: "Why is it valid to reverse a thermochemical equation and simply change the sign of ΔH, rather than recalculating it from scratch?"
  type: multiple-choice
  options:
    - "Because all chemical reactions are reversible, so the sign change is always experimentally confirmed"
    - "Because enthalpy is a state function: ΔH depends only on the initial and final states, not the path. Reversing the reaction swaps initial and final states, so ΔH must flip sign to describe the same state difference in the opposite direction"
    - "Because the law of conservation of mass requires that energy be conserved when reactions are reversed"
    - "Because the sign convention for ΔH is arbitrary, so it can be freely changed when convenient"
  answer: 1
  explanation: "The core reason is the state-function nature of enthalpy. A state function's change depends only on where you start and end, not how you get there. If going from state A to state B releases 100 kJ (ΔH = −100 kJ), then going from B back to A must absorb exactly 100 kJ (ΔH = +100 kJ) — because the difference in enthalpy between the two states is fixed by the states themselves. This is fundamentally different from a path-dependent quantity like heat flow in a non-quasistatic process. Hess's law is entirely a consequence of this state-function property."

- question: "Hess's law works because every reaction releases the same total amount of heat regardless of the temperature, pressure, or conditions under which it occurs."
  type: true-false
  answer: false
  explanation: "False. Hess's law works because enthalpy is a state function — the total enthalpy change depends only on the identities of reactants and products, not on the pathway between them. It does NOT say that ΔH is independent of conditions: temperature, pressure, and phase can affect ΔH values (Kirchhoff's law describes temperature dependence). Hess's law applies at a given set of conditions; it says that at those conditions, you can add reactions algebraically. Confusing path-independence (what Hess's law actually claims) with condition-independence (which is false) is a subtle but important error."

- question: "If the combustion of 1 mol of propane releases 2,220 kJ (ΔH = −2,220 kJ), then the combustion of 2 mol of propane has ΔH = −4,440 kJ."
  type: true-false
  answer: true
  explanation: "True. One of the manipulation rules underlying Hess's law is that multiplying a balanced thermochemical equation by any coefficient scales ΔH by the same factor. If burning 1 mol of C₃H₈ releases 2,220 kJ, then burning 2 mol releases twice as much: 4,440 kJ. This scaling rule follows directly from enthalpy being an extensive state function — doubling the amount of substance doubles the enthalpy change. This principle is used constantly in Hess's law calculations: you can multiply any step-reaction by the coefficient needed to balance intermediate species."

- question: "What property of enthalpy makes Hess's law valid, and how does this property differ fundamentally from a path-dependent quantity like the work done against friction?"
  type: short-answer
  answer: "Enthalpy is a state function: its value is determined entirely by the current thermodynamic state of the system (composition, temperature, pressure), not by the history of how that state was reached. Therefore, ΔH for any process equals H_final − H_initial, regardless of pathway. Hess's law follows directly: it doesn't matter whether a reaction occurs in one step or ten steps; the total ΔH equals the sum of the individual ΔH values, because the endpoints are the same. Friction work, by contrast, is path-dependent: sliding a book across a rough table a longer path generates more heat than a shorter path between the same endpoints. There is no analog of Hess's law for frictional work because it has no 'state function' equivalent."
  explanation: "The key conceptual move is understanding why state functions enable additive decomposition. Because enthalpy depends only on endpoints, intermediate states are 'invisible' — they can be added and subtracted freely as long as they cancel. Path-dependent quantities cannot be decomposed this way. This also explains why we can reverse reactions and change signs: we are just relabeling which endpoint is 'initial' and which is 'final.'"
```

## Explainer

From thermochemistry, you know that every chemical reaction involves an energy change — specifically a change in **enthalpy (ΔH)** at constant pressure, which you can measure as heat released or absorbed. From conservation of energy, you know that energy cannot be created or destroyed. **Hess's law** is the direct consequence of applying conservation of energy to chemical reactions: because enthalpy is a state function (it depends only on the current state of the system, not on how it got there), the total enthalpy change for a reaction is the same regardless of whether the reaction happens in one step or in a series of steps.

Here is a concrete way to think about it. Suppose you want to know the enthalpy change for converting carbon and oxygen into carbon dioxide: C(s) + O₂(g) → CO₂(g). You could measure this directly by burning graphite in pure oxygen in a calorimeter. But suppose instead you only have data for two other reactions: C(s) + ½O₂(g) → CO(g) with ΔH₁ = −110.5 kJ, and CO(g) + ½O₂(g) → CO₂(g) with ΔH₂ = −283.0 kJ. Hess's law says you can simply add these two equations together — the CO produced in the first reaction is consumed in the second, and the net result is C(s) + O₂(g) → CO₂(g) with ΔH = ΔH₁ + ΔH₂ = −393.5 kJ. The intermediate species cancels out, and the enthalpy changes add up, just as distances along a detour must sum to the same displacement as the direct route.

The practical power of Hess's law comes from two manipulation rules. First, if you **reverse** a reaction, the sign of ΔH flips — an exothermic forward reaction becomes an endothermic reverse reaction by the same magnitude. Second, if you **multiply** a reaction by a coefficient, ΔH scales by the same factor — doubling the reaction doubles the heat. These rules let you algebraically combine known thermochemical equations to construct any target reaction. The technique is essentially simultaneous equations: you arrange and scale your known reactions so that all unwanted intermediate species cancel, leaving only the reactants and products of the reaction you care about.

This approach is what makes Hess's law indispensable in chemistry. Many reactions cannot be performed cleanly in a calorimeter — they may be too slow, produce side products, or involve unstable intermediates. But if you can find a set of measurable reactions that, when combined, give the same overall transformation, you can calculate the enthalpy change with confidence. This is also the conceptual foundation for standard enthalpies of formation: by defining ΔH°f as the enthalpy change for forming one mole of a compound from its elements in their standard states, you create a reference system where any reaction's ΔH can be calculated as ΔH°rxn = ΣΔH°f(products) − ΣΔH°f(reactants) — which is itself just Hess's law applied systematically.
