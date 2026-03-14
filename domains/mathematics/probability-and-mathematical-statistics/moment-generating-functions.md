---
id: moment-generating-functions
title: Moment Generating Functions
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: expectation-measure-theoretic
  type: hard
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- characteristic-functions
- central-limit-theorem-rigorous
tags:
- moments
- mgf
- convergence
stage: abstract-reasoning
status: draft
---

# Moment Generating Functions

## Core Idea
The moment generating function M_X(t) = E[e^{tX}] encodes all moments: E[X^n] = M_X^{(n)}(0). MGFs uniquely determine distributions (when they exist near 0), and continuity of MGFs implies convergence in distribution. They are powerful tools for studying sums of independent random variables.
