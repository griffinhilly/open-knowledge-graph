---
id: fermats-little-theorem
title: Fermat's Little Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: congruence-properties
  type: hard
- id: group-definition-and-examples
  type: soft
builds-toward:
- eulers-theorem
- rsa-cryptography
tags:
- fermats-little-theorem
- prime-powers
- modular-exponentiation
stage: advanced
status: validated
---

# Fermat's Little Theorem

## Core Idea
If p is prime and gcd(a,p) = 1, then a^(p-1) ≡ 1 (mod p). This cornerstone result characterizes the exponent structure of multiplicative groups mod p and enables fast modular exponentiation in cryptography.

## Questions

```yaml
- question: "What is 3^100 mod 7?"
  type: multiple-choice
  options:
    - "1"
    - "4"
    - "2"
    - "6"
  answer: 1
  explanation: "By Fermat's Little Theorem, 3^6 ≡ 1 (mod 7) since 7 is prime and gcd(3,7) = 1. Write 100 = 16·6 + 4. Then 3^100 = (3^6)^16 · 3^4 ≡ 1 · 81 ≡ 81 (mod 7). Since 81 = 11·7 + 4, we get 3^100 ≡ 4 (mod 7). The key step is reducing the exponent 100 modulo p−1 = 6, not modulo p = 7 — a common error that would give the wrong answer."

- question: "To compute 2^1000 mod 17 using Fermat's Little Theorem, you should first reduce the exponent 1000 modulo which number?"
  type: multiple-choice
  options:
    - "17, because all arithmetic is done mod 17"
    - "16, because FLT gives 2^16 ≡ 1 (mod 17), so the exponent repeats with period 16"
    - "1000, because the theorem applies to the base, not the exponent"
    - "8, because you use half of p−1 for even bases"
  answer: 1
  explanation: "Fermat's Little Theorem says a^(p−1) ≡ 1 (mod p), so the exponent repeats with period p−1 = 16. Write 1000 = 62·16 + 8, so 2^1000 ≡ (2^16)^62 · 2^8 ≡ 1 · 256 ≡ 256 (mod 17). Since 256 = 15·17 + 1, the answer is 1. Reducing the exponent mod p instead of mod p−1 is the most common error — it gives 1000 mod 17 = 14, which produces the wrong result."

- question: "For any prime p and any integer a — including multiples of p — the congruence a^p ≡ a (mod p) holds."
  type: true-false
  answer: true
  explanation: "The corollary a^p ≡ a (mod p) is valid for all integers a. When gcd(a,p) = 1, it follows from a^(p−1) ≡ 1 by multiplying both sides by a. When p | a, both sides equal 0 mod p. The corollary is more convenient than the main theorem precisely because it requires no divisibility check — useful in proofs and applications where you cannot assume gcd(a,p) = 1."

- question: "Fermat's Little Theorem states that a^(p−1) ≡ 1 (mod p) for most integer a when p is prime."
  type: true-false
  answer: false
  explanation: "The theorem requires gcd(a, p) = 1 — that is, p does not divide a. If p | a, then a ≡ 0 (mod p), so a^(p−1) ≡ 0 (mod p), not 1. For example, 7^6 ≡ 0 (mod 7), not 1. The condition gcd(a,p) = 1 ensures a belongs to the multiplicative group (Z/pZ)*, which has order p−1; the theorem follows from the fact that every group element's order divides the group order."

- question: "Explain why the set {a, 2a, 3a, ..., (p−1)a} reduced modulo a prime p must be a permutation of {1, 2, ..., p−1} when gcd(a,p) = 1, and how this implies Fermat's Little Theorem."
  type: short-answer
  answer: "If two elements ka and la were congruent mod p — that is, p | (k−l)a — then since p is prime and gcd(a,p) = 1, p must divide k−l. But k and l are both in {1,...,p−1}, so |k−l| < p, forcing k = l. Thus all p−1 elements are distinct and nonzero mod p, so they must be exactly {1,...,p−1} in some order. Multiplying both sides of a·2a·...·(p−1)a ≡ 1·2·...·(p−1) (mod p) gives a^(p−1)·(p−1)! ≡ (p−1)! (mod p). Since (p−1)! is nonzero mod p, canceling it yields a^(p−1) ≡ 1 (mod p)."
  explanation: "This 'scrambling' proof uses only the pigeonhole principle and basic properties of primes — no group theory required. It also reveals why primality is essential: if p were composite, gcd(a,p) = 1 would not prevent two multiples ka and la from colliding mod p, and the permutation argument would fail."
```

## Explainer

You already know from congruence properties that modular arithmetic is self-consistent: if a ≡ b (mod p), then a^k ≡ b^k (mod p). Fermat's Little Theorem takes this arithmetic into the multiplicative structure: if p is prime and a is not divisible by p, then a^(p-1) ≡ 1 (mod p). The key intuition comes from examining the set of multiples {a, 2a, 3a, ..., (p-1)a} reduced mod p. Because p is prime and gcd(a, p) = 1, these p-1 values are all distinct and nonzero — they produce the set {1, 2, ..., p-1} in some scrambled order. So their product equals the product of all nonzero residues: a · 2a · 3a · ... · (p-1)a ≡ 1 · 2 · 3 · ... · (p-1) (mod p). Factoring out a^(p-1) from the left yields a^(p-1) · (p-1)! ≡ (p-1)! (mod p). Since (p-1)! is nonzero mod p, cancel it to get a^(p-1) ≡ 1 (mod p).

The theorem has a tidy corollary: for any integer a (not just those coprime to p), a^p ≡ a (mod p). This form is often more convenient because no divisibility check is needed. Both forms appear throughout number theory and in computing.

The practical power is enormous. **Modular exponentiation** — the engine of RSA encryption — relies on reducing large exponents mod (p-1). For example, to compute 7^100 mod 13: since 13 is prime, 7^12 ≡ 1 (mod 13). Write 100 = 8·12 + 4, so 7^100 = (7^12)^8 · 7^4 ≡ 1^8 · 7^4 ≡ 7^4 ≡ 2401 ≡ 9 (mod 13). Without Fermat's Little Theorem, this computation over cryptographic-scale numbers — hundreds of digits long — would be infeasible.

If you have encountered group theory, the result has a clean restatement: the nonzero residues mod p form a **multiplicative group** of order p-1. By Lagrange's theorem, every element's order divides the group order, so a^(p-1) = 1 for all elements a. Fermat's Little Theorem is Lagrange's theorem specialized to the group (Z/pZ)*. This group-theoretic view also explains why the exponent is p-1 specifically: it equals the size of the group, not an arbitrary bound.
