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
status: draft
---

# Type I and Type II Errors and Power

## Core Idea
Type I error (α)=P(reject H₀|H₀ true). Type II error (β)=P(fail to reject|H₁ true). Power=1−β=P(reject|H₁ true). Larger samples and larger effect sizes increase power. α and β tradeoff: reducing α increases β for fixed n.

## Explainer

From the hypothesis testing framework you already know, a test works by rejecting H₀ when a test statistic falls into a rejection region. The rejection region is chosen before seeing data. But nature presents two possible realities — H₀ is true, or H₁ is true — and no matter how careful you are, there are two distinct ways a test can be wrong. A **Type I error** is a false positive: you reject a null hypothesis that was actually true. A **Type II error** is a false negative: you fail to reject a null hypothesis that was actually false. Both errors are real risks, and the framework forces you to confront the tradeoff between them explicitly.

Think of it like a medical diagnostic test. A Type I error is diagnosing a healthy patient with a disease (false alarm). A Type II error is missing a disease that's really there (missed detection). The **significance level α** is the probability you're willing to tolerate for the false alarm; the quantity **β** is the probability of the missed detection. The **power** of a test, 1 − β, is the probability that the test correctly detects a real effect. High-power tests are sensitive; low-power tests often miss what they're looking for.

The tradeoff becomes concrete when you think geometrically. For a fixed distribution of the test statistic under H₀, making the rejection region smaller (stricter α) pushes the critical value further into the tail, which unavoidably *includes* more of the H₁ distribution in the non-rejection region — raising β and lowering power. There is no free adjustment that simultaneously shrinks both error rates without increasing the sample size. The only way to have both small α and small β (high power) is to collect more data, because larger samples make the sampling distributions narrower and easier to separate.

**Effect size** — how far the true parameter is from the null value — also drives power. A large true difference between H₀ and H₁ is inherently easier to detect; even a modest sample gives good power. A small effect size requires a large sample to distinguish from noise. In practice, a **power analysis** is done before collecting data: given a desired α, a target power (commonly 0.80 or 0.90), and an estimated effect size, it calculates the minimum sample size required. This is why understanding the α-β-power-n relationship matters beyond exam formulas — it directly governs the design of every experiment you will ever run.


