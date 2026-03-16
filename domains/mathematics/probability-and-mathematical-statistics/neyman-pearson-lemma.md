---
id: neyman-pearson-lemma
title: Neyman-Pearson Lemma
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: maximum-likelihood-estimation-theory
  type: hard
- id: type-i-and-type-ii-errors
  type: soft
builds-toward:
- likelihood-ratio-tests
- uniformly-most-powerful-tests
tags:
- neyman-pearson
- hypothesis-testing
- statistics
stage: advanced
status: draft
---

# Neyman-Pearson Lemma

## Core Idea
For testing H₀: θ = θ₀ vs H₁: θ = θ₁, the most powerful test rejects H₀ when L(θ₁|X)/L(θ₀|X) > k for some k determined by the significance level. The Neyman-Pearson lemma characterizes the optimal test in terms of likelihood ratios. This is the foundation for constructing best hypothesis tests.

## Explainer

From your study of Type I and Type II errors, you know there is a fundamental tradeoff: any test that reduces false positives (Type I errors, controlled by significance level α) tends to increase false negatives (Type II errors). The question the Neyman-Pearson lemma answers is: *given* that you've fixed α, what is the most powerful test — the one that minimizes Type II errors, or equivalently maximizes the probability of correctly rejecting H₀ when H₁ is true?

The answer hinges on the **likelihood ratio**. You know from maximum likelihood estimation that L(θ | X) measures how well parameter θ explains the data X. The ratio L(θ₁ | X) / L(θ₀ | X) compares how much better the data supports H₁ versus H₀. When this ratio is large, the data is much more consistent with H₁ — strong evidence to reject H₀. The lemma says: reject when this ratio exceeds some threshold k, where k is chosen to make the Type I error exactly α. This is the **Neyman-Pearson test**, and the lemma proves it is **most powerful** among all tests of size α.

A concrete example: testing whether a coin is fair (H₀: p = 0.5) versus biased (H₁: p = 0.7) after n = 10 flips. If you observe k heads, L(0.7 | k) / L(0.5 | k) = (0.7/0.5)^k · (0.3/0.5)^(10−k). This ratio increases in k — more heads is stronger evidence for p = 0.7. The NP test rejects when k ≥ c for some critical value c. Note the structure: the optimal rejection region is simply "enough heads" — the test statistic is just the number of heads, a natural sufficient statistic. This connection between NP tests and sufficient statistics is deep and recurring.

The lemma's importance extends beyond the simple case. For **simple vs. simple** hypotheses (both θ₀ and θ₁ are single values), NP gives the uniquely optimal test. For composite hypotheses (θ₁ ranges over a set), this extends to the concept of **Uniformly Most Powerful** (UMP) tests — tests that are simultaneously most powerful against every value in the alternative. Not all testing problems admit a UMP test, but when they do, the NP framework reveals why. Understanding the NP lemma is therefore not just about one test; it is the benchmark that defines what "optimal" means in hypothesis testing and anchors all subsequent developments in the theory.
