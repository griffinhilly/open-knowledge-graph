---
id: count-data-regression-models
title: 'Count Data Regression: Poisson and Negative Binomial Models'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: logistic-regression-binary-categorical
  type: hard
- id: poisson-distribution
  type: hard
- id: probability-distributions
  type: hard
- id: probability-mass-functions
  type: soft
tags:
- count-data
- poisson
- negative-binomial
- overdispersion
stage: advanced
status: draft
---

# Count Data Regression: Poisson and Negative Binomial Models

## Core Idea
Count outcomes like protest events or arrests are often overdispersed—more variable than Poisson assumes. Negative binomial regression accommodates overdispersion. Zero-inflated models address excess zeros. Proper model selection improves inference and prevents bias.

## Explainer

You already know that ordinary linear regression assumes a continuous, normally distributed outcome. But many social science outcomes are **counts** — the number of protests in a country in a year, arrests per month, bills introduced in a legislative session, or war casualties in a conflict. Counts are non-negative integers, and their distribution tends to be highly skewed: many observations near zero, a long tail of large values. Fitting OLS to count data can produce nonsensical predictions (negative counts, fractional events) and incorrect standard errors. The solution is a family of regression models built specifically for count data.

The starting point is **Poisson regression**. The Poisson distribution — which you've studied — has one defining property: its mean equals its variance. Poisson regression models the log of the expected count as a linear function of predictors, which guarantees non-negative predictions and has a natural interpretation: coefficients are log-incident rate ratios, and exponentiated coefficients are multiplicative effects on the expected count. If a coefficient is 0.5, e^0.5 ≈ 1.65, meaning a one-unit increase in that predictor multiplies the expected count by 1.65.

The critical limitation of Poisson is its mean-equals-variance constraint. Real count data is almost always **overdispersed** — the variance exceeds the mean, often dramatically. This happens when outcomes are clustered (protests cluster in time and space), when unobserved heterogeneity exists across units, or when events follow a contagion process. If you force Poisson on overdispersed data, the model is misspecified: standard errors are underestimated, test statistics are inflated, and you will declare spurious significance. **Negative binomial regression** relaxes the constraint by adding a dispersion parameter that captures extra-Poisson variation. Think of it as a Poisson model where each observation has its own underlying rate drawn from a gamma distribution — the resulting mixture is the negative binomial. In practice, negative binomial fits are nearly always preferred when overdispersion tests flag a problem.

A further complication is **excess zeros** — outcomes where the count is zero far more often than Poisson or negative binomial predicts. This arises when two distinct processes generate the data: one process determines whether any events occur at all (a logistic-type "always-zero" mechanism), and a second process governs how many occur when they do (a count mechanism). **Zero-inflated Poisson** and **zero-inflated negative binomial** models estimate both processes simultaneously. Model selection between these options typically uses the Vuong test, AIC/BIC comparison, and rootograms (graphical comparison of observed vs. predicted count frequencies) to diagnose where the plain Poisson fails.
