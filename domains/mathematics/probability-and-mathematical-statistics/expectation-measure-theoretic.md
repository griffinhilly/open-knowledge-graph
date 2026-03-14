---
id: expectation-measure-theoretic
title: Expectation (Measure-Theoretic Definition)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: random-variables-as-measurable-functions
  type: hard
- id: expected-value
  type: soft
- id: riemann-integral-darboux-sums
  type: soft
builds-toward:
- moment-generating-functions
- characteristic-functions
tags:
- expectation
- integration
- measure-theory
stage: abstract-reasoning
status: draft
---

# Expectation (Measure-Theoretic Definition)

## Core Idea
The expectation E[X] of a random variable X is defined as the Lebesgue integral ∫ X dP, unifying discrete sums and continuous integrals in a single framework. This definition handles singular distributions and pathological cases. Convergence theorems like dominated and monotone convergence justify swapping limits and expectations.
