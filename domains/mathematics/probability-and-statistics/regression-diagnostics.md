---
id: regression-diagnostics
title: Regression Diagnostics and Residual Analysis
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: regression-model-assumptions
  type: hard
builds-toward:
- inference-in-linear-regression
tags:
- regression
- diagnostics
- residuals
stage: formal-systems
status: draft
---

# Regression Diagnostics and Residual Analysis

## Core Idea
Residuals (yᵢ - ŷᵢ) show departures from the fitted model. Diagnostic plots include: residuals vs. fitted (linearity, homoscedasticity), Q-Q plots (normality), scale-location (variance), and residuals vs. leverage (influential points). Influential observations and outliers require investigation.

## Questions

```yaml
- question: "You fit a linear regression and examine the residuals vs. fitted plot. The residuals form a fan shape — small near low fitted values and large near high fitted values. What assumption is violated, and what is the appropriate response?"
  type: multiple-choice
  options:
    - "Linearity is violated; add a polynomial term to the model"
    - "Homoscedasticity is violated; use robust standard errors or transform the response"
    - "Independence is violated; use a time-series model"
    - "Normality is violated; use a non-parametric regression"
  answer: 1
  explanation: "A fan or funnel shape in the residuals vs. fitted plot is the signature of heteroscedasticity — the error variance grows with the fitted value rather than remaining constant. Remedies include robust standard errors, a variance-stabilizing transformation (e.g., log of the response), or weighted least squares. A curved pattern — not a fan — would indicate nonlinearity. Each plot pattern corresponds to a specific violated assumption."

- question: "An observation has predictor values far from the center of the data (high leverage) but a residual very close to zero. What is its likely effect on the regression?"
  type: multiple-choice
  options:
    - "It is highly influential and will distort the coefficient estimates"
    - "It will inflate standard errors for all coefficients"
    - "It will likely have minimal distorting influence despite its unusual predictor position"
    - "It should be removed because high-leverage points are always problematic"
  answer: 2
  explanation: "High leverage measures how unusual an observation's predictor values are — it captures potential for influence. But actual influence requires both high leverage AND a large residual. An observation that fits the model well (small residual) exerts little pull on the fitted line even from an extreme position. Cook's distance formalizes this: it combines leverage and residual size into a single influence measure. A high-leverage, low-residual point can actually stabilize the fit by confirming the trend at the extremes."

- question: "A Q-Q plot showing heavy-tailed deviations from the reference line indicates that OLS coefficient estimates are biased."
  type: true-false
  answer: false
  explanation: "Heavy tails in the residuals violate the normality assumption, but OLS estimates remain unbiased — they are unbiased under any error distribution as long as the Gauss-Markov conditions hold. What suffers is inference: t-statistics and F-statistics rely on normality, so p-values and confidence intervals become unreliable with severe non-normality, especially in small samples. OLS is robust to mild normality departures in large samples by the Central Limit Theorem."

- question: "A curved (bent) pattern in the residuals vs. fitted plot, rather than a random horizontal band, is evidence that the linearity assumption may be violated."
  type: true-false
  answer: true
  explanation: "The residuals vs. fitted plot should show a structureless horizontal band centered at zero if the model is correctly specified. A systematic curve indicates that the mean of the residuals is not zero across the range of fitted values — the linear model is systematically over- or under-predicting in different regions. This is the visual signature of a nonlinear true relationship. Adding a polynomial term or transforming a predictor are the typical remedies."

- question: "Why do regression diagnostics examine residuals (yᵢ − ŷᵢ) rather than the true errors εᵢ?"
  type: short-answer
  answer: "The true errors εᵢ = yᵢ − Xᵢβ are unobservable because β (the true population coefficients) is unknown. Residuals substitute the estimated β̂ for the unknown β, making the errors observable. If the model assumptions hold, residuals approximate the true errors and should exhibit no systematic patterns."
  explanation: "Residuals are imperfect proxies — they are not independent (they sum to zero by construction) and are slightly compressed toward zero by the estimation process. This is why diagnostics sometimes use standardized or studentized residuals, which correct for the fact that each residual has different variance depending on its leverage. Despite these imperfections, residual plots are remarkably informative because patterns in residuals reflect patterns in the true errors."
```

## Explainer

You've learned the OLS assumptions: linearity, independence, homoscedasticity (constant error variance), normally distributed errors, and no perfect multicollinearity. But fitting a regression model doesn't verify those assumptions — it merely produces estimates regardless of whether the assumptions hold. Regression diagnostics are the tools for checking whether your data actually satisfies what the model requires. The core insight is that the **residuals** (yᵢ − ŷᵢ) are observable proxies for the unobservable true errors εᵢ. If the model is correctly specified, residuals should look like a random, structureless cloud. Any pattern you find is evidence of a violated assumption.

The **residuals vs. fitted plot** is the first thing to examine. Plot the residuals on the y-axis against the fitted values ŷᵢ on the x-axis. Under correct specification, you should see a horizontal band centered at zero with uniform spread. Two warning signs: a curved or bent pattern (suggesting the linearity assumption is violated — your relationship is nonlinear and you need a transformed predictor or polynomial term) and a fan or funnel shape (suggesting heteroscedasticity — variance grows or shrinks with the fitted value). The **scale-location plot** reinforces the heteroscedasticity check by plotting √|standardized residuals| vs. fitted values; a horizontal trend line is what you want.

The **Q-Q (quantile-quantile) plot** tests normality of the residuals. The standardized residuals are ranked and plotted against the theoretical quantiles of a standard normal distribution. If the residuals are normally distributed, the points fall along the 45-degree reference line. Heavy tails show up as S-curves at the extremes; skewness appears as a systematic bow. Perfect normality is rarely achieved, and OLS inference is reasonably robust to mild departures, but severe non-normality — especially in small samples — undermines hypothesis tests and confidence intervals.

The **residuals vs. leverage plot** is conceptually different from the others. **Leverage** measures how far an observation's predictor values are from the center of the predictor space — a high-leverage point has unusual X values and can exert disproportionate influence on the fitted line. But high leverage alone is not a problem; it only becomes problematic when paired with a large residual. **Cook's distance** combines both into a single influence measure: it quantifies how much the estimated coefficients would change if the observation were deleted. Points appearing in the upper-right of the leverage plot (high leverage, high residual) are influential and deserve individual investigation — are they data entry errors, genuinely unusual cases, or observations from a different population? Each of these has a different remediation, so checking the data before automatically removing points is essential.
