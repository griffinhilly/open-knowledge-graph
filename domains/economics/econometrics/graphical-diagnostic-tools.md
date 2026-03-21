---
id: graphical-diagnostic-tools
title: 'Graphical Diagnostics: Residual Plots and QQ Plots'
domain: economics
course: econometrics
prerequisites:
- id: regression-diagnostics
  type: hard
- id: residuals-and-goodness-of-fit
  type: hard
tags:
- diagnostics
- residuals
- visualization
stage: formal-systems
status: draft
---

# Graphical Diagnostics: Residual Plots and QQ Plots

## Core Idea
Residual plots (vs. fitted values, scale-location) visually detect heteroskedasticity, nonlinearity, and outliers. QQ plots compare residuals to a normal distribution. These informal checks complement and motivate formal statistical tests.

## Questions

```yaml
- question: "A residuals vs. fitted values plot shows residuals scattered tightly near zero for small fitted values, but spreading widely for large fitted values in a fan shape. What does this pattern most likely indicate?"
  type: multiple-choice
  options:
    - "Nonlinearity — the model's functional form is incorrect and a quadratic term is needed"
    - "Heteroskedasticity — error variance increases with the level of fitted values"
    - "Autocorrelation — errors are correlated with prior residuals"
    - "Multicollinearity — two predictors are highly correlated with each other"
  answer: 1
  explanation: "A fan shape — narrow on the left, wide on the right — is the classic signature of heteroskedasticity, where error variance grows with the fitted value. Nonlinearity looks different: it appears as a U-shape or arch (systematic curvature), not a spreading fan. Autocorrelation produces wave-like patterns in residuals ordered by time, not a fan. Multicollinearity affects coefficient standard errors but doesn't produce a specific residual plot pattern."

- question: "A QQ plot of regression residuals shows points falling on the 45-degree line in the middle but curving strongly upward at the right tail and downward at the left tail, forming an S-curve. What does this indicate?"
  type: multiple-choice
  options:
    - "The residuals are approximately normally distributed"
    - "The residuals have heavy tails — extreme values are more frequent than a normal distribution predicts"
    - "The residuals are right-skewed, with more large positive values than expected"
    - "The model has a nonlinearity problem that should be addressed with a log transformation"
  answer: 1
  explanation: "An S-curve on a QQ plot — points above the line at the right tail and below at the left — indicates heavy tails (leptokurtosis). If residuals were normal, all points would track the 45-degree line. Right skew produces a different shape: points bow upward on the right only. Heavy tails matter because they affect the reliability of t-tests on individual coefficients, particularly in small samples."

- question: "A fan-shaped pattern in a residuals vs. fitted values plot suggests that the model's functional form is wrong and a quadratic term should be added."
  type: true-false
  answer: false
  explanation: "A fan shape indicates heteroskedasticity (non-constant error variance), not a functional form problem. The fix typically involves weighted least squares, robust standard errors, or a variance-stabilizing transformation. A U-shaped or curved pattern in the residuals indicates nonlinearity — that's when you consider adding polynomial terms or transforming variables. Confusing these two patterns leads to the wrong diagnosis and the wrong correction."

- question: "Graphical diagnostics like residual plots are valuable partly because they show where a model violation is concentrated, information that a single test statistic cannot convey."
  type: true-false
  answer: true
  explanation: "A Breusch-Pagan test or White test gives you a p-value: the violation is or isn't significant. A residual plot shows *which* fitted values are affected, whether the problem is smooth or driven by a few influential observations, and which variable might be driving it. This spatial information guides the correction — you can't tell from a p-value alone whether to use weighted least squares, transform a variable, or investigate outliers."

- question: "What distinguishes a residual plot showing heteroskedasticity from one showing nonlinearity, and why does the distinction matter for how you fix the model?"
  type: short-answer
  answer: "Heteroskedasticity appears as a fan shape — residuals spread out or contract systematically as fitted values increase, but with no systematic direction (positive or negative). Nonlinearity appears as a systematic curve — residuals trend positive then negative (or vice versa) across fitted values, indicating the model's mean function is misspecified. The fixes differ: heteroskedasticity calls for robust standard errors or weighted least squares; nonlinearity calls for adding nonlinear terms (quadratic, log) or transforming variables. Applying the nonlinearity fix to a heteroskedasticity problem leaves the variance problem unaddressed."
  explanation: "The diagnostic purpose of residual plots is to distinguish violations so you can apply the right correction. Confusing the fan pattern with the arch pattern is a common mistake. The scale-location plot (square root of absolute residuals vs. fitted values) is a cleaner tool for isolating heteroskedasticity, while the standard residuals vs. fitted plot is better for spotting nonlinearity as a curvature pattern."
```

## Explainer

From your work on regression diagnostics and residuals, you know that OLS residuals eᵢ = yᵢ − ŷᵢ capture what the model leaves unexplained. The formal OLS assumptions — linearity, homoskedasticity, normality, independence — are all claims about how those residuals should behave. Graphical diagnostic tools are the fastest way to check whether the residuals actually look the way the model says they should. The core idea is visual pattern recognition: if the model is correctly specified, residuals should look like white noise. Any pattern you see is evidence of a violation.

The **residuals vs. fitted values plot** is the most universally useful diagnostic. Plot each residual on the y-axis against its corresponding fitted value ŷᵢ on the x-axis. Under a correctly specified model with homoskedastic errors, you should see a horizontal cloud of points symmetrically scattered around zero — no curvature, no fanning, no outlier clusters. A U-shaped or arched pattern signals **nonlinearity**: the model's functional form is wrong, and a quadratic or log transformation of a variable may be needed. A fan shape — residuals spreading out as ŷ increases — is the hallmark of **heteroskedasticity**, where error variance grows with the fitted value. Both violations matter because they affect inference, not just fit.

The **scale-location plot** (also called the spread-location plot) is a refined version for detecting heteroskedasticity. It plots the square root of absolute residuals against fitted values. By taking the square root, you focus on the scale of errors rather than their sign; a flat smooth line through this plot confirms constant variance. The **QQ plot** (quantile-quantile plot) targets normality. It ranks your residuals and plots each residual's quantile against the theoretical quantile from a standard normal distribution. If residuals are normally distributed, the points fall on a 45-degree line. Heavy tails produce S-curves; right skew produces an upward bow on the right side. For large samples, minor departures are usually harmless due to the central limit theorem, but severe departures — especially from very small samples — matter for t-tests on individual coefficients.

These plots earn their place because they often reveal problems that formal tests miss or obscure. A White test or Breusch-Pagan test gives you a p-value; a residual plot shows you *where* the problem is concentrated, which variable drives it, and whether it is a smooth structural issue or a few influential observations. Think of the formal tests as confirmatory — you look at the plot first to understand the shape of the problem, then run the test to quantify it. Building the habit of plotting residuals before interpreting any regression is one of the highest-leverage practices in applied econometrics.
