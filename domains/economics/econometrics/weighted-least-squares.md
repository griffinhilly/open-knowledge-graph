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
status: validated
---

# Weighted Least Squares (WLS)

## Core Idea
WLS applies inverse-variance weights to observations to correct for heteroskedasticity. High-variance observations receive lower weight, improving efficiency when the variance structure is known or can be estimated.

## How It's Best Learned
Estimate the variance function from residuals, then use predicted variances as weights in a second-stage regression. Compare WLS standard errors to OLS standard errors to verify the efficiency gain.

## Questions

```yaml
- question: "A dataset contains household income surveys where wealthier households have far more variable income reports. You run OLS and find heteroskedasticity. What does WLS do differently from using robust standard errors?"
  type: multiple-choice
  options:
    - "WLS corrects the coefficient estimates; robust SEs correct only the standard errors"
    - "WLS re-weights observations to restore efficiency, producing BLUE estimates; robust SEs correct standard errors without changing the estimates or their efficiency"
    - "WLS removes high-variance observations; robust SEs keep them but downweight their influence"
    - "WLS and robust standard errors are equivalent approaches that produce identical results"
  answer: 1
  explanation: "Both approaches address heteroskedasticity, but they work differently. Robust standard errors leave the OLS coefficient estimates unchanged and correct only the standard errors for inference. WLS re-weights the data — giving low weight to high-variance observations — to produce a new estimator that is BLUE (Best Linear Unbiased Estimator) when the variance structure is correctly specified. WLS estimates are more efficient than OLS under heteroskedasticity; robust SEs make OLS inference valid without improving efficiency. The tradeoff: WLS is better when the variance model is correct; robust SEs are safer when it's not."

- question: "In feasible WLS, you estimate weights from the data rather than knowing the true variance function. What is the main risk of this two-stage procedure?"
  type: multiple-choice
  options:
    - "The coefficient estimates become biased because estimated weights introduce endogeneity"
    - "The efficiency gain disappears entirely if the variance model is misspecified"
    - "Estimated weights introduce additional uncertainty that can distort standard errors in finite samples, and misspecification of the variance model can reduce efficiency below OLS"
    - "Feasible WLS always produces larger standard errors than OLS, making it conservative"
  answer: 2
  explanation: "Feasible WLS uses the data twice — once to estimate the variance function, once to run WLS — which introduces additional uncertainty. In large samples this usually doesn't matter much, but in finite samples the estimated weights add noise. More importantly, if the variance model is misspecified (e.g., variance is modeled as a linear function of X when it's actually quadratic), feasible WLS can be less efficient than OLS, not more. This is why verifying that WLS residuals look more homoskedastic than OLS residuals is an important diagnostic step."

- question: "WLS assigns higher weight to observations with high variance because they contain more information about the true relationship."
  type: true-false
  answer: false
  explanation: "This is exactly backwards. WLS assigns LOWER weight (w_i = 1/σ²_i) to high-variance observations, because high variance means an observation contains less precise information about the true relationship. A noisily-measured data point should pull the regression line less than a precisely-measured one. Giving high-variance observations large weight — as plain OLS effectively does by treating all observations equally — allows a few noisy points to disproportionately distort the estimated coefficients."

- question: "WLS is a special case of Generalized Least Squares (GLS) applicable when errors are heteroskedastic but uncorrelated across observations."
  type: true-false
  answer: true
  explanation: "GLS handles the general case where the error covariance matrix Ω is any positive definite matrix. WLS is the special case where Ω is diagonal — errors are uncorrelated across observations but have different variances on the diagonal. The GLS transformation multiplies by Ω^{-1/2}; for the diagonal WLS case, this is simply dividing each observation i by its standard deviation σ_i, which is equivalent to multiplying by the square root of the weight. After this transformation, the rescaled errors are homoskedastic and OLS on the transformed data is efficient."

- question: "Explain intuitively why WLS assigns higher weight to low-variance observations, and what problem this solves."
  type: short-answer
  answer: "Low-variance observations are precisely measured — they tell us a lot about the true relationship between X and Y. High-variance observations are noisy — they tell us less. OLS treats all observations equally, so a handful of imprecise, noisy points can pull the fitted line away from the true relationship. WLS corrects this by giving each observation influence proportional to its precision (inverse variance). The result is a fitted line that is more tightly governed by informative data, achieving the minimum variance among all linear unbiased estimators — BLUE — when the variance structure is correctly specified."
  explanation: "This is the core intuition behind WLS: weight by precision, not by count. The analogy is measuring a table with a ruler versus with a tape measure — if you have 10 ruler measurements and 1 tape measure measurement, you should trust the average of the ruler measurements more, but not ignore the tape measure reading. WLS formalizes this intuition into a regression framework."
```

## Explainer

You already know that heteroskedasticity — non-constant error variance — doesn't bias OLS coefficient estimates, but it does make them inefficient and invalidates standard errors. Robust standard errors are one fix: they correct the standard errors without changing the point estimates. **Weighted Least Squares** (WLS) takes a more structural approach: it re-weights the data so that the effective error variance *becomes* constant, then runs OLS on the re-weighted problem.

The intuition is straightforward. Think of fitting a line through data where some observations are measured precisely (small variance) and others are measured noisily (large variance). OLS treats every data point equally, so a single noisy observation can pull the line substantially. That's wasteful — a data point with high variance contains less information about the true relationship and shouldn't count as much. WLS assigns each observation a weight equal to the inverse of its variance: w_i = 1/σ²_i. Observations with small variance (high precision) get large weights; observations with large variance get small weights. The result is **BLUE** — Best Linear Unbiased Estimator — under the correct variance specification, just as OLS is BLUE under homoskedasticity.

From your study of Generalized Least Squares (GLS), you know that WLS is a special case. GLS handles a general covariance structure Ω, transforming the model by Ω^{-1/2} to produce a homoskedastic, uncorrelated error. WLS is GLS restricted to the diagonal case where errors are uncorrelated but have different variances. The transformation is simply dividing each observation by its standard deviation σ_i — equivalently, multiplying by the square root of the weight. After this transformation, the rescaled errors have equal variance, and ordinary OLS applied to the transformed data is efficient.

The practical challenge is that the true σ²_i values are never observed. In **feasible WLS**, you estimate them from the data. One common approach: run OLS first, take the squared residuals as noisy proxies for σ²_i, then regress log(ê²_i) on functions of the regressors to get a smooth variance function. The fitted values from this auxiliary regression provide estimated weights for the second-stage WLS. The two-stage procedure introduces uncertainty into the weights themselves, which can affect standard errors in finite samples. This is why comparing WLS and OLS standard errors — and checking whether the residuals from the WLS regression look more homoskedastic — is important before trusting the efficiency gain.
