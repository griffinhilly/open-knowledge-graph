---
id: monotone-convergence-theorem-analysis
title: Monotone Convergence Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-non-negative
  type: hard
builds-toward:
- fatou-lemma-measure-theory
- dominated-convergence-theorem
tags:
- convergence-theorems
stage: abstract-reasoning
status: draft
---

# Monotone Convergence Theorem

## Core Idea
If 0 ≤ fₙ ≤ f_{n+1} pointwise for all n and fₙ → f, then ∫fₙ dμ → ∫f dμ. This is the most fundamental convergence theorem for the Lebesgue integral, allowing us to interchange limit and integral under monotonicity.
