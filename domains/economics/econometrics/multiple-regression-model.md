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
- id: matrix-inverses
  type: soft
- id: linear-regression
  type: soft
- id: linear-transformations
  type: hard
- id: expected-value-theory
  type: hard
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
status: validated
---

# Multiple Regression

## Core Idea
Multiple regression extends OLS to include several explanatory variables: y = β₀ + β₁x₁ + β₂x₂ + … + βₖxₖ + u. Each coefficient βⱼ represents the partial effect of xⱼ on y holding all other regressors constant — this 'ceteris paribus' interpretation is the central analytical payoff. In matrix form, the estimator is β̂ = (X'X)⁻¹X'y, which requires (X'X) to be invertible (no perfect multicollinearity). Adding control variables changes coefficient estimates if and only if those controls are correlated with both the dependent variable and the included regressors.

## How It's Best Learned
Compare simple and multiple regression estimates on the same dataset — seeing how the wage coefficient on education changes when experience is added illustrates what 'holding constant' means in practice.

## Common Misconceptions
- More control variables do not always improve estimation — including irrelevant variables reduces efficiency and including endogenous controls can introduce new bias.
- The coefficient on x₁ does not represent the effect of x₁ alone; it is always conditional on the other included variables.

## Questions

```yaml
- question: "A researcher estimates the effect of education on wages with a bivariate regression and gets β̂₁ = 0.12. She then adds years of experience as a control and gets β̂₁ = 0.09. Which interpretation is correct?"
  type: multiple-choice
  options: ["The bivariate estimate is wrong; 0.09 is the true effect of education.", "The multiple regression estimate represents the effect of education holding experience constant, while the bivariate estimate does not.", "Adding experience variables always reduces coefficients, so this is expected and uninformative.", "The two estimates cannot be compared because they are from different models."]
  answer: 1
  explanation: "The coefficient on education in the multiple regression is the partial effect — how wages change with one more year of education when experience is held fixed. The bivariate estimate conflates the direct effect of education with any correlation between education and experience. Neither is unconditionally 'wrong'; they answer different questions."

- question: "Adding more control variables to a multiple regression model typically improves the accuracy of coefficient estimates."
  type: true-false
  answer: false
  explanation: "This is the most important misconception about multiple regression. Including irrelevant variables reduces efficiency (increases standard errors) without reducing bias. Worse, including endogenous controls — variables that are themselves caused by the regressors or the outcome — can introduce new bias and make estimates less reliable. More controls is not a free lunch."

- question: "What condition is required for the matrix estimator β̂ = (X'X)⁻¹X'y to exist, and what economic situation would violate it?"
  type: short-answer
  answer: "The matrix (X'X) must be invertible, which requires no perfect multicollinearity — no regressor can be an exact linear combination of others. This is violated if, for example, you include both 'income in dollars' and 'income in thousands of dollars' as separate regressors, since one is exactly 1000 times the other."
  explanation: "Perfect multicollinearity makes the normal equations singular: the system has infinitely many solutions because the collinear variables cannot be separately identified. Near-perfect multicollinearity (high but not exact correlation) is the more common practical problem — it does not prevent estimation but inflates standard errors severely."
```

## Explainer

You already know bivariate regression: a single explanatory variable x₁ predicts y via ŷ = β̂₀ + β̂₁x₁, with OLS minimizing the sum of squared residuals. Multiple regression extends this to k explanatory variables — y = β₀ + β₁x₁ + β₂x₂ + … + βₖxₖ + u — and the conceptual payoff is enormous. Including additional regressors allows each coefficient to represent a partial effect: β₁ is the estimated change in y for a one-unit increase in x₁ *holding all other regressors constant*. This "ceteris paribus" interpretation is what lets economists isolate the effect of one variable from the confounding influence of others.

The wage-education example makes the logic concrete. A bivariate regression of wages on education gives a coefficient that captures not just education's direct effect but also any correlation between education and other determinants of wages (like experience or family background). When you add experience to the model, the education coefficient changes — and that change is informative. It tells you that part of the original estimate was actually attributable to the correlation between education and experience. The new coefficient is the effect of education among workers with the same years of experience.

In matrix notation, the OLS estimator is β̂ = (X'X)⁻¹X'y, where X is the n × (k+1) matrix of regressors including the constant column, and y is the n × 1 outcome vector. This formula generalizes the bivariate formula and makes the required conditions explicit: (X'X) must be invertible, which fails under perfect multicollinearity. You have seen matrix inverses in your prerequisites; here the condition det(X'X) ≠ 0 is the non-redundancy requirement — no regressor can be an exact linear combination of the others.

The "more controls is always better" intuition is wrong and important to resist. Adding a variable changes coefficient estimates only if it is correlated with both the outcome and the included regressors. Adding a truly irrelevant variable leaves coefficients unchanged in expectation but inflates their standard errors, reducing your ability to detect real effects. Adding an endogenous variable — one caused by your regressor — can introduce bias that wasn't there before, a phenomenon you'll study deeply when you reach omitted variable bias and simultaneity.

Multiple regression is the workhorse of empirical economics. From here, you'll study how to test whether a group of coefficients is jointly significant (F-tests), what happens when you omit a relevant variable, and how to handle categorical variables with dummies. Every one of those topics is an extension of the partial-effect logic you are building here.
