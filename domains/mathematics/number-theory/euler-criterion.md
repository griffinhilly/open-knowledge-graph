---
id: euler-criterion
title: Euler's Criterion for Quadratic Residues
domain: mathematics
course: number-theory
prerequisites:
- id: quadratic-residues-and-legendre-symbol
  type: hard
- id: fermat-little-theorem
  type: soft
builds-toward:
- law-of-quadratic-reciprocity
tags:
- quadratic-residues
- legendre-symbol
- fermat-little-theorem
stage: advanced
status: draft
---

# Euler's Criterion for Quadratic Residues

## Core Idea
Euler's criterion states that a^((p−1)/2) ≡ (a/p) (mod p) for odd prime p and integer a. This provides an efficient computational method to evaluate the Legendre symbol and connects Fermat's Little Theorem to quadratic character theory.

## Questions

```yaml
- question: "Using Euler's criterion to evaluate (3/11): which computation gives the correct result, and what does it tell you?"
  type: multiple-choice
  options:
    - "3^5 ≡ 1 (mod 11), so 3 is a quadratic residue mod 11"
    - "3^10 ≡ 1 (mod 11), so 3 is a quadratic residue mod 11"
    - "3^5 ≡ −1 (mod 11), so 3 is a non-residue mod 11"
    - "We must enumerate all squares mod 11 to determine residuosity — Euler's criterion only confirms residues, not non-residues"
  answer: 0
  explanation: "The criterion says compute a^((p−1)/2) mod p. Here p=11, so the exponent is 5. Computing: 3^2=9, 3^4≡4, 3^5≡12≡1 (mod 11). Since this equals +1, (3/11)=1 and 3 is a QR. (Verify: 5²=25≡3 mod 11, confirming 3 is indeed a square.) Option B uses the full Fermat exponent (p−1), which always gives 1 and tells you nothing. Option D misses the point: Euler's criterion handles both residues and non-residues, outputting −1 in the latter case."

- question: "Why can a^((p−1)/2) only be congruent to 1 or −1 mod p, and not some other value?"
  type: multiple-choice
  options:
    - "Because the Legendre symbol only takes those two values, so the exponentiation must match"
    - "Because a^((p−1)/2) is a square root of a^(p−1) ≡ 1 (mod p), and a prime has only ±1 as square roots of unity"
    - "Because (p−1)/2 is always even when p is an odd prime"
    - "Because Fermat's Little Theorem guarantees that any power less than p−1 reduces to 1 or −1"
  answer: 1
  explanation: "The core argument: let x = a^((p−1)/2). Then x² = a^(p−1) ≡ 1 (mod p) by Fermat. So x is a square root of 1 mod p, meaning p | (x−1)(x+1). Since p is prime, it must divide one of the factors, giving x ≡ 1 or x ≡ −1. This is why the output is binary — it follows from primality, not from the definition of the Legendre symbol. Option A reverses the logic: the Legendre symbol is defined to match the exponentiation result, not the other way around."

- question: "If a^((p−1)/2) ≡ 1 (mod p), then a is a perfect square in the ordinary integers."
  type: true-false
  answer: false
  explanation: "Euler's criterion only tells you about squares modulo p. Many numbers that are not perfect squares in the integers are quadratic residues mod p. For example, 3 is not a perfect square in the integers, but 3 ≡ 5² (mod 11), so it is a QR mod 11. The criterion is a statement about modular arithmetic, not about the integers themselves."

- question: "Euler's criterion provides a computationally efficient method for evaluating the Legendre symbol, requiring only O(log p) multiplications via fast exponentiation."
  type: true-false
  answer: true
  explanation: "Evaluating (a/p) directly requires checking whether any b satisfies b² ≡ a (mod p), which in the naive approach scans up to (p−1)/2 values. Euler's criterion replaces this with modular exponentiation of a^((p−1)/2) mod p, which fast (repeated squaring) exponentiation computes in O(log p) multiplications — far more efficient for large primes."

- question: "Explain why the residue case of Euler's criterion holds: if a ≡ b² (mod p), why does a^((p−1)/2) ≡ 1 (mod p)?"
  type: short-answer
  answer: "If a ≡ b² (mod p), then a^((p−1)/2) ≡ (b²)^((p−1)/2) = b^(p−1) ≡ 1 (mod p) by Fermat's Little Theorem (since p is prime and gcd(b,p)=1)."
  explanation: "This is the cleanest direction of the proof. Substituting the definition of quadratic residue directly into the criterion, the exponent (p−1)/2 on b² becomes the full Fermat exponent on b — and Fermat's Little Theorem delivers 1 immediately. The non-residue direction is harder and requires arguing via primitive roots."
```

## Explainer

Your prerequisites give you two key tools. The **Legendre symbol** (a/p) tells you whether a is a quadratic residue mod p: it equals 1 if a ≡ b² (mod p) for some b, −1 if no such b exists, and 0 if p divides a. **Fermat's Little Theorem** says a^(p−1) ≡ 1 (mod p) whenever gcd(a, p) = 1. Euler's criterion connects these two results through a single computation.

The key observation is that a^((p−1)/2) is a square root of a^(p−1) ≡ 1 (mod p). The only square roots of 1 modulo a prime are 1 and −1 (since x²≡1 means p | (x−1)(x+1), forcing x≡1 or x≡−1). So a^((p−1)/2) must be either 1 or −1 mod p. The criterion asserts the value matches the Legendre symbol exactly: +1 when a is a quadratic residue, −1 when it is a non-residue.

To see why the residue case works: if a ≡ b² (mod p), then a^((p−1)/2) ≡ b^(p−1) ≡ 1 (mod p) by Fermat's Little Theorem. For non-residues, the argument uses the fact that the multiplicative group mod p is cyclic: if g is a primitive root, then non-residues are odd powers of g. An odd power raised to (p−1)/2 gives g^(odd·(p−1)/2), which is an odd multiple of (p−1)/2, necessarily ≡ −1 (mod p).

A concrete example makes this tangible. Take p = 7. Is 2 a quadratic residue mod 7? Check: 1²=1, 2²=4, 3²=2, 4²=2, 5²=4, 6²=1 — yes, 2≡3² (mod 7), so (2/7)=1. Euler's criterion confirms: 2^3 = 8 ≡ 1 (mod 7). Now try a = 3: 3^3 = 27 ≡ 6 ≡ −1 (mod 7), so (3/7) = −1 and 3 is a non-residue. The computational payoff is significant: evaluating (a/p) via a^((p−1)/2) mod p takes O(log p) multiplications using fast exponentiation, far more efficient than checking all squares manually.
