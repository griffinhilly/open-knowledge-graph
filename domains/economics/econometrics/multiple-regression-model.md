---
id: multiple-regression-model
title: Multiple Regression
domain: economics
course: econometrics
prerequisites:
- id: bivariate-regression
  type: hard
- id: ols-assumptions
  type: hard
- id: matrices-intro
  type: soft
- id: matrix-operations
  type: soft
builds-toward:
- coefficient-interpretation-regression
- f-test-joint-significance
- omitted-variable-bias
- multicollinearity
- dummy-variables-regression
tags:
- multiple-regression
- OLS
- controls
- matrix-form
stage: formal-systems
status: draft
---

# Multiple Regression

## Core Idea
Multiple regression extends OLS to include several explanatory variables: y = β₀ + β₁x₁ + β₂x₂ + … + βₖxₖ + u. Each coefficient βⱼ represents the partial effect of xⱼ on y holding all other regressors constant — this 'ceteris paribus' interpretation is the central analytical payoff. In matrix form, the estimator is β̂ = (X'X)⁻¹X'y, which requires (X'X) to be invertible (no perfect multicollinearity). Adding control variables changes coefficient estimates if and only if those controls are correlated with both the dependent variable and the included regressors.

## How It's Best Learned
Compare simple and multiple regression estimates on the same dataset — seeing how the wage coefficient on education changes when experience is added illustrates what 'holding constant' means in practice.

## Common Misconceptions
- More control variables do not always improve estimation — including irrelevant variables reduces efficiency and including endogenous controls can introduce new bias.
- The coefficient on x₁ does not represent the effect of x₁ alone; it is always conditional on the other included variables.
