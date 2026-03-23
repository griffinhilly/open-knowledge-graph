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
stage: advanced
status: validated
---

# Simple Linear Regression Estimation

## Core Idea
OLS estimation for Y = β₀ + β₁X + u minimizes the sum of squared residuals to estimate coefficients. The estimators β̂₀ and β̂₁ are closed-form linear combinations of the data that produce the best linear prediction in the sense of minimizing squared errors.

## How It's Best Learned
Compute β̂₁ = Cov(X,Y)/Var(X) by hand using simple numeric examples. Then plot regression lines on scatter plots to visualize how OLS finds the line that minimizes residuals.

## Common Misconceptions
OLS does not assume Y is normally distributed—only errors need normality for inference. A high R² does not imply causality; causality requires exogeneity assumptions not testable from the regression alone.

## Questions

```yaml
- question: "A researcher runs OLS regression of annual income on years of education and obtains R² = 0.82. She concludes that education strongly causes higher income. What is the fundamental error in this reasoning?"
  type: multiple-choice
  options:
    - "R² above 0.8 is implausibly high, suggesting a coding error"
    - "OLS minimizes absolute errors, not squared errors, so R² measures the wrong criterion"
    - "R² measures goodness of fit — how well education predicts income in the sample — but causality requires E(u|X)=0, which cannot be established from the regression output alone"
    - "The intercept must be statistically significant for causal inference to be valid"
  answer: 2
  explanation: "R² tells you what share of Y's variance is explained by X in your sample — a prediction quality measure. Causality requires exogeneity: E(u|X) = 0, meaning no unobserved factors correlated with both education and income. This assumption is about the data-generating process, not the fit of the regression. People with more education may also differ in ability, family background, and networks (all in u) — so the slope may capture those effects, not the causal impact of education alone. High R² is perfectly compatible with severe omitted variable bias."

- question: "What is the correct interpretation of the OLS slope estimator β̂₁ = Cov(X,Y) / Var(X)?"
  type: multiple-choice
  options:
    - "The fraction of the variation in Y that is explained by X"
    - "The probability that a one-unit increase in X causes Y to increase"
    - "The average change in Y associated with a one-unit change in X, measuring how much Y co-moves with X scaled by X's own variability"
    - "The average value of X when Y equals zero"
  answer: 2
  explanation: "β̂₁ = Cov(X,Y)/Var(X) computes the joint variation between X and Y (Cov), then scales it by how much X varies on its own (Var(X)) to get a per-unit-of-X number. Concretely: if X is years of schooling and Y is wages, β̂₁ is the average dollar increase in wages for each additional year of schooling in the sample. Option A describes R², not the slope. Option B is a causal statement that requires additional assumptions. Option D describes the intercept β̂₀, not the slope."

- question: "OLS estimation of β̂₁ and β̂₀ requires that the residuals are normally distributed."
  type: true-false
  answer: false
  explanation: "Normal distribution of residuals (or equivalently, of the error term u) is required for the t-statistics and F-statistics used in inference (hypothesis testing and confidence intervals) to have their claimed distributions in small samples. But the OLS estimators β̂₁ = Cov(X,Y)/Var(X) and β̂₀ = Ȳ − β̂₁X̄ are just algebraic formulas — they can be computed and are unbiased under the Gauss-Markov assumptions without any normality requirement. Students often conflate the conditions needed for estimation with those needed for inference."

- question: "A high R² value in a regression of Y on X means that X explains a large share of the variation in Y, but does not by itself establish that X causes Y."
  type: true-false
  answer: true
  explanation: "R² is purely a goodness-of-fit measure: R² = 1 − SSR/SST = 1 − (unexplained variance)/(total variance). A regression of height on shoe size has high R² because they are strongly correlated, but shoe size does not cause height — both are driven by genetics and nutrition. Causality requires the exogeneity condition E(u|X) = 0, meaning X is uncorrelated with all other determinants of Y. No amount of predictive fit can substitute for this structural condition."

- question: "Why can a regression with high R² still fail to identify a causal effect of X on Y? What additional condition is required, and why is that condition not visible in the regression output?"
  type: short-answer
  answer: "High R² means X accounts for much of the variation in Y in the sample, but the variation being explained may come from confounders — variables correlated with both X and Y that are omitted from the regression and absorbed into the error term u. For X to have a causal interpretation, we need E(u|X) = 0 (exogeneity): no systematic relationship between X and the unobserved determinants of Y. This condition is not visible in the regression output because it is a claim about the data-generating process — the unmeasured variables — not about the data we observe. R² can be very high even when u and X are strongly correlated due to omitted variables."
  explanation: "The distinction between prediction and causation is the single most important conceptual gap in applied regression. R² measures fit; the exogeneity condition is what allows a slope coefficient to be interpreted as a causal effect. Every sophisticated regression strategy — instrumental variables, regression discontinuity, difference-in-differences — is essentially a way to create or exploit situations where exogeneity (or something close to it) plausibly holds."
```

## Explainer

From your work with least-squares regression fundamentals, you already know the core geometric idea: OLS finds the line through a scatter plot that minimizes the total squared vertical distance between each data point and the line. Simple linear regression makes this precise for the model Y = β₀ + β₁X + u. The **slope estimator** β̂₁ = Cov(X,Y)/Var(X) has a beautiful interpretation: it is exactly how much Y co-moves with X, scaled by how much X varies on its own. If X and Y move together a lot relative to X's variance, the slope is steep. If they barely co-move, the slope is flat.

The formula β̂₁ = Cov(X,Y)/Var(X) connects to your bivariate regression intuition in a concrete way. Consider estimating how years of schooling predict wages. You observe data on (schoolingᵢ, wageᵢ) for a sample. β̂₁ computes, for each observation, how far schooling is from its mean and how far wages are from their mean, then averages the product of those deviations — that's the covariance. Dividing by Var(X) scales the result so that β̂₁ has the right units: dollars per additional year of schooling. Once β̂₁ is pinned down, the **intercept** β̂₀ = Ȳ − β̂₁X̄ is determined automatically, since the regression line must pass through the sample means.

The **residual** for each observation, ûᵢ = Yᵢ − β̂₀ − β̂₁Xᵢ, is what the model doesn't explain. OLS minimizes Σûᵢ², which gives the estimators their name and their optimality property: under the Gauss-Markov assumptions (which you'll encounter when studying OLS assumptions formally), OLS is the Best Linear Unbiased Estimator. The **R²** = 1 − SSR/SST measures the fraction of variance in Y explained by X, ranging from 0 (no fit) to 1 (perfect fit). But R² is a goodness-of-fit measure, not a causal claim — a regression of height on shoe size has high R², but that doesn't mean shoe size causes height. Causality requires the exogeneity assumption E(u|X) = 0, which is an assumption about the data-generating process, not something you can read off R².

The practical power of OLS comes from its simplicity: two numbers (β̂₀ and β̂₁) summarize the average linear relationship between X and Y in your sample, and you can compute them from scratch with nothing more than means, variances, and a covariance. Every more complex method you'll encounter — multiple regression, instrumental variables, fixed effects — builds on this foundation by adjusting what variation in X is being used to estimate the slope. Understanding OLS deeply means understanding what goes wrong when its assumptions are violated, which makes it the essential starting point for all of causal econometrics.
