---
id: r-squared-and-model-fit
title: R-Squared and Model Fit
domain: economics
course: econometrics
prerequisites:
- id: bivariate-regression
  type: hard
- id: residuals-and-goodness-of-fit
  type: hard
- id: f-test-joint-significance
  type: soft
- id: correlation-coefficient
  type: soft
builds-toward:
- omitted-variable-bias
- multicollinearity
tags:
- R-squared
- goodness-of-fit
- adjusted-R-squared
- model-selection
stage: formal-systems
status: validated
---

# R-Squared and Model Fit

## Core Idea
R² measures the fraction of variation in y explained by the regressors: R² = 1 − SSR/SST, where SSR is the sum of squared residuals and SST is total variance. It always lies between 0 and 1, and adding any regressor — even irrelevant — cannot decrease it. The adjusted R² penalizes for additional regressors, making it more appropriate for model comparison: R̄² = 1 − [SSR/(n−k−1)]/[SST/(n−1)]. High R² does not imply unbiased coefficient estimates; low R² does not imply the estimates are wrong or the model is useless for causal inference.

## How It's Best Learned
Compare R² and adjusted R² across nested models (same data, different regressors). Note that adding noise variables can raise R² but lower R̄².

## Common Misconceptions
- A low R² (e.g., 0.05) does not invalidate a regression — causal identification is about E[u|x]=0, not explained variance.
- R² is not comparable across datasets or when the dependent variable is transformed (e.g., log y vs y).

## Questions

```yaml
- question: "A researcher adds three variables to a regression and reports that R² increased from 0.45 to 0.52. A colleague concludes the model is now substantially better. What is wrong with this interpretation?"
  type: multiple-choice
  options:
    - "R² should have decreased when variables are added"
    - "R² mechanically cannot decrease when variables are added, so the increase tells us nothing about whether the new variables are informative — adjusted R² is needed"
    - "An increase of 0.07 in R² is always too small to be meaningful"
    - "R² only measures fit for the training data, so this comparison is invalid"
  answer: 1
  explanation: "R² can only stay flat or rise when variables are added, because OLS can always set a new coefficient to zero if the variable contributes nothing. An increase in R² therefore proves nothing about the variables' usefulness. Adjusted R² penalizes for the additional degrees of freedom used; if adjusted R² falls, the new variables are hurting the model by overfitting rather than genuinely improving it."

- question: "A randomized experiment finds that a job training program increases wages by $200/week (p < 0.001), but R² = 0.03. A critic argues: 'The model explains almost nothing — this result can't be trusted.' What is the correct response?"
  type: multiple-choice
  options:
    - "The critic is right — a low R² indicates the estimate is biased"
    - "The critic is wrong — R² measures explained variance, not causal validity; wages vary for many reasons beyond the program, and the coefficient can be unbiased even if R² is low"
    - "The critic is right — a larger sample would raise R² and validate the result"
    - "The critic is wrong, but R² should be at least 0.10 to report results in economics"
  answer: 1
  explanation: "This is the deepest misconception about R². The key OLS assumption for unbiased estimation is E[u|x] = 0, not high R². In a randomized experiment, random assignment ensures the treatment indicator is uncorrelated with the error term — satisfying the identification condition regardless of how much unexplained variation remains. Wages vary enormously for reasons unrelated to the program (education, industry, experience), producing a low R² that is completely consistent with a valid, precisely estimated causal effect."

- question: "Adding any regressor to a regression, even an irrelevant one, can never decrease R²."
  type: true-false
  answer: true
  explanation: "This is a mechanical fact about OLS. The algorithm minimizes the sum of squared residuals, and it can always set the new variable's coefficient to zero if the variable adds nothing — in which case R² stays flat. If the variable has any relationship with y, even due to random chance in the sample, the coefficient will be nonzero and R² will rise. This is why raw R² is a misleading model comparison tool when models have different numbers of regressors."

- question: "A regression with R² = 0.92 provides stronger evidence for a valid causal estimate than one with R² = 0.08, all else equal."
  type: true-false
  answer: false
  explanation: "R² and causal validity are entirely separate. A high R² means the regressors explain most of the variation in y — but if those regressors are correlated with the error term (omitted variable bias, endogeneity), the coefficients are biased regardless of R². A low R² from a clean randomized experiment delivers perfectly unbiased estimates. The relevant criterion for causal identification is E[u|x] = 0, not the fraction of variance explained."

- question: "Why do econometricians pursuing causal identification often report low R² without apology, and what would actually need to be true for their coefficient estimates to be valid?"
  type: short-answer
  answer: "For causal identification, what matters is that the identifying assumption holds — most commonly E[u|x] = 0, meaning the regressor of interest is uncorrelated with the error term (no omitted variable bias, no reverse causation). This assumption is satisfied by good research design: randomization, instrumental variables, regression discontinuity, or difference-in-differences. R² measures how much variation the model explains, which is a separate question from whether the coefficient is unbiased. Low R² just means many other factors influence y — it does not compromise identification."
  explanation: "This distinction is fundamental to modern econometrics. The field moved away from treating high R² as a goal (which leads to overfitted kitchen-sink regressions) toward treating credible identification as the primary criterion. A study with R² = 0.04 from a clean natural experiment is far more informative about a causal question than one with R² = 0.85 from a poorly specified observational regression."
```

## Explainer

From bivariate regression, you learned how to fit a line through data by minimizing squared residuals — the vertical distances between data points and the fitted line. Those residuals capture what the model fails to explain. **R²** formalizes this intuition into a single summary statistic: the fraction of the total variation in y that your regression accounts for.

The formula makes the decomposition explicit. **Total sum of squares** (SST) = Σ(yᵢ − ȳ)² measures the total variation in the outcome around its unconditional mean. **Residual sum of squares** (SSR) = Σ(yᵢ − ŷᵢ)² is the unexplained variation that remains after fitting the model. R² = 1 − SSR/SST. When the model perfectly fits every data point, SSR = 0 and R² = 1. When the model simply predicts the mean for every observation (no regressors at all), SSR = SST and R² = 0. An R² of 0.60 means the regressors collectively account for 60% of the variation in y; the remaining 40% is unexplained.

A crucial mechanical fact: **adding any variable to a regression can never decrease R²**. OLS can always set a new coefficient to zero if the variable adds nothing, so SSR can only stay flat or fall, meaning R² can only stay flat or rise. This is why comparing R² across models with different numbers of predictors is misleading — you could achieve R² = 0.99 by including enough noise variables. **Adjusted R²** corrects for this by penalizing the loss of degrees of freedom: R̄² = 1 − [SSR/(n−k−1)] / [SST/(n−1)], where k is the number of regressors. The adjustment means adding a truly uninformative variable can lower R̄², making it a better model comparison tool than raw R².

The deepest point — and the most consequential misconception — is that R² has nothing to do with whether your regression is correctly specified for causal inference. The key OLS assumption for unbiased estimation is E[u|x] = 0: the regressors are uncorrelated with the error term. R² measures explained variance regardless of whether this assumption holds. You can have R² = 0.95 with severe omitted variable bias, and R² = 0.04 with a clean randomized experiment delivering perfectly unbiased coefficients. As you move further into econometrics, you will regularly see researchers report very low R² without apology — they are pursuing credible identification of a causal effect, not maximizing explained variance. The two goals are genuinely separate.
