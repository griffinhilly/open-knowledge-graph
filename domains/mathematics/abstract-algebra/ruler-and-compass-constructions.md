---
id: ruler-and-compass-constructions
title: Ruler and Compass Constructions
domain: mathematics
course: abstract-algebra
prerequisites:
- id: field-extensions
  type: hard
- id: galois-groups
  type: soft
tags:
- constructions
- compass
- ruler
- quadratic-extensions
stage: advanced
status: validated
---

# Ruler and Compass Constructions

## Core Idea
A length is constructible with ruler and compass iff it lies in a field extension Q(α₁, ..., αₙ) where each [Q(α₁, ..., αᵢ) : Q(α₁, ..., αᵢ₋₁)] = 2. This proves angle trisection and cube doubling are impossible: they require non-power-of-2 degree extensions. The theory uses Galois extensions of degree 2^k.

## Questions

```yaml
- question: "A student claims to have found a ruler-and-compass construction that trisects a 60° angle, achieved through an unusually long sequence of steps. Why must this claim be false?"
  type: multiple-choice
  options:
    - "Trisecting any angle requires at least one step that cannot be performed with a compass"
    - "cos(20°) has degree 3 over ℚ, and no tower of degree-2 extensions can reach a number of odd degree"
    - "The construction would require more precision than any physical compass can provide"
    - "Angle trisection was proven impossible by exhaustive computational search"
  answer: 1
  explanation: "Trisecting 60° requires constructing cos(20°), which is a root of the irreducible polynomial 8x³ - 6x - 1 over ℚ. This means [ℚ(cos 20°) : ℚ] = 3. Since every ruler-and-compass step adds at most a degree-2 extension, the degree of any constructible number over ℚ must be a power of 2. Since 3 is not a power of 2, no sequence of ruler-and-compass steps — however long or clever — can construct cos(20°). The impossibility is algebraic, not practical."

- question: "Squaring the circle (constructing a line segment of length √π from a unit segment) is impossible for a fundamentally different reason than doubling the cube. What is that reason?"
  type: multiple-choice
  options:
    - "π is irrational, while ∛2 is rational, so the degree argument applies differently"
    - "π is transcendental — it satisfies no polynomial over ℚ — so it lies outside the entire algebraic hierarchy, not merely in a wrong-degree extension"
    - "The circle has infinite area, making it geometrically incomparable to a square"
    - "√π has degree 4 over ℚ, which is a power of 2 but still not constructible"
  answer: 1
  explanation: "Doubling the cube fails because ∛2 is algebraic of degree 3 — it's inside the algebraic hierarchy but in the wrong-degree extension. Squaring the circle fails for a deeper reason: π is transcendental, meaning it satisfies no polynomial equation with rational coefficients at all. It cannot even be reached by any algebraic extension of ℚ, making the degree argument irrelevant. The impossibility is of a completely different kind."

- question: "Each ruler-and-compass step corresponds algebraically to solving at most a quadratic equation, which is why the degree of any constructible number over ℚ must be a power of 2."
  type: true-false
  answer: true
  explanation: "True. Drawing a line between two points or finding intersections solves linear equations (degree 1, staying in the same field). Finding circle-circle or line-circle intersections solves quadratic equations, adjoining a square root and creating a degree-2 extension. By the tower law, a chain of n such steps produces [Fₙ : ℚ] = 2ⁿ. Since every constructible number lives in such a tower, its degree over ℚ divides some power of 2 — and if it is a minimal polynomial, its degree must be a power of 2."

- question: "If [ℚ(α) : ℚ] = 4, then α is constructible by ruler and compass."
  type: true-false
  answer: false
  explanation: "False. Degree being a power of 2 is necessary but not sufficient for constructibility. The number must lie in a tower of degree-2 extensions Q ⊂ F₁ ⊂ ... ⊂ Fₙ where each step has degree 2. An element of degree 4 over ℚ could lie in an extension that is a degree-4 extension not decomposable into two quadratic steps. Constructibility requires the correct tower structure, not merely the correct degree."

- question: "Explain why the impossibility of doubling the cube is not a matter of insufficient geometric ingenuity but of algebraic necessity."
  type: short-answer
  answer: "Doubling the cube requires constructing ∛2, which has degree 3 over ℚ. Every ruler-and-compass step can only adjoin a square root, creating a degree-2 extension. Any tower of such steps produces a field of degree 2ⁿ over ℚ. Since 3 does not divide any power of 2, ∛2 cannot live in any such tower — no matter how many steps are used."
  explanation: "The key shift is from geometry to algebra: ruler-and-compass operations are exactly the operations that produce towers of quadratic extensions. The algebraic constraint on degrees is absolute. A more creative sequence of steps doesn't help because every step is still a linear or quadratic equation. The impossibility proof converts an ancient geometric question into an algebra problem that has a clean answer."
```

## Explainer

You know from field extensions that adjoining an element α to a field F creates a new field F(α), and the degree [F(α) : F] measures how many dimensions the extension adds. The key connection here is geometric: every ruler-and-compass step — drawing a line between two points, drawing a circle centered at one point and passing through another, finding their intersections — corresponds algebraically to solving a linear or quadratic equation. Linear equations keep you in the same field; quadratic equations adjoin a square root, adding a degree-2 extension. This means each construction step can at most double the degree of the field over ℚ.

The **constructibility criterion** follows: a length is constructible if and only if it lives in a field you can reach by a tower of quadratic extensions, Q ⊂ F₁ ⊂ F₂ ⊂ ... ⊂ Fₙ, where each step has degree 2. By the tower law you already know, [Fₙ : Q] = 2ⁿ for some n. So any constructible number has degree over ℚ equal to a power of 2. This is the gatekeeper: if a number requires a field extension whose degree is *not* a power of 2, it cannot be constructed.

Now the famous impossibility results fall out cleanly. **Doubling the cube** means constructing ∛2 — a root of x³ - 2, which is irreducible over ℚ. The degree [Q(∛2) : Q] = 3, which is not a power of 2. Impossible. **Trisecting a 60° angle** means constructing cos(20°), a root of 8x³ - 6x - 1, again irreducible of degree 3. Impossible. The impossibility is not about ingenuity or complexity — no sequence of compass-and-straightedge moves, no matter how clever, can escape the algebraic constraint that each step only adjoins square roots.

**Squaring the circle** (constructing √π) is also impossible, but for a deeper reason: π is transcendental, meaning it satisfies no polynomial with rational coefficients at all. It is not merely in a "wrong-degree" extension — it is outside the entire algebraic hierarchy. Contrast this with regular polygons: a regular n-gon is constructible if and only if n = 2^k · p₁ · p₂ · ... · pₘ where each pᵢ is a distinct **Fermat prime** (primes of the form 2^(2^k) + 1). Gauss proved this at age 19 by showing constructibility of a regular n-gon is equivalent to the Galois group of the n-th cyclotomic field being a 2-group. The field extension framework transforms ancient geometric puzzles into questions you can answer with algebra.
