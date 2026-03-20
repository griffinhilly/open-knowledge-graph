---
id: anova-one-way-theory
title: 'One-Way ANOVA: Theory and F-Test'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: anova-one-way
  type: soft
- id: f-distribution-theory
  type: hard
builds-toward:
- multiple-comparisons
tags:
- anova
stage: formal-systems
status: draft
---

# One-Way ANOVA: Theory and F-Test

## Core Idea
One-way ANOVA tests the null hypothesis H₀: μ₁ = μ₂ = ... = μₖ, asking whether k group means differ more than chance predicts. The F-statistic equals MS_Between / MS_Within, with degrees of freedom (k−1, n−k). MS_Between captures variation among group means, while MS_Within estimates pooled within-group error. The test assumes equal variances across groups, approximate normality within groups, and independence of observations. A large F value indicates the group means differ more than expected from within-group variability alone.

## How It's Best Learned
Start with a concrete example—compare exam scores across three teaching methods. Compute group means, then manually calculate SS_Between and SS_Within to build intuition for what the F-ratio measures before relying on software output.

## Common Misconceptions
A significant F-test does not tell you which groups differ—post-hoc tests are needed. ANOVA is also reasonably robust to mild normality violations, so the normality assumption is not as fragile as students often fear.

