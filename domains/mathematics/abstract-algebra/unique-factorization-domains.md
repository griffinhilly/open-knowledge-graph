---
id: unique-factorization-domains
title: Unique Factorization Domains
domain: mathematics
course: abstract-algebra
prerequisites:
- id: principal-ideal-domains
  type: hard
builds-toward:
- polynomial-rings
tags:
- ufd
- unique-factorization
- irreducible
- prime
stage: advanced
status: validated
---

# Unique Factorization Domains

## Core Idea
A unique factorization domain (UFD) is an integral domain in which every nonzero, non-unit element can be factored uniquely (up to order and units) into irreducible elements.

## Questions

```yaml
- question: "The ring ℤ[x] of polynomials with integer coefficients is a UFD but not a PID, because the ideal (2, x) is not principal. What does this tell you about the relationship between PIDs and UFDs?"
  type: multiple-choice
  options:
    - "ℤ[x] cannot be a UFD if it is not a PID — the claim must be wrong"
    - "UFDs are a strictly larger class than PIDs: every PID is a UFD, but there exist UFDs that are not PIDs"
    - "PIDs and UFDs are incomparable properties — neither implies the other"
    - "ℤ[x] is a UFD only because x is transcendental; algebraic extensions of ℤ are never UFDs"
  answer: 1
  explanation: "The hierarchy is fields ⊂ Euclidean domains ⊂ PIDs ⊂ UFDs ⊂ integral domains, and each inclusion is strict. Every PID is a UFD (the ideal structure of PIDs forces unique factorization), but the converse fails: ℤ[x] is a UFD (every polynomial over ℤ factors uniquely into irreducibles) but is not a PID because (2, x) requires two generators. This shows UFDs have better factorization structure than typical integral domains, but not necessarily the strong ideal structure of PIDs."

- question: "In which of the following rings does the element 6 fail to have a unique factorization into irreducibles?"
  type: multiple-choice
  options:
    - "ℤ (the integers)"
    - "ℤ[i] (the Gaussian integers)"
    - "ℤ[√−5]"
    - "ℤ[x] (polynomials with integer coefficients)"
  answer: 2
  explanation: "In ℤ[√−5], we have 6 = 2 × 3 = (1 + √−5)(1 − √−5), and these are genuinely distinct factorizations into irreducibles — the factors are not associates of each other (no unit relates them). Both ℤ and ℤ[i] are Euclidean domains, hence PIDs, hence UFDs, so factorization in them is unique. ℤ[x] is also a UFD. The pathological example ℤ[√−5] is the canonical demonstration that unique factorization is not automatic in algebraic number rings."

- question: "Every principal ideal domain (PID) is a unique factorization domain."
  type: true-false
  answer: true
  explanation: "This is a fundamental theorem in ring theory. The ideal structure of a PID — specifically the ascending chain condition on ideals and the fact that every prime ideal is maximal — forces the two conditions of a UFD: every nonzero non-unit factors into irreducibles (existence), and the factorization is unique up to order and units. The proof uses the fact that in a PID, irreducible elements and prime elements coincide, which is the key property that guarantees uniqueness."

- question: "Nearly every UFD is also a PID."
  type: true-false
  answer: false
  explanation: "The inclusion is strict: PIDs ⊂ UFDs, but not every UFD is a PID. The ring ℤ[x] is the standard counterexample — it has unique factorization (every polynomial over ℤ factors uniquely into irreducible polynomials), but the ideal (2, x) = {2f(x) + x·g(x) : f, g ∈ ℤ[x]} is not principal. No single polynomial generates all elements of this ideal. Unique factorization is a property of elements; being a PID is a property of ideals — and the latter is a stronger structural requirement."

- question: "Why does ℤ[√−5] fail to be a UFD? Identify the two distinct factorizations of 6 and explain why they cannot be considered equivalent."
  type: short-answer
  answer: "In ℤ[√−5], 6 factors as 2 × 3 and also as (1 + √−5)(1 − √−5), since (1 + √−5)(1 − √−5) = 1 + 5 = 6. These are genuinely distinct because the four elements 2, 3, (1 + √−5), (1 − √−5) are all irreducible (verified by the norm N(a + b√−5) = a² + 5b²: no element has norm 2 or 3) and no two of them are associates (there are no units other than ±1, and none of the four are ±1 multiples of each other). Unique factorization requires factorizations to agree up to order and units, but there is no unit relating the two factorizations."
  explanation: "The failure of unique factorization in ℤ[√−5] stems from the divergence of irreducible and prime elements in that ring. In a UFD, these must coincide. The element 2 is irreducible in ℤ[√−5] (norm 4, no factorization into elements of norm 2) but is NOT prime: 2 divides (1 + √−5)(1 − √−5) = 6, but 2 divides neither factor. This violation of the prime property is what breaks uniqueness. In ℤ or any PID, irreducible implies prime, which is exactly what guarantees the Fundamental Theorem of Arithmetic."
```

## Explainer

The Fundamental Theorem of Arithmetic says every positive integer factors uniquely into primes: 60 = 2² × 3 × 5, and no other prime factorization exists. This seems obvious in ℤ, but it is a special property that many integral domains do *not* share. Understanding when unique factorization holds — and when it fails — is the central question UFDs answer.

Consider the ring ℤ[√-5] = {a + b√-5 : a, b ∈ ℤ}. This is an integral domain, but 6 = 2 × 3 = (1 + √-5)(1 − √-5) are two genuinely different factorizations into irreducible elements. Neither 2 nor 3 divides (1 ± √-5), and neither (1 ± √-5) divides 2 or 3. Unique factorization has failed completely. This example, studied by Kummer in the 1840s in connection with Fermat's Last Theorem, motivated the entire theory of ideals and the ring hierarchy.

A **unique factorization domain** avoids this pathology. The definition has two parts: every nonzero non-**unit** (an element with a multiplicative inverse, like ±1 in ℤ) must factor into **irreducible elements** (existence), and any two such factorizations must agree up to reordering and multiplication by units (uniqueness). In ℤ, the units ±1 account for why 12 = 2² × 3 and −12 = (−1)(2²)(3) are considered the same factorization.

The key structural result is that **every principal ideal domain (PID) is a UFD** — the algebraic structure of PID ideals forces unique factorization to hold, much as in ℤ. The full hierarchy runs: fields ⊂ Euclidean domains ⊂ PIDs ⊂ UFDs ⊂ integral domains. Each inclusion is strict: ℤ[x] is a UFD but not a PID (the ideal (2, x) is not principal). The polynomial ring k[x] over a field is always a PID (hence a UFD), which is why polynomial factorization is unique — a fact that underlies every factoring algorithm you've used in algebra.
