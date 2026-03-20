---
id: lebesgue-integral-properties
title: Properties of the Lebesgue Integral
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-general-definition
  type: hard
builds-toward:
- lp-spaces-definition
- fubini-theorem
tags:
- integration
- properties
stage: advanced
status: draft
---

# Properties of the Lebesgue Integral

## Core Idea
The Lebesgue integral is linear, monotone, and σ-additive over disjoint sets. Functions equal a.e. have the same integral. These properties, stronger than those of the Riemann integral, make Lebesgue integration a powerful tool for analysis.

## Explainer

From the general definition of the Lebesgue integral, you know how to integrate non-negative measurable functions via simple functions, and how to extend to general functions by splitting into positive and negative parts. Now we catalog the structural properties that make this integral so powerful — properties that often fail for the Riemann integral or require much more delicate conditions.

**Linearity** is the most-used property: ∫(αf + βg) dμ = α∫f dμ + β∫g dμ whenever the integrals exist. This looks identical to the Riemann case, but its significance deepens because the Lebesgue integral handles far more functions. **Monotonicity** says that if f ≤ g almost everywhere, then ∫f dμ ≤ ∫g dμ. Again, familiar in spirit, but notice the "almost everywhere" — the Lebesgue integral genuinely ignores sets of measure zero. Two functions that disagree on a countable set, or on a Cantor set of measure zero, have the same integral. The Riemann integral does not have this robustness; a single badly-placed discontinuity can kill integrability.

The **σ-additivity over disjoint sets** says: if A = A₁ ∪ A₂ ∪ ··· is a countable disjoint union, then ∫_A f dμ = Σₙ ∫_{Aₙ} f dμ. This mirrors how the measure μ itself is σ-additive, and it means you can split integration domains into countably many pieces and sum the results — a freedom unavailable in the Riemann world, where domains must be intervals or similarly simple shapes.

The a.e.-equivalence property deserves special attention because it is what enables L^p spaces (the next topic in your path). If you define an equivalence class of functions that agree almost everywhere, the Lebesgue integral is constant on that class. This lets you identify two functions as "the same" for integration purposes, which is essential when constructing function spaces where completeness is required. The Riemann integral cannot do this: you cannot casually modify a Riemann-integrable function on a dense set and expect integrability to survive. The Lebesgue integral's indifference to measure-zero behavior is not a bug but a feature — it is precisely what makes the theory complete.
