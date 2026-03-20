---
id: improper-integrals-rigorous
title: Improper Integrals (Rigorous)
domain: mathematics
course: real-analysis
prerequisites:
- id: riemann-integral-properties
  type: hard
- id: series-convergence-rigorous
  type: soft
tags:
- improper-integrals
- convergence
- unbounded
stage: advanced
status: draft
---

# Improper Integrals (Rigorous)

## Core Idea
An improper integral extends the Riemann integral to unbounded intervals or unbounded integrands by taking limits. For infinite intervals, ∫ₐ^∞ f(x) dx = lim_{t→∞} ∫ₐᵗ f(x) dx; for unbounded integrands near a point c, ∫ₐᵇ f(x) dx = lim_{ε→0⁺} ∫ₐ^{c−ε} f(x) dx + lim_{ε→0⁺} ∫_{c+ε}ᵇ f(x) dx. The integral converges if these limits exist and are finite. Convergence criteria mirror those for series: comparison tests, limit comparison, and absolute convergence all apply. An integral can converge conditionally (like ∫₁^∞ sin(x)/x dx) without converging absolutely. These integrals arise naturally in probability, Fourier analysis, and Laplace transforms.

## How It's Best Learned
Work through the classic examples: ∫₁^∞ 1/xᵖ dx (converges iff p > 1), then ∫₀¹ 1/xᵖ dx (converges iff p < 1). These two cases build the intuition that convergence depends on how fast the integrand decays or blows up relative to the interval.

## Common Misconceptions
Students sometimes evaluate improper integrals by plugging in ∞ directly, skipping the limit process. This can produce correct-looking answers but obscures conditional convergence issues. Also, the two limits in a doubly improper integral must be taken independently—they cannot be combined into a single symmetric limit.

