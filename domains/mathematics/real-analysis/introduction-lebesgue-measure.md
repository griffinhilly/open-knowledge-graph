---
id: introduction-lebesgue-measure
title: Introduction to Lebesgue Measure
domain: mathematics
course: real-analysis
prerequisites:
- id: compact-sets
  type: hard
- id: open-sets-real-line
  type: hard
builds-toward:
- introduction-lebesgue-integral
tags:
- lebesgue-measure
- measure-theory
- advanced
stage: advanced
status: validated
---

# Introduction to Lebesgue Measure

## Core Idea
Lebesgue measure extends the notion of length to more general sets than intervals. It assigns a non-negative measure to sets in σ-algebra on ℝ, generalizing length of intervals. Lebesgue measure has better properties than Riemann integrability: it handles arbitrary unions of open sets, and a set has measure zero if it can be covered by countably many intervals of arbitrarily small total length. This foundation enables the Lebesgue integral to integrate a much wider class of functions.

## Questions

```yaml
- question: "The indicator function of the rationals, f(x) = 1 if x ∈ ℚ, f(x) = 0 otherwise, is not Riemann integrable on [0,1]. What is its Lebesgue integral on [0,1]?"
  type: multiple-choice
  options:
    - "1 — the rationals are dense in [0,1], so the function is effectively always 1"
    - "1/2 — the rationals and irrationals split [0,1] equally by density"
    - "0 — the rationals have Lebesgue measure zero, so f equals 0 almost everywhere"
    - "Undefined — this function is not Lebesgue measurable"
  answer: 2
  explanation: "The rationals in [0,1] are countable, and any countable set has Lebesgue measure zero (it can be covered by open intervals of total length ε for any ε > 0). Therefore f = 0 almost everywhere on [0,1], and its Lebesgue integral is 0. The Riemann approach fails because, in any sub-interval, f takes both values 0 and 1, so upper and lower Riemann sums cannot be made to agree. The Lebesgue approach succeeds because it measures where the function takes each value, and the set where f = 1 has measure zero."

- question: "A student argues: 'The rationals cannot have measure zero — they are infinite in number and dense in every interval of [0,1], so they must fill positive measure.' What is the flaw?"
  type: multiple-choice
  options:
    - "There is no flaw — the student is correct that the rationals have positive measure"
    - "Density and measure are different properties; the rationals are countable and can be covered by open intervals of arbitrarily small total length"
    - "The rationals have measure 1 because they are dense, not some measure between 0 and 1"
    - "Measure is only defined for uncountable sets; countable sets have undefined measure"
  answer: 1
  explanation: "Density (being everywhere close) and measure (size in the sense of length) are fundamentally different properties. Enumerate the rationals as q₁, q₂, …. Cover qₙ with an open interval of length ε/2ⁿ. The total length is Σε/2ⁿ = ε, arbitrarily small. So the rationals can be covered by intervals of total length as small as desired — outer measure zero. Denseness is a topological property; measure zero is a size property. A set can be topologically ubiquitous (dense) and measure-theoretically negligible."

- question: "Every open subset of ℝ is Lebesgue measurable."
  type: true-false
  answer: true
  explanation: "The Lebesgue measurable sets form a σ-algebra that contains all open sets. Open sets on ℝ are countable unions of open intervals, and open intervals have well-defined measure (their length). Countable unions of measurable sets are measurable by the σ-algebra property, so all open sets are measurable. The non-measurable sets that exist (assuming the axiom of choice) are exotic constructions that cannot be built from open and closed sets by standard set operations."

- question: "If two functions f and g on [0,1] differ primarily on the set of rational numbers, their Lebesgue integrals over [0,1] may differ."
  type: true-false
  answer: false
  explanation: "The rationals have Lebesgue measure zero, so f and g agree almost everywhere. In Lebesgue theory, two functions that agree almost everywhere have identical integrals — the integral is blind to what happens on measure-zero sets. This is one of the key advantages over Riemann integration and is what makes 'almost everywhere' the natural equivalence relation for integration theory. It allows the theory to treat equivalence classes of functions rather than insisting on pointwise values everywhere."

- question: "What does it mean for a property to hold 'almost everywhere' (a.e.), and why is this concept essential to Lebesgue integration theory rather than just a convenient shorthand?"
  type: short-answer
  answer: "'Almost everywhere' means the property holds except possibly on a set of Lebesgue measure zero. It is essential — not merely convenient — because Lebesgue integration inherently cannot distinguish between functions that agree almost everywhere: their integrals are equal. This means the natural objects of Lebesgue theory are equivalence classes of functions under 'equal a.e.,' not individual pointwise-defined functions. Powerful convergence theorems (Dominated Convergence, Monotone Convergence) are stated in a.e. terms because pointwise convergence everywhere is too strong to achieve in most analytic settings, while a.e. convergence is sufficient for all integration purposes."
  explanation: "The practical consequence: modifying a function on a measure-zero set changes nothing about its integral or its L² norm. This is why function spaces like L²[0,1] are spaces of equivalence classes — two functions differing only on a null set are identified as the same element. The 'a.e.' qualification also appears throughout probability theory, where almost sure convergence is the natural mode. Far from being a shorthand, 'almost everywhere' is where Lebesgue measure theory makes its most fundamental departure from the Riemann framework."
```

## Explainer

You already know that open sets on the real line are unions of open intervals, and that compact sets are closed and bounded subsets of ℝ. Now the question becomes: can we consistently assign a "length" to *any* set, not just intervals or simple combinations of them? The Riemann integral works by partitioning the *domain* into intervals, and for most functions this is enough. But there are natural sets — like the rational numbers in [0,1] — that are dense everywhere yet contain "almost nothing." The **Lebesgue measure** is the tool that makes this intuition precise.

The construction begins with a simple idea: a set E ⊆ ℝ has **outer measure** m*(E) equal to the infimum of the total length of all countable collections of open intervals that cover E. For an interval, this recovers ordinary length. For a single point or any countable set, it gives zero — because you can cover a countable collection of points with intervals of total length ε for any ε > 0. A set has **measure zero** when this infimum is 0, meaning the set is "negligibly small" in a size sense even if it is infinitely dense, like ℚ. This is the key concept that unlocks integration theory: events or sets of measure zero don't affect integration.

Not every subset of ℝ is **Lebesgue measurable** — there exist (assuming the axiom of choice) bizarre sets with no sensible length. The measurable sets form a **σ-algebra**: a collection closed under countable unions, countable intersections, and complements. Every open set, every closed set, and in particular every compact set you studied is measurable. Within this σ-algebra, Lebesgue measure satisfies **countable additivity**: the measure of a countable disjoint union is the sum of the individual measures. This property, which the Riemann approach cannot provide in full generality, is what makes modern analysis work.

The practical punchline is the notion of "almost everywhere." A property holds **almost everywhere** (a.e.) if it fails only on a set of measure zero. Two functions that differ on a set of measure zero behave identically for integration purposes. This is why the Lebesgue integral can handle the indicator function of the rationals — which is nowhere Riemann integrable — with ease: the rationals have measure zero, so the function is zero almost everywhere, and its integral is zero. This foundation, built on open sets and compact sets you already know, will enable a far more powerful and flexible theory of integration.


