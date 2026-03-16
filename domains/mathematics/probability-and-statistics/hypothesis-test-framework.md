---
id: hypothesis-test-framework
title: 'Hypothesis Testing: Framework and Logic'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-rules-for-events
  type: hard
- id: sampling-distributions
  type: hard
builds-toward:
- p-values-and-significance
- power-of-statistical-test
tags:
- hypothesis-testing
- inference
- framework
stage: formal-systems
status: draft
---

# Hypothesis Testing: Framework and Logic

## Core Idea
Hypothesis testing has two competing hypotheses: null (H₀, no effect) and alternative (H₁). We calculate a test statistic and p-value to decide whether data provides sufficient evidence against H₀. The test controls Type I error rate (α).

## How It's Best Learned
Set up hypotheses for various research questions. Understand the asymmetry: we test H₀, not H₁. Recognize that 'fail to reject H₀' ≠ 'H₀ is true'. Practice interpreting p-values correctly.

## Common Misconceptions
Thinking p-value is P(H₀|data); it's P(data|H₀). Interpreting failure to reject as acceptance of H₀. Believing small p-value proves large effect size. Confusing α (Type I error) with p-value.

## Explainer

You understand probability distributions and sampling distributions — the idea that a statistic computed from a sample (like a sample mean x̄) follows a predictable distribution when sampling is random. Hypothesis testing uses this to answer a precise question: is the pattern in my data consistent with chance alone, or is something real going on? The framework converts a scientific question into a decision procedure with controlled error rates.

Every hypothesis test begins with two competing claims. The **null hypothesis** H₀ is the "nothing special" baseline — typically no effect, no difference, or no relationship. The **alternative hypothesis** H₁ is what you are trying to find evidence for. This setup is deliberately asymmetric: you assume H₀ is true and ask whether the data are surprising under that assumption. You never directly "test" H₁; you only ask how incompatible the observed data are with H₀. The analogy to a courtroom is useful: H₀ is innocence (the default), and you are asking whether the evidence is strong enough to convict.

Once H₀ is fixed, you compute a **test statistic** — a single number summarizing how far the observed data are from what H₀ predicts. For testing a population mean μ against a hypothesized value μ₀, the test statistic is typically (x̄ − μ₀) / (s/√n): the sample mean expressed in units of standard error. You know from sampling distributions that this quantity follows a predictable distribution (t, z, χ², F, etc.) when H₀ is true. The **p-value** is the probability, under H₀, of observing a test statistic at least as extreme as the one you computed. A small p-value means your data would be unusual if H₀ were true — not impossible, but rare enough to warrant suspicion.

The **significance level** α (commonly 0.05) is a pre-chosen threshold: if p < α, you reject H₀; otherwise, you fail to reject it. Critically, α is the **Type I error rate** — the probability of rejecting H₀ when it is actually true. You fix α before seeing the data, not after, so that the decision rule is not influenced by the outcome. A **Type II error** — failing to reject H₀ when it is actually false — is a separate concern governed by the **power** of the test. The most important misconception to avoid: the p-value is P(data this extreme | H₀ true), a conditional probability with H₀ in the condition. It is not P(H₀ true | data). Failing to reject H₀ does not mean H₀ is true — it only means the data are not surprising enough under H₀ to cross the threshold you set.
