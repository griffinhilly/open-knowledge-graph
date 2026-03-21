---
id: hausman-test-fe-versus-re
title: 'Hausman Test: Fixed Effects vs. Random Effects'
domain: economics
course: econometrics
prerequisites:
- id: hausman-specification-test
  type: hard
- id: fixed-effects-within-transformation
  type: hard
- id: random-effects-error-components
  type: hard
tags:
- panel-data
- model-selection
- hypothesis-testing
stage: formal-systems
status: draft
---

# Hausman Test: Fixed Effects vs. Random Effects

## Core Idea
The Hausman test compares FE and RE estimators under H₀: Cov(αᵢ, X) = 0 (RE is valid). The test statistic H = (β̂_FE - β̂_RE)' Var̂(β̂_FE - β̂_RE)⁻¹ (β̂_FE - β̂_RE) ~ χ²ₖ. Rejection favors FE; failure to reject can justify the more efficient RE.

## Questions

```yaml
- question: "A researcher runs a Hausman test on a panel dataset and obtains a p-value of 0.02. What should she conclude?"
  type: multiple-choice
  options:
    - "The random effects estimator is more efficient and should be preferred"
    - "There is significant evidence that unit effects are correlated with the regressors; use fixed effects"
    - "The fixed effects estimator is biased and should be replaced with random effects"
    - "Neither FE nor RE is valid; the model needs to be respecified from scratch"
  answer: 1
  explanation: "A p-value of 0.02 means we reject H₀: Cov(αᵢ, X) = 0 at the 5% level. Rejection indicates that the unit-specific effects are correlated with the regressors, which invalidates the random effects assumption. Under this condition, RE is inconsistent (suffers omitted variable bias), while FE remains consistent by sweeping out the unit effects through the within transformation. The researcher should use fixed effects. Option A has the conclusion backwards; options C and D misread what rejection implies."

- question: "Under the null hypothesis of the Hausman test, why does the variance of (β̂_FE − β̂_RE) simplify to Var(β̂_FE) − Var(β̂_RE)?"
  type: multiple-choice
  options:
    - "Because under H₀, FE and RE produce numerically identical coefficient estimates"
    - "Because under H₀, RE is the efficient estimator, so the covariance between β̂_RE and (β̂_FE − β̂_RE) is zero — a property of efficient estimators"
    - "Because FE always has higher variance than RE by algebraic construction, regardless of the null"
    - "Because the test requires the two estimators to be run on independent subsamples of the data"
  answer: 1
  explanation: "This is an application of the Hausman (1978) efficiency result. Under H₀, RE is the efficient estimator in the class of linear unbiased estimators. A general property of efficient estimators is that their covariance with any other consistent estimator's deviation from them is zero: Cov(β̂_RE, β̂_FE − β̂_RE) = 0. From this, Var(β̂_FE − β̂_RE) = Var(β̂_FE) − Var(β̂_RE). This simplification is convenient because it means you only need the two variance-covariance matrices to construct the test statistic, with no need to estimate the cross-covariance."

- question: "Failing to reject the null hypothesis in a Hausman test proves that the random effects model is correctly specified."
  type: true-false
  answer: false
  explanation: "Failure to reject H₀ means the data are *consistent with* the RE assumption (Cov(αᵢ, X) = 0) — it does not prove that assumption is true. The test may have low power in small samples, so mild endogeneity might go undetected. Additionally, the Hausman test assumes FE is correctly specified; it does not test for omitted time-varying confounders, which would bias both estimators. 'Failure to reject' should be read as 'insufficient evidence against RE,' not as 'RE is validated.'"

- question: "Under the null hypothesis of the Hausman test, both FE and RE are consistent estimators of the coefficients, but FE is less efficient than RE."
  type: true-false
  answer: true
  explanation: "Under H₀ (Cov(αᵢ, X) = 0), the unit effects are uncorrelated with regressors, so both FE and RE consistently estimate the true parameters. However, FE discards between-unit variation by demeaning — it uses only within-unit changes over time. RE exploits both within and between variation, leading to smaller standard errors. The efficiency gain of RE under H₀ is precisely why we might prefer it when the null holds, and why the Hausman test is worth running: it lets you use the more efficient estimator when it is valid."

- question: "Explain the core logic of the Hausman test: what properties of FE and RE does it exploit, and what does a large discrepancy between their coefficient estimates indicate?"
  type: short-answer
  answer: "The test exploits the fact that FE and RE respond differently to endogeneity. FE is consistent whether or not Cov(αᵢ, X) = 0, because it eliminates unit effects through demeaning. RE is only consistent when Cov(αᵢ, X) = 0. Under H₀, both estimators are consistent and should produce similar estimates (apart from sampling noise). Under H₁ (endogeneity), RE is biased while FE is not — so their estimates diverge systematically. A large, statistically significant gap indicates that RE is picking up the correlation between unit effects and regressors, producing biased estimates. The test statistic quantifies this divergence and compares it to a χ² distribution."
  explanation: "The key insight is that the test does not pick the 'better' model in any general sense — it specifically tests whether RE's efficiency gains come at the cost of consistency. FE is always the safe choice for consistency; RE is the efficient choice when safe. The Hausman test tells you whether the safe and the efficient choice agree closely enough to trust the efficient one."
```

## Explainer

When you work with panel data — observations on multiple units (firms, countries, individuals) over time — a fundamental modeling choice is how to treat the unobserved heterogeneity across units. Your prerequisite study of fixed effects (FE) and random effects (RE) laid out the tradeoff. Fixed effects are conservative: they absorb all unit-level variation, including anything correlated with your regressors, by transforming away the unit means. Random effects are efficient: by treating unit effects as random draws uncorrelated with regressors, they can use between-unit variation and produce smaller standard errors. The catch is that RE is only valid if that correlation assumption actually holds. The **Hausman test** is the formal tool for deciding between them.

The logic exploits a comparison of two estimators that have different properties under the null. Under H₀ (the RE assumption holds), both FE and RE are consistent, but RE is more efficient — it uses more variation. Under H₁ (the unit effects correlate with regressors), FE is still consistent, but RE is inconsistent — it suffers omitted variable bias. If the null is true, β̂_FE and β̂_RE should be close to each other (apart from sampling noise). If the null is false, they should diverge systematically because they are estimating different quantities. The test statistic measures this divergence, weighting it by the precision of the difference.

The test statistic H = (β̂_FE − β̂_RE)' [Var(β̂_FE − β̂_RE)]⁻¹ (β̂_FE − β̂_RE) follows a χ² distribution with k degrees of freedom (where k is the number of time-varying regressors) under H₀. A useful property: because RE is efficient under H₀, the variance of the difference simplifies to Var(β̂_FE) − Var(β̂_RE), which means you only need the two individual variance matrices to compute it. **Rejection** of H₀ (large H statistic) means the coefficient estimates differ enough to reject the RE assumption — use FE. **Failure to reject** means RE's efficiency gains are defensible.

Two practical caveats are worth knowing. First, the Hausman test is a test of RE's validity conditional on FE being correct — it does not test whether either model is well-specified. If you have omitted time-varying confounders, FE won't save you. Second, in small samples the test can have low power, meaning it may fail to reject RE even when mild endogeneity is present. A modern alternative is the cluster-robust Hausman test or the Mundlak approach, which adds group means of time-varying regressors to the RE specification — a rejection there is equivalent to the Hausman conclusion but with robust inference. The key takeaway: the Hausman test is not about which model is "better" in the abstract. It is specifically about whether the efficiency gains of RE come at the cost of consistency.
