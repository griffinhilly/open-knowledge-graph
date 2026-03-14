---
id: riemann-integrability-criteria
title: Criteria for Riemann Integrability
domain: mathematics
course: real-analysis
prerequisites:
- id: riemann-integral-darboux-sums
  type: hard
- id: open-closed-sets-real-line
  type: soft
builds-toward:
- properties-riemann-integral
- fundamental-theorem-calculus-rigorous
tags:
- riemann-integrability
- discontinuities
- measure-zero
stage: abstract-reasoning
status: draft
---

# Criteria for Riemann Integrability

## Core Idea
A bounded function f on [a, b] is Riemann integrable if and only if the set of discontinuities has measure zero. Equivalently, f is integrable iff for every ε > 0, there exists a partition P such that U(P) − L(P) < ε. All continuous functions are integrable; some discontinuous functions are too.
