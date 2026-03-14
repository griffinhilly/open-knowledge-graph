---
id: anova-one-way-theory
title: 'One-Way ANOVA: Theory and F-Test'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: anova-one-way
  type: soft
- id: f-distribution-theory
  type: hard
builds-toward:
- multiple-comparisons
tags:
- anova
stage: formal-systems
status: draft
---

# One-Way ANOVA: Theory and F-Test

## Core Idea
Tests H₀: μ₁=...=μₖ across k groups. F=(MS_Between)/(MS_Within) with df (k−1, n−k). MS_Between ∝ group means variation; MS_Within ∝ within-group error. Assumes equal variances, normality, independence. Rejects if F is large.
