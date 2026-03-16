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
status: draft
---

# Unique Factorization Domains

## Core Idea
A unique factorization domain (UFD) is an integral domain in which every nonzero, non-unit element can be factored uniquely (up to order and units) into irreducible elements.

## Explainer

The Fundamental Theorem of Arithmetic says every positive integer factors uniquely into primes: 60 = 2² × 3 × 5, and no other prime factorization exists. This seems obvious in ℤ, but it is a special property that many integral domains do *not* share. Understanding when unique factorization holds — and when it fails — is the central question UFDs answer.

Consider the ring ℤ[√-5] = {a + b√-5 : a, b ∈ ℤ}. This is an integral domain, but 6 = 2 × 3 = (1 + √-5)(1 − √-5) are two genuinely different factorizations into irreducible elements. Neither 2 nor 3 divides (1 ± √-5), and neither (1 ± √-5) divides 2 or 3. Unique factorization has failed completely. This example, studied by Kummer in the 1840s in connection with Fermat's Last Theorem, motivated the entire theory of ideals and the ring hierarchy.

A **unique factorization domain** avoids this pathology. The definition has two parts: every nonzero non-**unit** (an element with a multiplicative inverse, like ±1 in ℤ) must factor into **irreducible elements** (existence), and any two such factorizations must agree up to reordering and multiplication by units (uniqueness). In ℤ, the units ±1 account for why 12 = 2² × 3 and −12 = (−1)(2²)(3) are considered the same factorization.

The key structural result is that **every principal ideal domain (PID) is a UFD** — the algebraic structure of PID ideals forces unique factorization to hold, much as in ℤ. The full hierarchy runs: fields ⊂ Euclidean domains ⊂ PIDs ⊂ UFDs ⊂ integral domains. Each inclusion is strict: ℤ[x] is a UFD but not a PID (the ideal (2, x) is not principal). The polynomial ring k[x] over a field is always a PID (hence a UFD), which is why polynomial factorization is unique — a fact that underlies every factoring algorithm you've used in algebra.
