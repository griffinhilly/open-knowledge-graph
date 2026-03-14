---
id: rigorous-derivative-definition
title: Rigorous Definition of the Derivative
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
- id: limit-laws
  type: soft
builds-toward:
- mean-value-theorem-rigorous
- taylors-theorem-remainder
- interchange-limit-derivative
tags:
- derivative
- definition
- rigor
stage: abstract-reasoning
status: draft
---

# Rigorous Definition of the Derivative

## Core Idea
The derivative f'(c) is defined rigorously as lim_{h→0} [f(c+h) - f(c)]/h, where the limit is in the ε-δ sense: for every ε > 0, there exists δ > 0 such that |h| < δ (h ≠ 0) implies |[f(c+h) - f(c)]/h - f'(c)| < ε. This definition generalizes to higher dimensions and abstract spaces, making it the standard in modern analysis.
