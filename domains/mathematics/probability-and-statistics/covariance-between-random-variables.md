---
id: covariance-between-random-variables
title: Covariance and Correlation of Random Variables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value
  type: hard
- id: variance-of-random-variables
  type: hard
builds-toward:
- joint-probability-distributions
- linear-regression
tags:
- dependence
- covariance
- correlation
stage: formal-systems
status: draft
---

# Covariance and Correlation of Random Variables

## Core Idea
Covariance measures how two random variables vary together: Cov(X,Y) = E[(X-μ_X)(Y-μ_Y)]. Correlation ρ = Cov(X,Y)/(σ_X σ_Y) scales covariance to [-1,1]. Correlation measures linear association; covariance incorporates both direction and scale.

## How It's Best Learned
Calculate covariance and correlation from bivariate data. Visualize relationships with scatterplots. Understand that correlation ≠ causation. Examine how transformations affect covariance.

## Common Misconceptions
Assuming zero correlation means independence. Thinking high covariance means strong relationship (it depends on variable scales). Interpreting correlation causally. Forgetting that covariance and correlation only measure linear association.

## Explainer

From expected value, you know E[X] is the "center of mass" of a random variable — the long-run average. From variance, you know Var(X) = E[(X − μ_X)²] measures how spread out X is around its mean, by averaging squared deviations. **Covariance** extends this idea from one variable to two: Cov(X, Y) = E[(X − μ_X)(Y − μ_Y)] averages the *product* of deviations. When X is above its mean and Y is simultaneously above its mean, the product (X − μ_X)(Y − μ_Y) is positive. When they move in opposite directions, the product is negative. The expected value of these products captures the overall tendency.

A practical computing formula is Cov(X, Y) = E[XY] − E[X]E[Y]. This is analogous to Var(X) = E[X²] − (E[X])², and it is often easier to apply. Notice that Cov(X, X) = Var(X) — variance is just covariance of a variable with itself. Covariance is **bilinear**: Cov(aX + b, cY + d) = ac · Cov(X, Y), meaning constants and shifts affect covariance multiplicatively. This bilinearity makes covariance central to the variance of sums: Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y). When X and Y are independent, the covariance term vanishes, giving the familiar Var(X + Y) = Var(X) + Var(Y).

The problem with raw covariance is that it depends on the units of X and Y. If X is measured in centimeters rather than meters, Cov(X, Y) scales by 100. To get a unit-free measure, **normalize** by dividing by the standard deviations: ρ = Cov(X, Y) / (σ_X σ_Y). This is the **correlation coefficient**, guaranteed to lie in [−1, 1]. Values near ±1 indicate a near-perfect linear relationship; values near 0 indicate little linear relationship. The Cauchy-Schwarz inequality is what constrains ρ to this range.

The most important subtlety is the gap between correlation and independence. If X and Y are independent, then E[XY] = E[X]E[Y], so Cov(X, Y) = 0 and ρ = 0. But the converse fails: zero correlation does not imply independence. A classic example: let X be uniform on [−1, 1] and Y = X². Then Cov(X, Y) = E[X³] − E[X]E[X²] = 0 − 0 = 0, yet Y is completely determined by X — perfect dependence, but nonlinear. Correlation only detects *linear* association; any purely nonlinear relationship can be invisible to it.
