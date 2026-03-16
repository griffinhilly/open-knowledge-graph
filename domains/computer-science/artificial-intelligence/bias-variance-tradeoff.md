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
- id: expected-value-and-variance
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

## Explainer

From your knowledge of expected value and variance, you know that the expected value of a random variable captures its central tendency, while variance captures how much it fluctuates around that center. The bias-variance tradeoff applies these same concepts to prediction models: **bias** measures how far the model's average prediction is from the truth (systematic error), while **variance** measures how much the model's predictions change when trained on different samples of data (instability). The total expected test error decomposes cleanly into three terms: Error = Bias² + Variance + Irreducible Noise.

Consider a concrete example. Suppose you are trying to predict house prices from square footage, and the true relationship is gently curved. A linear regression model imposes a straight line — it has **high bias** because its rigid assumption systematically misses the curvature, but **low variance** because a straight line fit on one sample looks nearly identical to one fit on another sample. A degree-15 polynomial can capture any curve, giving it **low bias**, but it is so flexible that it also fits the noise in each particular training set — on different samples, the wiggly polynomial looks wildly different, giving it **high variance**. Both models have high error, but for opposite reasons.

The tradeoff is inescapable because bias and variance pull in opposite directions as you increase model complexity. Simple models (few parameters, strong assumptions) have high bias and low variance. Complex models (many parameters, weak assumptions) have low bias and high variance. The sweet spot — the complexity level that minimizes total error — depends on the amount of training data and the true complexity of the underlying relationship. With very little data, simpler models win because there is not enough information to reliably fit a complex model; the variance penalty dominates. With abundant data, more complex models become viable because variance decreases as sample size grows.

This decomposition explains phenomena you will encounter repeatedly in machine learning. **Overfitting** is a variance problem: the model has learned noise in the training data that does not generalize. **Underfitting** is a bias problem: the model is too simple to capture real patterns. Regularization techniques (L1, L2 penalties) work by explicitly trading a small increase in bias for a large decrease in variance. The bias-variance framework gives you a diagnostic language — when your training error is low but test error is high, you have a variance problem; when both are high, you have a bias problem — and it guides every subsequent decision about model selection, regularization strength, and data collection strategy.
