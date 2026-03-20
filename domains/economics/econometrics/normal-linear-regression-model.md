---
id: normal-linear-regression-model
title: Normal Linear Regression Model
domain: economics
course: econometrics
prerequisites:
- id: simple-linear-regression-estimation
  type: hard
- id: normal-distribution
  type: soft
- id: linear-algebra
  type: hard
- id: probability-theory
  type: hard
- id: normal-distribution-theory
  type: hard
builds-toward:
- t-statistic-individual-coefficient
- f-statistic-overall-significance
tags:
- regression
- normality
- inference
- assumptions
stage: advanced
status: draft
---

# Normal Linear Regression Model

## Core Idea
The normal regression model assumes u ~ N(0,σ²) in addition to OLS assumptions. This distributional assumption enables hypothesis testing and confidence intervals via t and F statistics, allowing exact inference in finite samples rather than relying on asymptotics.

## Explainer

From simple linear regression, you know how to estimate coefficients by minimizing the sum of squared residuals. OLS gives you β̂ with desirable properties under the Gauss-Markov assumptions: it's unbiased and efficient among linear estimators. But those properties say nothing about the *distribution* of β̂ — without knowing the shape of that distribution, you cannot make probability statements about how far your estimate might be from the truth. That's where the **normal linear regression model** comes in: by adding one additional assumption about the error term's distribution, you unlock the entire apparatus of hypothesis testing and confidence intervals without needing large samples.

The new assumption is that the error terms follow a **normal distribution**: u ~ N(0, σ²). This is a strong claim — you're asserting not just that errors have mean zero and constant variance (the Gauss-Markov assumptions), but that they're drawn from a bell-shaped distribution. Once you make this assumption, a remarkable thing happens: because OLS is a linear function of the errors, and because linear combinations of normal random variables are also normal, the OLS estimator β̂ is itself normally distributed. Specifically, β̂ ~ N(β, σ²(X'X)⁻¹). You now have the exact sampling distribution of your estimator — not an approximation, but the precise distribution.

This sampling distribution is what makes inference possible. The **t-statistic** for testing whether a coefficient βⱼ equals some hypothesized value β₀ is (β̂ⱼ - β₀) / se(β̂ⱼ), where the standard error is estimated from the data. Under the null hypothesis and the normality assumption, this statistic follows an exact t-distribution with (n-k) degrees of freedom — where n is sample size and k is the number of parameters including the intercept. Similarly, the **F-statistic** for testing joint hypotheses (does this entire set of coefficients equal zero?) follows an exact F-distribution under the null. These are finite-sample results: they hold exactly even in small samples, not just approximately as sample size grows.

Without the normality assumption, you can still do inference — but only asymptotically, by appealing to the Central Limit Theorem. As n → ∞, the distribution of β̂ converges to normal regardless of the distribution of the errors (under mild regularity conditions), so t and F tests remain valid approximately in large samples. The practical implication: in small samples, the normality assumption is load-bearing. If you have 15 observations and your errors are highly skewed, your t-test p-values may be meaningfully wrong. In large samples — say, 500+ observations — the asymptotic justification is usually sufficient, and the normal regression model becomes a special case of the more general asymptotic theory rather than a necessary restriction. This is why econometrics courses introduce the normal model first for clean finite-sample theory, then relax it for the large-sample results that dominate applied work.
