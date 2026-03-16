---
id: standard-error-calculation
title: Standard Error Calculation and Correction Methods
domain: economics
course: econometrics
prerequisites:
- id: hypothesis-testing-regression
  type: hard
- id: ols-assumptions
  type: hard
builds-toward:
- robust-standard-errors
tags:
- standard-errors
- variance-estimation
- clustering
stage: formal-systems
status: draft
---

# Standard Error Calculation and Correction Methods

## Core Idea
Standard errors measure the precision of estimates. Conventional OLS standard errors assume homoskedasticity and no clustering. Robust standard errors (Huber-White), clustered standard errors, and two-way clustering adjust for violations of these assumptions.

## How It's Best Learned
Compare conventional, robust, and clustered standard errors in applied examples. Understand when each is appropriate based on data structure and likely violations of OLS assumptions.

## Explainer

A standard error answers this question: if you collected a new sample and refit the same regression, how much would the coefficient estimate move? A small standard error means the estimate is stable across samples — it is precisely estimated. A large standard error means the estimate is noisy. The OLS standard errors you first encountered are derived under a critical assumption from your work on OLS assumptions: **homoskedasticity** — that the variance of the error term is constant across all observations. When this assumption holds, the conventional formula for the variance of β̂ is σ²(X'X)⁻¹, where σ² is the common error variance estimated from residuals. This formula is clean and efficient, but it breaks down the moment error variance differs across observations.

**Robust standard errors** (also called Huber-White or heteroskedasticity-consistent standard errors) fix this. Instead of assuming a single σ², they let each observation contribute its own squared residual to the variance estimate: the sandwich estimator (X'X)⁻¹(X'Ω̂X)(X'X)⁻¹, where the middle matrix allows the residual variance to vary. The intuition is simple: observations with larger residuals are noisier and should contribute more uncertainty to the standard error. Robust SEs are almost always at least as large as conventional SEs — if the data actually are homoskedastic, robust and conventional SEs converge to the same value. This makes robust SEs a safe default: if in doubt, use them. They are the default in most modern applied work.

**Clustered standard errors** address a deeper problem: within-group correlation of errors. Suppose you are studying whether a job training program raises wages, using data on workers nested within firms. Workers in the same firm share management quality, culture, and shock exposures — their errors are not independent. Conventional or even robust SEs treat each observation as independent, which understates true uncertainty when many observations carry the same information. Clustered SEs allow arbitrary within-cluster correlation: all observations in the same cluster contribute only one "unit of information" for identifying within-cluster effects. The result is typically larger SEs and wider confidence intervals than robust SEs — sometimes dramatically so. The correct cluster level is not always obvious; it should match the level at which the key variation in your treatment variable occurs. In school-based studies, that is usually the school; in state-level policies, the state.

**Two-way clustering** extends this further when errors may be correlated along two dimensions simultaneously — for example, when analyzing panel data by both firm and year. If firm shocks persist over time and year shocks hit all firms, standard one-way clustering by firm understates the year-dimension correlation. Two-way clustered SEs account for both dimensions. The main practical lesson: the choice of standard error method is not a cosmetic adjustment — it can change t-statistics by factors of two or more, turning apparent significance into noise. Picking the wrong SE type is a validity problem, not just a technical one. Always ask: what is the error structure my data-generating process likely produced?
