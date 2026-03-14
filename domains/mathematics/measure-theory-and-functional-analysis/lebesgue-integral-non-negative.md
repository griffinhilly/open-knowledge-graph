---
id: lebesgue-integral-non-negative
title: Lebesgue Integral for Non-Negative Functions
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-simple-functions
  type: hard
builds-toward:
- lebesgue-integral-general-definition
- monotone-convergence-theorem-analysis
- fatou-lemma-measure-theory
tags:
- integration
- lebesgue-integral
stage: abstract-reasoning
status: draft
---

# Lebesgue Integral for Non-Negative Functions

## Core Idea
For non-negative measurable f, define ∫f dμ = sup{∫φ dμ : φ simple, φ ≤ f}. This definition is monotone: f ≤ g implies ∫f ≤ ∫g. The integral may be infinite but is always defined.
