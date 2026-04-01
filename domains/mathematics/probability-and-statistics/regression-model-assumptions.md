---
id: regression-model-assumptions
title: Assumptions in Linear Regression
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression
  type: hard
- id: multiple-regression-intro
  type: soft
builds-toward:
- regression-diagnostics
- inference-in-linear-regression
tags:
- regression
- assumptions
- diagnostics
stage: formal-systems
status: validated
---
# Assumptions in Linear Regression

## Core Idea
Standard linear regression assumes: linearity (relationship is linear), independence of observations, homoscedasticity (constant error variance), and normality of errors. Violations affect validity of inferential procedures. Residual plots help diagnose violations.

## How It's Best Learned
Create residual plots for various datasets and identify assumption violations. Compare behavior of regression under satisfied vs. violated assumptions. Use transformations to stabilize variance or linearize relationships.

## Common Misconceptions
Assuming regression works automatically without checking assumptions. Thinking normality is most important (independence violations are often more problematic). Fitting regression to inherently nonlinear relationships and ignoring residual patterns.

## Questions

```yaml
- question: "A researcher fits a linear regression and the residual-vs-fitted plot shows a clear U-shaped (curved) pattern. Which assumption is violated, and what is the primary consequence?"
  type: multiple-choice
  options:
    - "Homoscedasticity — standard errors are inflated but coefficient estimates remain unbiased."
    - "Normality — p-values are unreliable, especially for small samples."
    - "Linearity — the coefficient estimates themselves are biased because the model misrepresents the true relationship."
    - "Independence — standard errors are incorrect but the curvature pattern is unrelated to independence."
  answer: 2
  explanation: "A curved residual pattern is the signature of violated linearity: the model fits a straight line to a nonlinear relationship, so the slope coefficients are biased estimates of a nonlinear truth. This is the most fundamental violation — the estimates themselves are wrong, not just their standard errors. A fan shape indicates heteroscedasticity (option A); normality violations show up in a QQ-plot; independence violations leave no distinctive trace in a residual-vs-fitted plot."

- question: "A residual-vs-fitted plot shows residuals tightly clustered near fitted values of 10 but widely scattered near fitted values of 100. This pattern most likely indicates:"
  type: multiple-choice
  options:
    - "Autocorrelation — errors from nearby observations are correlated with each other."
    - "Non-linearity — the true relationship curves upward at higher predicted values."
    - "Heteroscedasticity — the variance of the errors grows with the fitted values."
    - "A normality violation — residuals at higher fitted values follow a non-normal distribution."
  answer: 2
  explanation: "A fan or funnel shape in the residual plot is the classic diagnostic for heteroscedasticity — the error variance is not constant but increases (or decreases) with the fitted values. This violates the homoscedasticity assumption. The consequence is incorrect standard errors (making significance tests and confidence intervals unreliable), though coefficient estimates remain unbiased. A log transformation of the outcome often stabilizes this pattern."

- question: "For large samples, the normality of errors assumption matters less because the Central Limit Theorem makes regression coefficient estimates approximately normal regardless of the error distribution."
  type: true-false
  answer: true
  explanation: "True. The normality assumption is needed for exact inference in small samples, but the CLT ensures that as sample size grows, the sampling distribution of the regression coefficients becomes approximately normal even when the errors themselves are not. Normality is therefore considered the mildest of the four LINE assumptions — large-sample inference is robust to departures from it."

- question: "If any regression assumption is violated, the regression model cannot be fitted and the software will refuse to compute coefficients."
  type: true-false
  answer: false
  explanation: "False — regression always produces coefficients by minimizing squared residuals, regardless of whether assumptions are satisfied. The mechanical fitting process is blind to violations. Assumptions govern the validity of inferential statements (p-values, confidence intervals, standard errors), not the ability to compute a line. A regression fit on non-linear data, correlated observations, or heteroscedastic errors will produce numbers — but the inferential interpretations of those numbers will be wrong."

- question: "Why is violation of the independence assumption often more damaging than violation of the normality assumption in linear regression?"
  type: short-answer
  answer: "Independence violations corrupt standard errors in hard-to-predict ways and are often invisible to standard diagnostic plots. When observations are correlated — in time-series data, clustered data (students within schools), or repeated measures — the effective sample size is smaller than the nominal n, and standard errors based on n independent observations understate true uncertainty, sometimes severely. Normality violations mainly affect small-sample inference and become negligible as n grows due to the CLT. Independence violations do not self-correct with larger samples."
  explanation: "The practical danger is that independence violations leave no trace in a residual-vs-fitted plot, which examines magnitudes, not the order or grouping of observations. You need specialized diagnostics: Durbin-Watson for autocorrelation, or knowledge of study design to identify clustering. Normality you can inspect in a QQ-plot and often ignore at large n; independence problems require structural fixes such as clustered standard errors or mixed models."
```

## Explainer

From your prerequisite on linear regression, you know how to fit a line by minimizing squared residuals and how to read off a coefficient like "for each additional year of education, income increases by $3,200." That fitting procedure always produces a line — it will always give you numbers. But the p-values, confidence intervals, and standard errors you compute alongside those coefficients rest on four assumptions that the data may or may not satisfy. Understanding assumptions is about knowing when those inferential statements are trustworthy, not about when regression "works" mechanically.

The four assumptions are often remembered by the acronym LINE. **Linearity** means the true relationship between the predictors and the outcome is additive and linear — if it curves, your coefficients are biased estimates of a nonlinear truth. **Independence** means each observation's error is unrelated to every other — this is violated in time-series data (where yesterday's error predicts today's), in clustered data (where students within the same school share unmeasured factors), and anywhere that repeated measurements come from the same unit. Independence violations are often the most damaging, yet they leave no trace in a standard residual plot. **Homoscedasticity** means error variance is constant across the range of fitted values — if higher predicted values also have larger residuals (a "fan" pattern), your standard errors are wrong in ways that can either inflate or deflate significance. **Normality of errors** is the mildest assumption: the Central Limit Theorem makes regression estimates approximately normal even when residuals are not, especially for large samples.

The primary diagnostic tool is the **residual plot** — a scatterplot of fitted values (x-axis) against residuals (y-axis). A well-satisfied model produces a cloud of points with no visible pattern: random scatter centered at zero, constant spread, no curves. Curved patterns indicate violated linearity; a fan or funnel shape indicates heteroscedasticity; systematic bands or waves often indicate autocorrelation. A QQ-plot of residuals against theoretical normal quantiles checks the normality assumption: points should fall on a straight diagonal line.

When you find violations, you have options rather than a dead end. A curved residual pattern often calls for a transformation of a predictor (log x, x²) or the outcome (log y for multiplicative relationships). Heteroscedasticity often responds to a log transformation of y, or to using robust standard errors that are valid without the constant-variance assumption. Autocorrelation requires modeling the error structure directly — Durbin-Watson tests detect it, and time-series methods correct for it. Independence violations from clustering are addressed by clustered standard errors or mixed models. The assumptions are not pass-or-fail gates; they are diagnostic signals that tell you what model refinements are needed.

A practical framing: think of the four assumptions as ordered by the severity of their violation. Nonlinearity produces biased coefficients — the fundamental estimates are wrong. Independence violations corrupt standard errors in hard-to-predict directions. Heteroscedasticity inflates or deflates standard errors but leaves coefficients unbiased. Normality violations matter primarily for small samples and are the first to forgive. Every regression analysis should at minimum produce a residual-vs-fitted plot and a QQ-plot before any inference is reported; skipping this step is not efficiency, it is silent model misspecification.
