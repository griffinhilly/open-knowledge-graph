---
id: euclidean-algorithm-gcd
title: The Euclidean Algorithm and Greatest Common Divisor
domain: mathematics
course: discrete-math
prerequisites:
- id: modular-arithmetic-congruences
  type: hard
builds-toward:
- chinese-remainder-theorem
tags:
- number-theory
- gcd
- algorithm
stage: formal-systems
status: draft
---

# The Euclidean Algorithm and Greatest Common Divisor

## Core Idea
The Euclidean algorithm efficiently computes gcd(a,b) using repeated division: gcd(a,b) = gcd(b, a mod b), stopping when the remainder is 0. Time complexity is O(log(min(a,b))). The extended Euclidean algorithm finds integers x, y such that ax + by = gcd(a,b).

## Explainer

The **greatest common divisor** gcd(a, b) is the largest integer that divides both a and b. A naive approach — list all divisors of both numbers and find the largest shared one — is painfully slow for large numbers. The Euclidean algorithm exploits a key insight from your prerequisite modular arithmetic: gcd(a, b) = gcd(b, a mod b). This follows because any common divisor of a and b also divides a − qb = a mod b, and vice versa — the set of common divisors is unchanged when you replace a with its remainder mod b.

The algorithm repeatedly applies this reduction: gcd(252, 105) → gcd(105, 42) → gcd(42, 21) → gcd(21, 0) = 21. Each step shrinks the problem: the new pair (b, a mod b) is strictly smaller than (a, b). In the worst case the size halves every two steps, so the total number of steps is O(log(min(a, b))). This logarithmic time complexity makes the algorithm practical for numbers with hundreds of digits — a massive improvement over naive factoring.

The **extended Euclidean algorithm** goes further: it finds integers x and y such that ax + by = gcd(a, b). This is **Bézout's identity**. The algorithm works by tracing the computation backwards. For the example above: 21 = 105 − 2(42) = 105 − 2(252 − 2·105) = 5·105 − 2·252, giving x = −2, y = 5. The back-substitution systematically expresses each remainder as a linear combination of the original inputs, and the last nonzero remainder (the GCD) ends up as that combination.

Bézout coefficients are the key to **modular inverses**: if gcd(a, n) = 1, then ax ≡ 1 (mod n), meaning x is the multiplicative inverse of a modulo n. The extended Euclidean algorithm computes this inverse directly, in O(log n) time. This is why it appears as a core subroutine inside the Chinese Remainder Theorem and RSA cryptography. Understanding the Euclidean algorithm is therefore not just about GCD — it is the computational engine behind much of number-theoretic cryptography and the gateway to the deeper number theory that follows.
