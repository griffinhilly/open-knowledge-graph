---
id: consistency-of-estimators
title: Consistency of Estimators
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: convergence-in-probability
  type: hard
- id: maximum-likelihood-estimation-theory
  type: soft
builds-toward:
- asymptotic-normality-mle
tags:
- consistency
- asymptotics
- estimation
stage: formal-systems
status: draft
---

# Consistency of Estimators

## Core Idea
An estimator θ̂ₙ is consistent if θ̂ₙ converges in probability to θ as n → ∞. Consistency is a minimum requirement for reasonable estimators—as sample size grows, the estimator should approach the truth. Under regularity conditions, MLEs and method of moments estimators are consistent.

## Explainer

An estimator is a rule for turning data into a guess about an unknown parameter. For that rule to be useful, it should at minimum do better with more data — intuitively, collecting millions of observations should get you very close to the truth. **Consistency** formalizes this requirement using the language of convergence in probability that you already know.

Recall that θ̂ₙ converges in probability to θ means: for any ε > 0, the probability P(|θ̂ₙ − θ| > ε) → 0 as n → ∞. In words, the chance that your estimate is far from the truth becomes negligible as the sample grows. This is weaker than almost-sure convergence (which says the estimate *will* eventually be close with probability 1 along every path), but it is the standard benchmark for estimators. A consistent estimator might produce a bad estimate for any specific sample — you could get unlucky — but the probability of a bad estimate vanishes as n grows.

The most important consistency results are for the **sample mean** and for **MLEs**. The sample mean X̄ₙ is consistent for the population mean μ by the Weak Law of Large Numbers, which is itself a direct consequence of convergence in probability. For MLEs, consistency follows from general regularity conditions (differentiability of the log-likelihood, identifiability of the model, compactness arguments) and is one reason MLEs are the default estimator in most settings. A useful sufficient condition: if an estimator is unbiased (E[θ̂ₙ] = θ) and its variance vanishes (Var(θ̂ₙ) → 0), then by Chebyshev's inequality it is consistent. But note that consistency does not require unbiasedness — a biased estimator can still be consistent if the bias shrinks to zero with n.

What consistency does *not* guarantee is equally important. Consistency is an asymptotic property — it says nothing about performance at any finite sample size. An estimator could be badly biased for small n yet perfectly consistent. And consistency gives no rate: it does not tell you how quickly the estimate approaches the truth. That information lives in **asymptotic normality** (the next topic), which tells you √n(θ̂ₙ − θ) converges in distribution to a normal, quantifying the speed of convergence and enabling confidence intervals. Think of consistency as the entry requirement for an estimator — necessary but far from sufficient for a complete understanding of its behavior.
