---
id: hypothesis-testing-framework-theory
title: 'Hypothesis Testing: Framework and Logic'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability-fundamentals
  type: hard
builds-toward:
- z-test-for-means
- chi-square-test
tags:
- hypothesis-testing
stage: formal-systems
status: draft
---

# Hypothesis Testing: Framework and Logic

## Core Idea
Test H₀ vs H₁. Compute test statistic under H₀. P-value=P(statistic this extreme or more|H₀ true). Reject H₀ if p<α; fail to reject otherwise. Significance level α controls Type I error. Logical structure: assume H₀ true, ask if data are surprising.

## Questions

```yaml
- question: "A researcher obtains p = 0.03 and states: 'There is a 3% probability that the null hypothesis is true.' What is wrong with this interpretation?"
  type: multiple-choice
  options:
    - "Nothing — this is the correct definition of the p-value"
    - "The p-value is P(observing data this extreme or more extreme | H₀ is true), not P(H₀ is true | data). The researcher has reversed the conditioning."
    - "The error is using 0.03 instead of 1 − 0.03 = 0.97 as the probability"
    - "The p-value only measures probability under the alternative hypothesis, not the null"
  answer: 1
  explanation: "This is the most important and most common misinterpretation of p-values. The p-value conditions on H₀ being true and asks how probable the observed data (or more extreme data) would be. It says nothing directly about the probability of H₀ itself. P(H₀ | data) is a Bayesian posterior probability that requires a prior; the frequentist p-value is P(data | H₀). Confusing these is called the 'prosecutor's fallacy' or the 'base rate neglect' error."

- question: "A study with significance level α = 0.05 obtains p = 0.08. Which conclusion is correct?"
  type: multiple-choice
  options:
    - "Accept H₀ — the data confirm the null hypothesis"
    - "Reject H₀ — the p-value is close enough to 0.05 to be practically significant"
    - "Fail to reject H₀ — the data are consistent with H₀, though this does not prove H₀ is true"
    - "Reject H₁ — the alternative hypothesis has been disproved"
  answer: 2
  explanation: "When p ≥ α, the correct language is 'fail to reject H₀,' never 'accept H₀.' Failing to reject means the data are consistent with H₀ — not that H₀ is true or confirmed. H₀ could be false but the study lacked sufficient power to detect the effect. 'Accept H₀' is wrong because hypothesis testing cannot prove a null hypothesis; it can only provide evidence against it. The distinction matters practically: a study with low power may 'fail to reject' a false H₀ frequently."

- question: "A p-value of 0.04 means there is a 96% probability that the alternative hypothesis H₁ is correct."
  type: true-false
  answer: false
  explanation: "The p-value does not measure the probability that any hypothesis is true or false. It is P(data this extreme or more | H₀ true) — a statement about how surprising the data are under H₀, not a statement about the probability of H₀ or H₁. The probability that H₁ is correct would require Bayesian methods and a prior probability for H₁. This misconception is extremely common and leads to overconfidence in the strength of statistical evidence."

- question: "Lowering the significance level α from 0.05 to 0.01 reduces the Type I error rate but also reduces the probability of detecting a true effect (statistical power)."
  type: true-false
  answer: true
  explanation: "Type I error (false positive) is the probability of rejecting a true H₀, and its rate is controlled by α — lower α means fewer false positives. However, making α smaller also moves the rejection threshold farther into the tail, so smaller effects that are genuinely real become harder to detect. Power = 1 − P(Type II error) decreases as α decreases, for fixed sample size and true effect size. The two error types trade off: you cannot simultaneously minimize both without increasing sample size."

- question: "Explain the logical structure of hypothesis testing: why does a very small p-value lead to rejecting H₀, and what does 'failing to reject' H₀ actually mean?"
  type: short-answer
  answer: "Hypothesis testing works like proof by contradiction. You assume H₀ is true and derive the distribution of a test statistic under that assumption. The p-value is the probability of observing data as extreme as yours if H₀ were true. A very small p-value means: 'If H₀ were true, what we observed would be extremely unlikely.' This undermines the assumption — just as a contradiction undermines an assumed premise. 'Failing to reject' means the data are not sufficiently surprising under H₀ to warrant rejecting it; it does not mean H₀ is true, only that the evidence against it is insufficient."
  explanation: "The asymmetry of the logic is important: we can gather strong evidence against H₀ (very small p-value) but we can never gather evidence that definitively proves H₀. This is why 'fail to reject' — not 'accept' — is the correct language when p ≥ α. Low power makes false negatives more likely, so absence of significance is not evidence of absence of effect."
```

## Explainer

Your prerequisite is **conditional probability**: P(A|B) = P(A ∩ B)/P(B). Hypothesis testing is built on exactly this idea, but the conditioning runs in a direction that can be disorienting at first. The p-value is P(data this extreme | H₀ true) — you condition on the hypothesis being true and ask how surprising the data are. This is *not* P(H₀ true | data), which is what you might intuitively want. Understanding this distinction is the most important conceptual move in the entire framework.

The logical structure is an analogy to proof by contradiction. You begin by assuming the **null hypothesis** H₀ (typically "no effect," "no difference," or some baseline claim). Under this assumption, you know — or can derive — the distribution of a **test statistic**, a number computed from the data that measures how far results are from what H₀ predicts. You then compute the **p-value**: the probability, under H₀, of observing a test statistic as extreme as yours or more extreme. If the p-value is tiny, the data would be very surprising if H₀ were true — this undermines H₀'s credibility, just as a contradiction undermines an assumption in a proof.

The **significance level** α is the threshold you set in advance. If p < α, you **reject H₀** and conclude the data are inconsistent with it. If p ≥ α, you **fail to reject H₀** — not "accept it," because a large p-value only means the data are *consistent* with H₀, not that H₀ is proven true. The choice α = 0.05 is conventional: you accept a 5% chance of rejecting H₀ when it is actually true. This is the **Type I error rate** (false positive rate). Smaller α reduces false positives but makes it harder to detect real effects.

The complementary error is **Type II error**: failing to reject H₀ when H₁ is actually true (a false negative). The probability of correctly detecting a real effect is called **power** = 1 - P(Type II error). These two error types trade off: making α smaller reduces Type I error but increases Type II error, reducing power. For a fixed α, power increases with sample size (more data makes real effects easier to detect) and with the size of the true effect. A complete understanding of any hypothesis test requires specifying both error rates — statistical significance at α = 0.05 only tells you about Type I error, and a "significant" result with low power may be rejecting H₀ for the wrong reasons.
