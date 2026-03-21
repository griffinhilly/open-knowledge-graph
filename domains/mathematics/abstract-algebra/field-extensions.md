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

## Questions

```yaml
- question: "You want to adjoin both √2 and √3 to the rationals, forming Q(√2, √3). You know [Q(√2) : Q] = 2 and [Q(√2, √3) : Q(√2)] = 2 (since √3 ∉ Q(√2)). What is [Q(√2, √3) : Q]?"
  type: multiple-choice
  options:
    - "2 — because you only added two irrational numbers to Q"
    - "3 — because the tower has three fields: Q, Q(√2), and Q(√2, √3)"
    - "4 — by the multiplicative property: [K:E]·[E:F] = 2·2 = 4"
    - "6 — because the degrees of the individual extensions add: 2 + 2 + 2"
  answer: 2
  explanation: "The tower law (multiplicative property) says [K : F] = [K : E] · [E : F] for a chain F ⊆ E ⊆ K. Here [Q(√2,√3) : Q(√2)] = 2 and [Q(√2) : Q] = 2, so [Q(√2,√3) : Q] = 2 · 2 = 4. Option B confuses the number of fields in the tower with the degree. Option D confuses multiplication with addition — degrees multiply, not add."

- question: "If [K : F] = 7, what can you conclude about intermediate fields E with F ⊊ E ⊊ K?"
  type: multiple-choice
  options:
    - "There is exactly one intermediate field, since 7 = 1 + 6"
    - "There are no intermediate fields — the multiplicative property forces [K:E]·[E:F] = 7, but 7 is prime, so neither factor can be between 1 and 7"
    - "There are at most 7 intermediate fields, one for each divisor of [K:F]"
    - "We cannot conclude anything without knowing which fields K and F are"
  answer: 1
  explanation: "By the tower law, [K:E]·[E:F] = [K:F] = 7. Since 7 is prime, the only factorizations are 1×7 and 7×1. The factor 1 would mean E = F or E = K — not a proper intermediate field. So there is no intermediate field strictly between F and K. This is a powerful consequence: prime degree forces a 'gap' in the lattice of subfields."

- question: "If F ⊆ E ⊆ K with [K : E] = 3 and [E : F] = 4, then [K : F] = 7."
  type: true-false
  answer: false
  explanation: "The tower law says [K : F] = [K : E] · [E : F] = 3 · 4 = 12, not 7. Adding the degrees is a common error. The multiplicative property uses multiplication because a basis for K over F is constructed by combining a basis for E/F (4 elements) with a basis for K/E (3 elements), giving 4 × 3 = 12 basis elements in total."

- question: "Every element of Q(√2) can be written uniquely as a + b√2 where a, b ∈ Q."
  type: true-false
  answer: true
  explanation: "The set {1, √2} is a basis for Q(√2) as a vector space over Q. This means every element has a unique representation as a linear combination a·1 + b·√2 with rational coefficients a and b. Uniqueness follows from the fact that {1, √2} is linearly independent over Q (if a + b√2 = 0 with a, b ∈ Q and b ≠ 0, then √2 = −a/b would be rational, a contradiction). The degree [Q(√2) : Q] = 2 is precisely the size of this basis."

- question: "How does the tower law (multiplicative property) allow mathematicians to prove that certain classical geometric constructions — like trisecting an arbitrary angle — are impossible with compass and straightedge?"
  type: short-answer
  answer: "Compass-and-straightedge constructions correspond to field extensions of degree 2 (each step adjoins a square root). A constructible length must lie in a field of degree that is a power of 2 over Q. Trisecting a general angle requires solving a cubic equation, which would produce an extension of degree 3. By the tower law, any intermediate field in a tower of quadratic extensions has degree that is a power of 2, so a degree-3 extension cannot appear in such a tower. Therefore trisection is impossible — it would require an extension whose degree (3) does not divide any power of 2."
  explanation: "The tower law makes degree arithmetic rigorous: it tells us exactly which degrees are achievable by chaining extensions. Since 3 is not a power of 2, no sequence of square-root constructions can produce an angle trisection. The same argument applies to doubling the cube (requires ∛2, degree 3) and squaring the circle (requires π, which is transcendental and lies in no finite-degree extension of Q)."
```

## Explainer

You already know that a field is a set with addition and multiplication where every nonzero element has an inverse — the rational numbers Q, the reals R, and the complex numbers C are all fields. A **field extension** K/F simply says that F is a subfield sitting inside the larger field K. The slash notation is suggestive: think of K "over" F, the way you might think of a skyscraper built on a foundation. Q ⊆ R ⊆ C is a chain of three field extensions.

The crucial insight is that K is automatically a **vector space over F**. You already know vector spaces from linear algebra: a set with scalar multiplication (by elements of F) and vector addition (using the addition of K). In the extension Q(√2)/Q — the smallest field containing Q and √2 — every element looks like a + b√2 for a, b ∈ Q. The set {1, √2} is a **basis**: any element is a unique linear combination of basis elements with rational scalars. Because this basis has two elements, the **degree** [Q(√2) : Q] = 2. The degree [K : F] is simply the dimension of K as a vector space over F.

The **multiplicative property** (also called the tower law) says that if you have a chain F ⊆ E ⊆ K of three fields, then [K : F] = [K : E] · [E : F]. Think of it like unit conversion: if E has degree 2 over F, and K has degree 3 over E, then K has degree 6 over F, because a basis for K over F is built by combining a basis for E/F with a basis for K/E. Concretely, Q ⊆ Q(√2) ⊆ Q(√2, √3) has degrees 2 and 2, so the big extension has degree at most 4 — and exactly 4 if √3 is not already in Q(√2).

The tower law has a powerful consequence: the degree of any intermediate field must divide [K : F]. If [K : F] = 7 (a prime), there are no intermediate fields at all — just F and K itself. This kind of arithmetic control over intermediate structures is what makes field extensions the right tool for proving impossibility results, like the classical theorem that you cannot trisect an arbitrary angle with compass and straightedge, because that would force the existence of an extension of degree 3 inside an extension whose degree is a power of 2.
