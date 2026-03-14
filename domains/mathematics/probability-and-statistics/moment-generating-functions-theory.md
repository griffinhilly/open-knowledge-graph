---
id: moment-generating-functions-theory
title: Moment Generating Functions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: variance-standard-deviation
  type: hard
- id: natural-logarithm-and-e
  type: soft
builds-toward:
- binomial-distribution-theory
- normal-distribution-theory
tags:
- mgf
- moments
stage: formal-systems
status: draft
---

# Moment Generating Functions

## Core Idea
MGF M(t)=E[e^{tX}] uniquely determines a distribution (when it exists). The n-th moment is M^{(n)}(0)=E[X^n]. MGFs simplify finding moments, proving distribution properties, and establishing convergence. Matching MGFs implies identical distributions.
