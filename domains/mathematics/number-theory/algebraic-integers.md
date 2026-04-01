---
id: algebraic-integers
title: Algebraic Integers
domain: mathematics
course: number-theory
prerequisites:
- id: field-extensions
  type: hard
- id: ring-definition-and-examples
  type: hard
builds-toward:
- gaussian-integers
- norm-algebraic-number-fields
tags:
- algebraic-integers
- algebraic-number-theory
stage: expert
status: validated
---

# Algebraic Integers

## Core Idea
An algebraic integer is a complex root of a monic integer polynomial. Algebraic integers in a number field K form a ring, generalizing ℤ. Gaussian integers ℤ[i] and Eisenstein integers ℤ[ω] exemplify this structure.

## Questions

```yaml
- question: "Is 1/2 an algebraic integer? Which answer correctly identifies the status of 1/2 and explains why?"
  type: multiple-choice
  options:
    - "Yes — it satisfies 2x − 1 = 0, which has integer coefficients, so it is an algebraic integer"
    - "No — it is not an integer, and only integers can be algebraic integers"
    - "No — no monic polynomial with integer coefficients has 1/2 as a root, so the defining criterion is not met"
    - "Yes — all rational numbers are algebraic integers because they can be expressed with integer numerators and denominators"
  answer: 2
  explanation: "The definition requires a *monic* polynomial with integer coefficients — leading coefficient must be 1. The number 1/2 satisfies 2x − 1 = 0, but this polynomial is not monic. If you try to write a monic polynomial with 1/2 as a root, you get x − 1/2 = 0, whose coefficients are not all integers. Option A is the classic misconception: any polynomial with integer coefficients is not sufficient; the monic requirement is the whole point. The rational algebraic integers are exactly ℤ itself — rational numbers with no integer polynomial whose monic version has integer coefficients."

- question: "In ℚ(√−3), the ring of integers 𝒪_K turns out to be ℤ[ω] where ω = (−1 + √−3)/2, not just ℤ[√−3]. This is initially surprising because ω looks like a 'half-integer.' Why does ω qualify as an algebraic integer?"
  type: multiple-choice
  options:
    - "Because ω has absolute value less than 1, placing it within the unit disk where all algebraic integers live"
    - "Because ω satisfies x² + x + 1 = 0, which is monic with integer coefficients, so the definition is satisfied"
    - "Because ω is a primitive cube root of unity and all roots of unity are automatically algebraic integers by convention"
    - "Because ℤ[ω] contains ℤ as a subring, and any extension of ℤ consists of algebraic integers"
  answer: 1
  explanation: "The answer is purely definitional: ω satisfies x² + x + 1 = 0, which is monic (leading coefficient 1) with integer coefficients (1, 1, 1). That is the complete criterion for being an algebraic integer, and ω meets it. Option C contains a true statement — roots of unity are algebraic integers — but the *reason* is that they satisfy monic integer polynomials like xⁿ − 1 = 0, not 'by convention.' Option D is false: extensions of ℤ can contain non-integers (like ℚ). The 'half-integer' appearance of ω is misleading intuition that the monic polynomial criterion overrides."

- question: "The sum and product of two algebraic integers are always algebraic integers — that is, the set of algebraic integers in any number field forms a ring."
  type: true-false
  answer: true
  explanation: "This is one of the key structural facts about algebraic integers. If α satisfies a monic integer polynomial of degree m and β satisfies one of degree n, then both α + β and αβ satisfy monic integer polynomials of degree at most mn. The proof uses the fact that the minimal polynomial of α + β divides the characteristic polynomial of a certain matrix constructed over ℤ. This closure under addition and multiplication is what makes 𝒪_K a ring — and it's not at all obvious from the definition alone."

- question: "A number is an algebraic integer if and only if it is a root of some polynomial with integer coefficients."
  type: true-false
  answer: false
  explanation: "The 'monic' requirement is essential and this statement omits it. Every algebraic integer is indeed a root of an integer polynomial, but the converse fails: 1/2 is a root of 2x − 1 = 0 (an integer polynomial) but is not an algebraic integer because no *monic* integer polynomial has 1/2 as a root. The distinction between 'integer polynomial' and 'monic integer polynomial' is precisely what separates algebraic numbers (roots of any integer polynomial, monic or not) from algebraic integers (roots of monic integer polynomials). Rational algebraic numbers that are not integers, like 1/2 or 2/3, are always excluded by the monic requirement."

- question: "Explain why the monic requirement in the definition of algebraic integer is essential. What goes wrong — concretely — if we drop it and allow any polynomial with integer coefficients?"
  type: short-answer
  answer: "If we drop the monic requirement and define 'algebraic integer' as any root of any polynomial with integer coefficients, then every algebraic number would qualify — including 1/2 (root of 2x − 1 = 0) and 1/3 (root of 3x − 1 = 0). The resulting set would just be the algebraic numbers ℚ-bar, which is a field, not a useful generalization of ℤ. The monic requirement is what ensures that the rational algebraic integers are exactly ℤ itself — giving the right generalization: just as ℤ ⊂ ℚ, so 𝒪_K ⊂ K, and the 'integers' of K are the ones satisfying the monic condition."
  explanation: "The monic requirement is the defining feature that makes algebraic integers a genuine generalization of ordinary integers rather than a trivial extension. It ensures that the notion of 'integer' in any number field reduces to ℤ when restricted to ℚ, and it produces a ring (closed under addition and multiplication) rather than an arbitrary subset. Without it, the theory loses its structural content and the connection to factorization and ideal theory in number fields collapses."
```

