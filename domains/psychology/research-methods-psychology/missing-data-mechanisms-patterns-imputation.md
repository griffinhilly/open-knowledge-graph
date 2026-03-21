---
id: missing-data-mechanisms-patterns-imputation
title: Missing Data Mechanisms, Patterns, and Handling Methods
domain: psychology
course: research-methods-psychology
prerequisites:
- id: inferential-statistics-psychology
  type: hard
- id: sampling-in-psychology
  type: soft
- id: longitudinal-designs-temporal-change-patterns
  type: soft
builds-toward:
- exploratory-vs-confirmatory-analysis-strategies
tags:
- statistics
- missing-data
- imputation
- data-quality
stage: formal-systems
status: draft
---

# Missing Data Mechanisms, Patterns, and Handling Methods

## Core Idea
Missing data is ubiquitous in psychological research and can bias results if not properly addressed. Mechanisms of missingness—missing completely at random (MCAR), missing at random (MAR), and missing not at random (MNAR)—determine appropriate handling strategies. Deletion methods (listwise, pairwise) are simple but can bias results and reduce statistical power when data are not MCAR. Multiple imputation and maximum likelihood estimation are sophisticated methods that can provide unbiased estimates when data are MCAR or MAR. Understanding the mechanism and pattern of missing data is essential for choosing analytical strategies.

## How It's Best Learned
Examine a dataset with missing data and determine the likely mechanism (MCAR, MAR, MNAR) by exploring patterns and relationships between missing status and observed variables.

## Common Misconceptions
Missing data can be ignored if the sample size is large enough (actually, bias from missing data depends on the mechanism, not sample size). Listwise deletion is appropriate because it uses only complete cases (actually, listwise deletion can introduce bias and reduces power unless data are MCAR).

## Questions

```yaml
- question: "A longitudinal clinical trial finds that participants with the worst symptoms are most likely to drop out before the final assessment. What is the missingness mechanism, and what is the consequence for a listwise-deletion analysis?"
  type: multiple-choice
  options:
    - "MCAR — dropout is random and listwise deletion yields unbiased estimates"
    - "MAR — missingness is related to observed variables and can be corrected by controlling for baseline severity"
    - "MNAR — missingness is related to the unobserved missing values themselves, and listwise deletion will make outcomes look better than the true population"
    - "MNAR — but because completers are a large enough sample, estimates remain valid"
  answer: 2
  explanation: "When dropout depends on the variable being measured (current symptom severity, which is unobserved at the missing time points), the mechanism is MNAR. Listwise deletion retains only completers — who by definition have less severe symptoms — creating a sample that is systematically healthier than the intended population. No statistical technique fully corrects MNAR without additional data or assumptions. Option D is the dangerous 'large sample = no bias' misconception; sample size affects precision, not the direction of systematic bias."

- question: "A researcher uses listwise deletion in a study where income data is missing more often for lower-education participants, but education is fully observed for all participants. Under what condition would listwise deletion still produce unbiased estimates?"
  type: multiple-choice
  options:
    - "If the proportion of missing data is below 10%"
    - "If the sample size is large enough to preserve statistical power"
    - "Only if the data are MCAR — that is, missingness is unrelated to any observed or unobserved variable"
    - "If the researcher controls for education in the regression model"
  answer: 2
  explanation: "Listwise deletion is unbiased only under MCAR. In this scenario, missingness depends on education (an observed variable), making it MAR — not MCAR. Listwise deletion will bias income estimates because completers are not a random subset; they skew toward higher education. Options A and B address power, not bias — even a large study with 5% missing data can be severely biased if the mechanism is MNAR or MAR. Option D (controlling for education) is actually the MAR fix, but that requires a method like MI or FIML, not listwise deletion."

- question: "Having a large sample size is sufficient to protect against bias caused by missing data, as long as the proportion of missingness is small."
  type: true-false
  answer: false
  explanation: "Bias from missing data depends on the missingness mechanism, not the sample size or the proportion missing. Under MNAR, even 5% missingness can produce substantial systematic distortion regardless of how large the study is. Large sample size reduces random error (increases precision) but does not correct systematic bias. A biased large study just gives you a precise estimate of the wrong answer."

- question: "Multiple imputation produces valid inferences under MAR because it replaces missing values with estimates drawn from a distribution based on observed data, and combines results across multiple completed datasets to propagate imputation uncertainty."
  type: true-false
  answer: true
  explanation: "This accurately describes MI. Under MAR, the observed variables contain sufficient information to model the missing data distribution. By creating multiple completed datasets (rather than a single imputed dataset), MI correctly captures the uncertainty introduced by imputation in the final standard errors and confidence intervals — via Rubin's rules. A single-imputation approach would underestimate uncertainty by treating imputed values as known."

- question: "Why is it impossible for any purely statistical method to fully correct for MNAR missingness without additional data or external assumptions?"
  type: short-answer
  answer: "Under MNAR, the probability of a value being missing depends on the unobserved value itself. Since we never see the missing values, we cannot model or verify this relationship from the observed data alone. Any statistical correction would require assumptions about the unobserved distribution of missing values — assumptions that the data cannot confirm or refute. Without additional information (e.g., external validation data, sensitivity analyses with explicit MNAR models), these assumptions are untestable."
  explanation: "For contrast: under MAR, we can use observed variables to model who is missing and why, allowing MI or FIML to recover unbiased estimates. But under MNAR, the very data we need to model the missingness process is the data that is missing. This is why MNAR is the most serious validity threat — it requires investigators to use substantive knowledge and sensitivity analyses rather than statistical techniques alone."
```

