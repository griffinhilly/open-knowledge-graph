---
id: pointwise-convergence-functions
title: Pointwise Convergence of Function Sequences
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
- id: function-notation-review
  type: soft
builds-toward:
- uniform-convergence-functions
- uniform-convergence-preserves-continuity
tags:
- function-sequences
- pointwise
- convergence
stage: advanced
status: draft
---

# Pointwise Convergence of Function Sequences

## Core Idea
A sequence of functions (fₙ) converges pointwise to f if for every x and every ε > 0, there exists N (depending on both x and ε) such that n > N implies |fₙ(x) - f(x)| < ε. This is the weakest notion of convergence for functions. Pointwise limits can have surprising properties: a sequence of continuous functions can converge pointwise to a discontinuous function.
