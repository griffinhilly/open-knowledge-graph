---
id: maximal-prime-ideals
title: Maximal and Prime Ideals
domain: mathematics
course: abstract-algebra
prerequisites:
- id: subrings-ideals
  type: hard
builds-toward:
- field-definition-examples
tags:
- maximal-ideal
- prime-ideal
- quotient-structure
stage: advanced
status: draft
---

# Maximal and Prime Ideals

## Core Idea
A maximal ideal M of a ring R is an ideal properly contained in R such that no ideal properly contains M. An ideal P is prime if ab ∈ P implies a ∈ P or b ∈ P. In a commutative ring with unity, R/M is a field iff M is maximal, and R/P is an integral domain iff P is prime.

## Questions

```yaml
- question: "Consider the ideal (6) in ℤ. Is it prime? Is it maximal?"
  type: multiple-choice
  options:
    - "Prime and maximal, because 6 is an integer and all nonzero ideals in ℤ are prime and maximal"
    - "Prime but not maximal, because ℤ/(6) has no zero divisors but is not a field"
    - "Neither prime nor maximal, because 2·3 = 6 ∈ (6) while 2 ∉ (6) and 3 ∉ (6), and (6) ⊊ (2) ⊊ ℤ"
    - "Maximal but not prime, because (6) cannot be extended to a larger proper ideal"
  answer: 2
  explanation: "For (6) to be prime, whenever ab ∈ (6) we would need a ∈ (6) or b ∈ (6). But 2·3 = 6 ∈ (6), yet neither 2 nor 3 is divisible by 6 — so (6) is not prime. For (6) to be maximal, there would need to be no proper ideal strictly between (6) and ℤ. But (6) ⊊ (2) ⊊ ℤ is a chain of proper inclusions, so (6) is not maximal either. In ℤ, an ideal (n) is prime iff n is prime, and maximal iff n is prime — both require n to be a prime number."

- question: "A student argues: 'Since every field is an integral domain, and R/P is an integral domain when P is prime, it follows that R/P is always a field.' What is wrong?"
  type: multiple-choice
  options:
    - "Nothing is wrong — prime ideals always give field quotients"
    - "The argument confuses sufficient and necessary conditions: R/P being an integral domain requires P prime; R/P being a field requires the stronger condition that P is maximal"
    - "R/P is never an integral domain unless R is itself an integral domain"
    - "The argument is correct for commutative rings but fails for noncommutative rings"
  answer: 1
  explanation: "Every field is an integral domain, but not every integral domain is a field. The correspondence mirrors this: maximal ↔ field (stronger), prime ↔ integral domain (weaker). In ℤ, the ideal (2) is both prime and maximal — ℤ/(2) ≅ F₂ is a field. But (0) is prime (ℤ/(0) ≅ ℤ is an integral domain) yet not maximal. The student's argument illegitimately reverses the implication 'field ⟹ integral domain' into 'integral domain ⟹ field.'"

- question: "In any commutative ring with unity, every maximal ideal is also a prime ideal."
  type: true-false
  answer: true
  explanation: "If M is maximal, then R/M is a field. Every field is an integral domain (it has no zero divisors). Since R/M is an integral domain, M is prime. The chain is: M maximal ⟹ R/M is a field ⟹ R/M is an integral domain ⟹ M is prime. The reverse implication fails: prime does not imply maximal."

- question: "In a commutative ring with unity, every prime ideal is also maximal."
  type: true-false
  answer: false
  explanation: "In ℤ, the ideal (0) is prime because ℤ has no zero divisors (if ab = 0 in ℤ, then a = 0 or b = 0). But (0) is not maximal because (0) ⊊ (2) ⊊ ℤ — the ideal (2) sits strictly between (0) and all of ℤ. However, in a principal ideal domain, every nonzero prime ideal is maximal. The claim holds in special settings but fails in general."

- question: "Why does the correspondence 'R/M is a field ⟺ M is maximal' hold, and what does it reveal about the relationship between algebraic structure and ideal size?"
  type: short-answer
  answer: "A field has no proper nonzero ideals. Under the correspondence between ideals of R/I and ideals of R containing I, the ideals of R/M correspond exactly to ideals J with M ⊆ J ⊆ R. If M is maximal, no such J exists strictly between M and R, so R/M has no nontrivial ideals — it is a field. Conversely, if R/M is a field, it has no nontrivial ideals, so no ideal of R sits strictly between M and R, making M maximal. The 'size' of the ideal (how close it is to all of R) directly controls the 'simplicity' of the quotient ring."
  explanation: "This is a deep structural insight: collapsing a maximal portion of a ring produces a maximally simple structure (a field). The hierarchy maximal → prime → general ideal mirrors the hierarchy field → integral domain → general ring, and studying which quotients have which properties is the essential technique of commutative algebra."
```

## Explainer

You know about ideals from your prerequisite: an ideal I of a ring R is a subset closed under addition and under multiplication by any element of R. Ideals are the "normal subgroups" of rings — the right building blocks for forming quotient rings R/I, where elements are cosets a + I and arithmetic is done modulo I. The question this topic asks is: what algebraic structure does R/I inherit from R, and what does that structure tell you about I itself?

The answer comes in two levels. An ideal P is called **prime** if whenever a product ab lands in P, at least one of a or b must already be in P. This is a direct generalization of the prime number property: in ℤ, the ideal (p) is prime exactly when p is a prime number — if p divides ab, then p divides a or p divides b. The algebraic payoff is that P is prime if and only if the quotient ring R/P has no **zero divisors**: nonzero elements whose product is zero. A commutative ring with unity and no zero divisors is called an **integral domain**, and the correspondence reads: R/P is an integral domain ⟺ P is prime.

An ideal M is **maximal** if no ideal sits strictly between M and all of R: there is no ideal J with M ⊊ J ⊊ R. Geometrically, M is as "large" as an ideal can be while remaining proper. The quotient R/M then has no nontrivial ideals of its own — and a commutative ring with unity and no nontrivial ideals is exactly a **field**. So R/M is a field ⟺ M is maximal.

The logical relationship between these: every maximal ideal is prime (because every field is an integral domain), but not every prime ideal is maximal. In ℤ, (0) is prime but not maximal, because (0) ⊊ (2) ⊊ ℤ. In a field itself, (0) is both prime and maximal. This hierarchy — fields inside integral domains inside general rings, mirrored by maximal ideals inside prime ideals inside general ideals — becomes the backbone of commutative algebra and algebraic geometry, where ideals correspond to algebraic varieties and the prime/maximal distinction tracks which varieties are irreducible versus which are points.
