---
id: type-i-type-ii-error-tradeoffs
title: Type I and Type II Error Trade-offs in Decision Making
domain: psychology
course: research-methods-psychology
prerequisites:
- id: inferential-statistics-psychology
  type: hard
builds-toward:
- multiple-comparisons-and-corrections
tags:
- statistics
- errors
- decision
stage: formal-systems
status: draft
---

# Type I and Type II Error Trade-offs in Decision Making

## Core Idea
Type I errors (false positives) reject a true null hypothesis; Type II errors (false negatives) fail to reject a false null hypothesis. These errors are inversely related: lowering the threshold for Type I error increases Type II error risk. Research design choices (sample size, effect size magnitude, alpha level) involve explicit trade-offs between false positive and false negative risks guided by research context.

## Explainer

From inferential statistics, you know that hypothesis testing produces a binary decision — reject or fail to reject the null — and that this decision is made by comparing a test statistic to a threshold set by α. The threshold is a choice, and like all choices, it has consequences in both directions. Setting α = .05 means you accept a 5% chance of rejecting a true null hypothesis. But that choice has a less visible flip side: it also determines how often you *miss* real effects.

A **Type I error** (false positive) occurs when you conclude an effect exists when it does not. The null hypothesis is actually true — there is no difference, no relationship — but your sample's data, through random variation, produced a test statistic that crossed the threshold. Your Type I error rate is directly controlled by α: it is exactly the probability you set. A **Type II error** (false negative) occurs when a real effect exists but you fail to detect it. The null is false, but your data didn't reach the threshold. The Type II error rate is β, and statistical **power** (1 − β) is the probability of detecting a real effect when one exists. The two errors are inversely related through the threshold: a stricter α (say, .01) means fewer false positives, but the narrower rejection region also misses more real effects, increasing β.

The tradeoff is not abstract — it has stakes that vary by context. Consider a screening test for a rare but serious disease. A **Type I error** means a healthy person is told they might be sick — unnecessary anxiety, follow-up tests, possible invasive procedures. A **Type II error** means a sick person is cleared — they don't receive treatment they need, and the disease progresses. Which error is worse? In this context, most people would rather risk false positives than miss real cases, so the threshold should be set to favor sensitivity (low α for the null that the person is healthy). Now flip to a drug trial: a **Type I error** means approving an ineffective drug, which patients take instead of effective treatments. A **Type II error** means rejecting an effective drug, denying benefit to patients. The relative costs shift again. There is no universally correct α — it is a value judgment about the relative costs of the two error types.

The key lever that reduces *both* errors simultaneously is **sample size**. Larger samples reduce random sampling error, making the test more sensitive to real effects (higher power) without changing α. This is why power analysis is a design requirement, not optional. If a study is underpowered — too small to detect a reasonable effect — a null result is nearly uninformative: you couldn't have detected the effect even if it was there. The critical distinction is between **absence of evidence** and **evidence of absence**. A p > .05 in a well-powered study is informative; a p > .05 in a study with 30 participants detecting a small effect tells you almost nothing. Learning to ask "what was the power of this test?" before interpreting a null result is one of the most important skills in reading psychological research.
