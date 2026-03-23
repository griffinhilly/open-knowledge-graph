---
id: fermat-little-theorem
title: Fermat's Little Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: modular-arithmetic
  type: hard
- id: group-definition-and-examples
  type: soft
builds-toward:
- euler-theorem
- rsa-cryptography
tags:
- modular-arithmetic
- group-theory
- primes
- fermat
stage: advanced
status: validated
---

# Fermat's Little Theorem

## Core Idea
If p is prime and gcd(a, p) = 1, then a^(p−1) ≡ 1 (mod p). This theorem follows from Lagrange's theorem applied to the multiplicative group (ℤ/pℤ)* and forms the basis for Fermat primality tests and many cryptographic algorithms.

## How It's Best Learned
Derive it from group theory using the multiplicative group mod p. Verify with numerical examples (e.g., 2^4 ≡ 1 (mod 5)). Apply it to compute large powers modulo p efficiently.

## Common Misconceptions
The converse is false: a^(n−1) ≡ 1 (mod n) does not imply n is prime (Carmichael numbers counterexample: 561 = 3·11·17). The condition gcd(a, p) = 1 is essential; the theorem fails when a is divisible by p.

## Questions

```yaml
- question: "You need to compute 3^100 (mod 7). Using Fermat's Little Theorem, the most efficient approach is..."
  type: multiple-choice
  options:
    - "Compute 3^100 directly by repeated squaring, then reduce mod 7 at the end"
    - "Use 3^6 ≡ 1 (mod 7), write 100 = 16×6 + 4, so 3^100 ≡ 3^4 = 81 ≡ 4 (mod 7)"
    - "Apply the corollary 3^7 ≡ 3 (mod 7) and write 100 as a multiple of 7 to reduce"
    - "Reduce the base: since 3 < 7, conclude 3^100 ≡ 1 (mod 7) by the theorem"
  answer: 1
  explanation: "Since 7 is prime and gcd(3, 7) = 1, Fermat's Little Theorem gives 3^6 ≡ 1 (mod 7). Dividing the exponent: 100 = 16×6 + 4, so 3^100 = (3^6)^16 × 3^4 ≡ 1^16 × 81 ≡ 81 (mod 7). Since 81 = 11×7 + 4, the answer is 4. Option D is a common mistake: the theorem says a^(p−1) ≡ 1, not a^n ≡ 1 for arbitrary n — the exponent must be p−1 = 6, not 100. Option C uses the corollary a^p ≡ a, but 100 is not easily expressed as a power of 7."

- question: "A primality test checks whether n = 561 satisfies a^560 ≡ 1 (mod 561) for several randomly chosen values of a coprime to 561. Every test passes. Can we conclude 561 is prime?"
  type: multiple-choice
  options:
    - "Yes — if a^(n−1) ≡ 1 (mod n) holds for multiple bases, n must be prime by Fermat's theorem"
    - "No — 561 = 3×11×17 is a Carmichael number, and Carmichael numbers satisfy a^(n−1) ≡ 1 (mod n) for all a coprime to n, even though they are composite"
    - "Yes, but only if we test at least p−1 different bases"
    - "No — but only because we should test a = 2 specifically; any other base gives false positives"
  answer: 1
  explanation: "The converse of Fermat's Little Theorem is false. Carmichael numbers are composite integers that satisfy a^(n−1) ≡ 1 (mod n) for every a coprime to n — they are 'absolute pseudoprimes' that defeat the Fermat test completely. 561 = 3×11×17 is the smallest Carmichael number. No matter how many bases you test, 561 will pass the Fermat test for all of them. This is why Fermat's test establishes only 'probable primality' — it definitively identifies composites (if it fails, n is composite), but cannot confirm primality. Stronger tests like Miller-Rabin close this gap."

- question: "If p is prime and a is divisible by p, then a^(p−1) ≡ 1 (mod p)."
  type: true-false
  answer: false
  explanation: "Fermat's Little Theorem requires gcd(a, p) = 1 — a must not be divisible by p. If p divides a, then a ≡ 0 (mod p), and 0^(p−1) = 0 ≢ 1 (mod p). The multiplicative group (ℤ/pℤ)* consists only of the nonzero residues {1, 2, …, p−1}; zero is not a member of this group. The theorem is a statement about elements of the multiplicative group, so it only applies when a is not a multiple of p."

- question: "For any prime p and any integer a (whether or not a is divisible by p), it is true that a^p ≡ a (mod p)."
  type: true-false
  answer: true
  explanation: "This corollary covers all integers a. Case 1: if gcd(a, p) = 1, Fermat's Little Theorem gives a^(p−1) ≡ 1 (mod p), and multiplying both sides by a gives a^p ≡ a (mod p). Case 2: if p divides a, then a ≡ 0 (mod p), so a^p ≡ 0^p = 0 ≡ a (mod p). Both cases satisfy a^p ≡ a (mod p). This unified form is often more convenient in proofs — it applies unconditionally with no coprimality requirement."

- question: "Why does passing the Fermat primality test — even for many different base values — not guarantee that n is prime?"
  type: short-answer
  answer: "Carmichael numbers are composite integers that satisfy a^(n−1) ≡ 1 (mod n) for every integer a coprime to n. They are counterexamples to the converse of Fermat's Little Theorem. For such numbers, the Fermat test will pass for every valid base, giving no indication that n is composite. Because Carmichael numbers exist (infinitely many, in fact), the Fermat test can only identify non-primes (a failure guarantees compositeness) but cannot confirm primality. Deterministic primality requires tests like Miller-Rabin that use additional structural properties of primes beyond the basic group order argument."
  explanation: "The Fermat test works by verifying a consequence of primality (the multiplicative group has order p−1). Carmichael numbers mimic this consequence for all bases without being prime — they are composite but structured so that their multiplicative group order divides n−1 for all coprime bases. Miller-Rabin adds a check for 'non-trivial square roots of 1 mod n,' which genuine primes cannot have, filtering out Carmichael numbers. For RSA key generation, Miller-Rabin's stronger guarantees are essential."
```

