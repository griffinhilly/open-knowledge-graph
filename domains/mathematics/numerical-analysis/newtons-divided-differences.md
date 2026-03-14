---
id: newtons-divided-differences
title: Newton's Divided Differences
domain: mathematics
course: numerical-analysis
prerequisites:
- id: lagrange-polynomial-interpolation
  type: hard
builds-toward:
- interpolation-error-analysis
tags:
- divided-differences
- newton-polynomial
- efficiency
stage: advanced
status: draft
---

# Newton's Divided Differences

## Core Idea
Newton's divided differences provide an efficient recursive method to construct the interpolating polynomial in the form p(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + .... The coefficients are computed via a systematic table, and new points can be added without recomputing all previous coefficients, making this form superior to Lagrange for practical computation.
