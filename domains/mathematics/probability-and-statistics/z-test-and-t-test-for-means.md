---
id: z-test-and-t-test-for-means
title: Z-Tests and T-Tests for Means
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
- id: standard-normal-and-z-scores
  type: hard
- id: confidence-intervals-means
  type: soft
tags:
- z-test
- t-test
- test-statistic
- p-value
stage: formal-systems
status: draft
---

# Z-Tests and T-Tests for Means

## Core Idea
A z-test tests hypotheses about a population mean when the population standard deviation σ is known (rare in practice). The test statistic is z = (x̄ - μ₀) / (σ/√n). A t-test is used when σ is unknown and replaced by sample standard deviation s; the test statistic is t = (x̄ - μ₀) / (s/√n), which follows a t-distribution with n-1 degrees of freedom. The t-distribution has heavier tails than normal, so t-tests account for additional uncertainty from estimating σ. Both tests compare observed sample means to hypothesized population means.

## How It's Best Learned
Compute z and t statistics from data. Use tables or software to find p-values. Compare z-test and t-test on the same data for large and small samples. Understand why t-distribution is appropriate for small samples.

## Common Misconceptions
Using z-test when σ is unknown. Confusing degrees of freedom in t-distribution. Thinking larger t values have larger p-values (opposite is true). Misapplying tests without checking normality assumptions for small samples.

## Explainer

You already know the core logic of hypothesis testing: assume the null hypothesis is true, compute how far your sample result is from what the null predicts, and ask how likely such a deviation is by chance. You also know how to convert raw values to **z-scores** using the standard normal distribution. The z-test and t-test both apply that exact logic to sample means — the only real difference is what you know about the population's variability.

A **z-test** applies when you know the true population standard deviation σ. The test statistic z = (x̄ − μ₀) / (σ/√n) measures how many standard errors your sample mean sits from the hypothesized population mean μ₀. The denominator σ/√n is the **standard error of the mean** — the theoretical spread of sample means when repeatedly drawing samples of size n. Because σ is known, this denominator is exact, and the test statistic follows a standard normal distribution precisely. In practice, knowing σ is rare (it would require surveying the entire population), so the z-test is mostly theoretical or used for large samples where the Central Limit Theorem ensures approximate normality.

In real data analysis, you almost always estimate σ from the sample itself using the sample standard deviation s. Plugging s in where σ was gives the **t-test statistic**: t = (x̄ − μ₀) / (s/√n). But here's the subtle problem: s is itself a random variable — it varies from sample to sample — introducing additional uncertainty into the denominator. This extra randomness makes the test statistic follow a **t-distribution** rather than a standard normal. The t-distribution looks like a normal distribution but with heavier tails, reflecting that extreme outcomes are somewhat more likely when your estimate of spread is itself imprecise. The exact shape depends on **degrees of freedom** (df = n − 1): with only a few observations, uncertainty is large and tails are heavy; as n grows, s stabilizes and the t-distribution converges to the standard normal. By n ≈ 30, the two distributions are nearly identical, which is why large-sample z-tests are defensible even when σ is unknown.

The decision rule is the same for both tests: compute the test statistic, find the p-value (the probability of observing a result this extreme under H₀), and compare to your significance level α. A larger absolute value of z or t pushes the p-value *down*, making the result more significant — the opposite of what beginners sometimes assume. When running a two-sided test, you're asking whether your sample mean is far from μ₀ in *either* direction, so you use the total tail probability on both ends. When choosing between z and t, the rule is simple: use t-tests by default. They handle the unknown-σ case correctly, and when n is large enough that z would have been fine, the t-test gives essentially the same answer anyway.

