---
id: confidence-intervals-means
title: Confidence Intervals for Means
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: central-limit-theorem
  type: hard
- id: standard-normal-and-z-scores
  type: hard
builds-toward:
- hypothesis-testing-fundamentals
tags:
- confidence-interval
- interval-estimation
- t-distribution
stage: formal-systems
status: draft
---

# Confidence Intervals for Means

## Core Idea
A confidence interval for a population mean is an interval (estimate ± margin of error) computed so that, in repeated sampling, it contains the true mean with a specified confidence level (typically 95%). For large samples, use the normal (z) distribution: x̄ ± z* × (s/√n). For smaller samples, use the t-distribution: x̄ ± t* × (s/√n). The confidence level describes the long-run proportion of intervals that capture the parameter, not the probability that the true mean lies in a specific computed interval.

## How It's Best Learned
Compute confidence intervals for various sample sizes and confidence levels. Interpret them correctly in context. Observe that wider confidence levels produce narrower intervals and vice versa.

## Common Misconceptions
Thinking a 95% CI means 95% probability the true mean is in the interval (it's fixed; the interval is random). Confusing confidence level with p-value. Misunderstanding how sample size affects margin of error.

## Explainer

The Central Limit Theorem guarantees that for a large enough sample, the sample mean X̄ is approximately normally distributed with mean μ and standard deviation σ/√n, regardless of the population's shape. This is the fact that makes confidence intervals for means work. From your study of z-scores, you can standardize: the quantity (X̄ - μ)/(σ/√n) is approximately standard normal. Choosing z* = 1.96, we know P(-1.96 ≤ (X̄ - μ)/(σ/√n) ≤ 1.96) ≈ 0.95. Rearranging to isolate μ in the middle gives X̄ - 1.96(σ/√n) ≤ μ ≤ X̄ + 1.96(σ/√n) — the 95% confidence interval.

In practice σ is unknown, so substitute the sample standard deviation s. For large samples (n ≥ 30 is a common guideline), this substitution introduces negligible additional error and the **z-interval** X̄ ± 1.96(s/√n) applies. The quantity 1.96(s/√n) is the **margin of error** — half the interval width. Notice two things: the margin of error shrinks like 1/√n as sample size grows, and the multiplier 1.96 corresponds to 95% confidence. For 99% confidence use z* = 2.576, which widens the interval. More confidence requires a wider net.

For small samples, substituting s for σ introduces real additional uncertainty, and the distribution of (X̄ - μ)/(s/√n) is not exactly standard normal — it follows a **t-distribution** with n-1 degrees of freedom. The t-distribution has heavier tails than the normal, reflecting the extra uncertainty from estimating σ. The **t-interval** X̄ ± t*(s/√n) uses the appropriate t-critical value from a table. For n = 10 at 95% confidence, t* ≈ 2.26 (wider than 1.96). As n increases, the t-distribution approaches the normal and t* approaches z* = 1.96.

The correct interpretation is the most important thing to internalize. A computed interval like [3.2, 4.8] does not have "a 95% probability of containing μ." The true mean μ is a fixed number; it either lies in [3.2, 4.8] or it does not — probability does not apply to the specific interval in front of you. What 95% describes is the **procedure**: if you repeatedly drew samples and computed intervals by this method, 95% of those intervals would contain μ. Confidence is a property of the long-run procedure, not of any individual interval.
