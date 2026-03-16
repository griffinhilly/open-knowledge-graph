---
id: riemann-vs-lebesgue-integrals
title: 'Comparison: Riemann and Lebesgue Integrals'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: riemann-integral-darboux-sums
  type: hard
- id: lebesgue-integral-general-definition
  type: hard
builds-toward:
- dominated-convergence-theorem
tags:
- integration
stage: abstract-reasoning
status: draft
---

# Comparison: Riemann and Lebesgue Integrals

## Core Idea
If a bounded function on [a,b] is Riemann integrable, it is Lebesgue integrable with equal integrals. The Lebesgue integral applies to a much broader class of functions and has superior convergence theorems (e.g., dominated convergence).

## How It's Best Learned
Show that Dirichlet's function (1 on rationals, 0 on irrationals) is Lebesgue integrable but not Riemann integrable. Understand that Lebesgue slices 'horizontally' while Riemann slices 'vertically.'

## Common Misconceptions
Lebesgue integration is not strictly stronger in existence: every Riemann integrable function is Lebesgue integrable, but the reverse is false. The real advantage is better convergence theorems.

## Explainer

Both the Riemann and Lebesgue integrals are trying to do the same thing — compute the "signed area" under a function's graph. The difference lies in *how* they carve up the problem, and that difference has profound consequences. You already know Riemann integration via Darboux sums: you partition the **domain** [a, b] into subintervals and approximate the integral by summing f(x) × (width of interval). Lebesgue's insight was to partition the **range** instead: divide the y-axis into bands, ask "what is the measure of the set of x-values where f(x) falls in this band?", and sum (band height) × (measure of preimage).

This range-partitioning is powerful because it decouples the behavior of the function from the structure of the domain. Consider **Dirichlet's function**: f(x) = 1 if x is rational, 0 if x is irrational. Riemann integration fails here — every subinterval of [0, 1] contains both rationals and irrationals, so upper and lower Darboux sums never converge. But Lebesgue handles it trivially: the preimage of the value 1 is the rationals (measure zero), and the preimage of the value 0 is the irrationals (measure 1). The integral is 1 × 0 + 0 × 1 = 0.

The **inclusion relationship** is clean but asymmetric: every bounded Riemann integrable function on [a, b] is also Lebesgue integrable, and the two integrals agree. But the Lebesgue integral applies to many functions that are not Riemann integrable — precisely those where the domain has complicated structure that defeats the Darboux partition approach. The reverse fails: a function like the unbounded 1/√x on (0, 1] requires an improper Riemann integral but is directly Lebesgue integrable; however, this is a technicality and not the main point of distinction.

The real payoff of Lebesgue integration is its **convergence theorems**. The Dominated Convergence Theorem, which you'll encounter next, says: if fₙ → f pointwise almost everywhere and all the fₙ are dominated by an integrable function g, then ∫fₙ → ∫f. This result is routinely used in analysis, probability, and PDEs. The Riemann framework offers no analogous general theorem — you can construct sequences of Riemann integrable functions converging to a non-Riemann-integrable limit. Lebesgue integration is designed precisely so that limits and integrals commute under mild conditions, which is why it has become the standard in modern analysis.
