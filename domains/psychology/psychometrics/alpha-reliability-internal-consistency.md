---
id: alpha-reliability-internal-consistency
title: Cronbach's Alpha and Internal Consistency Reliability
domain: psychology
course: psychometrics
prerequisites:
- id: internal-consistency-reliability
  type: hard
- id: domain-sampling-theory-reliability-generalization
  type: hard
builds-toward:
- split-half-reliability-spearman-brown
- reliability-estimation-method-selection
tags:
- alpha
- internal-consistency
- reliability-coefficient
stage: advanced
status: draft
---

# Cronbach's Alpha and Internal Consistency Reliability

## Core Idea
Cronbach's alpha is the average of all possible split-half reliabilities and estimates internal consistency for scales measuring a single construct. It depends on both number of items and average inter-item correlation, making it sensitive to item homogeneity. Acceptable alpha ranges from .70 (research) to .90+ (clinical diagnosis), though values above .90 may indicate redundancy.

## How It's Best Learned
Calculate alpha by hand for small datasets using the formula α = (k / k-1) × [1 - (Σσ_i² / σ_total²)] to understand the relationship between item variance, covariance, and total variance.

## Common Misconceptions
- Alpha measures unidimensionality (it measures internal consistency only)
- Higher alpha is always better (alpha is scale-length dependent)
