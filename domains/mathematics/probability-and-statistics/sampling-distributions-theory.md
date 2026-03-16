---
id: sampling-distributions-theory
title: Sampling Distributions of Statistics
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-definition-types
  type: hard
builds-toward:
- distribution-of-sample-mean
- central-limit-theorem
tags:
- sampling-distribution
stage: formal-systems
status: draft
---

# Sampling Distributions of Statistics

## Core Idea
A sampling distribution is the probability distribution of a sample statistic (mean, proportion, variance) computed from repeated random samples. It describes how statistics vary from sample to sample—crucial for inference. Does not depend on sample size in the way many misconceive.

## Explainer

You already know that a random variable is a quantity whose value is determined by a random process. A sample statistic — a mean, a proportion, a variance — is itself a random variable. It takes a different value every time you draw a new sample from the same population. The **sampling distribution** is simply the probability distribution of that statistic: it tells you, across all possible samples of a given size, how likely each value of the statistic is.

To make this concrete, imagine a population of exam scores with a true mean of 72 and a standard deviation of 10. If you draw one random sample of 30 students and compute the sample mean, you might get 71.4. Draw another 30 students and you might get 73.1. Do this thousands of times, collect every sample mean, and plot the histogram — that histogram approximates the sampling distribution of the sample mean. Notice that the sampling distribution is a distribution *about the statistic itself*, not about individual scores. Its center, spread, and shape are separate questions from those of the original population.

The sampling distribution's shape and spread depend on two things: the population distribution and the sample size n. When n is small, the sampling distribution of the mean inherits more of the population's quirks (skewness, heavy tails). As n increases, something remarkable happens — the sampling distribution of the mean tends toward a normal distribution regardless of the population's shape. That is the content of the Central Limit Theorem, which builds directly on this concept. What matters here is understanding *why* the sampling distribution exists as an object: it captures the variability introduced by the random act of sampling, not variability in the population itself.

A crucial precision: the sampling distribution exists even when you only draw one sample in practice. It is a theoretical object — the distribution you would observe *if* you could repeat the experiment many times. This is the foundation of all frequentist inference. When a textbook says "the standard error of the mean is σ/√n," it is describing the standard deviation of the sampling distribution of the sample mean. Every confidence interval and hypothesis test is a statement about where in the sampling distribution the observed statistic falls — which is why mastering this concept unlocks everything that follows in statistical inference.
