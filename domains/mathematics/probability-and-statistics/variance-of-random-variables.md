---
id: variance-of-random-variables
title: Variance and Standard Deviation of Random Variables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value
  type: hard
- id: measures-of-spread
  type: soft
builds-toward:
- sampling-distributions
- binomial-distribution
tags:
- variance
- standard-deviation
- random-variable
- spread
stage: formal-systems
status: draft
---

# Variance and Standard Deviation of Random Variables

## Core Idea
The variance of a random variable X is Var(X) = E[(X − μ)²] = E(X²) − [E(X)]², measuring expected squared deviation from the mean. The standard deviation σ = √Var(X) restores original units. Key rules: Var(aX + b) = a²Var(X) (adding a constant doesn't change spread; scaling multiplies variance by the square of the scale factor). For independent variables, Var(X + Y) = Var(X) + Var(Y) — variances add for independent random variables, but standard deviations do not.

## How It's Best Learned
Use the shortcut formula E(X²) − μ² in practice, but derive Var(X) = E[(X − μ)²] conceptually first. Emphasize the independence requirement for adding variances — this is a common source of errors.

## Common Misconceptions
- Adding standard deviations directly instead of adding variances first.
- Thinking Var(X + Y) = Var(X) + Var(Y) holds without independence.
- Forgetting that the ±b shift in aX + b has no effect on variance.
