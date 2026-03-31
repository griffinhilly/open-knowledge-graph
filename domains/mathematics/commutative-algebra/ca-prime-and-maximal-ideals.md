---
id: ca-prime-and-maximal-ideals
title: Prime and Maximal Ideals
domain: mathematics
course: commutative-algebra
prerequisites:
- id: subrings-ideals
  type: hard
- id: integral-domains
  type: hard
builds-toward:
- ca-local-rings
- ca-localization
- ca-primary-decomposition
- ca-spec-and-zariski-topology
- ca-krull-dimension
tags:
- prime-ideal
- maximal-ideal
- spectrum
- zorns-lemma
- quotient-ring
stage: expert
status: validated
---

# Prime and Maximal Ideals

## Core Idea
A prime ideal P of a commutative ring R is a proper ideal such that ab in P implies a in P or b in P -- equivalently, R/P is an integral domain. A maximal ideal M is a proper ideal contained in no larger proper ideal -- equivalently, R/M is a field. Every maximal ideal is prime, but not conversely. The existence of maximal ideals (via Zorn's lemma) and the structure of the set of all prime ideals (the spectrum Spec R) are foundational to commutative algebra and algebraic geometry.

## Questions

```yaml
- question: "Which of the following is a prime ideal of Z[x] that is NOT maximal?"
  type: multiple-choice
  options:
    - "(2, x)"
    - "(x)"
    - "(5, x)"
    - "(3, x^2 + 1)"
  answer: 1
  explanation: "The ideal (x) is prime because Z[x]/(x) ≅ Z is an integral domain. But it is not maximal because Z is not a field. By contrast, (2, x) is maximal since Z[x]/(2, x) ≅ Z/2Z ≅ F_2, a field, and similarly for (5, x) and (3, x^2 + 1)."

- question: "In a commutative ring R, the intersection of all prime ideals equals the nilradical (the set of nilpotent elements)."
  type: true-false
  answer: true
  explanation: "This is a fundamental result. If a^n = 0, then a^n lies in every prime ideal, and since primes absorb factors, a itself lies in every prime ideal. Conversely, if a is not nilpotent, one constructs a prime ideal avoiding all powers of a using Zorn's lemma applied to the set of ideals disjoint from {1, a, a^2, ...}."

- question: "In the ring Z/12Z, list all prime ideals."
  type: short-answer
  answer: "(2)/(12) and (3)/(12), corresponding to the prime factors of 12."
  explanation: "The prime ideals of Z/nZ correspond to the prime ideals of Z containing nZ, which are (p) for primes p dividing n. Since 12 = 2^2 * 3, the prime ideals of Z/12Z are the images of (2) and (3). These are also the maximal ideals, since Z/12Z modulo either is a field."

- question: "Every commutative ring with unity has at least one maximal ideal."
  type: true-false
  answer: true
  explanation: "This is a direct application of Zorn's lemma. The set of proper ideals of R, ordered by inclusion, is nonempty (it contains (0) if R is not the zero ring) and every chain has an upper bound (the union of a chain of proper ideals is a proper ideal since 1 is not in any member). Zorn's lemma gives a maximal element. Note: the zero ring has no maximal ideal, but by convention the statement requires R ≠ 0."

- question: "Explain why every maximal ideal is prime, and give an example of a prime ideal that is not maximal."
  type: short-answer
  answer: "If M is maximal, then R/M is a field, hence an integral domain, so M is prime. The ideal (0) in Z is prime (since Z is a domain) but not maximal (since Z is not a field)."
  explanation: "The key is the characterization via quotient rings: M prime iff R/M is a domain, M maximal iff R/M is a field. Every field is a domain, so maximal implies prime. In Z, (0) is prime but (0) subset (2) shows it is not maximal. In k[x, y], (x) is prime (quotient is k[y], a domain) but not maximal (quotient is not a field)."
```

## Explainer

Prime and maximal ideals are the two most important classes of ideals in commutative algebra. A proper ideal P of a commutative ring R is **prime** if whenever ab belongs to P, at least one of a or b belongs to P. Equivalently, the quotient ring R/P is an integral domain. A proper ideal M is **maximal** if there is no ideal strictly between M and R -- equivalently, R/M is a field. Since every field is an integral domain, every maximal ideal is prime. The converse fails: in the integers Z, the zero ideal (0) is prime (since Z is a domain) but not maximal (since Z is not a field).

The existence of maximal ideals relies on **Zorn's lemma**, an axiom equivalent to the axiom of choice. Given any proper ideal I, the collection of proper ideals containing I is partially ordered by inclusion, and every chain in this poset has an upper bound (the union, which is still a proper ideal since 1 is not in any member of the chain). Zorn's lemma then guarantees a maximal element. This argument is used constantly in commutative algebra: the existence of prime ideals containing a given ideal, the existence of minimal primes, and many localization arguments all trace back to this Zorn's lemma template.

The set of all prime ideals of R, denoted **Spec R** (the spectrum), is far more than a bare set. It carries the Zariski topology, making it a topological space, and a structure sheaf, making it a locally ringed space. This is the foundation of modern algebraic geometry, where commutative rings are studied through their spectra. The closed points of Spec R correspond to maximal ideals (the "geometric points"), while non-closed points correspond to non-maximal primes (generic points of subvarieties). The passage from a ring to its spectrum is a contravariant functor that converts ring homomorphisms into continuous maps.

In a Noetherian ring, every prime ideal is finitely generated, and the set of minimal primes over any ideal is finite. These finiteness results make the spectrum of a Noetherian ring well-behaved enough for dimension theory (Krull dimension = supremum of lengths of chains of prime ideals) and primary decomposition (every ideal decomposes into components "supported" at finitely many primes). Understanding prime and maximal ideals is the entry point to all of these deeper theories.
