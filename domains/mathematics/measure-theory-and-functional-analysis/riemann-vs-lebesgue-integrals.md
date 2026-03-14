---
id: riemann-vs-lebesgue-integrals
title: 'Comparison: Riemann and Lebesgue Integrals'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: riemann-integral-darboux-sums
  type: hard
- id: lebesgue-integral-general-definition
  type: hard
builds-toward:
- dominated-convergence-theorem
tags:
- integration
stage: abstract-reasoning
status: draft
---

# Comparison: Riemann and Lebesgue Integrals

## Core Idea
If a bounded function on [a,b] is Riemann integrable, it is Lebesgue integrable with equal integrals. The Lebesgue integral applies to a much broader class of functions and has superior convergence theorems (e.g., dominated convergence).

## How It's Best Learned
Show that Dirichlet's function (1 on rationals, 0 on irrationals) is Lebesgue integrable but not Riemann integrable. Understand that Lebesgue slices 'horizontally' while Riemann slices 'vertically.'

## Common Misconceptions
Lebesgue integration is not strictly stronger in existence: every Riemann integrable function is Lebesgue integrable, but the reverse is false. The real advantage is better convergence theorems.
