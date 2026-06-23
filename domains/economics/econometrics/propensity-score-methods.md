---
id: propensity-score-methods
title: Propensity Score Methods and Estimation
domain: economics
course: econometrics
prerequisites:
- id: logit-probit-models
  type: hard
- id: causal-inference-observational-data
  type: soft
tags:
- propensity-score
- treatment-effects
- observational
stage: advanced
status: validated
---

# Propensity Score Methods and Estimation

## Core Idea
The propensity score is the probability of treatment given covariates. Propensity score methods balance treated and control groups on observed characteristics through matching, stratification, weighting, or regression adjustment.

## Questions

```yaml
- question: "A researcher estimates the effect of a job training program using propensity score matching. After matching, treated and control groups are nearly identical on all 12 measured covariates. She reports an unbiased causal estimate. What critical assumption is implicit in this claim?"
  type: multiple-choice
  options:
    - "The propensity score model must be correctly specified with no omitted interactions"
    - "Unconfoundedness: all variables that affect both treatment selection and outcomes have been measured and included"
    - "The sample must be large enough that the law of large numbers guarantees balance on unmeasured variables"
    - "The outcome model must be linear for propensity score estimates to be consistent"
  answer: 1
  explanation: "Good observed covariate balance after matching is necessary but not sufficient for an unbiased causal estimate. The unconfoundedness assumption — also called 'selection on observables' or 'conditional independence' — requires that every variable influencing both treatment assignment and potential outcomes has been observed and included. If an unobserved variable (e.g., motivation, family connections) affects who gets training and what their earnings would be, propensity score matching cannot remove that bias. Observing 12 balanced covariates says nothing about the 13th covariate you didn't measure. This assumption is fundamentally untestable."

- question: "Why does propensity score matching solve the 'curse of dimensionality' that plagues direct matching on many covariates?"
  type: multiple-choice
  options:
    - "It selects only the most important covariates and discards the rest, reducing the matching space"
    - "It replaces the high-dimensional covariate vector with a single scalar — the conditional treatment probability — while preserving covariate balance by the balancing property"
    - "It uses a nearest-neighbor algorithm that scales efficiently in high dimensions"
    - "It approximates direct matching but doesn't actually solve dimensionality — it just makes the bias more manageable"
  answer: 1
  explanation: "The Rosenbaum-Rubin (1983) balancing property is the key result: conditional on the propensity score p(X), the distribution of covariates X is the same in treated and control groups. This means matching on one number — the propensity score — achieves the same covariate balance as matching on all the underlying covariates simultaneously. The curse of dimensionality arises because exact matches become impossible as the number of covariates grows; collapsing X to a scalar solves this elegantly without discarding any covariates from the estimation."

- question: "After propensity score matching produces excellent covariate balance on most observed variables, the estimated treatment effect is expected to be unbiased."
  type: true-false
  answer: false
  explanation: "False. Propensity score methods can only balance on observed covariates. The unconfoundedness assumption — which is required for unbiasedness — asserts that no unobserved variable affects both treatment selection and outcomes. This assumption is untestable from the data; good observed balance is consistent with both confounded and unconfounded identification. Sensitivity analysis tools (such as Rosenbaum bounds) can quantify how large an unobserved confounder would need to be to reverse the conclusion, but they cannot prove the assumption holds."

- question: "Propensity scores are estimated by regressing the outcome variable on observed covariates using logistic regression."
  type: true-false
  answer: false
  explanation: "False. The propensity score is the estimated probability of receiving treatment — so the dependent variable in the logistic regression is treatment status (D = 1 if treated, D = 0 if control), not the outcome. The covariates X are the predictors. Regressing the outcome on covariates produces a predictive model for outcomes, which is a different object entirely. This confusion is common because the outcome regression and the propensity score model both use the same covariate set X but serve completely different roles."

- question: "Why does covariate balance on observed variables — even perfect balance — not guarantee that propensity score estimates are free from omitted-variable bias?"
  type: short-answer
  answer: "Propensity score methods condition on observed covariates to make treatment assignment 'as good as random' within matched groups. But this only eliminates selection bias caused by the observed variables you included. If an unobserved variable — say, innate ability, family wealth, or a physician's judgment — affects both who receives treatment and what outcomes they would experience, that selection bias remains in the estimate regardless of how well the observed covariates are balanced. The unconfoundedness assumption requires that the potential outcomes be independent of treatment assignment conditional on all confounders, but if some confounders are unobserved, this condition cannot be verified from the data."
  explanation: "This is the fundamental limitation of all observational study methods that rely on selection on observables. Randomized experiments solve this by design — random assignment guarantees that even unobserved confounders are distributed equally across groups in expectation. Propensity scores are a substitute for randomization when it is unavailable, but they only mimic the effects of randomization on observed covariates. The researcher must rely on domain knowledge to argue that the measured covariates are sufficient to explain all selection — an argument the data alone cannot settle."
```

## Explainer

From matching methods, you know the fundamental problem of causal inference: treated and control units may differ systematically in ways that affect both who receives treatment and what outcomes they'd achieve. Direct matching on observed covariates works when you have a small number of variables, but it breaks down fast. If units differ on five or ten variables, finding a "close match" in that high-dimensional space becomes nearly impossible — the **curse of dimensionality**. Propensity score methods solve this by collapsing all those covariates into a single number.

The **propensity score** p(X) = P(D=1 | X) is the conditional probability that a unit receives treatment given its observed characteristics. The key theoretical result (Rosenbaum and Rubin, 1983) is the balancing property: conditional on the propensity score, treated and control units have the same distribution of observed covariates. In other words, if two units have the same propensity score, they are comparable — even if they differ on individual covariates. This reduces a high-dimensional matching problem to a one-dimensional one.

In practice, you estimate the propensity score using logit or probit — your prerequisite from binary choice models. You regress treatment status D on all observed covariates X, and the fitted probabilities are your estimated propensity scores. Once you have scores, you can apply them in four ways: **propensity score matching** pairs each treated unit to the control unit with the closest score; **stratification** (subclassification) divides the score distribution into bins and compares averages within each bin; **inverse probability of treatment weighting (IPTW)** reweights the sample so treated and control groups look like they came from the same population; **regression adjustment** includes the score as a control variable in an outcome regression.

The critical assumption underlying all propensity score methods is **unconfoundedness** (also called conditional independence or selection on observables): conditional on observed covariates, treatment assignment is independent of potential outcomes. This assumption is untestable — if there are unobserved variables that affect both treatment and outcomes, propensity scores cannot remove that bias, no matter how carefully estimated. This is why checking covariate balance *after* applying the method is essential: good balance means treated and control groups look similar on observed characteristics. It doesn't guarantee good balance on unobserved ones, but poor observed balance is a definitive sign the method has failed. Sensitivity analysis tools (like Rosenbaum bounds) help assess how robust conclusions are to potential hidden confounders.
