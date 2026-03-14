---
id: lebesgue-integral-general-definition
title: 'Lebesgue Integral: General Definition'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-non-negative
  type: hard
builds-toward:
- lebesgue-integral-properties
- riemann-vs-lebesgue-integrals
- dominated-convergence-theorem
tags:
- integration
- lebesgue-integral
stage: abstract-reasoning
status: draft
---

# Lebesgue Integral: General Definition

## Core Idea
For general measurable f, decompose f = f⁺ - f⁻ (positive and negative parts). If at least one of ∫f⁺ or ∫f⁻ is finite, define ∫f dμ = ∫f⁺ - ∫f⁻. Functions with ∫|f| < ∞ are integrable. This preserves linearity for signed functions.
