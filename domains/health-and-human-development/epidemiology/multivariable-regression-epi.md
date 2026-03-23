---
id: multivariable-regression-epi
title: Multivariable Regression in Epidemiology
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: stratification-and-adjustment
  type: hard
- id: biostatistics-in-public-health
  type: hard
builds-toward:
- cox-proportional-hazards
- meta-analysis-methods
tags:
- logistic-regression
- linear-regression
- adjustment
- multicollinearity
stage: expert
status: validated
---

# Multivariable Regression in Epidemiology

## Core Idea
Multivariable regression simultaneously models associations between an outcome and multiple exposures/confounders, providing adjusted effect estimates. Linear regression is used for continuous outcomes; logistic regression for binary outcomes; Cox regression for time-to-event. Regression assumes specific functional forms, handles interactions explicitly, and is flexible for many confounders, but requires careful model specification and diagnostics.

## Questions

```yaml
- question: "In a logistic regression of disease status (1 = case, 0 = control), the coefficient for a binary exposure variable is 0.69. After adjusting for confounders, what does this coefficient represent?"
  type: multiple-choice
  options: ["The adjusted risk difference for the exposure", "The adjusted log odds ratio for the exposure", "The probability of disease given the exposure", "The adjusted relative risk for the exposure"]
  answer: 1
  explanation: "Logistic regression models the log odds of the outcome. Coefficients are on the log-odds scale, so the coefficient of 0.69 is the natural log of the odds ratio. Exponentiating gives e^0.69 ≈ 2.0 — the adjusted odds ratio. Logistic regression does not directly yield risk differences or relative risks (though marginal methods can approximate them)."

- question: "Adding more covariates to a multivariable regression model always improves confounding control and should be done whenever additional variables are available."
  type: true-false
  answer: false
  explanation: "This is a common and consequential misconception. Including colliders (variables causally downstream of both exposure and outcome) opens backdoor paths and introduces bias. Adjusting for mediators blocks the causal pathway of interest, underestimating the total effect. Including many variables with sparse data causes overfitting and inflated standard errors. Model specification must be guided by a causal DAG or explicit epidemiologic reasoning, not by statistical availability."

- question: "What is the primary goal of multivariable regression in a causal epidemiologic study, as opposed to a predictive modeling context?"
  type: short-answer
  answer: "The goal is to obtain an adjusted, unconfounded estimate of the causal effect of a specific exposure on an outcome — not to maximize predictive accuracy or explain variance. The set of covariates to include is determined by the causal structure (e.g., via a DAG), not by model fit statistics."
  explanation: "Epidemiologic regression and predictive machine learning share tools but have different objectives. In causal epidemiology, including the wrong covariates (colliders, mediators) can bias the exposure coefficient even while improving model fit, so goodness-of-fit metrics are insufficient guides to covariate selection."
```

## Explainer

When you learned stratification and standardization, you saw how to control confounding by dividing your data into strata — comparing exposed and unexposed individuals who are similar on the confounder. The limitation is that stratification breaks down quickly when multiple confounders are present simultaneously. With 5 binary confounders, you have up to 32 strata; with continuous confounders, stratification becomes impossible. Multivariable regression solves this by modeling all confounders mathematically at once, producing a single adjusted estimate of the exposure-outcome association.

The choice of regression model depends on the outcome type. Linear regression is appropriate for continuous outcomes (e.g., blood pressure, BMI), where the coefficient on the exposure represents a mean difference. Logistic regression handles binary outcomes (case/control, disease/no disease), producing coefficients on the log-odds scale — exponentiate to get the odds ratio. Cox proportional hazards regression, which you will encounter in survival analysis, extends this to time-to-event outcomes where participants are followed until an event or censoring.

The fundamental logic of confounding adjustment via regression is that each coefficient represents the association between a variable and the outcome *holding all other variables in the model constant*. If age confounds the relationship between exercise and heart disease, including age in the model allows you to compare the exercise coefficient among people of the same age — the adjusted estimate. Crucially, what you adjust for matters enormously. The set of covariates to include should be determined by a causal diagram (DAG), not by statistical significance or convenience. Adjusting for a *collider* — a variable caused by both the exposure and the outcome — can introduce spurious associations where none exist. Adjusting for a *mediator* — a variable on the causal pathway from exposure to outcome — can block the very effect you are trying to measure.

Model diagnostics are not optional. For logistic regression, check for separation (a variable perfectly predicts the outcome in some stratum), sparse cells, and excessive collinearity among predictors (multicollinearity inflates standard errors). For any regression, examine residuals to assess whether the linearity assumption holds, and consider whether a log-transformed or nonlinear term better fits continuous exposures. The output of a regression is only as trustworthy as the model specification behind it.

Multivariable regression is powerful, but it is not a substitute for good study design. Regression can adjust for measured confounders, but unmeasured confounding remains a threat in observational epidemiology. When you encounter a well-adjusted regression analysis, ask: what important confounders might still be unmeasured? Is the model form plausible? Were any colliders or mediators inadvertently adjusted? These are the questions that distinguish competent epidemiologic analysis from mechanical number-crunching.
