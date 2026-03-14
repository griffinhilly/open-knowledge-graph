---
id: fuzzy-regression-discontinuity-design
title: Fuzzy Regression Discontinuity Design
domain: economics
course: econometrics
prerequisites:
- id: regression-discontinuity
  type: hard
- id: instrumental-variables
  type: hard
tags:
- causal-inference
- regression-discontinuity
- instrumental-variables
stage: formal-systems
status: draft
---

# Fuzzy Regression Discontinuity Design

## Core Idea
In fuzzy RDD, the probability of treatment jumps discontinuously at the threshold c*, but not from 0 to 1. The running variable serves as an instrument for treatment. The estimand is the LATE (Local Average Treatment Effect) for units near the cutoff whose treatment status is affected by the discontinuity.
