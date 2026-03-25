---
id: radon-nikodym-theorem
title: Radon-Nikodym Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: measure-spaces
  type: hard
- id: lp-spaces
  type: soft
- id: null-sets-almost-everywhere
  type: soft
builds-toward:
- signed-measures-hahn-jordan
tags:
- measure-theory
stage: expert
status: validated
---
# Radon-Nikodym Theorem

## Core Idea
If ν is σ-finite and absolutely continuous with respect to μ, then ∃h measurable: ν(A) = ∫_A h dμ. The Radon-Nikodym derivative dν/dμ = h formalizes differentiation of measures.

## Questions

```yaml
- question: "Let μ be Lebesgue measure on [0,1], and let ν be the measure defined by ν(A) = ∫_A x² dx. Is ν absolutely continuous with respect to μ, and what is dν/dμ?"
  type: multiple-choice
  options:
    - "No — ν is not absolutely continuous because it assigns different weights to sets than μ does"
    - "Yes — ν ≪ μ because any Lebesgue-null set also has ν-measure zero, and dν/dμ = x²"
    - "Yes — ν ≪ μ, but the Radon-Nikodym derivative cannot be identified with x² since it is not integrable on all of ℝ"
    - "The answer depends on whether ν is σ-finite, which is not given"
  answer: 1
  explanation: "Absolute continuity ν ≪ μ means: whenever μ(A) = 0, also ν(A) = 0. If a set has Lebesgue measure zero, then ∫_A x² dx = 0 as well (integrating a non-negative function over a null set gives zero). So ν ≪ μ. The function h(x) = x² satisfies ν(A) = ∫_A h dμ for all measurable A, making it the Radon-Nikodym derivative. Option A confuses 'absolutely continuous' with 'equal' — absolute continuity is about null sets, not about whether the two measures assign the same mass to every set."

- question: "In elementary probability, if a continuous random variable X has probability density function f(x), what is f(x) in measure-theoretic terms?"
  type: multiple-choice
  options:
    - "The derivative of the CDF with respect to x, which has no direct measure-theoretic interpretation"
    - "The Radon-Nikodym derivative of the probability measure P with respect to Lebesgue measure λ: f = dP/dλ"
    - "A convenient summary of P that is not formally derived from the measure structure"
    - "The inverse of the CDF, normalized to integrate to 1"
  answer: 1
  explanation: "When P is the probability measure of a continuous random variable and λ is Lebesgue measure, P(A) = ∫_A f(x) dx for all measurable A — this is exactly the Radon-Nikodym condition ν(A) = ∫_A h dμ. The density f is the Radon-Nikodym derivative f = dP/dλ. The theorem therefore is not an abstraction disconnected from elementary probability — it is the theorem that justifies the existence and uniqueness of probability density functions, and extends the concept to arbitrary measure spaces."

- question: "If ν ≪ μ and both measures are σ-finite, the Radon-Nikodym derivative dν/dμ is unique everywhere on the space, not just μ-almost everywhere."
  type: true-false
  answer: false
  explanation: "The Radon-Nikodym theorem guarantees uniqueness only μ-almost everywhere. Two functions h and h' satisfying ν(A) = ∫_A h dμ = ∫_A h' dμ for all measurable A must agree μ-a.e., but they can differ on a set of μ-measure zero. Since μ-null sets are invisible to all absolutely continuous measures, this is the strongest uniqueness statement available — and it is the right one for measure theory."

- question: "If ν ≪ μ (ν absolutely continuous with respect to μ), then necessarily μ ≪ ν as well."
  type: true-false
  answer: false
  explanation: "Absolute continuity is not symmetric. A simple example: let μ be Lebesgue measure on [0,1] and let ν(A) = ∫_A 2·1_{[0,1/2]}(x) dx — Lebesgue measure restricted to [0, 1/2] and scaled. Any Lebesgue-null set has ν-measure zero, so ν ≪ μ. But the set (1/2, 1] has μ-measure 1/2 and ν-measure 0, so μ assigns positive mass to a ν-null set, meaning μ is not absolutely continuous with respect to ν. When both ν ≪ μ and μ ≪ ν hold, the measures are called mutually absolutely continuous or equivalent."

- question: "Explain in your own words why absolute continuity of ν with respect to μ is the right condition for ν to have a density with respect to μ."
  type: short-answer
  answer: "A density h satisfying ν(A) = ∫_A h dμ assigns zero mass to any set A that μ considers negligible (μ(A) = 0), because an integral over a null set is always zero. So if ν has a density with respect to μ, then ν must automatically assign zero mass to every μ-null set — that is, ν ≪ μ must hold. Conversely, if ν assigns positive mass to some μ-null set, no non-negative function h could produce that mass by integrating against μ, so no density can exist. Absolute continuity is therefore both necessary and sufficient for a density to exist (given σ-finiteness)."
  explanation: "The intuition: if μ cannot 'see' a set (μ-measure zero), then integration against μ cannot accumulate mass there either. Any measure that places positive mass on μ-invisible sets is fundamentally not derivable from μ by integration — there is no way to 'create' mass on sets that μ ignores."
```

## Explainer

You have been working with measure spaces — sets X equipped with a σ-algebra and a measure μ that assigns sizes to measurable sets. Now suppose you have *two* measures on the same space: μ and ν. A natural question arises: when can ν be expressed in terms of μ? When can we write ν as "μ with a weight function"?

The key condition is **absolute continuity**: ν is absolutely continuous with respect to μ, written ν ≪ μ, if every μ-null set is also ν-null. That is, whenever μ(A) = 0, we also have ν(A) = 0. This says: ν cannot see anything that μ considers negligible. In probabilistic terms, if an event has probability zero under μ, it also has probability zero under ν. Absolute continuity is the precise condition under which ν is "dominated by" μ.

The **Radon-Nikodym theorem** says: if ν ≪ μ and both measures are σ-finite, then there exists a non-negative measurable function h such that ν(A) = ∫_A h dμ for every measurable set A. This function h is unique μ-almost everywhere, and we write it as dν/dμ — the **Radon-Nikodym derivative**. The name is deliberate: this is literally a derivative of one measure with respect to another. Just as the ordinary derivative df/dx tells you how f changes relative to x, the Radon-Nikodym derivative tells you how ν is distributed relative to μ.

A concrete example anchors the abstraction. In classical probability, if X has probability density function f(x) and we take μ to be Lebesgue measure, then P(A) = ∫_A f(x) dx for every measurable set A. In Radon-Nikodym language, P ≪ λ (Lebesgue) and dP/dλ = f. The density function you learned in probability theory is a Radon-Nikodym derivative! The theorem generalizes this: any absolutely continuous probability measure on Rⁿ has a density, and conversely. This also underlies conditional expectation in advanced probability: E[X | G] is the Radon-Nikodym derivative of a signed measure with respect to a restricted measure — a perspective that makes its properties (linearity, tower property) transparent.
