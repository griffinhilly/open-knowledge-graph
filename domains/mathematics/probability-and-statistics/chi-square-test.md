---
id: chi-square-test
title: Chi-Square Tests
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
- id: expected-value
  type: hard
- id: combinations
  type: soft
tags:
- chi-square
- goodness-of-fit
- independence
- contingency-table
- categorical
stage: formal-systems
status: validated
---

# Chi-Square Tests

## Core Idea
Chi-square tests apply to categorical data. The goodness-of-fit test compares observed frequencies to expected frequencies under a hypothesized distribution: χ² = Σ (O − E)² / E. The test of independence assesses whether two categorical variables are associated in a two-way table. In both cases, χ² measures the total discrepancy between observed and expected counts and follows a chi-square distribution with appropriate degrees of freedom under H₀.

## How It's Best Learned
Compute expected counts (row total × column total / grand total) in a contingency table by hand before using software. Verify that all expected counts are at least 5 before applying the chi-square approximation. Contrast the independence test with the two-sample z-test — both test association but chi-square handles more than two categories.

## Common Misconceptions
- Using observed counts in the formula instead of expected counts in the denominator — always E in the denominator.
- Applying chi-square when expected cell counts are below 5 — the approximation breaks down.
- Concluding causation from a significant test of independence — association is not causation.
