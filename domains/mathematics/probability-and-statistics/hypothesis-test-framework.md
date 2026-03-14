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
