---
id: field-extensions
title: Field Extensions
domain: mathematics
course: abstract-algebra
prerequisites:
- id: field-definition-examples
  type: hard
- id: vector-spaces
  type: hard
builds-toward:
- algebraic-transcendental-elements
- splitting-fields
tags:
- extension
- degree
- vector-space
- multiplicative
stage: advanced
status: draft
---

# Field Extensions

## Core Idea
A field extension K/F is a pair of fields with F ⊆ K. K is a vector space over F, and its dimension is the degree [K : F]. The multiplicative property holds: [K : F] = [K : E][E : F] for intermediate fields E.

## Explainer

You already know that a field is a set with addition and multiplication where every nonzero element has an inverse — the rational numbers Q, the reals R, and the complex numbers C are all fields. A **field extension** K/F simply says that F is a subfield sitting inside the larger field K. The slash notation is suggestive: think of K "over" F, the way you might think of a skyscraper built on a foundation. Q ⊆ R ⊆ C is a chain of three field extensions.

The crucial insight is that K is automatically a **vector space over F**. You already know vector spaces from linear algebra: a set with scalar multiplication (by elements of F) and vector addition (using the addition of K). In the extension Q(√2)/Q — the smallest field containing Q and √2 — every element looks like a + b√2 for a, b ∈ Q. The set {1, √2} is a **basis**: any element is a unique linear combination of basis elements with rational scalars. Because this basis has two elements, the **degree** [Q(√2) : Q] = 2. The degree [K : F] is simply the dimension of K as a vector space over F.

The **multiplicative property** (also called the tower law) says that if you have a chain F ⊆ E ⊆ K of three fields, then [K : F] = [K : E] · [E : F]. Think of it like unit conversion: if E has degree 2 over F, and K has degree 3 over E, then K has degree 6 over F, because a basis for K over F is built by combining a basis for E/F with a basis for K/E. Concretely, Q ⊆ Q(√2) ⊆ Q(√2, √3) has degrees 2 and 2, so the big extension has degree at most 4 — and exactly 4 if √3 is not already in Q(√2).

The tower law has a powerful consequence: the degree of any intermediate field must divide [K : F]. If [K : F] = 7 (a prime), there are no intermediate fields at all — just F and K itself. This kind of arithmetic control over intermediate structures is what makes field extensions the right tool for proving impossibility results, like the classical theorem that you cannot trisect an arbitrary angle with compass and straightedge, because that would force the existence of an extension of degree 3 inside an extension whose degree is a power of 2.
