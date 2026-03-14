---
id: dominated-convergence-theorem
title: Dominated Convergence Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: fatou-lemma
  type: hard
builds-toward:
- lp-completeness
tags:
- convergence-theorems
stage: advanced
status: draft
---

# Dominated Convergence Theorem

## Core Idea
If (fₙ) converges pointwise to f and every |fₙ| ≤ g with ∫g dμ < ∞, then ∫fₙ dμ → ∫f dμ. This is the most practical convergence result, requiring only a dominating integrable function.
