---
id: characteristic-functions
title: Characteristic Functions
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: moment-generating-functions
  type: soft
- id: variance-higher-moments-rigorous
  type: hard
- id: complex-exponential-function
  type: soft
builds-toward:
- central-limit-theorem-rigorous
- convergence-in-distribution
tags:
- characteristic-functions
- fourier-analysis
- moments
stage: advanced
status: draft
---

# Characteristic Functions

## Core Idea
The characteristic function is φ(t) = E[e^{itX}], which exists for all real t. Unlike the MGF, φ always exists, making it more versatile. The characteristic function is the Fourier transform of the probability distribution; inversion formulas recover the CDF from φ. Convergence of characteristic functions implies convergence of distributions.

## How It's Best Learned
Compute characteristic functions for standard distributions. Apply the inversion formula to recover CDFs. Use characteristic functions to prove the central limit theorem.

## Common Misconceptions
- Confusing characteristic and moment generating functions; use φ(t) = E[e^{itX}] for characteristic. - Thinking moment-generating functions always exist; MGFs may not, but characteristic functions always do. - Forgetting to use the complex exponential in the definition.
