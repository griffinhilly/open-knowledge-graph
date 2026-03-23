---
id: missing-data-econometrics
title: 'Missing Data: Mechanisms and Analytical Solutions'
domain: economics
course: econometrics
prerequisites:
- id: ols-assumptions
  type: soft
tags:
- missing-data
- attrition
- imputation
stage: formal-systems
status: validated
---

# Missing Data: Mechanisms and Analytical Solutions

## Core Idea
Missing data can be missing completely at random (MCAR), missing at random (MAR), or missing not at random (MNAR). The missingness mechanism determines whether listwise deletion is valid or whether imputation, inverse-probability weighting, or selection models are needed.

## How It's Best Learned
Examine patterns of missing data. Use listwise deletion as a baseline, then try multiple imputation or IPW to see if conclusions change.

## Questions

```yaml
- question: "A clinical trial studies a new antidepressant. Patients experiencing severe side effects are significantly more likely to drop out before the final measurement. The missing outcome data is best classified as:"
  type: multiple-choice
  options:
    - "MCAR — dropout is essentially random because we cannot predict exactly who will drop out"
    - "MAR — dropout depends on observed side effect severity, so missingness is 'at random' conditional on that variable"
    - "MNAR — the probability of being missing depends on the unobserved outcome itself (the very outcome we're trying to measure drives dropout)"
    - "Listwise-deletable — because the dropout mechanism is known, complete-case analysis is valid"
  answer: 2
  explanation: "This is MNAR: patients doing worst (most side effects, least treatment benefit) are most likely to drop out, so the probability of missingness depends directly on the missing outcome value. MCAR requires missingness to be unrelated to all variables — clearly violated here. MAR (option B) would hold only if side effect severity were fully captured in observed covariates and the missing outcomes were representative conditional on those covariates — but if non-response to treatment itself drives dropout, observed covariates cannot account for it. Under MNAR, complete-case analysis and standard imputation are both invalid without modeling the dropout mechanism."

- question: "A researcher uses multiple imputation to handle missing income data in a household survey. Under which mechanism does multiple imputation produce valid estimates?"
  type: multiple-choice
  options:
    - "MCAR only — imputation is unnecessary under MCAR and invalid under MAR and MNAR"
    - "MAR — multiple imputation uses observed variables to model and fill in missing values, which is valid when missingness depends only on observed variables"
    - "MNAR only — imputation models the missingness process, which is only necessary when data is missing not at random"
    - "All three mechanisms — multiple imputation produces unbiased estimates regardless of the missing data mechanism"
  answer: 1
  explanation: "Multiple imputation is designed for the MAR setting: it builds a model from observed data to predict missing values, draws multiple imputed datasets, estimates the model of interest on each, and combines results using Rubin's rules. Under MAR, observed variables contain enough information to make the imputation valid. Under MCAR, it also works (though listwise deletion would too). Under MNAR, imputation that ignores the missingness mechanism is biased — you would need a selection model with explicit identifying assumptions. Multiple imputation assumes MAR; it does not fix MNAR."

- question: "Under the MCAR mechanism, listwise deletion (dropping all observations with missing values) produces an unbiased but smaller sample."
  type: true-false
  answer: true
  explanation: "MCAR means the probability of being missing is completely independent of all variables, observed and unobserved. Under MCAR, the complete cases are a simple random subsample of the full sample — not systematically different from the missing cases on any relevant dimension. Listwise deletion therefore produces unbiased estimates; the only cost is reduced sample size (and thus wider confidence intervals). Under MAR or MNAR, the complete cases are a biased subsample, and listwise deletion produces biased estimates."

- question: "If missing data is classified as MAR (Missing at Random), no statistical adjustment is needed because the data is, by definition, randomly missing."
  type: true-false
  answer: false
  explanation: "'Missing at Random' is a technical term that does NOT mean randomly missing in the colloquial sense. MAR means that, conditional on observed variables, missingness is unrelated to the unobserved values — but unconditionally, missingness may still correlate with observed covariates. For example, older respondents may be less likely to report income, so the complete cases are not a representative sample of the full population. Methods like multiple imputation or inverse-probability weighting are still needed. MCAR — not MAR — is the mechanism closest to 'randomly missing' in the everyday sense."

- question: "Why is MNAR considered the most analytically dangerous missing data mechanism, and what distinguishes it from MAR in terms of what statistical methods can achieve?"
  type: short-answer
  answer: "MNAR is dangerous because missingness depends on the missing value itself — meaning absent data is systematically different from observed data in ways unmeasurable from what you have. Under MAR, observed variables predict missingness and imputation or inverse-probability weighting can produce valid estimates. Under MNAR, even complete knowledge of observed covariates leaves you unable to determine how different the missing values are from observed ones. Standard methods like multiple imputation assume MAR and produce biased results if applied to MNAR data. The only solutions are collecting the missing data through follow-up or building a selection model with identifying assumptions that cannot be tested from the data alone."
  explanation: "The practical implication is that under MNAR, researchers must report sensitivity analyses showing how conclusions change under different assumptions about the missingness. No result can be presented as clean and unbiased. This is why study design emphasizes minimizing attrition — preventing MNAR is far easier than correcting for it after the fact."
```

## Explainer

Missing data is not just an inconvenience — it is a selection problem. When observations drop out of your dataset, the remaining sample may no longer be representative of the population you care about. Whether this matters depends entirely on *why* the data are missing, which is what the three standard mechanisms capture. Think of the missingness mechanism as a treatment assignment rule: what determined whether each observation's data was observed or not?

**MCAR (Missing Completely at Random)** means the probability of being missing is unrelated to both observed and unobserved variables. Imagine a lab assistant randomly drops 5% of blood sample vials — there is no systematic pattern to which samples are lost. Under MCAR, listwise deletion (dropping incomplete cases) produces an unbiased sample; you lose efficiency but not validity. **MAR (Missing at Random)** is more common and more nuanced: missingness depends on observed variables but, conditional on those variables, is unrelated to the unobserved outcome. For example, older survey respondents are less likely to report income, but conditional on age, the missing income values are not systematically different from the reported ones. Under MAR, listwise deletion is still biased because it throws away the information in the observed covariates, but methods that model the missingness process — like **multiple imputation** — can recover valid estimates.

**MNAR (Missing Not at Random)** is the hardest case: the probability of being missing depends on the missing value itself. High-income respondents systematically refuse to report income; severely depressed patients drop out of clinical trials. No standard statistical adjustment can fix MNAR without external assumptions, because you cannot distinguish "the data is missing" from "the data has a particular value" using only what you observe. You must either obtain the missing data through follow-up or build a **selection model** that jointly models the outcome and the missingness process with identifying assumptions.

Your OLS assumptions prerequisite is relevant here because missingness interacts directly with the sample selection requirement. OLS on a complete-case subsample is valid only if that subsample is representative of the full population — which requires MCAR or a carefully conditioned MAR assumption. The practical workflow is: first describe patterns of missingness (what variables predict whether an observation is missing?), then test sensitivity by comparing complete-case results to results from **inverse-probability weighting** (which re-weights observed cases by the inverse probability of being observed) or multiple imputation (which fills in missing values multiple times from a model, preserving uncertainty). If the conclusions change materially across methods, the missing data mechanism is doing real work and the choice of approach must be justified and reported.
