---
id: fundamental-theorem-algebra-complex
title: Fundamental Theorem of Algebra (Complex-Analytic Proof)
domain: mathematics
course: complex-analysis
prerequisites:
- id: liouville-theorem
  type: hard
- id: cauchys-theorem
  type: soft
tags:
- fundamental-theorem-algebra
- roots
- polynomials
stage: advanced
status: draft
---

# Fundamental Theorem of Algebra (Complex-Analytic Proof)

## Core Idea
Every non-constant polynomial p(z) of degree n ≥ 1 has exactly n roots (counting multiplicity) in ℂ. The complex-analytic proof: assume p has no zeros; then 1/p is entire and bounded (since |1/p(z)| → 0 as |z| → ∞), so by Liouville's theorem, 1/p is constant, contradicting that p is non-constant.
