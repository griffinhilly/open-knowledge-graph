---
id: bias-variance-tradeoff
title: Bias-Variance Tradeoff
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: probability-basics
  type: hard
- id: expected-value
  type: soft
- id: variance-of-random-variables
  type: soft
tags:
- learning-theory
- generalization
- model-complexity
stage: advanced
status: draft
---

# Bias-Variance Tradeoff

## Core Idea
Test error decomposes into bias (error from model assumptions), variance (sensitivity to training data), and noise. Bias increases with simplicity; variance increases with complexity. Optimal generalization requires balancing these terms.

## How It's Best Learned
Train models of increasing complexity on synthetic data, plotting train/test error to visualize the tradeoff.

## Common Misconceptions
Lower bias does not always mean better models; high bias with low variance often generalizes well. The tradeoff is fundamental.
