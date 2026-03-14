---
id: method-of-moments
title: Method of Moments Estimation
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: expectation-measure-theoretic
  type: hard
- id: weak-law-of-large-numbers
  type: soft
builds-toward:
- consistency-of-estimators
tags:
- method-of-moments
- estimation
- empirical-moments
stage: abstract-reasoning
status: draft
---

# Method of Moments Estimation

## Core Idea
Method of moments estimators set sample moments m̂_k equal to population moments E[X^k] and solve for parameters. For example, if X ~ Gamma(α, β) with E[X] = α/β and E[X²] = (α+α²)/β², this yields estimators of α and β. MoM estimators are consistent but often less efficient than MLEs; they are computationally simple.
