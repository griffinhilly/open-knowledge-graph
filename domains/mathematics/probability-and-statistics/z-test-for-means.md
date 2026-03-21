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

## Questions

```yaml
- question: "A researcher knows the population standard deviation is σ = 10. She takes a sample of n = 25 and observes x̄ = 104. She wants to test H₀: μ = 100. What is the correct z-statistic?"
  type: multiple-choice
  options:
    - "z = (104 − 100) / 10 = 0.4"
    - "z = (104 − 100) / (10/√25) = 2.0"
    - "z = (104 − 100) / √(10/25) = 6.3"
    - "z = (104 − 100) / (10 × 25) = 0.016"
  answer: 1
  explanation: "The test statistic divides by the standard error σ/√n = 10/√25 = 10/5 = 2, giving z = 4/2 = 2.0. Option A uses σ alone (=10) instead of σ/√n — the most common error. Dividing by σ ignores the effect of sample size: a sample mean of 104 from n=25 observations is far more surprising than a single observation of 104, because averaging reduces spread. The standard error σ/√n is what characterizes the spread of sample means."

- question: "After computing z = 2.1 and a two-tailed p-value of 0.036, a student writes: 'There is a 3.6% chance that the sample mean equals the null value.' What is wrong with this statement?"
  type: multiple-choice
  options:
    - "Nothing — the p-value gives the probability that x̄ equals μ₀"
    - "The p-value is the probability of observing a z-statistic this extreme or more extreme, assuming H₀ is true — not the probability that x̄ equals a specific value"
    - "The p-value gives the probability that H₀ is true, not a probability about x̄"
    - "Nothing — the statement is equivalent to saying the result is statistically significant at α = 0.05"
  answer: 1
  explanation: "The p-value is P(|Z| ≥ 2.1 | H₀ true) — a probability about the test statistic under the assumption that H₀ holds. It says nothing directly about whether x̄ equals μ₀ (a specific value has probability 0 for a continuous distribution) or about whether H₀ is true. Misinterpreting p as the probability that H₀ is true (option C) is an equally common error. The correct interpretation is: 'If H₀ were true, we would see a result this extreme only 3.6% of the time by chance.'"

- question: "The standard error σ/√n is smaller than σ because averaging over more observations reduces the variability of the sample mean."
  type: true-false
  answer: true
  explanation: "Each individual observation has variance σ². The sample mean x̄ averages n independent observations, so its variance is σ²/n and its standard deviation is σ/√n. As n increases, the standard error shrinks — large samples produce sample means clustered tightly around μ. This is why a sample mean of 104 is far more statistically surprising (stronger evidence against H₀: μ=100) when n=100 than when n=4, even though x̄ is the same in both cases."

- question: "A z-test is appropriate whenever the sample size is large (n > 30), even when the population standard deviation σ is unknown."
  type: true-false
  answer: false
  explanation: "The z-test requires knowing σ, the population standard deviation — not just the sample standard deviation s. When σ is unknown (which is almost always in practice), substituting s for σ changes the distribution of the test statistic from standard normal to a t-distribution with n−1 degrees of freedom. The t-distribution has heavier tails to account for the extra uncertainty from estimating σ from data. For large n, the t-distribution approximates the normal, but the correct test is still technically a t-test, not a z-test."

- question: "Explain why the z-test formula uses σ/√n in the denominator rather than σ, and what σ/√n represents."
  type: short-answer
  answer: "σ/√n is the standard error of the sample mean — the standard deviation of the sampling distribution of x̄. Individual observations vary with standard deviation σ, but the test is about x̄, not a single observation. By the central limit theorem, x̄ is approximately normally distributed with mean μ and standard deviation σ/√n. Dividing by σ/√n standardizes x̄ into z-score units of 'how many standard errors is x̄ from μ₀?' Using σ instead of σ/√n would ignore sample size entirely: a sample mean of 104 from n=1 and from n=10,000 would produce the same z, which is wrong — larger samples provide far stronger evidence."
  explanation: "The standard error is the key quantity that links sample size to inferential power. It embodies the core logic: more data → tighter sampling distribution of x̄ → more surprising a given deviation from μ₀ → larger |z| → smaller p-value."
```

## Explainer

From hypothesis testing fundamentals you already know the setup: you have a null hypothesis H₀ (some claim about a population parameter) and an alternative Hₐ (what you believe might be true instead), and you need a procedure for deciding whether your data are surprising enough under H₀ to reject it. The one-sample z-test is the cleanest instantiation of that procedure for population means, because the math falls out in a single, interpretable formula.

The core move is **standardization**. You know from z-scores that any normal random variable X with mean μ and standard deviation σ can be transformed to a standard normal by computing (X − μ)/σ. The sample mean x̄ from a sample of size n is itself a random variable — it has mean μ (assuming H₀ is true) and standard deviation σ/√n, which is called the **standard error**. The standard error is smaller than σ because averaging over n observations reduces the spread: the more data you collect, the more precisely x̄ estimates μ. By the central limit theorem, x̄ is approximately normally distributed for large n regardless of the shape of the population. This is what justifies using the normal distribution to evaluate the test.

Substituting x̄ into the standardization formula gives the test statistic: z = (x̄ − μ₀) / (σ/√n). Here μ₀ is the hypothesized mean from H₀. Under H₀ this statistic follows a standard normal distribution, so large |z| values indicate that x̄ is far from μ₀ in units of standard errors — suspicious evidence against H₀. The **p-value** you already know is then just the probability of observing |z| this extreme or more under the standard normal, which you read from the z-table.

The practical limitation is equally important to understand: σ is virtually never known in real research. You know the sample standard deviation s, not the population σ. When you substitute s for σ, the resulting statistic no longer follows a standard normal — it follows a t-distribution, which has heavier tails to account for the extra uncertainty. The z-test is therefore mostly theoretical scaffolding: it reveals the logic clearly (standardize, compare to reference distribution, compute p-value), and that logic carries over without change to the t-test you study next. Think of the z-test as the idealized version of the procedure, made concrete before the complication of unknown σ is introduced.
