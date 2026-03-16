---
id: method-of-moments
title: Method of Moments
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: variance-higher-moments-rigorous
  type: hard
- id: weak-law-of-large-numbers
  type: soft
builds-toward:
- consistency-of-estimators
tags:
- method-of-moments
- estimation
- statistics
stage: formal-systems
status: draft
---

# Method of Moments

## Core Idea
The method of moments equates sample moments with population moments: set m̂ₖ = μₖ(θ) where m̂ₖ = (1/n)Σ Xᵢᵏ. Solve for θ. This approach is simple but less efficient than MLE. Method of moments estimators are consistent by the WLLN and asymptotically normal under suitable conditions.

## Explainer

Your prerequisite on **variance and higher moments** gave you the concept of population moments: μ'_k = E[X^k], the k-th moment of a distribution — functions of the unknown parameter(s) θ. Your introduction to the **weak law of large numbers** told you that sample averages converge to their expectations. Method of moments puts these two facts together into a simple and general estimation strategy.

The idea is direct: the **k-th sample moment** m̂_k = (1/n)Σᵢ Xᵢᵏ is a natural estimate of the population moment μ'_k(θ) = E[X^k], because the WLLN guarantees m̂_k → μ'_k(θ) in probability. If your model has p unknown parameters, you set up a system of p equations — m̂_1 = μ'_1(θ), m̂_2 = μ'_2(θ), …, m̂_p = μ'_p(θ) — and solve for θ. As a concrete example: for a Normal(μ, σ²) distribution, the first two population moments are μ'_1 = μ and μ'_2 = μ² + σ². Setting m̂_1 = μ̂ and m̂_2 = μ̂² + σ̂² and solving gives μ̂ = X̄ and σ̂² = (1/n)Σ(Xᵢ − X̄)² — the sample mean and sample variance (with divisor n, not n−1).

Method of moments estimators are consistent because they are continuous functions of sample moments that converge in probability to the correct population moments. They are also typically asymptotically normal by the delta method applied to the CLT for sample moments. However, they are often **less efficient than MLEs** because they use only moment summaries and can ignore information embedded in the full shape of the likelihood. For example, for an Exponential(λ) distribution, the MOM estimator from the first moment gives λ̂ = 1/X̄, which coincidentally equals the MLE. But for distributions with complex shapes, like the Beta distribution, MOM and MLE can differ noticeably, with MLE being more efficient.

The real virtue of method of moments is **tractability**. When the log-likelihood is hard to differentiate or maximize analytically, method of moments provides a closed-form starting point — often used to initialize numerical MLE optimization. It is also the conceptual ancestor of **generalized method of moments (GMM)**, a cornerstone of modern econometrics, where you match more moment conditions than you have parameters and use the over-identification as a diagnostic for model misspecification. Before encountering MLE or Bayesian estimation, method of moments teaches the essential principle: use observed data to match theoretically predicted features of the distribution.
