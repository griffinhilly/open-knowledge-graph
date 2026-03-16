---
id: generalized-least-squares
title: Generalized Least Squares (GLS) for Non-Spherical Errors
domain: economics
course: econometrics
prerequisites:
- id: white-test-heteroskedasticity
  type: hard
- id: ols-assumptions
  type: hard
- id: linear-algebra
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- feasible-generalized-least-squares-fgls
tags:
- estimation
- heteroskedasticity
- gls
stage: formal-systems
status: draft
---

# Generalized Least Squares (GLS) for Non-Spherical Errors

## Core Idea
GLS transforms the regression by the inverse of the error variance-covariance matrix, restoring efficiency when errors are heteroskedastic or serially correlated. When the covariance structure is known, GLS recovers BLUE properties; when unknown and must be estimated from residuals, the procedure is feasible GLS (FGLS).

## Explainer

You know from the OLS assumptions that the Gauss-Markov theorem requires **spherical errors**: residuals that are homoskedastic (constant variance) and uncorrelated with each other. When these conditions fail — because errors are heteroskedastic or serially correlated — OLS is no longer the Best Linear Unbiased Estimator. It is still unbiased, but it is inefficient: some other linear estimator uses the data better. GLS is that better estimator.

The core idea is a transformation. Suppose the error variance-covariance matrix is Ω rather than σ²I. OLS minimizes the sum of squared residuals, treating each observation equally. But if some observations have much higher variance than others, they are noisier signals about the true relationship — they should count for less. GLS formalizes this: it pre-multiplies the regression equation by Ω^(-1/2) (the inverse of the Cholesky factor of Ω), which rescales observations by the inverse of their error standard deviation. Observations with high variance get down-weighted; observations with low variance get up-weighted. This transformation restores spherical errors in the new equation, so OLS applied to the transformed data is BLUE.

In matrix terms: the GLS estimator is β̂_GLS = (X'Ω⁻¹X)⁻¹X'Ω⁻¹y. Notice how this collapses to OLS when Ω = σ²I: you recover the standard formula (X'X)⁻¹X'y. The generalization is a **weighted least squares** procedure when Ω is diagonal (only variances differ across observations), or a correlated-errors transformation when Ω has off-diagonal terms (serial correlation). For the serial correlation case, the Prais-Winsten or Cochrane-Orcutt procedures implement GLS by first estimating the autocorrelation parameter ρ and then applying the transformation that removes it.

The practical complication is that Ω is almost never known in advance. You must estimate it from OLS residuals, giving **Feasible GLS** (FGLS). This two-step procedure is consistent but no longer exactly BLUE in finite samples — you've introduced estimation error from the first step. FGLS is often contrasted with the alternative of just using OLS with **robust standard errors** (Huber-White for heteroskedasticity, Newey-West for serial correlation): robust standard errors leave the point estimates alone but correct the inference, while FGLS changes both estimates and standard errors. For large samples the two approaches often give similar results, but FGLS can be more efficient; for small samples, robust standard errors are frequently preferred for their weaker assumptions.
