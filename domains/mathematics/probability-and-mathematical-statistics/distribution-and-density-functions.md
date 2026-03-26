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
status: validated
---

# Distribution and Density Functions (Rigorous)

## Core Idea
The cumulative distribution function F(x) = P(X ≤ x) uniquely determines the distribution of X. A probability density function f is the Radon-Nikodym derivative when the distribution is absolutely continuous with respect to Lebesgue measure. Distributions may also be purely singular or have atoms.

## Questions

```yaml
- question: "A student claims that every random variable has a probability density function because 'you can always compute the probability of falling in any interval.' What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Not every random variable has well-defined probabilities for intervals — some distributions are not σ-finite"
    - "A PDF requires the distribution to be absolutely continuous with respect to Lebesgue measure; discrete and singular distributions have no PDF even though interval probabilities are perfectly well-defined"
    - "The student is essentially correct — every distribution has an associated PDF, though for discrete distributions it takes the form of a sum of delta functions"
    - "PDFs are only defined for distributions supported on bounded intervals; unbounded distributions require a different formalism"
  answer: 1
  explanation: "The existence of a PDF is not about whether probabilities for intervals exist — it's about whether the distribution is absolutely continuous with respect to Lebesgue measure. A discrete distribution places all mass on countable points (e.g., P(X = k) = pₖ); interval probabilities are well-defined but no PDF exists because the distribution is singular with respect to Lebesgue measure. The Radon-Nikodym theorem guarantees a PDF exists if and only if the distribution μ_X satisfies μ_X ≪ λ (absolute continuity). Delta functions are a generalized-function tool that is not part of the rigorous measure-theoretic framework."

- question: "The Cantor distribution has a CDF that increases continuously from 0 to 1 but has derivative zero almost everywhere. What does this imply?"
  type: multiple-choice
  options:
    - "The distribution has a well-defined PDF equal to zero almost everywhere, which is consistent with a total probability of 1"
    - "The distribution is singular continuous — it has no atoms and no PDF, because it is not absolutely continuous with respect to Lebesgue measure"
    - "The Cantor distribution is actually discrete, with probability mass concentrated on the rational points of [0, 1]"
    - "Since the CDF is continuous and non-decreasing, the PDF can be recovered by differentiating the CDF as usual"
  answer: 1
  explanation: "The Cantor distribution's CDF (the Devil's staircase) increases entirely on the Cantor set, which has Lebesgue measure zero. This means the distribution concentrates all its probability on a measure-zero set — it is not absolutely continuous with respect to Lebesgue measure. If a PDF f existed, we would need ∫_B f dλ = μ_X(B) for all Borel B, but the derivative is zero a.e., so any Radon-Nikodym density would be zero a.e. and integrate to zero, not 1 — a contradiction. The Cantor distribution is the canonical example of a third type: singular continuous (no atoms, but also no PDF)."

- question: "Any random variable whose CDF is everywhere continuous should have a probability density function."
  type: true-false
  answer: false
  explanation: "A continuous CDF means the distribution has no atoms — no individual point x with positive probability P(X = x) > 0. But continuity of the CDF is weaker than absolute continuity of the distribution with respect to Lebesgue measure. The Cantor distribution is the definitive counterexample: its CDF is continuous, yet no PDF exists because the distribution is singular continuous, concentrating probability on the Cantor set (a measure-zero set with no isolated points). For a PDF to exist, you need the stronger condition that the distribution is absolutely continuous with respect to Lebesgue measure."

- question: "The cumulative distribution function F(x) = P(X ≤ x) uniquely determines the probability distribution of X."
  type: true-false
  answer: true
  explanation: "There is a one-to-one correspondence between CDFs (non-decreasing, right-continuous functions with F(−∞) = 0 and F(+∞) = 1) and probability measures on (ℝ, ℬ(ℝ)). Any function satisfying these three properties corresponds to a unique probability measure, and conversely every probability measure on ℝ has a unique CDF. This is why CDFs are the universal language for describing distributions — regardless of whether a PDF or PMF exists, the CDF always exists and fully encodes the distribution."

- question: "What does it mean to say that a probability density function is the Radon-Nikodym derivative of the distribution with respect to Lebesgue measure, and why does this framing explain when a PDF fails to exist?"
  type: short-answer
  answer: "A PDF exists when the distribution μ_X is absolutely continuous with respect to Lebesgue measure λ — meaning that any set of zero length also has zero probability. Under this condition, the Radon-Nikodym theorem guarantees a measurable function f such that P(X ∈ B) = ∫_B f dλ for all Borel sets B. The function f is the 'density of probability per unit length.' If the distribution is not absolutely continuous — as with a discrete distribution (all mass on countable points, a set of zero Lebesgue measure) or a singular continuous distribution (mass on a Cantor-like set of zero Lebesgue measure) — then the Radon-Nikodym hypothesis fails and no such f can exist. Intuitively: you cannot express probability as 'area under a curve' if probability doesn't spread continuously over intervals."
  explanation: "The Radon-Nikodym framing unifies the otherwise apparently different formulas for continuous and discrete distributions. P(a < X ≤ b) = ∫_a^b f(x) dx and P(X = k) = pₖ are both special cases of P(X ∈ B) = ∫_B dμ_X — in the first case μ_X is absolutely continuous so you can substitute f dλ; in the second case μ_X is a sum of point masses. The measure-theoretic framework is not just aesthetic: it provides the tools (Radon-Nikodym, Lebesgue decomposition) to handle all three types of distributions uniformly."
```

