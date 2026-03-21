---
id: fundamental-theorem-of-arithmetic-rigorous
title: Fundamental Theorem of Arithmetic (Rigorous)
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-of-arithmetic
  type: hard
- id: euclidean-algorithm
  type: soft
builds-toward:
- arithmetic-functions-and-multiplicativity
- failure-of-unique-factorization
tags:
- unique-factorization
- prime-factorization
- integers
stage: advanced
status: draft
---

# Fundamental Theorem of Arithmetic (Rigorous)

## Core Idea
Every integer greater than 1 either is prime or is uniquely expressible as a product of primes, up to order. This rigorous treatment proves both existence (by strong induction) and uniqueness (via Euclid's lemma) and explores why it holds in ℤ but fails in other number systems.

## How It's Best Learned
Prove existence and uniqueness separately using strong induction and Euclid's lemma. Compare with domains where unique factorization fails, such as ℤ[√5] where 6 = 2·3 = (1+√5)(1−√5).

## Common Misconceptions
Unique factorization is not universal across all algebraic structures; it requires special conditions. The unit 1 is not prime and must be handled separately in the uniqueness statement.

## Questions

```yaml
- question: "A student claims that unique prime factorization is 'obvious' because it's just a fact about integers — no real proof is needed. What important insight does the rigorous proof provide that this intuition misses?"
  type: multiple-choice
  options:
    - "The proof shows that 1 is actually a prime number, which is non-obvious"
    - "The proof reveals that unique factorization is not universal — it requires special conditions that hold in ℤ but fail in other number systems like ℤ[√−5], where 6 = 2·3 = (1+√−5)(1−√−5) are two genuinely different factorizations into irreducibles"
    - "The proof provides a faster algorithm for finding prime factors"
    - "The proof shows that strong induction, not weak induction, is the correct tool for all arithmetic facts"
  answer: 1
  explanation: "Unique factorization feels obvious in ℤ because we grew up with it, but the rigorous proof reveals *why* it holds — and that it can fail. In ℤ[√−5], the element 6 has two genuinely different factorizations into irreducibles: 2·3 and (1+√−5)(1−√−5). Each factor is irreducible (cannot be broken down further in that ring), yet neither factorization can be obtained from the other by reordering. This is impossible in ℤ because of Euclid's Lemma — which depends on the Euclidean algorithm. The proof doesn't just confirm the obvious; it identifies exactly which property of ℤ makes uniqueness work and shows it is not automatic."

- question: "Euclid's Lemma states that if a prime p divides ab, then p | a or p | b. Why is this lemma the crucial step in proving that prime factorization is unique?"
  type: multiple-choice
  options:
    - "It proves that every integer greater than 1 has at least one prime factor, establishing existence"
    - "It guarantees that if two factorizations p₁p₂···pₖ = q₁q₂···qₘ exist, then each pᵢ must equal some qⱼ — the lemma forces the two lists to match up element by element, so they cannot truly differ"
    - "It provides the efficient algorithm for computing prime factorizations"
    - "It shows that 1 is not prime, eliminating trivial counterexamples to uniqueness"
  answer: 1
  explanation: "Here is how uniqueness works: suppose p₁p₂···pₖ = q₁q₂···qₘ. Since p₁ divides the right side (a product), Euclid's Lemma says p₁ must divide some qⱼ. Since qⱼ is prime, the only divisors are 1 and itself — so p₁ = qⱼ. Cancel both sides. Repeat. The two factorizations collapse to the same list. Without Euclid's Lemma, this argument doesn't work — in ℤ[√−5], 2 divides (1+√−5)(1−√−5) = 6, but 2 divides neither factor, so the lemma fails and uniqueness breaks down."

- question: "In the ring ℤ[√−5], the number 6 can be factored as both 2·3 and (1+√−5)(1−√−5), and these are genuinely different factorizations into irreducible elements — demonstrating that unique factorization does not hold universally."
  type: true-false
  answer: true
  explanation: "This is precisely the counterexample that shows unique factorization is a non-trivial property. One can verify that 2, 3, 1+√−5, and 1−√−5 are all irreducible in ℤ[√−5] (cannot be factored further within the ring), and that neither factorization can be obtained from the other by reordering or multiplying by units. The reason this is possible is that in ℤ[√−5], irreducible does not imply prime — Euclid's Lemma fails for these elements. This example motivates the definition of a Unique Factorization Domain (UFD) and shows ℤ[√−5] is not one."

- question: "The number 1 is considered a prime number in the rigorous statement of the Fundamental Theorem of Arithmetic, since it can trivially be factored as a product of zero primes."
  type: true-false
  answer: false
  explanation: "1 is explicitly excluded from the primes and must be handled separately. The standard definition requires a prime to be greater than 1 with no positive divisors other than 1 and itself. Including 1 as a prime would destroy uniqueness: 6 = 2·3 = 1·2·3 = 1·1·2·3 = ··· would give infinitely many factorizations. The theorem is stated as: every integer greater than 1 is either prime or a unique product of primes. The exclusion of 1 is not a technicality but is essential for the uniqueness claim to hold."

- question: "Why does proving uniqueness of prime factorization require Euclid's Lemma (if p | ab then p | a or p | b), rather than following immediately from the definition of prime numbers?"
  type: short-answer
  answer: "The definition of a prime says it has no divisors other than 1 and itself — this tells us about divisors of the prime, not about what the prime divides. To prove uniqueness, we need to know: if p appears in one factorization of n, must it appear in every factorization? This requires showing that p | (product) implies p | (some factor), which is exactly Euclid's Lemma. The lemma is non-trivial and depends on the Euclidean algorithm (via Bézout's identity: if gcd(p,a) = 1 then there exist integers x,y with px + ay = 1, so if p | ab, multiply through by b to get p | b). In rings where the Euclidean algorithm fails, so does this argument, and so does uniqueness."
  explanation: "The distinction between 'irreducible' (cannot be factored) and 'prime' (satisfies Euclid's Lemma) is the heart of the matter. In ℤ, every irreducible is prime — this is provable precisely because the Euclidean algorithm works in ℤ. In other rings, the two notions come apart. The rigorous proof of the FTA is really a proof that in ℤ, irreducible implies prime — and that proof goes through the Euclidean algorithm. Understanding this is what allows you to recognize when and why the theorem fails in other settings."
```

## Explainer

You already know from the introductory treatment that every integer greater than 1 can be broken into prime factors, and that 60 = 2² · 3 · 5 regardless of how you start factoring it. The rigorous version asks: *why* is this true? The proof has two completely separate jobs — proving a prime factorization **exists** and proving it is **unique** — and each requires a distinct technique.

**Existence** is proved by **strong induction**. The base case is 2, which is already prime. For the inductive step, assume every integer from 2 to n−1 is either prime or has a prime factorization. Now consider n: if n is prime, we are done. If n is composite, then n = a · b with 2 ≤ a, b < n. By the inductive hypothesis, both a and b have prime factorizations. Multiplying those factorizations together gives a prime factorization of n. Notice that strong induction — where you assume the result holds for *all* smaller values, not just the immediate predecessor — is what makes this work. The Euclidean algorithm from your prerequisites isn't needed for existence, but it is the key to uniqueness.

**Uniqueness** rests on **Euclid's Lemma**: if a prime p divides a product ab, then p | a or p | b (or both). This lemma is provable using the Euclidean algorithm through Bézout's identity. Here is where it matters: if two different prime factorizations of n existed, say p₁p₂···pₖ = q₁q₂···qₘ, then p₁ divides the right side. By repeated application of Euclid's Lemma, p₁ must equal some qⱼ. Cancel both and repeat — the two factorizations must be identical up to order.

The theorem's limitations are equally important to understand. Consider the ring ℤ[√−5], which consists of numbers of the form a + b√−5. In this ring, 6 = 2 · 3 = (1 + √−5)(1 − √−5), and one can verify that 2, 3, 1+√−5, and 1−√−5 are all **irreducible** (cannot be factored further in the ring) yet 2 does not divide either factor on the right — Euclid's Lemma fails. The reason is that irreducible does not imply prime in this ring. The Fundamental Theorem holds in ℤ precisely because every irreducible integer *is* prime, which is itself a consequence of the Euclidean algorithm. Rings where unique factorization holds are called **unique factorization domains (UFDs)**; the existence of ℤ[√−5] shows that not every ring deserves this title.
