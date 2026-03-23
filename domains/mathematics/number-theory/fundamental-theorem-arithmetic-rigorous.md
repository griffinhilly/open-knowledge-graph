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
status: validated
---

# Fundamental Theorem of Arithmetic (Rigorous Proof)

## Core Idea
Every integer greater than 1 either is prime or factors uniquely into primes (up to order). The rigorous proof establishes existence via strong induction and uniqueness via Euclid's lemma: if p is prime and p|ab, then p|a or p|b.

## Questions

```yaml
- question: "The rigorous proof of the Fundamental Theorem of Arithmetic has two independent parts. Which part is genuinely harder and requires Euclid's lemma?"
  type: multiple-choice
  options:
    - "Existence — showing every integer greater than 1 has at least one prime factorization requires Euclid's lemma to prevent circular reasoning"
    - "Uniqueness — showing no integer has two different prime factorizations requires Euclid's lemma to transfer divisibility through a product"
    - "Both parts require Euclid's lemma equally — it is the fundamental tool throughout the proof"
    - "Neither part requires Euclid's lemma; strong induction alone suffices for both"
  answer: 1
  explanation: "Existence is proved by strong induction alone: if n is composite, write n = a × b; since a and b are smaller than n, they have factorizations by induction, and multiplying them gives a factorization of n. No Euclid's lemma needed. Uniqueness is the hard part: suppose p₁p₂⋯pₛ = q₁q₂⋯qₜ; we need to show p₁ equals some qⱼ. Since p₁ divides the product q₁⋯qₜ, Euclid's lemma tells us p₁ must divide some qⱼ — but since qⱼ is prime, p₁ = qⱼ. Without Euclid's lemma, we cannot make this step."

- question: "In the number system Z[√-5] (integers of the form a + b√-5), the number 6 factors both as 2 × 3 and as (1+√-5)(1-√-5), with none of these factors dividing further. What does this demonstrate?"
  type: multiple-choice
  options:
    - "The Fundamental Theorem of Arithmetic is false — 6 has two factorizations in ordinary integers too"
    - "Euclid's lemma fails in Z[√-5], which shows that unique factorization is not automatic — it depends on specific properties of the number system"
    - "This is impossible; the Fundamental Theorem applies to all number systems containing the integers"
    - "Z[√-5] is not a valid number system, so this counterexample does not apply"
  answer: 1
  explanation: "This example shows that unique factorization is not a universal truth about all number-like systems — it is a specific property of the integers that requires proof. In Z[√-5], 2, 3, (1+√-5), and (1-√-5) are all irreducible (nothing divides them except units and themselves), yet 6 has two genuinely different factorizations. The reason unique factorization fails there is that Euclid's lemma fails: 2 divides (1+√-5)(1-√-5) = 6, but 2 divides neither factor. The integers have properties Z[√-5] lacks."

- question: "Euclid's lemma — if a prime p divides a product ab, then p divides a or p divides b — is the key step in proving uniqueness of prime factorization."
  type: true-false
  answer: true
  explanation: "Without Euclid's lemma, uniqueness cannot be proved. The argument works by induction: given two factorizations p₁⋯pₛ = q₁⋯qₜ, we know p₁ divides the right side, so by Euclid's lemma applied repeatedly, p₁ must divide some qⱼ. Since qⱼ is prime and p₁ is prime, p₁ = qⱼ. Cancel both and repeat. The entire uniqueness argument is a chain of applications of Euclid's lemma. As the Z[√-5] counterexample shows, without this lemma, uniqueness fails."

- question: "The existence of a prime factorization for every integer n > 1 is proved by assuming the factorization is unique and then using that uniqueness to show existence."
  type: true-false
  answer: false
  explanation: "Existence and uniqueness are proved independently. Existence uses strong induction: if n is composite, it equals a × b with 1 < a, b < n; by strong induction both a and b have prime factorizations, whose product gives one for n. If n is prime, it is already a product of one prime. No assumption of uniqueness is used anywhere in this argument. The proof structure is: first establish existence (every integer has at least one factorization), then separately prove uniqueness (it has exactly one)."

- question: "Why does Euclid's lemma guarantee that two prime factorizations of the same integer must be identical, and why can't we prove this more directly?"
  type: short-answer
  answer: "Suppose n = p₁p₂⋯pₛ = q₁q₂⋯qₜ. We know p₁ divides the entire product q₁⋯qₜ. By Euclid's lemma, p₁ must divide at least one factor qⱼ. Since qⱼ is prime — divisible only by 1 and itself — and p₁ is also prime, we must have p₁ = qⱼ. Cancel p₁ and qⱼ from both sides and repeat the argument for p₂, and so on. Every prime on the left is matched by an equal prime on the right, so s = t and the factorizations are identical up to order."
  explanation: "The 'more direct' approach fails because divisibility through a product requires Euclid's lemma — there's no shortcut. The lemma is needed to bridge from 'p₁ divides the product' to 'p₁ equals one of the factors.' Without this bridge (as in Z[√-5]), a prime can divide a product without dividing any factor, and uniqueness collapses. Euclid's lemma is not a trivial observation but a theorem that depends on the specific arithmetic of the integers."
```

## Explainer

You already know informally that every integer factors into primes — you've been doing it since arithmetic. What the rigorous proof adds is something deeper: a guarantee that the factorization is *unique*. It's not obvious that 60 couldn't secretly factor two different ways into primes. The theorem rules this out completely, and the proof splits into two independent parts: existence and uniqueness.

**Existence** is the easier half. Suppose for contradiction that some integer n > 1 cannot be written as a product of primes. Take the smallest such n. It can't be prime (a prime is already a product of one prime), so it must be composite: n = a × b with 1 < a, b < n. Since a and b are smaller than n, by strong induction they both have prime factorizations. Multiplying those factorizations together gives a prime factorization of n — contradiction. Every integer greater than 1 has at least one prime factorization.

**Uniqueness** is harder and hinges entirely on **Euclid's lemma**: if a prime p divides a product ab, then p divides a or p divides b. This is the key fact your prerequisite in divisibility theory established. Without it, uniqueness would be false in other number systems (like Z[√−5], where factorization can fail). Euclid's lemma extends: if p | a₁a₂⋯aₖ, then p divides at least one factor. Now suppose n has two prime factorizations: p₁p₂⋯pₛ = q₁q₂⋯qₜ. Since p₁ divides the left side, it divides the right side, so by Euclid's lemma p₁ | qⱼ for some j. But qⱼ is prime, so p₁ = qⱼ. Cancel both sides and repeat — every prime on the left matches a prime on the right. The two factorizations are identical up to reordering.

The theorem is the bedrock of number theory. It means that primes are the "atoms" of multiplication — every integer has a unique atomic decomposition. This justifies everything that follows: defining arithmetic functions multiplicatively, using prime factorizations to study divisors and GCDs, and reasoning about modular arithmetic. The proof technique — Euclid's lemma + strong induction — is itself a model for dozens of similar uniqueness arguments throughout mathematics.
