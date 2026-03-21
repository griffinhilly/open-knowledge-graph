---
id: fundamental-theorem-of-arithmetic
title: The Fundamental Theorem of Arithmetic
domain: mathematics
course: discrete-math
prerequisites:
- id: divisibility-and-gcd
  type: hard
- id: mathematical-induction
  type: hard
- id: proof-by-contradiction
  type: soft
tags:
- fundamental-theorem-arithmetic
- prime-factorization
- unique-factorization
- euclids-lemma
stage: formal-systems
status: validated
---

# The Fundamental Theorem of Arithmetic

## Core Idea
The Fundamental Theorem of Arithmetic states that every integer greater than 1 can be expressed as a product of prime numbers in exactly one way, up to the order of factors. Existence of the factorization is proved by strong induction. Uniqueness requires Euclid's lemma: if a prime p divides ab, then p divides a or p divides b. The theorem underpins the entire structure of elementary number theory — GCD, LCM, and divisibility results all depend on factorizations being unique.

## How It's Best Learned
Prove existence by strong induction, then prove Euclid's lemma separately using Bezout's identity, and finally assemble the uniqueness proof by contradiction. Contrast with systems where unique factorization fails (e.g., Z[√−5], where 6 = 2×3 = (1+√−5)(1−√−5)) to appreciate why the theorem is non-trivial.

## Common Misconceptions
- Treating unique factorization as self-evident — the proof is non-trivial and the property fails in other algebraic systems.
- Incorrectly classifying 1 as prime; 1 is excluded by convention and has the vacuous empty product as its factorization.

## Questions

```yaml
- question: "Which part of proving the Fundamental Theorem of Arithmetic specifically requires Euclid's lemma (if p divides ab, then p divides a or p divides b)?"
  type: multiple-choice
  options:
    - "Proving that every integer greater than 1 has at least one prime factorization (existence)"
    - "Proving that the prime factorization is unique — that no integer has two genuinely different factorizations"
    - "Proving that 1 is not prime"
    - "Proving that there are infinitely many primes"
  answer: 1
  explanation: "Existence is proved by strong induction alone: if n is prime, done; if composite, it has a factor 1 < d < n, and by strong induction both d and n/d have prime factorizations. Uniqueness is the hard part: to show two factorizations must be identical, you need Euclid's lemma — if a prime p appears in one factorization, it divides the product on the other side, and the lemma forces p to equal one of those primes. Without Euclid's lemma, you cannot rule out genuinely different factorizations."

- question: "In the ring Z[√−5], the number 6 factors as both 2 × 3 and (1+√−5)(1−√−5), where all four factors are irreducible. What does this tell us about the Fundamental Theorem of Arithmetic?"
  type: multiple-choice
  options:
    - "The theorem is false — 6 itself is a counterexample to unique factorization in the ordinary integers"
    - "The theorem relies on specific properties of the ordinary integers that do not hold in all number systems"
    - "The theorem is trivially true because factorizations involving complex numbers don't count"
    - "This shows that primes and irreducible elements are always the same thing in any ring"
  answer: 1
  explanation: "This example shows that unique factorization is not a universal truth about all number systems — it depends on the specific structure of the integers, particularly the property that enables Euclid's lemma (which follows from the Euclidean algorithm). In Z[√−5], Euclid's lemma fails, and so does unique factorization. This is why FTA requires a real proof rather than just an appeal to intuition — the intuition that 'of course factorization is unique' is wrong in closely related systems."

- question: "The uniqueness of prime factorization in the integers follows from Euclid's lemma: if a prime p divides ab, then p divides a or p divides b."
  type: true-false
  answer: true
  explanation: "Euclid's lemma is the key to the uniqueness proof. Suppose two prime factorizations of n exist. Take any prime p from the first — it divides n, and therefore divides the product in the second factorization. By repeated application of Euclid's lemma, p must divide one of the primes in the second factorization — and since those are prime, p must equal that prime. Continuing this argument shows the two factorizations must contain the same primes with the same multiplicities."

- question: "The Fundamental Theorem of Arithmetic is intuitively obvious and doesn't require a non-trivial proof, since it's clear that any number factors into primes in only one way."
  type: true-false
  answer: false
  explanation: "Unique factorization is not intuitively obvious — it is false in other algebraic systems that closely resemble the integers. The ring Z[√−5] provides a concrete counterexample where factorization is not unique. The proof requires Euclid's lemma, which in turn requires Bézout's identity from the Euclidean algorithm. These are non-trivial results that depend on specific properties of the integers. Treating FTA as obvious is the most common misconception about the theorem."

- question: "Why is Euclid's lemma the critical tool for proving uniqueness in the Fundamental Theorem of Arithmetic, and what would go wrong in the proof without it?"
  type: short-answer
  answer: "Euclid's lemma states: if a prime p divides a product ab, then p divides a or p divides b. Without it, we cannot connect a prime in one factorization to any prime in a second factorization. The uniqueness proof works by assuming two factorizations exist and showing they must be the same: pick a prime from the first, note it divides the product on the second side, and use Euclid's lemma to force it to equal one of the primes there. Without this lemma, a prime from one factorization might divide the product without dividing any individual factor — and we'd have no way to rule out different factorizations."
  explanation: "The example of Z[√−5] is instructive: in that ring, Euclid's lemma fails, and indeed 6 has two distinct factorizations. The theorem's truth in the ordinary integers is a consequence of the Euclidean algorithm giving us the Bézout identity, which implies Euclid's lemma. The chain of dependence: Euclidean algorithm → Bézout identity → Euclid's lemma → FTA uniqueness."
```

## Explainer

From your work on **divisibility and GCD**, you know that primes are the integers with no divisors except 1 and themselves, and that GCD can be computed using the Euclidean algorithm. The Fundamental Theorem of Arithmetic makes a deeper claim: these primes are the unique "atoms" of multiplication. Every integer greater than 1 breaks into primes in exactly one way (ignoring order). This feels obvious — try to factor 12 any way you like, you always get 2 × 2 × 3. But the theorem is not trivial, and its proof has two distinct parts that require different techniques.

**Existence** of a prime factorization is proved by strong induction, which you've already mastered. The argument is: if n is prime, it's its own factorization. If n is composite, it has a divisor d with 1 < d < n, so both d and n/d are smaller than n. By strong induction, each has a prime factorization, and multiplying them gives a prime factorization of n. Clean and complete.

**Uniqueness** is harder and is where **Euclid's lemma** enters: if a prime p divides a product ab, then p divides a or p divides b (or both). This follows from Bézout's identity — if p doesn't divide a, then gcd(p, a) = 1 (since p is prime), so there exist integers x, y with px + ay = 1, multiply both sides by b to get p(xb) + (ab)y = b, and since p divides ab, p divides the left side, so p divides b. With Euclid's lemma in hand, you can prove uniqueness by contradiction: assume two different prime factorizations exist, use the lemma to show each prime on one side must appear on the other, producing a contradiction.

To appreciate why uniqueness is non-trivial, consider the ring Z[√−5] — integers of the form a + b√−5. In this system, 6 = 2 × 3 = (1 + √−5)(1 − √−5), and all four factors are "irreducible" (can't be factored further) yet the two factorizations are genuinely different. Unique factorization fails because Euclid's lemma fails. In the ordinary integers, the proof works because of the specific structure of the Euclidean algorithm — a reminder that theorems depend on the axioms of their system, not just intuition.
