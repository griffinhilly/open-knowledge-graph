---
id: robust-standard-errors
title: Robust Standard Errors
domain: economics
course: econometrics
prerequisites:
- id: heteroskedasticity
  type: hard
- id: hypothesis-testing-regression
  type: hard
- id: multicollinearity
  type: soft
builds-toward:
- panel-data-basics
tags:
- robust-SE
- sandwich-estimator
- clustered-errors
- inference
stage: formal-systems
status: validated
---
# Robust Standard Errors

## Core Idea
Robust standard errors (Huber-White or 'sandwich' estimators) produce valid standard errors and confidence intervals in the presence of heteroskedasticity of unknown form, without requiring knowledge of the specific variance structure. Clustered standard errors extend this to settings where observations within groups (e.g., workers in the same firm, students in the same school) share common unobserved factors, inducing within-cluster correlation. Using clustered standard errors when observations are not truly independent is essential for valid inference in panel and grouped data. Modern applied econometrics routinely reports clustered standard errors as a default.

## Common Misconceptions
- Robust standard errors are never smaller than OLS standard errors on average; they can be larger or smaller in any given regression.
- Clustering at too fine a level (few clusters) produces unreliable estimates; the rule of thumb requires at least 30-50 clusters.

## Explainer

You already know that **heteroskedasticity** — non-constant variance of the error term — does not bias OLS coefficient estimates but does invalidate the standard formula for standard errors, making hypothesis tests and confidence intervals unreliable. The classical OLS standard error formula assumes the error variance is constant across all observations (Var(εᵢ) = σ² for all i). When this assumption fails, the formula produces the wrong answer, and the t-statistics you compute do not follow a t-distribution under the null — so your p-values are wrong.

The **Huber-White robust standard error** (also called the sandwich estimator) corrects this without requiring you to know the specific form of the heteroskedasticity. The name "sandwich" comes from the matrix formula: the robust variance estimator is (X'X)⁻¹ × [Σ εᵢ² xᵢxᵢ'] × (X'X)⁻¹ — the bread is (X'X)⁻¹ on both sides, and the meat in the middle is estimated directly from the squared residuals. Instead of assuming a constant σ², you let each observation's squared residual stand in for its own variance. The result is a consistent estimator of the true variance-covariance matrix of β̂ regardless of the heteroskedasticity pattern, as long as n is large.

**Clustered standard errors** extend this logic to a second kind of violation: within-group correlation. Suppose you are studying the effect of a policy on workers in the same firm, or students in the same school. Workers in the same firm share a common manager, culture, and economic environment — their errors are likely correlated, not independent. If you treat them as independent observations, you overstate how much information you actually have. The clustered sandwich estimator replaces individual squared residuals with the sum of residuals within each cluster, then sums across clusters. This produces standard errors that are valid when observations within clusters are correlated in any arbitrary way, as long as the clusters themselves are independent.

The choice of clustering level requires judgment. You should cluster at the level where assignment variation occurs — if a policy was assigned at the state level, cluster by state, not by individual. Clustering at too fine a level wastes the correction; clustering at too broad a level risks running out of clusters (the estimator requires many clusters, typically 30-50 minimum, to be reliable). With few clusters, alternative approaches like wild cluster bootstrap are more appropriate. In modern applied econometrics, reporting clustered standard errors is the default in virtually any setting with grouped or panel data — not doing so requires justification.

One subtlety: robust and clustered standard errors do not make your OLS estimates more efficient or less biased. They only correct the inference — the standard errors, confidence intervals, and p-values. If heteroskedasticity or clustering is severe, the OLS estimator may still be inefficient compared to alternatives like GLS or FGLS, which explicitly model the error structure. But in most applied settings, OLS with clustered standard errors is preferred for its robustness: it does not require correctly specifying the within-cluster correlation structure, whereas FGLS requires you to get that structure right or risk introducing bias.


