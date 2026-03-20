---
id: nonlinear-models-interpretation
title: Interpretation and Marginal Effects in Nonlinear Models
domain: economics
course: econometrics
prerequisites:
- id: logit-probit-models
  type: hard
- id: maximum-likelihood-econometrics
  type: hard
tags:
- nonlinear
- interpretation
- marginal-effects
stage: advanced
status: draft
---

# Interpretation and Marginal Effects in Nonlinear Models

## Core Idea
In logit, probit, and other nonlinear models, raw coefficients do not represent marginal effects on the outcome. The effect of a unit change in X depends on both the coefficient and the probability/density evaluated at specific covariate values.

## How It's Best Learned
Calculate marginal effects at the mean (MEM) and average marginal effects (AME) for a few key variables. Use plots to show how predicted probabilities change across the range of X.

## Explainer

In a linear regression model, the coefficient β on a variable X has a clean interpretation: a one-unit increase in X shifts the predicted outcome by exactly β, regardless of where X starts, who the observation is, or what other variables look like. This constant-effect property is what makes linear regression coefficients so easy to communicate. Nonlinear models like logit and probit, which you studied as prerequisites, trade away this simplicity in exchange for a more appropriate model of binary outcomes — and the price is that interpretation requires an extra step.

In a **logit model**, the coefficient β on X tells you how much the **log-odds** (the log of the probability of success divided by the probability of failure) changes for a one-unit increase in X. The log-odds scale is linear in the parameters, which is why maximum likelihood estimation works cleanly. But log-odds are not probabilities, and the translation from log-odds to probabilities is nonlinear — it runs through the logistic function, which produces the familiar S-shaped curve. This means the effect of X on the probability of success depends on where on the S-curve you are sitting. Near the tails (very high or very low predicted probabilities), the curve is nearly flat, so a coefficient of 0.5 on X translates into a very small probability change. Near the middle of the curve (baseline probability around 0.5), the same coefficient translates into a much larger probability change.

This is why raw logit or probit coefficients should never be directly interpreted as probability effects. Instead, economists compute **marginal effects** — the derivative of the predicted probability with respect to X, evaluated at specific covariate values. Two approaches are standard. **Marginal effects at the mean (MEM)** evaluate the derivative at the sample mean of each covariate: you plug in the average age, average income, average education level, and compute the probability change for a one-unit shift in X at that hypothetical "average" individual. **Average marginal effects (AME)** compute the derivative for every observation in the sample using their actual covariate values, then average those individual effects. AME is generally preferred because the "average individual" may not represent anyone in the data — averages of many characteristics may not correspond to any real person.

Consider a concrete example: estimating the effect of years of education on the probability of voting. A logit coefficient of 0.2 on education means log-odds increase by 0.2 per year of education. But for someone currently at a 20% baseline voting probability, this might translate into a 3 percentage-point increase per year of education. For someone at a 70% baseline probability, the same coefficient might translate into only 1.5 percentage points. The AME across the full sample might be 2.2 percentage points — that is the number you would report and discuss. **Discrete change effects** extend this logic to dummy variables: for a binary X (e.g., college degree vs. no degree), you compute the change in predicted probability when X switches from 0 to 1, rather than taking a derivative. The same nonlinearity applies, reinforcing that no single number captures the "effect" of a variable — context always determines magnitude.
