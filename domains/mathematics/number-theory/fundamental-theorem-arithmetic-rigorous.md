---
id: fundamental-theorem-arithmetic-rigorous
title: Fundamental Theorem of Arithmetic (Rigorous Proof)
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-of-arithmetic
  type: hard
- id: divisibility-theory-formal
  type: hard
builds-toward:
- arithmetic-functions-multiplicativity
tags:
- prime-factorization
- uniqueness
- foundational
stage: advanced
status: draft
---

# Fundamental Theorem of Arithmetic (Rigorous Proof)

## Core Idea
Every integer greater than 1 either is prime or factors uniquely into primes (up to order). The rigorous proof establishes existence via strong induction and uniqueness via Euclid's lemma: if p is prime and p|ab, then p|a or p|b.

## Explainer

You already know informally that every integer factors into primes — you've been doing it since arithmetic. What the rigorous proof adds is something deeper: a guarantee that the factorization is *unique*. It's not obvious that 60 couldn't secretly factor two different ways into primes. The theorem rules this out completely, and the proof splits into two independent parts: existence and uniqueness.

**Existence** is the easier half. Suppose for contradiction that some integer n > 1 cannot be written as a product of primes. Take the smallest such n. It can't be prime (a prime is already a product of one prime), so it must be composite: n = a × b with 1 < a, b < n. Since a and b are smaller than n, by strong induction they both have prime factorizations. Multiplying those factorizations together gives a prime factorization of n — contradiction. Every integer greater than 1 has at least one prime factorization.

**Uniqueness** is harder and hinges entirely on **Euclid's lemma**: if a prime p divides a product ab, then p divides a or p divides b. This is the key fact your prerequisite in divisibility theory established. Without it, uniqueness would be false in other number systems (like Z[√−5], where factorization can fail). Euclid's lemma extends: if p | a₁a₂⋯aₖ, then p divides at least one factor. Now suppose n has two prime factorizations: p₁p₂⋯pₛ = q₁q₂⋯qₜ. Since p₁ divides the left side, it divides the right side, so by Euclid's lemma p₁ | qⱼ for some j. But qⱼ is prime, so p₁ = qⱼ. Cancel both sides and repeat — every prime on the left matches a prime on the right. The two factorizations are identical up to reordering.

The theorem is the bedrock of number theory. It means that primes are the "atoms" of multiplication — every integer has a unique atomic decomposition. This justifies everything that follows: defining arithmetic functions multiplicatively, using prime factorizations to study divisors and GCDs, and reasoning about modular arithmetic. The proof technique — Euclid's lemma + strong induction — is itself a model for dozens of similar uniqueness arguments throughout mathematics.
