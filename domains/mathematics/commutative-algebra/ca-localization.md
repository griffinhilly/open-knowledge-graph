---
id: ca-localization
title: Localization
domain: mathematics
course: commutative-algebra
prerequisites:
- id: integral-domains
  type: hard
- id: ring-homomorphisms
  type: hard
builds-toward:
- ca-local-rings
- ca-discrete-valuation-rings
tags:
- localization
- multiplicative-set
- fraction
- local-global
stage: expert
status: validated
---

# Localization

## Core Idea
Localization generalizes the construction of fractions. Given a commutative ring R and a multiplicatively closed subset S, the localization S⁻¹R consists of formal fractions r/s with r ∈ R, s ∈ S, subject to the same equivalence relation as ordinary fractions. This construction lets you "zoom in" on the behavior of a ring near a prime ideal by inverting everything outside it, reducing global questions to local ones.

## Questions

```yaml
- question: "What is the localization of ℤ at the multiplicative set S = {1, 2, 4, 8, ...} = {2ⁿ : n ≥ 0}?"
  type: multiple-choice
  options:
    - "The ring ℤ[1/2] of fractions with denominator a power of 2"
    - "The field ℚ of all rational numbers"
    - "The ring ℤ/(2) of integers modulo 2"
    - "The ring of 2-adic integers ℤ₂"
  answer: 0
  explanation: "Localizing ℤ at S = {2ⁿ} inverts exactly the powers of 2, producing fractions a/2ⁿ — the ring ℤ[1/2]. This ring sits strictly between ℤ and ℚ: it contains 3/4 and 7/8 but not 1/3. To get all of ℚ, you would localize at S = ℤ \\ {0}, inverting all nonzero integers. Localization at a single element (or powers of it) is the simplest non-trivial example and illustrates how localization selectively enlarges a ring."

- question: "When localizing a ring R at a prime ideal 𝔭, you form S⁻¹R where S = R \\ 𝔭. Why must S be multiplicatively closed?"
  type: multiple-choice
  options:
    - "S is not always multiplicatively closed — it works only because prime ideals are maximal"
    - "S = R \\ 𝔭 is multiplicatively closed precisely because 𝔭 is prime: if a, b ∉ 𝔭, then ab ∉ 𝔭 (otherwise 𝔭 would contain a or b by the prime property)"
    - "S is multiplicatively closed because R \\ 𝔭 is always a subring"
    - "Multiplicative closure is not actually required for localization to work"
  answer: 1
  explanation: "The definition of a prime ideal says: if ab ∈ 𝔭 then a ∈ 𝔭 or b ∈ 𝔭. Contrapositively: if a ∉ 𝔭 and b ∉ 𝔭, then ab ∉ 𝔭. This is exactly the statement that S = R \\ 𝔭 is closed under multiplication. Since 1 ∉ 𝔭 (prime ideals are proper), S also contains 1. This is one of the key reasons prime ideals, rather than arbitrary ideals, play a central role in commutative algebra — their complements are the right sets to localize at."

- question: "If R is an integral domain, the localization of R at S = R \\ {0} is the field of fractions of R."
  type: true-false
  answer: true
  explanation: "When S = R \\ {0}, you invert every nonzero element, producing all fractions a/b with b ≠ 0. For R = ℤ, this gives ℚ. For R = k[x], this gives k(x), the field of rational functions. The field of fractions is the 'most localized' version of an integral domain — you have made every nonzero element invertible, which is exactly what it means to be a field. Every other localization of R (at a smaller multiplicative set) sits between R and its fraction field."

- question: "Localization is an exact functor on modules."
  type: true-false
  answer: true
  explanation: "If 0 → M' → M → M'' → 0 is an exact sequence of R-modules, then 0 → S⁻¹M' → S⁻¹M → S⁻¹M'' → 0 is exact as S⁻¹R-modules. This exactness — localization preserves kernels and cokernels — is fundamental. It means properties like 'an element is zero' or 'a map is surjective' can be checked locally at each prime ideal. This is the algebraic foundation of the local-global principle."

- question: "Explain what it means to 'localize ℤ at the prime ideal (5)' and describe the resulting ring."
  type: short-answer
  answer: "Localizing ℤ at (5) means forming S⁻¹ℤ where S = ℤ \\ (5) — all integers not divisible by 5. The result is the ring ℤ₍₅₎ of fractions a/b where b is not divisible by 5. This ring contains ℤ but not all of ℚ: 1/3 ∈ ℤ₍₅₎ but 1/5 ∉ ℤ₍₅₎. It is a local ring with unique maximal ideal 5ℤ₍₅₎, consisting of fractions a/b where 5 | a but 5 ∤ b. Every element not in this maximal ideal is a unit."
  explanation: "Localization at a prime 'zooms in' on divisibility by that prime, forgetting all other primes. In ℤ₍₅₎, the primes 2, 3, 7, etc. become invertible (harmless units), and only the prime 5 retains its special status. This is why the resulting ring is local — there is exactly one prime left to worry about. This construction is the algebraic analog of looking at a geometric object near a specific point."
```

## Explainer

The construction of the rational numbers from the integers — forming fractions a/b with b ≠ 0 — is the prototype of localization. In commutative algebra, **localization** generalizes this by letting you choose which denominators to allow. Given a commutative ring R and a **multiplicatively closed set** S ⊆ R (meaning 1 ∈ S and if s, t ∈ S then st ∈ S), the localization S⁻¹R consists of formal fractions r/s, where two fractions r/s and r'/s' are identified if there exists u ∈ S with u(rs' - r's) = 0.

The two most important cases are localization at a single element and localization at a prime ideal. **Localizing at an element** f means taking S = {1, f, f², ...}, producing R_f = R[1/f], the ring where f becomes invertible. **Localizing at a prime ideal** 𝔭 means taking S = R \ 𝔭, inverting everything outside 𝔭. The result, written R_𝔭, is a **local ring** — a ring with exactly one maximal ideal. This is the most powerful application: it lets you study the behavior of R "near 𝔭" by making all other prime structure invisible.

Localization has excellent algebraic properties. It is an **exact functor**: it preserves short exact sequences of modules, meaning it commutes with taking kernels, images, and cokernels. It also commutes with taking quotients, sums, and intersections of ideals. The ideal structure of S⁻¹R is simpler than that of R: the prime ideals of S⁻¹R correspond exactly to the prime ideals of R that are disjoint from S. When localizing at 𝔭, this means the primes of R_𝔭 are exactly the primes of R contained in 𝔭, with 𝔭 itself becoming the unique maximal ideal.

The **local-global principle** is the philosophical payoff. Many properties of a ring or module hold globally (over R) if and only if they hold locally (over R_𝔭 for every prime 𝔭). For instance, a module is zero if and only if it is zero after localizing at every prime. An R-module homomorphism is injective (or surjective) if and only if it is so after every localization. This reduces hard global questions to easier local ones, where you work in a ring with a single maximal ideal and can exploit the special structure of local rings.
