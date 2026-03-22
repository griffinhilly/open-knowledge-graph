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

## Questions

```yaml
- question: "A researcher wants to estimate average daily screen time for teenagers nationally. She posts a survey link on social media and gets 50,000 responses. A colleague runs a simple random sample of 400 teenagers from a national registry. Whose result should you trust more?"
  type: multiple-choice
  options:
    - "The 50,000-response survey — larger samples are always more accurate"
    - "The 400-person random sample — randomization, not size, determines validity"
    - "They are equally valid — both capture real responses from real teenagers"
    - "The 50,000 survey — self-selection introduces healthy diversity of perspectives"
  answer: 1
  explanation: "The 50,000-response survey is a voluntary response sample: only people motivated enough to click and respond are included, systematically over-representing high-screen-time users who may be more online. This bias cannot be reduced by collecting more responses — it just yields a more confident wrong answer. The 400-person SRS gives every teenager an equal chance of selection, making it an unbiased representation of the population. This is the core lesson of the 1936 Literary Digest poll, which polled millions yet wrongly predicted the election outcome."

- question: "A researcher studying income by region divides the US into four geographic quadrants and draws a separate random sample from each. A second researcher randomly selects 50 city blocks nationwide and surveys every household in each selected block. Which methods are these, respectively?"
  type: multiple-choice
  options:
    - "Stratified sampling; cluster sampling"
    - "Cluster sampling; stratified sampling"
    - "Systematic sampling; simple random sampling"
    - "Stratified sampling; systematic sampling"
  answer: 0
  explanation: "Stratified sampling divides the population into mutually exclusive subgroups (strata) and draws a separate random sample from each — here, the four geographic quadrants. Cluster sampling divides the population into clusters, randomly selects entire clusters, and studies every individual within them — here, the 50 city blocks (all households surveyed within selected blocks). The key distinction: in stratified sampling you sample *within* every stratum; in cluster sampling you select entire clusters and skip all others."

- question: "Increasing the size of a convenience sample will eventually eliminate sampling bias if the sample is large enough."
  type: true-false
  answer: false
  explanation: "Bias from non-probability sampling cannot be corrected by increasing sample size. A larger convenience or voluntary-response sample just produces a more statistically precise estimate of the wrong quantity. The mechanism of bias — systematic over- or under-representation of certain groups — is unaffected by n. Only switching to a probability-based sampling method (where every member of the population has a known, nonzero chance of selection) eliminates bias."

- question: "Simple random sampling is the theoretical gold standard for inference because every individual in the population has an equal probability of being selected."
  type: true-false
  answer: true
  explanation: "This is precisely what makes SRS the foundation of sampling theory. Equal probability of selection (and, more precisely, equal probability for every possible sample of size n) guarantees that the sample is an unbiased representation of the population — the expected value of any sample statistic equals the corresponding population parameter. All other probability sampling methods (stratified, cluster, systematic) trade off some of this theoretical purity for practical benefits like reduced variance or cost."

- question: "Why is a large biased sample potentially worse than a small random one — not just less accurate, but actively worse?"
  type: short-answer
  answer: "A large biased sample produces a precise estimate of the wrong quantity, giving false confidence in an incorrect conclusion. The statistical precision (narrow confidence interval) makes the wrong answer look reliable, so decision-makers are more likely to act on it. A small random sample is honest about its uncertainty — its wide confidence interval signals that we don't know much. The biased sample is misleading in a way the small random sample is not."
  explanation: "Precision and accuracy are distinct properties. Precision refers to how consistent or tightly clustered estimates are; accuracy refers to whether they're centered on the truth. A large biased sample can be highly precise (low variance from repetition) but systematically inaccurate. The danger is that standard error calculations assume randomness — applied to a biased sample, they give artificially narrow intervals that don't account for the bias at all. You end up confidently wrong rather than usefully uncertain."
```

## Explainer

You already know the distinction between a sample and a population. Now the question becomes: how should you draw that sample? The answer matters enormously, because the validity of every inference you make depends on it. The central insight of this topic is that **randomization** — not sample size — is what makes inference valid.

**Simple random sampling (SRS)** is the theoretical foundation. Every individual in the population has an equal probability of selection, and every possible sample of size n is equally likely. This guarantees that the sample is an unbiased representation of the population in the precise sense that the expected value of any sample statistic equals the corresponding population parameter. SRS is the gold standard against which all other methods are judged. In practice, drawing a true SRS requires a complete list of the population and a mechanism for random selection, which is often expensive or logistically impossible — motivating the alternatives.

Real-world sampling often requires modifications. **Stratified sampling** divides the population into mutually exclusive subgroups (strata) — say, age groups or geographic regions — and draws a separate random sample from each stratum. When strata differ substantially in the quantity being measured, stratification reduces variance and improves precision compared to SRS of the same total size. **Cluster sampling** works differently: divide the population into clusters (schools, city blocks), randomly select entire clusters, and study every individual within selected clusters. This is cheaper when populations are geographically dispersed but introduces more variability because individuals within a cluster tend to be similar. **Systematic sampling** picks every kth individual from an ordered list — easy to implement, but vulnerable if there is a periodic pattern in the list that aligns with the sampling interval.

The critical danger is **non-probability sampling**: convenience samples (whoever is easy to reach) and voluntary response samples (whoever chooses to respond). These introduce **bias** that cannot be reduced by increasing n. A famous cautionary tale is the 1936 Literary Digest poll predicting Landon over Roosevelt — they mailed surveys to millions drawn from phone books and car registrations, which over-represented wealthy Republicans. Gallup sampled only a few thousand using probability methods and correctly predicted Roosevelt's landslide. The lesson: a large biased sample is worse than a small random one, because a bigger biased sample just gives you a more confident wrong answer.
