---
id: linear-regression-social-science
title: Linear Regression for Social Science
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: matrix-operations
  type: hard
- id: partial-derivatives
  type: hard
- id: optimization-multivariable-basics
  type: hard
- id: matrices-intro
  type: soft
- id: vector-spaces
  type: soft
- id: linear-regression
  type: hard
builds-toward:
- multilevel-modeling-hierarchical
- logistic-regression-binary-outcomes
- structural-equation-modeling-latent
tags:
- regression
- correlation
- coefficients
- assumptions
stage: advanced
status: validated
---

# Linear Regression for Social Science

## Core Idea
Applies linear regression modeling to social science research questions, covering ordinary least squares estimation, interpretation of regression coefficients, model diagnostics, and addressing violations of assumptions. Emphasizes theoretical justification and causal thinking in observational research.

## How It's Best Learned
Estimate regressions on social science datasets, create visualizations of relationships, test assumption violations, practice interpreting coefficients for different outcome scales.

## Common Misconceptions
- Significant coefficients mean causal effects
- High R-squared means the model is good
- Controlling for everything improves inference

## Questions

```yaml
- question: "A regression model predicts income from years of education. The coefficient on education is 4,200, with p < 0.001. What can you correctly conclude?"
  type: multiple-choice
  options: ["Each additional year of education causes a $4,200 increase in income", "There is a statistically significant positive association between education and income in the sample", "Education accounts for 42% of the variation in income", "The model is well-specified because the coefficient is significant"]
  answer: 1
  explanation: "Statistical significance tells you the association is unlikely to be due to chance in the sample, not that education causes higher income. Causation requires ruling out confounders and ideally experimental or quasi-experimental designs. Options A, C, and D each reflect common over-interpretations of OLS output."

- question: "A regression model with R² = 0.85 is generally preferable to one with R² = 0.45 for making causal inferences in social science."
  type: true-false
  answer: false
  explanation: "R² measures how much variance the model explains, not whether the model is correctly specified or whether coefficients have causal interpretations. Adding irrelevant variables always increases R², and a model with many controls can have high R² while introducing collider bias or multicollinearity that undermines inference."

- question: "What is the difference between a confounder and a collider in regression, and why does controlling for a collider cause problems?"
  type: short-answer
  answer: "A confounder is a variable that causally affects both the treatment and the outcome; controlling for it removes spurious association. A collider is a variable that is caused by both the treatment and outcome; controlling for it opens a spurious path between them, inducing bias where none existed."
  explanation: "Blindly adding controls to 'improve' a regression ignores the causal structure. Controlling for a collider — a variable that is a common effect of the predictor and outcome — creates a spurious correlation between them. This is why causal diagrams (DAGs) are valuable before specifying a regression model."
```

## Explainer

When you apply linear regression to social science data, the mechanics are the same as in statistics or mathematics — fit a line through data by minimizing the sum of squared residuals (OLS). But social science adds a layer that statistics courses often skip: *what do the coefficients mean, and when can you call them causal?*

The OLS estimate of a coefficient represents the average change in the outcome associated with a one-unit increase in the predictor, *holding all other included variables constant*. That phrase "holding constant" is doing a lot of work. It does not mean the other variables are actually fixed in reality — it means you are comparing observations that differ only in the predictor of interest given the model's specification. If you have omitted a variable that is correlated with both the predictor and the outcome (a confounder), your estimates are biased.

This is why social scientists obsess over identification — the process of isolating causal effects from correlational noise. A significant p-value tells you the coefficient is probably nonzero in the population, but it says nothing about whether the relationship is causal. Two of the most common errors in reading regression output are (1) treating significant associations as causal effects, and (2) assuming that adding more controls always improves inference. The second is particularly dangerous: some variables, called colliders, are *caused by* both the treatment and the outcome. Controlling for a collider opens a spurious association that was not present before — adding it to the regression makes things worse.

The assumptions underlying OLS — linearity, homoskedasticity, no perfect multicollinearity, independence, and exogeneity — each have a diagnostic test and a remedy. Heteroskedasticity (non-constant variance) inflates or deflates standard errors; robust standard errors address this. Multicollinearity (highly correlated predictors) does not bias coefficients but inflates their standard errors, making estimates unstable. Endogeneity — when a predictor is correlated with the error term, often due to omitted variables — produces biased coefficients and is the hardest assumption to fix without an instrumental variable or natural experiment.

R² measures how much variance in the outcome the model explains, and high R² feels satisfying. But R² can be increased mechanically by adding variables, even irrelevant ones (adjusted R² penalizes for this). In causal social science, a model with R² = 0.15 but a clean identification strategy is far more credible than R² = 0.85 with ambiguous causal structure. Focus on whether the coefficient of interest has a defensible causal interpretation, not on whether the model explains lots of variance.
