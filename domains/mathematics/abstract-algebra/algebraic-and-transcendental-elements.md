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

## Explainer

From your study of field extensions, you know that given a base field K and a larger field F, every element α ∈ F sits in some relationship with K. The fundamental question is: does α "live inside" the polynomial world of K, or does it escape it entirely? This is exactly the distinction between **algebraic** and **transcendental** elements.

An element α ∈ F is **algebraic over K** if there exists a nonzero polynomial p(x) ∈ K[x] such that p(α) = 0. In plain terms, you can express α as a root of some polynomial whose coefficients you can write down using elements of K alone. The classic example: √2 is algebraic over ℚ because it satisfies x² − 2 = 0, a polynomial with rational coefficients. Similarly, i = √(−1) satisfies x² + 1 = 0 over ℚ. The cube root of 5 satisfies x³ − 5 = 0. All of these elements, while not in ℚ themselves, are "reachable" from ℚ via polynomial equations.

An element is **transcendental over K** if no such polynomial exists — no polynomial with K-coefficients has it as a root. The numbers π and e are transcendental over ℚ, but proving this requires deep analysis (Hermite proved it for e in 1873, Lindemann for π in 1882). Transcendental elements are in a precise sense "algebraically invisible" to K: you cannot pin them down with any finite polynomial relationship over the base field.

For an algebraic element α, the **minimal polynomial** min_K(α) is the unique monic polynomial of smallest degree in K[x] that has α as a root. "Monic" means the leading coefficient is 1. The minimal polynomial is always irreducible over K — if it factored into two lower-degree polynomials over K, one of them would also vanish at α, contradicting minimality. Its degree, [K(α):K], is called the **degree of α** over K, and it equals the dimension of K(α) as a K-vector space. For √2, the minimal polynomial over ℚ is x² − 2 (degree 2), so [ℚ(√2):ℚ] = 2. For a primitive cube root of unity ω satisfying ω² + ω + 1 = 0, the minimal polynomial over ℚ has degree 2, so [ℚ(ω):ℚ] = 2. The degree of the minimal polynomial is the precise measure of "how far" α is from K in the algebraic sense — it tells you the minimum number of K-linear dimensions needed to describe the extension K(α). This will be the key invariant in Galois theory and the study of splitting fields.