## Explainer

From your work with modular arithmetic, you know that integers mod p form a system where addition and multiplication wrap around. When p is prime, something special happens: every nonzero element has a multiplicative inverse mod p. This means the nonzero residues {1, 2, ..., p−1} form a **multiplicative group** under multiplication mod p, denoted (ℤ/pℤ)*. Its size — the **order** of the group — is p−1.

Fermat's Little Theorem follows almost immediately from one key fact about groups: for any element a in a finite group of order n, raising a to the power n gives the identity. In (ℤ/pℤ)*, the identity is 1 and the group has order p−1, so a^(p−1) ≡ 1 (mod p) for any a not divisible by p. If you haven't seen the group-theoretic proof yet, there's a more elementary argument: list the p−1 nonzero residues, then consider the list multiplied by a (mod p). Because a is coprime to p, the new list is a permutation of the old one. So the product of both lists must be equal mod p — the a^(p−1) factor cancels against the same product, leaving a^(p−1) ≡ 1.

A useful corollary restates the theorem as a^p ≡ a (mod p) for *all* integers a (including multiples of p, where both sides are 0). This version is often more convenient in proofs. The practical power of the theorem is **modular exponentiation**: to compute 7^1000 (mod 13), note that 13 is prime and 7 is coprime to 13, so 7^12 ≡ 1 (mod 13). Write 1000 = 83 × 12 + 4, so 7^1000 = (7^12)^83 · 7^4 ≡ 1^83 · 7^4 ≡ 2401 ≡ 9 (mod 13). A computation that seemed impossible becomes routine.

The one trap to watch: the converse fails. If a^(n−1) ≡ 1 (mod n), you cannot conclude n is prime. **Carmichael numbers** like 561 = 3 · 11 · 17 satisfy this equation for all a coprime to n, even though they are composite. This is why Fermat's test is only a *probable* primality check — it identifies non-primes efficiently (if the equation fails, n is definitely composite), but passing the test is not a guarantee of primality. This gap is closed by more sophisticated tests like Miller–Rabin, which also underpins the RSA cryptographic system you will encounter next.
