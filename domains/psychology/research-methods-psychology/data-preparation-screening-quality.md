---
id: data-preparation-screening-quality
title: Data Preparation, Screening, and Quality Assurance
domain: psychology
course: research-methods-psychology
prerequisites:
- id: survey-development-administration-sampling
  type: soft
- id: systematic-observation-coding-analysis
  type: soft
builds-toward:
- descriptive-analysis-visualization-summary
tags:
- data-management
- data-quality
- missing-data
- outliers
stage: formal-systems
status: validated
---

# Data Preparation, Screening, and Quality Assurance

## Core Idea
Before analysis, data must be checked for entry errors, missing values, outliers, and assumption violations. Missing data mechanisms (missing completely at random vs. missing at random) affect appropriate handling. Outliers require investigation—are they errors, genuine extreme values, or violations of assumptions? Data cleaning documentation ensures transparency and reproducibility.

## How It's Best Learned
Conduct exploratory data analysis on a dataset: describe distributions, identify missing patterns, investigate outliers. Practice multiple imputation for missing data. Discuss how data preparation decisions can influence downstream results.

## Common Misconceptions
- Data cleaning is optional if sample size is large; - Outliers should always be removed; - Missing data can be ignored if < 5%; - Transformation of variables is data manipulation.

## Questions

```yaml
- question: "In a depression study, participants with the highest depression scores are significantly more likely to skip the follow-up questionnaire. What type of missingness is this, and what is its primary implication?"
  type: multiple-choice
  options:
    - "MCAR — missingness is unrelated to anything, so listwise deletion produces unbiased estimates"
    - "MAR — missingness depends on observed variables, so multiple imputation using other variables is valid"
    - "MNAR — missingness is related to the unobserved values themselves, meaning analyses that ignore it will likely be biased"
    - "MCAR — because we cannot directly observe why participants skipped the questionnaire"
  answer: 2
  explanation: "When the probability of missingness is related to the missing value itself — severely depressed participants skip depression questions because they are severely depressed — the data are Missing Not at Random (MNAR). This is the most serious mechanism because no standard statistical technique can fully correct for it using observed data alone. Listwise deletion, mean imputation, and even multiple imputation all produce biased estimates under MNAR. The problem cannot be solved from the observed data; it requires sensitivity analyses and transparent acknowledgment."

- question: "You discover that three participants have their age recorded as '220'. What is the most appropriate first step?"
  type: multiple-choice
  options:
    - "Remove all three cases immediately to protect data integrity"
    - "Replace each value with the sample mean age"
    - "Verify the values against original records; correct if possible, flag for exclusion if not verifiable"
    - "Ignore them — three impossible values cannot materially affect a large sample"
  answer: 2
  explanation: "An impossible value is most likely a data entry error, but the responsible action is verification rather than reflexive deletion. The original questionnaire or data record may reveal the actual value. If verification is impossible, the case should be excluded with documentation. Replacing with the mean treats a likely error as a valid observation. And ignoring extreme values — even in large samples — risks distorting distributions and violating assumptions of downstream parametric tests."

- question: "If less than 5% of values are missing, listwise deletion always produces unbiased estimates."
  type: true-false
  answer: false
  explanation: "The appropriateness of listwise deletion depends on the missingness mechanism, not the proportion of missing data. If data are MNAR — even if only 1% are missing — listwise deletion produces biased estimates because the excluded cases are systematically different from those retained. The 5% threshold is a rough guideline for when missingness is unlikely to be a practical problem under MCAR, not a guarantee against bias under any mechanism."

- question: "Documenting every data preparation decision — what was found, what was done, and why — is essential for scientific reproducibility, not optional bookkeeping."
  type: true-false
  answer: true
  explanation: "Data preparation decisions (which outliers were removed, how missing data were handled, which variables were transformed) directly affect statistical results and can alter conclusions. Without documentation, another researcher cannot reproduce the analysis and reviewers cannot evaluate whether decisions were reasonable or introduced bias. These decisions belong in the methods section of any publication — they are part of the analytical record, not pre-analysis housekeeping."

- question: "Why is it necessary to determine the mechanism of missingness (MCAR, MAR, or MNAR) before deciding how to handle missing data?"
  type: short-answer
  answer: "Each mechanism has different implications for bias. Under MCAR, the missing cases are a random subsample, so listwise deletion is unbiased (only losing power). Under MAR, missingness is related to observed variables but not to the missing values themselves, so multiple imputation using those observed variables can restore unbiased estimates. Under MNAR, missingness is related to the unobserved value itself, and neither listwise deletion nor standard imputation is unbiased — any analysis ignoring the missingness is systematically skewed. Applying the wrong method can produce results that look complete and valid but are driven by who did not respond."
  explanation: "The key insight is that missing data is not just a nuisance with a default remedy. The mechanism determines whether the observed data is a representative sample of what you intended to measure. Treating all missingness the same — say, always using listwise deletion — can introduce systematic bias that inflates or deflates effect estimates, undermining the entire analysis."
```

## Explainer

Data analysis is only as trustworthy as the data it operates on — and raw data almost never arrives clean. Before running any statistical model, you need to understand what you actually have: how it was collected, where it might have gone wrong, and what decisions you made to handle its imperfections. This is **data preparation and quality assurance**, and it is not a formality — the choices made here can meaningfully change your conclusions.

Start with the basics: entry errors and range violations. A participant age recorded as 220, a Likert response of 9 on a 1–7 scale, or a reaction time of –200ms are not plausible. These require verification against original records or flagging for exclusion. Then examine distributions: a variable that should be approximately normal but is heavily skewed might indicate a recording error, a floor or ceiling effect, or a genuine distributional feature that violates assumptions of downstream parametric tests. Plotting histograms and running descriptives (mean, median, range, kurtosis) is not busywork — it is your first look at the actual structure of the data.

**Missing data** is where the methodological stakes rise. The key distinction comes from the *mechanism* of missingness. **Missing completely at random (MCAR)** means the probability of missingness is unrelated to anything — data are missing as if by random deletion. This is the least damaging because listwise deletion (dropping incomplete cases) produces unbiased estimates, just with reduced power. **Missing at random (MAR)** means missingness is related to observed variables but not to the missing values themselves — for example, men are more likely to skip depression items, but among men, those who skip don't differ systematically from those who respond. MAR allows valid imputation using other variables. **Missing not at random (MNAR)** is the most problematic: people with severe depression skip depression items precisely because they're severely depressed. Here, any analysis ignoring missingness is potentially biased, and the problem cannot be fully solved from the observed data alone.

**Outliers** require investigation, not reflexive deletion. An extreme value might be a genuine data-entry error (delete or correct it), a legitimate unusual case (consider whether your research question applies to such cases), or an influential observation that reveals a model misspecification (investigate the model, not just the point). Running analyses with and without outliers and reporting both sets of results is often more informative than any single decision rule. Similarly, **variable transformations** — taking the log of a skewed distribution, standardizing variables before analysis — are not manipulations in the pejorative sense; they are adjustments to better satisfy model assumptions. The test of whether a transformation is appropriate is whether it makes substantive sense and whether you declare it transparently in your methods section. Every data preparation decision should be documented: what you found, what you did, and why. This documentation is not optional overhead — it is what separates reproducible science from analysis that cannot be audited or replicated.