## Explainer

Missing data is not just an inconvenience — it is a measurement and inference problem that, if handled naively, can systematically distort your conclusions. From your work on inferential statistics, you know that valid inference requires your observed sample to represent the target population. When data are missing, you no longer have a clean random sample; you have a sample shaped by a process that determined who or what is missing. Understanding that process — the **missingness mechanism** — is the essential first step, because the right remedy depends entirely on why data are absent.

The three mechanisms form a hierarchy of seriousness. **Missing Completely At Random (MCAR)** means the probability of a value being missing is unrelated to anything — not to the variable itself, not to any other measured variable. A participant's questionnaire page getting coffee spilled on it is MCAR. Under MCAR, your complete cases are a random subset of your intended sample, and simple deletion methods (listwise, pairwise) produce unbiased estimates — just with reduced power. **Missing At Random (MAR)** is more subtle: missingness is related to other *observed* variables in the dataset, but not to the unobserved missing values themselves. Women in a survey might be less likely to report income, but if you can model who is missing income based on other observed variables (gender, education, age), the missingness is "explainable" by things you've measured. Under MAR, sophisticated methods can recover unbiased estimates. **Missing Not At Random (MNAR)** is the hardest case: missingness is related to the missing value itself. Depressed individuals are less likely to complete depression measures precisely because of their depression. No statistical method can fully correct for MNAR without additional assumptions or external data.

**Listwise deletion** — dropping any case with any missing value — is the default in most software and the most commonly misused approach. Under MCAR it gives unbiased (but underpowered) results. Under MAR or MNAR it introduces **selection bias**: your "complete case" sample is systematically different from the intended sample in ways that distort your estimates. Imagine a longitudinal study where participants with worsening symptoms are most likely to drop out. Your remaining sample of "completers" will look healthier than the true population, biasing outcome estimates downward. This isn't a statistical technicality — it's a substantive distortion of your research conclusions.

**Multiple imputation (MI)** addresses this by replacing each missing value not with a single number but with a set of plausible values drawn from a distribution estimated from observed data. Running analyses on multiple completed datasets and combining results using Rubin's rules propagates the uncertainty from the imputation into your final estimates, producing correct standard errors. **Full information maximum likelihood (FIML)** takes a different approach: instead of filling in missing values, it uses all observed information to estimate model parameters directly, including cases with partial data. Under MAR, both MI and FIML produce valid inferences. Under MNAR, both are biased — and so is any other method — but MI and FIML typically produce *less* biased estimates than listwise deletion, making them the preferred default.

The practical workflow starts with **diagnosing the mechanism**: examine whether missingness correlates with observed variables (test MCAR formally with Little's test, explore MAR patterns by regressing missingness indicators on observed covariates). Then choose your method accordingly — and always report how you handled missing data so readers can evaluate the validity threat. The key mindset shift is treating missing data as a data quality issue to be modeled, not a nuisance to be removed. A dataset with 30% missing data handled thoughtfully via MI can yield more valid conclusions than a "complete" dataset where missingness was ignored.
