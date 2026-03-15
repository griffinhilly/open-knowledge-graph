---
id: pointwise-convergence-function-sequences
title: Pointwise Convergence of Function Sequences
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
builds-toward:
- uniform-convergence
- interchange-limit-integral
tags:
- pointwise-convergence
- function-sequences
- limits
stage: advanced
status: draft
---

# Pointwise Convergence of Function Sequences

## Core Idea
A sequence of functions (fₙ) converges pointwise to f on a set S if for every x in S and every ε > 0, there exists N (depending on both ε and x) such that for all n > N, |fₙ(x) − f(x)| < ε. Pointwise convergence is the basic notion but can behave pathologically: limits of continuous functions need not be continuous.
