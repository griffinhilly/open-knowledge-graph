---
id: convolution-theorem
title: Convolution Theorem and Applications
domain: mathematics
course: differential-equations
prerequisites:
- id: laplace-transform-definition-and-properties
  type: hard
- id: convolution-integral
  type: soft
builds-toward:
- dirac-delta-function
tags:
- laplace-transform
- convolution
- product-rule
stage: advanced
status: draft
---

# Convolution Theorem and Applications

## Core Idea
The convolution of f and g is (f * g)(t) = ∫₀ᵗ f(τ)g(t - τ) dτ. The convolution theorem states L{f * g} = F(s)·G(s), enabling solutions to ODEs with complicated forcing by interpreting them as Laplace products, then inverting via convolution.
