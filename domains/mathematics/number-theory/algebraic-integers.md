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
stage: advanced
status: draft
---

# Algebraic Integers

## Core Idea
An algebraic integer is a complex root of a monic integer polynomial. Algebraic integers in a number field K form a ring, generalizing ℤ. Gaussian integers ℤ[i] and Eisenstein integers ℤ[ω] exemplify this structure.

## Explainer

You already know that ℤ sits inside ℚ as a distinguished subring — the integers are special among rationals because they have no denominator. When you studied field extensions, you learned to build bigger fields like ℚ(√2) or ℚ(i) by adjoining roots of polynomials. The natural next question is: what plays the role of ℤ inside these larger fields? The answer is the **ring of algebraic integers**, and the key criterion is surprisingly simple: a number is an algebraic integer if it satisfies a monic polynomial with integer coefficients.

The word "monic" is what distinguishes algebraic integers from algebraic numbers more broadly. The number √2 is an algebraic integer because it satisfies x² − 2 = 0, which is monic (leading coefficient 1) with integer coefficients. The number 1/2 is an algebraic number (it satisfies 2x − 1 = 0) but not an algebraic integer — you cannot write a monic integer polynomial with 1/2 as a root. The rational algebraic integers are exactly ℤ itself, which gives you the right intuition: "algebraic integer" really is a generalization of "ordinary integer."

From your ring theory background, the critical structural fact is that the set of all algebraic integers in a number field K forms a **ring**, meaning sums and products of algebraic integers are again algebraic integers. This is not obvious — if α satisfies a degree-m monic integer polynomial and β satisfies a degree-n one, then α + β satisfies some monic integer polynomial of degree mn. The proof uses the fact that the minimal polynomial of α + β divides the characteristic polynomial of a certain matrix over ℤ. The resulting ring, denoted 𝒪_K, is called the **ring of integers** of K and is the fundamental object of algebraic number theory.

The two most important examples show you how different this can look in practice. In ℚ(i), the ring of integers is ℤ[i] = {a + bi : a, b ∈ ℤ}, the Gaussian integers — because i satisfies x² + 1 = 0. In ℚ(√−3), the ring of integers is not just ℤ[√−3] but the larger ring ℤ[ω] where ω = (−1 + √−3)/2 is a primitive cube root of unity satisfying x² + x + 1 = 0. This is the ring of Eisenstein integers. The fact that ω, not just √−3, is the "integer" here is initially surprising, but ω satisfies a monic integer polynomial and (−1 + √−3)/2 is indeed not a "half-integer" in the relevant sense — it lives naturally inside 𝒪_K.

Understanding algebraic integers is the entry point to understanding factorization in number fields. Just as ℤ has unique factorization into primes, one asks whether 𝒪_K does too. Sometimes it does (as in ℤ[i]) and sometimes it does not — and the failure of unique factorization is measured by the **ideal class group**, a central object in algebraic number theory. The concepts you have built here — monic polynomials, rings of integers, specific examples like ℤ[i] — are the concrete foundation for all of that deeper theory.
