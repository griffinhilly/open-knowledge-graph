---
id: chi-square-test
title: Chi-Square Test
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
tags:
- chi-square
- goodness-of-fit
- independence
stage: formal-systems
status: draft
---

# Chi-Square Test

## Core Idea
The chi-square test assesses whether observed frequencies in categories differ significantly from expected frequencies under a null hypothesis. For a goodness-of-fit test, it compares observed category frequencies to theoretical (expected) frequencies. For a test of independence, it tests whether two categorical variables are independent in a contingency table. The test statistic is χ² = Σ(Observed - Expected)²/Expected, which follows a chi-square distribution when the null hypothesis is true and expected frequencies are sufficiently large (typically ≥ 5).

## How It's Best Learned
Set up null hypotheses for goodness-of-fit scenarios (coin fairness, six-sided die). Create contingency tables and test independence. Verify that expected frequencies meet assumptions.

## Common Misconceptions
Using chi-square with expected frequencies < 5. Confusing goodness-of-fit with independence tests. Forgetting that small p-values indicate deviation from the null, not confirmation of hypotheses. Thinking chi-square tests directionality (they don't).
