---
id: type-i-type-ii-errors-tradeoff
title: Type I and Type II Errors and Power
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: type-i-and-type-ii-errors
  type: hard
builds-toward:
- power-and-sample-size
tags:
- hypothesis-testing
- errors
- power
stage: formal-systems
status: draft
---

# Type I and Type II Errors and Power

## Core Idea
Type I error (α) is rejecting H₀ when it's true; Type II error (β) is failing to reject H₀ when H₁ is true. Power = 1 - β is the ability to detect a true effect. These errors trade off: decreasing α typically increases β. Sample size and effect size influence power.

## How It's Best Learned
Visualize error regions under both null and alternative distributions. Calculate power using software. Explore how sample size and effect size change the tradeoff between error types.

## Common Misconceptions
Confusing Type I and Type II errors. Thinking we can minimize both errors simultaneously without changing sample size. Assuming α and β are equally important in all contexts.

## Explainer

Picture two overlapping distributions: one showing what test statistics look like when H₀ is true, and another showing what they look like when some specific alternative H₁ is true. Your significance threshold α draws a vertical line. Everything to the right of that line gets labeled "reject H₀." **Type I error** (rate α) is the probability that a statistic from the null distribution falls to the right of the line anyway — a false alarm. **Type II error** (rate β) is the probability that a statistic from the alternative distribution falls to the left of the line — a miss. **Power** (1 − β) is the probability that a statistic from the alternative distribution correctly lands on the rejection side.

The tradeoff is immediate once you visualize it: if you move the threshold to the right to make false alarms rarer (lower α), more of the alternative distribution now falls on the "accept" side, so β increases and power falls. If you move the threshold left to catch more true effects (lower β, higher power), you also admit more of the null distribution into the rejection region, inflating α. You cannot simultaneously reduce both error types by adjusting the threshold — with fixed distributions, they move in opposite directions.

The escape from this tradeoff is **sample size**. A larger sample makes both distributions narrower and more separated, so the overlap between them shrinks. With enough data, you can achieve low α and high power simultaneously — the distributions are far apart enough that the threshold line sits in a gap between them rather than in a region of overlap. This is why power analysis before a study matters: it asks "how many observations do I need so that both error types are acceptably small?"

The relative costs of the two errors depend on context, and the right balance is a substantive judgment, not a statistical one. In medical screening, false negatives (missing a disease) may be catastrophic, so you accept a higher false positive rate to ensure near-perfect sensitivity. In criminal justice, the norm is "beyond reasonable doubt" — accepting many false negatives to keep false positives (wrongful convictions) very rare. **Effect size** also matters: a small true effect means the alternative distribution is only slightly shifted from the null, creating heavy overlap and requiring large samples to achieve adequate power. Understanding this geometry — two distributions, one threshold, and the four cells it creates — gives you a principled mental model for every inference decision you will encounter.


