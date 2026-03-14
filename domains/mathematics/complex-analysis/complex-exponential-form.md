---
id: complex-exponential-form
title: Complex Exponential Form and Euler's Formula
domain: mathematics
course: complex-analysis
prerequisites:
- id: polar-form-complex-numbers
  type: hard
- id: power-series
  type: soft
builds-toward:
- complex-exponential-function
- complex-logarithm-branch-cuts
tags:
- complex-exponentials
- euler-formula
- power-series
stage: abstract-reasoning
status: draft
---

# Complex Exponential Form and Euler's Formula

## Core Idea
Euler's formula e^(iθ) = cos θ + i sin θ allows us to write z = r e^(iθ) in exponential form. This unifies trigonometry with exponentials and makes complex multiplication simple: z₁z₂ = r₁r₂ e^(i(θ₁+θ₂)). The exponential form is fundamental to all of complex analysis because it extends naturally to complex exponents.

## How It's Best Learned
Verify Euler's formula by expanding e^(iθ) = Σ(iθ)ⁿ/n! and grouping real/imaginary parts. Compute specific examples like e^(iπ) = -1. Use the exponential form to multiply complex numbers and see how arguments add.

## Common Misconceptions
Treating e^(iθ) as purely formal; it represents a real geometric transformation (rotation). Forgetting the 2π periodicity: e^(i(θ+2π)) = e^(iθ).
