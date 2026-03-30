---
id: ca-dedekind-domains
title: Dedekind Domains
domain: mathematics
course: commutative-algebra
prerequisites:
- id: principal-ideal-domains
  type: hard
- id: integral-domains
  type: hard
builds-toward:
- ca-discrete-valuation-rings
tags:
- dedekind-domain
- ideal-class-group
- fractional-ideal
- unique-factorization-of-ideals
stage: expert
status: validated
---

# Dedekind Domains

## Core Idea
A Dedekind domain is a Noetherian, integrally closed, one-dimensional integral domain. While elements in a Dedekind domain may not factor uniquely (ℤ[√-5] is the classic example), every nonzero ideal factors uniquely as a product of prime ideals. This "unique factorization of ideals" recovers the arithmetic lost at the element level and is the foundation of algebraic number theory.

## Questions

```yaml
- question: "The ring ℤ[√-5] is not a UFD because 6 = 2 × 3 = (1+√-5)(1-√-5) are distinct element factorizations. However, ℤ[√-5] is a Dedekind domain. What does this mean concretely?"
  type: multiple-choice
  options:
    - "Unique factorization of elements is secretly valid if you allow complex units"
    - "Every nonzero ideal of ℤ[√-5] factors uniquely as a product of prime ideals, restoring a form of unique factorization at the ideal level"
    - "The ring is actually a PID when you localize at every prime"
    - "ℤ[√-5] has unique factorization after adjoining finitely many new elements"
  answer: 1
  explanation: "In ℤ[√-5], the ideal (6) factors as (2, 1+√-5)²(3, 1+√-5)(3, 1-√-5) — a product of prime ideals. The two element factorizations 2·3 and (1+√-5)(1-√-5) correspond to different groupings of these prime ideal factors. This unique factorization of ideals is the defining feature of Dedekind domains and was Dedekind's great insight: when elements don't factor uniquely, pass to ideals, which always do."

- question: "Which of the following is NOT a characterization of Dedekind domains?"
  type: multiple-choice
  options:
    - "Noetherian, integrally closed, dimension 1"
    - "Every nonzero ideal factors uniquely into prime ideals"
    - "Every nonzero fractional ideal is invertible"
    - "Every ideal is principal"
  answer: 3
  explanation: "The first three are equivalent characterizations of Dedekind domains. The fourth describes PIDs, which are a strictly smaller class. Every PID is a Dedekind domain (it is Noetherian, integrally closed, and has dimension 1 since nonzero primes are maximal), but Dedekind domains like ℤ[√-5] need not be PIDs. The class group of a Dedekind domain — the group of fractional ideals modulo principal ones — measures exactly how far the domain is from being a PID."

- question: "Every PID is a Dedekind domain."
  type: true-false
  answer: true
  explanation: "A PID is an integral domain where every ideal is principal. It is automatically Noetherian (every ideal has one generator), integrally closed (PIDs are UFDs, and UFDs are integrally closed), and one-dimensional (every nonzero prime ideal is maximal in a PID). These three conditions are exactly the definition of a Dedekind domain. The converse fails: ℤ[√-5] is a Dedekind domain but not a PID."

- question: "The class group of a Dedekind domain is trivial if and only if the domain is a PID."
  type: true-false
  answer: true
  explanation: "The class group Cl(R) of a Dedekind domain R is the group of fractional ideals modulo principal fractional ideals. It is trivial — consisting of just the identity — precisely when every fractional ideal is principal, which happens if and only if every ideal is principal (i.e., R is a PID). The class number |Cl(R)| measures the failure of unique factorization at the element level. For ℤ[√-5], the class number is 2."

- question: "Explain why unique factorization of ideals in a Dedekind domain can be viewed as 'rescuing' the unique factorization that fails at the element level."
  type: short-answer
  answer: "In a UFD, every element factors uniquely into irreducibles. In a Dedekind domain that is not a UFD (like ℤ[√-5]), elements can have multiple genuinely distinct factorizations. But every nonzero ideal factors uniquely into prime ideals. The principal ideal (6) in ℤ[√-5] factors into four prime ideals, and the two element factorizations 2·3 and (1+√-5)(1-√-5) correspond to grouping those prime ideal factors differently. The 'lost' uniqueness at the element level is recovered at the ideal level — prime ideals serve as the 'true primes' of the ring."
  explanation: "This perspective was historically revolutionary. Kummer originally introduced 'ideal numbers' to restore unique factorization in cyclotomic rings. Dedekind formalized this as the theory of ideals. The insight is that individual elements may be too coarse to capture the arithmetic structure — ideals, being sets of elements, carry finer information. This is why algebraic number theory is fundamentally about ideals, not elements."
```

## Explainer

In a principal ideal domain like ℤ, every nonzero element factors uniquely into primes. But many rings of algebraic integers — like ℤ[√-5], where 6 = 2 × 3 = (1 + √-5)(1 - √-5) — lose this property. The question that drove 19th-century number theory was: can anything be salvaged? Dedekind's answer was yes, by shifting attention from elements to ideals. A **Dedekind domain** is an integral domain that is Noetherian, integrally closed in its fraction field, and has Krull dimension 1 (every nonzero prime ideal is maximal). In such a ring, every nonzero ideal factors uniquely as a product of prime ideals.

The three conditions in the definition each contribute something essential. **Noetherian** ensures every ideal is finitely generated, preventing pathological infinite behavior. **Integrally closed** prevents the ring from "missing" elements it should contain (ℤ[√-3] is not integrally closed and is not a Dedekind domain, but its integral closure ℤ[(1+√-3)/2] is). **Dimension 1** means the prime ideal structure is as simple as possible beyond the trivial cases: primes are either zero or maximal, with no chains of length 2 or more.

The payoff is **unique factorization of ideals**. In ℤ[√-5], the ideal (6) = (2, 1+√-5)² · (3, 1+√-5) · (3, 1-√-5). Each factor is a prime ideal, and this factorization is unique. The two element-level factorizations 2·3 and (1+√-5)(1-√-5) arise from different ways of combining these prime ideal factors into principal ideals. The **class group** Cl(R) measures how far a Dedekind domain is from being a PID: it is the group of fractional ideals modulo principal ones, and Cl(R) = 0 if and only if R is a PID. For ℤ[√-5], the class group has order 2, reflecting a single obstruction to principality.

Every ring of algebraic integers in a number field is a Dedekind domain, making this class central to algebraic number theory. Beyond number theory, Dedekind domains appear as coordinate rings of smooth algebraic curves and in the study of one-dimensional regular schemes. The local behavior of a Dedekind domain at each prime is captured by a discrete valuation ring (DVR), and the global-to-local passage — studying a Dedekind domain through its localizations — is a fundamental technique that extends far beyond the one-dimensional case.
