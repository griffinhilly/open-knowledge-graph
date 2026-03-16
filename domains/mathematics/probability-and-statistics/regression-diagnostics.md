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

## Explainer

You've learned the OLS assumptions: linearity, independence, homoscedasticity (constant error variance), normally distributed errors, and no perfect multicollinearity. But fitting a regression model doesn't verify those assumptions — it merely produces estimates regardless of whether the assumptions hold. Regression diagnostics are the tools for checking whether your data actually satisfies what the model requires. The core insight is that the **residuals** (yᵢ − ŷᵢ) are observable proxies for the unobservable true errors εᵢ. If the model is correctly specified, residuals should look like a random, structureless cloud. Any pattern you find is evidence of a violated assumption.

The **residuals vs. fitted plot** is the first thing to examine. Plot the residuals on the y-axis against the fitted values ŷᵢ on the x-axis. Under correct specification, you should see a horizontal band centered at zero with uniform spread. Two warning signs: a curved or bent pattern (suggesting the linearity assumption is violated — your relationship is nonlinear and you need a transformed predictor or polynomial term) and a fan or funnel shape (suggesting heteroscedasticity — variance grows or shrinks with the fitted value). The **scale-location plot** reinforces the heteroscedasticity check by plotting √|standardized residuals| vs. fitted values; a horizontal trend line is what you want.

The **Q-Q (quantile-quantile) plot** tests normality of the residuals. The standardized residuals are ranked and plotted against the theoretical quantiles of a standard normal distribution. If the residuals are normally distributed, the points fall along the 45-degree reference line. Heavy tails show up as S-curves at the extremes; skewness appears as a systematic bow. Perfect normality is rarely achieved, and OLS inference is reasonably robust to mild departures, but severe non-normality — especially in small samples — undermines hypothesis tests and confidence intervals.

The **residuals vs. leverage plot** is conceptually different from the others. **Leverage** measures how far an observation's predictor values are from the center of the predictor space — a high-leverage point has unusual X values and can exert disproportionate influence on the fitted line. But high leverage alone is not a problem; it only becomes problematic when paired with a large residual. **Cook's distance** combines both into a single influence measure: it quantifies how much the estimated coefficients would change if the observation were deleted. Points appearing in the upper-right of the leverage plot (high leverage, high residual) are influential and deserve individual investigation — are they data entry errors, genuinely unusual cases, or observations from a different population? Each of these has a different remediation, so checking the data before automatically removing points is essential.
