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

## Explainer

Your prerequisite is **conditional probability**: P(A|B) = P(A ∩ B)/P(B). Hypothesis testing is built on exactly this idea, but the conditioning runs in a direction that can be disorienting at first. The p-value is P(data this extreme | H₀ true) — you condition on the hypothesis being true and ask how surprising the data are. This is *not* P(H₀ true | data), which is what you might intuitively want. Understanding this distinction is the most important conceptual move in the entire framework.

The logical structure is an analogy to proof by contradiction. You begin by assuming the **null hypothesis** H₀ (typically "no effect," "no difference," or some baseline claim). Under this assumption, you know — or can derive — the distribution of a **test statistic**, a number computed from the data that measures how far results are from what H₀ predicts. You then compute the **p-value**: the probability, under H₀, of observing a test statistic as extreme as yours or more extreme. If the p-value is tiny, the data would be very surprising if H₀ were true — this undermines H₀'s credibility, just as a contradiction undermines an assumption in a proof.

The **significance level** α is the threshold you set in advance. If p < α, you **reject H₀** and conclude the data are inconsistent with it. If p ≥ α, you **fail to reject H₀** — not "accept it," because a large p-value only means the data are *consistent* with H₀, not that H₀ is proven true. The choice α = 0.05 is conventional: you accept a 5% chance of rejecting H₀ when it is actually true. This is the **Type I error rate** (false positive rate). Smaller α reduces false positives but makes it harder to detect real effects.

The complementary error is **Type II error**: failing to reject H₀ when H₁ is actually true (a false negative). The probability of correctly detecting a real effect is called **power** = 1 - P(Type II error). These two error types trade off: making α smaller reduces Type I error but increases Type II error, reducing power. For a fixed α, power increases with sample size (more data makes real effects easier to detect) and with the size of the true effect. A complete understanding of any hypothesis test requires specifying both error rates — statistical significance at α = 0.05 only tells you about Type I error, and a "significant" result with low power may be rejecting H₀ for the wrong reasons.
