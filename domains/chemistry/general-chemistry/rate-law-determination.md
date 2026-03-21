---
id: rate-law-determination
title: Rate Law Determination
domain: chemistry
course: general-chemistry
prerequisites:
- id: chemical-kinetics
  type: hard
builds-toward:
- integrated-rate-laws
tags:
- rate-law
- method-of-initial-rates
- reaction-order
- rate-constant
- experimental-kinetics
stage: advanced
status: draft
---
# Rate Law Determination

## Core Idea
The rate law expresses reaction rate as a function of reactant concentrations: rate = k[A]ᵐ[B]ⁿ, where k is the rate constant and m and n are the reaction orders with respect to each reactant. Reaction orders are determined experimentally, not from stoichiometric coefficients. The method of initial rates compares experiments where one reactant concentration is changed while others are held constant: if doubling [A] doubles the rate, the reaction is first order in A; if doubling [A] quadruples the rate, it is second order in A. The overall order is the sum of individual orders (m + n + ...).

## How It's Best Learned
Set up ratio equations from pairs of experiments that isolate one variable at a time. Practice recognizing common patterns: rate unchanged when concentration doubles (zero order), rate doubles (first order), rate quadruples (second order). After finding orders, substitute back into any experiment to solve for k, paying attention to its units.

## Common Misconceptions
- Reaction orders are not necessarily equal to stoichiometric coefficients. For elementary reactions they match, but most reactions studied in general chemistry are not elementary — orders must be measured experimentally.
- The rate constant k is not truly constant across all conditions — it depends on temperature (via the Arrhenius equation). It is constant only at a fixed temperature.

## Questions

```yaml
- question: "The balanced equation for a reaction is A + 2B → C. A student concludes that the reaction is first order in A and second order in B. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — stoichiometric coefficients always determine reaction orders"
    - "The student should have used molar masses, not coefficients, to determine the orders"
    - "Reaction orders must be determined experimentally; the balanced equation only gives stoichiometry, not mechanism"
    - "The overall order should equal the number of reactants, making this first order overall"
  answer: 2
  explanation: "Reaction orders cannot be read from stoichiometric coefficients except for elementary reactions — reactions that occur in a single molecular step exactly as written. Most reactions studied in general chemistry are not elementary; they proceed through multi-step mechanisms with a rate-determining step. The observed rate law reflects that slow step, not the overall stoichiometry. A reaction written as A + 2B → C could be zero order in B (if B doesn't appear in the rate-determining step), first order in A and zero order in B, or any combination — only the method of initial rates can determine this."

- question: "Three experiments are run. In Exp 1: [A] = 0.10 M, [B] = 0.10 M, rate = 2.0 × 10⁻³ M/s. In Exp 2: [A] = 0.20 M, [B] = 0.10 M, rate = 8.0 × 10⁻³ M/s. What is the order with respect to A?"
  type: multiple-choice
  options:
    - "First order — doubling [A] doubled the rate"
    - "Second order — doubling [A] quadrupled the rate"
    - "Zero order — [B] was held constant so we cannot determine the order in A"
    - "Third order — the rate increased by a factor of 4, and 4 = 2³"
  answer: 1
  explanation: "Comparing Exp 1 and Exp 2: [A] doubled while [B] was held constant, and the rate quadrupled (8.0/2.0 = 4). Using the ratio method: (rate₂/rate₁) = ([A]₂/[A]₁)ᵐ → 4 = 2ᵐ → m = 2. Second order. Option A inverts the logic: doubling [A] and doubling the rate would mean first order (2¹ = 2), but the rate quadrupled (2² = 4), indicating second order. Keeping [B] constant is the point — it isolates the effect of A so you can determine its order unambiguously."

- question: "For a reaction A + B → products, the balanced equation shows a coefficient of 2 for reactant B, so the reaction must be second order in B."
  type: true-false
  answer: false
  explanation: "Stoichiometric coefficients reflect amounts consumed, not the reaction mechanism. Reaction orders are experimental quantities determined by the method of initial rates. A coefficient of 2 for B means two moles of B are consumed per mole of product formed, but B could be zero order (not involved in the rate-determining step), first order, second order, or even fractional order — depending entirely on the mechanism. The equation 2HA → H₂ + A₂ looks second order, but many dimerizations have first-order kinetics because of their mechanism."

- question: "The rate constant k for a given reaction has the same numerical value at 25°C and at 75°C."
  type: true-false
  answer: false
  explanation: "The rate constant k depends strongly on temperature through the Arrhenius equation: k = A·e^(−Ea/RT). Increasing temperature increases k because a greater fraction of molecular collisions have enough energy to overcome the activation energy barrier. A 10°C temperature rise often roughly doubles the rate constant for reactions with typical activation energies. 'Constant' in 'rate constant' means k is fixed at a given temperature for a given reaction — it does not mean k is invariant across temperatures. This is a common source of confusion: k is constant in the sense of not depending on concentration, but it does depend on temperature."

- question: "Why can't you determine reaction orders directly from a balanced chemical equation, and what experimental approach is used instead?"
  type: short-answer
  answer: "The balanced equation shows overall stoichiometry — how much of each reactant is consumed — but not the mechanism by which the reaction occurs. Reaction orders reflect the rate-determining step of the mechanism, which typically involves only a subset of reactants, sometimes at different stoichiometries than the overall equation. The method of initial rates isolates one reactant at a time by varying its concentration while holding all others constant, then comparing how the initial rate changes to determine each reactant's order experimentally."
  explanation: "The disconnect between stoichiometry and kinetics is fundamental. For example, the reaction 2NO₂ → 2NO + O₂ has a stoichiometric coefficient of 2 for NO₂, but the rate law is rate = k[NO₂]² — second order, which in this case happens to match. But the reason it is second order is that the rate-determining step involves two NO₂ molecules colliding, not because the coefficient is 2. Coincidence of stoichiometry and order in elementary reactions (single-step mechanisms) is why the textbook sometimes says 'you can read the orders from elementary steps' — but this only works when you already know the mechanism is elementary."
```

