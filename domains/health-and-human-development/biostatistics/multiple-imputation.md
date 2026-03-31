---
id: multiple-imputation
title: Multiple Imputation for Missing Data
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: linear-regression
  type: hard
- id: logistic-regression-biostatistics
  type: soft
- id: mixed-effects-models-biostatistics
  type: soft
builds-toward:
- causal-inference-methods-biostatistics
tags:
- missing-data
- multiple-imputation
- MCAR
- MAR
- MNAR
- Rubin
stage: expert
status: validated
---

# Multiple Imputation for Missing Data

## Core Idea
Missing data is ubiquitous in health research — patients miss clinic visits, questionnaire items are left blank, lab values are not drawn. Simple approaches (complete-case analysis, single-value imputation) either waste data or underestimate uncertainty. Multiple imputation (MI) addresses both problems by creating m (typically 20-50) complete datasets, each with missing values replaced by plausible values drawn from the predictive distribution of the missing data given the observed data. Each dataset is analyzed separately with standard methods, and the results are combined using Rubin's rules, which properly account for both within-imputation uncertainty (sampling variability) and between-imputation uncertainty (uncertainty about the missing values). MI is valid under the Missing at Random (MAR) assumption — that missingness depends on observed data but not on the missing values themselves — which is weaker than the Missing Completely at Random (MCAR) assumption required by complete-case analysis.

## Questions

```yaml
- question: "A clinical trial has 30% missing outcome data. The analyst performs complete-case analysis, using only the 70% of patients with complete data. Under what condition is this approach unbiased?"
  type: multiple-choice
  options:
    - "When the data are Missing at Random (MAR)"
    - "When the data are Missing Completely at Random (MCAR) — missingness is unrelated to any variable, observed or unobserved"
    - "Complete-case analysis is always unbiased because it uses real observed data"
    - "When more than 50% of data are observed"
  answer: 1
  explanation: "Complete-case analysis is unbiased only under MCAR — when the probability of being a complete case is the same for everyone, regardless of their covariate values or outcomes. If sicker patients are more likely to drop out (MAR or MNAR), complete-case analysis is biased because the remaining patients are healthier than the original sample. MCAR is a strong assumption that is rarely plausible in clinical research. Even when unbiased, complete-case analysis is inefficient because it discards all partial information from incomplete cases."

- question: "Single imputation (replacing each missing value with one predicted value, like the mean) produces unbiased point estimates under MAR. However, it still underestimates uncertainty. Why?"
  type: short-answer
  answer: "Single imputation treats the imputed values as if they were observed — it ignores the uncertainty about what the true values were. The resulting dataset has the correct sample size but artificially low variability because every imputed value is the same predicted value rather than a range of plausible values. Standard errors computed from the singly-imputed dataset are too small, confidence intervals are too narrow, and p-values are too small. Multiple imputation corrects this by creating multiple plausible versions of the data, allowing the variability across imputations to quantify the uncertainty introduced by the missing data."
  explanation: "Rubin's rules formalize this: the total variance of an estimate after MI equals the within-imputation variance (average of the m variances) plus the between-imputation variance (variance of the m point estimates) scaled by (1 + 1/m). The between-imputation component is zero for single imputation, which is why it underestimates uncertainty."

- question: "Data are Missing Not at Random (MNAR) when the probability of missingness depends on the unobserved value itself. For example, patients with severe depression are less likely to return for follow-up questionnaires. Multiple imputation under MAR assumptions will produce biased results in this scenario."
  type: true-false
  answer: true
  explanation: "MI under MAR assumes that after conditioning on observed data, the missing values have the same distribution as the observed values. Under MNAR, the missing values are systematically different from what any model based on observed data would predict — depressed patients who drop out have worse scores than depressed patients who remain, even after adjusting for all observed variables. MI would impute scores that are too optimistic. MNAR requires sensitivity analyses (pattern-mixture models, selection models) that explicitly model the missingness mechanism, and these require untestable assumptions about the relationship between missingness and the unobserved data."

- question: "A colleague uses 5 imputations for a multiple imputation analysis, arguing this is sufficient based on Rubin's original recommendation. Is this still considered adequate?"
  type: multiple-choice
  options:
    - "Yes — 5 imputations is always sufficient"
    - "No — current guidance recommends 20-50 or more imputations, especially when the fraction of missing information is high, to stabilize standard error estimates and p-values"
    - "The number of imputations does not affect the results"
    - "Only 1 imputation is needed if the imputation model is correct"
  answer: 1
  explanation: "Rubin's original recommendation of 3-5 imputations was based on efficiency of the point estimate, which stabilizes quickly. However, standard errors, p-values, and particularly confidence interval coverage require many more imputations to stabilize. With 5 imputations, the variability of the variance estimate across repeated analyses is substantial. Current best practice recommends at least 20 imputations as a baseline, with more (50+) when the fraction of missing information is high or when precise p-values are needed."
```

## Explainer

Missing data is not just an inconvenience — it is a structural problem that can invalidate study conclusions if handled incorrectly. The three missing data mechanisms defined by Rubin (1976) determine what is at stake. **MCAR** (Missing Completely at Random) means missingness is unrelated to any data, observed or unobserved — like a lab machine randomly failing. **MAR** (Missing at Random) means missingness depends on observed data but not on the missing values — sicker patients (identified by observed severity scores) are more likely to drop out, but among patients with the same severity, missingness is random. **MNAR** (Missing Not at Random) means missingness depends on the missing values themselves — patients with the worst outcomes are the ones who stop coming back.

Complete-case analysis — analyzing only subjects with no missing data — is valid only under MCAR. Mean imputation, last-observation-carried-forward, and other single-imputation methods either introduce bias or underestimate uncertainty (or both). **Multiple imputation** was developed to handle MAR data while properly quantifying the additional uncertainty caused by missingness.

The MI procedure has three steps. **Imputation**: a statistical model predicts missing values based on observed data, drawing from the predictive distribution to create m complete datasets. Each dataset has different imputed values, reflecting uncertainty about the true values. **Analysis**: each complete dataset is analyzed with the standard method (regression, survival analysis, etc.), producing m sets of estimates and standard errors. **Pooling**: Rubin's rules combine the m results. The pooled point estimate is the average of the m estimates. The total variance includes both the **within-imputation variance** (average of the m variance estimates) and the **between-imputation variance** (variance of the m point estimates, scaled by (1 + 1/m)). The between-imputation component captures exactly the uncertainty due to not knowing the missing values.

The imputation model is critical and must be at least as rich as the analysis model — it should include all variables in the analysis model, auxiliary variables correlated with the missing data or the missingness mechanism, and the outcome variable. An imputation model that omits important predictors will produce biased imputations. Modern implementations (mice in R, mi in Stata) use chained equations (MICE/FCS) that iterate through conditionally specified models for each variable with missing data, accommodating mixtures of continuous, binary, and categorical variables. The practical guidance is: include everything plausibly related to the missing data or the missingness mechanism, use at least 20 imputations, and perform sensitivity analyses for MNAR.
