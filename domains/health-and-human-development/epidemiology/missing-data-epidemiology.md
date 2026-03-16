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
stage: advanced
status: draft
---

# Missing Data and Imputation Methods

## Core Idea
Missing data can introduce bias and reduce precision. Data may be Missing Completely at Random (MCAR), Missing at Random (MAR), or Missing Not at Random (MNAR). Multiple imputation is valid under MAR if the missing data mechanism is correctly modeled. Sensitivity analyses assess robustness to MNAR scenarios.

## Explainer

From your study of exposure measurement error and outcome misclassification, you know that imperfect data measurement introduces bias — the recorded value differs systematically from the true value. Missing data is a related but distinct problem: for some observations, no value is recorded at all. Like measurement error, missing data can bias results, reduce effective sample size, and undermine inference — but the solution depends entirely on understanding *why* the data is missing, not just that it is.

The three-way taxonomy of missing data mechanisms is the essential conceptual tool. **Missing Completely at Random (MCAR)** means missingness has no relationship to any variable, observed or unobserved — like randomly discarding blood samples in the lab due to a freezer malfunction. MCAR is the only case where simply discarding missing observations (complete-case analysis) produces unbiased estimates, though it wastes data and reduces precision. **Missing at Random (MAR)** — despite the confusing name — does not mean random; it means missingness depends only on *observed* variables, not on the unobserved value itself. For example, older patients may be more likely to have missing biomarker data, but conditional on age, the missing values are not systematically different from observed values. This is the crucial assumption for most imputation methods. **Missing Not at Random (MNAR)** means missingness depends on the value that is missing itself: patients with the highest blood pressure readings are most likely to skip follow-up visits, so missing blood pressure values are systematically higher than observed ones. MNAR is the most dangerous and most common scenario in practice, and it cannot be verified from the observed data alone.

**Multiple imputation** is the standard solution under MAR. Rather than filling in a single "best guess" for each missing value (single imputation, which underestimates uncertainty), multiple imputation creates M complete datasets by drawing M plausible values for each missing observation from a model of the missing data process. Each dataset is analyzed separately using standard methods, and results are combined using Rubin's rules. The key insight is that uncertainty about the imputed values is propagated through the analysis — the variance across imputations adds to, rather than hides, the uncertainty due to missingness. The imputation model should include all variables that will appear in the analysis model plus any auxiliary variables that predict missingness, to satisfy the MAR assumption as broadly as possible.

When MNAR is plausible, the honest response is **sensitivity analysis** rather than a single fixed answer. You posit different assumptions about how missing values differ from observed values — for example, "suppose missing cholesterol values are 10 mg/dL higher on average than the observed distribution" — and re-run the analysis under each scenario. If conclusions are robust across a range of MNAR assumptions, confidence grows. If conclusions flip under plausible MNAR scenarios, the study must acknowledge that the finding is not robust to the missing data structure. The connection to your multivariable regression prerequisite is direct: the imputation model is itself a regression model, and understanding which variables to include and how to specify it requires the same thinking as building any regression model correctly.
