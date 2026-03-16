---
id: divisibility-and-gcd
title: Divisibility and Greatest Common Divisor
domain: mathematics
course: discrete-math
prerequisites:
- id: prime-and-composite-numbers
  type: hard
- id: mathematical-induction
  type: soft
builds-toward:
- euclidean-algorithm
- modular-arithmetic
- fundamental-theorem-of-arithmetic
tags:
- divisibility
- gcd
- lcm
- number-theory
- bezout
stage: formal-systems
status: validated
---

# Divisibility and Greatest Common Divisor

## Core Idea
An integer a divides b (a | b) if there exists an integer k such that b = ak. The greatest common divisor gcd(a,b) is the largest positive integer dividing both a and b. Bezout's identity guarantees integers x, y such that ax + by = gcd(a,b). The least common multiple satisfies lcm(a,b) = |ab|/gcd(a,b). These concepts are the algebraic foundation of number theory and underlie primality testing, modular arithmetic, and public-key cryptography.

## How It's Best Learned
Compute GCDs first by prime factorization to build intuition, then learn the Euclidean algorithm for efficiency. Prove Bezout's identity constructively. Connect GCD to familiar applications: simplifying fractions, finding when two periodic events coincide.

## Common Misconceptions
- Confusing GCD (largest common divisor) with LCM (smallest common multiple).
- Assuming gcd(a,b) must be prime — it can be any positive integer.
- Not knowing that Bezout coefficients x, y may be negative integers.

## Explainer

From your study of prime and composite numbers, you know that every integer greater than 1 factors uniquely into primes. Divisibility formalizes a related relationship: **a divides b** (written a | b) means b is an exact multiple of a — there exists a whole number k such that b = ak, with no remainder. Saying 6 | 42 is saying 42 = 6 × 7. If the division leaves a remainder, divisibility fails: 6 does not divide 43. This simple "exact fit" idea is the foundation of everything in number theory.

The **greatest common divisor** gcd(a,b) is the largest integer that divides both a and b. One approach is via prime factorizations: find all primes the two numbers share and take the lowest power of each. For 12 = 2²·3 and 18 = 2·3², the shared primes are 2 and 3, giving gcd(12,18) = 2¹·3¹ = 6. This method builds directly on your prime-factorization knowledge, but it is slow for large numbers — which is why the Euclidean algorithm (your next topic) matters. The **least common multiple** is the flip side: take the *maximum* power of every prime appearing in either number. The connecting formula lcm(a,b) = |ab| / gcd(a,b) ties the two together cleanly. A practical image: two gears with 12 and 18 teeth realign every lcm(12,18) = 36 tooth-advances.

**Bézout's identity** elevates GCD from an arithmetic curiosity to an algebraic tool. For any integers a and b, there exist integers x and y (which may be zero or negative) such that ax + by = gcd(a,b). For 12 and 18: 12·(−1) + 18·(1) = 6. This means the GCD is not just the largest common divisor — it is also the *smallest positive integer expressible as a linear combination of a and b*. The coefficients x and y are called **Bézout coefficients** and may be negative, which surprises students who expect them to be positive. Finding these coefficients explicitly uses the extended Euclidean algorithm.

The applications reach far beyond elementary arithmetic. GCD determines when two periodic processes sync up. It tells you when a fraction is fully reduced (a/b is in lowest terms when gcd(a,b) = 1, meaning a and b are **coprime**). Bézout's identity is the key lemma behind modular arithmetic: if gcd(a,m) = 1, then a has a multiplicative inverse modulo m, which is what makes public-key cryptography possible. Every result in that direction traces back to the simple question of when one integer divides another exactly.
