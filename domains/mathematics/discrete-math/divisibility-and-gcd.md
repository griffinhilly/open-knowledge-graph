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

## Questions

```yaml
- question: "Two integers a and b satisfy gcd(a, b) = 6. According to Bézout's identity, which of the following is guaranteed to exist?"
  type: multiple-choice
  options:
    - "Positive integers x and y such that ax + by = 6"
    - "Integers x and y (which may be negative or zero) such that ax + by = 6"
    - "A prime number p such that p divides both a and b"
    - "Integers x and y such that ax + by = 1"
  answer: 1
  explanation: "Bézout's identity guarantees integers x and y (not necessarily positive) such that ax + by = gcd(a, b). Since gcd(a, b) = 6, we get ax + by = 6 for some integers x, y that may be negative. Option A is wrong because Bézout coefficients can be negative — this is a common misconception. Option C is wrong because gcd(a, b) = 6 means the greatest common divisor is 6, which is not prime; the pair might not share any prime factor with multiplicity that makes a prime divide both. Option D would require gcd(a, b) = 1, but gcd = 6 here."

- question: "What is the correct interpretation of 'a and b are coprime'?"
  type: multiple-choice
  options:
    - "Both a and b are prime numbers"
    - "Neither a nor b has any prime factors"
    - "gcd(a, b) = 1 — the only positive integer dividing both is 1"
    - "a divides b or b divides a"
  answer: 2
  explanation: "Coprime (also called relatively prime) means the two integers share no common factors other than 1, i.e., gcd(a, b) = 1. This does not require either number to be prime itself — for example, 8 and 9 are coprime (gcd = 1) even though neither is prime. Coprimality is crucial because Bézout's identity, applied when gcd = 1, guarantees an integer x such that ax ≡ 1 (mod b) — i.e., a has a multiplicative inverse modulo b. This is the foundation of modular arithmetic and public-key cryptography."

- question: "The Bézout coefficients x and y in the equation ax + by = gcd(a, b) are always positive integers."
  type: true-false
  answer: false
  explanation: "Bézout coefficients are integers that may be positive, negative, or zero — this surprises many students who expect coefficients in a sum to be positive. For example, gcd(12, 18) = 6, and the Bézout representation is 12·(−1) + 18·1 = 6, where x = −1. In general, if (x₀, y₀) is one solution, then infinitely many solutions exist by adjusting with multiples of b/gcd and a/gcd, and both positive and negative coefficients are possible. Finding the specific coefficients requires the extended Euclidean algorithm."

- question: "If gcd(a, m) = 1, then there exists an integer x such that ax ≡ 1 (mod m) — meaning a has a multiplicative inverse modulo m."
  type: true-false
  answer: true
  explanation: "This follows directly from Bézout's identity: if gcd(a, m) = 1, then there exist integers x, y such that ax + my = 1. Reducing this equation modulo m gives ax ≡ 1 (mod m), so x is the multiplicative inverse of a modulo m. This is the key result that makes modular arithmetic work for cryptographic applications — in RSA encryption, for instance, the decryption key is computed as a modular inverse. The requirement that gcd(a, m) = 1 is essential: if gcd(a, m) > 1, no such inverse exists."

- question: "Explain why Bézout's identity is described as elevating the GCD from 'an arithmetic curiosity to an algebraic tool.'"
  type: short-answer
  answer: "Before Bézout's identity, the GCD is just a number — the largest common divisor of a and b. Bézout's identity reveals that this number can be expressed as a linear combination ax + by of the original integers, making it accessible through algebraic operations. This unlocks a chain of applications: it proves that if gcd(a, m) = 1, then a has a multiplicative inverse mod m (essential for modular arithmetic), and it provides the constructive method (extended Euclidean algorithm) for finding that inverse. The GCD stops being a static property and becomes a lever for solving equations and building cryptographic systems."
  explanation: "The phrase 'algebraic tool' points to the shift from description to manipulation. Knowing that gcd(12, 18) = 6 describes a relationship; knowing that 12·(−1) + 18·1 = 6 gives you something to work with algebraically. The extended form makes the GCD actionable in proofs and algorithms in a way that the simple definition does not."
```

## Explainer

From your study of prime and composite numbers, you know that every integer greater than 1 factors uniquely into primes. Divisibility formalizes a related relationship: **a divides b** (written a | b) means b is an exact multiple of a — there exists a whole number k such that b = ak, with no remainder. Saying 6 | 42 is saying 42 = 6 × 7. If the division leaves a remainder, divisibility fails: 6 does not divide 43. This simple "exact fit" idea is the foundation of everything in number theory.

The **greatest common divisor** gcd(a,b) is the largest integer that divides both a and b. One approach is via prime factorizations: find all primes the two numbers share and take the lowest power of each. For 12 = 2²·3 and 18 = 2·3², the shared primes are 2 and 3, giving gcd(12,18) = 2¹·3¹ = 6. This method builds directly on your prime-factorization knowledge, but it is slow for large numbers — which is why the Euclidean algorithm (your next topic) matters. The **least common multiple** is the flip side: take the *maximum* power of every prime appearing in either number. The connecting formula lcm(a,b) = |ab| / gcd(a,b) ties the two together cleanly. A practical image: two gears with 12 and 18 teeth realign every lcm(12,18) = 36 tooth-advances.

**Bézout's identity** elevates GCD from an arithmetic curiosity to an algebraic tool. For any integers a and b, there exist integers x and y (which may be zero or negative) such that ax + by = gcd(a,b). For 12 and 18: 12·(−1) + 18·(1) = 6. This means the GCD is not just the largest common divisor — it is also the *smallest positive integer expressible as a linear combination of a and b*. The coefficients x and y are called **Bézout coefficients** and may be negative, which surprises students who expect them to be positive. Finding these coefficients explicitly uses the extended Euclidean algorithm.

The applications reach far beyond elementary arithmetic. GCD determines when two periodic processes sync up. It tells you when a fraction is fully reduced (a/b is in lowest terms when gcd(a,b) = 1, meaning a and b are **coprime**). Bézout's identity is the key lemma behind modular arithmetic: if gcd(a,m) = 1, then a has a multiplicative inverse modulo m, which is what makes public-key cryptography possible. Every result in that direction traces back to the simple question of when one integer divides another exactly.
