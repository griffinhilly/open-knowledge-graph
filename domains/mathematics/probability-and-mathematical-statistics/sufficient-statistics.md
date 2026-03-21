---
id: sufficient-statistics
title: Sufficient Statistics
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: conditional-expectation
  type: hard
- id: exponential-family
  type: soft
builds-toward:
- rao-blackwell-theorem
- cramer-rao-lower-bound
tags:
- sufficient-statistics
- statistics
- inference
stage: advanced
status: draft
---

# Sufficient Statistics

## Core Idea
A statistic T(X) is sufficient for θ if the conditional distribution of X given T(X) does not depend on θ. Intuitively, T captures all information about θ in the data. The factorization theorem: T is sufficient iff f(x|θ) = g(T(x)|θ)h(x) where h doesn't depend on θ. Sufficient statistics form the basis for efficient inference.

## Questions

```yaml
- question: "The sample mean X̄ is a sufficient statistic for the mean μ of a normal distribution with known variance. Which statement best captures what 'sufficient' means here?"
  type: multiple-choice
  options:
    - "X̄ is the most accurate (minimum variance) unbiased estimator of μ"
    - "Given X̄, the conditional distribution of the full data no longer contains any information about μ"
    - "X̄ uses all n observations in its formula, so no information is discarded"
    - "No other statistic derived from the data could provide additional information about μ beyond what X̄ already provides"
  answer: 1
  explanation: "Sufficiency is precisely the statement that T(X) 'screens off' the raw data from the parameter: knowing T(X), the conditional distribution of X given T(X) = t does not depend on θ. So a second analyst who only receives T(X) can do everything inferentially that a first analyst with the full dataset can do. Option A confuses sufficiency with efficiency (minimum variance). Option C confuses using all data points in a formula with capturing all parameter information. Option D is close but subtly wrong — another statistic *could* be computed, but it adds no new information about θ."

- question: "You have a random sample from a Poisson(λ) distribution. Another analyst tells you only the sample sum ΣXᵢ. According to sufficiency of ΣXᵢ for λ, which of the following is correct?"
  type: multiple-choice
  options:
    - "You could reconstruct the individual observation values from ΣXᵢ if you knew their order"
    - "The sample sum is less informative than the sample mean since it ignores sample size"
    - "Knowing the individual observation values beyond ΣXᵢ provides additional information about λ that ΣXᵢ alone does not capture"
    - "Knowing the individual observation values beyond ΣXᵢ provides no additional information about λ"
  answer: 3
  explanation: "This is the direct meaning of sufficiency: once you have the sufficient statistic ΣXᵢ, the remaining individual data values (conditioned on the sum) are distributed independently of λ — they carry no further information about λ. The analogy: if you want to know how many heads a biased coin will produce, knowing the total number of heads in n flips (the sufficient statistic) tells you everything; the order of the flips adds nothing. Option C (wrong answer) is the common mistake of assuming more data always means more information — sufficiency is exactly the theorem that says a compressed summary can be lossless."

- question: "A sufficient statistic must always reduce the data to a single scalar number."
  type: true-false
  answer: false
  explanation: "Sufficient statistics can be vector-valued. For a Uniform(0, θ) distribution, the sufficient statistic is the sample maximum X_(n) — a single number. But for a Normal(μ, σ²) distribution with both parameters unknown, the sufficient statistic is the pair (X̄, S²) — a two-dimensional vector. More generally, k-parameter exponential family distributions have k-dimensional sufficient statistics. The dimensionality of the sufficient statistic reflects how many degrees of freedom the parameter has, not some general rule that compression must reach a single number."

- question: "If T(X) is a sufficient statistic for θ, any one-to-one function of T(X) is also sufficient for θ."
  type: true-false
  answer: true
  explanation: "A one-to-one (invertible) function of a sufficient statistic is still sufficient, because no information is lost. If you know h(T(X)) and h is invertible, you can recover T(X) exactly, so the conditional distribution of X given h(T(X)) still does not depend on θ. This is why ΣXᵢ and X̄ are both sufficient for the normal mean — they contain identical information. However, a non-invertible function of a sufficient statistic is generally *not* sufficient, because it may discard information."

- question: "Explain in your own words why the factorization theorem — f(x|θ) = g(T(x)|θ)·h(x) — captures the concept of sufficiency."
  type: short-answer
  answer: "The factorization says the likelihood function can be split into two parts: g, which depends on both the data and θ but only through the statistic T(x), and h, which depends on the data but not on θ. This means all of the data's 'signal' about θ flows through T(x). The part of the data not captured by T(x) — encoded in h(x) — tells you nothing about θ. So conditioning on T(x), the remaining variation in x is parameter-free, which is exactly what sufficiency requires."
  explanation: "The factorization is powerful because it gives a practical test for sufficiency without computing conditional distributions directly. If you can write the joint density as a product where one factor only involves θ through T(x) and the other factor is free of θ, then T(x) is sufficient. The intuition: g(T(x)|θ) is the 'informative' factor; h(x) is the 'noise' that carries no signal about θ. This structure also underlies the Rao-Blackwell theorem — a sufficient statistic is the right object to condition on when improving estimators."
```
