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
stage: abstract-reasoning
status: draft
---

# Data Preparation, Screening, and Quality Assurance

## Core Idea
Before analysis, data must be checked for entry errors, missing values, outliers, and assumption violations. Missing data mechanisms (missing completely at random vs. missing at random) affect appropriate handling. Outliers require investigation—are they errors, genuine extreme values, or violations of assumptions? Data cleaning documentation ensures transparency and reproducibility.

## How It's Best Learned
Conduct exploratory data analysis on a dataset: describe distributions, identify missing patterns, investigate outliers. Practice multiple imputation for missing data. Discuss how data preparation decisions can influence downstream results.

## Common Misconceptions
- Data cleaning is optional if sample size is large; - Outliers should always be removed; - Missing data can be ignored if < 5%; - Transformation of variables is data manipulation.

## Explainer

Data analysis is only as trustworthy as the data it operates on — and raw data almost never arrives clean. Before running any statistical model, you need to understand what you actually have: how it was collected, where it might have gone wrong, and what decisions you made to handle its imperfections. This is **data preparation and quality assurance**, and it is not a formality — the choices made here can meaningfully change your conclusions.

Start with the basics: entry errors and range violations. A participant age recorded as 220, a Likert response of 9 on a 1–7 scale, or a reaction time of –200ms are not plausible. These require verification against original records or flagging for exclusion. Then examine distributions: a variable that should be approximately normal but is heavily skewed might indicate a recording error, a floor or ceiling effect, or a genuine distributional feature that violates assumptions of downstream parametric tests. Plotting histograms and running descriptives (mean, median, range, kurtosis) is not busywork — it is your first look at the actual structure of the data.

**Missing data** is where the methodological stakes rise. The key distinction comes from the *mechanism* of missingness. **Missing completely at random (MCAR)** means the probability of missingness is unrelated to anything — data are missing as if by random deletion. This is the least damaging because listwise deletion (dropping incomplete cases) produces unbiased estimates, just with reduced power. **Missing at random (MAR)** means missingness is related to observed variables but not to the missing values themselves — for example, men are more likely to skip depression items, but among men, those who skip don't differ systematically from those who respond. MAR allows valid imputation using other variables. **Missing not at random (MNAR)** is the most problematic: people with severe depression skip depression items precisely because they're severely depressed. Here, any analysis ignoring missingness is potentially biased, and the problem cannot be fully solved from the observed data alone.

**Outliers** require investigation, not reflexive deletion. An extreme value might be a genuine data-entry error (delete or correct it), a legitimate unusual case (consider whether your research question applies to such cases), or an influential observation that reveals a model misspecification (investigate the model, not just the point). Running analyses with and without outliers and reporting both sets of results is often more informative than any single decision rule. Similarly, **variable transformations** — taking the log of a skewed distribution, standardizing variables before analysis — are not manipulations in the pejorative sense; they are adjustments to better satisfy model assumptions. The test of whether a transformation is appropriate is whether it makes substantive sense and whether you declare it transparently in your methods section. Every data preparation decision should be documented: what you found, what you did, and why. This documentation is not optional overhead — it is what separates reproducible science from analysis that cannot be audited or replicated.
