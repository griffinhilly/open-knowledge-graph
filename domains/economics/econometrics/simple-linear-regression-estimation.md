---
id: simple-linear-regression-estimation
title: Simple Linear Regression Estimation
domain: economics
course: econometrics
prerequisites:
- id: least-squares-regression-fundamentals
  type: hard
- id: bivariate-regression
  type: soft
builds-toward:
- normal-linear-regression-model
- coefficient-interpretation-regression
tags:
- ols
- estimation
- regression
- foundations
stage: formal-systems
status: draft
---

# Simple Linear Regression Estimation

## Core Idea
OLS estimation for Y = β₀ + β₁X + u minimizes the sum of squared residuals to estimate coefficients. The estimators β̂₀ and β̂₁ are closed-form linear combinations of the data that produce the best linear prediction in the sense of minimizing squared errors.

## How It's Best Learned
Compute β̂₁ = Cov(X,Y)/Var(X) by hand using simple numeric examples. Then plot regression lines on scatter plots to visualize how OLS finds the line that minimizes residuals.

## Common Misconceptions
OLS does not assume Y is normally distributed—only errors need normality for inference. A high R² does not imply causality; causality requires exogeneity assumptions not testable from the regression alone.

## Explainer

From your work with least-squares regression fundamentals, you already know the core geometric idea: OLS finds the line through a scatter plot that minimizes the total squared vertical distance between each data point and the line. Simple linear regression makes this precise for the model Y = β₀ + β₁X + u. The **slope estimator** β̂₁ = Cov(X,Y)/Var(X) has a beautiful interpretation: it is exactly how much Y co-moves with X, scaled by how much X varies on its own. If X and Y move together a lot relative to X's variance, the slope is steep. If they barely co-move, the slope is flat.

The formula β̂₁ = Cov(X,Y)/Var(X) connects to your bivariate regression intuition in a concrete way. Consider estimating how years of schooling predict wages. You observe data on (schoolingᵢ, wageᵢ) for a sample. β̂₁ computes, for each observation, how far schooling is from its mean and how far wages are from their mean, then averages the product of those deviations — that's the covariance. Dividing by Var(X) scales the result so that β̂₁ has the right units: dollars per additional year of schooling. Once β̂₁ is pinned down, the **intercept** β̂₀ = Ȳ − β̂₁X̄ is determined automatically, since the regression line must pass through the sample means.

The **residual** for each observation, ûᵢ = Yᵢ − β̂₀ − β̂₁Xᵢ, is what the model doesn't explain. OLS minimizes Σûᵢ², which gives the estimators their name and their optimality property: under the Gauss-Markov assumptions (which you'll encounter when studying OLS assumptions formally), OLS is the Best Linear Unbiased Estimator. The **R²** = 1 − SSR/SST measures the fraction of variance in Y explained by X, ranging from 0 (no fit) to 1 (perfect fit). But R² is a goodness-of-fit measure, not a causal claim — a regression of height on shoe size has high R², but that doesn't mean shoe size causes height. Causality requires the exogeneity assumption E(u|X) = 0, which is an assumption about the data-generating process, not something you can read off R².

The practical power of OLS comes from its simplicity: two numbers (β̂₀ and β̂₁) summarize the average linear relationship between X and Y in your sample, and you can compute them from scratch with nothing more than means, variances, and a covariance. Every more complex method you'll encounter — multiple regression, instrumental variables, fixed effects — builds on this foundation by adjusting what variation in X is being used to estimate the slope. Understanding OLS deeply means understanding what goes wrong when its assumptions are violated, which makes it the essential starting point for all of causal econometrics.
