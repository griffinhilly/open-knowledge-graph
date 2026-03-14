---
id: interchange-limit-derivative
title: Interchange of Limit and Derivative
domain: mathematics
course: real-analysis
prerequisites:
- id: uniform-convergence-functions
  type: hard
- id: rigorous-derivative-definition
  type: hard
builds-toward:
- uniform-convergence-power-series
tags:
- limit-derivative
- interchange
- convergence
stage: abstract-reasoning
status: draft
---

# Interchange of Limit and Derivative

## Core Idea
If (fₙ) is a sequence of differentiable functions such that (fₙ') converges uniformly and (fₙ) converges pointwise, then (fₙ) converges uniformly to f, and lim fₙ' = f'. This is a deep result: passing limits through derivatives requires uniform convergence of derivatives, not just the original functions. It enables term-by-term differentiation of power series.
