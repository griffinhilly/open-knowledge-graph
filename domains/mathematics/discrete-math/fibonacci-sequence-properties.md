---
id: fibonacci-sequence-properties
title: Fibonacci Sequence and Properties
domain: mathematics
course: discrete-math
prerequisites:
- id: recurrence-relations
  type: hard
builds-toward:
- fibonacci-identities
tags:
- sequences
- recurrence
- fibonacci
stage: formal-systems
status: validated
---

# Fibonacci Sequence and Properties

## Core Idea
The Fibonacci sequence (F₀=0, F₁=1, Fₙ=Fₙ₋₁+Fₙ₋₂) appears throughout nature and mathematics. It can be solved using the characteristic equation to get Binet's formula. Fibonacci numbers have remarkable divisibility properties and appear in combinatorial counting problems.

## Questions

```yaml
- question: "Binet's formula states F_n = (φⁿ − ψⁿ)/√5 where φ = (1+√5)/2 and ψ = (1−√5)/2 are both irrational. A student claims this formula must be wrong because it produces irrational outputs for integer inputs. What is the correct explanation?"
  type: multiple-choice
  options:
    - "The formula only works for even values of n, where the irrationals happen to cancel"
    - "φ and ψ are actually rational numbers that merely resemble surds in written form"
    - "The irrational parts always cancel exactly when φⁿ and ψⁿ are subtracted and divided by √5, producing an integer"
    - "The formula is an approximation that rounds to the nearest integer rather than giving an exact result"
  answer: 2
  explanation: "Binet's formula is exact, not approximate. The key is that φ and ψ are conjugate surds: when raised to the same power and subtracted, the irrational √5 terms cancel in just the right way to leave an integer. Option D conflates Binet's formula with the useful approximation that F_n ≈ φⁿ/√5 (which works because |ψⁿ/√5| < 0.5 and can be ignored). The exact formula always gives an integer; rounding is not needed."

- question: "According to the divisibility property gcd(F_m, F_n) = F_{gcd(m,n)}, which of the following is true?"
  type: multiple-choice
  options:
    - "F_3 = 2 divides every Fibonacci number because 3 divides every index"
    - "F_5 = 5 divides F_9 because F_5 < F_9"
    - "F_4 = 3 divides F_12 because gcd(4, 12) = 4, so F_4 | F_12"
    - "gcd(F_6, F_9) = F_3 = 2, so F_6 and F_9 share no common factor greater than 2"
  answer: 2
  explanation: "The property states gcd(F_m, F_n) = F_{gcd(m,n)}, and a direct corollary is that F_m divides F_n if and only if m divides n. Since 4 divides 12, F_4 = 3 divides F_12 = 144. Option A is wrong because 3 does not divide every integer index — only every third Fibonacci number is divisible by F_3 = 2. Option B confuses size with divisibility. Option D correctly computes gcd(F_6, F_9) = F_{gcd(6,9)} = F_3 = 2, but then misstates the conclusion — it means they share a common factor of exactly 2."

- question: "Since |ψ| = |(1−√5)/2| < 1, the term ψⁿ/√5 approaches zero as n grows, meaning every Fibonacci number equals the nearest integer to φⁿ/√5."
  type: true-false
  answer: true
  explanation: "Because |ψ| ≈ 0.618 < 1, ψⁿ shrinks exponentially. For all n ≥ 0, |ψⁿ/√5| < 0.5, so F_n = (φⁿ − ψⁿ)/√5 must be the nearest integer to φⁿ/√5. This gives a practical way to compute large Fibonacci numbers: raise φ to the power n, divide by √5, and round."

- question: "The ratio of consecutive Fibonacci numbers F_{n+1}/F_n converges to √5 as n increases."
  type: true-false
  answer: false
  explanation: "The ratio converges to φ = (1+√5)/2 ≈ 1.618, not √5 ≈ 2.236. This follows directly from Binet's formula: F_{n+1}/F_n = (φⁿ⁺¹ − ψⁿ⁺¹)/(φⁿ − ψⁿ) → φ as the ψ terms vanish. The ratio alternates above and below φ, converging from both sides."

- question: "Explain the tiling interpretation of Fibonacci numbers and how it can be used to prove the identity F_1 + F_2 + ··· + F_n = F_{n+2} − 1."
  type: short-answer
  answer: "A 1×n board can be tiled using 1×1 tiles and 1×2 dominoes. For the first square: either a 1×1 tile covers it (leaving n−1 squares, F_n tilings) or a 1×2 domino covers the first two (leaving n−2 squares, F_{n−1} tilings). This gives the Fibonacci recurrence, so the count is F_{n+1} tilings for a board of length n. To prove the sum identity, count tilings of a 1×(n+2) board by where the last tile or domino ends: if it ends at position k, the remaining board has F_k tilings. Summing over all possible endings gives F_1 + F_2 + ··· + F_{n+1} = F_{n+3} − 1, which after reindexing yields the stated identity. The tiling interpretation converts algebraic identities into combinatorial counting arguments."
  explanation: "The key power of the tiling interpretation is that it makes algebraic Fibonacci identities visually obvious by counting the same configurations two different ways — a standard combinatorial proof technique called double counting."
```

## Explainer

From your study of recurrence relations, you know that a recurrence like Fₙ = Fₙ₋₁ + Fₙ₋₂ can be solved by assuming a solution of the form Fₙ = rⁿ and finding what r must be. Substituting into the Fibonacci recurrence gives r² = r + 1, or r² − r − 1 = 0. The two roots are φ = (1 + √5)/2 ≈ 1.618 (the **golden ratio**) and ψ = (1 − √5)/2 ≈ −0.618. The general solution is Fₙ = Aφⁿ + Bψⁿ. Applying the initial conditions F₀ = 0 and F₁ = 1 pins down A and B, yielding **Binet's formula**: Fₙ = (φⁿ − ψⁿ)/√5. This closed form looks surprising — an integer produced by an expression involving √5 — but the irrational parts always cancel exactly.

Binet's formula has a useful corollary: since |ψ| < 1, the term ψⁿ/√5 shrinks toward zero as n grows. This means Fₙ is always the nearest integer to φⁿ/√5. In practice, you can compute large Fibonacci numbers simply by rounding φⁿ/√5. It also reveals the exponential growth rate: consecutive Fibonacci numbers have ratio Fₙ₊₁/Fₙ → φ, converging to the golden ratio from both sides alternately.

The **divisibility properties** of Fibonacci numbers have a remarkable pattern. The greatest common divisor of two Fibonacci numbers satisfies gcd(Fₘ, Fₙ) = F_{gcd(m,n)} — the GCD of Fibonacci-indexed numbers is itself a Fibonacci number, indexed by the GCD of the indices. A consequence: Fₙ divides Fₘ if and only if n divides m. So F₃ = 2 divides every third Fibonacci number, F₄ = 3 divides every fourth, and so on. These divisibility patterns connect the sequence to number theory in unexpected ways.

In combinatorics, Fibonacci numbers count the number of ways to tile a 1×n board using 1×1 and 1×2 tiles: one tile can always cover the first square, or a domino can cover the first two, giving Fₙ₊₁ tilings for a board of length n. This **tiling interpretation** provides an intuitive proof of many Fibonacci identities. For example, the identity F₁ + F₂ + ··· + Fₙ = Fₙ₊₂ − 1 follows by counting tilings of an (n+2)-length board by cases. The Fibonacci sequence is not just a curiosity — it is a bridge between recurrence theory, number theory, and combinatorial reasoning.
