---
id: sampling-methods
title: Sampling Methods
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sample-vs-population
  type: hard
builds-toward:
- sampling-distributions
tags:
- simple-random-sample
- stratified
- cluster
- systematic-sampling
- bias
stage: formal-systems
status: validated
---

# Sampling Methods

## Core Idea
Statistical inference requires that samples be drawn in ways that allow valid generalization to the population. Simple random sampling (SRS) gives every individual an equal chance of selection and is the theoretical gold standard. Stratified sampling divides the population into subgroups and samples each stratum, improving precision when groups differ. Cluster and systematic sampling are practical alternatives. Non-probability methods (convenience, voluntary response) introduce bias that cannot be corrected by increasing sample size.

## How It's Best Learned
Design a study: ask students to estimate average sleep hours for the school. How would they sample? Walk through each method's implementation and flaws. Emphasize that randomization is the key to valid inference, not sample size alone.

## Common Misconceptions
- Thinking bigger samples always fix bias — a large biased sample is worse than a small random one.
- Confusing stratified sampling (sampling within each stratum) with cluster sampling (sampling entire clusters).
- Assuming any sample called 'random' in a study actually used probability sampling.

## Explainer

You already know the distinction between a sample and a population. Now the question becomes: how should you draw that sample? The answer matters enormously, because the validity of every inference you make depends on it. The central insight of this topic is that **randomization** — not sample size — is what makes inference valid.

**Simple random sampling (SRS)** is the theoretical foundation. Every individual in the population has an equal probability of selection, and every possible sample of size n is equally likely. This guarantees that the sample is an unbiased representation of the population in the precise sense that the expected value of any sample statistic equals the corresponding population parameter. SRS is the gold standard against which all other methods are judged. In practice, drawing a true SRS requires a complete list of the population and a mechanism for random selection, which is often expensive or logistically impossible — motivating the alternatives.

Real-world sampling often requires modifications. **Stratified sampling** divides the population into mutually exclusive subgroups (strata) — say, age groups or geographic regions — and draws a separate random sample from each stratum. When strata differ substantially in the quantity being measured, stratification reduces variance and improves precision compared to SRS of the same total size. **Cluster sampling** works differently: divide the population into clusters (schools, city blocks), randomly select entire clusters, and study every individual within selected clusters. This is cheaper when populations are geographically dispersed but introduces more variability because individuals within a cluster tend to be similar. **Systematic sampling** picks every kth individual from an ordered list — easy to implement, but vulnerable if there is a periodic pattern in the list that aligns with the sampling interval.

The critical danger is **non-probability sampling**: convenience samples (whoever is easy to reach) and voluntary response samples (whoever chooses to respond). These introduce **bias** that cannot be reduced by increasing n. A famous cautionary tale is the 1936 Literary Digest poll predicting Landon over Roosevelt — they mailed surveys to millions drawn from phone books and car registrations, which over-represented wealthy Republicans. Gallup sampled only a few thousand using probability methods and correctly predicted Roosevelt's landslide. The lesson: a large biased sample is worse than a small random one, because a bigger biased sample just gives you a more confident wrong answer.
