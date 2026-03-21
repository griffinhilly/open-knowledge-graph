---
id: divisibility-and-primes-discrete
title: Divisibility, Primes, and Fundamental Theorem of Arithmetic
domain: mathematics
course: discrete-math
prerequisites:
- id: divisibility-and-gcd
  type: hard
- id: prime-and-composite-numbers
  type: hard
builds-toward:
- modular-arithmetic-discrete
tags:
- divisibility
- primes
- factorization
- fundamental-theorem
stage: formal-systems
status: draft
---

# Divisibility, Primes, and Fundamental Theorem of Arithmetic

## Core Idea
An integer a divides b (a | b) if b = ka for some integer k. Prime numbers have exactly two divisors (1 and themselves). The Fundamental Theorem of Arithmetic: every integer > 1 has a unique prime factorization. The proof relies on the Euclidean algorithm and mathematical induction.

## How It's Best Learned
Factor numbers into primes by trial division. Understand gcd via prime factorization: gcd(a, b) is the product of common prime factors to their minimum powers. Use the Euclidean algorithm for large numbers.

## Common Misconceptions
1 is not prime. Uniqueness of factorization requires using primes specifically, not other structures. Division by 0 is undefined; divisibility is defined only for nonzero divisors.

## Questions

```yaml
- question: "A student claims: '1 is prime because it has exactly two divisors: 1 and itself — and 1 = itself, so the two divisors are the same.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing is wrong — 1 is actually prime by this definition"
    - "The definition of prime requires exactly two *distinct* positive divisors. 1 has only one distinct positive divisor (which is 1 itself), so it has exactly one divisor, not two"
    - "1 is prime but only in the integers, not in other number systems"
    - "The student is right about the divisors, but 1 is excluded from primes because it is not an integer greater than 1"
  answer: 1
  explanation: "Primes are defined as integers greater than 1 with exactly two distinct positive divisors: 1 and themselves. For any prime p > 1, these two divisors are different: 1 ≠ p. For the number 1, the only positive divisor is 1 itself — there is only one distinct divisor. So 1 has exactly one positive divisor, not two, and fails the prime definition. The real reason this matters: if 1 were prime, prime factorization would lose uniqueness (12 = 2²×3 = 1×2²×3 = 1²×2²×3, etc.), destroying the Fundamental Theorem of Arithmetic."

- question: "Which part of the Fundamental Theorem of Arithmetic is mathematically non-trivial and requires careful proof?"
  type: multiple-choice
  options:
    - "Existence — proving that every integer greater than 1 has at least one prime factorization"
    - "Uniqueness — proving that the prime factorization is the same regardless of how you factor the number"
    - "Both parts are equally trivial and follow immediately from the definition of prime"
    - "Neither part requires proof — the FTA is an axiom of arithmetic"
  answer: 1
  explanation: "Existence is straightforward: if n > 1 is not prime, it factors as n = ab with 1 < a, b < n. Apply the same reasoning to a and b, and by strong induction (the factors decrease each time), you eventually reach all primes. Uniqueness is the deep part: you must show that no integer can be written as two genuinely different products of primes. The proof requires Euclid's lemma (if p is prime and p | ab, then p | a or p | b), which itself depends on properties of GCD. Uniqueness is also what fails in other algebraic systems like Z[√-5], where 6 = 2×3 = (1+√-5)(1-√-5) — two distinct factorizations into 'irreducibles.'"

- question: "The number 1 is not considered prime because the convention excluding it is arbitrary — mathematicians simply chose not to include it."
  type: true-false
  answer: false
  explanation: "The exclusion of 1 is not arbitrary — it is necessary to preserve the uniqueness part of the Fundamental Theorem of Arithmetic. If 1 were prime, every integer would have infinitely many prime factorizations (just multiply by 1 repeatedly: 12 = 2²×3 = 1×2²×3 = 1²×2²×3 = ...). The FTA's uniqueness statement would collapse. Definitions in mathematics are chosen to make theorems work cleanly; excluding 1 from primes is a principled decision that preserves one of number theory's foundational results."

- question: "The GCD of two integers can be computed from their prime factorizations by taking the minimum power of each common prime factor."
  type: true-false
  answer: true
  explanation: "Yes — this is a direct application of the FTA. For example: 360 = 2³×3²×5 and 504 = 2³×3²×7. The common prime factors are 2 and 3. Taking the minimum exponent for each: min(3,3)=3 for 2 and min(2,2)=2 for 3. So gcd(360, 504) = 2³×3² = 8×9 = 72. The prime 5 appears only in 360, and 7 only in 504, so neither contributes to the GCD. This factorization-based method is conceptually clear, but for large numbers the Euclidean algorithm is far faster since factoring large integers is computationally hard."

- question: "Why does the definition of prime numbers exclude 1, and what would break in arithmetic if 1 were classified as prime?"
  type: short-answer
  answer: "1 is excluded to preserve the uniqueness of prime factorization (the Fundamental Theorem of Arithmetic). If 1 were prime, every integer would have infinitely many factorizations: 12 = 2²×3 = 1×2²×3 = 1⁷×2²×3 = ... The theorem states that factorization is unique 'up to order of factors' — with 1 as a prime, there would be infinitely many ways to factor any integer, making the theorem false. The exclusion is a principled definition choice to make the FTA hold."
  explanation: "This illustrates a general principle in mathematics: definitions are not arbitrary — they are engineered to make theorems clean and powerful. The 'right' definition of prime is the one that makes the FTA and related results work. In more abstract algebra (ring theory), a 'prime' and an 'irreducible' are formally distinguished, and the FTA holds in rings called 'unique factorization domains' (UFDs). The integers Z are the canonical example of a UFD, and excluding 1 from the primes is part of what makes them one."
```

## Explainer

You've already worked with divisibility and GCD, and you know what prime and composite numbers are. This topic formalizes those ideas with precise notation and a powerful theorem. **Divisibility** is written a | b (read "a divides b") and means there exists an integer k such that b = ka. This notation is precise: it's a relationship between integers, not a fraction, and it is defined only when a ≠ 0. Saying 4 | 12 is a true statement (k = 3); saying 4 | 13 is false.

**Prime numbers** are integers greater than 1 whose only positive divisors are 1 and themselves. The number 1 is not prime — this is a definition choice, but a critical one. If 1 were prime, prime factorization would not be unique (12 could be written as 2² × 3 or as 1 × 2² × 3 or 1² × 2² × 3, and so on indefinitely). **Composite numbers** are those with at least one divisor other than 1 and themselves, meaning they factor into smaller positive integers. Every integer greater than 1 is either prime or composite — there is no third option.

The **Fundamental Theorem of Arithmetic** states that every integer greater than 1 can be written as a product of primes in exactly one way, up to the order of the factors. For example, 360 = 2³ × 3² × 5, and no other prime factorization produces 360. The theorem has two parts: existence (every such integer has at least one factorization) and uniqueness (it has exactly one). Uniqueness is the deep and surprising part — it fails in some other algebraic systems, which is why arithmetic in the integers is special.

From your prerequisite on GCD, you can now see it through prime factorizations: gcd(a, b) is the product of primes common to both factorizations, each taken to the minimum power. For example, gcd(360, 504) = gcd(2³·3²·5, 2³·3²·7) = 2³·3² = 72. The **Euclidean algorithm** computes this without factoring at all — useful because factoring large numbers is computationally hard, while the Euclidean algorithm is fast. Together, divisibility, primes, the FTA, GCD, and the Euclidean algorithm form the foundation of number theory and underpin modern cryptographic systems like RSA.
