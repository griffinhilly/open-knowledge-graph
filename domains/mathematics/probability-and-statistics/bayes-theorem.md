---
id: bayes-theorem
title: Bayes' Theorem
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability
  type: hard
- id: law-of-total-probability
  type: hard
tags:
- bayes
- posterior
- prior
- likelihood
stage: formal-systems
status: draft
---

# Bayes' Theorem

## Core Idea
Bayes' theorem gives the posterior probability P(B|A) = P(A|B) × P(B) / P(A), allowing us to reverse the direction of conditioning. It describes how to update prior beliefs P(B) when we observe evidence A, using the likelihood P(A|B). This is foundational for statistical inference and decision-making under uncertainty.

## How It's Best Learned
Start with medical testing scenarios (positive test → disease probability). Work through multi-step examples with explicit calculation of the denominator using the law of total probability.

## Common Misconceptions
Confusing P(A|B) with P(B|A) (base rate fallacy). Forgetting to normalize by P(A) in the denominator.
