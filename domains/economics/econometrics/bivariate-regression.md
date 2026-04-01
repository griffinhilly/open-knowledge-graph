---
id: bivariate-regression
title: Simple (Bivariate) OLS Regression
domain: economics
course: econometrics
prerequisites:
- id: linear-regression
  type: hard
- id: correlation-coefficient
  type: hard
- id: residuals-and-goodness-of-fit
  type: hard
- id: variance-of-random-variables
  type: soft
- id: scatterplots-and-correlation
  type: soft
- id: econometrics-intro
  type: soft
- id: linear-transformations
  type: hard
- id: linear-systems-notation
  type: soft
builds-toward:
- ols-assumptions
- multiple-regression-model
- r-squared-and-model-fit
tags:
- OLS
- regression
- estimation
stage: formal-systems
status: validated
---
# Simple (Bivariate) OLS Regression

## Core Idea
Simple OLS regression fits the line ŷ = β₀ + β₁x that minimizes the sum of squared residuals between observed and predicted values of y. The slope estimator β̂₁ equals Cov(x,y)/Var(x), capturing how much y is predicted to change per unit increase in x. OLS is the default workhorse of empirical economics because it is computationally tractable and, under standard assumptions, produces unbiased and efficient estimates. The intercept β̂₀ gives the predicted value of y when x equals zero, though this is often not economically meaningful.

## How It's Best Learned
Derive the OLS formulas by hand from the minimization problem before using software. Then replicate published regressions in a dataset like wage-education data to see how coefficient interpretation works in context.

## Common Misconceptions
- The OLS line describes the conditional mean of y given x — it does not describe causation.
- A steep slope does not mean a strong fit; R² measures fit, not the magnitude of the slope.

## Questions

```yaml
- question: "The OLS slope estimator β̂₁ in a bivariate regression of y on x is equal to which of the following?"
  type: multiple-choice
  options: ["Var(x) / Cov(x, y)", "Cov(x, y) / Var(x)", "Cov(x, y) / Var(y)", "Corr(x, y) × Var(x)"]
  answer: 1
  explanation: "β̂₁ = Cov(x, y) / Var(x). This formula comes directly from minimizing the sum of squared residuals: take the derivative of Σ(yᵢ − β₀ − β₁xᵢ)² with respect to β₁, set it to zero, and solve. The result says the slope equals how much x and y move together (covariance) normalized by how much x varies on its own (variance). If you flip numerator and denominator you get the inverse — not a valid slope estimator."

- question: "A bivariate OLS regression with a large, statistically significant slope coefficient (β̂₁) necessarily implies that the model fits the data well."
  type: true-false
  answer: false
  explanation: "The slope coefficient and model fit (R²) measure different things. β̂₁ captures the estimated relationship between x and y; R² measures what fraction of the total variation in y is explained by x. A large slope can coexist with a very low R² if there is enormous scatter around the regression line — for example, a steep average relationship between education and wages that has very high individual variability. Conversely, a tiny slope can yield a high R² if the data are very tightly clustered around the line."

- question: "OLS estimates the line of best fit by minimizing a specific objective function. What does it minimize, and why is that criterion used rather than minimizing the sum of raw residuals?"
  type: short-answer
  answer: "OLS minimizes the sum of squared residuals, Σ(yᵢ − ŷᵢ)². The sum of raw residuals is not used because positive and negative errors cancel out — any line through the mean of the data has a zero sum of residuals, so this criterion cannot distinguish a good fit from a bad one. Squaring the residuals eliminates cancellation, penalizes large errors more heavily than small ones, and produces a unique, analytically solvable minimum."
  explanation: "The cancellation problem is the key insight. If you simply sum (yᵢ − ŷᵢ), a line that systematically over-predicts half the data and under-predicts the other half by equal amounts scores the same as a line with no error at all. Squaring forces all contributions to be non-negative, so the only way to drive the sum toward zero is to make every individual residual small. This also explains why OLS is sensitive to outliers — a single point far from the line contributes a very large squared residual that the estimator works hard to reduce."
```

## Explainer

Simple OLS regression answers a basic but important question: given data on two variables x and y, what is the best-fitting straight line through those points, and what does the slope of that line tell us? You have already worked with the correlation coefficient, which measures the strength and direction of a linear relationship. OLS regression goes further — it produces an actual line with a quantified slope that can be used to predict y from x and to estimate by how much y is expected to change for each unit increase in x.

The "best-fitting" line is defined precisely as the one that minimizes the **sum of squared residuals** — the sum of the squared vertical distances between each observed data point and the corresponding point on the line. This criterion is not arbitrary: summing raw (unsquared) residuals fails because positive and negative errors cancel, making it impossible to distinguish a good fit from a bad one. Squaring forces all residuals to contribute positively, and the unique line that minimizes this sum is the OLS line. Taking the derivative of the sum-of-squares expression with respect to the slope and intercept, setting both to zero, and solving yields closed-form formulas: β̂₁ = Cov(x, y) / Var(x) and β̂₀ = ȳ − β̂₁x̄. These are the OLS estimators.

The slope β̂₁ has a clean interpretation: it is the predicted change in y for a one-unit increase in x, holding everything else constant — though in a bivariate model there is no "everything else," so it simply captures the average linear relationship between the two variables. The intercept β̂₀ is the predicted value of y when x = 0, which is mathematically necessary but often economically meaningless (e.g., the predicted wage when education = 0 years). Notice that β̂₁ equals Cov(x,y)/Var(x): it is the covariance of x and y normalized by the variance of x. A larger covariance means a steeper slope; a larger variance in x (more spread in the predictor) means a flatter slope for the same covariance.

The most important limitation of OLS is that it estimates a conditional mean, not a causal effect. The regression line tells you that, on average in your data, a one-unit increase in x is associated with a β̂₁-unit change in y. It does not tell you that changing x causes y to change by that amount. If education and wages are positively correlated, OLS will give a positive slope — but that slope reflects the sum of every reason why educated people earn more, including unobserved factors like family background or ability that are correlated with both. Establishing causality requires additional assumptions or research designs (instrumental variables, natural experiments, randomized control) that you will study in later topics. For now, treat OLS as a tool for describing associations precisely — which is already enormously useful.
