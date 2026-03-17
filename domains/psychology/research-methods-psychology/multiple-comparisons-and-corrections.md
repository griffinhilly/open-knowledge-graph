---
id: multiple-comparisons-and-corrections
title: Multiple Comparisons Problem and Correction Methods
domain: psychology
course: research-methods-psychology
prerequisites:
- id: inferential-statistics-psychology
  type: hard
- id: type-i-type-ii-error-tradeoffs
  type: soft
builds-toward:
- analysis-plan-preregistration-commitment
tags:
- statistics
- multiple-comparisons
- correction
stage: abstract-reasoning
status: draft
---

# Multiple Comparisons Problem and Correction Methods

## Core Idea
When conducting multiple statistical tests (comparing many conditions, testing multiple outcomes, exploring subgroups), the probability of false positives accumulates. Corrections like Bonferroni, false discovery rate control, or planned contrasts manage error rates but reduce statistical power. The appropriate correction depends on whether comparisons were planned a priori or exploratory post-hoc.

## Explainer

Your understanding of inferential statistics already tells you that a significance threshold of α = .05 means you accept a 5% chance of a false positive on any single test. The **multiple comparisons problem** follows directly from this: if you run 20 independent tests at α = .05 and there are truly no effects, you expect about one false positive by chance alone. The more tests you run, the more likely you are to find something that looks significant but isn't. This is the mathematical foundation of the **familywise error rate (FWER)** — the probability of making at least one Type I error across a family of tests.

The **Bonferroni correction** is the simplest solution: divide your alpha by the number of tests. If you run 20 tests, use α = .0025 per test instead of .05. This controls the FWER at .05 — the probability of any false positive across the whole family remains at most 5%. The logic is intuitive (you've made the threshold harder to clear), but the cost is real: Bonferroni is conservative when tests are correlated (as many tests of the same construct will be), and it reduces statistical power substantially. With 20 tests at α = .0025, you need a much larger effect to achieve significance, which means you'll miss more true effects (increased Type II error).

The **false discovery rate (FDR)** approach, developed by Benjamini and Hochberg, offers a different philosophical deal: instead of guaranteeing that no false positive slips through, it controls the *expected proportion* of your significant results that are false positives. An FDR of .05 means that among all findings you declare significant, about 5% are expected to be false positives. This is less stringent than FWER control, but for exploratory research generating hypotheses — rather than making confirmatory decisions — it captures the right trade-off. When exploring 200 brain regions for an effect, FDR control at .05 allows many comparisons while promising that most significant findings are probably real.

The most practically important distinction is between **planned contrasts** and **post-hoc comparisons**. If you specify, before collecting data, that you will compare exactly three conditions using two theoretically motivated contrasts, you have two tests and a coherent family — and you may not need aggressive correction. If you run an ANOVA, find overall significance, and then examine every possible pairwise comparison to find where the effect lives, you are conducting post-hoc exploration and must apply corrections (Tukey, Scheffé, or others designed for this case). The reason is not ceremonial — it is that post-hoc exploration capitalizes on chance in ways that planned contrasts do not. The honest accounting of your testing strategy, declared before data collection in a preregistration, is what determines the correct correction. The multiple comparisons problem cannot be fixed after the fact; it must be planned around.
