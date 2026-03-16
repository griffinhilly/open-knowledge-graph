---
id: likelihood-ratio-tests
title: Likelihood Ratio Tests
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: neyman-pearson-lemma
  type: hard
- id: convergence-in-distribution
  type: soft
builds-toward:
- uniformly-most-powerful-tests
tags:
- likelihood-ratio-tests
- hypothesis-testing
- statistics
stage: advanced
status: draft
---

# Likelihood Ratio Tests

## Core Idea
The likelihood ratio test rejects H₀ when Λ = L(θ̂₀|X)/L(θ̂|X) < c, where θ̂₀ is the MLE under H₀ and θ̂ is the unrestricted MLE. Under H₀, -2log(Λ) converges in distribution to χ²_r where r is the dimension reduction. LR tests are general and achieve optimal Type II error (power) asymptotically.

## Explainer

The **Neyman-Pearson lemma** — your core prerequisite — gave you the most powerful test for a specific kind of problem: a simple null hypothesis (H₀: θ = θ₀) against a simple alternative (H₁: θ = θ₁). The NP test rejects when the likelihood ratio L(θ₁|x)/L(θ₀|x) exceeds a threshold. That ratio compares two fixed parameter values. The likelihood ratio test generalizes this idea to composite hypotheses, where H₀ and H₁ each specify a set of parameter values rather than a single point.

The key insight is to replace the two fixed likelihoods with the best possible likelihoods under each hypothesis. Let Θ₀ be the null parameter space and Θ be the full parameter space. Define the **likelihood ratio statistic** Λ = sup_{θ ∈ Θ₀} L(θ|x) / sup_{θ ∈ Θ} L(θ|x). The numerator is the maximum likelihood achievable while respecting H₀; the denominator is the maximum likelihood overall, achieved at the unrestricted MLE θ̂. Since Θ₀ ⊆ Θ, we always have Λ ∈ [0, 1]. A value of Λ near 1 means the null hypothesis fits the data almost as well as the best unconstrained model — no reason to reject. A value of Λ near 0 means the data is far better explained by some θ outside Θ₀ — strong evidence against H₀. The test rejects when Λ < c for some threshold c.

The practical power of the LRT comes from **Wilks' theorem**: under H₀ and regularity conditions, the statistic −2 log Λ converges in distribution to a chi-squared distribution with r degrees of freedom, where r is the difference in the dimension of the full parameter space and the null parameter space (the number of constraints imposed by H₀). This asymptotic result means you can determine the critical value without knowing the exact distribution of Λ: just compare −2 log Λ to the χ²_r quantile for your chosen significance level. Your prerequisite on **convergence in distribution** is exactly what makes this work — you know that "converges in distribution to χ²_r" means the chi-squared approximation becomes exact as n → ∞, and is often good enough for moderate n.

As a concrete example, suppose X₁, …, Xₙ ~ Normal(μ, σ²) with both μ and σ² unknown, and you want to test H₀: μ = 0 against H₁: μ ≠ 0. The full model has two free parameters (μ, σ²); under H₀, only σ² is free. So r = 2 − 1 = 1, and −2 log Λ ≈ χ²₁. In this normal case, the LRT is equivalent to the t-test (the t-statistic squared follows an F-distribution, and by Wilks the LRT is asymptotically equivalent). For more complex models — exponential families, nested regression models, logistic regression — Wilks' theorem delivers the same chi-squared test, making the LRT a universal framework rather than a collection of special-case tests.
