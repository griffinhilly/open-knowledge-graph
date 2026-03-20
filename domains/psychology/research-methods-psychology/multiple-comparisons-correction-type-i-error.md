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
- id: multiple-comparisons-and-corrections
  type: hard
- id: type-i-type-ii-error-tradeoffs
  type: hard
builds-toward:
- exploratory-vs-confirmatory-analysis-strategies
tags:
- statistics
- type-i-error
- multiple-comparisons
- correction
stage: formal-systems
status: draft
---

# Multiple Comparisons and Type I Error Rate Control

## Core Idea
Multiple comparisons problem occurs when researchers conduct numerous statistical tests within a single study, which inflates the family-wise Type I error rate (probability of at least one false positive) beyond the nominal alpha level. Each statistical test carries a probability of Type I error; conducting many tests mathematically increases the probability that at least one will be statistically significant by chance alone. Corrections including Bonferroni, Holm, false discovery rate (FDR), and permutation testing adjust p-values or alpha levels to maintain overall Type I error control. The appropriate severity of correction depends on whether tests are planned (confirmatory) versus exploratory.

## How It's Best Learned
Simulate running multiple independent statistical tests where the null hypothesis is true and observe how often at least one reaches statistical significance.

## Common Misconceptions
Bonferroni correction is always appropriate (actually, it can be overly conservative when tests are correlated). Multiple comparisons corrections only apply to many p-values from the same dataset (actually, any multiple tests of related hypotheses require correction).

## Explainer

From inferential statistics, you know that a **Type I error** — rejecting a true null hypothesis — has probability α, conventionally set at .05. This means that if the null hypothesis is genuinely true, you'll obtain a "significant" result 5% of the time purely by chance. From your work on Type I and Type II error tradeoffs, you understand that setting α defines your tolerance for false positives in a single test. The multiple comparisons problem is what happens when you apply that single-test logic across an entire family of tests — and the conditional probability calculation that drives it follows directly from the probability foundations you already have.

Suppose you run 20 independent significance tests in a single study, each at α = .05, and all null hypotheses are actually true. What is the probability that at least one test reaches significance? Use the complement rule you know from conditional probability: 1 − (1 − .05)^20 ≈ 1 − .95^20 ≈ .64. With 20 independent tests of truly null effects, you'd observe at least one "significant" result about 64% of the time — in a universe of pure noise. This inflated rate is the **family-wise error rate (FWER)**: the probability of at least one false positive across the family of tests. It grows rapidly: 10 tests yields roughly 40% FWER; 50 tests yields over 92%.

**Bonferroni correction** is the most conservative solution: divide the nominal α by the number of tests and require each individual test to reach that stricter threshold. For 20 tests, each test must clear p < .0025. This guarantees FWER ≤ .05 across the family, but at a cost: demanding much smaller p-values for each test increases the probability of Type II errors — real effects may be missed because they don't survive the heightened bar. Bonferroni assumes that all tests are independent; when tests are positively correlated (as they often are within a study, since they draw on the same participants), it becomes **overly conservative** — the actual FWER is already lower than .05 because the tests are not providing independent chances at a false positive.

The **Holm procedure** improves on Bonferroni by applying corrections sequentially. Rank your p-values from smallest to largest; compare the smallest to α/k, the second-smallest to α/(k−1), and so on, stopping when a test fails to reach its threshold. Every test that clears its step-down threshold is declared significant. Holm controls FWER as strictly as Bonferroni but is less conservative for the larger (less significant) p-values, so you recover some statistical power without sacrificing error control. For exploratory work where you are willing to tolerate a small proportion of false discoveries in exchange for more power to detect true ones, the **false discovery rate (FDR)** approach shifts the target: instead of controlling the probability of any false positive, it controls the expected proportion of significant findings that are false. The Benjamini-Hochberg procedure implements this and is standard in neuroimaging and genomics, where thousands of simultaneous tests make FWER control nearly impossible without destroying power entirely.

The underlying principle is that the right correction depends on your inferential goals and the structure of your tests. Pre-registered, theoretically motivated tests of specific hypotheses warrant less severe correction than post-hoc mining of a dataset for any significant association. When a researcher runs 50 correlations, finds 3 that survive α = .05, and reports only those 3, no correction applied to those 3 p-values can fix the problem — the issue is **selective reporting**, which makes the reported results uninterpretable regardless of what correction is applied. Multiple comparisons control is a statistical procedure that assumes honest reporting of the full family; it cannot substitute for transparency about how many tests were actually conducted.
