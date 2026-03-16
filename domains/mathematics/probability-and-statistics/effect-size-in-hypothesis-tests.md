---
id: effect-size-in-hypothesis-tests
title: Effect Size and Practical Significance
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: p-values-and-significance
  type: hard
builds-toward:
- multiple-comparison-corrections
tags:
- hypothesis-testing
- effect-size
- significance
stage: formal-systems
status: draft
---

# Effect Size and Practical Significance

## Core Idea
Effect size measures the magnitude of a difference or relationship, independent of sample size. Common measures: Cohen's d for means, correlation coefficient, odds ratio. Large sample sizes can yield significant p-values with negligible effect sizes. Report both p-values and effect sizes.

## How It's Best Learned
Calculate effect sizes alongside p-values for real datasets. Compare small vs. large effects with same p-value by varying sample size. Interpret effect sizes using Cohen's guidelines. Recognize that significance ≠ large effect.

## Common Misconceptions
Assuming statistical significance indicates large effect. Ignoring effect size when p-value is small. Thinking effect size is dimensionless (it depends on outcome scale). Confusing effect size with importance.

## Explainer

From your study of **p-values**, you know that a small p-value means "this result would be unlikely if the null hypothesis were true" — it is evidence against chance. What p-values do not tell you is how *large* the difference is. Statistical significance is about confidence; **effect size** is about magnitude. These are completely separate questions, and confusing them is one of the most consequential errors in applied statistics.

Here is the core problem: with a large enough sample, even a trivially small difference becomes statistically significant. Suppose you test whether two drugs differ in blood pressure reduction. With n = 1,000,000 patients per group, you might detect a difference of 0.1 mmHg at p < 0.001 — a result that is undeniably real but clinically meaningless (blood pressure fluctuates more than that just from sitting up). The p-value is telling you the data is nearly impossible under the null hypothesis; it says nothing about whether the difference matters.

**Cohen's d** is the standard effect size measure for comparing two means: d = (μ₁ − μ₂) / σ_pooled. Dividing by the pooled standard deviation standardizes the difference, putting it in units of "standard deviations apart." Cohen's rough guidelines — small: d ≈ 0.2, medium: d ≈ 0.5, large: d ≈ 0.8 — give reference points, though appropriate effect sizes vary by field. A study finding d = 0.05 with p = 0.001 has detected a real but negligible effect. A study finding d = 1.2 with p = 0.08 has found a potentially large effect that the sample was too small to confirm at conventional significance levels. Both situations call for different responses, and you cannot distinguish them by looking at the p-value alone.

Other effect size measures suit different situations. For a single-sample proportion test, report the proportion itself. For a two-way contingency table, use **Cramér's V**. For a correlation, the **correlation coefficient r** is already an effect size (r² is the proportion of variance explained). For regression, **R²** plays the same role. The common thread: all effect sizes express the size of a finding in terms that do not depend on sample size. Reporting both a p-value and an effect size is now standard practice in medicine, psychology, and other empirical sciences — the p-value answers "are we sure there is an effect?" and the effect size answers "is the effect worth caring about?" Neither question is complete without the other.
