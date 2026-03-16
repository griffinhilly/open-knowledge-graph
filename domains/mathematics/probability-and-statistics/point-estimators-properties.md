---
id: point-estimators-properties
title: Properties of Point Estimators
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value
  type: hard
builds-toward:
- unbiased-and-consistent-estimators
- maximum-likelihood-estimation-intro
tags:
- estimation
- properties
- bias
stage: formal-systems
status: draft
---

# Properties of Point Estimators

## Core Idea
Point estimators have properties including: unbiasedness (E[θ̂] = θ), consistency (θ̂ → θ as n→∞), efficiency (low variance), and robustness. Comparing estimators by these properties helps choose between alternatives.

## How It's Best Learned
Calculate bias and variance of simple estimators analytically. Compare sample mean and sample median as estimators of location. Examine how efficiency changes with sample size or distribution shape.

## Explainer

An estimator is just a recipe — a function of your data that produces a guess for an unknown parameter. Before you can compare two recipes, you need a vocabulary for what "good" means. That vocabulary is the four key properties: unbiasedness, consistency, efficiency, and robustness.

**Unbiasedness** is the most intuitive. An estimator θ̂ is unbiased if, on average over all possible datasets of a given size, it lands exactly on the true parameter: E[θ̂] = θ. Think of it like a scale that, even if individual readings fluctuate, averages out to the true weight. The sample mean X̄ is the classic unbiased estimator of the population mean μ — you can verify this directly using your prerequisite knowledge of expected value: E[X̄] = E[(X₁ + ... + Xₙ)/n] = nμ/n = μ. The **bias** of an estimator is the signed difference E[θ̂] − θ; unbiasedness means bias equals zero.

**Consistency** captures a different desirable behavior: as your sample grows, does θ̂ get closer and closer to θ? A consistent estimator converges in probability to the true parameter as n → ∞. This is an asymptotic property, unlike unbiasedness which applies at every sample size. Most well-behaved estimators are both unbiased and consistent, but they can be decoupled — an estimator can be unbiased at every n yet inconsistent (high variance that never shrinks), or biased at every finite n yet consistent (bias shrinks to zero as n grows).

**Efficiency** asks: among all unbiased estimators, which has the smallest variance? A more efficient estimator wastes less information — it extracts more signal from the same data. The **Cramér-Rao lower bound** establishes the minimum possible variance any unbiased estimator can achieve, and an estimator that achieves this bound is called **efficient**. For example, when data is normally distributed, the sample mean is the efficient estimator of μ — no unbiased estimator can do better with the same data. The sample median is also unbiased for μ (by symmetry) but has higher variance, making it less efficient in the normal case.

**Robustness** is the practical counterpart to efficiency: how badly does the estimator perform when assumptions are violated? The sample mean is efficient under normality but sensitive to outliers — a single extreme value can drag it far from the bulk of the data. The sample median, though less efficient under normality, is **robust**: its value depends only on the middle rank, so outliers cause no damage. Choosing among estimators always involves navigating this tradeoff between efficiency (optimal under the assumed model) and robustness (safe when the model is wrong). Real statistical practice requires knowing which property matters more for the problem at hand.
