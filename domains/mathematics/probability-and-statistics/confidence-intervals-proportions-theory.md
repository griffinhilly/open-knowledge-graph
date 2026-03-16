---
id: confidence-intervals-proportions-theory
title: Confidence Intervals for Proportions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: binomial-distribution-properties
  type: hard
- id: central-limit-theorem-theory
  type: hard
builds-toward:
- hypothesis-testing-fundamentals
tags:
- confidence-interval
- proportions
stage: formal-systems
status: draft
---

# Confidence Intervals for Proportions

## Core Idea
Sample proportion p̂=X/n has approximately N(p, p(1−p)/n) distribution when np≥10 and n(1−p)≥10. CI: p̂±z_{α/2}√(p̂(1−p̂)/n). Exact methods (Clopper-Pearson) preferred when normality conditions fail.

## Explainer

You know from the Central Limit Theorem that sample means of i.i.d. observations are approximately normally distributed for large n. A sample proportion p̂ = X/n is a special case: X counts successes in n Bernoulli trials, so X ~ Binomial(n, p). Each trial contributes either 0 or 1 to the sum, and p̂ is the mean of these 0-1 observations. By the CLT, p̂ ≈ N(p, p(1−p)/n) — the true proportion p is the mean of the Bernoulli, and p(1−p) is its variance, so the standard error of p̂ is √(p(1−p)/n).

The confidence interval formula follows directly from this approximation. A 95% confidence interval for a Normal mean is point estimate ± 1.96 × (standard error). Since we don't know p (that's what we're estimating), we plug in p̂ in its place: CI = p̂ ± z_{α/2} √(p̂(1−p̂)/n). Here z_{α/2} is the z-critical value for the desired confidence level — 1.96 for 95%, 2.576 for 99%. The **margin of error** is the ± part: it tells you the half-width of the interval.

The conditions np ≥ 10 and n(1−p) ≥ 10 (sometimes stated as np ≥ 5) ensure the Binomial is well-approximated by the Normal. Intuitively, if p = 0.01 and n = 50, then you'd expect only 0.5 successes on average — the distribution is heavily skewed toward zero, and the Normal approximation is poor. These conditions require enough expected successes *and* expected failures for the distribution to look roughly symmetric and bell-shaped. When they fail, the Normal-based interval can have poor **coverage** — the actual proportion of intervals containing the true p may be much less than the nominal 95%.

In that case, the **Clopper-Pearson interval** (also called the "exact" binomial interval) uses the Binomial distribution directly rather than the Normal approximation. It constructs the interval by finding the values of p that make the observed count X neither too extreme in the lower tail nor the upper tail. Clopper-Pearson is conservative — its actual coverage is always at least the nominal level — but it tends to be wider than necessary. This is the fundamental tradeoff: the approximate Normal interval is narrower and simpler but unreliable for small n or extreme p; the exact interval is always valid but wider.

A useful fact: the margin of error is maximized when p̂ = 0.5, giving maximum margin = z_{α/2} / (2√n). For a 95% CI and n = 1000, this is approximately 1.96/(2·31.6) ≈ 0.031 — about 3 percentage points. This is why political polls with "margin of error ±3%" typically use roughly 1,000 respondents. Doubling the precision (halving the margin) requires quadrupling n — the square root in the denominator means precision is expensive to buy with sample size alone.
