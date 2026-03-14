---
id: confidence-intervals-proportions-theory
title: Confidence Intervals for Proportions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: binomial-distribution-properties
  type: hard
- id: central-limit-theorem-theory
  type: hard
builds-toward:
- hypothesis-testing-fundamentals
tags:
- confidence-interval
- proportions
stage: formal-systems
status: draft
---

# Confidence Intervals for Proportions

## Core Idea
Sample proportion p̂=X/n has approximately N(p, p(1−p)/n) distribution when np≥10 and n(1−p)≥10. CI: p̂±z_{α/2}√(p̂(1−p̂)/n). Exact methods (Clopper-Pearson) preferred when normality conditions fail.
