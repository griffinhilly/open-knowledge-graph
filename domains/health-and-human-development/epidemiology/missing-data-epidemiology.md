---
id: missing-data-epidemiology
title: Missing Data and Imputation Methods
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: exposure-measurement-error-epi
  type: soft
- id: outcome-misclassification-epi
  type: soft
- id: multivariable-regression-epi
  type: soft
builds-toward:
- bayesian-epidemiology
tags:
- missing-data
- imputation
- data-quality
- bias-handling
stage: expert
status: draft
---

# Missing Data and Imputation Methods

## Core Idea
Missing data can introduce bias and reduce precision. Data may be Missing Completely at Random (MCAR), Missing at Random (MAR), or Missing Not at Random (MNAR). Multiple imputation is valid under MAR if the missing data mechanism is correctly modeled. Sensitivity analyses assess robustness to MNAR scenarios.

## Questions

```yaml
- question: "In a cohort study, patients with higher blood pressure values are more likely to miss their follow-up visit. Which missing data mechanism applies, and what is the appropriate analytic response?"
  type: multiple-choice
  options:
    - "MCAR — complete-case analysis is valid because missingness is unrelated to outcomes"
    - "MAR — multiple imputation using observed covariates will produce unbiased estimates"
    - "MNAR — standard imputation methods cannot correct for this bias; sensitivity analysis is needed"
    - "MAR — simply using the last observed value for missing visits is sufficient"
  answer: 2
  explanation: "Missingness here depends on the missing value itself (patients with the highest blood pressure are most likely to have missing blood pressure data) — this is MNAR by definition. Under MNAR, neither complete-case analysis nor standard multiple imputation (which assumes MAR) can be trusted to produce unbiased estimates, because the missing values are systematically different from observed ones in a way that cannot be modeled from observed data alone. Sensitivity analysis under different MNAR assumptions is the appropriate response."

- question: "A study finds that older patients are significantly more likely to have missing biomarker data. After controlling for age, the probability of missingness is the same regardless of the biomarker value. Which mechanism applies?"
  type: multiple-choice
  options:
    - "MCAR — because the missing values themselves are unrelated to the biomarker"
    - "MNAR — because age predicts missingness and age is related to the outcome"
    - "MAR — missingness depends on observed age but not on the unobserved biomarker value itself"
    - "MCAR — any relationship between missingness and an observed variable disqualifies MNAR"
  answer: 2
  explanation: "This is the MAR scenario. MAR means: conditional on observed variables (here, age), the probability of being missing does not depend on the missing value itself. Older patients have higher missingness, but among patients of the same age, the missing biomarker values are not systematically different from observed ones. This satisfies MAR, making multiple imputation including age in the imputation model a valid approach. MCAR would require that even age had no relationship to missingness — a stronger assumption."

- question: "'Missing at Random' (MAR) means that the missing observations are a random subset of all observations, similar to randomly discarding data."
  type: true-false
  answer: false
  explanation: "MAR is one of the most poorly named concepts in statistics. It does NOT mean data are missing by random chance — that is MCAR. MAR means missingness depends only on *observed* variables, not on the value of the missing variable itself. A study where younger patients are systematically less likely to have lab results recorded is NOT MCAR (missingness is related to age), but it may be MAR if the missing lab values, conditional on age, are not systematically different from observed lab values. MCAR is a special case of MAR where no observed variable predicts missingness either."

- question: "Under MCAR, discarding all observations with missing data (complete-case analysis) produces unbiased effect estimates, though it reduces sample size and statistical power."
  type: true-false
  answer: true
  explanation: "This is the one scenario where complete-case analysis is unbiased. If data are MCAR, the complete cases are a random sample of the full dataset — there is no systematic selection that would distort effect estimates. The cost is efficiency: you lose observations and thus precision, widening confidence intervals. Under MAR or MNAR, complete-case analysis is biased because the complete cases are not a representative random sample of all observations."

- question: "Why is MNAR impossible to verify from the observed data alone, and what is the appropriate analytic strategy when MNAR is plausible?"
  type: short-answer
  answer: "MNAR means missingness depends on the missing value itself — but since those values are unobserved, you cannot use the data to test whether this relationship exists. Any model of missingness can only be fitted to observed data, leaving the MNAR mechanism unidentifiable. The appropriate strategy is sensitivity analysis: posit a range of plausible MNAR assumptions (e.g., 'missing values are X units higher than observed'), re-run the analysis under each, and assess whether conclusions change. If results are robust across plausible scenarios, confidence grows; if conclusions flip, the uncertainty must be reported."
  explanation: "This is a fundamental epistemological limit: the very data needed to test the MNAR assumption is the data that is missing. Unlike measurement error (where the magnitude of error can sometimes be estimated from validation substudies), MNAR mechanisms are inherently unverifiable without additional external information. Sensitivity analysis makes the uncertainty explicit rather than hiding it under an untestable assumption."
```

## Explainer

From your study of exposure measurement error and outcome misclassification, you know that imperfect data measurement introduces bias — the recorded value differs systematically from the true value. Missing data is a related but distinct problem: for some observations, no value is recorded at all. Like measurement error, missing data can bias results, reduce effective sample size, and undermine inference — but the solution depends entirely on understanding *why* the data is missing, not just that it is.

The three-way taxonomy of missing data mechanisms is the essential conceptual tool. **Missing Completely at Random (MCAR)** means missingness has no relationship to any variable, observed or unobserved — like randomly discarding blood samples in the lab due to a freezer malfunction. MCAR is the only case where simply discarding missing observations (complete-case analysis) produces unbiased estimates, though it wastes data and reduces precision. **Missing at Random (MAR)** — despite the confusing name — does not mean random; it means missingness depends only on *observed* variables, not on the unobserved value itself. For example, older patients may be more likely to have missing biomarker data, but conditional on age, the missing values are not systematically different from observed values. This is the crucial assumption for most imputation methods. **Missing Not at Random (MNAR)** means missingness depends on the value that is missing itself: patients with the highest blood pressure readings are most likely to skip follow-up visits, so missing blood pressure values are systematically higher than observed ones. MNAR is the most dangerous and most common scenario in practice, and it cannot be verified from the observed data alone.

**Multiple imputation** is the standard solution under MAR. Rather than filling in a single "best guess" for each missing value (single imputation, which underestimates uncertainty), multiple imputation creates M complete datasets by drawing M plausible values for each missing observation from a model of the missing data process. Each dataset is analyzed separately using standard methods, and results are combined using Rubin's rules. The key insight is that uncertainty about the imputed values is propagated through the analysis — the variance across imputations adds to, rather than hides, the uncertainty due to missingness. The imputation model should include all variables that will appear in the analysis model plus any auxiliary variables that predict missingness, to satisfy the MAR assumption as broadly as possible.

When MNAR is plausible, the honest response is **sensitivity analysis** rather than a single fixed answer. You posit different assumptions about how missing values differ from observed values — for example, "suppose missing cholesterol values are 10 mg/dL higher on average than the observed distribution" — and re-run the analysis under each scenario. If conclusions are robust across a range of MNAR assumptions, confidence grows. If conclusions flip under plausible MNAR scenarios, the study must acknowledge that the finding is not robust to the missing data structure. The connection to your multivariable regression prerequisite is direct: the imputation model is itself a regression model, and understanding which variables to include and how to specify it requires the same thinking as building any regression model correctly.
