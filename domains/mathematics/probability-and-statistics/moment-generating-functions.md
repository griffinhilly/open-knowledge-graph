---
id: moment-generating-functions
title: Moment Generating Functions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value
  type: hard
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- central-limit-theorem-theory
tags:
- mgf
- probability
- moments
stage: formal-systems
status: draft
---

# Moment Generating Functions

## Core Idea
The moment generating function is M(t) = E[e^{tX}]. Its derivatives at t=0 give moments: M^{(n)}(0) = E[X^n]. MGFs uniquely determine distributions and are useful for finding distributions of sums of random variables.

## How It's Best Learned
Calculate MGFs for simple distributions like Bernoulli and exponential. Use MGFs to find moments without direct integration. Compare MGFs of related distributions to understand relationships.

## Common Misconceptions
Forgetting that MGFs only exist for distributions with appropriate moment conditions. Confusing MGF with characteristic function. Not recognizing that MGF uniqueness determines uniqueness of distributions.
