---
id: irreducibility-criteria
title: Irreducibility Criteria
domain: mathematics
course: abstract-algebra
prerequisites:
- id: polynomial-rings
  type: hard
builds-toward:
- field-extensions
- splitting-fields
tags:
- irreducible
- eisenstein
- content
- primitive
stage: advanced
status: draft
---

# Irreducibility Criteria

## Core Idea
A polynomial is irreducible if it cannot be factored into non-constant polynomials. Eisenstein's criterion provides a sufficient condition for irreducibility over fields and principal ideal domains.

## Explainer

From your work on polynomial rings, you know that polynomials can be factored much like integers — and just as a prime integer resists factorization, an **irreducible polynomial** cannot be written as a product of two non-constant polynomials of lower degree. Over ℚ, this is a richer question than it might seem: a polynomial could be irreducible over ℚ yet factor completely over ℝ or ℂ. Irreducibility is always relative to the coefficient ring or field you're working in.

The most practical tool for detecting irreducibility over ℚ is **Eisenstein's criterion**. It says: if you can find a prime p such that p divides every coefficient except the leading one, and p² does not divide the constant term, then the polynomial is irreducible over ℚ. For example, take f(x) = x⁴ + 6x³ + 12x² + 18x + 6. The prime p = 3 divides 6, 12, 18, and 6 (all non-leading coefficients), does not divide the leading coefficient 1, and 9 does not divide 6. Eisenstein applies: f is irreducible over ℚ.

An important technique is **substitution before applying Eisenstein**. The polynomial x^p − 1 is not directly Eisenstein, but substituting x → x + 1 gives (x+1)^p − 1, which after expanding has Eisenstein structure with the prime p. This proves the cyclotomic polynomial Φ_p(x) = (x^p − 1)/(x − 1) is irreducible — a non-obvious fact that substitution makes transparent.

Eisenstein is only a sufficient condition, not necessary — many irreducible polynomials fail every prime's test. When Eisenstein doesn't apply, other methods come into play: the **rational root theorem** (if f has a rational root, it factors as a linear times a lower-degree polynomial), reduction mod p (if f is irreducible mod p for some prime p, then f is irreducible over ℚ, by Gauss's lemma), or degree arguments (a cubic with no rational roots must be irreducible over ℚ). Together these criteria form a toolkit for proving that specific polynomials — like the minimal polynomials of algebraic numbers — cannot be factored, which is the foundation for building field extensions.
