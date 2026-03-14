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
- total-probability
- partition
- law-of-total-probability
stage: formal-systems
status: draft
---

# Law of Total Probability

## Core Idea
If events B₁, B₂, ..., Bₙ partition the sample space (are mutually exclusive and exhaustive), then for any event A: P(A) = Σ P(A|Bᵢ) × P(Bᵢ). This law decomposes the probability of an event into a weighted sum over all possible conditioning scenarios, useful when direct computation is difficult but conditional probabilities are known.
