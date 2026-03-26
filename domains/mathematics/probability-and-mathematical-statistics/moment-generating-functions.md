---
id: moment-generating-functions
title: Moment Generating Functions
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: variance-higher-moments-rigorous
  type: hard
- id: taylor-series
  type: soft
builds-toward:
- characteristic-functions
- central-limit-theorem-rigorous
- multivariate-normal-distribution
tags:
- mgf
- generating-functions
- moments
stage: advanced
status: validated
---

# Moment Generating Functions

## Core Idea
The moment generating function (MGF) is M(t) = E[e^{tX}], defined for t in some neighborhood of 0. If M(t) exists, all moments can be recovered: E[Xᵏ] = M^{(k)}(0). The MGF uniquely determines the distribution, and convergence of MGFs implies convergence of distributions.

## Questions

```yaml
- question: "Which of the following is FALSE about moment generating functions?"
  type: multiple-choice
  options:
    - "The kth derivative of M(t) evaluated at t = 0 equals E[Xᵏ]"
    - "If the MGF exists on an open interval around 0, it uniquely determines the probability distribution"
    - "The MGF always exists for any random variable, since e^{tX} is always a real number"
    - "Convergence of MGFs to M(t) implies convergence of the corresponding distributions"
  answer: 2
  explanation: "The MGF M(t) = E[e^{tX}] requires computing an expectation, which may be infinite. For heavy-tailed distributions like the Cauchy, E[e^{tX}] = ∞ for any t ≠ 0 — the MGF does not exist. The other three statements are all true when the MGF exists on an open interval around 0. This is precisely why the characteristic function φ(t) = E[e^{itX}] is preferred in rigorous probability theory: |e^{itX}| = 1 always, so the characteristic function always exists."

- question: "A sequence of standardized random variables has MGFs that converge pointwise to exp(t²/2). This fact is most directly useful for proving:"
  type: multiple-choice
  options:
    - "That the random variables have finite variance equal to 1"
    - "That the distributions converge to a standard normal distribution"
    - "That the characteristic functions of the sequence do not exist"
    - "That the random variables are independent"
  answer: 1
  explanation: "The MGF of a standard normal N(0,1) is exp(t²/2). The MGF continuity theorem states that if the MGFs of a sequence converge pointwise to the MGF of some distribution X in a neighborhood of 0, then the distributions converge weakly to the distribution of X. So convergence of MGFs to exp(t²/2) directly implies convergence in distribution to N(0,1). This is one proof route for the Central Limit Theorem — show that the MGF of the standardized sum of iid variables converges to exp(t²/2)."

- question: "The moment generating function M(t) = E[e^{tX}] typically exists for any random variable X, because e^{tX} is a well-defined real number for most value of X."
  type: true-false
  answer: false
  explanation: "e^{tX} is indeed a real number for each specific value of X, but the MGF requires taking the *expectation* E[e^{tX}], which is an integral (or sum) over all possible values. For heavy-tailed distributions, this integral diverges — the MGF is infinite. The Cauchy distribution is the standard example: E[e^{tX}] = ∞ for all t ≠ 0. This is why the characteristic function E[e^{itX}], which uses complex exponentials satisfying |e^{itX}| = 1, is more general."

- question: "Two random variables X and Y with the same moment generating function (wherever it exists on an open interval around 0) must have identical probability distributions."
  type: true-false
  answer: true
  explanation: "This uniqueness property is what makes the MGF so powerful for proving limit theorems. It is analogous to the fact that a smooth function is determined by all its Taylor coefficients at a point — the MGF encodes all moments, and when those are sufficient to determine the distribution (which requires the MGF to exist on an open interval, ensuring the Taylor series converges), the distribution is fully pinned down. This is why showing that MGFs converge is equivalent to showing that distributions converge."

- question: "Explain why differentiating the MGF M(t) = E[e^{tX}] exactly k times and evaluating at t = 0 recovers the kth moment E[Xᵏ]."
  type: short-answer
  answer: "By the Taylor expansion, e^{tX} = 1 + tX + t²X²/2! + t³X³/3! + ⋯ Taking expectations term by term gives M(t) = 1 + tE[X] + t²E[X²]/2! + t³E[X³]/3! + ⋯ This is a power series in t with coefficient E[Xᵏ]/k! in front of tᵏ. Differentiating a power series k times and evaluating at t = 0 isolates the coefficient of tᵏ and multiplies by k!, yielding E[Xᵏ]."
  explanation: "The Taylor series argument is the cleanest way to see why the MGF 'generates' moments. The function e^{tX} is just a device for packaging all powers of X into one expression, weighted by powers of t. Taking the expectation distributes this over all moments. The derivative operation then acts as a 'selector' that extracts one moment at a time by evaluating at t = 0, where all higher-power terms vanish. The key requirement is that the Taylor series of M(t) converges — guaranteed when M(t) exists in an open interval around 0."
```

## Explainer

The **moment generating function** is an encoding trick: it packages all the moments of a distribution into a single function of one variable t. The definition M(t) = E[e^{tX}] looks mysterious at first, but the connection to moments becomes transparent through the **Taylor series** you already know. Recall that e^{tX} = 1 + tX + t²X²/2! + t³X³/3! + ... Taking expectations term by term: M(t) = 1 + t·E[X] + t²·E[X²]/2! + t³·E[X³]/3! + ... This is the ordinary power series for M(t) with coefficients E[Xᵏ]/k!. Differentiating k times and evaluating at t = 0 plucks out E[Xᵏ], which is exactly why the kth derivative at zero gives the kth moment: M^{(k)}(0) = E[Xᵏ].

This makes computing **variance and higher moments** from prerequisites much easier for well-known distributions. For the exponential distribution with rate λ, M(t) = λ/(λ − t) for t < λ. Differentiating: M'(t) = λ/(λ − t)², so E[X] = M'(0) = 1/λ. Differentiating again: M''(t) = 2λ/(λ − t)³, giving E[X²] = 2/λ² and Var(X) = 2/λ² − (1/λ)² = 1/λ². One function generates everything. For the normal distribution N(μ, σ²), the MGF is M(t) = exp(μt + σ²t²/2) — a compact encoding that makes normal calculations tractable.

The deeper power of the MGF is that it **uniquely determines the distribution**: two distributions with the same MGF (when it exists on an open interval around 0) are identical. This is analogous to how a function is determined by all its derivatives at a point (when the Taylor series converges). This uniqueness property is the key to proving limit theorems: if you can show that the MGF of a sequence of distributions converges to M(t) = exp(μt + σ²t²/2) (the normal MGF), then the distributions themselves converge to normal. This is one route to the **Central Limit Theorem** — show that the MGF of the standardized sum converges pointwise to the standard normal MGF.

One important caveat: the MGF may fail to exist (the expectation E[e^{tX}] may be infinite) for heavy-tailed distributions like the Cauchy. This is why the **characteristic function** (replacing t with it, using complex exponentials) is more generally applicable and is the preferred tool in rigorous probability theory — the characteristic function always exists because |e^{itX}| = 1. Think of the MGF as the practical, computable tool for distributions with finite moments, and the characteristic function as its more powerful but less elementary extension.
