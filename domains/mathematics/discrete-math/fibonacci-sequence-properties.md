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
- generating-functions-applications
tags:
- sequences
- recurrence
- fibonacci
stage: formal-systems
status: draft
---

# Fibonacci Sequence and Properties

## Core Idea
The Fibonacci sequence (F₀=0, F₁=1, Fₙ=Fₙ₋₁+Fₙ₋₂) appears throughout nature and mathematics. It can be solved using the characteristic equation to get Binet's formula. Fibonacci numbers have remarkable divisibility properties and appear in combinatorial counting problems.

## Explainer

From your study of recurrence relations, you know that a recurrence like Fₙ = Fₙ₋₁ + Fₙ₋₂ can be solved by assuming a solution of the form Fₙ = rⁿ and finding what r must be. Substituting into the Fibonacci recurrence gives r² = r + 1, or r² − r − 1 = 0. The two roots are φ = (1 + √5)/2 ≈ 1.618 (the **golden ratio**) and ψ = (1 − √5)/2 ≈ −0.618. The general solution is Fₙ = Aφⁿ + Bψⁿ. Applying the initial conditions F₀ = 0 and F₁ = 1 pins down A and B, yielding **Binet's formula**: Fₙ = (φⁿ − ψⁿ)/√5. This closed form looks surprising — an integer produced by an expression involving √5 — but the irrational parts always cancel exactly.

Binet's formula has a useful corollary: since |ψ| < 1, the term ψⁿ/√5 shrinks toward zero as n grows. This means Fₙ is always the nearest integer to φⁿ/√5. In practice, you can compute large Fibonacci numbers simply by rounding φⁿ/√5. It also reveals the exponential growth rate: consecutive Fibonacci numbers have ratio Fₙ₊₁/Fₙ → φ, converging to the golden ratio from both sides alternately.

The **divisibility properties** of Fibonacci numbers have a remarkable pattern. The greatest common divisor of two Fibonacci numbers satisfies gcd(Fₘ, Fₙ) = F_{gcd(m,n)} — the GCD of Fibonacci-indexed numbers is itself a Fibonacci number, indexed by the GCD of the indices. A consequence: Fₙ divides Fₘ if and only if n divides m. So F₃ = 2 divides every third Fibonacci number, F₄ = 3 divides every fourth, and so on. These divisibility patterns connect the sequence to number theory in unexpected ways.

In combinatorics, Fibonacci numbers count the number of ways to tile a 1×n board using 1×1 and 1×2 tiles: one tile can always cover the first square, or a domino can cover the first two, giving Fₙ₊₁ tilings for a board of length n. This **tiling interpretation** provides an intuitive proof of many Fibonacci identities. For example, the identity F₁ + F₂ + ··· + Fₙ = Fₙ₊₂ − 1 follows by counting tilings of an (n+2)-length board by cases. The Fibonacci sequence is not just a curiosity — it is a bridge between recurrence theory, number theory, and combinatorial reasoning.
