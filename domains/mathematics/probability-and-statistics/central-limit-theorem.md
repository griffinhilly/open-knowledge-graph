---
id: central-limit-theorem
title: Central Limit Theorem
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sampling-distributions
  type: hard
- id: normal-distribution
  type: hard
builds-toward:
- confidence-intervals-means
- hypothesis-testing-fundamentals
tags:
- central-limit-theorem
- clt
- approximate-normality
stage: formal-systems
status: draft
---

# Central Limit Theorem

## Core Idea
The Central Limit Theorem states that for samples of size n drawn from any distribution with mean μ and standard deviation σ, the sample mean x̄ is approximately normally distributed with mean μ and standard deviation σ/√n, regardless of the population's shape—provided n is sufficiently large. This remarkable result justifies using normal-based inference methods for non-normal populations and explains why the normal distribution is so prevalent in statistics.

## How It's Best Learned
Simulate sampling from non-normal populations (uniform, exponential, bimodal). Observe that sample means become more normal as n increases. Verify the standard error formula σ/√n.

## Common Misconceptions
Thinking CLT applies to individual observations (it applies to sample means/sums). Assuming small samples have normal sampling distributions. Forgetting that the population doesn't need to be normal—only sample means do.

## Explainer

The Central Limit Theorem (CLT) is the reason statisticians can apply the same normal-distribution machinery to data from wildly different sources — exponential waiting times, binary survey responses, skewed income data — as long as they're working with sample means rather than individual observations. From your study of sampling distributions, you know that the sample mean x̄ is itself a random variable that varies from sample to sample. The CLT tells you the shape of that distribution: for large enough n, it's approximately normal, regardless of what the population looks like.

Here's the intuition. The sample mean x̄ = (X₁ + X₂ + ... + Xₙ)/n is a scaled sum of independent random variables. When you add many independent random variables, the extreme idiosyncrasies of any single one get averaged out — spikes, skewness, and irregular modes tend to cancel across many draws. What remains in the limit is the smooth, symmetric bell shape of the normal distribution. The mathematical engine behind this is that the **characteristic function** (a tool from probability theory) of a sum of independent variables is the product of individual characteristic functions, and this product converges to the characteristic function of a normal distribution under very mild conditions.

The standard error **σ/√n** is the most practically important consequence. You know from your prerequisite work that the normal distribution has mean μ (the population mean) and some standard deviation. The CLT specifies that standard deviation to be σ/√n, where σ is the population's standard deviation. This formula captures a precise tradeoff: doubling sample size shrinks the spread of x̄ by a factor of √2, not 2. Quadrupling sample size halves the standard error. This square-root relationship governs how quickly estimation precision improves with more data.

How large must n be? The answer depends on the population's shape. For nearly normal populations, even n = 5 or 10 works well. For moderately skewed distributions like incomes or wait times, n = 30 is a common (though rough) threshold. For extremely heavy-tailed or highly irregular distributions, you may need n = 100 or more before the normal approximation is reliable. Simulation is the clearest way to see this: draw repeated samples of size n from a skewed or bimodal population, compute x̄ each time, and plot a histogram of those means. As n grows, the histogram converges visibly to a bell curve centered at μ with spread σ/√n — making concrete what the theorem guarantees in the limit.
