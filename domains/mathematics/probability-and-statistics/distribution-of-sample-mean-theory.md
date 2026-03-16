---
id: distribution-of-sample-mean-theory
title: Distribution of the Sample Mean
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sampling-distributions-theory
  type: hard
builds-toward:
- central-limit-theorem
- confidence-intervals-means
tags:
- sample-mean
stage: formal-systems
status: draft
---

# Distribution of the Sample Mean

## Core Idea
For random sample X₁,...,Xₙ with mean μ and variance σ²: E[X̄]=μ and Var(X̄)=σ²/n. Standard error SE(X̄)=σ/√n. If population is normal, X̄ is exactly normal; otherwise normal holds approximately for large n by CLT.

## Explainer

From sampling distributions, you know that a statistic is itself a random variable — it varies across samples. The sample mean X̄ = (X₁ + ··· + Xₙ)/n is a particularly important statistic. What can we say about its distribution? Two properties follow from linearity of expectation and variance, without any assumption about the population shape. First, **E[X̄] = μ**: the expected value of the sample mean equals the population mean. Averaging is unbiased — in the long run, the sample mean is right on target. Second, **Var(X̄) = σ²/n**: the variance of the sample mean is n times smaller than the population variance.

The variance formula is the deeper and more important result. Think about why it makes sense: if you average n independent observations, extreme values in individual observations partially cancel each other out. With more observations, there is more cancellation, so the average is less variable. The formula says the variance shrinks proportionally to 1/n. Since standard deviation is the square root of variance, the **standard error SE(X̄) = σ/√n** shrinks proportionally to 1/√n. To halve the standard error, you need four times as many observations — this square root law explains why collecting data has diminishing returns in reducing estimation uncertainty.

The shape of X̄'s distribution depends on the population. If the population is exactly normal — X_i ~ N(μ, σ²) — then X̄ is exactly normal for any sample size n. This follows because the sum of independent normal random variables is normal, and dividing by n just rescales. In this case, X̄ ~ N(μ, σ²/n) exactly, which is the basis for exact z-tests and t-tests when σ is known. The t-distribution enters when σ must be estimated from the same sample — the extra uncertainty in estimating σ fattens the tails compared to the normal.

When the population is not normal, the exact distribution of X̄ is typically intractable. Here the **Central Limit Theorem** provides the rescue: for any population with finite mean μ and variance σ², the standardized sample mean (X̄ − μ)/(σ/√n) converges in distribution to the standard normal as n → ∞. In practice this approximation is reliable for n ≥ 30 for moderately skewed populations, though heavier-tailed distributions require larger n. The CLT is why the normal distribution appears throughout statistics: even if individual measurements are not normal, averages of many measurements tend to be, and statistics are almost always aggregates of many observations.
