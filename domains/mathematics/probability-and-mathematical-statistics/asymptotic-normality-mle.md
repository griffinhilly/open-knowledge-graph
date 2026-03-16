---
id: asymptotic-normality-mle
title: Asymptotic Normality of MLEs
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: consistency-of-estimators
  type: hard
- id: central-limit-theorem-rigorous
  type: hard
- id: fisher-information
  type: hard
builds-toward:
- umvue
- confidence-intervals-rigorous-theory
tags:
- asymptotic-normality
- mle
- asymptotics
stage: advanced
status: draft
---

# Asymptotic Normality of MLEs

## Core Idea
Under regularity conditions, √n(θ̂ₙ - θ) converges in distribution to N(0, 1/I(θ)), where I(θ) is Fisher information. This shows MLEs are asymptotically normal and efficient (achieving the Cramer-Rao bound asymptotically). Asymptotic normality enables hypothesis tests and confidence intervals for MLEs.
