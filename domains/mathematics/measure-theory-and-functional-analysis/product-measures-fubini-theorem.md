---
id: product-measures-fubini-theorem
title: Product Measures and Fubini's Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-measure-euclidean-space
  type: hard
- id: lebesgue-integral
  type: hard
builds-toward:
- fourier-series-lp-theory
tags:
- product-measures
- integration
stage: advanced
status: draft
---

# Product Measures and Fubini's Theorem

## Core Idea
The product of two σ-finite measure spaces has a natural product measure. Fubini's theorem guarantees that integrable functions on product spaces can be iterated: ∫∫f dμ dν = ∫(∫f(x,y) dν(y)) dμ(x).
