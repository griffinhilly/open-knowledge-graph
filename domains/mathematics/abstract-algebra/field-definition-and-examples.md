---
id: field-definition-and-examples
title: Field Definition and Examples
domain: mathematics
course: abstract-algebra
prerequisites:
- id: ring-definition-and-examples
  type: hard
- id: integral-domains
  type: soft
builds-toward:
- field-extensions
- finite-fields
tags:
- fields
- definitions
- examples
stage: advanced
status: draft
---

# Field Definition and Examples

## Core Idea
A field is a commutative ring with unity where every nonzero element has a multiplicative inverse. Fields are integral domains with additional structure. Examples: rationals Q, reals R, complex numbers C, finite fields Z/p. Every field is an integral domain.

## Explainer

A field is essentially a number system where you can add, subtract, multiply, and divide freely — except you can never divide by zero. From your work on rings, you know that a ring gives you addition and multiplication with nice properties, and an integral domain adds the condition that there are no zero divisors. A field is one step further: every nonzero element has a **multiplicative inverse**, meaning you can always "undo" multiplication.

Think about the rationals ℚ. You can add 3/4 + 1/2, multiply 3/4 × 2/3, and you can always divide: 3/4 ÷ 5/7 = 3/4 × 7/5. Every nonzero rational has a reciprocal. The integers ℤ fail this: 2 has no multiplicative inverse in ℤ because 1/2 is not an integer. So ℤ is an integral domain but not a field — it has no zero divisors, but it also lacks inverses for most elements.

The hallmark examples are ℚ, ℝ, ℂ, and the **finite fields** ℤ/pℤ for prime p. The prime condition is crucial: in ℤ/6ℤ, the element [2] has no inverse because gcd(2, 6) = 2 ≠ 1. But in ℤ/5ℤ, every nonzero element has an inverse — [2]·[3] = [6] = [1], [4]·[4] = [16] = [1]. When p is prime, every nonzero element is coprime to p, so inverses exist by Bezout's theorem. A modular ring is a field exactly when the modulus is prime.

The relationship between fields and integral domains is clean: every field is an integral domain (inverses prevent zero divisors), but not every integral domain is a field. The integers are the canonical counterexample. This distinction becomes structurally significant when building **field extensions** — the foundation of Galois theory — where the goal is to adjoin roots of polynomials to existing fields, creating larger fields that contain solutions you could not find in the original.
