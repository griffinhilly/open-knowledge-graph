---
id: cauchy-sequences-completeness
title: Cauchy Sequences and Completeness
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
- id: completeness-axiom
  type: hard
builds-toward:
- uniform-convergence
- interchange-limit-integral
tags:
- cauchy
- convergence
- completeness
- metric
stage: abstract-reasoning
status: draft
---

# Cauchy Sequences and Completeness

## Core Idea
A sequence is Cauchy if for every ε > 0, there exists N such that for all m, n > N, |aₘ − aₙ| < ε. In ℝ, a sequence converges if and only if it is Cauchy. This characterization is crucial because it describes convergence without knowing what the limit is, making it invaluable for proving existence of limits.
