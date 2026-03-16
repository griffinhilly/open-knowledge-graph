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
status: draft
---

# Missing Data: Mechanisms and Analytical Solutions

## Core Idea
Missing data can be missing completely at random (MCAR), missing at random (MAR), or missing not at random (MNAR). The missingness mechanism determines whether listwise deletion is valid or whether imputation, inverse-probability weighting, or selection models are needed.

## How It's Best Learned
Examine patterns of missing data. Use listwise deletion as a baseline, then try multiple imputation or IPW to see if conclusions change.

## Explainer

Missing data is not just an inconvenience — it is a selection problem. When observations drop out of your dataset, the remaining sample may no longer be representative of the population you care about. Whether this matters depends entirely on *why* the data are missing, which is what the three standard mechanisms capture. Think of the missingness mechanism as a treatment assignment rule: what determined whether each observation's data was observed or not?

**MCAR (Missing Completely at Random)** means the probability of being missing is unrelated to both observed and unobserved variables. Imagine a lab assistant randomly drops 5% of blood sample vials — there is no systematic pattern to which samples are lost. Under MCAR, listwise deletion (dropping incomplete cases) produces an unbiased sample; you lose efficiency but not validity. **MAR (Missing at Random)** is more common and more nuanced: missingness depends on observed variables but, conditional on those variables, is unrelated to the unobserved outcome. For example, older survey respondents are less likely to report income, but conditional on age, the missing income values are not systematically different from the reported ones. Under MAR, listwise deletion is still biased because it throws away the information in the observed covariates, but methods that model the missingness process — like **multiple imputation** — can recover valid estimates.

**MNAR (Missing Not at Random)** is the hardest case: the probability of being missing depends on the missing value itself. High-income respondents systematically refuse to report income; severely depressed patients drop out of clinical trials. No standard statistical adjustment can fix MNAR without external assumptions, because you cannot distinguish "the data is missing" from "the data has a particular value" using only what you observe. You must either obtain the missing data through follow-up or build a **selection model** that jointly models the outcome and the missingness process with identifying assumptions.

Your OLS assumptions prerequisite is relevant here because missingness interacts directly with the sample selection requirement. OLS on a complete-case subsample is valid only if that subsample is representative of the full population — which requires MCAR or a carefully conditioned MAR assumption. The practical workflow is: first describe patterns of missingness (what variables predict whether an observation is missing?), then test sensitivity by comparing complete-case results to results from **inverse-probability weighting** (which re-weights observed cases by the inverse probability of being observed) or multiple imputation (which fills in missing values multiple times from a model, preserving uncertainty). If the conclusions change materially across methods, the missing data mechanism is doing real work and the choice of approach must be justified and reported.
