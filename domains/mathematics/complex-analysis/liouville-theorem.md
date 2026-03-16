---
id: liouville-theorem
title: Liouville's Theorem
domain: mathematics
course: complex-analysis
prerequisites:
- id: cauchys-integral-formula-derivatives
  type: hard
builds-toward:
- fundamental-theorem-algebra-complex
- maximum-modulus-principle
tags:
- liouvilles-theorem
- bounded-entire
- rigidity
stage: advanced
status: draft
---

# Liouville's Theorem

## Core Idea
Any bounded entire function (holomorphic on all of ℂ) must be constant. This remarkable rigidity theorem shows that the only way a holomorphic function can be bounded globally is if it doesn't vary. It follows from Cauchy's integral formula and has profound consequences, including elegant proofs of the Fundamental Theorem of Algebra.

## Explainer

Liouville's Theorem is a statement about the extreme rigidity of holomorphic functions — a rigidity that has no analog in real analysis. In real analysis, you can easily write bounded, non-constant smooth functions: sin(x) oscillates forever between −1 and 1. But in complex analysis, a function that is holomorphic everywhere on ℂ (called **entire**) and bounded must be constant. No oscillation, no variation at all. This contrast makes the theorem feel almost paradoxical at first.

The proof comes directly from **Cauchy's integral formula for derivatives**, your prerequisite. That formula says: for a holomorphic function f and a circle of radius R centered at a point z₀, the derivative f'(z₀) = (1/2πi) ∮ f(z)/(z − z₀)² dz. The crucial estimate is to bound the modulus of this integral. The integrand has modulus |f(z)|/|z − z₀|² ≤ M/R² (where M is the bound on |f|), and the circle has circumference 2πR. Therefore |f'(z₀)| ≤ (1/2π) · (M/R²) · 2πR = M/R. This holds for every R, because the function is entire — we can take the circle as large as we wish. Sending R → ∞ forces |f'(z₀)| ≤ 0, so f'(z₀) = 0. Since z₀ was arbitrary, f' ≡ 0 everywhere, meaning f is constant.

The key insight is that boundedness, combined with holomorphicity, destroys the derivative through a size argument: as the circle grows, the bound M/R shrinks to zero. In real analysis, you cannot make this argument — the integral formulas for real functions don't have the same structure. Complex differentiability is far stronger than real differentiability, and Liouville's Theorem is one of its sharpest consequences.

The most celebrated application is a one-paragraph proof of the **Fundamental Theorem of Algebra**: every non-constant polynomial p(z) has a root in ℂ. Suppose p has no roots; then 1/p(z) is entire (no zeros means no poles). For large |z|, |p(z)| → ∞, so |1/p(z)| → 0, making 1/p bounded. By Liouville's Theorem, 1/p is constant — but that would make p constant, contradicting our assumption. Therefore p must have a root. The entire proof is: "assume no root → get bounded entire function → Liouville says it's constant → contradiction." Liouville's Theorem is the engine that makes this two-line proof work.
