---
id: z-test-t-test-means-theory
title: Z-Tests and T-Tests for Means
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-framework-theory
  type: hard
builds-toward:
- type-i-and-type-ii-errors
tags:
- z-test
- t-test
stage: formal-systems
status: draft
---

# Z-Tests and T-Tests for Means

## Core Idea
Z-test: Z=(X̄−μ₀)/(σ/√n) when σ known. T-test: T=(X̄−μ₀)/(s/√n) with n−1 df when σ unknown. Use t-test (more conservative) in practice. Both test H₀:μ=μ₀. T-distribution accounts for estimating σ from data.

## Explainer

From the hypothesis testing framework, you know the core procedure: assume H₀ is true, compute a test statistic measuring how far the data falls from what H₀ predicts, then calculate the probability of observing a result that extreme by chance. The z-test and t-test are the two standard implementations of this framework when the question is about a population mean. They share the same logic — they differ only in how much you know about the population.

The **z-test** applies when the population standard deviation σ is known. The test statistic is Z = (X̄ − μ₀) / (σ/√n). The denominator σ/√n is the **standard error** — the standard deviation of the sampling distribution of X̄, which you derived from the Central Limit Theorem. Dividing the observed deviation X̄ − μ₀ by the standard error converts the raw difference into a dimensionless z-score: how many standard errors away from μ₀ your sample mean landed. Under H₀, this statistic follows a standard normal distribution, and you look up the tail probability from that distribution.

The **t-test** applies when σ is unknown — which is nearly always in practice. You estimate σ using the sample standard deviation s, giving T = (X̄ − μ₀) / (s/√n). The problem is that s itself varies from sample to sample, introducing additional uncertainty. This extra variability means the test statistic no longer follows a standard normal distribution; instead, it follows a **t-distribution** with n − 1 **degrees of freedom**. The t-distribution looks like a normal distribution but has heavier tails — it assigns more probability to extreme values, making it more conservative. As n grows large, s converges to σ, the t-distribution converges to the normal, and the t-test and z-test give identical results.

The degrees of freedom n − 1 reflect a subtle cost: once you've estimated the mean X̄ from your n data points, only n − 1 of the deviations (xᵢ − X̄) are free to vary independently. The last one is determined by the constraint that deviations sum to zero. Fewer degrees of freedom → more uncertainty → heavier tails → a higher threshold to reject H₀. This is why the t-test is described as more conservative: at small sample sizes, it demands stronger evidence before concluding the effect is real, appropriately accounting for the uncertainty in estimating σ from limited data.
