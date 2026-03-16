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
status: validated
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

## Explainer

You already know the two-sample t-test: compare two group means by asking how many standard errors separate them. **One-way ANOVA** extends this logic to three or more groups. The natural instinct is to run all pairwise t-tests — with five groups you'd run ten — but this has a serious problem you've encountered in hypothesis testing: **Type I error inflation**. If each test has a 5% false-positive rate and tests are independent, the probability of at least one false positive across ten tests climbs toward 40%. ANOVA provides a single test that handles all groups simultaneously, preserving the overall error rate at α.

The central idea is a **decomposition of variance**. Take all the observations together and measure their total variation around the grand mean — the overall mean of all groups combined. This **total sum of squares** splits into two additive pieces: **SS_between**, which measures how far each group mean sits from the grand mean (weighted by group size), and **SS_within**, which measures how much individual observations scatter around their own group mean. SS_within is the baseline noise — variation that cannot be explained by group membership. SS_between is the signal — variation attributable to the groups themselves.

The **F-statistic** is the ratio F = MS_between / MS_within, where MS (mean square) divides each sum of squares by its **degrees of freedom** to make the quantities comparable. MS_between uses df = k − 1 (k groups), and MS_within uses df = N − k (N total observations). Under the null hypothesis that all group means are equal, both MS_between and MS_within estimate the same population variance σ², so F should be near 1. When group means genuinely differ, MS_between inflates while MS_within remains anchored to within-group noise, pushing F above 1. The F-distribution gives the probability of observing a ratio this large by chance alone.

A significant F-test tells you "at least one group mean differs," not which ones. **Post-hoc tests** like Tukey's Honestly Significant Difference (HSD) perform all pairwise comparisons with a correction that controls the familywise error rate at α — solving the multiple-comparison problem that motivated ANOVA in the first place. The procedure assumes roughly normal data within groups and approximately equal variances (**homoscedasticity**). The normality assumption is fairly robust for moderate sample sizes by the central limit theorem, but unequal variances can distort the F-test; in that case, **Welch's ANOVA** provides a correction analogous to Welch's t-test for the two-group setting.