## Explainer

From chemical kinetics, you know that reactions happen at different speeds and that reaction rate measures how fast reactant concentrations decrease (or product concentrations increase) over time. The **rate law** takes this further by expressing the exact mathematical relationship between rate and reactant concentrations: rate = k[A]ᵐ[B]ⁿ. Here, k is the **rate constant** (a number specific to the reaction at a given temperature), [A] and [B] are reactant concentrations, and m and n are the **reaction orders** — exponents that tell you how sensitively the rate responds to each concentration.

The critical point that surprises many students is that reaction orders must be determined experimentally — you cannot simply read them off the balanced equation. A balanced equation tells you the stoichiometry (how much reacts), not the mechanism (how it reacts). The **method of initial rates** is the standard experimental approach. You run the reaction multiple times, each time changing the starting concentration of only one reactant while holding the others constant. By comparing how the initial rate changes, you deduce the order with respect to that reactant. If doubling [A] doubles the rate, the reaction is **first order** in A (m = 1). If doubling [A] quadruples the rate, it is **second order** (m = 2). If doubling [A] has no effect on the rate, it is **zero order** (m = 0).

The practical technique uses ratios. Take two experiments where only [A] changes. Divide one rate by the other: rate₂/rate₁ = ([A]₂/[A]₁)ᵐ. If [A] was doubled (ratio = 2) and the rate quadrupled (ratio = 4), then 2ᵐ = 4, so m = 2. Repeat this process for each reactant using a different pair of experiments. The **overall reaction order** is the sum of all individual orders (m + n + ...). Once you know all the orders, substitute the data from any single experiment into the rate law and solve for k. Pay attention to the **units of k** — they depend on the overall order. For a first-order reaction, k has units of s⁻¹; for second order, L mol⁻¹ s⁻¹. Getting the units right is a good check that your orders are correct.

Understanding the rate law unlocks the rest of kinetics. The orders tell you about the reaction mechanism — which species are involved in the rate-determining step. A reaction that is first order in A and first order in B suggests that one molecule of A and one of B collide in the slow step. Zero order in a reactant means it does not participate in the rate-determining step at all, even if it appears in the balanced equation. As you move on to integrated rate laws, you will use these same orders to derive equations that predict concentration as a function of time, determine half-lives, and distinguish reaction orders from graphical data.
