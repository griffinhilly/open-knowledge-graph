---
id: eulers-theorem
title: Euler's Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: fermats-little-theorem
  type: soft
- id: eulers-totient-function
  type: hard
builds-toward:
- cryptographic-applications-rsa
tags:
- euler-theorem
- totient
- modular-exponentiation
stage: advanced
status: draft
---

# Euler's Theorem

## Core Idea
If gcd(a,n) = 1, then a^φ(n) ≡ 1 (mod n). This generalizes Fermat's Little Theorem to any modulus and is fundamental to RSA encryption, where φ(pq) = (p-1)(q-1) plays a central role.

## How It's Best Learned
Prove via group theory: (Z/nZ)* has order φ(n). Verify with examples like a=3, n=7, computing φ(7)=6 and checking 3^6 ≡ 1 (mod 7).

## Common Misconceptions
Forgetting the gcd(a,n) = 1 requirement. Confusing φ(n) with p-1 in the general case.

## Questions

```yaml
- question: "You want to apply Euler's theorem to compute 6^20 (mod 9). You check that φ(9) = 6. Does the theorem guarantee 6^6 ≡ 1 (mod 9)?"
  type: multiple-choice
  options:
    - "Yes — φ(9) = 6 and 6 < 9, so the theorem applies"
    - "No — gcd(6, 9) = 3 ≠ 1, so 6 is not in (ℤ/9ℤ)* and the theorem does not apply"
    - "Yes — Euler's theorem applies to any integer and any modulus"
    - "No — the theorem only applies when n is prime"
  answer: 1
  explanation: "Euler's theorem requires gcd(a, n) = 1. Here gcd(6, 9) = 3, so 6 shares a factor with 9. The element 6 is not in the multiplicative group (ℤ/9ℤ)*, and the theorem gives no guarantee. Checking: 6^6 = 46656 = 5184 × 9, so 6^6 ≡ 0 (mod 9) — not 1. The coprimality condition is not a technicality; it defines exactly which elements the theorem covers."

- question: "Euler's theorem states a^φ(n) ≡ 1 (mod n) when gcd(a,n) = 1. Which of the following best explains WHY the exponent φ(n) appears specifically?"
  type: multiple-choice
  options:
    - "φ(n) is the smallest integer k such that a^k ≡ 1 (mod n) for every a coprime to n"
    - "The elements coprime to n form a multiplicative group of order φ(n), and by Lagrange's theorem any element raised to the group order equals the identity"
    - "φ(n) is defined so that a^φ(n) ≡ 1 always holds, making the theorem circular"
    - "It follows directly from the prime factorization of n without needing group theory"
  answer: 1
  explanation: "The integers coprime to n form the multiplicative group (ℤ/nℤ)*, which has exactly φ(n) elements. Lagrange's theorem states that the order of any element divides the order of the group. So the sequence a, a², a³, ... must return to 1 within φ(n) steps. Note that φ(n) need not be the *smallest* such exponent — the order of a divides φ(n) but may be smaller. The group-theoretic structure explains why φ(n) works for every coprime a simultaneously."

- question: "Euler's theorem states a^φ(n) ≡ 1 (mod n) for all integers a and all positive integers n."
  type: true-false
  answer: false
  explanation: "The theorem requires the additional condition gcd(a, n) = 1. When a shares a common factor with n, the element a is not in the multiplicative group (ℤ/nℤ)* and the conclusion fails. For example, gcd(2, 10) = 2 ≠ 1, and 2^4 = 16 ≡ 6 (mod 10), not 1. The coprimality condition is essential — omitting it is the most common error when applying the theorem."

- question: "Fermat's Little Theorem (a^(p−1) ≡ 1 (mod p) for prime p with gcd(a,p) = 1) is a special case of Euler's Theorem."
  type: true-false
  answer: true
  explanation: "When n = p is prime, every integer from 1 to p−1 is coprime to p, so φ(p) = p − 1. Substituting into Euler's theorem gives a^(p−1) ≡ 1 (mod p), which is exactly Fermat's Little Theorem. Euler's theorem is the generalization that covers any modulus n, not just primes — it was specifically designed to extend the result beyond the prime case."

- question: "Why is the condition gcd(a, n) = 1 necessary for Euler's theorem, and what goes wrong when it fails?"
  type: short-answer
  answer: "The proof relies on the elements coprime to n forming a multiplicative group (ℤ/nℤ)*. A group requires every element to have a multiplicative inverse mod n — which is only possible when gcd(a, n) = 1. When gcd(a, n) > 1, a has no inverse mod n, it cannot be in the group, and repeated multiplication by a does not cycle back to 1. For instance, multiplying by 2 mod 6 cycles through 2, 4, 2, 4, ... — never reaching 1. The Lagrange's theorem argument that guarantees a^φ(n) ≡ 1 simply does not apply outside the group."
  explanation: "In RSA, this is exactly why the plaintext message m must satisfy gcd(m, pq) = 1. For large primes p and q, this holds for every m < pq that isn't a multiple of p or q — an astronomically rare failure case in practice. Understanding why the coprimality condition is necessary, not just a side constraint, is what separates mechanical use of the theorem from genuine understanding of how it works."
```

## Explainer

Euler's theorem sits at the heart of modern cryptography, but its logic flows naturally from your prerequisite: Euler's totient function φ(n), which counts how many integers from 1 to n share no common factor with n. Those integers form a group under multiplication modulo n — call it (ℤ/nℤ)*. This group has exactly φ(n) elements, and that group structure is the key to everything.

Here's the argument in plain language. Pick any element a in (ℤ/nℤ)* — that is, any integer coprime to n. Multiplying a by itself repeatedly (mod n) cycles through a sequence: a, a², a³, ... This sequence must eventually repeat, because there are only finitely many residues. When it repeats, you've found a subgroup, and by Lagrange's theorem, the order of any subgroup divides the order of the whole group. Since the whole group has order φ(n), the sequence must satisfy a^φ(n) ≡ 1 (mod n).

The theorem generalizes Fermat's Little Theorem, which is the special case where n = p is prime. When n = p, φ(p) = p − 1, so a^(p−1) ≡ 1 (mod p). Euler's theorem works for any modulus. For example, φ(10) = 4 (the coprimes to 10 are 1, 3, 7, 9), so 3^4 = 81 ≡ 1 (mod 10). Check: 81 = 8×10 + 1. ✓

The gcd(a, n) = 1 condition is not optional. If a shares a factor with n, then a is not in the group (ℤ/nℤ)* at all — the argument collapses. For instance, gcd(2, 10) = 2, and 2^4 = 16 ≡ 6 (mod 10), not 1. The coprimality condition defines exactly the elements for which the theorem holds. In RSA encryption, this is precisely why n = pq is chosen with φ(pq) = (p−1)(q−1): it guarantees that encryption and decryption are inverses modulo φ(n), making the entire scheme work.
