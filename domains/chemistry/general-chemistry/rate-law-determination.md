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
stage: abstract-reasoning
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

## Explainer

From chemical kinetics, you know that reactions happen at different speeds and that reaction rate measures how fast reactant concentrations decrease (or product concentrations increase) over time. The **rate law** takes this further by expressing the exact mathematical relationship between rate and reactant concentrations: rate = k[A]ᵐ[B]ⁿ. Here, k is the **rate constant** (a number specific to the reaction at a given temperature), [A] and [B] are reactant concentrations, and m and n are the **reaction orders** — exponents that tell you how sensitively the rate responds to each concentration.

The critical point that surprises many students is that reaction orders must be determined experimentally — you cannot simply read them off the balanced equation. A balanced equation tells you the stoichiometry (how much reacts), not the mechanism (how it reacts). The **method of initial rates** is the standard experimental approach. You run the reaction multiple times, each time changing the starting concentration of only one reactant while holding the others constant. By comparing how the initial rate changes, you deduce the order with respect to that reactant. If doubling [A] doubles the rate, the reaction is **first order** in A (m = 1). If doubling [A] quadruples the rate, it is **second order** (m = 2). If doubling [A] has no effect on the rate, it is **zero order** (m = 0).

The practical technique uses ratios. Take two experiments where only [A] changes. Divide one rate by the other: rate₂/rate₁ = ([A]₂/[A]₁)ᵐ. If [A] was doubled (ratio = 2) and the rate quadrupled (ratio = 4), then 2ᵐ = 4, so m = 2. Repeat this process for each reactant using a different pair of experiments. The **overall reaction order** is the sum of all individual orders (m + n + ...). Once you know all the orders, substitute the data from any single experiment into the rate law and solve for k. Pay attention to the **units of k** — they depend on the overall order. For a first-order reaction, k has units of s⁻¹; for second order, L mol⁻¹ s⁻¹. Getting the units right is a good check that your orders are correct.

Understanding the rate law unlocks the rest of kinetics. The orders tell you about the reaction mechanism — which species are involved in the rate-determining step. A reaction that is first order in A and first order in B suggests that one molecule of A and one of B collide in the slow step. Zero order in a reactant means it does not participate in the rate-determining step at all, even if it appears in the balanced equation. As you move on to integrated rate laws, you will use these same orders to derive equations that predict concentration as a function of time, determine half-lives, and distinguish reaction orders from graphical data.
