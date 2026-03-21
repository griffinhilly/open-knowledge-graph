---
id: integral-domains
title: Integral Domains
domain: mathematics
course: abstract-algebra
prerequisites:
- id: first-isomorphism-theorem-rings
  type: hard
builds-toward:
- principal-ideal-domains
- unique-factorization-domains
tags:
- integral-domain
- no-zero-divisors
- cancellation
stage: advanced
status: draft
---

# Integral Domains

## Core Idea
An integral domain is a commutative ring with unity in which there are no zero divisors: ab = 0 implies a = 0 or b = 0. Integral domains are the natural setting for factorization and divisibility.

## Questions

```yaml
- question: "In ℤ/6ℤ, we have 2 × 1 ≡ 2 × 4 (mod 6), yet 1 ≠ 4. This failure of the cancellation law is best explained by:"
  type: multiple-choice
  options:
    - "ℤ/6ℤ lacks a multiplicative identity, so cancellation is undefined"
    - "ℤ/6ℤ is not commutative, and the cancellation law requires commutativity"
    - "ℤ/6ℤ has zero divisors (2 × 3 ≡ 0 mod 6), and the cancellation law fails precisely when zero divisors are present"
    - "Cancellation is only valid for elements with multiplicative inverses, and 2 has no inverse in ℤ/6ℤ"
  answer: 2
  explanation: "The cancellation law and the absence of zero divisors are logically equivalent in a commutative ring with unity. In ℤ/6ℤ, 2 × 3 ≡ 0 with both 2 and 3 nonzero — so 2 is a zero divisor. This is precisely why 2 × 1 ≡ 2 × 4 doesn't imply 1 = 4: subtracting gives 2 × (1 − 4) ≡ 2 × (−3) ≡ 0, but −3 ≢ 0. The zero-divisor relationship is the root cause, and this equivalence is the central theorem of integral domain theory."

- question: "Which of the following is an integral domain?"
  type: multiple-choice
  options:
    - "ℤ/6ℤ (integers mod 6)"
    - "ℤ/4ℤ (integers mod 4)"
    - "ℤ/5ℤ (integers mod 5)"
    - "ℤ/9ℤ (integers mod 9)"
  answer: 2
  explanation: "ℤ/nℤ is an integral domain if and only if n is prime. Since 5 is prime, ℤ/5ℤ has no zero divisors and is actually a field — and every field is an integral domain. In contrast: ℤ/6ℤ has 2 × 3 ≡ 0, ℤ/4ℤ has 2 × 2 ≡ 0, and ℤ/9ℤ has 3 × 3 ≡ 0. Each of these has zero divisors, so none is an integral domain."

- question: "Every integral domain is a field."
  type: true-false
  answer: false
  explanation: "The integers ℤ are the canonical counterexample. ℤ is a commutative ring with unity and has no zero divisors — so it is an integral domain. But ℤ is not a field because most integers lack multiplicative inverses within ℤ (there is no integer n such that 2n = 1). Every field is an integral domain, but not every integral domain is a field. The hierarchy runs: fields ⊂ integral domains ⊂ commutative rings with unity."

- question: "Every field is an integral domain."
  type: true-false
  answer: true
  explanation: "In a field, every nonzero element has a multiplicative inverse. Suppose ab = 0 with a ≠ 0 in a field. Then a has an inverse a⁻¹, and multiplying both sides gives b = 0. This proves fields have no zero divisors, satisfying the definition of an integral domain. Since fields are also commutative rings with unity, they meet all requirements. Fields ⊂ integral domains, not the other way around."

- question: "Why does the absence of zero divisors in an integral domain guarantee that the cancellation law holds?"
  type: short-answer
  answer: "Suppose ac = bc with c ≠ 0. Subtracting gives (a − b)c = 0. Since c ≠ 0 and there are no zero divisors, we must have a − b = 0, so a = b. The cancellation law follows directly from the no-zero-divisors condition. Conversely, if the ring had zero divisors — say dc = 0 with d ≠ 0 and c ≠ 0 — then 0·c = d·c but 0 ≠ d, so cancellation fails. The two conditions are logically equivalent."
  explanation: "The deeper point is that cancellation is what makes divisibility arguments work the way we expect from the integers: if 6 = 2×3 and 6 = 2×k, we can conclude k = 3. In a ring with zero divisors, this reasoning breaks down entirely. The entire theory of GCDs, prime factorization, and irreducibility depends on being able to cancel — which is why these concepts are defined in integral domains, not arbitrary commutative rings."
```

## Explainer

From your work with the first isomorphism theorem for rings, you know that rings are algebraic structures with addition and multiplication satisfying specific axioms — but multiplication need not be commutative, need not have an identity, and products of nonzero elements can equal zero. An integral domain imposes three clarifying conditions: the ring is commutative, it has a multiplicative identity (unity), and it has **no zero divisors**.

A **zero divisor** is a nonzero element a such that ab = 0 for some nonzero b. The integers ℤ have no zero divisors — a fact so familiar it seems obvious. But consider ℤ/6ℤ (integers mod 6): here 2 × 3 = 6 ≡ 0, yet both 2 and 3 are nonzero elements of ℤ/6ℤ. So ℤ/6ℤ is *not* an integral domain. The problem is that 6 is composite; in contrast, ℤ/pℤ for any prime p has no zero divisors and is actually a field.

The no-zero-divisors condition is equivalent to the **cancellation law**: if ac = bc and c ≠ 0, then a = b. Proof: ac = bc means ac − bc = 0, i.e., (a − b)c = 0. Since c ≠ 0 and there are no zero divisors, a − b = 0, so a = b. This cancellation is what makes divisibility arguments work correctly — you can cancel common factors without ambiguity. In ℤ/6ℤ, the cancellation law fails: 2·1 ≡ 2·4 (mod 6), but 1 ≠ 4.

The hierarchy of ring types is worth fixing in your mind: every **field** is an integral domain (nonzero elements have inverses, preventing zero divisors), but not every integral domain is a field (ℤ is the canonical non-field domain). Integral domains sit between general commutative rings and fields, and they are precisely the setting where factorization, divisibility, GCDs, and primality all behave the way you expect from the integers. The concepts of "prime element" and "irreducible element" — which coincide in ℤ but can diverge in other rings — are both defined within integral domains, and studying when they agree leads directly to unique factorization domains.
