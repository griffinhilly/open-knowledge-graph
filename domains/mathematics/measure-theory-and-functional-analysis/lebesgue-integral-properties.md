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
stage: expert
status: validated
---

# Properties of the Lebesgue Integral

## Core Idea
The Lebesgue integral is linear, monotone, and σ-additive over disjoint sets. Functions equal a.e. have the same integral. These properties, stronger than those of the Riemann integral, make Lebesgue integration a powerful tool for analysis.

## Questions

```yaml
- question: "Define f(x) = 0 for all x ∈ [0,1], and g(x) = 1 if x is rational, 0 if x is irrational, on [0,1]. What is the Lebesgue integral ∫₀¹ g dλ?"
  type: multiple-choice
  options:
    - "1, because g takes the value 1 on infinitely many points"
    - "Undefined, because g is not Riemann integrable"
    - "0, because g equals f almost everywhere — the rationals form a measure-zero set"
    - "1/2, because g oscillates between 0 and 1 with equal frequency"
  answer: 2
  explanation: "The rationals in [0,1] are countable, hence have Lebesgue measure zero. Since g differs from f (the zero function) only on a set of measure zero, g = f almost everywhere. By the a.e.-equivalence property of the Lebesgue integral, ∫g dλ = ∫f dλ = 0. This function (the Dirichlet function) is famously not Riemann integrable — it has discontinuities everywhere — yet the Lebesgue integral handles it trivially by ignoring the measure-zero set of rationals. This example is a canonical demonstration of the Lebesgue integral's robustness over the Riemann integral."

- question: "Why is the almost-everywhere equivalence property of the Lebesgue integral essential for constructing L^p spaces as complete metric spaces?"
  type: multiple-choice
  options:
    - "Because L^p spaces require functions to be defined at every point of the domain, and a.e. equivalence guarantees this"
    - "Because it allows functions differing only on measure-zero sets to be identified as the same element, making the L^p norm well-defined on equivalence classes and enabling completeness"
    - "Because almost-everywhere convergence implies norm convergence in L^p, which is needed for the Riesz-Fischer theorem"
    - "Because the Riemann integral shares this property and L^p spaces must agree with Riemann integration on continuous functions"
  answer: 1
  explanation: "If two functions differ on a measure-zero set, the Lebesgue integral cannot distinguish them — they have the same integral. L^p spaces are built from equivalence classes of functions that agree a.e.: the 'elements' of L^p are these classes, not individual functions. Without this identification, ‖f‖_p = 0 would not imply f = 0 (you could have a nonzero function supported on a measure-zero set), and the norm would not be a genuine norm. This a.e. identification is precisely what makes L^p a normed space and ultimately a complete (Banach) space."

- question: "If f and g are Lebesgue integrable functions on ℝ that differ on exactly a countable set of points, then ∫f dλ = ∫g dλ."
  type: true-false
  answer: true
  explanation: "Any countable set has Lebesgue measure zero (countable unions of measure-zero points are measure zero). Since f and g differ only on a set of measure zero, they are equal almost everywhere. The Lebesgue integral is constant on a.e.-equivalence classes: functions equal a.e. have identical integrals. This is exactly the robustness property that makes Lebesgue integration powerful — measure-zero modifications are genuinely irrelevant."

- question: "The Riemann integral handles measure-zero modifications just as gracefully as the Lebesgue integral: if two bounded functions on [a,b] differ only on a measure-zero set, both are Riemann integrable with equal integrals."
  type: true-false
  answer: false
  explanation: "The Riemann integral does not have this robustness. A bounded function is Riemann integrable if and only if it is continuous almost everywhere (Lebesgue's criterion). A function that differs from a Riemann-integrable function on a dense set (like the rationals) may be everywhere discontinuous and therefore not Riemann integrable at all — even though the modification set has measure zero. The Dirichlet function demonstrates this exactly: it differs from the zero function on a measure-zero set yet is not Riemann integrable."

- question: "Why does the Lebesgue integral's indifference to measure-zero sets make it better suited for building complete function spaces than the Riemann integral?"
  type: short-answer
  answer: "Completeness requires that every Cauchy sequence of functions converges to a limit in the space. If we use Riemann integration, a Cauchy sequence of integrable functions may converge pointwise to a limit that is not Riemann integrable — the space is not closed under limits. With Lebesgue integration, we work with equivalence classes of functions agreeing a.e., and the Riesz-Fischer theorem guarantees that every Cauchy sequence in L^p converges to an element of L^p. The a.e.-indifference is what allows the limit to 'absorb' badly-behaved modifications on measure-zero sets without escaping the space."
  explanation: "The key is that completeness requires taking limits, and limits can produce functions with measure-zero sets of bad behavior that Riemann integration cannot tolerate. Lebesgue's willingness to ignore those sets is not a concession but the exact feature that makes the resulting function spaces behave well analytically — it is the difference between a complete and an incomplete metric space."
```

## Explainer

From the general definition of the Lebesgue integral, you know how to integrate non-negative measurable functions via simple functions, and how to extend to general functions by splitting into positive and negative parts. Now we catalog the structural properties that make this integral so powerful — properties that often fail for the Riemann integral or require much more delicate conditions.

**Linearity** is the most-used property: ∫(αf + βg) dμ = α∫f dμ + β∫g dμ whenever the integrals exist. This looks identical to the Riemann case, but its significance deepens because the Lebesgue integral handles far more functions. **Monotonicity** says that if f ≤ g almost everywhere, then ∫f dμ ≤ ∫g dμ. Again, familiar in spirit, but notice the "almost everywhere" — the Lebesgue integral genuinely ignores sets of measure zero. Two functions that disagree on a countable set, or on a Cantor set of measure zero, have the same integral. The Riemann integral does not have this robustness; a single badly-placed discontinuity can kill integrability.

The **σ-additivity over disjoint sets** says: if A = A₁ ∪ A₂ ∪ ··· is a countable disjoint union, then ∫_A f dμ = Σₙ ∫_{Aₙ} f dμ. This mirrors how the measure μ itself is σ-additive, and it means you can split integration domains into countably many pieces and sum the results — a freedom unavailable in the Riemann world, where domains must be intervals or similarly simple shapes.

The a.e.-equivalence property deserves special attention because it is what enables L^p spaces (the next topic in your path). If you define an equivalence class of functions that agree almost everywhere, the Lebesgue integral is constant on that class. This lets you identify two functions as "the same" for integration purposes, which is essential when constructing function spaces where completeness is required. The Riemann integral cannot do this: you cannot casually modify a Riemann-integrable function on a dense set and expect integrability to survive. The Lebesgue integral's indifference to measure-zero behavior is not a bug but a feature — it is precisely what makes the theory complete.
