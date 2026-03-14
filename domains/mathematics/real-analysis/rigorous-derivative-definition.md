---
id: rigorous-derivative-definition
title: Rigorous Definition of the Derivative
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
- id: limit-definition-of-derivative
  type: hard
builds-toward:
- mean-value-theorem-rigorous
- taylors-theorem-remainder
tags:
- derivative
- limits
- differentiability
stage: abstract-reasoning
status: draft
---

# Rigorous Definition of the Derivative

## Core Idea
A function f is differentiable at c with derivative f'(c) if the limit lim_{h→0} [f(c+h) − f(c)] / h exists and equals f'(c). This rigorous epsilon-delta formulation requires that for every ε > 0, there exists δ > 0 such that if 0 < |h| < δ, then |(f(c+h) − f(c))/h − f'(c)| < ε. Differentiability implies continuity.
