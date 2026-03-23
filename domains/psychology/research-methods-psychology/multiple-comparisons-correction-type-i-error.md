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
status: validated
---

# Multiple Comparisons and Type I Error Rate Control

## Core Idea
Multiple comparisons problem occurs when researchers conduct numerous statistical tests within a single study, which inflates the family-wise Type I error rate (probability of at least one false positive) beyond the nominal alpha level. Each statistical test carries a probability of Type I error; conducting many tests mathematically increases the probability that at least one will be statistically significant by chance alone. Corrections including Bonferroni, Holm, false discovery rate (FDR), and permutation testing adjust p-values or alpha levels to maintain overall Type I error control. The appropriate severity of correction depends on whether tests are planned (confirmatory) versus exploratory.

## How It's Best Learned
Simulate running multiple independent statistical tests where the null hypothesis is true and observe how often at least one reaches statistical significance.

## Common Misconceptions
Bonferroni correction is always appropriate (actually, it can be overly conservative when tests are correlated). Multiple comparisons corrections only apply to many p-values from the same dataset (actually, any multiple tests of related hypotheses require correction).

## Questions

```yaml
- question: "A researcher runs 20 independent hypothesis tests at α = .05 and finds 2 significant results. After applying Bonferroni correction, both remain significant. A reviewer still calls the original analysis problematic. What is the reviewer's most likely concern?"
  type: multiple-choice
  options:
    - "Bonferroni correction is never valid for more than 10 simultaneous tests"
    - "Without correction, the family-wise error rate for 20 tests was approximately 64% — meaning a very high chance of at least one false positive in a universe of pure noise, before any correction was applied"
    - "Two significant results from 20 tests is exactly the 10% rate expected by chance, so both must be false positives"
    - "Bonferroni correction increases Type I error, making the surviving results less trustworthy"
  answer: 1
  explanation: "The reviewer's concern is that the original uncorrected analysis had a family-wise error rate of 1 − (1 − .05)^20 ≈ .64 — a 64% chance of at least one false positive if all nulls are true. Bonferroni correction applied afterward does bring the surviving results to a defensible threshold, but the concern may be about analytical transparency (were the corrections pre-planned?) and whether the reported results are cherry-picked. The critique is about the design and reporting, not the mathematical validity of Bonferroni itself."

- question: "A neuroimaging study tests 50,000 voxels simultaneously. The team uses Bonferroni correction to control family-wise error rate. A colleague recommends switching to FDR control. What is the main advantage of FDR in this high-dimensional setting?"
  type: multiple-choice
  options:
    - "FDR control guarantees zero false positives, while Bonferroni allows up to 5%"
    - "FDR control is less stringent — it tolerates a small proportion of false discoveries in exchange for substantially more statistical power to detect true effects across tens of thousands of tests"
    - "FDR control is more conservative than Bonferroni, providing better error control with no power cost"
    - "FDR adjusts each test's alpha upward when tests are correlated, making it more powerful than Bonferroni in all situations"
  answer: 1
  explanation: "Bonferroni at 50,000 tests requires each voxel to reach p < .05/50,000 = .000001 — an extraordinarily stringent threshold that will miss many real effects (high Type II error rate). FDR control (e.g., Benjamini-Hochberg) instead controls the expected proportion of significant results that are false positives. Accepting that perhaps 5% of reported significant voxels might be false positives dramatically lowers the required p-value threshold, recovering power to detect real signals. This tradeoff is appropriate in exploratory neuroimaging where some false positives are tolerable if many true signals are found."

- question: "When 20 independent statistical tests are conducted at α = .05 and all null hypotheses are true, the probability that at least one test yields a significant result is approximately 64%."
  type: true-false
  answer: true
  explanation: "Using the complement rule: P(at least one significant) = 1 − P(none significant) = 1 − (1 − .05)^20 = 1 − .95^20 ≈ 1 − .358 ≈ .642. This is the family-wise error rate (FWER) without any correction. It grows rapidly: 10 tests → ~40%, 30 tests → ~79%, 50 tests → ~92%. The intuition is powerful: each independent test is a separate lottery ticket with a 5% chance of a false 'win.' More tickets mean a near-certain false win eventually — even when nothing is real."

- question: "Applying a multiple comparisons correction to a selected subset of statistically significant findings is sufficient to make those findings valid, even if the researcher ran many more tests and reported only the significant ones."
  type: true-false
  answer: false
  explanation: "Multiple comparisons corrections are designed to be applied to the entire family of tests conducted. If a researcher runs 100 tests, finds 5 significant results, and then applies Bonferroni correction only to those 5, the correction is meaningless — it ignores the 95 tests that 'failed,' which were equally available to produce false positives. Selective reporting of only significant findings makes the reported p-values uninterpretable regardless of any post-hoc correction. No statistical procedure can compensate for the bias introduced by non-disclosure of the full family of tests."

- question: "Explain why Bonferroni correction becomes overly conservative when the statistical tests within a study are positively correlated with each other."
  type: short-answer
  answer: "Bonferroni correction is derived by treating all k tests as statistically independent — each as a separate, unrelated chance of a false positive. The correction divides α by k assuming the worst case: k fully independent opportunities for error. When tests are positively correlated (e.g., testing related hypotheses with overlapping participant data), a false positive in one test makes false positives in correlated tests more likely — the tests are not providing k independent chances at a false positive. The actual FWER is therefore lower than the k-independent worst case, meaning Bonferroni over-corrects. Setting the threshold at α/k demands smaller p-values than the data structure warrants, increasing Type II error (missed real effects) without proportional gain in error control."
  explanation: "Holm's step-down procedure and permutation-based corrections are less conservative alternatives that can account for test correlation. The Benjamini-Hochberg FDR procedure is entirely agnostic about correlation in its guarantee (it controls expected FDR), making it robust in many high-correlation settings like genomics."
```

