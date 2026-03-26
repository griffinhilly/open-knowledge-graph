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
status: validated
---

# Irreducibility Criteria

## Core Idea
A polynomial is irreducible if it cannot be factored into non-constant polynomials. Eisenstein's criterion provides a sufficient condition for irreducibility over fields and principal ideal domains.

## Questions

```yaml
- question: "A student applies Eisenstein's criterion to f(x) = x³ + x + 1, trying every prime, and finds no prime works. They conclude f(x) must be reducible over ℚ. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student should have applied Eisenstein over ℂ rather than ℚ"
    - "Eisenstein's criterion is a sufficient condition only — failing every prime's test means Eisenstein cannot be used, but the polynomial may still be irreducible, provable by other methods"
    - "For cubics, Eisenstein is the only valid irreducibility test, so failing it proves reducibility"
    - "The student should have tried substitution before giving up, and the substitution will always produce an Eisenstein polynomial"
  answer: 1
  explanation: "Eisenstein provides a sufficient condition for irreducibility — when it applies, irreducibility is guaranteed. But it is not necessary: many irreducible polynomials fail every prime's test. For f(x) = x³ + x + 1, the rational root theorem shows its only possible rational roots are ±1, and neither satisfies f(x) = 0. Since it's a cubic with no rational roots, it must be irreducible over ℚ (a cubic factors over ℚ if and only if it has a rational root). Eisenstein failed; the polynomial is irreducible anyway."

- question: "The polynomial x^p − 1 is not directly Eisenstein, but substituting x → x+1 yields a polynomial that Eisenstein's criterion applies to. What does this demonstrate?"
  type: multiple-choice
  options:
    - "Eisenstein's criterion can be applied directly to any polynomial after a change of variables"
    - "Substitution before applying Eisenstein can reveal irreducibility that is invisible in the original form, by transforming the polynomial into one with the required divisibility structure"
    - "The substitution proves that x^p − 1 and (x+1)^p − 1 are the same polynomial up to a unit"
    - "Irreducibility is not preserved under variable substitution, so the result applies to the substituted polynomial only"
  answer: 1
  explanation: "Irreducibility is preserved under substitution by a unit — replacing x with x+1 gives a polynomial over ℚ, and f(x) irreducible iff f(x+1) irreducible. When x+1 is substituted into x^p − 1, expanding by the binomial theorem yields (x+1)^p − 1. The binomial coefficients C(p,k) for 0 < k < p are all divisible by p, and the constant term (after dividing by x) is p — not divisible by p². Eisenstein applies with prime p, proving (x^p−1)/(x−1) = Φ_p(x) is irreducible. The substitution trick extends Eisenstein's reach to polynomials whose original form hides the required structure."

- question: "A polynomial that is irreducible over ℚ may factor completely into linear factors over ℂ — irreducibility is always relative to a specific coefficient ring or field."
  type: true-false
  answer: true
  explanation: "Irreducibility is not an absolute property of a polynomial but a relational one: it depends on the ring or field you're working over. x² + 1 is irreducible over ℝ (no real roots) but factors as (x+i)(x−i) over ℂ. x² − 2 is irreducible over ℚ but factors over ℝ as (x−√2)(x+√2). By the fundamental theorem of algebra, every non-constant polynomial over ℂ splits into linear factors — so every polynomial of degree ≥ 2 is reducible over ℂ. Specifying the field is essential when claiming a polynomial is irreducible."

- question: "If Eisenstein's criterion applies to a polynomial f(x), then f(x) is irreducible over most field."
  type: true-false
  answer: false
  explanation: "Eisenstein proves irreducibility over ℚ (or more generally over the fraction field of a UFD). It says nothing about irreducibility over other fields. For example, f(x) = x² − 2 is Eisenstein with p = 2 (wait — actually let me think: 2 divides -2 and not the leading coeff, and 4 does not divide -2). Actually x² − 2 is Eisenstein with prime 2. It's irreducible over ℚ. But over ℝ it factors as (x − √2)(x + √2). Eisenstein establishes irreducibility over ℚ specifically; the polynomial may or may not be irreducible over other fields. Every polynomial of degree ≥ 2 factors completely over ℂ."

- question: "Describe two methods for testing polynomial irreducibility over ℚ when Eisenstein's criterion cannot be directly applied, and explain why no single test suffices for all polynomials."
  type: short-answer
  answer: "Two methods: (1) Rational Root Theorem — if f has degree n with integer coefficients, the only possible rational roots are p/q where p divides the constant term and q divides the leading coefficient. If none of these candidates are roots, a degree-3 polynomial must be irreducible (a cubic factors over ℚ iff it has a rational root). (2) Reduction mod p — if f reduces to an irreducible polynomial mod some prime p (and the degree is preserved), then f is irreducible over ℚ by Gauss's lemma. No single test suffices because each has gaps: Eisenstein requires a prime with the right divisibility structure; rational roots only helps for cubics and quartics directly; reduction mod p requires finding a prime where the reduced polynomial happens to be irreducible."
  explanation: "The toolkit approach reflects the nature of irreducibility: there is no universal algorithm that works for all polynomials with bounded complexity. Each method succeeds for different structural reasons. Together they cover a wide range, and in practice, trying methods in order — Eisenstein, rational root theorem, mod-p reduction — handles most polynomials encountered in field extension constructions. The substitution technique (x → x+a for various a) further extends the reach of Eisenstein without adding a fundamentally new principle."
```

## Explainer

From your work on polynomial rings, you know that polynomials can be factored much like integers — and just as a prime integer resists factorization, an **irreducible polynomial** cannot be written as a product of two non-constant polynomials of lower degree. Over ℚ, this is a richer question than it might seem: a polynomial could be irreducible over ℚ yet factor completely over ℝ or ℂ. Irreducibility is always relative to the coefficient ring or field you're working in.

The most practical tool for detecting irreducibility over ℚ is **Eisenstein's criterion**. It says: if you can find a prime p such that p divides every coefficient except the leading one, and p² does not divide the constant term, then the polynomial is irreducible over ℚ. For example, take f(x) = x⁴ + 6x³ + 12x² + 18x + 6. The prime p = 3 divides 6, 12, 18, and 6 (all non-leading coefficients), does not divide the leading coefficient 1, and 9 does not divide 6. Eisenstein applies: f is irreducible over ℚ.

An important technique is **substitution before applying Eisenstein**. The polynomial x^p − 1 is not directly Eisenstein, but substituting x → x + 1 gives (x+1)^p − 1, which after expanding has Eisenstein structure with the prime p. This proves the cyclotomic polynomial Φ_p(x) = (x^p − 1)/(x − 1) is irreducible — a non-obvious fact that substitution makes transparent.

Eisenstein is only a sufficient condition, not necessary — many irreducible polynomials fail every prime's test. When Eisenstein doesn't apply, other methods come into play: the **rational root theorem** (if f has a rational root, it factors as a linear times a lower-degree polynomial), reduction mod p (if f is irreducible mod p for some prime p, then f is irreducible over ℚ, by Gauss's lemma), or degree arguments (a cubic with no rational roots must be irreducible over ℚ). Together these criteria form a toolkit for proving that specific polynomials — like the minimal polynomials of algebraic numbers — cannot be factored, which is the foundation for building field extensions.
