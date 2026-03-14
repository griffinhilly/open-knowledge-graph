---
id: lagrange-polynomial-interpolation
title: Lagrange Polynomial Interpolation
domain: mathematics
course: numerical-analysis
prerequisites: []
builds-toward:
- newtons-divided-differences
- interpolation-error-analysis
- newton-cotes-quadrature
tags:
- interpolation
- polynomial
- lagrange-basis
stage: advanced
status: draft
---

# Lagrange Polynomial Interpolation

## Core Idea
Lagrange interpolation constructs the unique polynomial of degree n-1 passing through n points using a sum of basis polynomials, each of which equals 1 at one data point and 0 at all others. This representation is elegant for theoretical work and explicit formula derivation but can suffer numerical instability for many points due to large basis polynomial oscillations.