## Explainer

From inferential statistics, you know that a **Type I error** — rejecting a true null hypothesis — has probability α, conventionally set at .05. This means that if the null hypothesis is genuinely true, you'll obtain a "significant" result 5% of the time purely by chance. From your work on Type I and Type II error tradeoffs, you understand that setting α defines your tolerance for false positives in a single test. The multiple comparisons problem is what happens when you apply that single-test logic across an entire family of tests — and the conditional probability calculation that drives it follows directly from the probability foundations you already have.

Suppose you run 20 independent significance tests in a single study, each at α = .05, and all null hypotheses are actually true. What is the probability that at least one test reaches significance? Use the complement rule you know from conditional probability: 1 − (1 − .05)^20 ≈ 1 − .95^20 ≈ .64. With 20 independent tests of truly null effects, you'd observe at least one "significant" result about 64% of the time — in a universe of pure noise. This inflated rate is the **family-wise error rate (FWER)**: the probability of at least one false positive across the family of tests. It grows rapidly: 10 tests yields roughly 40% FWER; 50 tests yields over 92%.

**Bonferroni correction** is the most conservative solution: divide the nominal α by the number of tests and require each individual test to reach that stricter threshold. For 20 tests, each test must clear p < .0025. This guarantees FWER ≤ .05 across the family, but at a cost: demanding much smaller p-values for each test increases the probability of Type II errors — real effects may be missed because they don't survive the heightened bar. Bonferroni assumes that all tests are independent; when tests are positively correlated (as they often are within a study, since they draw on the same participants), it becomes **overly conservative** — the actual FWER is already lower than .05 because the tests are not providing independent chances at a false positive.

The **Holm procedure** improves on Bonferroni by applying corrections sequentially. Rank your p-values from smallest to largest; compare the smallest to α/k, the second-smallest to α/(k−1), and so on, stopping when a test fails to reach its threshold. Every test that clears its step-down threshold is declared significant. Holm controls FWER as strictly as Bonferroni but is less conservative for the larger (less significant) p-values, so you recover some statistical power without sacrificing error control. For exploratory work where you are willing to tolerate a small proportion of false discoveries in exchange for more power to detect true ones, the **false discovery rate (FDR)** approach shifts the target: instead of controlling the probability of any false positive, it controls the expected proportion of significant findings that are false. The Benjamini-Hochberg procedure implements this and is standard in neuroimaging and genomics, where thousands of simultaneous tests make FWER control nearly impossible without destroying power entirely.

The underlying principle is that the right correction depends on your inferential goals and the structure of your tests. Pre-registered, theoretically motivated tests of specific hypotheses warrant less severe correction than post-hoc mining of a dataset for any significant association. When a researcher runs 50 correlations, finds 3 that survive α = .05, and reports only those 3, no correction applied to those 3 p-values can fix the problem — the issue is **selective reporting**, which makes the reported results uninterpretable regardless of what correction is applied. Multiple comparisons control is a statistical procedure that assumes honest reporting of the full family; it cannot substitute for transparency about how many tests were actually conducted.
