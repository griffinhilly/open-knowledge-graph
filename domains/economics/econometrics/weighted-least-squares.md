---
id: weighted-least-squares
title: Weighted Least Squares (WLS)
domain: economics
course: econometrics
prerequisites:
- id: heteroskedasticity
  type: hard
- id: generalized-least-squares
  type: hard
tags:
- wls
- heteroskedasticity
- weights
stage: formal-systems
status: draft
---

# Weighted Least Squares (WLS)

## Core Idea
WLS applies inverse-variance weights to observations to correct for heteroskedasticity. High-variance observations receive lower weight, improving efficiency when the variance structure is known or can be estimated.

## How It's Best Learned
Estimate the variance function from residuals, then use predicted variances as weights in a second-stage regression. Compare WLS standard errors to OLS standard errors to verify the efficiency gain.

## Explainer

You already know that heteroskedasticity — non-constant error variance — doesn't bias OLS coefficient estimates, but it does make them inefficient and invalidates standard errors. Robust standard errors are one fix: they correct the standard errors without changing the point estimates. **Weighted Least Squares** (WLS) takes a more structural approach: it re-weights the data so that the effective error variance *becomes* constant, then runs OLS on the re-weighted problem.

The intuition is straightforward. Think of fitting a line through data where some observations are measured precisely (small variance) and others are measured noisily (large variance). OLS treats every data point equally, so a single noisy observation can pull the line substantially. That's wasteful — a data point with high variance contains less information about the true relationship and shouldn't count as much. WLS assigns each observation a weight equal to the inverse of its variance: w_i = 1/σ²_i. Observations with small variance (high precision) get large weights; observations with large variance get small weights. The result is **BLUE** — Best Linear Unbiased Estimator — under the correct variance specification, just as OLS is BLUE under homoskedasticity.

From your study of Generalized Least Squares (GLS), you know that WLS is a special case. GLS handles a general covariance structure Ω, transforming the model by Ω^{-1/2} to produce a homoskedastic, uncorrelated error. WLS is GLS restricted to the diagonal case where errors are uncorrelated but have different variances. The transformation is simply dividing each observation by its standard deviation σ_i — equivalently, multiplying by the square root of the weight. After this transformation, the rescaled errors have equal variance, and ordinary OLS applied to the transformed data is efficient.

The practical challenge is that the true σ²_i values are never observed. In **feasible WLS**, you estimate them from the data. One common approach: run OLS first, take the squared residuals as noisy proxies for σ²_i, then regress log(ê²_i) on functions of the regressors to get a smooth variance function. The fitted values from this auxiliary regression provide estimated weights for the second-stage WLS. The two-stage procedure introduces uncertainty into the weights themselves, which can affect standard errors in finite samples. This is why comparing WLS and OLS standard errors — and checking whether the residuals from the WLS regression look more homoskedastic — is important before trusting the efficiency gain.
