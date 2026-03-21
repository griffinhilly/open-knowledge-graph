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

## Questions

```yaml
- question: "A polynomial f(x) has a root r₀ with f(r₀) ≡ 0 (mod p). Under what additional condition does Hensel's lemma guarantee that this root lifts to an exact root in ℚ_p?"
  type: multiple-choice
  options:
    - "No additional condition is needed — any modular root can always be lifted"
    - "f'(r₀) ≢ 0 (mod p), meaning the derivative at the root is not divisible by p"
    - "The polynomial must have degree at most 2"
    - "The prime p must be odd"
  answer: 1
  explanation: "Hensel's lemma requires a non-degeneracy condition: the derivative f'(r₀) must not be divisible by p. Without this, the root may be 'singular' modulo p and may not lift uniquely — or at all. Option A describes a common misconception: a modular root is necessary but not sufficient. The derivative condition ensures the Newton's-method iteration converges geometrically in the p-adic metric."

- question: "Which philosophical principle does Hensel's lemma most directly support when combined with the Hasse principle for quadratic forms?"
  type: multiple-choice
  options:
    - "The local-global philosophy: understanding a problem at every prime (and at ∞) gives information about global rational solutions"
    - "The completeness of ℚ_p: every Cauchy sequence in the p-adic metric converges"
    - "The ultrametric inequality: p-adic absolute values satisfy |x + y|_p ≤ max(|x|_p, |y|_p)"
    - "The uniqueness of prime factorization in the integers"
  answer: 0
  explanation: "The Hasse principle (for quadratic forms) states that a quadratic equation has a rational solution if and only if it has a solution in ℝ and in ℚ_p for every prime p. Hensel's lemma supplies the p-adic solutions by lifting modular ones. Together they exemplify the local-global philosophy: checking everywhere locally (at each prime p and at infinity) suffices to answer the global question over ℚ."

- question: "If a polynomial f(x) has a root modulo every prime p, then it necessarily has a root in ℚ."
  type: true-false
  answer: false
  explanation: "This is false in general — the Hasse principle does NOT hold for polynomials of degree higher than 2. For quadratic forms it is a theorem, but for higher-degree polynomials there can be 'failures of the Hasse principle': a polynomial may have roots in every ℚ_p (and in ℝ) yet have no rational root. The Hasse principle is a special property of quadratic forms, not a universal law."

- question: "The p-adic integers ℤ_p are exactly the elements of ℚ_p with p-adic valuation greater than or equal to zero."
  type: true-false
  answer: true
  explanation: "True. The p-adic valuation v_p(x) measures divisibility by p: elements with v_p(x) ≥ 0 are those not in the 'denominator' part of the p-adic expansion. These form the ring of integers ℤ_p inside the field ℚ_p, analogous to how ℤ sits inside ℚ. Hensel's lemma, when the root is in ℤ/pℤ, lifts it into ℤ_p."

- question: "Explain in your own words what 'lifting' means in Hensel's lemma, and why the p-adic completion is the natural setting for it."
  type: short-answer
  answer: "Lifting means starting with an approximate solution (a root mod p) and systematically refining it into increasingly precise solutions (mod p², mod p³, ...) until you have an infinite sequence that converges to an exact root in ℚ_p. The p-adic completion is natural because the p-adic metric makes these approximations converge: each step multiplies the error by p, so errors shrink toward zero in the p-adic sense. The completed field ℚ_p guarantees that the infinite sequence of consistent approximations has an actual limit."
  explanation: "The key analogy is Newton's method in calculus: each iteration of the Hensel lift doubles the number of correct digits (in the p-adic expansion), just as Newton's method doubles the correct decimal places in a real root. The p-adic metric is what makes 'convergence' meaningful — in ordinary ℤ, the sequence of residues grows without bound, but in ℚ_p they converge because divisibility by higher powers of p means 'smaller.'"
```

## Explainer

You already know that ℚ_p is built by completing the rationals under the p-adic metric — a measure of size where numbers divisible by high powers of p are considered "small." Arithmetic in ℚ_p follows the same rules as ordinary rational arithmetic: you can add, subtract, multiply, and divide (by nonzero elements). The algebraic structure is a **field**, meaning all the familiar properties hold. What's new is understanding how equations behave in this setting, and that's where Hensel's lemma becomes the central tool.

**Hensel's lemma** is a p-adic analogue of Newton's method from calculus. The idea is a "lifting" procedure: if you have a solution to a polynomial equation modulo p — that is, a solution in ℤ/pℤ — and a certain non-degeneracy condition holds (the derivative at the solution is not divisible by p), then you can systematically extend that solution to a solution modulo p², then p³, and so on indefinitely. Because ℚ_p is the completion of ℚ, this infinite sequence of consistent approximations converges to an exact solution in ℚ_p. The **p-adic integers** ℤ_p appear as the "ring of integers" in this setting — elements with p-adic valuation ≥ 0.

To make the lifting concrete, consider the equation x² = a. You want to know whether a is a perfect square in ℚ_p. Start by checking: is a a square mod p? If so, take a square root r₀ with r₀² ≡ a (mod p). The Hensel lifting step says: given rₙ with rₙ² ≡ a (mod pⁿ), set rₙ₊₁ = rₙ − (rₙ² − a)/(2rₙ) — this is Newton's iteration, applied in the p-adic world. Each step doubles the number of correct p-adic digits. After infinitely many steps, the sequence converges to an exact p-adic square root of a.

The power of Hensel's lemma lies in turning global questions (does this polynomial have a rational root?) into local questions (does it have a root modulo each prime p?). By the **Hasse principle** (which holds for quadratic forms), a quadratic equation has a rational solution if and only if it has a solution in ℝ and in ℚ_p for every prime p. This is the beginning of the **local-global philosophy** that runs through modern number theory: understand a problem everywhere locally (at each prime and at infinity), and you may be able to understand it globally over ℚ.
