---
id: gaussian-quadrature
title: Gaussian Quadrature
domain: mathematics
course: numerical-analysis
prerequisites:
- id: lagrange-polynomial-interpolation
  type: hard
builds-toward:
- romberg-integration
tags:
- gaussian-quadrature
- optimal-quadrature
- weight-functions
stage: advanced
status: draft
---

# Gaussian Quadrature

## Core Idea
Gaussian quadrature optimally chooses both node locations and weights to integrate polynomials of degree up to 2n-1 exactly using only n function evaluations. Nodes are roots of orthogonal polynomials (e.g., Legendre for [-1,1]). Gaussian quadrature achieves higher accuracy than Newton-Cotes rules for smooth functions with the same number of evaluations.
