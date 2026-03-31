---
id: ca-chain-conditions
title: Chain Conditions and Artinian Rings
domain: mathematics
course: commutative-algebra
prerequisites:
- id: ca-noetherian-rings
  type: hard
- id: ca-prime-and-maximal-ideals
  type: hard
builds-toward:
- ca-krull-dimension
- ca-associated-primes
tags:
- artinian-ring
- ascending-chain-condition
- descending-chain-condition
- composition-series
- hopkins-levitzki
stage: expert
status: validated
---

# Chain Conditions and Artinian Rings

## Core Idea
The ascending chain condition (ACC) on ideals defines Noetherian rings; the descending chain condition (DCC) on ideals defines Artinian rings. A commutative Artinian ring is always Noetherian, has Krull dimension zero (every prime ideal is maximal), and decomposes as a finite product of Artinian local rings. The Hopkins-Levitzki theorem establishes that DCC implies ACC for modules over Artinian rings, revealing that the descending chain condition is strictly stronger than the ascending one in the commutative setting.

## Questions

```yaml
- question: "Which of the following rings is Artinian?"
  type: multiple-choice
  options:
    - "The integers Z"
    - "The polynomial ring k[x] over a field k"
    - "The quotient ring k[x]/(x^3)"
    - "The formal power series ring k[[x]]"
  answer: 2
  explanation: "k[x]/(x^3) is a finite-dimensional k-vector space (basis {1, x, x^2}), so it satisfies DCC on ideals. Its only prime ideal is (x)/(x^3), which is also maximal, consistent with Krull dimension zero. The other rings all have infinite descending chains or infinite Krull dimension."

- question: "A commutative Artinian ring has Krull dimension zero."
  type: true-false
  answer: true
  explanation: "In an Artinian ring, every prime ideal is maximal. Proof: if P is prime, then R/P is an Artinian domain. In an Artinian domain, every nonzero element is a unit (given 0 ≠ a, the chain (a) ⊇ (a^2) ⊇ ... stabilizes, so a^n = ba^(n+1), giving 1 = ba by cancellation). So R/P is a field, making P maximal. Since every prime is maximal, no chain of primes has length > 0."

- question: "The ring Z is Noetherian but not Artinian. Give a descending chain of ideals in Z that does not stabilize."
  type: short-answer
  answer: "(2) ⊃ (4) ⊃ (8) ⊃ (16) ⊃ ... , i.e., (2^n) for n = 1, 2, 3, ..., is a strictly descending chain."
  explanation: "Each (2^n) strictly contains (2^(n+1)) since 2^n is not a multiple of 2^(n+1). This chain never stabilizes, so Z fails DCC. More generally, any Noetherian domain that is not a field fails to be Artinian, since it has Krull dimension at least 1."

- question: "Every commutative Artinian ring is Noetherian, but the converse is false."
  type: true-false
  answer: true
  explanation: "The Hopkins-Levitzki theorem proves that DCC implies ACC for commutative rings (and more generally for modules over left-Artinian rings). The converse fails because Z is Noetherian but not Artinian. The key asymmetry is that DCC forces Krull dimension 0 and finite length, while ACC allows arbitrary Krull dimension."
```

## Explainer

Chain conditions are finiteness constraints on the partially ordered set of ideals (or submodules) of a ring. The **ascending chain condition (ACC)** requires that every ascending chain I_1 ⊆ I_2 ⊆ I_3 ⊆ ... eventually stabilizes. The **descending chain condition (DCC)** requires the same for descending chains I_1 ⊇ I_2 ⊇ I_3 ⊇ .... Rings satisfying ACC are Noetherian; rings satisfying DCC are **Artinian** (named after Emil Artin). These are the two fundamental finiteness hypotheses in ring theory.

In the commutative setting, the Artinian condition is strictly stronger than the Noetherian condition. The **Hopkins-Levitzki theorem** establishes that every commutative Artinian ring is Noetherian. The converse fails spectacularly: Z is Noetherian but not Artinian, since (p) ⊃ (p^2) ⊃ (p^3) ⊃ ... never stabilizes for any prime p. The essential reason is that Artinian rings have **Krull dimension zero** -- every prime ideal is maximal. The proof is elegant: if P is a prime ideal of an Artinian ring R, then R/P is an Artinian integral domain. The DCC forces every nonzero element to be a unit (the chain (a) ⊇ (a^2) ⊇ ... stabilizes, yielding invertibility), so R/P is a field and P is maximal.

The structure theory of Artinian rings is remarkably clean. Every commutative Artinian ring decomposes as a **finite product of Artinian local rings** -- this is the Artinian analogue of the Chinese Remainder Theorem. Each factor has a unique maximal ideal whose powers eventually vanish (the ring is a "thickened point" in geometric language). The number of factors equals the number of maximal ideals, which is finite. This decomposition reduces many questions about Artinian rings to the local case.

Artinian rings and modules play a central role in several areas of commutative algebra. **Composition series** (finite chains with simple successive quotients) exist precisely for modules that are both Noetherian and Artinian, and the Jordan-Holder theorem guarantees that the length of such a series is an invariant. The notion of **length** of a module generalizes dimension of a vector space and is the starting point for multiplicity theory and intersection theory in algebraic geometry. Artinian rings also appear as completions of local rings modulo powers of the maximal ideal, connecting chain conditions to the theory of formal neighborhoods.
