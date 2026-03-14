---
id: fubini-theorem
title: Fubini's Theorem and Tonelli's Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: product-measures-definition
  type: hard
- id: lebesgue-integral-general-definition
  type: hard
builds-toward:
- lp-space-completeness-riesz-fischer
tags:
- integration
- fubini-theorem
stage: abstract-reasoning
status: draft
---

# Fubini's Theorem and Tonelli's Theorem

## Core Idea
Fubini's theorem: for integrable f on X × Y, ∫∫f d(μ⊗ν) = ∫(∫f(x,y) dν(y)) dμ(x). Tonelli's version handles non-negative functions without integrability, allowing interchange of iteration under more general conditions.