## Explainer

You already know that ℤ sits inside ℚ as a distinguished subring — the integers are special among rationals because they have no denominator. When you studied field extensions, you learned to build bigger fields like ℚ(√2) or ℚ(i) by adjoining roots of polynomials. The natural next question is: what plays the role of ℤ inside these larger fields? The answer is the **ring of algebraic integers**, and the key criterion is surprisingly simple: a number is an algebraic integer if it satisfies a monic polynomial with integer coefficients.

The word "monic" is what distinguishes algebraic integers from algebraic numbers more broadly. The number √2 is an algebraic integer because it satisfies x² − 2 = 0, which is monic (leading coefficient 1) with integer coefficients. The number 1/2 is an algebraic number (it satisfies 2x − 1 = 0) but not an algebraic integer — you cannot write a monic integer polynomial with 1/2 as a root. The rational algebraic integers are exactly ℤ itself, which gives you the right intuition: "algebraic integer" really is a generalization of "ordinary integer."

From your ring theory background, the critical structural fact is that the set of all algebraic integers in a number field K forms a **ring**, meaning sums and products of algebraic integers are again algebraic integers. This is not obvious — if α satisfies a degree-m monic integer polynomial and β satisfies a degree-n one, then α + β satisfies some monic integer polynomial of degree mn. The proof uses the fact that the minimal polynomial of α + β divides the characteristic polynomial of a certain matrix over ℤ. The resulting ring, denoted 𝒪_K, is called the **ring of integers** of K and is the fundamental object of algebraic number theory.

The two most important examples show you how different this can look in practice. In ℚ(i), the ring of integers is ℤ[i] = {a + bi : a, b ∈ ℤ}, the Gaussian integers — because i satisfies x² + 1 = 0. In ℚ(√−3), the ring of integers is not just ℤ[√−3] but the larger ring ℤ[ω] where ω = (−1 + √−3)/2 is a primitive cube root of unity satisfying x² + x + 1 = 0. This is the ring of Eisenstein integers. The fact that ω, not just √−3, is the "integer" here is initially surprising, but ω satisfies a monic integer polynomial and (−1 + √−3)/2 is indeed not a "half-integer" in the relevant sense — it lives naturally inside 𝒪_K.

Understanding algebraic integers is the entry point to understanding factorization in number fields. Just as ℤ has unique factorization into primes, one asks whether 𝒪_K does too. Sometimes it does (as in ℤ[i]) and sometimes it does not — and the failure of unique factorization is measured by the **ideal class group**, a central object in algebraic number theory. The concepts you have built here — monic polynomials, rings of integers, specific examples like ℤ[i] — are the concrete foundation for all of that deeper theory.
