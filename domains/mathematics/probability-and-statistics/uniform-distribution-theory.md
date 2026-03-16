---
id: uniform-distribution-theory
title: 'Uniform Distribution: Theory and Applications'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-density-functions-theory
  type: hard
builds-toward:
- normal-distribution-theory
tags:
- uniform
stage: formal-systems
status: draft
---

# Uniform Distribution: Theory and Applications

## Core Idea
Uniform[a,b] has constant density f(x)=1/(b−a). E[X]=(a+b)/2, Var(X)=(b−a)²/12. Probabilities equal interval lengths. Used for inverse transform sampling and as baseline for model comparison.

## Explainer

The uniform distribution is the simplest possible continuous distribution: every point in [a, b] is equally likely, and probability is purely proportional to length. From your prerequisite on **probability density functions**, you know that P(c ≤ X ≤ d) = ∫ f(x) dx over [c, d]. For the uniform, f(x) = 1/(b−a) is constant, so the integral is just (d−c)/(b−a) — the fraction of the interval's total length that [c, d] occupies. This makes all computations immediate: no integration is required once you see the geometry.

The mean (a+b)/2 is the midpoint of the interval, exactly where symmetry demands it be. The variance (b−a)²/12 scales with the square of the interval length: double the width, quadruple the variance. This formula is worth memorizing alongside the normal distribution's variance, because the standard uniform (a=0, b=1) has variance 1/12 ≈ 0.083 — a reference point for how much variability a bounded distribution with no preference for any sub-region can have.

The deepest application of the uniform distribution is the **probability integral transform**: if X is any continuous random variable with CDF F, then the transformed variable U = F(X) follows Uniform[0,1]. Running this in reverse — if U ~ Uniform[0,1], then X = F⁻¹(U) has CDF F — is the foundation of **inverse transform sampling**. Every software package that generates random numbers from non-uniform distributions (normal, exponential, Poisson, beta) ultimately starts from uniform pseudo-random numbers and transforms them. The uniform distribution is thus the universal raw material of random simulation.

As a modeling assumption, Uniform[a, b] encodes maximum ignorance about a bounded quantity: you know only that the value lies in [a, b] and have no additional information favoring any sub-region. In Bayesian statistics, a uniform prior over a parameter's plausible range is a natural starting point when all values in the range seem equally credible before seeing data. In performance evaluation, a model that does no better than predicting uniformly at random over an output range provides a natural performance floor — a baseline against which more sophisticated models should be compared.
