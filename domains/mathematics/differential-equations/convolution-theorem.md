---
id: convolution-theorem
title: Convolution Theorem
domain: mathematics
course: differential-equations
prerequisites:
- id: solving-ivps-laplace-transform
  type: hard
- id: integration-by-parts
  type: soft
builds-toward:
- dirac-delta-function
tags:
- convolution
- product-rule
- inverse-transform
stage: formal-systems
status: draft
---

# Convolution Theorem

## Core Idea
The convolution of f and g is (f * g)(t) = ∫₀^t f(τ)g(t-τ)dτ. The convolution theorem states L[f * g] = F(s)G(s), so L^(-1)[F(s)G(s)] = (f * g)(t). This theorem is invaluable for solving non-homogeneous equations where the forcing function's transform is a product of simpler transforms, allowing you to decompose complex solutions into manageable parts.
