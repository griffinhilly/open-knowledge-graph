---
id: algebraic-and-transcendental-elements
title: Algebraic and Transcendental Elements
domain: mathematics
course: abstract-algebra
prerequisites:
- id: field-extensions
  type: hard
builds-toward:
- splitting-fields
- galois-groups
tags:
- algebraic
- transcendental
- minimal-polynomial
stage: advanced
status: draft
---

# Algebraic and Transcendental Elements

## Core Idea
An element α in F is algebraic over K if it satisfies a polynomial equation with coefficients in K; otherwise it is transcendental. For algebraic α, the minimal polynomial is the monic polynomial of smallest degree with α as root. The degree of α equals the degree of its minimal polynomial.

## Questions

```yaml
- question: "Consider α = ∛5 (the real cube root of 5). Over ℚ, which of the following is the minimal polynomial of α, and what is [ℚ(α):ℚ]?"
  type: multiple-choice
  options:
    - "x³ − 5 (degree 3), so [ℚ(α):ℚ] = 3"
    - "x − ∛5 (degree 1), because α is a single specific number"
    - "x⁶ − 25 (degree 6), obtained by eliminating the cube root algebraically"
    - "There is no minimal polynomial because ∛5 is irrational"
  answer: 0
  explanation: "The minimal polynomial must lie in ℚ[x] (coefficients in ℚ) and have α as a root. x³ − 5 satisfies this: (∛5)³ − 5 = 0, and it is irreducible over ℚ by Eisenstein's criterion with p = 5. Option B is wrong because x − ∛5 has the irrational number ∛5 as a coefficient — it is not in ℚ[x]. Option D confuses irrational with transcendental: ∛5 is irrational but algebraic over ℚ. The degree of the minimal polynomial is 3, giving [ℚ(∛5):ℚ] = 3, meaning ℚ(∛5) is a 3-dimensional ℚ-vector space with basis {1, ∛5, ∛25}."

- question: "A student argues: 'The minimal polynomial of π over ℚ must exist — just compute it from the decimal expansion.' What is the correct response?"
  type: multiple-choice
  options:
    - "The student is right — every real number satisfies some polynomial over ℚ with high enough degree"
    - "π is transcendental over ℚ: Lindemann proved in 1882 that no nonzero polynomial with rational coefficients has π as a root, so no minimal polynomial exists"
    - "π is irrational, and all irrational numbers are transcendental, so no minimal polynomial exists"
    - "The minimal polynomial exists but has infinite degree, which is why it cannot be written down"
  answer: 1
  explanation: "Transcendental over ℚ means exactly that no nonzero polynomial in ℚ[x] vanishes at that element — a fact Lindemann proved in 1882 for π. The decimal expansion is irrelevant: what matters is whether any finite polynomial equation with rational coefficients is satisfied. Option C is wrong: being irrational does not imply transcendental. √2 is irrational but algebraic (satisfies x² − 2 = 0). Transcendence is a stronger, harder-to-prove condition that requires ruling out infinitely many polynomial equations simultaneously."

- question: "The minimal polynomial of an algebraic element α over K must be irreducible over K."
  type: true-false
  answer: true
  explanation: "If the minimal polynomial factored as p(x) = q(x)r(x) over K with both factors having strictly smaller degree, then p(α) = 0 implies q(α) = 0 or r(α) = 0. Either factor would be a polynomial in K[x] of smaller degree having α as a root, contradicting the minimality of p. Irreducibility is therefore not an additional assumption — it follows directly from the definition of the minimal polynomial as the lowest-degree polynomial in K[x] that vanishes at α."

- question: "If the minimal polynomial of α over K has degree 3, then [K(α):K] = 9, because the extension contains elements up to degree 3 in both α and α²."
  type: true-false
  answer: false
  explanation: "[K(α):K] equals the degree of the minimal polynomial — here 3, not 9. K(α) has K-basis {1, α, α²} as a vector space (dimension 3). The element α³ can be expressed in terms of {1, α, α²} using the minimal polynomial relation, so no higher powers of α are needed as independent basis elements. There is no squaring of the degree: [K(α):K] = deg(min_K(α)) is a direct equality, and this dimension is exactly the minimum number of K-linear directions needed to describe the extension."

- question: "What does it mean to say the degree of the minimal polynomial measures 'how far' α is from K algebraically? Give a concrete example illustrating two different degrees."
  type: short-answer
  answer: "The degree [K(α):K] = deg(min_K(α)) is the dimension of K(α) as a K-vector space — the minimum number of K-linearly independent basis elements needed to reach α from K. A degree-1 minimal polynomial means α ∈ K (no extension). A degree-2 polynomial (e.g., x² − 2 for √2 over ℚ) gives a 2-dimensional extension with basis {1, √2}, so every element of ℚ(√2) looks like a + b√2. A degree-3 polynomial (e.g., x³ − 5 for ∛5 over ℚ) gives a 3-dimensional extension {1, ∛5, ∛25}. Higher degree means more algebraically 'remote' from K."
  explanation: "The degree is the key invariant that carries through into Galois theory and splitting fields: it measures the 'algebraic complexity' of α relative to K with a single integer. Two algebraic elements with the same minimal polynomial degree are, in a precise sense, equidistant from K, even if they look very different."
```

## Explainer

From your study of field extensions, you know that given a base field K and a larger field F, every element α ∈ F sits in some relationship with K. The fundamental question is: does α "live inside" the polynomial world of K, or does it escape it entirely? This is exactly the distinction between **algebraic** and **transcendental** elements.

An element α ∈ F is **algebraic over K** if there exists a nonzero polynomial p(x) ∈ K[x] such that p(α) = 0. In plain terms, you can express α as a root of some polynomial whose coefficients you can write down using elements of K alone. The classic example: √2 is algebraic over ℚ because it satisfies x² − 2 = 0, a polynomial with rational coefficients. Similarly, i = √(−1) satisfies x² + 1 = 0 over ℚ. The cube root of 5 satisfies x³ − 5 = 0. All of these elements, while not in ℚ themselves, are "reachable" from ℚ via polynomial equations.

An element is **transcendental over K** if no such polynomial exists — no polynomial with K-coefficients has it as a root. The numbers π and e are transcendental over ℚ, but proving this requires deep analysis (Hermite proved it for e in 1873, Lindemann for π in 1882). Transcendental elements are in a precise sense "algebraically invisible" to K: you cannot pin them down with any finite polynomial relationship over the base field.

For an algebraic element α, the **minimal polynomial** min_K(α) is the unique monic polynomial of smallest degree in K[x] that has α as a root. "Monic" means the leading coefficient is 1. The minimal polynomial is always irreducible over K — if it factored into two lower-degree polynomials over K, one of them would also vanish at α, contradicting minimality. Its degree, [K(α):K], is called the **degree of α** over K, and it equals the dimension of K(α) as a K-vector space. For √2, the minimal polynomial over ℚ is x² − 2 (degree 2), so [ℚ(√2):ℚ] = 2. For a primitive cube root of unity ω satisfying ω² + ω + 1 = 0, the minimal polynomial over ℚ has degree 2, so [ℚ(ω):ℚ] = 2. The degree of the minimal polynomial is the precise measure of "how far" α is from K in the algebraic sense — it tells you the minimum number of K-linear dimensions needed to describe the extension K(α). This will be the key invariant in Galois theory and the study of splitting fields.