## Explainer

From your prerequisite on random variables as measurable functions, you know that a random variable X is a measurable map X: (Ω, ℱ) → (ℝ, ℬ(ℝ)), and you've worked with the Borel σ-algebra ℬ(ℝ). The **distribution** of X is the pushforward measure μ_X defined by μ_X(B) = P(X ∈ B) = P(X⁻¹(B)) for Borel sets B ⊆ ℝ. Everything you want to know about X — probabilities, expectations, quantiles — is encoded in μ_X. Crucially, μ_X is a probability measure on (ℝ, ℬ(ℝ)), so it inherits all the properties of measures: countable additivity, σ-finiteness on ℝ, and so on.

The **cumulative distribution function** F(x) = P(X ≤ x) = μ_X((−∞, x]) is a convenient scalar summary of the distribution. Its properties follow directly from measure theory: F is non-decreasing (measures of nested sets are nested), right-continuous (by the continuity-from-above property of measures), and satisfies F(−∞) = 0, F(+∞) = 1. Conversely, any function with these three properties is the CDF of some random variable. The key structural fact is that F **uniquely determines** μ_X — there is a one-to-one correspondence between CDFs satisfying these properties and probability measures on ℝ. This is why CDFs are the universal language for describing distributions.

A **probability density function** arises when the distribution is absolutely continuous with respect to Lebesgue measure λ. Absolute continuity μ_X ≪ λ means: whenever a Borel set has Lebesgue measure zero, it also has μ_X-measure zero. When this holds, the **Radon-Nikodym theorem** guarantees a unique (up to a.e. equivalence) measurable function f such that μ_X(B) = ∫_B f dλ for all Borel B. This function f is the PDF, and it equals F'(x) almost everywhere. The Radon-Nikodym framing is the rigorous version of the intuitive statement "probability = area under the density curve" — you are literally saying that the probability measure is absolutely continuous with respect to length (Lebesgue measure), and the derivative f is the density of probability per unit length.

Not all distributions have PDFs. A **discrete distribution** concentrates all its mass on a countable set of points: P(X = xₖ) = pₖ > 0 for a countable collection. Such a distribution is singular with respect to Lebesgue measure — it is entirely supported on a set of Lebesgue measure zero — so no Radon-Nikodym density exists. A stranger beast is the **purely singular continuous** distribution, whose CDF is continuous (no atoms) but is constant almost everywhere. The Cantor distribution is the canonical example: its CDF is the Devil's staircase, which increases from 0 to 1 entirely on the Cantor set (measure zero), so its "density" would have to be zero almost everywhere but still integrate to 1 — a contradiction, so no density exists. The full Lebesgue decomposition theorem says every distribution uniquely decomposes into an absolutely continuous part (has a PDF), a discrete part (atoms), and a singular continuous part.

Understanding the Radon-Nikodym perspective matters because it unifies otherwise disparate formulas. The PDF formula P(a < X ≤ b) = ∫_a^b f(x) dx and the PMF formula P(X = k) = pₖ are not really two different things — they are both special cases of P(X ∈ B) = ∫_B dμ_X, one where μ_X is absolutely continuous (use Radon-Nikodym to get f) and one where μ_X is a sum of point masses. Characteristic functions, the joint distribution theory that builds on this topic, and all of measure-theoretic probability depend on fluency with this framework.
