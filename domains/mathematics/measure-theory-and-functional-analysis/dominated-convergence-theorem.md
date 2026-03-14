---
id: dominated-convergence-theorem
title: Dominated Convergence Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-general-definition
  type: hard
builds-toward:
- lp-space-completeness-riesz-fischer
tags:
- convergence-theorems
stage: abstract-reasoning
status: draft
---

# Dominated Convergence Theorem

## Core Idea
If fₙ → f pointwise a.e. and |fₙ| ≤ g with ∫g < ∞, then ∫fₙ → ∫f. This is the most powerful convergence theorem, requiring only pointwise a.e. convergence and an integrable dominating function.

## How It's Best Learned
Apply to sequences shrinking to zero outside growing intervals, or bounded sequences on finite-measure sets.

## Common Misconceptions
The dominating function must be integrable; |fₙ| ≤ g pointwise is insufficient if ∫g = ∞. Without a dominating function, DCT does not apply.
