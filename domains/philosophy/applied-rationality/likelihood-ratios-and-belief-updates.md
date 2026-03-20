---
id: likelihood-ratios-and-belief-updates
title: "Likelihood Ratios and Belief Updates"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: bayesian-thinking-in-practice
    type: hard
  - id: bayes-theorem
    type: hard
  - id: conditional-probability
    type: soft
builds-toward:
  - calibration-training
  - reference-class-forecasting
tags: ["bayesian", "likelihood-ratio", "belief-updating", "quantitative-reasoning"]
stage: advanced
status: draft
---

## Core Idea

The likelihood ratio is the engine of Bayesian updating: it measures how much more (or less) likely a piece of evidence is under one hypothesis compared to another. A likelihood ratio of 10 means the evidence is 10 times more likely if the hypothesis is true than if it is false — a strong update. A ratio near 1 means the evidence is equally expected either way — no update warranted. Thinking in likelihood ratios rather than raw probabilities makes Bayesian reasoning more intuitive: instead of juggling joint probabilities, you ask "how much more expected is this evidence under my hypothesis?" and shift your confidence proportionally. In log-odds form, updates become simple addition: log-odds posterior = log-odds prior + log likelihood ratio.

## How It's Best Learned

Practice with the classic medical diagnosis example: a test with 99% sensitivity and 5% false positive rate gives a likelihood ratio of 99/5 ≈ 20. For a disease with 1% base rate (prior odds 1:99), a positive test gives posterior odds of 20:99, or about 17% — far from certainty despite a 99% accurate test. Work problems in both probability and log-odds form to build fluency with both representations.

## Common Misconceptions

- A high likelihood ratio does not mean the hypothesis is probably true — it depends on the prior. A likelihood ratio of 100 applied to a prior of 1 in a million still yields a tiny posterior.
- Likelihood ratios are not the same as the probability of the hypothesis given the evidence — that is the posterior, which combines the ratio with the prior.
