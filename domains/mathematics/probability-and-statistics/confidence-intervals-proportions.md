---
id: confidence-intervals-proportions
title: Confidence Intervals for Proportions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: central-limit-theorem
  type: hard
- id: binomial-distribution
  type: soft
builds-toward:
- hypothesis-testing-fundamentals
tags:
- confidence-interval
- proportion
- binomial
stage: formal-systems
status: draft
---

# Confidence Intervals for Proportions

## Core Idea
A confidence interval for a population proportion p is computed from sample proportion p̂. When the sample size is large enough that both np̂ and n(1-p̂) exceed 10, the sample proportion is approximately normal, and we can use: p̂ ± z* × √(p̂(1-p̂)/n). The margin of error decreases with larger sample size and larger confidence level. For smaller samples, exact binomial methods or continuity corrections provide better coverage.

## How It's Best Learned
Compute confidence intervals for proportions in polling contexts. Understand how sample size affects margin of error. Compare normal approximation to exact binomial.

## Common Misconceptions
Using normal approximation when np̂ or n(1-p̂) < 10. Confusing sample proportion p̂ with population proportion p. Thinking margin of error accounts for all sources of error (sampling only).

## Explainer

A proportion is just a mean of 0s and 1s — if you code "success" as 1 and "failure" as 0, then the sample proportion p̂ = (number of successes)/n is the sample mean of those coded values. This observation connects proportions directly to everything you know from the Central Limit Theorem: for large enough n, sample means are approximately normally distributed, so p̂ is approximately normal with mean p (the true population proportion) and variance p(1−p)/n.

The **confidence interval** follows from this normal approximation. Since p̂ is approximately N(p, p(1−p)/n), standardizing gives (p̂ − p)/√(p(1−p)/n) ≈ N(0,1). Rearranging this to isolate p gives an interval centered on p̂: p̂ ± z* × √(p(1−p)/n). The catch is that the true p appears in the standard error formula, but we don't know p (that's what we're trying to estimate). The standard solution is to plug in p̂ for p in the standard error, giving the **Wald interval**: p̂ ± z* × √(p̂(1−p̂)/n). Here z* is the critical value: 1.96 for a 95% confidence level, 2.576 for 99%, and so on — values you can look up from the standard normal table.

The **margin of error** is the ± part: z* × √(p̂(1−p̂)/n). It quantifies the precision of your estimate. Notice that the margin of error shrinks as n grows (proportional to 1/√n) but increases as your confidence level increases (larger z*). To cut the margin of error in half, you need four times as many observations. The margin of error is maximized when p̂ = 0.5 (the most uncertain case), so conservative sample size calculations often assume p̂ = 0.5 when the true proportion is unknown.

The normal approximation breaks down when the sample contains very few successes or failures — specifically when np̂ < 10 or n(1−p̂) < 10. In these cases, the binomial distribution (which you know) is skewed, and the normal approximation produces intervals with poor coverage — they claim 95% but actually contain the truth less often. For small samples, the preferred alternative is the **exact binomial interval** (Clopper-Pearson), which inverts the exact binomial test rather than using a normal approximation. It is more conservative (wider) but has guaranteed coverage properties. In practice, poll results and clinical trial proportions usually have large enough samples that the Wald interval works well, but always check the condition before applying the formula.
