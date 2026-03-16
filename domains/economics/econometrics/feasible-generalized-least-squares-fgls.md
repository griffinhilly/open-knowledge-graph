---
id: feasible-generalized-least-squares-fgls
title: Feasible GLS (FGLS) with Estimated Covariance Structure
domain: economics
course: econometrics
prerequisites:
- id: generalized-least-squares
  type: hard
builds-toward:
- dynamic-panel-gmm
tags:
- estimation
- heteroskedasticity
- fgls
stage: formal-systems
status: draft
---

# Feasible GLS (FGLS) with Estimated Covariance Structure

## Core Idea
FGLS estimates the error covariance matrix from residuals, then applies GLS using the estimated structure. While more practical than GLS (which requires knowing covariance a priori), FGLS is sensitive to misspecification of the covariance form and sacrifices some efficiency through the two-step estimation.

## Explainer

From your study of GLS, you know the fundamental problem it solves: when errors have non-constant variance (heteroskedasticity) or are correlated across observations, OLS is still unbiased but no longer efficient, and standard errors are wrong. GLS corrects this by pre-multiplying the model by the inverse square root of the error covariance matrix Ω, transforming the data into a form where OLS is once again the best linear unbiased estimator. The catch is that GLS requires knowing Ω — the exact structure of the errors — which in practice you almost never do. **FGLS** (Feasible GLS) resolves this by estimating Ω from the data itself, then using that estimate in place of the true covariance structure.

The mechanics are a two-step procedure. In **Step 1**, you run OLS and collect the residuals. You then use those residuals to estimate the covariance structure — the specific approach depends on what form of misspecification you suspect. For heteroskedasticity, you might regress squared residuals on the regressors or their functions to estimate how variance scales with covariates. For serial correlation, you might estimate an AR(1) process from the residuals to get ρ, the autocorrelation coefficient. This gives you Ω̂, your estimate of the covariance matrix. In **Step 2**, you apply GLS using Ω̂ in place of Ω: transform the data by pre-multiplying by Ω̂^(-1/2) and run OLS on the transformed model. The resulting estimator is FGLS.

The key tradeoff relative to true GLS is that FGLS is no longer exactly optimal in finite samples, because Ω̂ is itself estimated with error. This introduces a form of generated-regressor bias that shrinks as sample size grows. In large samples, FGLS is asymptotically equivalent to GLS — both achieve the same efficiency gains over OLS. In small samples, however, the two-step estimation can introduce substantial noise, and FGLS may actually perform worse than plain OLS if the covariance model is poorly estimated. The practical rule: FGLS pays off most when (a) the sample is large enough for the first-stage covariance estimation to be precise, and (b) the misspecification (heteroskedasticity or autocorrelation) is severe enough to make the efficiency gain worth the additional complexity.

The deeper sensitivity is **misspecification of the covariance form**. If you assume heteroskedasticity follows a particular parametric pattern but the true pattern differs, your Ω̂ is wrong in a systematic way, and FGLS can perform badly — potentially worse than either OLS or the correct GLS. This is why practitioners often prefer **heteroskedasticity-robust standard errors** (which leave OLS point estimates unchanged but correct the inference) over FGLS for heteroskedasticity problems: they require no assumption about the form of heteroskedasticity. FGLS is most natural when the covariance structure is well-motivated theoretically — for example, in **feasible WLS** (weighted least squares), where you have strong prior reason to believe variance is proportional to a particular variable, or in panel data settings with known autocorrelation structures. Knowing when to use FGLS versus robust standard errors versus a fully specified panel estimator is the judgment call that separates mechanical application from genuine econometric skill.
