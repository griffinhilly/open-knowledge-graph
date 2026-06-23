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
- id: standard-error-of-estimators
  type: soft
builds-toward:
- p-values-and-significance
tags:
- hypothesis-testing
- inference
- framework
stage: formal-systems
status: validated
---

# Hypothesis Testing: Framework and Logic

## Core Idea
Hypothesis testing has two competing hypotheses: null (H₀, no effect) and alternative (H₁). We calculate a test statistic and p-value to decide whether data provides sufficient evidence against H₀. The test controls Type I error rate (α).

## How It's Best Learned
Set up hypotheses for various research questions. Understand the asymmetry: we test H₀, not H₁. Recognize that 'fail to reject H₀' ≠ 'H₀ is true'. Practice interpreting p-values correctly.

## Common Misconceptions
Thinking p-value is P(H₀|data); it's P(data|H₀). Interpreting failure to reject as acceptance of H₀. Believing small p-value proves large effect size. Confusing α (Type I error) with p-value.

## Questions

```yaml
- question: "A researcher tests whether a new drug reduces blood pressure and finds p = 0.02 with α = 0.05. Which interpretation is correct?"
  type: multiple-choice
  options:
    - "There is a 2% chance the drug has no effect — the p-value is the probability H₀ is true"
    - "If the drug truly had no effect, there is only a 2% chance of observing data this extreme or more extreme"
    - "The researcher can be 98% confident the drug is effective"
    - "The drug reduces blood pressure in 98% of patients"
  answer: 1
  explanation: "The p-value is P(data this extreme | H₀ true) — a conditional probability with H₀ in the condition. It is NOT P(H₀ true | data). Option A is the most common and consequential misinterpretation of p-values. The p-value tells you how surprising your data would be in a world where the null is true, not how likely the null is to be true given your data."

- question: "A study comparing two teaching methods finds p = 0.30, with α = 0.05. The researchers fail to reject H₀. What is the most accurate conclusion?"
  type: multiple-choice
  options:
    - "The null hypothesis is proven true — the two methods are equally effective"
    - "The alternative hypothesis is false"
    - "The data are not surprising enough under H₀ to cross the pre-set rejection threshold"
    - "The study was conducted incorrectly and should be repeated"
  answer: 2
  explanation: "Failing to reject H₀ is not the same as proving H₀ true. The data are simply insufficiently surprising under H₀ — the result is consistent with both H₀ being true and H₀ being false but the study being underpowered. This asymmetry is fundamental: hypothesis tests can produce evidence against H₀, but 'no evidence against' is not the same as 'evidence for.'"

- question: "A p-value of 0.03 means there is a 3% chance the null hypothesis is true."
  type: true-false
  answer: false
  explanation: "This is the single most common p-value misinterpretation. The p-value is P(observing data this extreme or more | H₀ is true) — it conditions on H₀ being true. Computing P(H₀ is true | data) requires knowing the prior probability of H₀, which the frequentist hypothesis testing framework does not provide. The p-value tells you how unusual your data are under H₀, not how likely H₀ is."

- question: "The significance level α must be chosen before seeing the data, not after, in order to maintain a valid Type I error rate."
  type: true-false
  answer: true
  explanation: "Choosing α after seeing the data — for example, setting α = 0.06 to just barely reject a null you already know produced p = 0.05 — is a form of p-hacking that inflates the true Type I error rate above the nominal α. The error-rate guarantee of hypothesis testing only holds when the decision rule is fixed independently of the data. Pre-registration of α is the mechanism that prevents this form of circular reasoning."

- question: "What is a p-value, and why does it not tell you the probability that the null hypothesis is true?"
  type: short-answer
  answer: "A p-value is the probability of observing a test statistic as extreme as (or more extreme than) the one computed, assuming the null hypothesis is true. It conditions on H₀ — it tells you how surprising your data would be in a world where H₀ holds. The probability that H₀ is true given the data (P(H₀|data)) is a different quantity that requires a prior probability for H₀, which frequentist hypothesis testing does not specify."
  explanation: "The confusion arises from inverting the conditional. P(data | H₀) is what the p-value measures. P(H₀ | data) is what people want it to mean. These are related by Bayes' theorem but are not equal unless P(H₀) = P(data), which is rarely the case. Recognizing this distinction is essential for correctly interpreting any statistical test."
```

## Explainer

You understand probability distributions and sampling distributions — the idea that a statistic computed from a sample (like a sample mean x̄) follows a predictable distribution when sampling is random. Hypothesis testing uses this to answer a precise question: is the pattern in my data consistent with chance alone, or is something real going on? The framework converts a scientific question into a decision procedure with controlled error rates.

Every hypothesis test begins with two competing claims. The **null hypothesis** H₀ is the "nothing special" baseline — typically no effect, no difference, or no relationship. The **alternative hypothesis** H₁ is what you are trying to find evidence for. This setup is deliberately asymmetric: you assume H₀ is true and ask whether the data are surprising under that assumption. You never directly "test" H₁; you only ask how incompatible the observed data are with H₀. The analogy to a courtroom is useful: H₀ is innocence (the default), and you are asking whether the evidence is strong enough to convict.

Once H₀ is fixed, you compute a **test statistic** — a single number summarizing how far the observed data are from what H₀ predicts. For testing a population mean μ against a hypothesized value μ₀, the test statistic is typically (x̄ − μ₀) / (s/√n): the sample mean expressed in units of standard error. You know from sampling distributions that this quantity follows a predictable distribution (t, z, χ², F, etc.) when H₀ is true. The **p-value** is the probability, under H₀, of observing a test statistic at least as extreme as the one you computed. A small p-value means your data would be unusual if H₀ were true — not impossible, but rare enough to warrant suspicion.

The **significance level** α (commonly 0.05) is a pre-chosen threshold: if p < α, you reject H₀; otherwise, you fail to reject it. Critically, α is the **Type I error rate** — the probability of rejecting H₀ when it is actually true. You fix α before seeing the data, not after, so that the decision rule is not influenced by the outcome. A **Type II error** — failing to reject H₀ when it is actually false — is a separate concern governed by the **power** of the test. The most important misconception to avoid: the p-value is P(data this extreme | H₀ true), a conditional probability with H₀ in the condition. It is not P(H₀ true | data). Failing to reject H₀ does not mean H₀ is true — it only means the data are not surprising enough under H₀ to cross the threshold you set.
