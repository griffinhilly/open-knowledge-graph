---
id: true-score-theory-and-measurement-error
title: True Score Theory and Measurement Error
domain: psychology
course: psychometrics
prerequisites:
- id: classical-test-theory
  type: hard
builds-toward:
- domain-sampling-theory-reliability-generalization
- standard-error-of-measurement-applications
tags:
- classical-test-theory
- measurement-error
- reliability
stage: advanced
status: draft
---

# True Score Theory and Measurement Error

## Core Idea
In classical test theory, an observed score equals the true score plus random error: X = T + E. True scores represent the expected value of measurements across infinite replications, while error is assumed random, uncorrelated with true scores, and independent across administrations. This foundational model underlies all reliability theory and score interpretation.

## Explainer

Classical test theory begins with a deceptively simple equation: **X = T + E**. The observed score (X) is the number you actually get when someone takes a test. The true score (T) is the theoretical value that the person "really" has — the average they would obtain if you could give them the same test infinitely many times under identical conditions. The error (E) is everything else: guessing, momentary distraction, misread instructions, how the person happened to sleep the night before. This decomposition is so fundamental that nearly all of psychometrics is an elaboration of its implications.

The model makes several critical assumptions. **Error is random**: it is uncorrelated with the true score, so high-ability people don't have systematically higher or lower errors than low-ability people. This is why averaging helps — random errors cancel out, while the true score accumulates. **Errors across items and occasions are uncorrelated**: knowing that you got one item wrong by guessing doesn't tell you anything about the next item's error. And the true score is defined as the **expected value** of observed scores across repeated measurement — not a score the person "really has" in some metaphysical sense, but a statistical limit toward which their scores would converge with more measurement.

These assumptions have direct practical consequences. Because error is random and uncorrelated with T, the variance of observed scores equals the variance of true scores plus the variance of error: Var(X) = Var(T) + Var(E). **Reliability** is simply the proportion of observed-score variance that is true-score variance: r = Var(T) / Var(X). A perfectly reliable test would have no error variance; all variability in observed scores would reflect real differences between people. In practice, reliability coefficients of .80–.90 are considered good for psychological measures, meaning 10–20% of observed score variance is measurement error.

The practical payoff is **the standard error of measurement** (SEM): SEM = SD × √(1 − r), where SD is the standard deviation of observed scores. The SEM tells you how much an individual's score might fluctuate from measurement to measurement due to error alone, and it enables you to construct confidence intervals around observed scores. Crucially, this means no single test score should be interpreted as a precise point estimate — it is always an estimate with uncertainty. When a psychologist reports that a person has an IQ of 112, best practice is to interpret this as a range (perhaps 107–117) rather than a precise number, because the observed score contains error and the true score is never directly observed.
