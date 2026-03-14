---
id: gaussian-quadrature
title: Gaussian Quadrature
domain: mathematics
course: numerical-analysis
prerequisites:
- id: composite-quadrature
  type: hard
builds-toward:
- romberg-integration
tags:
- gaussian-quadrature
- optimal
- integration
stage: abstract-reasoning
status: draft
---

# Gaussian Quadrature

## Core Idea
Gaussian quadrature optimally chooses both sample points x_i and weights w_i to integrate polynomials of degree up to 2n-1 exactly using only n function evaluations. The sample points are roots of orthogonal polynomials (Legendre, Hermite, Laguerre, Chebyshev) with respect to a weight function. Gaussian quadrature achieves exponential convergence for smooth integrands and is the most efficient for general-purpose integration.
