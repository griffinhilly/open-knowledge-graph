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
stage: abstract-reasoning
status: draft
---

# Missing Data Mechanisms, Patterns, and Handling Methods

## Core Idea
Missing data is ubiquitous in psychological research and can bias results if not properly addressed. Mechanisms of missingness—missing completely at random (MCAR), missing at random (MAR), and missing not at random (MNAR)—determine appropriate handling strategies. Deletion methods (listwise, pairwise) are simple but can bias results and reduce statistical power when data are not MCAR. Multiple imputation and maximum likelihood estimation are sophisticated methods that can provide unbiased estimates when data are MCAR or MAR. Understanding the mechanism and pattern of missing data is essential for choosing analytical strategies.

## How It's Best Learned
Examine a dataset with missing data and determine the likely mechanism (MCAR, MAR, MNAR) by exploring patterns and relationships between missing status and observed variables.

## Common Misconceptions
Missing data can be ignored if the sample size is large enough (actually, bias from missing data depends on the mechanism, not sample size). Listwise deletion is appropriate because it uses only complete cases (actually, listwise deletion can introduce bias and reduces power unless data are MCAR).
