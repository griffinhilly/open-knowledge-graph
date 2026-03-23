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
status: validated
---

# Effect Size and Practical Significance

## Core Idea
Effect size measures the magnitude of a difference or relationship, independent of sample size. Common measures: Cohen's d for means, correlation coefficient, odds ratio. Large sample sizes can yield significant p-values with negligible effect sizes. Report both p-values and effect sizes.

## How It's Best Learned
Calculate effect sizes alongside p-values for real datasets. Compare small vs. large effects with same p-value by varying sample size. Interpret effect sizes using Cohen's guidelines. Recognize that significance ≠ large effect.

## Common Misconceptions
Assuming statistical significance indicates large effect. Ignoring effect size when p-value is small. Thinking effect size is dimensionless (it depends on outcome scale). Confusing effect size with importance.

## Questions

```yaml
- question: "A pharmaceutical trial with n = 500,000 participants per group finds a statistically significant reduction in cholesterol (p < 0.0001, Cohen's d = 0.04). What is the correct interpretation?"
  type: multiple-choice
  options:
    - "The drug is highly effective because the p-value is very small"
    - "The result is probably a false positive despite the significant p-value"
    - "The drug produces a real but negligibly small effect — statistical significance does not imply practical importance"
    - "The sample size is too large for p-values to be meaningful"
  answer: 2
  explanation: "This is the classic disconnect between statistical and practical significance. A p-value of < 0.0001 means we are very confident the effect is real — the data would be extraordinarily unlikely under the null. But Cohen's d = 0.04 means the difference is only 0.04 standard deviations, negligible by any clinical standard. The enormous sample size is what drove a trivially small effect to statistical significance. The correct conclusion: real, but practically meaningless."

- question: "What does Cohen's d measure that a p-value cannot?"
  type: multiple-choice
  options:
    - "Whether the observed result would be unlikely by chance"
    - "The probability that the null hypothesis is true"
    - "The magnitude of the difference between groups, in units of pooled standard deviations"
    - "The confidence level at which we can reject the null hypothesis"
  answer: 2
  explanation: "Cohen's d = (μ₁ − μ₂) / σ_pooled standardizes the difference by the pooled standard deviation, expressing 'how many standard deviations apart are the two groups?' This magnitude measure does not change with sample size. A p-value answers 'how unlikely is this data under the null?' — which depends heavily on n. Cohen's d answers 'how large is the effect?' — which is independent of how many people you measured."

- question: "A study can produce a statistically significant result (p < 0.05) even when the true effect size is negligibly small."
  type: true-false
  answer: true
  explanation: "Statistical significance depends on both effect size and sample size. With a large enough sample, even an infinitesimally small effect will eventually achieve significance — the test has enough power to detect essentially any departure from zero. A study with n = 10,000,000 could find p < 0.001 for an effect of d = 0.001, which is practically invisible. Reporting only the p-value can therefore be deeply misleading without an accompanying effect size."

- question: "A p-value of 0.001 tells us that the observed effect is large enough to be practically important."
  type: true-false
  answer: false
  explanation: "P-values and effect sizes measure entirely different things. A p-value of 0.001 tells us there is very strong evidence against the null hypothesis — it says nothing about the size of the effect. The effect could be real but minuscule (d = 0.01) and still yield a tiny p-value given sufficient sample size. Practical importance depends on effect size, not on how confident we are that an effect exists."

- question: "Why is it insufficient to report only a p-value when presenting hypothesis test results? What additional information is needed, and what does it tell us?"
  type: short-answer
  answer: "A p-value only answers 'are we confident the effect isn't zero?' It says nothing about how large the effect is. An effect size measure (such as Cohen's d, r, or R²) answers 'how large is the effect, and does it matter?' The p-value establishes that an effect exists; the effect size establishes whether it is worth caring about. Together they provide a complete picture: confident it's real (p-value) and knowing whether it's meaningful (effect size)."
  explanation: "A drug that achieves p < 0.001 with d = 0.03 has a real but clinically useless effect; prescribing it based on the p-value alone would be a mistake. Conversely, a study with d = 1.5 and p = 0.09 found a potentially large effect that the small sample couldn't confirm at conventional thresholds — dismissing it as 'not significant' would also be wrong. Neither piece of information is complete without the other."
```

## Explainer

From your study of **p-values**, you know that a small p-value means "this result would be unlikely if the null hypothesis were true" — it is evidence against chance. What p-values do not tell you is how *large* the difference is. Statistical significance is about confidence; **effect size** is about magnitude. These are completely separate questions, and confusing them is one of the most consequential errors in applied statistics.

Here is the core problem: with a large enough sample, even a trivially small difference becomes statistically significant. Suppose you test whether two drugs differ in blood pressure reduction. With n = 1,000,000 patients per group, you might detect a difference of 0.1 mmHg at p < 0.001 — a result that is undeniably real but clinically meaningless (blood pressure fluctuates more than that just from sitting up). The p-value is telling you the data is nearly impossible under the null hypothesis; it says nothing about whether the difference matters.

**Cohen's d** is the standard effect size measure for comparing two means: d = (μ₁ − μ₂) / σ_pooled. Dividing by the pooled standard deviation standardizes the difference, putting it in units of "standard deviations apart." Cohen's rough guidelines — small: d ≈ 0.2, medium: d ≈ 0.5, large: d ≈ 0.8 — give reference points, though appropriate effect sizes vary by field. A study finding d = 0.05 with p = 0.001 has detected a real but negligible effect. A study finding d = 1.2 with p = 0.08 has found a potentially large effect that the sample was too small to confirm at conventional significance levels. Both situations call for different responses, and you cannot distinguish them by looking at the p-value alone.

Other effect size measures suit different situations. For a single-sample proportion test, report the proportion itself. For a two-way contingency table, use **Cramér's V**. For a correlation, the **correlation coefficient r** is already an effect size (r² is the proportion of variance explained). For regression, **R²** plays the same role. The common thread: all effect sizes express the size of a finding in terms that do not depend on sample size. Reporting both a p-value and an effect size is now standard practice in medicine, psychology, and other empirical sciences — the p-value answers "are we sure there is an effect?" and the effect size answers "is the effect worth caring about?" Neither question is complete without the other.
