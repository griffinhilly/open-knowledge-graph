---
id: multiple-comparisons-correction-type-i-error
title: Multiple Comparisons and Type I Error Rate Control
domain: psychology
course: research-methods-psychology
prerequisites:
- id: inferential-statistics-psychology
  type: hard
- id: effect-size-and-power
  type: soft
- id: statistical-conclusion-validity-assumptions
  type: soft
- id: conditional-probability
  type: hard
builds-toward:
- exploratory-vs-confirmatory-analysis-strategies
tags:
- statistics
- type-i-error
- multiple-comparisons
- correction
stage: abstract-reasoning
status: draft
---

# Multiple Comparisons and Type I Error Rate Control

## Core Idea
Multiple comparisons problem occurs when researchers conduct numerous statistical tests within a single study, which inflates the family-wise Type I error rate (probability of at least one false positive) beyond the nominal alpha level. Each statistical test carries a probability of Type I error; conducting many tests mathematically increases the probability that at least one will be statistically significant by chance alone. Corrections including Bonferroni, Holm, false discovery rate (FDR), and permutation testing adjust p-values or alpha levels to maintain overall Type I error control. The appropriate severity of correction depends on whether tests are planned (confirmatory) versus exploratory.

## How It's Best Learned
Simulate running multiple independent statistical tests where the null hypothesis is true and observe how often at least one reaches statistical significance.

## Common Misconceptions
Bonferroni correction is always appropriate (actually, it can be overly conservative when tests are correlated). Multiple comparisons corrections only apply to many p-values from the same dataset (actually, any multiple tests of related hypotheses require correction).
