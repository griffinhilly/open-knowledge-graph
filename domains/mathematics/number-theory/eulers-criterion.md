---
id: eulers-criterion
title: Euler's Criterion
domain: mathematics
course: number-theory
prerequisites:
- id: quadratic-residues-legendre-symbol
  type: hard
- id: fermats-little-theorem
  type: hard
builds-toward:
- law-quadratic-reciprocity
tags:
- eulers-criterion
- quadratic-residues
- legendre-symbol
stage: advanced
status: draft
---

# Euler's Criterion

## Core Idea
(a/p) ≡ a^((p-1)/2) (mod p). This criterion computes the Legendre symbol via modular exponentiation and reveals that quadratic residuosity is determined by the group structure of (Z/pZ)*.

## Questions

```yaml
- question: "To determine whether 5 is a quadratic residue mod 11 using Euler's Criterion (p = 11), what computation must you perform?"
  type: multiple-choice
  options:
    - "Check whether 5 divides 11 − 1 = 10"
    - "Compute 5^5 mod 11, since (p−1)/2 = 5"
    - "Compute 5^10 mod 11 to apply Fermat's Little Theorem directly"
    - "Find the square root of 5 mod 11 by testing all residue classes"
  answer: 1
  explanation: "Euler's Criterion says: compute a^((p−1)/2) mod p. For p = 11, (p−1)/2 = 5. So you compute 5^5 mod 11. If the result is 1, then 5 is a quadratic residue; if −1 (≡ 10 mod 11), then it is not. Actually: 5^2 = 25 ≡ 3, 5^4 ≡ 9, 5^5 ≡ 45 ≡ 1 (mod 11), so 5 is a QR mod 11 (indeed 4² = 16 ≡ 5). Option C computes a^(p−1) which always gives 1 by Fermat and tells you nothing. Option D works but is inefficient and misses the point of the criterion."

- question: "Suppose you compute a^((p−1)/2) ≡ −1 (mod p). What does this tell you about a?"
  type: multiple-choice
  options:
    - "a is a quadratic residue mod p because −1 is a perfect square in some fields"
    - "a is a quadratic non-residue mod p — it has no square root mod p"
    - "a ≡ −1 (mod p), so a = p − 1"
    - "The computation was performed incorrectly, since a^((p−1)/2) must equal 1 by Fermat's Little Theorem"
  answer: 1
  explanation: "Euler's Criterion gives a two-way test: a^((p−1)/2) ≡ 1 means QR; a^((p−1)/2) ≡ −1 means non-residue. The result −1 (mod p) is perfectly valid — it is the unique element of order 2 in (ℤ/pℤ)*, and it indicates that a is not a perfect square in that group. Option D is wrong because Fermat says a^(p−1) ≡ 1, which factors as (a^((p−1)/2))² ≡ 1 — this allows the half-power to be either 1 or −1, it does not force 1."

- question: "The fact that a^((p−1)/2) (mod p) must equal either 1 or −1 follows from Fermat's Little Theorem via the factorization (a^((p−1)/2) − 1)(a^((p−1)/2) + 1) ≡ 0 (mod p) and the primality of p."
  type: true-false
  answer: true
  explanation: "Fermat's Little Theorem gives a^(p−1) ≡ 1 (mod p), so a^(p−1) − 1 ≡ 0. This factors as (a^((p−1)/2) − 1)(a^((p−1)/2) + 1) ≡ 0 (mod p). Since p is prime, ℤ/pℤ has no zero divisors, so one factor must be 0 — meaning a^((p−1)/2) ≡ 1 or a^((p−1)/2) ≡ −1. The primality of p is essential: for composite moduli, a product can be zero mod n without either factor being zero mod n."

- question: "Euler's Criterion holds for all moduli, not just prime moduli, since it follows from Fermat's Little Theorem which holds whenever gcd(a, n) = 1."
  type: true-false
  answer: false
  explanation: "Fermat's Little Theorem holds only for prime moduli. For composite n, the order of (ℤ/nℤ)* may not be n−1, and (ℤ/nℤ)* may not even be cyclic. The factorization argument that forces a^((p−1)/2) to be ±1 depends on p being prime (so ℤ/pℤ is a field with no zero divisors). For composite moduli, a^((n−1)/2) need not equal the Legendre symbol, and the Jacobi symbol (the generalization) does not reliably indicate quadratic residuosity."

- question: "Using the group structure of (ℤ/pℤ)*, explain why a^((p−1)/2) ≡ 1 (mod p) if and only if a is a perfect square in that group."
  type: short-answer
  answer: "(ℤ/pℤ)* is cyclic of order p−1 with generator g. Every element a = g^k for some k. The element a is a perfect square iff k is even (since g^k = (g^(k/2))² requires k/2 to be an integer). Now compute a^((p−1)/2) = g^(k(p−1)/2). If k is even, the exponent k(p−1)/2 is a multiple of p−1, so by Fermat g^(k(p−1)/2) = (g^(p−1))^(k/2) = 1. If k is odd, the exponent k(p−1)/2 is an odd multiple of (p−1)/2, and since g^((p−1)/2) is the unique element of order 2 in the group (which equals −1 mod p), the result is −1. So the test a^((p−1)/2) ≡ 1 perfectly detects even k, i.e., perfect squares."
  explanation: "The group-theoretic argument shows why the criterion is not a coincidence: it is a direct consequence of the cyclic structure of (ℤ/pℤ)*. Squares are exactly the elements with even discrete logarithm, and raising to the (p−1)/2 power is exactly the parity-detection map in that cyclic group."
```

