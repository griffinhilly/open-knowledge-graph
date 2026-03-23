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
status: validated
---

# The Euclidean Algorithm and Greatest Common Divisor

## Core Idea
The Euclidean algorithm efficiently computes gcd(a,b) using repeated division: gcd(a,b) = gcd(b, a mod b), stopping when the remainder is 0. Time complexity is O(log(min(a,b))). The extended Euclidean algorithm finds integers x, y such that ax + by = gcd(a,b).

## Questions

```yaml
- question: "Why does gcd(a, b) = gcd(b, a mod b)? What justifies this reduction step?"
  type: multiple-choice
  options:
    - "Because dividing a by b produces the same quotient as dividing a mod b by b"
    - "Because every common divisor of a and b also divides a mod b, and vice versa — so the set of common divisors is identical"
    - "Because the Euclidean algorithm defines gcd this way, without deeper mathematical justification"
    - "Because a mod b is always smaller than b, which guarantees the algorithm terminates"
  answer: 1
  explanation: "The key insight is that if d divides both a and b, then d divides a − qb = a mod b (since a mod b is a linear combination of a and b). Conversely, if d divides both b and a mod b, it divides a = qb + (a mod b). So the set of common divisors is identical for (a, b) and (b, a mod b), meaning their GCD must be the same. Option D is true but explains only termination, not correctness — the two are distinct questions."

- question: "If gcd(a, n) = 3, does a have a multiplicative inverse modulo n?"
  type: multiple-choice
  options:
    - "Yes — any nonzero number has a multiplicative inverse modulo any n"
    - "No — a multiplicative inverse of a modulo n exists only when gcd(a, n) = 1"
    - "Yes — because 3 divides both a and n, they share structure that enables an inverse"
    - "No — but only because n must be composite in this case"
  answer: 1
  explanation: "A multiplicative inverse of a modulo n exists if and only if gcd(a, n) = 1. Bézout's identity gives ax + ny = gcd(a, n). For a modular inverse we need ax ≡ 1 (mod n), which requires gcd(a, n) = 1. If gcd(a, n) = 3, then ax + ny is always a multiple of 3 and can never equal 1 — no inverse exists. This is why RSA and other cryptographic systems require choosing values coprime to the modulus."

- question: "The extended Euclidean algorithm computes not just gcd(a, b) but also integers x and y such that ax + by = gcd(a, b). Its primary practical application is computing multiplicative inverses modulo n."
  type: true-false
  answer: true
  explanation: "Bézout's identity guarantees that ax + by = gcd(a, b). When gcd(a, n) = 1, this gives ax + ny = 1, so ax ≡ 1 (mod n) — meaning x is the multiplicative inverse of a modulo n. The extended Euclidean algorithm computes this inverse in O(log n) time. This is the core subroutine inside the Chinese Remainder Theorem and RSA, making the extended algorithm indispensable in number-theoretic cryptography."

- question: "A naive algorithm for gcd(a, b) lists all divisors of both numbers and finds the largest shared one. The Euclidean algorithm is faster primarily because it checks fewer divisor pairs."
  type: true-false
  answer: false
  explanation: "The Euclidean algorithm is faster because it achieves O(log(min(a, b))) time through repeated reduction — not by searching fewer divisors. Each step replaces the pair (a, b) with (b, a mod b), strictly shrinking the problem. In the worst case (consecutive Fibonacci numbers), the size roughly halves every two steps. For numbers with hundreds of digits, this is the difference between instant computation and impossibly slow enumeration. The algorithm avoids factoring entirely."

- question: "Using the Euclidean algorithm, compute gcd(91, 35). Show your steps."
  type: short-answer
  answer: "gcd(91, 35): 91 = 2·35 + 21, so gcd(91, 35) = gcd(35, 21). 35 = 1·21 + 14, so gcd(35, 21) = gcd(21, 14). 21 = 1·14 + 7, so gcd(21, 14) = gcd(14, 7). 14 = 2·7 + 0, so gcd(14, 7) = gcd(7, 0) = 7. Answer: gcd(91, 35) = 7."
  explanation: "Each step applies gcd(a, b) → gcd(b, a mod b) until the remainder is zero. The last nonzero remainder is the GCD. Four steps suffice here because the numbers are small; for numbers with hundreds of digits the same structure applies, still completing in logarithmic time."
```

## Explainer

The **greatest common divisor** gcd(a, b) is the largest integer that divides both a and b. A naive approach — list all divisors of both numbers and find the largest shared one — is painfully slow for large numbers. The Euclidean algorithm exploits a key insight from your prerequisite modular arithmetic: gcd(a, b) = gcd(b, a mod b). This follows because any common divisor of a and b also divides a − qb = a mod b, and vice versa — the set of common divisors is unchanged when you replace a with its remainder mod b.

The algorithm repeatedly applies this reduction: gcd(252, 105) → gcd(105, 42) → gcd(42, 21) → gcd(21, 0) = 21. Each step shrinks the problem: the new pair (b, a mod b) is strictly smaller than (a, b). In the worst case the size halves every two steps, so the total number of steps is O(log(min(a, b))). This logarithmic time complexity makes the algorithm practical for numbers with hundreds of digits — a massive improvement over naive factoring.

The **extended Euclidean algorithm** goes further: it finds integers x and y such that ax + by = gcd(a, b). This is **Bézout's identity**. The algorithm works by tracing the computation backwards. For the example above: 21 = 105 − 2(42) = 105 − 2(252 − 2·105) = 5·105 − 2·252, giving x = −2, y = 5. The back-substitution systematically expresses each remainder as a linear combination of the original inputs, and the last nonzero remainder (the GCD) ends up as that combination.

Bézout coefficients are the key to **modular inverses**: if gcd(a, n) = 1, then ax ≡ 1 (mod n), meaning x is the multiplicative inverse of a modulo n. The extended Euclidean algorithm computes this inverse directly, in O(log n) time. This is why it appears as a core subroutine inside the Chinese Remainder Theorem and RSA cryptography. Understanding the Euclidean algorithm is therefore not just about GCD — it is the computational engine behind much of number-theoretic cryptography and the gateway to the deeper number theory that follows.
