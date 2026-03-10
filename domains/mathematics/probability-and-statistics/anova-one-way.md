---
id: anova-one-way
title: One-Way ANOVA
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
- id: measures-of-spread
  type: hard
- id: t-test-for-means
  type: soft
tags:
- ANOVA
- F-test
- between-group-variance
- within-group-variance
- multiple-groups
stage: formal-systems
status: draft
---

# One-Way ANOVA

## Core Idea
One-way Analysis of Variance (ANOVA) tests whether the means of three or more groups are all equal, using H₀: μ₁ = μ₂ = … = μₖ. The F-statistic is the ratio of between-group variance to within-group variance: F = MS_between / MS_within. A large F suggests means differ more than would be expected from chance alone. ANOVA does not identify which specific means differ — post-hoc tests (like Tukey's HSD) are required for pairwise comparisons after rejecting H₀.

## How It's Best Learned
Run a simple experiment: measure plant heights under three different fertilizers. Partition total variability into between-group and within-group components in an ANOVA table. Emphasize why running multiple t-tests inflates the Type I error rate — this motivates ANOVA as the correct approach.

## Common Misconceptions
- Using ANOVA when the response variable is categorical — ANOVA requires a quantitative response.
- Concluding which specific means differ from a significant F-test alone — post-hoc tests are required.
- Ignoring ANOVA's assumptions: approximately normal distributions within each group, and roughly equal variances.
