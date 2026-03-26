---
id: euler-theorem
title: Euler's Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: fermat-little-theorem
  type: soft
- id: euler-totient-function
  type: hard
builds-toward:
- rsa-cryptography
tags:
- modular-arithmetic
- euler-phi
- group-theory
stage: advanced
status: validated
---

# Euler's Theorem

## Core Idea
If gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n), where φ is Euler's totient function. This generalizes Fermat's Little Theorem (where n = p gives φ(p) = p−1) and is essential for understanding RSA cryptography and computing modular exponentiation.

## Questions

```yaml
- question: "You need to compute 3^100 mod 7. Applying Euler's theorem with φ(7) = 6, which computation is correct?"
  type: multiple-choice
  options:
    - "3^100 ≡ 3^(100 mod 7) ≡ 3^2 ≡ 2 (mod 7) — reduce the exponent by the modulus"
    - "3^100 ≡ 3^(100 mod 6) ≡ 3^4 ≡ 81 ≡ 4 (mod 7) — reduce the exponent modulo φ(7)"
    - "3^100 ≡ 1 (mod 7) — Euler's theorem says any power of any number is 1 mod the modulus"
    - "3^100 ≡ 3^(100 mod 3) ≡ 3^1 ≡ 3 (mod 7) — reduce by the base"
  answer: 1
  explanation: "Euler's theorem says a^φ(n) ≡ 1 (mod n) when gcd(a, n) = 1. Since 7 is prime, gcd(3, 7) = 1 and φ(7) = 6. This means 3^6 ≡ 1 (mod 7), so 3^100 = (3^6)^16 · 3^4 ≡ 1^16 · 3^4 ≡ 81 ≡ 4 (mod 7). The reduction is: reduce the exponent modulo φ(n), not modulo n. The common mistake (option A) reduces by n itself — that is wrong; n is the modulus for the *result*, not for the exponent."

- question: "A student wants to apply Euler's theorem to compute 6^10 mod 9. They note φ(9) = 6 and conclude 6^10 ≡ 6^(10 mod 6) ≡ 6^4 (mod 9). What is wrong?"
  type: multiple-choice
  options:
    - "φ(9) is not 6; it should be 3"
    - "The exponent reduction rule uses φ(n) − 1, not φ(n)"
    - "Euler's theorem requires gcd(a, n) = 1, but gcd(6, 9) = 3 ≠ 1, so the theorem does not apply"
    - "Nothing — the computation is correct"
  answer: 2
  explanation: "Euler's theorem has a necessary hypothesis: gcd(a, n) = 1. Here gcd(6, 9) = 3, so 6 and 9 share a common factor and the theorem simply does not apply. φ(9) = 6 is actually correct (the units mod 9 are 1, 2, 4, 5, 7, 8). But since 6 is not a unit mod 9, you cannot use Euler's theorem to reduce 6^10 mod 9. In fact 6^10 mod 9 = 0, since 6^2 = 36 ≡ 0 (mod 9)... wait, that's 3^2|36, and 9|36, so yes 6^2 ≡ 0. The coprimality condition is not a technical nicety — without it the theorem is false."

- question: "Fermat's Little Theorem — that a^(p−1) ≡ 1 (mod p) for any prime p not dividing a — is a special case of Euler's Theorem."
  type: true-false
  answer: true
  explanation: "Yes. When n = p is prime, every integer from 1 to p−1 is coprime to p, so φ(p) = p − 1. Euler's theorem then says a^φ(p) = a^(p−1) ≡ 1 (mod p) for gcd(a, p) = 1 — exactly Fermat's Little Theorem. Euler's theorem is the generalization that extends this to composite moduli, which is what gives it broader applicability, including in RSA where the modulus n = pq is the product of two large primes."

- question: "Euler's theorem states that a^φ(n) ≡ 1 (mod n) holds for most integer a, including those that share a common factor with n."
  type: true-false
  answer: false
  explanation: "The condition gcd(a, n) = 1 is essential — without it the theorem is false. For example, a = 2, n = 4: φ(4) = 2, and 2^2 = 4 ≡ 0 (mod 4), not 1. The reason is that the proof relies on the set of units modulo n (integers coprime to n) forming a group under multiplication; multiplying by a unit permutes this group. If gcd(a, n) > 1, then a is not a unit and does not act on the units by permutation — the proof breaks down entirely."

- question: "Explain in your own words why the proof of Euler's theorem works — why does multiplying all units modulo n by a fixed unit a give back the same set of units?"
  type: short-answer
  answer: "The units modulo n form a group under multiplication. If a is a unit (gcd(a,n)=1), multiplying any unit u by a gives another unit (since gcd(au, n) = 1 when gcd(a,n)=1 and gcd(u,n)=1), and the map u ↦ au is injective (cancellation holds for units). So the map sends the finite set of units to itself injectively — meaning it is a bijection, a rearrangement. The product of all units equals the product of their images under this rearrangement. Setting these equal gives a^φ(n) · (product of units) ≡ (product of units) (mod n), and canceling the product of units (which is itself a unit, hence invertible) yields a^φ(n) ≡ 1 (mod n)."
  explanation: "This 'rearrangement argument' is elegant because it requires no calculation — just the observation that a bijection from a finite set to itself preserves the product. The same argument proves Fermat's Little Theorem as a special case and generalizes to any finite group (as Lagrange's theorem): the order of any element divides the order of the group."
```

## Explainer

You already know from the totient function that φ(n) counts how many integers from 1 to n share no common factor with n — the **units modulo n**. Euler's theorem makes a powerful claim about what happens when you raise any such unit to the φ(n) power: you always land on 1. Think of this as a "reset" — repeated multiplication eventually cycles back to the identity.

To build intuition, consider n = 10 and a = 3. We have φ(10) = 4 (the units are 1, 3, 7, 9). Compute: 3¹ = 3, 3² = 9, 3³ = 27 ≡ 7 (mod 10), 3⁴ = 81 ≡ 1 (mod 10). The power cycle resets after exactly 4 steps. Euler's theorem guarantees this will happen for any a coprime to n — it might reset earlier (when the order divides φ(n)), but it always resets by step φ(n).

You may recognize a special case: if n = p is prime, then φ(p) = p − 1, and the theorem says a^(p−1) ≡ 1 (mod p) for any a not divisible by p. This is exactly **Fermat's Little Theorem**. Euler's theorem is the generalization that works for composite moduli too, which is why it has broader applications. The proof strategy is elegant: the set {a·1, a·3, a·7, a·9} (multiplying all units by a) is just a rearrangement of {1, 3, 7, 9} modulo n. Multiplying all elements on both sides yields a^φ(n) times the product of units ≡ that same product — cancel, and you get a^φ(n) ≡ 1.

The main application you'll encounter is **modular exponentiation for large numbers**. If you need to compute a^k mod n, you can reduce the exponent: a^k ≡ a^(k mod φ(n)) (mod n) when gcd(a, n) = 1. This is the mathematical engine behind RSA encryption, where message decryption requires computing m^d mod n for astronomically large numbers. Euler's theorem is what makes that computation tractable — without it, you could never decrypt quickly.
