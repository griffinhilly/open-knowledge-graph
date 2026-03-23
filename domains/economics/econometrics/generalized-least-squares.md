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
status: validated
---

# Generalized Least Squares (GLS) for Non-Spherical Errors

## Core Idea
GLS transforms the regression by the inverse of the error variance-covariance matrix, restoring efficiency when errors are heteroskedastic or serially correlated. When the covariance structure is known, GLS recovers BLUE properties; when unknown and must be estimated from residuals, the procedure is feasible GLS (FGLS).

## Questions

```yaml
- question: "A researcher runs OLS on panel data where urban observations have much higher error variance than rural ones. The OLS estimates are unbiased. Why might she prefer GLS?"
  type: multiple-choice
  options:
    - "OLS estimates are biased under heteroskedasticity, so GLS corrects this bias"
    - "OLS is unbiased but inefficient — it weights all observations equally, while GLS down-weights noisy observations to achieve lower variance"
    - "GLS guarantees unbiasedness in cases where OLS does not"
    - "OLS cannot be computed when error variances differ across observations"
  answer: 1
  explanation: "This is the key: OLS remains unbiased under heteroskedasticity — the bias critique is wrong. The problem is inefficiency. OLS treats every observation as equally informative when computing the estimator, but observations with high error variance are noisy signals about the true relationship and should count for less. GLS formalizes this by down-weighting high-variance observations (pre-multiplying by Ω^{-1/2}), which restores spherical errors in the transformed regression and makes OLS on the transformed data BLUE — the Best Linear Unbiased Estimator."

- question: "What happens to the GLS estimator formula β̂_GLS = (X'Ω⁻¹X)⁻¹X'Ω⁻¹y when the error covariance matrix is Ω = σ²I?"
  type: multiple-choice
  options:
    - "GLS becomes infeasible because σ²I is not invertible"
    - "GLS reduces to the standard OLS estimator (X'X)⁻¹X'y"
    - "GLS produces different, more efficient estimates than OLS even under spherical errors"
    - "GLS is only defined for non-spherical errors and cannot handle the Ω = σ²I case"
  answer: 1
  explanation: "Substituting Ω = σ²I into the GLS formula: (X'(σ²I)⁻¹X)⁻¹X'(σ²I)⁻¹y = (X'(1/σ²)X)⁻¹X'(1/σ²)y = σ²(X'X)⁻¹(1/σ²)X'y = (X'X)⁻¹X'y. The σ² cancels, and you recover standard OLS. This is the elegant consistency of GLS: it is a generalization of OLS that reduces to OLS when the errors are already spherical. When errors are not spherical, GLS 'transforms away' the problem by rescaling the data."

- question: "When the error covariance matrix Ω is known, GLS is BLUE — but when Ω must be estimated from OLS residuals (Feasible GLS), the estimator is no longer exactly BLUE in finite samples."
  type: true-false
  answer: true
  explanation: "True GLS with known Ω satisfies the Gauss-Markov conditions in the transformed regression, making it BLUE. But Ω is almost never known in practice. FGLS estimates Ω from OLS residuals (e.g., regressing squared residuals on covariates to estimate the heteroskedasticity pattern, or estimating the autocorrelation parameter ρ). This introduces first-step estimation error that propagates into the second step. In finite samples, FGLS is consistent and asymptotically efficient but not exactly BLUE — the small-sample properties depend on how well Ω is estimated."

- question: "OLS is biased when regression errors are heteroskedastic."
  type: true-false
  answer: false
  explanation: "Heteroskedasticity violates the Gauss-Markov assumption of homoskedasticity but does NOT cause bias. OLS is still unbiased (and consistent) under heteroskedasticity — the expected value of the OLS estimator still equals the true parameter. What heteroskedasticity causes is inefficiency: OLS is no longer BLUE because it ignores the information in the variance pattern. It also invalidates standard OLS standard errors and t-statistics (though these can be fixed with Huber-White robust standard errors without changing the point estimates)."

- question: "Why might a researcher prefer robust standard errors over Feasible GLS, even though FGLS can be more efficient?"
  type: short-answer
  answer: "FGLS requires correctly specifying and estimating the error covariance structure Ω. If the model for Ω is misspecified — for example, if you assume a particular heteroskedasticity pattern that doesn't match the true one — FGLS estimates can be worse than OLS. Robust standard errors (Huber-White for heteroskedasticity, Newey-West for serial correlation) make no assumptions about the form of Ω: they leave the OLS point estimates unchanged and only correct the standard errors. In small samples or when the variance structure is uncertain, the weaker assumptions of robust standard errors make them safer and more credible."
  explanation: "This is a classic robustness-efficiency tradeoff. FGLS is potentially more efficient (lower variance) but relies on getting the structure of Ω right. Robust standard errors sacrifice some efficiency but are valid under much broader conditions. In practice, many applied econometricians default to OLS with robust standard errors and only use FGLS when the error structure is well-understood and the efficiency gain is substantial — for instance, in time-series models where AR(1) errors are theoretically motivated and the autocorrelation parameter is precisely estimated."
```

## Explainer

You know from the OLS assumptions that the Gauss-Markov theorem requires **spherical errors**: residuals that are homoskedastic (constant variance) and uncorrelated with each other. When these conditions fail — because errors are heteroskedastic or serially correlated — OLS is no longer the Best Linear Unbiased Estimator. It is still unbiased, but it is inefficient: some other linear estimator uses the data better. GLS is that better estimator.

The core idea is a transformation. Suppose the error variance-covariance matrix is Ω rather than σ²I. OLS minimizes the sum of squared residuals, treating each observation equally. But if some observations have much higher variance than others, they are noisier signals about the true relationship — they should count for less. GLS formalizes this: it pre-multiplies the regression equation by Ω^(-1/2) (the inverse of the Cholesky factor of Ω), which rescales observations by the inverse of their error standard deviation. Observations with high variance get down-weighted; observations with low variance get up-weighted. This transformation restores spherical errors in the new equation, so OLS applied to the transformed data is BLUE.

In matrix terms: the GLS estimator is β̂_GLS = (X'Ω⁻¹X)⁻¹X'Ω⁻¹y. Notice how this collapses to OLS when Ω = σ²I: you recover the standard formula (X'X)⁻¹X'y. The generalization is a **weighted least squares** procedure when Ω is diagonal (only variances differ across observations), or a correlated-errors transformation when Ω has off-diagonal terms (serial correlation). For the serial correlation case, the Prais-Winsten or Cochrane-Orcutt procedures implement GLS by first estimating the autocorrelation parameter ρ and then applying the transformation that removes it.

The practical complication is that Ω is almost never known in advance. You must estimate it from OLS residuals, giving **Feasible GLS** (FGLS). This two-step procedure is consistent but no longer exactly BLUE in finite samples — you've introduced estimation error from the first step. FGLS is often contrasted with the alternative of just using OLS with **robust standard errors** (Huber-White for heteroskedasticity, Newey-West for serial correlation): robust standard errors leave the point estimates alone but correct the inference, while FGLS changes both estimates and standard errors. For large samples the two approaches often give similar results, but FGLS can be more efficient; for small samples, robust standard errors are frequently preferred for their weaker assumptions.
