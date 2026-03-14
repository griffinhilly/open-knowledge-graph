---
id: weierstrass-m-test
title: Weierstrass M-Test
domain: mathematics
course: real-analysis
prerequisites:
- id: uniform-convergence-functions
  type: hard
- id: series-convergence-rigorous
  type: hard
builds-toward:
- uniform-convergence-power-series
tags:
- weierstrass-m-test
- uniform-convergence
- series
stage: abstract-reasoning
status: draft
---

# Weierstrass M-Test

## Core Idea
If |fₙ(x)| ≤ Mₙ for all x in a set S and all n, and if ∑Mₙ converges, then ∑fₙ(x) converges uniformly on S. This is the workhorse for proving uniform convergence of series without explicit calculation. It applies to power series, Fourier series, and integral representations.
