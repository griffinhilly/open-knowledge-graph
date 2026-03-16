---
id: z-test-for-means
title: One-Sample Z-Test for Means
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
- id: standard-normal-and-z-scores
  type: hard
- id: central-limit-theorem
  type: soft
- id: p-values-and-significance
  type: soft
builds-toward:
- t-test-for-means
tags:
- z-test
- one-sample
- test-statistic
- known-variance
- hypothesis-testing
stage: formal-systems
status: validated
---
# One-Sample Z-Test for Means

## Core Idea
The one-sample z-test assesses whether a sample mean x̄ differs significantly from a hypothesized population mean μ₀, when the population standard deviation σ is known. The test statistic z = (x̄ − μ₀) / (σ/√n) follows a standard normal distribution under H₀, by the central limit theorem. The z-test is rarely applicable in practice (σ is almost never known) but provides the theoretical foundation for the more practical t-test.

## How It's Best Learned
Work through complete examples: state H₀ and Hₐ, compute z, find the p-value from the z-table, state the conclusion in context. Practice both one-tailed and two-tailed tests. Explicitly note that the z-test assumes σ is known — ask students why this is unrealistic.

## Common Misconceptions
- Dividing by σ instead of σ/√n — forgetting the standard error adjustment.
- Using the z-test when the population is non-normal and n is small.
- Stating the conclusion in terms of x̄ rather than the population parameter μ.

## Explainer

From hypothesis testing fundamentals you already know the setup: you have a null hypothesis H₀ (some claim about a population parameter) and an alternative Hₐ (what you believe might be true instead), and you need a procedure for deciding whether your data are surprising enough under H₀ to reject it. The one-sample z-test is the cleanest instantiation of that procedure for population means, because the math falls out in a single, interpretable formula.

The core move is **standardization**. You know from z-scores that any normal random variable X with mean μ and standard deviation σ can be transformed to a standard normal by computing (X − μ)/σ. The sample mean x̄ from a sample of size n is itself a random variable — it has mean μ (assuming H₀ is true) and standard deviation σ/√n, which is called the **standard error**. The standard error is smaller than σ because averaging over n observations reduces the spread: the more data you collect, the more precisely x̄ estimates μ. By the central limit theorem, x̄ is approximately normally distributed for large n regardless of the shape of the population. This is what justifies using the normal distribution to evaluate the test.

Substituting x̄ into the standardization formula gives the test statistic: z = (x̄ − μ₀) / (σ/√n). Here μ₀ is the hypothesized mean from H₀. Under H₀ this statistic follows a standard normal distribution, so large |z| values indicate that x̄ is far from μ₀ in units of standard errors — suspicious evidence against H₀. The **p-value** you already know is then just the probability of observing |z| this extreme or more under the standard normal, which you read from the z-table.

The practical limitation is equally important to understand: σ is virtually never known in real research. You know the sample standard deviation s, not the population σ. When you substitute s for σ, the resulting statistic no longer follows a standard normal — it follows a t-distribution, which has heavier tails to account for the extra uncertainty. The z-test is therefore mostly theoretical scaffolding: it reveals the logic clearly (standardize, compare to reference distribution, compute p-value), and that logic carries over without change to the t-test you study next. Think of the z-test as the idealized version of the procedure, made concrete before the complication of unknown σ is introduced.
