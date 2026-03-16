---
id: modular-arithmetic
title: Modular Arithmetic and Congruences
domain: mathematics
course: discrete-math
prerequisites:
- id: divisibility-and-gcd
  type: hard
- id: euclidean-algorithm
  type: soft
- id: equivalence-relations
  type: soft
builds-toward:
- chinese-remainder-theorem
tags:
- modular-arithmetic
- congruence
- residue-classes
- clock-arithmetic
- modular-inverse
stage: formal-systems
status: validated
---

# Modular Arithmetic and Congruences

## Core Idea
Two integers a and b are congruent modulo n (written a ≡ b (mod n)) if n divides their difference a − b. Congruence is an equivalence relation that partitions the integers into n residue classes forming the ring ℤₙ. Addition, subtraction, and multiplication all respect congruence. A multiplicative inverse of a mod n exists if and only if gcd(a,n) = 1, and can be computed via the extended Euclidean algorithm. Fast exponentiation (repeated squaring) computes aᵏ mod n efficiently, underpinning RSA encryption.

## How It's Best Learned
Use clock arithmetic (mod 12) as an entry point — familiar from daily life. Practice reducing large expressions mod n, then computing modular inverses and powers. Carefully work through cases where inverses do not exist to understand the role of the gcd condition.

## Common Misconceptions
- Dividing both sides of a congruence by d without verifying gcd(d,n) = 1 first — this is a common error that gives wrong results.
- Assuming every nonzero element has a multiplicative inverse mod n — only elements coprime to n do.
- Confusing the expression a mod n = r with the congruence statement a ≡ r (mod n).

## Questions

```yaml
- question: "You want the multiplicative inverse of 3 modulo 7 — a number x such that 3x ≡ 1 (mod 7). What is x?"
  type: multiple-choice
  options: ["2", "3", "5", "6"]
  answer: 2
  explanation: "3 × 5 = 15 = 2(7) + 1, so 15 ≡ 1 (mod 7), confirming x = 5. The inverse exists because gcd(3,7) = 1. You can verify the other options: 3×2 = 6 ≢ 1, 3×3 = 9 ≡ 2, 3×6 = 18 ≡ 4. Only 5 works."

- question: "Since 4 ≡ 10 (mod 6) is true, dividing both sides by 2 gives the valid congruence 2 ≡ 5 (mod 6)."
  type: true-false
  answer: false
  explanation: "4 ≡ 10 (mod 6) is correct (both have remainder 4). But 2 ≢ 5 (mod 6) — their remainders differ. Division in modular arithmetic requires that gcd(divisor, modulus) = 1 for the modulus to stay the same; gcd(2,6) = 2 ≠ 1, so you cannot cancel 2 freely. This is one of the most common errors in modular arithmetic."

- question: "Why does a multiplicative inverse of a modulo n exist if and only if gcd(a, n) = 1?"
  type: short-answer
  answer: "We need ax ≡ 1 (mod n), i.e., n | (ax − 1), i.e., ax − ny = 1 for some integer y. By Bezout's theorem, integers x and y satisfying ax + ny = 1 exist exactly when gcd(a, n) = 1. If gcd(a, n) > 1, no such x exists because gcd(a,n) divides ax − ny but cannot divide 1."
  explanation: "Bezout's identity is the key: gcd(a,n) = 1 guarantees a linear combination ax + ny = 1 exists, which is precisely the condition that x is a modular inverse. The extended Euclidean algorithm finds this x efficiently."
```

## Explainer

You already understand divisibility: n divides a when a is a multiple of n. Modular arithmetic builds a full arithmetic system on top of divisibility. Instead of asking whether n divides (a − b) each time, we write a ≡ b (mod n) and work within residue classes — the n buckets into which all integers are sorted by their remainder when divided by n. The clock is the canonical mental model: on a 12-hour clock, 10 + 5 = 15, but we report 3, because 15 ≡ 3 (mod 12). The clock wraps around automatically.

The key algebraic fact is that addition, subtraction, and multiplication all commute with taking remainders: (a + b) mod n = ((a mod n) + (b mod n)) mod n. This means you can reduce large numbers early in a computation rather than waiting until the end. Instead of computing 1000 × 999 and then taking mod 7, you can reduce first: 1000 ≡ 6, 999 ≡ 5, and 6 × 5 = 30 ≡ 2 (mod 7). This makes computations tractable even when the numbers involved are astronomically large — a property essential for cryptography.

Multiplicative inverses are where modular arithmetic becomes more interesting — and trickier — than simple clock arithmetic. A multiplicative inverse of a mod n is a number x such that ax ≡ 1 (mod n). This is the modular version of division. By Bezout's identity, such an x exists if and only if gcd(a, n) = 1. When n is prime, every nonzero element has an inverse; when n is composite, some elements don't. This is why cryptographic systems typically use prime moduli — they guarantee a complete field where division always works. The extended Euclidean algorithm (which you may know from the euclidean-algorithm prerequisite) computes these inverses efficiently.

The most seductive error in modular arithmetic is cancellation: "if ac ≡ bc (mod n), then a ≡ b (mod n)." This is not always true. You can cancel c only when gcd(c, n) = 1. Otherwise, the modulus must be adjusted: ac ≡ bc (mod n) implies a ≡ b (mod n/gcd(c,n)). The example 4 ≡ 10 (mod 6) shows the danger — dividing by 2 gives 2 ≡ 5 (mod 3), not (mod 6). Always check the gcd before canceling.

Fast exponentiation (repeated squaring) lets you compute aᵏ mod n in O(log k) multiplications. The idea: a⁸ = ((a²)²)² — eight multiplications collapse to three squarings, each followed by a mod-n reduction to keep numbers small. This algorithm is the workhorse of RSA encryption: every HTTPS response your browser receives depends on computing something like 2¹⁰²⁴ mod p efficiently. From modular congruences and the gcd condition, you now have the foundation to understand why RSA works and what it means for a system to be cryptographically secure.
