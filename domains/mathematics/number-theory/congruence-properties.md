---
id: congruence-properties
title: Properties of Congruences
domain: mathematics
course: number-theory
prerequisites:
- id: modular-arithmetic
  type: hard
builds-toward:
- fermats-little-theorem
- eulers-theorem
- quadratic-residues-legendre-symbol
tags:
- congruences
- modular-arithmetic
- properties
stage: advanced
status: draft
---

# Properties of Congruences

## Core Idea
Congruences mod n form an equivalence relation: a ≡ b (mod n) iff n|(a-b). They respect addition, subtraction, and multiplication. If gcd(a,n) = 1, division is possible. These properties make congruences a powerful algebraic tool for number theory.

## Questions

```yaml
- question: "Starting from 6 ≡ 2 (mod 4), a student cancels the factor of 2 from both sides to obtain 3 ≡ 1 (mod 4). What went wrong?"
  type: multiple-choice
  options:
    - "You can never cancel common factors in congruences — division is entirely undefined in modular arithmetic"
    - "You can cancel the factor of 2, but since gcd(2, 4) = 2, the modulus must also be divided by 2, giving the correct result 3 ≡ 1 (mod 2)"
    - "The original congruence 6 ≡ 2 (mod 4) is false, so no valid manipulation can follow"
    - "Division requires the factor to be prime; since 2 is prime, the cancellation should indeed give 3 ≡ 1 (mod 4)"
  answer: 1
  explanation: "When cancelling a factor c from ac ≡ bc (mod n), you must also divide the modulus by gcd(c, n). Here c = 2 and n = 4, so gcd(2, 4) = 2, and the correct result is 3 ≡ 1 (mod 4/2) = 3 ≡ 1 (mod 2), which is true (both are odd). The student kept the original modulus 4 after dividing both sides by 2, producing a false statement. This is the key subtlety of 'division' in congruences: it is valid, but it shrinks the modulus when the divisor shares a common factor with it."

- question: "Which of the following operations can always be performed on both sides of a valid congruence a ≡ b (mod n) while preserving validity?"
  type: multiple-choice
  options:
    - "Dividing both sides by any integer c, keeping the modulus n unchanged"
    - "Squaring both sides to get a² ≡ b² (mod n)"
    - "Taking the square root of both sides to get √a ≡ √b (mod n)"
    - "Adding an arbitrary integer c to the modulus"
  answer: 1
  explanation: "Because congruences are closed under multiplication, squaring is always valid: if a ≡ b (mod n), then a² = a·a ≡ b·b = b² (mod n). This is a direct application of the multiplicative property. Option A (division while keeping modulus unchanged) only works when the divisor is coprime to n. Option C (square roots) has no general guarantee in modular arithmetic — square roots may not exist, or may not be unique. Option D makes no sense as a manipulation of a congruence."

- question: "If a ≡ b (mod n) and c divides both a and b, then a/c ≡ b/c (mod n) always holds."
  type: true-false
  answer: false
  explanation: "This is false when gcd(c, n) > 1. The classic example: 6 ≡ 2 (mod 4). Dividing by c = 2 gives 3 ≡ 1 (mod 4), which is false (4 does not divide 3 − 1 = 2). Division preserves the congruence at the same modulus only when gcd(c, n) = 1. When gcd(c, n) = d > 1, cancelling c requires dividing the modulus by d: a/c ≡ b/c (mod n/d). This rule is the most common source of errors in elementary number theory computations."

- question: "When the modulus n is prime, every nonzero residue class mod n has a multiplicative inverse."
  type: true-false
  answer: true
  explanation: "When n is prime, gcd(a, n) = 1 for every a not divisible by n (since n has no factors other than 1 and itself). By Bézout's identity, this implies there exist integers x, y such that ax + ny = 1, which means ax ≡ 1 (mod n) — so x = a⁻¹ mod n exists. This makes ℤ/pℤ a field: every nonzero element has a multiplicative inverse and all four arithmetic operations are fully defined. This property is what enables Fermat's little theorem and makes prime moduli central to cryptographic applications."

- question: "Why does division in modular arithmetic require the divisor to be coprime to the modulus, when addition and multiplication have no such restriction?"
  type: short-answer
  answer: "Addition and multiplication are defined directly by the ring structure of ℤ/nℤ — the sum or product of any two residue classes is another residue class, always. Division means multiplying by the multiplicative inverse. An inverse of c mod n exists if and only if gcd(c, n) = 1, because c·c⁻¹ ≡ 1 (mod n) requires that 1 is reachable as a multiple of c modulo n — which only happens when c and n share no common factor. When gcd(c, n) = d > 1, the element c is a zero-divisor: there exist nonzero elements it sends to zero (e.g., c · (n/d) ≡ 0 mod n), destroying the injectivity required for division to be well-defined."
  explanation: "The algebraic intuition: in ℤ/6ℤ, the element 2 has no inverse because 2·1=2, 2·2=4, 2·3=0, 2·4=2, 2·5=4 — none equals 1. But in ℤ/7ℤ (prime), every nonzero element has an inverse: 2·4=8≡1, so 2⁻¹=4."
```

## Explainer

From your study of modular arithmetic, you know that a ≡ b (mod n) means a and b leave the same remainder when divided by n — equivalently, n divides (a − b). What congruences gain from being an **equivalence relation** is structure: they carve the integers into n disjoint **residue classes** (the classes 0, 1, 2, ..., n−1), and every integer belongs to exactly one. You can think of the integers as being "folded" onto a circle of n positions, and two numbers are congruent precisely when they land on the same position.

The arithmetic rules follow directly from this picture. If a ≡ b (mod n) and c ≡ d (mod n), then a + c ≡ b + d and a × c ≡ b × d (mod n). To see why multiplication works: a = b + kn and c = d + ln for some integers k, l, so ac = (b + kn)(d + ln) = bd + (bl + dk + kln)n. The extra terms are all multiples of n, so ac and bd land on the same residue class. This means you can reduce intermediate results at any stage of a computation — a powerful shortcut when doing arithmetic mod n.

**Division** is the subtler operation. You cannot always divide both sides of a congruence by a common factor and preserve the modulus. For example, 6 ≡ 2 (mod 4), but dividing by 2 gives 3 ≡ 1 (mod 4), which is false. Division works cleanly only when the divisor is **coprime to n** — that is, gcd(a, n) = 1. In that case, a has a **multiplicative inverse mod n**, a unique number a⁻¹ such that a·a⁻¹ ≡ 1 (mod n). Multiplying both sides by a⁻¹ is valid division. When gcd(a, n) = d > 1, you can still cancel a from ac ≡ ab (mod n), but the modulus shrinks: c ≡ b (mod n/d).

These properties are what make congruences a genuine algebraic system rather than just notation. The set {0, 1, ..., n−1} under addition and multiplication mod n forms a **ring** (written ℤ/nℤ); when n is prime, every nonzero element has a multiplicative inverse and it becomes a **field**. This algebraic lens is what powers everything downstream — Fermat's little theorem, Euler's theorem, and the Legendre symbol all live inside this structure. Whenever you see a proof that "reduces mod p," the congruence properties are the invisible machinery making each step valid.
