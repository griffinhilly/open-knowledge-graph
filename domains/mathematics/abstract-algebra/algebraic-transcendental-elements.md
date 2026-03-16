---
id: algebraic-transcendental-elements
title: Algebraic and Transcendental Elements
domain: mathematics
course: abstract-algebra
prerequisites:
- id: field-extensions
  type: hard
builds-toward:
- splitting-fields
tags:
- algebraic
- transcendental
- minimal-polynomial
- algebraic-closure
stage: advanced
status: draft
---

# Algebraic and Transcendental Elements

## Core Idea
An element α of a field extension K/F is algebraic over F if it is a root of a nonzero polynomial with coefficients in F; otherwise it is transcendental. Every algebraic element has a unique minimal polynomial.

## Explainer

You already know what a field extension K/F is: a larger field K containing a base field F. Now you want to understand an individual element α ∈ K in relation to F. The central question is: does α satisfy any polynomial equation with coefficients in F? The answer divides all elements cleanly into two types.

An element α is **algebraic over F** if there exists a nonzero polynomial p(x) ∈ F[x] such that p(α) = 0. For example, √2 is algebraic over ℚ because it satisfies x² − 2 = 0 — a polynomial with rational coefficients. The complex number i is algebraic over ℚ because it satisfies x² + 1 = 0. Among all polynomials in F[x] that vanish at α, there is a unique monic polynomial of smallest degree: the **minimal polynomial** of α over F, often written min_F(α). It is irreducible over F (if it factored, one factor would be a lower-degree polynomial with α as a root, contradicting minimality), and it divides every other polynomial in F[x] that has α as a root.

An element α is **transcendental over F** if no nonzero polynomial in F[x] has α as a root — α evades every algebraic relation you can write over F. The canonical examples are π and e over ℚ: no rational-coefficient polynomial equation is satisfied by either (though proving this is nontrivial). Transcendental elements are, in a precise sense, "free" — they do not collapse under any polynomial constraint, so adjoining a transcendental element to F produces an extension isomorphic to the field of rational functions F(x), not a finite-degree extension.

The structural difference has immediate consequences. If α is algebraic over F with minimal polynomial of degree n, then F(α) — the smallest subfield of K containing both F and α — has degree [F(α):F] = n as a vector space over F, with basis {1, α, α², ..., αⁿ⁻¹}. The minimal polynomial completely determines this extension. If α is transcendental over F, then [F(α):F] is infinite — you need infinitely many basis elements to span the extension. This dichotomy between finite and infinite degree is what makes the algebraic/transcendental distinction so fundamental: algebraic elements generate controlled, finite extensions; transcendental elements generate extensions that behave like function fields.

