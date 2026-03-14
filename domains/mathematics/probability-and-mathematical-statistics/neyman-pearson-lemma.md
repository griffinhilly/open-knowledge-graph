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
stage: abstract-reasoning
status: draft
---

# Neyman-Pearson Lemma

## Core Idea
For testing H₀: θ = θ₀ vs H₁: θ = θ₁, the most powerful test rejects H₀ when L(θ₁|X)/L(θ₀|X) > k for some k determined by the significance level. The Neyman-Pearson lemma characterizes the optimal test in terms of likelihood ratios. This is the foundation for constructing best hypothesis tests.
