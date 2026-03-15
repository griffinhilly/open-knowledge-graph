---
id: cauchys-theorem
title: Cauchy's Theorem
domain: mathematics
course: complex-analysis
prerequisites:
- id: contour-integration
  type: hard
- id: greens-theorem
  type: soft
builds-toward:
- cauchys-integral-formula
- fundamental-theorem-algebra-complex
tags:
- cauchys-theorem
- holomorphic
- closed-contours
stage: advanced
status: draft
---

# Cauchy's Theorem

## Core Idea
If f is holomorphic on a simply connected domain D and γ is any closed contour in D, then ∮_γ f(z) dz = 0. This is the cornerstone of complex analysis: it implies line integrals of holomorphic functions are path-independent, and it leads directly to Cauchy's integral formula, Taylor series, and residue methods. The proof uses Green's theorem and the Cauchy-Riemann equations.

## How It's Best Learned
Verify this for f(z) = z² around a circle; integrate directly and use the theorem to check both give zero. Try f(z) = 1/z around a circle centered at the origin; the theorem does NOT apply (f is not holomorphic at 0), and the integral is nonzero.

## Common Misconceptions
Assuming Cauchy's theorem applies to all functions; it requires holomorphicity and a simply connected domain. Forgetting that the domain must be simply connected; on multiply-connected domains with holes, the integral can be nonzero.
