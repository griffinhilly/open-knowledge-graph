---
id: carmichael-function-and-numbers
title: Carmichael Function and Carmichael Numbers
domain: mathematics
course: discrete-math
prerequisites:
- id: euler-totient-function
  type: hard
- id: fermat-little-theorem
  type: soft
tags:
- number-theory
- carmichael
- prime-testing
stage: formal-systems
status: draft
---

# Carmichael Function and Carmichael Numbers

## Core Idea
The Carmichael function λ(n) is the exponent of the multiplicative group modulo n. Carmichael numbers are composite numbers n where aⁿ⁻¹ ≡ 1 (mod n) for all a coprime to n, making them pseudoprimes to all bases. Understanding them is essential for probabilistic primality testing.

## Explainer

You already know Euler's totient function φ(n), which counts how many integers from 1 to n are coprime to n. You also know that for any such integer a, the multiplicative order of a modulo n divides φ(n) — meaning a^φ(n) ≡ 1 (mod n). But φ(n) is often larger than necessary: it counts elements, but what you really want is the smallest exponent that works for *all* of them simultaneously. That smaller value is the **Carmichael function** λ(n), defined as the **exponent** of the multiplicative group (ℤ/nℤ)×.

Concretely, λ(n) is the least positive integer m such that a^m ≡ 1 (mod n) for every a coprime to n. For prime p, λ(p) = p−1 = φ(p), so nothing changes. For prime powers and composites, λ(n) can be a proper divisor of φ(n). For example, λ(12) = 2 even though φ(12) = 4, because every integer coprime to 12 satisfies a² ≡ 1 (mod 12). The formula for λ on prime powers is: λ(2) = 1, λ(4) = 2, λ(2^k) = 2^(k−2) for k ≥ 3, and λ(p^k) = p^(k−1)(p−1) for odd primes p. For composite n, λ(n) = lcm of λ over the prime-power factors.

Carmichael numbers arise from a subtle flaw in Fermat's primality test. Fermat's little theorem says a^(p−1) ≡ 1 (mod p) for all a coprime to p — so if this congruence *fails*, p is definitely composite. The test checks this as a primality certificate. A **Carmichael number** is a composite n that passes this test for *every* base a coprime to n: a^(n−1) ≡ 1 (mod n) for all gcd(a,n) = 1. The smallest example is 561 = 3 × 7 × 11. Because λ(561) = lcm(2, 6, 10) = 30 divides 560 = n−1, every valid base satisfies the Fermat condition — despite 561 being composite.

The **Korselt criterion** characterizes Carmichael numbers elegantly: a squarefree composite n is Carmichael if and only if (p−1) | (n−1) for every prime p dividing n. This directly connects the structure of Carmichael numbers to the Carmichael function: the condition guarantees λ(n) | (n−1). Infinitely many Carmichael numbers exist (proved by Alford, Granville, and Pomerance in 1994), which means Fermat's test alone is not a reliable primality test. Modern primality tests like Miller-Rabin specifically address this weakness by choosing bases adversarially and checking additional conditions that Carmichael numbers cannot satisfy for all bases.
