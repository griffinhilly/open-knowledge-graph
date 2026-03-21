---
id: r-squared-goodness-of-fit
title: 'R-Squared: Goodness of Fit'
domain: economics
course: econometrics
prerequisites:
- id: simple-linear-regression-estimation
  type: hard
builds-toward:
- adjusted-r-squared-model-comparison
tags:
- model-fit
- goodness-of-fit
stage: advanced
status: draft
---

# R-Squared: Goodness of Fit

## Core Idea
R² = 1 - (RSS / TSS) measures the fraction of variation in Y explained by regressors, ranging from 0 to 1. Higher values indicate better fit, but R² cannot determine whether the model is causal or whether omitted variables bias estimates.

## Questions

```yaml
- question: "A researcher adds 15 additional control variables to a regression, and R² rises from 0.41 to 0.68. A colleague says this proves the new model is better. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — higher R² always indicates a better model, since more variation is explained"
    - "R² mechanically rises when variables are added, even irrelevant ones; in-sample fit improvement says nothing about out-of-sample prediction or causal validity"
    - "The colleague should have used adjusted R² only if the added variables were categorical"
    - "R² above 0.5 is a sign of overfitting, so the original model was preferable"
  answer: 1
  explanation: "OLS minimizes residuals for the sample in hand, so adding any variable — even pure noise — can never make R² decrease. The rise from 0.41 to 0.68 may partly reflect genuine explanatory power, but could also reflect overfitting. To evaluate whether the additions improve the model, you need adjusted R² (which penalizes for added parameters) or out-of-sample validation. R² alone cannot distinguish a better model from a more overfitted one."

- question: "A randomized controlled trial estimates the effect of a job training program on earnings with R² = 0.04. An observational study of the same program achieves R² = 0.71 by including many demographic controls. Which estimate is more causally trustworthy?"
  type: multiple-choice
  options:
    - "The observational study — its R² is far higher, meaning the model fits the data much better"
    - "The RCT — randomization eliminates confounding, making the treatment effect estimate unbiased regardless of R²"
    - "They are equivalent — both report regression estimates, so the causal validity is the same"
    - "The observational study — more controls always reduce omitted variable bias"
  answer: 1
  explanation: "R² measures how much variation in the outcome the model explains — a purely descriptive statistic. A low-R² RCT produces an unbiased estimate of the causal effect because randomization ensures treatment assignment is independent of all confounders, observed or not. The high-R² observational estimate may still be heavily biased if selection into the program is correlated with unobserved characteristics. Causal validity comes from the identification strategy, not from R²."

- question: "Adding a variable to an OLS regression model can never decrease R²."
  type: true-false
  answer: true
  explanation: "True. OLS finds the coefficients that minimize the residual sum of squares for the given sample. With an additional variable, the model has more flexibility — at worst, it sets the new coefficient to zero and achieves the same fit as before. It cannot do worse. This is why R² always weakly increases with more variables, making it an unreliable criterion for model selection (unlike adjusted R² or information criteria like AIC/BIC, which penalize for complexity)."

- question: "A regression model with R² = 0.90 produces coefficient estimates that are more likely to be unbiased than a model with R² = 0.30."
  type: true-false
  answer: false
  explanation: "False. R² is a measure of descriptive fit — how much of the outcome's variance is explained in-sample. Unbiasedness of coefficient estimates depends on whether the model's identification assumptions hold: no omitted variables correlated with regressors, no reverse causality, no measurement error. A model with R² = 0.90 can be severely confounded, producing biased estimates. A model with R² = 0.30 from a clean randomized experiment produces unbiased estimates. These two properties are independent."

- question: "Why is R² an inadequate criterion for evaluating the causal validity of a regression model, and what should researchers care about instead?"
  type: short-answer
  answer: "R² measures only how much of the in-sample variation in Y is explained by the regressors — a descriptive property. A model can have high R² while producing badly biased coefficient estimates if important confounders are omitted or if regressors are endogenous. Causal validity depends on the identification strategy: whether assignment to the key regressor is as good as random (RCT, instrumental variables, regression discontinuity, etc.). Econometricians prioritize consistency and unbiasedness of estimates over fit, because a precise answer to the wrong question is worse than a noisy answer to the right one."
  explanation: "This is why econometrics puts such emphasis on endogeneity, omitted variable bias, and instrumental variables — these are threats to causal identification that R² cannot detect. An R² near zero can be perfectly acceptable in a well-identified causal study; an R² near one in an observational study should raise suspicion that the model is either overfitted or confounded by variables correlated with both Y and the regressors."
```

## Explainer

From your study of simple linear regression, you know that OLS finds the line that minimizes the sum of squared residuals — the vertical distances between the data points and the fitted line. R² is built from two quantities derived from those residuals. **Total Sum of Squares (TSS)** is the total variation in Y around its mean: how spread out the outcome variable is before you add any predictors. **Residual Sum of Squares (RSS)** is the variation left over after fitting your model — the variation your regressors failed to explain. R² = 1 - (RSS/TSS) is then simply the fraction of total variation that the model accounts for.

The formula has a clean geometric interpretation. If your model explained nothing, RSS would equal TSS and R² = 0. If your model explained everything perfectly, RSS = 0 and R² = 1. In practice R² lives between these extremes, and interpreting it is context-dependent. A model explaining household income from age and education might achieve R² = 0.35 and be considered quite good, because income is driven by dozens of unobserved factors. A model predicting tomorrow's temperature from yesterday's temperature might achieve R² = 0.97. The benchmark is never "how close to 1?" but rather "how much variation was plausibly explainable by these specific predictors?"

The most important limitation of R² is that it rises mechanically whenever you add a variable — even a completely irrelevant one. Because OLS fits the sample data, adding noise variables never hurts in-sample fit. A model with 50 predictors will always have higher R² than a model with 5 predictors on the same data, even if 45 of those predictors are uncorrelated with Y in the population. This motivates the **adjusted R²**, which penalizes for the number of parameters, and cross-validation methods that assess out-of-sample fit.

The deeper limitation is that R² says nothing about causality. A model with R² = 0.95 might be severely confounded, with biased coefficient estimates, if key variables are omitted or endogenous. Conversely, a randomized experiment might produce a regression with R² = 0.02, but the estimate of the treatment effect is unbiased and causally interpretable. R² is a measure of descriptive fit, not of the quality of causal identification. This is why econometricians often care more about whether their estimates are consistent and unbiased than about whether R² is high.
