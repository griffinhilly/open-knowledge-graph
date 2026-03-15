---
id: complex-differentiability
title: Complex Differentiability
domain: mathematics
course: complex-analysis
prerequisites:
- id: limits-continuity-complex-functions
  type: hard
builds-toward:
- holomorphic-functions
- cauchy-riemann-equations
tags:
- differentiability
- derivatives
- holomorphic
stage: advanced
status: draft
---

# Complex Differentiability

## Core Idea
A function f is differentiable at z₀ if the limit f'(z₀) = lim(h→0) [f(z₀+h) - f(z₀)]/h exists and is independent of the direction in which h approaches 0. This requirement — that the derivative exists along all paths and is the same value — is far more restrictive than real differentiability and is the gateway to rigid complex analysis.

## How It's Best Learned
Compute derivatives directly from the definition for f(z) = z² and f(z) = 1/z. Attempt this for f(z) = |z|² and observe that the limit fails (depends on direction). This contrast shows why complex differentiability is special.

## Common Misconceptions
Thinking complex differentiability is just real differentiability of u and v separately; that gives only a function of two real variables, not an analytic function. Assuming all functions satisfying Cauchy-Riemann are differentiable; continuity of partials is needed too.
