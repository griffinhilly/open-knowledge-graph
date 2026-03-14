---
id: laplace-transform-of-derivatives
title: Laplace Transform of Derivatives and Integrals
domain: mathematics
course: differential-equations
prerequisites:
- id: laplace-transform-definition-and-properties
  type: hard
- id: integration-by-parts
  type: soft
builds-toward:
- solving-ivps-with-laplace-transforms
tags:
- laplace-transform
- derivative
- integral
stage: advanced
status: draft
---

# Laplace Transform of Derivatives and Integrals

## Core Idea
The key property L{f'(t)} = sF(s) - f(0) (and generalizations for higher derivatives) converts ODE initial value problems into algebraic problems. Similarly, L{∫₀ᵗ f(τ) dτ} = F(s)/s, converting integro-differential equations to algebraic form.
