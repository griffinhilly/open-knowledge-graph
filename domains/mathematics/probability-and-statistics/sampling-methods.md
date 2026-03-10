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
status: draft
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
