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

## Questions

```yaml
- question: "A researcher has 40 observations with severe heteroskedasticity. She specifies an FGLS model assuming variance is proportional to x², estimates Ω̂ from OLS residuals, then applies GLS using Ω̂. But the true variance structure is actually proportional to x³. What is the most likely outcome?"
  type: multiple-choice
  options:
    - "FGLS will still be efficient because any correction for heteroskedasticity improves on OLS"
    - "FGLS may perform worse than both OLS and correct GLS due to misspecification of the covariance form"
    - "FGLS will be unbiased but inefficient, with performance identical to OLS"
    - "FGLS will be exactly as efficient as OLS because the sample size is too small for GLS improvements"
  answer: 1
  explanation: "This is the central danger of FGLS: if you specify the wrong covariance model, Ω̂ is systematically wrong, and the FGLS transformation distorts the data in the wrong way. The resulting estimator can have worse properties than plain OLS, which makes no transformation at all. With only 40 observations, the first-stage covariance estimation is also imprecise. The practical lesson: FGLS requires both a well-motivated covariance form AND a large enough sample for the first-stage estimation to be reliable."

- question: "What does FGLS estimate in its first step, and why is this step necessary?"
  type: multiple-choice
  options:
    - "The regression coefficients β, which are then used to construct Ω̂"
    - "The error covariance structure Ω from OLS residuals, because true GLS requires knowing Ω a priori"
    - "The instrumental variables needed to address endogeneity in the transformed model"
    - "The optimal bandwidth for kernel-based heteroskedasticity correction"
  answer: 1
  explanation: "True GLS requires knowing the exact error covariance matrix Ω — which in practice you almost never have. FGLS makes GLS feasible by estimating Ω from the data. In step 1, you run OLS and collect residuals, then use those residuals to estimate the covariance structure (regressing squared residuals on regressors for heteroskedasticity, estimating ρ from an AR model for serial correlation, etc.). Only then can you perform step 2: apply GLS using Ω̂ in place of Ω. The necessity of step 1 is precisely what distinguishes FGLS from GLS."

- question: "In large samples, FGLS is asymptotically equivalent to true GLS — both achieve the same efficiency gains over OLS."
  type: true-false
  answer: true
  explanation: "As sample size grows, the first-stage estimate Ω̂ converges to the true Ω, so the FGLS transformation converges to the true GLS transformation. In the limit, the two estimators are asymptotically equivalent: both achieve the Gauss-Markov lower bound under the correctly specified covariance model. This is why the FGLS tradeoff depends heavily on sample size — in small samples, the estimation error in Ω̂ can dominate, but in large samples it becomes negligible."

- question: "FGLS is always more efficient than OLS because it corrects for non-spherical errors, so it should be the default estimator whenever heteroskedasticity or autocorrelation is suspected."
  type: true-false
  answer: false
  explanation: "This is the most dangerous misconception about FGLS. Efficiency gains require that (a) the covariance structure is correctly specified and (b) the sample is large enough for step-1 estimation to be precise. If either condition fails, FGLS can have *higher* mean squared error than OLS. In small samples with misspecified covariance structure, the two-step estimation introduces noise that can more than offset the efficiency gains. This is why practitioners often prefer heteroskedasticity-robust standard errors for moderate samples — they require no assumption about the form of heteroskedasticity."

- question: "Why do practitioners often prefer heteroskedasticity-robust standard errors over FGLS when facing heteroskedasticity, even though FGLS explicitly models and corrects for the heteroskedasticity?"
  type: short-answer
  answer: "Robust standard errors correct the *inference* (standard errors and test statistics) without modifying the OLS point estimates, and they require no assumption about the *form* of heteroskedasticity — only its existence. FGLS requires specifying a parametric model for how variance depends on covariates, estimating that model from residuals, and transforming the data accordingly. If the specified form is wrong, FGLS introduces systematic bias in the transformation. Robust standard errors sacrifice the efficiency gains from GLS but avoid the risk of misspecification-induced distortions. FGLS is most valuable when the covariance structure is well-motivated theoretically and the sample is large enough for precise first-stage estimation."
  explanation: "The key asymmetry: robust standard errors are conservative (sacrifice efficiency) but robust to misspecification; FGLS gains efficiency conditional on correct specification but can fail badly when misspecified. In practice, the form of heteroskedasticity is rarely known with certainty, making the robustness of the simpler approach more attractive unless there is a strong theoretical prior about the variance structure."
```

## Explainer

From your study of GLS, you know the fundamental problem it solves: when errors have non-constant variance (heteroskedasticity) or are correlated across observations, OLS is still unbiased but no longer efficient, and standard errors are wrong. GLS corrects this by pre-multiplying the model by the inverse square root of the error covariance matrix Ω, transforming the data into a form where OLS is once again the best linear unbiased estimator. The catch is that GLS requires knowing Ω — the exact structure of the errors — which in practice you almost never do. **FGLS** (Feasible GLS) resolves this by estimating Ω from the data itself, then using that estimate in place of the true covariance structure.

The mechanics are a two-step procedure. In **Step 1**, you run OLS and collect the residuals. You then use those residuals to estimate the covariance structure — the specific approach depends on what form of misspecification you suspect. For heteroskedasticity, you might regress squared residuals on the regressors or their functions to estimate how variance scales with covariates. For serial correlation, you might estimate an AR(1) process from the residuals to get ρ, the autocorrelation coefficient. This gives you Ω̂, your estimate of the covariance matrix. In **Step 2**, you apply GLS using Ω̂ in place of Ω: transform the data by pre-multiplying by Ω̂^(-1/2) and run OLS on the transformed model. The resulting estimator is FGLS.

The key tradeoff relative to true GLS is that FGLS is no longer exactly optimal in finite samples, because Ω̂ is itself estimated with error. This introduces a form of generated-regressor bias that shrinks as sample size grows. In large samples, FGLS is asymptotically equivalent to GLS — both achieve the same efficiency gains over OLS. In small samples, however, the two-step estimation can introduce substantial noise, and FGLS may actually perform worse than plain OLS if the covariance model is poorly estimated. The practical rule: FGLS pays off most when (a) the sample is large enough for the first-stage covariance estimation to be precise, and (b) the misspecification (heteroskedasticity or autocorrelation) is severe enough to make the efficiency gain worth the additional complexity.

The deeper sensitivity is **misspecification of the covariance form**. If you assume heteroskedasticity follows a particular parametric pattern but the true pattern differs, your Ω̂ is wrong in a systematic way, and FGLS can perform badly — potentially worse than either OLS or the correct GLS. This is why practitioners often prefer **heteroskedasticity-robust standard errors** (which leave OLS point estimates unchanged but correct the inference) over FGLS for heteroskedasticity problems: they require no assumption about the form of heteroskedasticity. FGLS is most natural when the covariance structure is well-motivated theoretically — for example, in **feasible WLS** (weighted least squares), where you have strong prior reason to believe variance is proportional to a particular variable, or in panel data settings with known autocorrelation structures. Knowing when to use FGLS versus robust standard errors versus a fully specified panel estimator is the judgment call that separates mechanical application from genuine econometric skill.