## Explainer

You already know two things that Euler's Criterion connects: the **Legendre symbol** (a/p), which tells you whether a is a quadratic residue mod p, and **Fermat's Little Theorem**, which tells you a^(p-1) ≡ 1 (mod p) for any a not divisible by p. Euler's Criterion is what happens when you ask: can Fermat's Little Theorem tell us about squares?

The key algebraic step is to factor. Since a^(p-1) ≡ 1 (mod p), we have a^(p-1) - 1 ≡ 0 (mod p), which factors as (a^((p-1)/2) - 1)(a^((p-1)/2) + 1) ≡ 0 (mod p). Because p is prime, one of the factors must be zero mod p — so a^((p-1)/2) is either 1 or -1 (mod p). Euler's Criterion asserts exactly which outcome corresponds to which: a is a quadratic residue mod p if and only if a^((p-1)/2) ≡ 1 (mod p), and a non-residue if and only if a^((p-1)/2) ≡ -1 (mod p).

Why does this work? Consider the **multiplicative group** (ℤ/pℤ)*, which is cyclic of order p-1. Every element can be written as g^k for a fixed generator g. The element g^k is a perfect square in this group if and only if k is even, because g^k = (g^(k/2))² only makes sense when k/2 is an integer. Now compute (g^k)^((p-1)/2) = g^(k(p-1)/2). If k is even, this equals (g^(p-1))^(k/2) = 1^(k/2) = 1 by Fermat. If k is odd, the exponent k(p-1)/2 is not a multiple of p-1, and the result is g^((p-1)/2) — the unique element of order 2 in the group, which equals -1 (mod p). The exponent test perfectly separates squares from non-squares.

In practice, Euler's Criterion turns a question about square roots into a fast modular exponentiation. To decide whether 7 is a quadratic residue mod 11, compute 7^5 mod 11: 7² = 49 ≡ 5, 7⁴ ≡ 25 ≡ 3, 7⁵ ≡ 21 ≡ 10 ≡ -1 (mod 11). So (7/11) = -1, meaning 7 has no square root mod 11 — far more efficient than checking all residue classes individually. This computational power, rooted in the group structure of (ℤ/pℤ)*, is what makes the criterion foundational for the deeper theory of quadratic reciprocity.
