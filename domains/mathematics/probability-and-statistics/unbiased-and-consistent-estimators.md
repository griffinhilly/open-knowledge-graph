---
id: unbiased-and-consistent-estimators
title: Unbiased and Consistent Estimators
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: point-estimators-properties
  type: hard
builds-toward:
- confidence-intervals-framework
tags:
- estimation
- unbiased
- consistency
stage: formal-systems
status: draft
---

# Unbiased and Consistent Estimators

## Core Idea
An estimator is unbiased if its expected value equals the parameter: E[θ̂] = θ. An estimator is consistent if it converges in probability to the parameter as n → ∞. Unbiasedness is a finite-sample property; consistency is asymptotic.

## How It's Best Learned
Prove unbiasedness and consistency for sample mean and sample variance. Compare estimators: sample variance (unbiased but inconsistent-adjacent concept) versus MLE. Understand why both properties matter.

## Common Misconceptions
Thinking unbiasedness implies consistency or vice versa. Assuming all standard estimators are unbiased. Confusing 'unbiased' with 'accurate' (unbiased estimators can have high variance).
