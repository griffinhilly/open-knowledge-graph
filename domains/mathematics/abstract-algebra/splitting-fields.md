---
id: splitting-fields
title: Splitting Fields
domain: mathematics
course: abstract-algebra
prerequisites:
- id: algebraic-transcendental-elements
  type: hard
builds-toward:
- galois-groups
- finite-fields
tags:
- splitting-field
- root
- complete-factorization
stage: advanced
status: validated
---

# Splitting Fields

## Core Idea
A splitting field of a polynomial f(x) ∈ F[x] is the smallest field extension of F in which f splits into linear factors. Splitting fields exist and are unique up to isomorphism.

## Questions

```yaml
- question: "What is the splitting field of f(x) = x⁴ − 5 over ℚ?"
  type: multiple-choice
  options:
    - "ℚ(⁴√5), since it contains one real root of f"
    - "ℚ(⁴√5, i), since all four roots are ±⁴√5 and ±i·⁴√5, requiring both ⁴√5 and i"
    - "ℂ, because all polynomials ultimately split over ℂ"
    - "ℚ(√5), since f factors as (x²−√5)(x²+√5) over that extension"
  answer: 1
  explanation: "The four roots of x⁴ − 5 are ⁴√5, −⁴√5, i·⁴√5, and −i·⁴√5. Adjoining ⁴√5 to ℚ gives the real roots but not the complex ones. You also need i to get i·⁴√5 and −i·⁴√5. So the splitting field is ℚ(⁴√5, i) — the smallest field containing all four roots. Option A is wrong because ℚ(⁴√5) ⊂ ℝ cannot contain i·⁴√5. Option C is too large: ℂ is not the *smallest* field where f splits. Option D gives ℚ(√5), which is degree 2 over ℚ and does not contain ⁴√5."

- question: "Two students construct the splitting field of f(x) = x³ − 2 over ℚ by adjoining roots in different orders. Student A adjoins ∛2 first, then ω (a primitive cube root of unity). Student B adjoins ω first, then ∛2. Why must their resulting fields be the same?"
  type: multiple-choice
  options:
    - "Because ℚ(∛2, ω) = ℚ(ω, ∛2) trivially as sets"
    - "Because the splitting field is unique up to isomorphism: any two splitting fields of f over F are isomorphic by a map fixing F"
    - "Because all finite extensions of ℚ of the same degree are isomorphic"
    - "Because the order of adjunction does not matter for polynomials of degree 3 specifically"
  answer: 1
  explanation: "The uniqueness up to isomorphism is not just set-equality (though in this case the fields happen to literally be equal). The deeper point is that no matter how you construct a splitting field — which root you adjoin first, which tower you climb — you always arrive at a field that is isomorphic to any other splitting field of f over F by an isomorphism fixing F. This makes the splitting field a canonical, well-defined object, not an artifact of construction. This uniqueness is what allows the Galois group to be defined: you need the splitting field to be canonical before you can count its automorphisms."

- question: "Adjoining one root of x² − 2 to ℚ automatically provides the other root as well, since −√2 is already in ℚ(√2)."
  type: true-false
  answer: true
  explanation: "ℚ(√2) = {a + b√2 : a, b ∈ ℚ}. The other root of x² − 2 is −√2 = 0 + (−1)·√2, which is clearly in this set with a = 0, b = −1. So the splitting field of x² − 2 over ℚ is just ℚ(√2), a degree-2 extension. This does not always happen: for x³ − 2 over ℚ, adjoining ∛2 does not give the complex cube roots, so a further extension is required."

- question: "The degree of the splitting field of a degree-n polynomial over F always equals n! (n factorial)."
  type: true-false
  answer: false
  explanation: "The degree of the splitting field *divides* n!, but it is often much smaller. The factorial bound arises because the first root creates an extension of degree at most n, the second at most n−1, and so on. But when roots are algebraically related — for instance, when adjoining one root gives you others for free — the actual degree is smaller. For x² − 2, the splitting field has degree 2 over ℚ, not 2! = 2 (coincidentally equal here), but for x⁴ − 1 the splitting field has degree 2 over ℚ even though 4! = 24."

- question: "What does 'smallest' mean in the definition of a splitting field, and why is this minimality condition important?"
  type: short-answer
  answer: "The splitting field of f over F is the smallest field extension of F containing all roots of f — meaning it is contained in every other field extension of F in which f splits completely. Minimality means you adjoin exactly what is needed (the roots of f) and nothing extra. The condition matters because without it 'a splitting field' would be non-unique: any field containing a splitting field would also qualify. With minimality, the splitting field is the canonical choice, uniquely determined up to isomorphism, and the right object for defining the Galois group as its automorphism group over F."
  explanation: "ℂ contains all roots of every polynomial over ℚ, but ℂ is not the splitting field of x² − 2: ℚ(√2) is much smaller and still splits f. Minimality pins down which extension we care about. The uniqueness up to isomorphism then ensures that even though we could in principle choose different embeddings, the resulting structure is always 'the same' in the relevant sense."
```

## Explainer

You've already worked with algebraic and transcendental elements, so you know that adjoining a root α of an irreducible polynomial p(x) to a field F produces the extension F(α). A **splitting field** is the result of doing this repeatedly — adjoining every root until the polynomial completely factors into linear pieces.

Start with a concrete case. Over ℚ, the polynomial f(x) = x² − 2 doesn't split: it has no rational roots. But ℚ(√2) = {a + b√2 : a, b ∈ ℚ} is the smallest extension where f factors as (x − √2)(x + √2). Notice that adjoining one root automatically provided the other, because −√2 = −(√2) is already in ℚ(√2). That's the splitting field: ℚ(√2). For x² + 1 over ℝ, the splitting field is ℂ = ℝ(i), since x² + 1 = (x − i)(x + i) and both roots land in ℂ.

For a degree-n polynomial, you might need to adjoin up to n roots. Each adjunction creates a tower of extensions: F ⊆ F(α₁) ⊆ F(α₁, α₂) ⊆ · · · ⊆ F(α₁, …, αₙ). The degree of the splitting field over F divides n! — the factorial bound arises because the first root creates an extension of degree at most n, the second of degree at most n−1, and so on. In practice the degree is often much smaller if roots are algebraically related, as in the x² − 2 example above.

The **uniqueness up to isomorphism** is what makes splitting fields a well-defined concept rather than an artifact of construction order. Two different towers of root adjunctions may look different, but they produce fields that are structurally identical — any two splitting fields of f over F are isomorphic by a map fixing F. This uniqueness is the foundation for defining Galois groups: once you know the splitting field is a canonical object, you can meaningfully ask how many automorphisms it has, and that count gives you the Galois group.
