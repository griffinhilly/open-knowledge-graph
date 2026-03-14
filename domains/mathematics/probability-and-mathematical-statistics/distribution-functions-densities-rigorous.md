---
id: distribution-functions-densities-rigorous
title: Distribution Functions and Densities (Rigorous)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: random-variables-as-measurable-functions
  type: hard
- id: riemann-integral-darboux-sums
  type: hard
builds-toward:
- expectation-measure-theoretic
- joint-distributions-marginals-rigorous
- characteristic-functions
tags:
- distributions
- densities
- measure-theory
stage: abstract-reasoning
status: draft
---

# Distribution Functions and Densities (Rigorous)

## Core Idea
The cumulative distribution function (CDF) F(x) = P(X ≤ x) is right-continuous, non-decreasing, and uniquely determines the distribution of a random variable. A probability density function (pdf) is a measurable function f ≥ 0 where P(X ∈ A) = ∫ₐ f(x) dx with respect to Lebesgue measure. The Radon-Nikodym theorem guarantees densities exist when distributions are absolutely continuous with respect to Lebesgue measure.
