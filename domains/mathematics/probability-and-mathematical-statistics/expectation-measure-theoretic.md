---
id: expectation-measure-theoretic
title: Expectation (Measure-Theoretic)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: distribution-functions-densities-rigorous
  type: hard
- id: expected-value
  type: soft
builds-toward:
- variance-higher-moments-rigorous
- conditional-expectation
- convergence-in-lp
tags:
- expectation
- integration
- measure-theory
stage: advanced
status: draft
---

# Expectation (Measure-Theoretic)

## Core Idea
The expectation E[X] = ∫_Ω X dP is defined as a Lebesgue integral with respect to the probability measure P, generalizing the Riemann integral definition. For X to have finite expectation, ∫_Ω |X| dP < ∞. The monotone convergence theorem and dominated convergence theorem characterize when expectations of limits equal limits of expectations.

## How It's Best Learned
Compare Riemann and Lebesgue expectations. Work examples where exchanging limits and integrals is justified (or not). Apply monotone and dominated convergence theorems.

## Common Misconceptions
- Thinking Riemann and Lebesgue integrals always coincide; they differ on sets of measure zero. - Assuming E[lim Xₙ] = lim E[Xₙ] without verifying conditions. - Forgetting that X must be integrable; finite mean is not automatic.
