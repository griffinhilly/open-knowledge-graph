---
id: confidence-intervals-framework
title: 'Confidence Intervals: General Framework'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sampling-distributions
  type: hard
- id: standard-error-of-estimators
  type: hard
builds-toward:
- confidence-intervals-means
- confidence-intervals-proportions
tags:
- inference
- confidence-intervals
- estimation
stage: formal-systems
status: draft
---

# Confidence Intervals: General Framework

## Core Idea
A confidence interval is an interval estimate of a parameter with specified confidence level. A 95% CI means that if we repeated sampling, 95% of intervals constructed this way would contain the true parameter. The interval is: estimate ± (critical value) × (standard error).

## How It's Best Learned
Simulate repeated sampling and construct CIs to verify coverage. Understand that confidence level is about the method, not the specific interval. Explore how sample size, confidence level, and variability affect interval width.
