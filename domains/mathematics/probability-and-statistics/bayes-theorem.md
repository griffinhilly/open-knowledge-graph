---
id: bayes-theorem
title: Bayes' Theorem
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability
  type: hard
- id: independence-and-multiplication-rule
  type: soft
tags:
- bayes-theorem
- prior
- posterior
- likelihood
- medical-testing
stage: formal-systems
status: validated
---

# Bayes' Theorem

## Core Idea
Bayes' theorem provides a way to update probabilities given new evidence: P(A | B) = P(B | A) · P(A) / P(B). The denominator P(B) is expanded using the law of total probability: P(B) = P(B | A)·P(A) + P(B | Aᶜ)·P(Aᶜ). Bayes' theorem formalizes how prior beliefs (P(A)) are updated by data (the likelihood P(B | A)) to produce posterior beliefs (P(A | B)), making it the foundation of Bayesian statistics.

## How It's Best Learned
Medical screening is the canonical application: given a rare disease (low prior) and an imperfect test (high sensitivity), compute the probability a positive test actually indicates disease. The result surprises most students and builds genuine appreciation for the theorem.

## Common Misconceptions
- Ignoring the base rate (prior probability) — leading to incorrect intuitions about rare events.
- Confusing the likelihood P(B | A) with the posterior P(A | B).
- Treating Bayes' theorem as a formula to memorize rather than a consequence of conditional probability definitions.
