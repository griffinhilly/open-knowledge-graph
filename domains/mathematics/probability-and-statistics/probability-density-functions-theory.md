---
id: probability-density-functions-theory
title: Probability Density Functions and Continuous Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-definition-types
  type: hard
- id: definite-integral-definition
  type: hard
builds-toward:
- expected-value
- normal-distribution
tags:
- pdf
- continuous
stage: formal-systems
status: draft
---

# Probability Density Functions and Continuous Distributions

## Core Idea
The PDF f(x) of a continuous random variable satisfies P(a≤X≤b)=∫ₐᵇ f(x)dx. Valid PDFs satisfy f(x)≥0 and ∫f(x)dx=1. Unlike the PMF, f(x) is not a probability itself, and P(X=x)=0 for any single value. The PDF completely characterizes continuous distributions.
