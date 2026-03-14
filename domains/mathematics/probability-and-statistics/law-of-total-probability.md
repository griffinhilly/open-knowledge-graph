---
id: law-of-total-probability
title: Law of Total Probability
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability
  type: hard
builds-toward:
- bayes-theorem
tags:
- probability
- conditional-probability
- partitions
stage: formal-systems
status: draft
---

# Law of Total Probability

## Core Idea
If events B₁, B₂, ..., Bₙ partition the sample space, then P(A) = Σ P(A|Bᵢ)P(Bᵢ). This rule allows us to calculate the probability of an event by conditioning on all possible ways it can occur.

## How It's Best Learned
Work through examples involving disease diagnosis or quality control where you condition on a known partition. Draw tree diagrams showing all paths to the target event. Practice recognizing when this rule applies.

## Common Misconceptions
Not verifying that the events form a partition (they must be mutually exclusive and exhaustive). Forgetting to sum over all conditioning events. Confusing this with just conditional probability.
