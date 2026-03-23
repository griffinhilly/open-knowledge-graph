---
id: type-i-and-type-ii-errors
title: Type I and Type II Errors and Power
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-framework-theory
  type: hard
builds-toward:
- neyman-pearson-lemma
tags:
- errors
- power
stage: formal-systems
status: validated
---

# Type I and Type II Errors and Power

## Core Idea
Type I error (α)=P(reject H₀|H₀ true). Type II error (β)=P(fail to reject|H₁ true). Power=1−β=P(reject|H₁ true). Larger samples and larger effect sizes increase power. α and β tradeoff: reducing α increases β for fixed n.

## Questions

```yaml
- question: "A hospital sets an extremely strict diagnostic threshold for a rare disease (very low α, so only the most extreme test results trigger a positive diagnosis). What is the most likely consequence?"
  type: multiple-choice
  options:
    - "Fewer false positives AND fewer false negatives, since the strict threshold makes the test more accurate overall"
    - "More false positives, because the strict threshold makes the test oversensitive"
    - "More false negatives (missed cases), because the smaller rejection region is harder to enter even when the disease is present"
    - "No effect on false negatives — α only controls false positives"
  answer: 2
  explanation: "Lowering α shrinks the rejection region (moves the critical value further into the tail). This reduces false positives (good) but simultaneously pushes more of the alternative distribution H₁ into the non-rejection region — increasing β, the false negative rate. In the medical context: a test that almost never calls a healthy person sick (low α) will frequently miss patients who are genuinely sick (high β). The tradeoff is unavoidable for a fixed sample size."

- question: "A research team wants to simultaneously achieve α = 0.01 (very strict significance) and 0.95 power (very high sensitivity) without collecting additional data. Is this feasible?"
  type: multiple-choice
  options:
    - "Yes — choosing the optimal test statistic can eliminate the tradeoff between α and power"
    - "Yes — switching from a two-tailed to a one-tailed test automatically achieves both goals"
    - "No — for a fixed sample size and effect size, reducing α necessarily increases β and reduces power"
    - "No — once α is chosen, power is fixed regardless of sample size or effect size"
  answer: 2
  explanation: "For a fixed sample size and effect size, α and β are in direct tension: shrinking the rejection region to achieve α = 0.01 pushes more of the H₁ distribution into the non-rejection region, lowering power. The only way to achieve both strict α and high power is to collect more data (larger n), which narrows the sampling distributions under both H₀ and H₁, making them easier to separate."

- question: "Increasing sample size is the only design lever that can simultaneously reduce the Type I error rate and increase statistical power."
  type: true-false
  answer: true
  explanation: "For a fixed effect size and test design, α and β are linked: reducing one increases the other. Increasing sample size narrows the sampling distributions under both H₀ and H₁, allowing a stricter critical value (lower α) while keeping most of the H₁ distribution in the rejection region (lower β, higher power). Effect size is a property of reality, not a design choice; sample size is the primary lever the experimenter controls for reducing both error rates simultaneously."

- question: "A test with significance level α = 0.01 is more statistically powerful than a test with α = 0.05, all else being equal."
  type: true-false
  answer: false
  explanation: "This is exactly backwards. A stricter significance level (α = 0.01) means a smaller rejection region — the critical value is pushed further into the tail. For the same sample size and effect size, more of the H₁ distribution falls in the non-rejection region, so β increases and power (= 1 − β) *decreases*. The test with α = 0.05 has more power. Stricter α makes it harder to reject H₀ — which hurts sensitivity, not helps it."

- question: "Explain why reducing the significance level α necessarily increases the Type II error rate β, for a fixed sample size and effect size."
  type: short-answer
  answer: "Reducing α means making the rejection region smaller by moving the critical value further into the tail of the H₀ distribution. But the H₁ distribution overlaps with the H₀ distribution — the amount of overlap is fixed by sample size and effect size. A smaller rejection region means less of the H₁ distribution falls inside it, so the probability of correctly detecting a true effect (power) decreases and β = 1 − power increases. There is no free adjustment that shrinks both error rates without narrowing the distributions — which only larger n achieves."
  explanation: "Geometrically: imagine two overlapping bell curves, one centered at the null value and one at the true parameter value. The rejection region is the right tail past the critical value. Moving the boundary rightward (lower α) cuts off part of the alternative distribution that previously fell in the rejection region — that cut-off portion becomes additional β. The only fix is to make the curves narrower (larger n) or more separated (larger effect size, which isn't a design choice)."
```

## Explainer

From the hypothesis testing framework you already know, a test works by rejecting H₀ when a test statistic falls into a rejection region. The rejection region is chosen before seeing data. But nature presents two possible realities — H₀ is true, or H₁ is true — and no matter how careful you are, there are two distinct ways a test can be wrong. A **Type I error** is a false positive: you reject a null hypothesis that was actually true. A **Type II error** is a false negative: you fail to reject a null hypothesis that was actually false. Both errors are real risks, and the framework forces you to confront the tradeoff between them explicitly.

Think of it like a medical diagnostic test. A Type I error is diagnosing a healthy patient with a disease (false alarm). A Type II error is missing a disease that's really there (missed detection). The **significance level α** is the probability you're willing to tolerate for the false alarm; the quantity **β** is the probability of the missed detection. The **power** of a test, 1 − β, is the probability that the test correctly detects a real effect. High-power tests are sensitive; low-power tests often miss what they're looking for.

The tradeoff becomes concrete when you think geometrically. For a fixed distribution of the test statistic under H₀, making the rejection region smaller (stricter α) pushes the critical value further into the tail, which unavoidably *includes* more of the H₁ distribution in the non-rejection region — raising β and lowering power. There is no free adjustment that simultaneously shrinks both error rates without increasing the sample size. The only way to have both small α and small β (high power) is to collect more data, because larger samples make the sampling distributions narrower and easier to separate.

**Effect size** — how far the true parameter is from the null value — also drives power. A large true difference between H₀ and H₁ is inherently easier to detect; even a modest sample gives good power. A small effect size requires a large sample to distinguish from noise. In practice, a **power analysis** is done before collecting data: given a desired α, a target power (commonly 0.80 or 0.90), and an estimated effect size, it calculates the minimum sample size required. This is why understanding the α-β-power-n relationship matters beyond exam formulas — it directly governs the design of every experiment you will ever run.


