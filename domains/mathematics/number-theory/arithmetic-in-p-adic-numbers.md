---
id: arithmetic-in-p-adic-numbers
title: Arithmetic in p-adic Numbers
domain: mathematics
course: number-theory
prerequisites:
- id: introduction-to-p-adic-numbers
  type: hard
tags:
- p-adic
- arithmetic
- algebraic-structures
stage: advanced
status: draft
---

# Arithmetic in p-adic Numbers

## Core Idea
The p-adic numbers form a field with a metric structure that preserves arithmetic operations. Algebraic equations over ℚ_p can be analyzed using Hensel's lemma, which 'lifts' solutions from modular arithmetic to p-adic convergent sequences, enabling powerful solution techniques.

## Explainer

You already know that ℚ_p is built by completing the rationals under the p-adic metric — a measure of size where numbers divisible by high powers of p are considered "small." Arithmetic in ℚ_p follows the same rules as ordinary rational arithmetic: you can add, subtract, multiply, and divide (by nonzero elements). The algebraic structure is a **field**, meaning all the familiar properties hold. What's new is understanding how equations behave in this setting, and that's where Hensel's lemma becomes the central tool.

**Hensel's lemma** is a p-adic analogue of Newton's method from calculus. The idea is a "lifting" procedure: if you have a solution to a polynomial equation modulo p — that is, a solution in ℤ/pℤ — and a certain non-degeneracy condition holds (the derivative at the solution is not divisible by p), then you can systematically extend that solution to a solution modulo p², then p³, and so on indefinitely. Because ℚ_p is the completion of ℚ, this infinite sequence of consistent approximations converges to an exact solution in ℚ_p. The **p-adic integers** ℤ_p appear as the "ring of integers" in this setting — elements with p-adic valuation ≥ 0.

To make the lifting concrete, consider the equation x² = a. You want to know whether a is a perfect square in ℚ_p. Start by checking: is a a square mod p? If so, take a square root r₀ with r₀² ≡ a (mod p). The Hensel lifting step says: given rₙ with rₙ² ≡ a (mod pⁿ), set rₙ₊₁ = rₙ − (rₙ² − a)/(2rₙ) — this is Newton's iteration, applied in the p-adic world. Each step doubles the number of correct p-adic digits. After infinitely many steps, the sequence converges to an exact p-adic square root of a.

The power of Hensel's lemma lies in turning global questions (does this polynomial have a rational root?) into local questions (does it have a root modulo each prime p?). By the **Hasse principle** (which holds for quadratic forms), a quadratic equation has a rational solution if and only if it has a solution in ℝ and in ℚ_p for every prime p. This is the beginning of the **local-global philosophy** that runs through modern number theory: understand a problem everywhere locally (at each prime and at infinity), and you may be able to understand it globally over ℚ.
