---
id: t-distribution-theory
title: 'T-Distribution: Theory and Inference'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: t-distribution
  type: soft
- id: standard-normal-z-scores-theory
  type: hard
builds-toward:
- t-test-for-means
- confidence-intervals-means
tags:
- t-distribution
stage: formal-systems
status: draft
---

# T-Distribution: Theory and Inference

## Core Idea
T(k) has heavier tails than N(0,1) and is used when population SD is unknown. Arises when replacing σ with sample s. As k→∞, T(k)→N(0,1). More conservative than z-test, reflecting additional uncertainty from estimating σ.
