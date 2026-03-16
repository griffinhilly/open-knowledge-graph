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

## Explainer

From your work on regression diagnostics and residuals, you know that OLS residuals eᵢ = yᵢ − ŷᵢ capture what the model leaves unexplained. The formal OLS assumptions — linearity, homoskedasticity, normality, independence — are all claims about how those residuals should behave. Graphical diagnostic tools are the fastest way to check whether the residuals actually look the way the model says they should. The core idea is visual pattern recognition: if the model is correctly specified, residuals should look like white noise. Any pattern you see is evidence of a violation.

The **residuals vs. fitted values plot** is the most universally useful diagnostic. Plot each residual on the y-axis against its corresponding fitted value ŷᵢ on the x-axis. Under a correctly specified model with homoskedastic errors, you should see a horizontal cloud of points symmetrically scattered around zero — no curvature, no fanning, no outlier clusters. A U-shaped or arched pattern signals **nonlinearity**: the model's functional form is wrong, and a quadratic or log transformation of a variable may be needed. A fan shape — residuals spreading out as ŷ increases — is the hallmark of **heteroskedasticity**, where error variance grows with the fitted value. Both violations matter because they affect inference, not just fit.

The **scale-location plot** (also called the spread-location plot) is a refined version for detecting heteroskedasticity. It plots the square root of absolute residuals against fitted values. By taking the square root, you focus on the scale of errors rather than their sign; a flat smooth line through this plot confirms constant variance. The **QQ plot** (quantile-quantile plot) targets normality. It ranks your residuals and plots each residual's quantile against the theoretical quantile from a standard normal distribution. If residuals are normally distributed, the points fall on a 45-degree line. Heavy tails produce S-curves; right skew produces an upward bow on the right side. For large samples, minor departures are usually harmless due to the central limit theorem, but severe departures — especially from very small samples — matter for t-tests on individual coefficients.

These plots earn their place because they often reveal problems that formal tests miss or obscure. A White test or Breusch-Pagan test gives you a p-value; a residual plot shows you *where* the problem is concentrated, which variable drives it, and whether it is a smooth structural issue or a few influential observations. Think of the formal tests as confirmatory — you look at the plot first to understand the shape of the problem, then run the test to quantify it. Building the habit of plotting residuals before interpreting any regression is one of the highest-leverage practices in applied econometrics.
