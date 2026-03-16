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
stage: formal-systems
status: draft
---

# Moment Generating Functions

## Core Idea
The moment generating function (MGF) is M(t) = E[e^{tX}], defined for t in some neighborhood of 0. If M(t) exists, all moments can be recovered: E[Xᵏ] = M^{(k)}(0). The MGF uniquely determines the distribution, and convergence of MGFs implies convergence of distributions.

## Explainer

The **moment generating function** is an encoding trick: it packages all the moments of a distribution into a single function of one variable t. The definition M(t) = E[e^{tX}] looks mysterious at first, but the connection to moments becomes transparent through the **Taylor series** you already know. Recall that e^{tX} = 1 + tX + t²X²/2! + t³X³/3! + ... Taking expectations term by term: M(t) = 1 + t·E[X] + t²·E[X²]/2! + t³·E[X³]/3! + ... This is the ordinary power series for M(t) with coefficients E[Xᵏ]/k!. Differentiating k times and evaluating at t = 0 plucks out E[Xᵏ], which is exactly why the kth derivative at zero gives the kth moment: M^{(k)}(0) = E[Xᵏ].

This makes computing **variance and higher moments** from prerequisites much easier for well-known distributions. For the exponential distribution with rate λ, M(t) = λ/(λ − t) for t < λ. Differentiating: M'(t) = λ/(λ − t)², so E[X] = M'(0) = 1/λ. Differentiating again: M''(t) = 2λ/(λ − t)³, giving E[X²] = 2/λ² and Var(X) = 2/λ² − (1/λ)² = 1/λ². One function generates everything. For the normal distribution N(μ, σ²), the MGF is M(t) = exp(μt + σ²t²/2) — a compact encoding that makes normal calculations tractable.

The deeper power of the MGF is that it **uniquely determines the distribution**: two distributions with the same MGF (when it exists on an open interval around 0) are identical. This is analogous to how a function is determined by all its derivatives at a point (when the Taylor series converges). This uniqueness property is the key to proving limit theorems: if you can show that the MGF of a sequence of distributions converges to M(t) = exp(μt + σ²t²/2) (the normal MGF), then the distributions themselves converge to normal. This is one route to the **Central Limit Theorem** — show that the MGF of the standardized sum converges pointwise to the standard normal MGF.

One important caveat: the MGF may fail to exist (the expectation E[e^{tX}] may be infinite) for heavy-tailed distributions like the Cauchy. This is why the **characteristic function** (replacing t with it, using complex exponentials) is more generally applicable and is the preferred tool in rigorous probability theory — the characteristic function always exists because |e^{itX}| = 1. Think of the MGF as the practical, computable tool for distributions with finite moments, and the characteristic function as its more powerful but less elementary extension.
