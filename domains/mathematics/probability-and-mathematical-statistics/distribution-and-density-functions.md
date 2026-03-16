---
id: distribution-and-density-functions
title: Distribution and Density Functions (Rigorous)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: random-variables-as-measurable-functions
  type: hard
- id: borel-sigma-algebra
  type: soft
builds-toward:
- joint-distributions-and-marginals-rigorous
- characteristic-functions
tags:
- distributions
- density
- cdf
stage: advanced
status: draft
---

# Distribution and Density Functions (Rigorous)

## Core Idea
The cumulative distribution function F(x) = P(X ≤ x) uniquely determines the distribution of X. A probability density function f is the Radon-Nikodym derivative when the distribution is absolutely continuous with respect to Lebesgue measure. Distributions may also be purely singular or have atoms.

## Explainer

From your prerequisite on random variables as measurable functions, you know that a random variable X is a measurable map X: (Ω, ℱ) → (ℝ, ℬ(ℝ)), and you've worked with the Borel σ-algebra ℬ(ℝ). The **distribution** of X is the pushforward measure μ_X defined by μ_X(B) = P(X ∈ B) = P(X⁻¹(B)) for Borel sets B ⊆ ℝ. Everything you want to know about X — probabilities, expectations, quantiles — is encoded in μ_X. Crucially, μ_X is a probability measure on (ℝ, ℬ(ℝ)), so it inherits all the properties of measures: countable additivity, σ-finiteness on ℝ, and so on.

The **cumulative distribution function** F(x) = P(X ≤ x) = μ_X((−∞, x]) is a convenient scalar summary of the distribution. Its properties follow directly from measure theory: F is non-decreasing (measures of nested sets are nested), right-continuous (by the continuity-from-above property of measures), and satisfies F(−∞) = 0, F(+∞) = 1. Conversely, any function with these three properties is the CDF of some random variable. The key structural fact is that F **uniquely determines** μ_X — there is a one-to-one correspondence between CDFs satisfying these properties and probability measures on ℝ. This is why CDFs are the universal language for describing distributions.

A **probability density function** arises when the distribution is absolutely continuous with respect to Lebesgue measure λ. Absolute continuity μ_X ≪ λ means: whenever a Borel set has Lebesgue measure zero, it also has μ_X-measure zero. When this holds, the **Radon-Nikodym theorem** guarantees a unique (up to a.e. equivalence) measurable function f such that μ_X(B) = ∫_B f dλ for all Borel B. This function f is the PDF, and it equals F'(x) almost everywhere. The Radon-Nikodym framing is the rigorous version of the intuitive statement "probability = area under the density curve" — you are literally saying that the probability measure is absolutely continuous with respect to length (Lebesgue measure), and the derivative f is the density of probability per unit length.

Not all distributions have PDFs. A **discrete distribution** concentrates all its mass on a countable set of points: P(X = xₖ) = pₖ > 0 for a countable collection. Such a distribution is singular with respect to Lebesgue measure — it is entirely supported on a set of Lebesgue measure zero — so no Radon-Nikodym density exists. A stranger beast is the **purely singular continuous** distribution, whose CDF is continuous (no atoms) but is constant almost everywhere. The Cantor distribution is the canonical example: its CDF is the Devil's staircase, which increases from 0 to 1 entirely on the Cantor set (measure zero), so its "density" would have to be zero almost everywhere but still integrate to 1 — a contradiction, so no density exists. The full Lebesgue decomposition theorem says every distribution uniquely decomposes into an absolutely continuous part (has a PDF), a discrete part (atoms), and a singular continuous part.

Understanding the Radon-Nikodym perspective matters because it unifies otherwise disparate formulas. The PDF formula P(a < X ≤ b) = ∫_a^b f(x) dx and the PMF formula P(X = k) = pₖ are not really two different things — they are both special cases of P(X ∈ B) = ∫_B dμ_X, one where μ_X is absolutely continuous (use Radon-Nikodym to get f) and one where μ_X is a sum of point masses. Characteristic functions, the joint distribution theory that builds on this topic, and all of measure-theoretic probability depend on fluency with this framework.
