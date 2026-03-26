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
status: validated
---

# Field Definition and Examples

## Core Idea
A field is a commutative ring with unity where every nonzero element has a multiplicative inverse. Fields are integral domains with additional structure. Examples: rationals Q, reals R, complex numbers C, finite fields Z/p. Every field is an integral domain.

## Questions

```yaml
- question: "Is ℤ/6ℤ a field? Why or why not?"
  type: multiple-choice
  options:
    - "Yes — it is a commutative ring with unity, which is all a field requires"
    - "No — because 6 is not prime, elements like [2] have no multiplicative inverse in ℤ/6ℤ"
    - "Yes — every modular ring is a field because arithmetic always works modulo n"
    - "No — because ℤ/6ℤ contains zero divisors, which disqualifies it as an integral domain, but it could still be a field"
  answer: 1
  explanation: "A field requires every nonzero element to have a multiplicative inverse. In ℤ/6ℤ, [2] has no inverse because gcd(2, 6) = 2 ≠ 1 — no element [k] satisfies [2]·[k] = [1]. This also means [2]·[3] = [6] = [0], revealing a zero divisor and disqualifying ℤ/6ℤ as even an integral domain. Only ℤ/pℤ for prime p is a field, because primality guarantees every nonzero element is coprime to p, so Bézout's theorem yields an inverse."

- question: "Which of the following correctly describes the relationship between fields and integral domains?"
  type: multiple-choice
  options:
    - "Every integral domain is a field, but not every field is an integral domain"
    - "Every field is an integral domain, but not every integral domain is a field"
    - "Fields and integral domains are identical — they have the same axioms"
    - "Neither implies the other — they are independent algebraic structures"
  answer: 1
  explanation: "Every field is an integral domain: if ab = 0 in a field and a ≠ 0, multiply both sides by a⁻¹ to get b = 0, so there are no zero divisors. But the converse fails — ℤ is an integral domain (no zero divisors) yet 2 has no multiplicative inverse in ℤ, so ℤ is not a field. The integers are the canonical counterexample showing the inclusion is strict."

- question: "Nearly every integral domain is a field."
  type: true-false
  answer: false
  explanation: "The integers ℤ are an integral domain — they have no zero divisors — but ℤ is not a field because most elements lack multiplicative inverses. For example, 2 has no inverse in ℤ because 1/2 ∉ ℤ. A field is a strictly stronger structure: it requires multiplicative inverses for all nonzero elements, not just the absence of zero divisors."

- question: "ℤ/pℤ is a field for every prime p."
  type: true-false
  answer: true
  explanation: "When p is prime, every nonzero element [a] in ℤ/pℤ satisfies gcd(a, p) = 1. By Bézout's theorem, there exist integers s, t such that as + pt = 1, which means [a]·[s] = [1] in ℤ/pℤ — so [s] is the multiplicative inverse of [a]. Since every nonzero element has an inverse and ℤ/pℤ is already a commutative ring with unity, it is a field."

- question: "Why does ℤ/pℤ form a field when p is prime but not when p is composite? Explain the key algebraic reason."
  type: short-answer
  answer: "When p is prime, every integer 1 ≤ a < p is coprime to p, so Bézout's theorem guarantees a multiplicative inverse for each nonzero element [a] in ℤ/pℤ. When p is composite, say p = mn with 1 < m, n < p, then [m]·[n] = [mn] = [0], producing a zero divisor — which immediately means the ring cannot be a field, since in a field ab = 0 forces a = 0 or b = 0."
  explanation: "Primality is the exact condition needed to ensure every nonzero residue class is invertible. A composite modulus always produces zero divisors from its non-trivial factorizations, which violates even the integral domain property, let alone the field property. This is why the prime condition is not just sufficient but necessary for ℤ/nℤ to be a field."
```

## Explainer

A field is essentially a number system where you can add, subtract, multiply, and divide freely — except you can never divide by zero. From your work on rings, you know that a ring gives you addition and multiplication with nice properties, and an integral domain adds the condition that there are no zero divisors. A field is one step further: every nonzero element has a **multiplicative inverse**, meaning you can always "undo" multiplication.

Think about the rationals ℚ. You can add 3/4 + 1/2, multiply 3/4 × 2/3, and you can always divide: 3/4 ÷ 5/7 = 3/4 × 7/5. Every nonzero rational has a reciprocal. The integers ℤ fail this: 2 has no multiplicative inverse in ℤ because 1/2 is not an integer. So ℤ is an integral domain but not a field — it has no zero divisors, but it also lacks inverses for most elements.

The hallmark examples are ℚ, ℝ, ℂ, and the **finite fields** ℤ/pℤ for prime p. The prime condition is crucial: in ℤ/6ℤ, the element [2] has no inverse because gcd(2, 6) = 2 ≠ 1. But in ℤ/5ℤ, every nonzero element has an inverse — [2]·[3] = [6] = [1], [4]·[4] = [16] = [1]. When p is prime, every nonzero element is coprime to p, so inverses exist by Bezout's theorem. A modular ring is a field exactly when the modulus is prime.

The relationship between fields and integral domains is clean: every field is an integral domain (inverses prevent zero divisors), but not every integral domain is a field. The integers are the canonical counterexample. This distinction becomes structurally significant when building **field extensions** — the foundation of Galois theory — where the goal is to adjoin roots of polynomials to existing fields, creating larger fields that contain solutions you could not find in the original.
