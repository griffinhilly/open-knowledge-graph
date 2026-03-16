---
id: missing-data-mechanisms-imputation
title: 'Missing Data: Mechanisms, Diagnostics, and Multiple Imputation'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: regression-diagnostics-assumption-violations
  type: hard
- id: probability-mass-functions
  type: soft
- id: conditional-probability
  type: soft
- id: probability-axioms
  type: hard
tags:
- missing-data
- imputation
- mcar-mar
- multiple-imputation
stage: advanced
status: draft
---

# Missing Data: Mechanisms, Diagnostics, and Multiple Imputation

## Core Idea
Missing data is ubiquitous in social research. Data can be missing completely at random (MCAR), at random given observed data (MAR), or not at random (MNAR). Each mechanism requires different handling. Multiple imputation under MAR preserves uncertainty and produces valid inference.

## Explainer

Your prerequisite on regression diagnostics introduced the idea that real data often violates the clean assumptions of standard models. Missing data is one of the most common and consequential violations: when observations are incomplete, naive analysis can produce severely biased results. The key insight is that *how* data goes missing matters as much as *how much* is missing. The three mechanisms form a hierarchy of severity, and each implies a different treatment strategy.

**Missing Completely at Random (MCAR)** is the most benign: whether a value is missing is entirely unrelated to any variable in the dataset, observed or unobserved. A random lab malfunction destroying 5% of samples is MCAR. Listwise deletion — dropping all rows with any missing value — produces unbiased estimates under MCAR, though it reduces statistical power. **Missing at Random (MAR)** is more realistic and more insidious: missingness depends on observed variables but not on the missing values themselves. Older survey respondents might be less likely to report income, but their missingness depends on age (observed), not their actual income. Here, listwise deletion produces biased estimates because it drops a systematically non-random subset of observations. Your conditional probability prerequisite explains why: the dropped observations don't represent a random draw from the population, so the remaining sample is distorted. **Missing Not at Random (MNAR)** is the worst case: missingness depends on the unobserved value itself. High earners skip the income question *because* they earn a lot — the missingness carries information about the very thing you're trying to measure. No standard imputation method can fully correct for MNAR.

**Multiple imputation** is the principled solution for MAR data. Rather than substituting a single "best guess" for each missing value — a strategy called single imputation that understates uncertainty — multiple imputation generates several complete datasets, each with plausible imputed values drawn from a probability model that conditions on all observed data. This is where your probability foundations are essential: each imputed value is a draw from the conditional distribution of the missing variable given everything observed. The analysis model is run on each imputed dataset separately, and results are combined using **Rubin's rules**, which pool point estimates and inflate standard errors to reflect the uncertainty introduced by missingness itself. The final confidence intervals are appropriately wider than they would be with complete data — which is honest, because information was genuinely lost.

Diagnosing the missing data mechanism is crucial before choosing a method, but it is partly untestable. You can detect departures from MCAR by comparing cases with and without missing values on observed variables — if the two groups differ systematically, MCAR is violated. But distinguishing MAR from MNAR is fundamentally unidentifiable from the observed data alone, because the relevant information is by definition missing. Subject-matter knowledge about why data might be missing — survey design, participant attrition, measurement error patterns — is the primary resource here. Sensitivity analyses that model different MNAR scenarios and check how much conclusions change are the best available defense against overconfident inference when the missing data mechanism is uncertain.
