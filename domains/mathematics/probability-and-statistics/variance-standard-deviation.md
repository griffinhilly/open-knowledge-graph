---
id: variance-standard-deviation
title: Variance and Standard Deviation
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value-theory
  type: hard
builds-toward:
- covariance-between-random-variables
- chebyshev-bounds
tags:
- variance
- spread
stage: formal-systems
status: draft
---

# Variance and Standard Deviation

## Core Idea
Variance σ²=Var(X)=E[(X−μ)²]=E[X²]−μ² measures spread. Standard deviation σ=√Var(X) is in original units. Var(aX+b)=a²Var(X). For independent variables, Var(X+Y)=Var(X)+Var(Y). Variance characterizes dispersion around the mean.

## Explainer

You already know that the **expected value** E[X] = μ is the probability-weighted average of a random variable — the center of mass of the distribution. But two distributions can share the same mean yet behave very differently. A coin that pays $1 with certainty has the same expected value as a coin that pays $0 or $2 with equal probability, but the second one is riskier. **Variance** is the tool that quantifies that spread.

Variance is defined as Var(X) = E[(X − μ)²]. The logic: subtract the mean from each outcome to get the deviation, square it so negatives don't cancel positives, then take the expectation. Squaring is the canonical choice — it penalizes large deviations quadratically and produces a mathematically clean theory. The computational shortcut E[X²] − μ² follows directly from expanding the square: E[(X−μ)²] = E[X² − 2μX + μ²] = E[X²] − 2μ² + μ² = E[X²] − μ². Use whichever form is easier for a given distribution.

The squaring introduces a units problem: if X is in dollars, variance is in dollars-squared. **Standard deviation** σ = √Var(X) restores original units and is typically what you report. But variance is what you use in formulas, because it has the crucial additivity property: for *independent* random variables, Var(X + Y) = Var(X) + Var(Y). This property doesn't hold for standard deviation (√(σ_X² + σ_Y²) ≠ σ_X + σ_Y), which is why variance is the fundamental object even if standard deviation is more interpretable.

The scaling rule Var(aX + b) = a²Var(X) is worth internalizing. Shifting a distribution by a constant b doesn't change its spread — variance ignores location. Scaling by a factor a stretches all deviations by a, so squared deviations scale by a². This means if you double the measurement scale of a variable, its variance quadruples. This rule is essential for standardizing random variables: if you form Z = (X − μ)/σ, then Var(Z) = (1/σ²)·Var(X) = (1/σ²)·σ² = 1. Standard deviation is the natural unit of spread, and standardization sets it to 1.

Variance connects to everything downstream. The Chebyshev inequality (which you'll study next) uses variance to bound how much probability can lie far from the mean — a distribution with small variance can't put much probability far from its center. Covariance, which measures joint spread of two variables, is the generalization of variance to pairs: Cov(X, X) = Var(X). Understanding variance as squared expected deviation from the mean is the conceptual foundation for all of these extensions.
