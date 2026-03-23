---
id: sampling-distributions
title: Sampling Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-intro
  type: hard
- id: sample-spaces-and-events
  type: soft
builds-toward:
- central-limit-theorem
- confidence-intervals-means
- confidence-intervals-proportions
tags:
- sampling-distribution
- sample-mean
- sample-proportion
stage: formal-systems
status: validated
---

# Sampling Distributions

## Core Idea
A sampling distribution is the probability distribution of a statistic (like sample mean or sample proportion) computed from all possible samples of a given size from a population. The sampling distribution of the sample mean x̄ has mean μ and standard deviation σ/√n (the standard error). Sampling distributions form the foundation of statistical inference by describing how statistics vary from sample to sample and enabling us to quantify uncertainty in estimators.

## How It's Best Learned
Simulate drawing many samples and computing statistics for each. Observe that the sampling distribution of means is less spread out than the population. Verify theoretical standard errors match simulation results.

## Common Misconceptions
Confusing the population distribution with the sampling distribution. Thinking larger samples have larger standard errors. Assuming sampling distribution is normal without sufficient sample size or population normality.

## Questions

```yaml
- question: "A population has mean μ = 50 and standard deviation σ = 10. For random samples of size n = 25, what is the standard error of the sample mean?"
  type: multiple-choice
  options: ["10", "2", "0.4", "50"]
  answer: 1
  explanation: "Standard error = σ/√n = 10/√25 = 10/5 = 2. The standard error measures how much the sample mean varies from sample to sample. It shrinks as n grows because averaging more observations cancels out individual variability."

- question: "If you increase the sample size from n = 25 to n = 100, the standard error of the sample mean doubles."
  type: true-false
  answer: false
  explanation: "Increasing sample size DECREASES the standard error. Going from n = 25 to n = 100 changes √n from 5 to 10, so the standard error is halved (σ/10 instead of σ/5). A common misconception is that more data means more variability; in fact, averaging more observations reduces the variability of the estimate."

- question: "What is the difference between the population distribution and the sampling distribution of the sample mean?"
  type: short-answer
  answer: "The population distribution describes how individual observations vary. The sampling distribution of the sample mean describes how the average of a sample (of size n) varies across all possible samples. The sampling distribution has mean μ and standard deviation σ/√n, and is approximately normal for large n regardless of the population's shape."
  explanation: "These are distributions at different levels: one describes raw observations, the other describes a statistic computed from a batch of observations. The distinction is fundamental to inference — when we use x̄ to estimate μ, we are reasoning about the sampling distribution, not the population distribution directly."
```

## Explainer

Suppose you want to estimate the mean height of all adults in a country. You cannot measure everyone, so you draw a random sample of 100 people and compute their average height x̄. But if someone else draws a different sample of 100, they get a slightly different x̄. A third person gets yet another. The sampling distribution is the probability distribution of all these x̄ values — a description of how the sample mean behaves across every possible sample of the same size. It is a distribution of a statistic, not a distribution of individual observations.

This is the conceptual shift that makes statistical inference possible. Rather than treating x̄ as a single fixed number, we recognize it is itself a random variable: it varies because it depends on which random sample was drawn. The sampling distribution quantifies that variability. Its mean equals the population mean μ (the estimator is unbiased — on average, it hits the target), and its standard deviation — called the standard error — equals σ/√n. The standard error tells you how much a typical sample mean strays from the truth.

The standard error formula SE = σ/√n contains a critical insight: increasing sample size reduces uncertainty, but at a diminishing rate. To halve the standard error, you must quadruple the sample size (because √(4n) = 2√n). This is why large studies provide more precise estimates, but doubling your effort does not double your precision. A persistent misconception runs in the wrong direction — that larger samples produce more variability. The opposite is true: averaging more observations cancels individual fluctuations. Think of it this way: if you flip a coin 10 times you might get 8 heads, but if you flip 10,000 times you will almost certainly land very close to 50%.

It is essential to keep two distributions separate in your mind. The population distribution describes how individual data points are spread — it might be skewed, bimodal, or any shape at all. The sampling distribution of the mean describes how the average of a random sample behaves — and for large enough n, this distribution is approximately normal by the Central Limit Theorem, regardless of the population's shape. The population could be heavily skewed (like household income), yet sample means from that population will be approximately bell-shaped once n is large enough.

Sampling distributions underlie every tool of classical inference. When you construct a confidence interval for a mean, you are asking: given the sampling distribution, what range of sample means would occur 95% of the time? When you run a hypothesis test, you ask: if the null hypothesis were true, how likely is a sample mean this extreme? Both questions are answered by the sampling distribution — it is the bridge between the probability theory you have been building and the inferential statistics that uses it.
