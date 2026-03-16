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

## Explainer

The Fundamental Theorem of Algebra makes a stark claim: every non-constant polynomial has at least one root, and if you work in the complex numbers, that root always exists. Over the real numbers this fails — x² + 1 = 0 has no real solutions. Over ℂ it always holds. The theorem is what makes ℂ **algebraically closed**: there is no polynomial equation that forces you to invent new numbers beyond the complex numbers to find a solution. In a sense, the complex numbers are "complete" for polynomial algebra.

The complex-analytic proof is one of the most elegant arguments in all of mathematics, and it rests entirely on Liouville's theorem, which you've already proved: the only bounded entire functions are constant functions. Suppose for contradiction that p(z) has no roots — that is, p(z) ≠ 0 for all z ∈ ℂ. Then 1/p(z) is everywhere defined, and since p is a polynomial (hence entire), 1/p is also **entire**. Now examine its behavior as |z| → ∞: because p has degree n ≥ 1, |p(z)| → ∞, which means |1/p(z)| → 0. In particular, 1/p is bounded on the entire complex plane (it's continuous on the compact disk |z| ≤ R, and small outside that disk). By Liouville's theorem, a bounded entire function must be constant. But 1/p being constant would mean p is constant, contradicting the assumption that p is non-constant. Therefore our assumption was wrong: p must have at least one root.

From the existence of one root, you get all n roots by an inductive argument. If z₁ is a root of p(z), then polynomial division gives p(z) = (z − z₁)q(z) where q has degree n − 1. If n − 1 ≥ 1, you can apply the theorem again to q to find a second root z₂, and so on, until you have factored p completely as p(z) = c(z − z₁)(z − z₂)⋯(z − zₙ). Counting roots with **multiplicity** (a factor (z − zᵢ)^k contributes k to the count) ensures exactly n roots.

What makes this proof remarkable is what it uses and what it doesn't. It never explicitly constructs the root — it shows one must exist via contradiction. The heavy lifting is done by Liouville's theorem, which is itself a consequence of Cauchy's integral formula and the rich structure of analytic functions. Real analysis lacks the tools for this argument: the real analogue of an entire bounded function need not be constant. Complex differentiability is far more rigid than real differentiability, and this rigidity — captured by Liouville — is what forces polynomials to have roots. The theorem is thus a triumph of complex-analytic structure applied to an algebraic question.
