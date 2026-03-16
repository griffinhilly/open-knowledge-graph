---
id: fermat-last-theorem-overview
title: Fermat's Last Theorem (Overview)
domain: mathematics
course: number-theory
prerequisites:
- id: pythagorean-triples-parametrization
  type: soft
tags:
- fermat-last-theorem
- diophantine
- history
stage: advanced
status: draft
---

# Fermat's Last Theorem (Overview)

## Core Idea
Fermat's Last Theorem states that x^n + y^n = z^n has no positive integer solutions for integer n > 2, while Pythagorean triples show solutions exist for n = 2. Fermat's 350-year conjecture was proved by Andrew Wiles in 1995 using deep tools from algebraic geometry and number theory.

## Explainer

From your study of Pythagorean triples, you know that the equation x² + y² = z² has infinitely many positive integer solutions — (3, 4, 5), (5, 12, 13), and the full parametric family (m²−n², 2mn, m²+n²). Fermat's Last Theorem asks: what happens when you replace the exponent 2 with something larger? Can you find three positive integers satisfying x³ + y³ = z³, or x⁴ + y⁴ = z⁴? The answer, famously, is no — and not just for specific exponents, but for *every* integer exponent greater than 2.

Pierre de Fermat wrote this claim in the margin of his copy of Diophantus's *Arithmetica* around 1637, adding the tantalizing note that he had "a truly marvelous proof which this margin is too narrow to contain." For 358 years, every attempt to find that proof failed. The theorem was verified computationally for countless specific exponents, and partial proofs covered many cases, but a complete proof eluded everyone. It became one of the most famous open problems in mathematics — simple to state, impossible to settle.

What makes the problem so hard is that the natural approaches don't scale. For n = 4, Fermat himself gave a proof using **infinite descent** — a technique where you assume a solution exists and derive a smaller one, contradicting the minimality of positive integers. For n = 3, Euler supplied a proof. But generalizing these case-by-case arguments to all n proved intractable. The structure of the equation changes character depending on the exponent, and no elementary framework could capture all cases at once.

Andrew Wiles's 1995 proof took a completely different route. Rather than attacking the Diophantine equation directly, Wiles worked through **elliptic curves** — a class of curves defined by equations of the form y² = x³ + ax + b — and the **Taniyama-Shimura conjecture**, which claimed that every elliptic curve over the rationals is modular (i.e., arises from a modular form). In the 1980s, Gerhard Frey observed that if a solution to Fermat's equation existed, you could construct an elliptic curve with such bizarre properties that it could *not* be modular. Ken Ribet proved this rigorously. So if the Taniyama-Shimura conjecture were true, Fermat's Last Theorem would follow as a corollary — because the supposedly-non-modular Frey curve would be a contradiction. Wiles spent seven years in secret proving a crucial case of Taniyama-Shimura, and the proof was complete.

The story of Fermat's Last Theorem is thus less about the equation itself and more about the unexpected bridges mathematics builds between distant fields. A question about integers was answered through the theory of curves over complex numbers, which was answered through the theory of automorphic forms. This is why the theorem is an overview — the actual proof machinery lies far beyond its statement — but the statement itself is a perfect illustration of how number theory's simplest-looking questions can encode the deepest structure.
