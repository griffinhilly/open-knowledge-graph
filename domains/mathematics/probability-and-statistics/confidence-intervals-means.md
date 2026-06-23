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
- id: confidence-intervals-framework
  type: hard
- id: distribution-of-sample-mean-theory
  type: hard
- id: standard-normal-z-scores-theory
  type: hard
- id: t-distribution-theory
  type: hard
builds-toward:
- hypothesis-testing-fundamentals
tags:
- confidence-interval
- interval-estimation
- t-distribution
stage: formal-systems
status: validated
---

# Confidence Intervals for Means

## Core Idea
A confidence interval for a population mean is an interval (estimate ± margin of error) computed so that, in repeated sampling, it contains the true mean with a specified confidence level (typically 95%). For large samples, use the normal (z) distribution: x̄ ± z* × (s/√n). For smaller samples, use the t-distribution: x̄ ± t* × (s/√n). The confidence level describes the long-run proportion of intervals that capture the parameter, not the probability that the true mean lies in a specific computed interval.

## How It's Best Learned
Compute confidence intervals for various sample sizes and confidence levels. Interpret them correctly in context. Observe that wider confidence levels produce narrower intervals and vice versa.

## Common Misconceptions
Thinking a 95% CI means 95% probability the true mean is in the interval (it's fixed; the interval is random). Confusing confidence level with p-value. Misunderstanding how sample size affects margin of error.

## Questions

```yaml
- question: "A researcher computes a 95% CI for mean sleep hours and gets [6.8, 7.4]. Which interpretation is correct?"
  type: multiple-choice
  options:
    - "There is a 95% probability that the true mean lies between 6.8 and 7.4 hours"
    - "If this procedure were repeated many times, 95% of such intervals would contain the true mean"
    - "95% of people in the sample sleep between 6.8 and 7.4 hours"
    - "The true mean is 95% likely to be close to 7.1 hours"
  answer: 1
  explanation: "The true mean μ is a fixed constant — it either lies in [6.8, 7.4] or it doesn't. Probability doesn't apply to a specific computed interval. What 95% describes is the long-run procedure: if you repeated this sampling and interval-construction process many times, 95% of the resulting intervals would contain μ. Option A is the most common misconception and is incorrect for exactly this reason."

- question: "A 95% CI is computed from a sample of n = 50. If the sample size is increased to n = 200 with the same confidence level, what happens to the interval width?"
  type: multiple-choice
  options:
    - "It stays the same — confidence level determines width, not sample size"
    - "It decreases by a factor of 2 — the margin of error is proportional to 1/√n"
    - "It increases — more data introduces more sources of variability"
    - "It doubles — larger samples cover more of the population"
  answer: 1
  explanation: "The margin of error is z*(s/√n), so it shrinks like 1/√n. Quadrupling n (from 50 to 200) halves √n's denominator effect, cutting the margin of error in half. The common misconception is that more data means more uncertainty; in fact, more data means better precision and a narrower interval."

- question: "A 99% confidence interval computed from the same data is wider than a 95% confidence interval."
  type: true-false
  answer: true
  explanation: "Higher confidence requires a larger multiplier (z* = 2.576 for 99% vs. 1.96 for 95%), which widens the margin of error. The intuition: to be more confident of capturing μ, you must cast a wider net. More confidence always means a wider interval, all else equal."

- question: "A 95% CI guarantees that 95% of future sample means drawn from the same population will fall inside it."
  type: true-false
  answer: false
  explanation: "A CI makes a claim about the population parameter μ, not about future sample means. The 95% refers to the proportion of confidence intervals (computed by this procedure) that would contain μ — a statement about the interval-generating process, not about the distribution of x̄ values. Future sample means are covered by the sampling distribution, which is a separate concept."

- question: "Why is it incorrect to say 'there is a 95% probability that the true mean is in this interval'?"
  type: short-answer
  answer: "The true mean μ is a fixed (though unknown) constant — it either is or isn't in the computed interval. Since μ is not random, probability doesn't apply to it. The randomness is in the interval itself, which varies from sample to sample. '95%' describes what fraction of intervals would contain μ across many repetitions of the procedure, not a probability about where μ sits relative to one particular interval."
  explanation: "This is the central interpretive challenge of confidence intervals. Frequentist probability only applies to random events. Once an interval is computed, μ's location relative to it is a fixed fact — we just don't know which. The correct statement shifts the randomness to the procedure: 'this method produces intervals that capture μ 95% of the time,' not 'this interval has a 95% chance of being right.'"
```

## Explainer

The Central Limit Theorem guarantees that for a large enough sample, the sample mean X̄ is approximately normally distributed with mean μ and standard deviation σ/√n, regardless of the population's shape. This is the fact that makes confidence intervals for means work. From your study of z-scores, you can standardize: the quantity (X̄ - μ)/(σ/√n) is approximately standard normal. Choosing z* = 1.96, we know P(-1.96 ≤ (X̄ - μ)/(σ/√n) ≤ 1.96) ≈ 0.95. Rearranging to isolate μ in the middle gives X̄ - 1.96(σ/√n) ≤ μ ≤ X̄ + 1.96(σ/√n) — the 95% confidence interval.

In practice σ is unknown, so substitute the sample standard deviation s. For large samples (n ≥ 30 is a common guideline), this substitution introduces negligible additional error and the **z-interval** X̄ ± 1.96(s/√n) applies. The quantity 1.96(s/√n) is the **margin of error** — half the interval width. Notice two things: the margin of error shrinks like 1/√n as sample size grows, and the multiplier 1.96 corresponds to 95% confidence. For 99% confidence use z* = 2.576, which widens the interval. More confidence requires a wider net.

For small samples, substituting s for σ introduces real additional uncertainty, and the distribution of (X̄ - μ)/(s/√n) is not exactly standard normal — it follows a **t-distribution** with n-1 degrees of freedom. The t-distribution has heavier tails than the normal, reflecting the extra uncertainty from estimating σ. The **t-interval** X̄ ± t*(s/√n) uses the appropriate t-critical value from a table. For n = 10 at 95% confidence, t* ≈ 2.26 (wider than 1.96). As n increases, the t-distribution approaches the normal and t* approaches z* = 1.96.

The correct interpretation is the most important thing to internalize. A computed interval like [3.2, 4.8] does not have "a 95% probability of containing μ." The true mean μ is a fixed number; it either lies in [3.2, 4.8] or it does not — probability does not apply to the specific interval in front of you. What 95% describes is the **procedure**: if you repeatedly drew samples and computed intervals by this method, 95% of those intervals would contain μ. Confidence is a property of the long-run procedure, not of any individual interval.
